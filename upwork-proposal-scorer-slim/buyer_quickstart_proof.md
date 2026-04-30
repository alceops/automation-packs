# Buyer quickstart proof

Use this when someone asks "what do I actually get?" It is designed to convert a low-friction public visit into a paste-safe sample request without requiring login, scraping, payment setup, or private data.

## 60-second local demo

```bash
python3 upwork_proposal_scorer_slim.py --job sample_job.txt --proposal sample_proposal.txt --niche agency
```

Expected proof:

- returns a numeric proposal score;
- highlights missing client-specific proof;
- suggests safer, more concrete fixes;
- stays local to text files;
- does not log in, scrape, auto-submit, auto-message, or promise wins.

## What to send for a free sample

Open the structured sample-request form at `https://github.com/alceops/automation-packs/issues/new?template=sample_request.yml` or email `alce.ops@gmail.com` with only:

1. niche: `freelancer`, `coach`, or `agency`;
2. public/redacted job post text;
3. public/redacted draft proposal text;
4. one desired rubric emphasis, such as proof, brevity, risk, or niche fit.

Do **not** send credentials, account access, private client data, non-public job details, or anything that requires logging into Upwork.

## Qualified signal rule

Count as qualified pipeline only when the reply includes paste-safe sample inputs or explicit paid-pilot intent.

Do not count stars, views, likes, generic interest, silence, unsafe login/scrape/auto-submit requests, private-data requests, or guaranteed-win asks.

## Paid pilot hold

If someone asks to pay for a customized rubric and one reviewed proposal sample, stop before collecting money. Payment collection, invoice links, account setup, KYC, wallet, or on-chain actions require Corey approval first.
