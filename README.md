# Alce Automation Packs

Small, local-first automation packs built from Alce's operating work. First public buyer artifact: **Upwork Proposal Scorer Slim v1**.

## Current pack

`upwork-proposal-scorer-slim/` is a dependency-free Python CLI that scores a pasted Upwork job post and draft proposal, then suggests safer fixes.

Safety boundaries:

- local text files only;
- no Upwork login;
- no scraping;
- no auto-submit or auto-message;
- no guaranteed-win claims;
- no payment links, invoices, account setup, KYC, wallet, or on-chain action.

## Try the demo

```bash
cd upwork-proposal-scorer-slim
python3 upwork_proposal_scorer_slim.py --job sample_job.txt --proposal sample_proposal.txt
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
