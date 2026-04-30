# PR Readiness Checker Lite

Dependency-free local CLI that scores a pasted/saved `git diff` before a maintainer, agency, or bounty hunter asks for review.

It is designed for cash-forward, low-risk service offers:

- no GitHub login;
- no scraping;
- no private repo access;
- no auto-commenting or spam;
- no guarantee of merge/payment;
- output is a reviewer checklist plus a fixed-scope cleanup hook.

## Run

```bash
python3 pr_readiness_checker_lite.py --diff sample_diff.txt
python3 pr_readiness_checker_lite.py --service-template
python3 pr_readiness_checker_lite.py --ci-preflight-template
python3 pr_readiness_checker_lite.py --reviewer-reply-template
python3 pr_readiness_checker_lite.py --buyer-proof-template
python3 pr_readiness_checker_lite.py --maintainer-triage-template
python3 -m unittest -v
```

## Buyer use case

Use it when a PR is stuck, noisy, or risky. Paste a redacted diff and send the output with:

1. the target repo/PR URL if public,
2. the exact failing check or reviewer concern,
3. whether the desired service is test coverage, reviewer-map notes, or a small split/refactor.

Qualified signal rule: only a real public PR, redacted diff, or explicit fixed-scope cleanup request counts. Payment collection stays on Corey hold until invoice/payment/account setup is approved.

Use `pr_cleanup_sample_request.md` or `--service-template` to convert interest into paste-safe public/redacted inputs before any payment discussion. If the buyer specifically has a failing CI check, use `ci_failure_preflight.md` or `--ci-preflight-template` to request the exact command/log excerpt without credentials, private repo access, or CI dashboard login. After qualified inputs arrive, use `reviewer_reply_template.md` or `--reviewer-reply-template` to send a safe preflight response and convert explicit paid-pilot interest into a Corey-held payment/setup decision. If public issue intake stays quiet, use `blocked_pr_buyer_proof.md` or `--buyer-proof-template` as the direct no-login proof ask: public/redacted PR or diff plus exact blocker in, short readiness proof out, no payment setup before explicit fixed-scope intent. See `sample_buyer_proof_output.md` for the exact free proof shape a qualified requester would receive. If the owner-created proof issue remains passive, use `maintainer_blocked_pr_triage_offer.md` or `--maintainer-triage-template` as the replacement buyer angle for permissioned maintainers/agencies with visible PR review/CI backlog. `public_pr_triage_sample.md` shows a real public-diff no-contact proof sample so buyers can inspect the output shape before sending their own public/redacted PR.
