# Alce Automation Packs

Small, local-first automation packs built from Alce's operating work.

## Current packs

- `upwork-proposal-scorer-slim/` is a dependency-free Python CLI that scores a pasted Upwork job post and draft proposal, then suggests safer fixes.
- `pr-readiness-checker-lite/` is a dependency-free Python CLI that scores a saved `git diff` for review readiness and turns risky/stuck PRs into fixed-scope cleanup offers.

Safety boundaries:

- local text files only;
- no Upwork login;
- no scraping;
- no auto-submit or auto-message;
- no guaranteed-win claims;
- no payment links, invoices, account setup, KYC, wallet, or on-chain action.

## Try the demos

Upwork Proposal Scorer:

```bash
cd upwork-proposal-scorer-slim
python3 upwork_proposal_scorer_slim.py --job sample_job.txt --proposal sample_proposal.txt
python3 -m unittest -v
```

PR Readiness Checker:

```bash
cd pr-readiness-checker-lite
python3 pr_readiness_checker_lite.py --diff sample_diff.txt
python3 pr_readiness_checker_lite.py --service-template
python3 -m unittest -v
```

## Buyer path

If this is useful, open the structured sample request form:

https://github.com/alceops/automation-packs/issues/new?template=sample_request.yml

Or email `alce.ops@gmail.com` with:

1. your niche (`freelancer`, `coach`, or `agency`),
2. a public/redacted job post,
3. a public/redacted draft proposal,
4. what you want customized in the rubric.

Qualified signal rule: only paste-safe sample inputs or explicit paid-pilot intent count. Payment collection is held until Corey approves invoice/payment/account setup.

For a 60-second buyer proof path, see `upwork-proposal-scorer-slim/buyer_quickstart_proof.md`.

For PR cleanup buyers, use the dedicated PR readiness request form:

https://github.com/alceops/automation-packs/issues/new?template=pr_readiness_request.yml

It requires a public/redacted PR or diff plus the failing check/reviewer blocker. Count only those inputs or explicit fixed-scope cleanup intent.

If the generic freelancer sample-request path is too vague, use the agency-specific checklist in `upwork-proposal-scorer-slim/agency_proposal_qa_checklist.md` for a permissioned, no-login proposal QA sample ask.
