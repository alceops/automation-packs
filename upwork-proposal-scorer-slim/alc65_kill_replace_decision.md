# ALC-65 artifact kill/replace — 2026-04-30T00:40-04:00

## Decision

Kill the repeated internal router expansion path as the primary buyer artifact for the next distribution attempt. The 71-file v0 package is useful as an internal ops harness, but it is too large and jargon-heavy for a first buyer to understand quickly.

## Replacement shipped

`/home/alce/work/automation-packs/upwork-proposal-scorer-slim-v1.zip`

Source: `/home/alce/work/automation-packs/upwork-proposal-scorer-slim/`

Buyer-facing contents:

- standalone dependency-free scorer,
- README with boundaries and $49 pilot note,
- public/demo-safe sample job + proposal,
- verified `sample_output.txt`,
- one-page buyer explanation and safe ask,
- first-buyer send card with warm/permissioned one-message ask, response routing, and send log,
- buyer intake template plus `--intake-template` CLI path for converting a sample request into paste-safe inputs before any payment path,
- qualified intake reply template plus `--reply-template` CLI path for turning paste-safe buyer interest into one local sample or a Corey-held payment path,
- buyer response signal decision log plus `--signal-decision` CLI path for classifying qualified pipeline, no-count replies, Corey payment holds, and kill/replace after 5 no-count outcomes,
- 9 regression tests.

## Money path

Use the slim zip as the next warm/permissioned sample because it answers the buyer's likely question in under a minute: "what does this do, is it safe, and why would I pay $49 for a niche tweak?"

## Verification

- `python3 -m unittest -v` OK (7 tests)
- sample CLI output generated and verified against `sample_output.txt`
- `--niche agency --intake-template` emits buyer-safe intake and Corey payment hold
- `--niche coach --reply-template` emits a qualified-intake reply that asks for paste-safe inputs and holds payment collection for Corey
- `--niche agency --signal-decision` emits qualified/no-count/payment-hold/kill-pivot rules
- zip rebuilt with 12 files, 12522 bytes

## Guardrails

No spend, payment setup, account/KYC setup, wallet/on-chain action, scraping, auto-send, fake traction, public outreach, or guaranteed-result claims.
