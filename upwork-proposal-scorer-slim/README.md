# Upwork Proposal Scorer Slim v1

A buyer-ready, dependency-free Python CLI for freelancers, coaches, and agencies that want a quick human-reviewed QA pass before sending an Upwork proposal.

## Why this slim package exists

The previous internal pack became a large operations router. This v1-slim package kills that weak buyer path and keeps only the part a buyer can understand in 30 seconds: paste a job post + draft proposal, get a score and fixes.

## Boundaries

- Local text files only.
- No Upwork login.
- No scraping.
- No auto-submit or auto-message.
- No guaranteed-win claims.
- No payment links, invoices, account setup, KYC, wallet, or on-chain action.

## Run

```bash
python3 upwork_proposal_scorer_slim.py --job sample_job.txt --proposal sample_proposal.txt
python3 upwork_proposal_scorer_slim.py --job sample_job.txt --proposal sample_proposal.txt --niche agency
python3 upwork_proposal_scorer_slim.py --job sample_job.txt --proposal sample_proposal.txt --niche agency --intake-template
python3 upwork_proposal_scorer_slim.py --job sample_job.txt --proposal sample_proposal.txt --niche coach --reply-template
python3 upwork_proposal_scorer_slim.py --job sample_job.txt --proposal sample_proposal.txt --niche agency --signal-decision
```

## First-sale offer

Suggested no-cost demo: send `sample_output.txt` and offer one custom niche rubric tweak.

Suggested paid pilot after explicit buyer interest: **$49** for a customized rubric and one reviewed proposal sample. Route payment collection to Corey before any invoice/payment/account setup.

## Files

- `upwork_proposal_scorer_slim.py` — standalone scorer.
- `sample_job.txt` — public/demo-safe job post.
- `sample_proposal.txt` — public/demo-safe draft proposal.
- `sample_output.txt` — verified sample output.
- `buyer_one_page.md` — paste-ready buyer explanation and ask.
- `buyer_quickstart_proof.md` — public proof/quickstart that tells a buyer exactly what to send for a safe sample.
- `first_buyer_send_card.md` — one-message warm/permissioned send card, response routes, and signal-safe log.
- `buyer_intake_template.md` — exact safe reply after a buyer asks for a sample, trial, or more detail.
- `qualified_intake_reply_template.md` — paste-ready follow-up after a buyer gives qualified intake or asks for a sample.
- `buyer_response_signal_decision.md` — response log rules separating qualified pipeline, no-count replies, Corey payment holds, and kill/replace after 5 no-count outcomes.
- `agency_proposal_qa_checklist.md` — replacement agency-facing QA checklist and paste-ready permissioned ask if the generic freelancer sample-request route stays silent.
- `test_slim_scorer.py` — regression tests.
