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


def render_service_template() -> str:
    """Return a paste-safe intake template for converting PR/diff interest into qualified pipeline."""
    return "\n".join([
        "PR Readiness fixed-scope cleanup intake",
        "",
        "Use this only for public or redacted PR/diff review. Do not share credentials, private repo exports, private customer data, secrets, or non-public source.",
        "",
        "Qualified signal: a public PR URL, a redacted saved git diff, or explicit fixed-scope cleanup intent. Do not count stars, views, generic interest, silence, or requests for login/scraping/auto-commenting.",
        "",
        "Paste these inputs:",
        "1. Public PR or repo URL (or say redacted diff only):",
        "2. Saved/redacted git diff or the risky file snippets:",
        "3. Failing CI/test command or reviewer concern:",
        "4. Desired cleanup: tests, reviewer map, split/refactor, docs, or release notes:",
        "5. Paid-pilot interest: free sample only / maybe after sample / yes, fixed-scope cleanup:",
        "",
        "Safety boundaries:",
        "- local text review only; no GitHub login, private repo access, scraping, auto-comments, or guaranteed merge/payment claims;",
        "- payment collection stays on Corey hold until invoice/payment/account/KYC setup is approved after explicit buyer intent.",
    ])


def render_ci_preflight_template() -> str:
    """Return a narrow CI-failure intake template for buyers with a blocked PR."""
    return "\n".join([
        "CI failure preflight for fixed-scope PR cleanup",
        "",
        "Use this when the buyer has a public or redacted PR/diff plus a failing check. Do not request credentials, private repo access, private logs, secrets, or CI dashboard login.",
        "",
        "Qualified signal: a public PR URL or redacted diff AND the exact failing command/log excerpt or reviewer blocker. Do not count stars, views, generic interest, silence, or requests for login/scraping/auto-fixing.",
        "",
        "Paste-ready buyer ask:",
        "1. Public PR URL or redacted diff-only note:",
        "2. Failing command/check name:",
        "3. Redacted failure excerpt (first error + stack/context only):",
        "4. What changed recently in the PR:",
        "5. Desired outcome: reproduce note / minimal patch / test update / reviewer reply draft:",
        "6. Paid-pilot interest after the free preflight: no / maybe / yes fixed-scope cleanup:",
        "",
        "Safe first response if qualified:",
        "- restate the suspected failure class and the smallest reproducible command;",
        "- name one likely fix path and one rollback/risk note;",
        "- offer paid fixed-scope cleanup only after explicit buyer intent; payment/invoice/account/KYC setup remains on Corey hold.",
    ])


def render_reviewer_reply_template() -> str:
    """Return a paste-ready reply that converts qualified PR/CI inputs into a safe cleanup ask."""
    return "\n".join([
        "Reviewer reply template for blocked PR cleanup",
        "",
        "Use this after a buyer provides paste-safe public/redacted PR or diff inputs plus a failing command, log excerpt, or reviewer blocker.",
        "",
        "Paste-ready response:",
        "Thanks — I can review this from the public/redacted material only.",
        "- Failure class: <test failure | type error | lint | reviewer-risk | unclear>",
        "- Smallest repro: <exact command/check name, if supplied>",
        "- Likely fix path: <one small patch/test/docs/reviewer-map action>",
        "- Risk/rollback note: <what could break and how to revert>",
        "",
        "Safe next step: I can send a short cleanup plan from the public PR/diff first. If you want implementation help after that, reply with \"fixed-scope cleanup\" and the exact public/redacted inputs below. Payment/invoice/account/KYC setup stays on Corey hold until explicit paid-pilot intent is present.",
        "",
        "Required inputs before counting as qualified pipeline:",
        "1. Public PR URL or redacted saved diff:",
        "2. Exact failing command/check name:",
        "3. Redacted first error/log excerpt or reviewer comment:",
        "4. Desired outcome: reproduce note / minimal patch / test update / reviewer reply draft:",
        "5. Paid-pilot intent: no / maybe / yes fixed-scope cleanup:",
        "",
        "Do not accept credentials, secrets, private repo exports, CI dashboard login, private logs, scraping, auto-commenting, guaranteed merge/payment claims, or broad consulting without public/redacted PR/diff inputs.",
        "",
        "Signal rule: count only usable public/redacted PR/diff inputs with an exact failing command/log/reviewer blocker, or explicit fixed-scope cleanup intent. Silence, stars, views, generic interest, and unsafe private-data/login asks are no-count.",
    ])


