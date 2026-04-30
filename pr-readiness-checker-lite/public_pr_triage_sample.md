# Public PR triage sample — no-login proof shape

This is a demo-safe sample generated from a public pull request diff. It is not a buyer signal, not an endorsement, and not a public comment to the project. It exists to show maintainers/agencies what a free no-login blocked-PR triage sample returns before any paid cleanup discussion.

Source checked: `apache/airflow` PR #65571, "Adds async support to SageMakerNotebookJobTrigger"  
Public diff URL: https://github.com/apache/airflow/pull/65571.diff  
Local command used:

```bash
python3 pr_readiness_checker_lite.py --diff airflow_65571.diff
```

## Generated readiness output

```text
PR Readiness Checker Lite
Verdict: not-ready (49/100)
Changed files: 248; changed lines: 9614

Reviewer checklist:
- Test signal present: keep/quote the exact command and result in the PR.
- Documentation/change note present.
- Risk terms found: auth, billing, delete, migration, password, schema, security, token. Add rollback and reviewer notes.
- Large diff (9614 changed lines): split or add a reviewer map.

Cash-forward service hook:
- If this flags risk, offer a fixed-scope PR cleanup: tests, reviewer map, and merge-ready notes.
- Keep payment/invoice setup on Corey hold until buyer intent is explicit.
```

## What a maintainer/agency would receive in the free proof

1. **Readiness verdict:** `not-ready` due to very high review surface, despite visible test/docs signal.
2. **Top blocker:** 248 files / 9,614 changed lines is too broad for fast review without a reviewer map or split plan.
3. **Smallest missing input:** exact failing check or reviewer blocker; if none exists, the useful next input is the exact test command/result from the PR author.
4. **Likely cleanup path:** produce a reviewer map grouped by provider/runtime/test/doc areas, then split or explicitly justify any unrelated generated/churn-heavy files.
5. **Paste-ready reviewer note:**

> I can review this faster if the PR description lists the exact test command/result, a file-group reviewer map, and the risk/rollback note for auth/security/token/schema-adjacent changes. If the large generated/churn section is required, please call it out separately from the behavioral async trigger change.

## Qualification rule

Count only a non-owner requester who provides a usable public/redacted PR or diff plus exact failing command/log/reviewer blocker, or explicit fixed-scope cleanup intent. Do **not** count this demo sample, owner-created issues, stars, views, downloads, silence, generic interest, or unsafe private-data/login asks as pipeline.

## Safety/payment boundary

No credentials, secrets, private repo exports, private logs, customer data, CI dashboard login, scraping, auto-commenting, guaranteed merge claims, payment links, invoices, account setup, or KYC before explicit paid-pilot intent and Corey approval for payment setup.
