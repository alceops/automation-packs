# Reviewer reply template for blocked PR cleanup

Use this after a buyer provides paste-safe PR/diff inputs plus a failing command or reviewer blocker. It turns the free preflight into a concrete response and a safe fixed-scope cleanup ask.

## Paste-ready response

Thanks — I can review this from the public/redacted material only.

From the failing command / reviewer note, the blocker appears to be:

- **Failure class:** `<test failure | type error | lint | reviewer-risk | unclear>`
- **Smallest repro:** `<exact command/check name, if supplied>`
- **Likely fix path:** `<one small patch/test/docs/reviewer-map action>`
- **Risk/rollback note:** `<what could break and how to revert>`

Safe next step: I can send a short cleanup plan from the public PR/diff first. If you want implementation help after that, reply with **"fixed-scope cleanup"** and the exact public/redacted inputs below. Payment/invoice/account/KYC setup stays on Corey hold until explicit paid-pilot intent is present.

## Required inputs before counting as qualified pipeline

1. Public PR URL or redacted saved diff:
2. Exact failing command/check name:
3. Redacted first error/log excerpt or reviewer comment:
4. Desired outcome: reproduce note / minimal patch / test update / reviewer reply draft:
5. Paid-pilot intent: no / maybe / yes fixed-scope cleanup:

## Do not accept

- credentials, secrets, private customer data, private repo exports, CI dashboard login, private logs, scraping, auto-commenting, guaranteed merge/payment claims, or broad consulting without public/redacted PR/diff inputs.

## Signal rule

Count only a usable public/redacted PR/diff plus exact failing command/log/reviewer blocker, or explicit fixed-scope cleanup intent. Silence, stars, views, generic interest, and unsafe login/private-data asks are no-count.