def render_buyer_proof_template() -> str:
    """Return a direct buyer proof path for a no-login blocked-PR sample."""
    return "\n".join([
        "Blocked PR buyer proof path",
        "",
        "Use this when public issues are silent and the next cash-forward move is a narrow no-login proof, not more passive monitoring.",
        "",
        "Paste-ready public ask:",
        "I can do a no-login PR readiness proof from public/redacted material only. Paste a public PR URL or redacted saved diff, the exact failing command/check or reviewer blocker, and the desired outcome: reproduce note, minimal patch, tests, or reviewer reply.",
        "",
        "What the free proof returns:",
        "1. Readiness verdict from the local diff only.",
        "2. Top 3 risk findings.",
        "3. Smallest reproducible command or missing input.",
        "4. One likely fix path.",
        "5. One rollback/reviewer note.",
        "",
        "Qualification rule: count only usable public/redacted PR or diff inputs with an exact failing command/log/reviewer blocker, or explicit fixed-scope cleanup intent. Silence, views, stars, generic interest, and unsafe private-access asks are no-count.",
        "",
        "Safety/payment boundary: no credentials, secrets, private repo exports, private logs, CI dashboard login, scraping, auto-commenting, guaranteed merge claims, payment links, invoices, account setup, or KYC before explicit paid-pilot intent and Corey approval for payment setup.",
    ])


def render_maintainer_triage_template() -> str:
    """Return a maintainer-facing triage offer for permissioned blocked-PR cleanup."""
    return "\n".join([
        "Maintainer blocked-PR triage offer",
        "",
        "Use this as a sharper buyer angle when passive sample-request intake has no qualified replies. It targets maintainers or agency leads with visible PR review/CI backlog and stays public/redacted-only.",
        "",
        "Paste-ready permissioned ask:",
        "I can triage one blocked public PR from public/redacted material only and return a short maintainer handoff: readiness verdict, top blocker, smallest repro/missing input, likely patch/test path, and a reviewer-ready reply. If useful, we can discuss fixed-scope cleanup after that.",
        "",
        "Qualified inputs before counting pipeline:",
        "1. Public PR URL or redacted saved diff:",
        "2. Exact failing command/check name or reviewer blocker:",
        "3. Redacted first error/log excerpt if CI is failing:",
        "4. Desired maintainer outcome: close as stale / request changes / minimal patch / tests / reviewer reply:",
        "5. Paid-pilot intent after the free triage: no / maybe / yes fixed-scope cleanup:",
        "",
        "Free triage output:",
        "- ready / needs-tightening / not-ready verdict;",
        "- one blocker that prevents maintainer action;",
        "- smallest repro or missing input;",
        "- likely patch or test path;",
        "- paste-ready maintainer/reviewer note.",
        "",
        "No-count outcomes: silence, stars, views, generic interest, requests for private repo access, requests to log into CI/GitHub, broad backlog consulting without a public/redacted PR, or guaranteed-merge/payment expectations.",
        "",
        "Safety/payment boundary: no credentials, secrets, private repo exports, private logs, customer data, CI dashboard login, scraping, auto-commenting, guaranteed merge claims, payment links, invoices, account setup, or KYC before explicit paid-pilot intent and Corey approval for payment setup.",
    ])


def main() -> int:
    parser = argparse.ArgumentParser(description="Score a git diff for PR readiness without network access.")
    parser.add_argument("--diff", help="Path to a saved git diff text file")
    parser.add_argument("--service-template", action="store_true", help="Print a paste-safe buyer intake template for PR cleanup requests")
    parser.add_argument("--ci-preflight-template", action="store_true", help="Print a narrower CI-failure buyer intake template")
    parser.add_argument("--reviewer-reply-template", action="store_true", help="Print a paste-ready reply for qualified blocked-PR cleanup inputs")
    parser.add_argument("--buyer-proof-template", action="store_true", help="Print a no-login buyer proof path for blocked PR cleanup")
    parser.add_argument("--maintainer-triage-template", action="store_true", help="Print a maintainer-facing blocked-PR triage offer")
    args = parser.parse_args()
    if args.service_template:
        print(render_service_template())
    elif args.ci_preflight_template:
        print(render_ci_preflight_template())
    elif args.reviewer_reply_template:
        print(render_reviewer_reply_template())
    elif args.buyer_proof_template:
        print(render_buyer_proof_template())
    elif args.maintainer_triage_template:
        print(render_maintainer_triage_template())
    else:
        if not args.diff:
            parser.error("--diff is required unless a template flag is used")
        print(render(score_diff(read_text(args.diff))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
