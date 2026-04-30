#!/usr/bin/env python3
"""Buyer-ready slim Upwork proposal scorer.

Paste a public job post and a draft proposal. Get a local, human-review score
and concrete fixes. No login, scraping, auto-send, or guaranteed-win claims.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

RUBRIC = {
    "job relevance": 25,
    "proof specificity": 20,
    "understanding": 20,
    "risk reversal": 15,
    "clarity/brevity": 10,
    "CTA": 10,
}
PROOF_WORDS = {"built", "shipped", "case", "result", "metric", "%", "$", "client", "portfolio", "example"}
RISK_WORDS = {"milestone", "first", "audit", "sample", "refund", "risk", "pilot", "fixed"}
CTA_WORDS = {"call", "chat", "send", "share", "start", "available", "next", "today", "tomorrow"}
RISKY_PATTERNS = {
    "guaranteed outcome": [
        r"\bguarantee(?:d|s)?\b.*\b(win|wins|job|jobs|hire|hires|roi|revenue|results?)\b",
        r"\b(win|wins|job|jobs|hire|hires|roi|revenue|results?)\b.*\bguarantee(?:d|s)?\b",
    ],
    "platform automation": [
        r"\b(auto|automatically)\b.*\b(send|submit|apply|dm|message)\b",
        r"\b(send|submit|apply|dm|message)\b.*\b(auto|automatically)\b",
    ],
}


def words(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9+#.-]+", text.lower()))


def score(job: str, proposal: str) -> dict:
    jw, pw = words(job), words(proposal)
    overlap = len((jw & pw) - {"the", "and", "for", "with", "you", "your", "that", "this"})
    proof_hits = len(PROOF_WORDS & pw)
    risk_hits = len(RISK_WORDS & pw)
    cta_hits = len(CTA_WORDS & pw)
    length = len(proposal.split())
    risky = [name for name, patterns in RISKY_PATTERNS.items() if any(re.search(p, proposal, re.I | re.S) for p in patterns)]

    subscores = {
        "job relevance": min(25, overlap * 3),
        "proof specificity": min(20, proof_hits * 5),
        "understanding": 20 if overlap >= 6 else 12 if overlap >= 3 else 5,
        "risk reversal": min(15, risk_hits * 5),
        "clarity/brevity": 10 if 80 <= length <= 220 else 7 if 40 <= length < 300 else 4,
        "CTA": min(10, cta_hits * 5),
    }
    total = sum(subscores.values())
    if risky:
        total = max(0, total - 10)
    return {"total": total, "subscores": subscores, "risky": risky, "overlap": overlap, "length": length}


def fixes(result: dict) -> list[str]:
    out = []
    if result["subscores"]["job relevance"] < 18:
        out.append("Mirror 3-5 exact words from the job post in the first two sentences.")
    if result["subscores"]["proof specificity"] < 15:
        out.append("Add one concrete proof point: shipped example, metric, client type, or portfolio sample.")
    if result["subscores"]["risk reversal"] < 10:
        out.append("Offer a fixed-scope first milestone, audit, or sample before a broad engagement.")
    if result["subscores"]["CTA"] < 10:
        out.append("End with one clear next step: ask to review a sample, call, or share project access.")
    if result["risky"]:
        out.append("Replace guaranteed-win or auto-submit language with human-reviewed process language.")
    return out or ["Draft is usable; keep final review human and avoid guaranteed outcomes or auto-send claims."]


def render(job: str, proposal: str, niche: str | None = None) -> str:
    result = score(job, proposal)
    lines = [
        "Upwork Proposal Scorer Slim Report",
        f"Score: {result['total']}/100",
        "Subscores:",
    ]
    for name, max_points in RUBRIC.items():
        lines.append(f"- {name}: {result['subscores'][name]}/{max_points}")
    lines.append("Recommended fixes:")
    for item in fixes(result):
        lines.append(f"- {item}")
    if niche:
        lines.extend([
            f"Niche tweak ({niche}):",
            f"- Add one {niche}-specific constraint, buyer risk, or proof example before sending.",
        ])
    lines.append("Safety boundary: local paste-in tool only; no scraping, login, auto-send, guaranteed wins, payment links, or account setup.")
    return "\n".join(lines)


def intake_template(niche: str | None = None) -> str:
    """Return the exact buyer intake needed before a paid pilot quote."""
    niche_line = f"Preferred niche/rubric: {niche}" if niche else "Preferred niche/rubric: agency / coach / freelancer / other"
    return "\n".join([
        "Buyer intake for one proposal QA sample",
        niche_line,
        "1. Paste one public job post or a redacted job summary.",
        "2. Paste one draft proposal you are comfortable having reviewed locally.",
        "3. Name the buyer type you sell to and the proof you can truthfully cite.",
        "4. Say whether you want only a sample score or a custom $49 rubric pilot.",
        "Safety boundary: do not send login credentials, private client data, payment details, scraping requests, auto-submit requests, or guaranteed-win expectations.",
        "Payment rule: if the buyer asks to pay, pause and route Corey approval before any invoice, payment link, account setup, or KYC path.",
    ])


def reply_template(niche: str | None = None) -> str:
    """Return a paste-ready, non-pushy reply for a qualified intake response."""
    niche_text = niche or "your niche"
    return "\n".join([
        "Qualified intake reply for one proposal QA sample",
        f"Thanks — I can run one {niche_text} proposal sample locally and send back the score, the top 3 fixes, and a short rubric note.",
        "Please send only the public/redacted job post and the draft proposal text you are comfortable sharing.",
        "I will not log in, scrape, auto-submit, message clients, promise wins, or use private client/payment data.",
        "If the sample is useful and you want the custom $49 rubric pilot, I will pause for Corey to approve the payment collection path before any invoice, payment link, account setup, or KYC step.",
        "Signal log: count this only if the buyer sends paste-safe job/proposal text or explicitly asks for the paid pilot.",
    ])


def signal_decision_template(niche: str | None = None) -> str:
    """Return a safe decision log for handling the next buyer response."""
    niche_text = niche or "agency / coach / freelancer"
    return "\n".join([
        "Buyer response signal decision log",
        f"Target niche: {niche_text}",
        "Count as qualified pipeline only if the buyer sends a public/redacted job post plus draft proposal, asks for a one-sample review, or explicitly asks for the $49 custom rubric pilot.",
        "No-count outcomes: likes, views, silence, generic 'interesting', requests for login/scraping/auto-submit, private client data, or guaranteed-win expectations.",
        "Autonomous next action when qualified sample inputs arrive: run the scorer locally, send the score/top 3 fixes, and log the response; do not request payment first.",
        "Corey hold when paid intent appears: pause before invoice, payment link, payment account setup, KYC, subscription, or billing change.",
        "Kill/replace rule: after 5 no-count outcomes, stop this freelancer-proposal angle and pivot the same scorer into an agency proposal QA checklist or coach review-copy sample.",
    ])


def main() -> None:
    parser = argparse.ArgumentParser(description="Score a pasted Upwork proposal draft locally.")
    parser.add_argument("--job", required=True, help="Path to job-post text")
    parser.add_argument("--proposal", required=True, help="Path to proposal-draft text")
    parser.add_argument("--niche", choices=["agency", "coach", "freelancer"], help="Optional buyer niche tweak")
    parser.add_argument("--intake-template", action="store_true", help="Append safe buyer intake text for a sample/pilot reply")
    parser.add_argument("--reply-template", action="store_true", help="Append safe qualified-intake reply text for a one-sample follow-up")
    parser.add_argument("--signal-decision", action="store_true", help="Append buyer-response signal/no-count/payment-hold decision log")
    args = parser.parse_args()
    job = Path(args.job).read_text(encoding="utf-8")
    proposal = Path(args.proposal).read_text(encoding="utf-8")
    output = render(job, proposal, args.niche)
    if args.intake_template:
        output += "\n\n" + intake_template(args.niche)
    if args.reply_template:
        output += "\n\n" + reply_template(args.niche)
    if args.signal_decision:
        output += "\n\n" + signal_decision_template(args.niche)
    print(output)


if __name__ == "__main__":
    main()
