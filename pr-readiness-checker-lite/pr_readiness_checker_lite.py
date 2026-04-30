#!/usr/bin/env python3
"""PR Readiness Checker Lite: local-only diff triage for maintainers/freelancers."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

RISK_TERMS = {
    "auth": 12,
    "security": 12,
    "password": 10,
    "token": 10,
    "payment": 10,
    "billing": 10,
    "migration": 8,
    "schema": 8,
    "delete": 6,
}
TEST_TERMS = ("test", "spec", "pytest", "vitest", "jest", "unittest")
DOC_TERMS = ("readme", "docs/", "changelog", ".md")


def read_text(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    return ""


def changed_files(diff: str) -> list[str]:
    files: list[str] = []
    for line in diff.splitlines():
        if line.startswith("diff --git "):
            parts = line.split()
            if len(parts) >= 4:
                files.append(parts[3][2:] if parts[3].startswith("b/") else parts[3])
        elif line.startswith("+++ b/"):
            candidate = line[6:]
            if candidate and candidate != "/dev/null" and candidate not in files:
                files.append(candidate)
    return files


def score_diff(diff: str) -> dict:
    files = changed_files(diff)
    lower = diff.lower()
    added_lines = [line for line in diff.splitlines() if line.startswith("+") and not line.startswith("+++")]
    removed_lines = [line for line in diff.splitlines() if line.startswith("-") and not line.startswith("---")]
    score = 65
    findings: list[str] = []

    if any(term in f.lower() for f in files for term in TEST_TERMS) or any(term in lower for term in TEST_TERMS):
        score += 15
        findings.append("Test signal present: keep/quote the exact command and result in the PR.")
    else:
        score -= 18
        findings.append("No obvious test signal: add a targeted test or document a verified manual check.")

    if any(term in f.lower() for f in files for term in DOC_TERMS):
        score += 6
        findings.append("Documentation/change note present.")
    else:
        findings.append("No docs signal: state why docs are unnecessary or add a short note.")

    risk_hits = {term: weight for term, weight in RISK_TERMS.items() if re.search(rf"\b{re.escape(term)}\b", lower)}
    if risk_hits:
        penalty = min(25, sum(risk_hits.values()))
        score -= penalty
        findings.append("Risk terms found: " + ", ".join(sorted(risk_hits)) + ". Add rollback and reviewer notes.")

    churn = len(added_lines) + len(removed_lines)
    if churn > 250:
        score -= 12
        findings.append(f"Large diff ({churn} changed lines): split or add a reviewer map.")
    elif churn < 80:
        score += 5
        findings.append(f"Small diff ({churn} changed lines): likely reviewable if tests are clear.")

    score = max(0, min(100, score))
    if score >= 80:
        verdict = "ready-with-notes"
    elif score >= 60:
        verdict = "needs-tightening"
    else:
        verdict = "not-ready"
    return {"score": score, "verdict": verdict, "files": files, "findings": findings, "changed_lines": churn}


def render(result: dict) -> str:
    out = [
        "PR Readiness Checker Lite",
        f"Verdict: {result['verdict']} ({result['score']}/100)",
        f"Changed files: {len(result['files'])}; changed lines: {result['changed_lines']}",
        "",
        "Reviewer checklist:",
    ]
    out.extend(f"- {item}" for item in result["findings"])
    out.extend([
        "",
        "Cash-forward service hook:",
        "- If this flags risk, offer a fixed-scope PR cleanup: tests, reviewer map, and merge-ready notes.",
        "- Keep payment/invoice setup on Corey hold until buyer intent is explicit.",
    ])
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description="Score a git diff for PR readiness without network access.")
    parser.add_argument("--diff", required=True, help="Path to a saved git diff text file")
    args = parser.parse_args()
    print(render(score_diff(read_text(args.diff))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
