# Buyer response signal decision log

Use this after one warm/permissioned send or a buyer reply. It prevents fake traction and keeps the next cash step safe.

## Count as qualified pipeline only if

- Buyer sends a public/redacted job post plus draft proposal.
- Buyer asks for a one-sample review using paste-safe inputs.
- Buyer explicitly asks for the $49 custom rubric pilot.

## No-count outcomes

- Likes, views, silence, generic "interesting", or noncommittal praise.
- Requests for Upwork login, scraping, auto-submit, client messaging, private client data, payment details, or guaranteed wins.
- Bot/onboarding-only responses without a human ask.

## Next action rules

1. If paste-safe sample inputs arrive, run the scorer locally and send back the score, top 3 fixes, and one niche rubric note. Do not ask for payment first.
2. If the buyer asks to pay or requests an invoice/payment link/account path, pause for Corey approval before invoice, payment link, payment account setup, KYC, billing, or subscription change.
3. If the response asks for login, scraping, auto-submit, private data, or guaranteed outcomes, decline that scope and offer paste-only manual review.
4. After 5 no-count outcomes, kill the generic freelancer-proposal angle and pivot the same scorer into an agency proposal QA checklist or coach review-copy sample.

## CLI

```bash
python3 upwork_proposal_scorer_slim.py --job sample_job.txt --proposal sample_proposal.txt --niche agency --signal-decision
```
