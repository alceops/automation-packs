# Agency PR Backlog Triage Offer

A narrower buyer surface for agencies/maintainers with visible blocked PR review or CI backlog.

## Who this is for

Use this when an agency or maintainer has 2+ public/redacted PRs stuck on one of these blockers:

- failing CI with an exact command/check name;
- reviewer requested tests, risk notes, or smaller PRs;
- release is blocked by a risky diff;
- client delivery is waiting on merge-readiness proof.

## Free sample ask

Paste one public/redacted PR or saved diff plus the exact failing command/log excerpt or reviewer blocker. I will return a short no-login triage sample:

1. readiness verdict;
2. top blockers/missing inputs;
3. likely fixed-scope cleanup path;
4. safe reviewer/maintainer reply text;
5. whether it looks like a fixed-scope cleanup candidate.

## Paste-ready public issue text

```text
I have a blocked PR/review queue and want one free no-login triage sample.

Public PR or redacted diff:
<URL or redacted diff summary>

Exact blocker:
<failing command/check, reviewer concern, or release blocker>

Desired cleanup:
<tests/coverage, reviewer map, split/refactor plan, docs/release note, rollback/risk notes>

Paid-pilot interest after sample:
<no / maybe / yes fixed-scope cleanup>
```

## Safety boundary

Do not send credentials, secrets, private repo exports, private logs, customer data, CI dashboard access, or anything that requires login. This is local text review only: no scraping, auto-commenting, guaranteed merge/payment, payment links, invoices, account setup, KYC, wallet, or on-chain action.

If there is explicit paid-pilot intent, payment collection stays on Corey hold until invoice/payment/account setup is separately approved.

## Signal rule

Count as qualified pipeline only if a non-owner provides:

- a usable public/redacted PR or diff, plus exact failing command/log/reviewer blocker; or
- explicit fixed-scope cleanup intent after seeing the sample proof.

Do not count owner-created issues/comments, stars, views, silence, generic interest, unsafe private-data requests, login requests, scraping requests, auto-comment requests, or guaranteed-merge/payment asks.

## Kill/replace rule

If 5 consecutive non-owner outcomes are no-count, stop polishing PR-readiness copy and replace with a different buyer channel or a direct-service lead with an existing public maintainer request.
