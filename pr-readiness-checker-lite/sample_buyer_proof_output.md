# Sample buyer proof output

This is the shape of the free no-login proof returned from a public or redacted blocked-PR input. It uses the included `sample_diff.txt`; do not paste credentials, secrets, private repo exports, private CI logs, customer data, or CI dashboard links.

## Input used for this demo

- PR/source: redacted demo diff (`sample_diff.txt`)
- Blocker: reviewer/CI concern around payment-related scoring behavior
- Desired outcome: readiness verdict + likely cleanup path before any paid work

## Readiness proof

```text
PR Readiness Checker Lite
Verdict: needs-tightening (75/100)
Changed files: 2; changed lines: 8

Reviewer checklist:
- Test signal present: keep/quote the exact command and result in the PR.
- No docs signal: state why docs are unnecessary or add a short note.
- Risk terms found: payment. Add rollback and reviewer notes.
- Small diff (8 changed lines): likely reviewable if tests are clear.

Cash-forward service hook:
- If this flags risk, offer a fixed-scope PR cleanup: tests, reviewer map, and merge-ready notes.
- Keep payment/invoice setup on Corey hold until buyer intent is explicit.
```

## What I would send back to a qualified requester

Verdict: **needs-tightening**. The diff is small and has a targeted test, so it is close to reviewable. The blocker is that it touches payment-sensitive behavior without a rollback/reviewer note or a short docs/change note.

Top risks:
1. Payment-related scoring logic changed; reviewers need the exact intended behavior and rollback path.
2. Test signal exists, but the proof needs the exact command/result pasted with the request.
3. No docs/change-note signal; either add a short note or state why none is needed.

Likely fixed-scope cleanup path:
- add a one-paragraph reviewer note explaining the payment-risk branch;
- quote the exact test command/result;
- add a rollback note: revert the branch and test if payment scoring regresses;
- only discuss paid implementation after explicit fixed-scope cleanup intent.

Qualification rule: count only a usable public/redacted PR or diff plus exact failing command/log/reviewer blocker, or explicit fixed-scope cleanup intent. Stars, views, silence, generic interest, private-access requests, credentials, scraping, auto-commenting, guaranteed merge claims, payment links, invoices, account setup, and KYC are no-count or Corey-held.
