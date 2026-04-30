# CI Failure Preflight

Use this as the narrower replacement angle when generic PR readiness interest produces no qualified requests.

## What counts as qualified pipeline

Count only:

- a public PR URL or a saved/redacted `git diff`, **and**
- the exact failing check/command or reviewer blocker, **or**
- explicit fixed-scope cleanup intent after a free preflight sample.

Do not count stars, views, silence, generic "interesting", broad consulting asks, or any request for private repo login, credentials, secrets, scraping, CI dashboard access, auto-comments, guaranteed merge, or guaranteed payment.

## Paste-ready buyer ask

```text
I can do a no-login CI failure preflight from public/redacted text only.

Please paste:
1. Public PR URL or say "redacted diff only":
2. Failing check name and command:
3. Redacted failure excerpt (first error + stack/context only):
4. What changed recently in the PR:
5. Desired outcome: reproduce note / minimal patch / test update / reviewer reply draft:
6. Paid-pilot interest after the free preflight: no / maybe / yes fixed-scope cleanup:

Do not send credentials, secrets, private repo exports, private logs, or customer data. I will not log in, scrape, auto-comment, or guarantee merge/payment. Payment collection waits for Corey approval before invoice/payment/account/KYC setup.
```

## First response shape

If the request is qualified, respond with:

1. suspected failure class;
2. smallest reproducible command/check to run;
3. one likely fix path;
4. one risk/rollback note;
5. optional fixed-scope cleanup offer only if the buyer explicitly indicates paid-pilot interest.
