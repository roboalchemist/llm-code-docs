# Source: https://developers.smtp2go.com/docs/rate-limiting.md

# Rate Limiting

## Rate Limiting

The `/activity/search` endpoint has a rate limit of 60 per minute. If you need realtime access to a data, you should make use of [Webhooks](https://developers.smtp2go.com/docs/webhooks-overview).

In the event that your interaction with the API results in what we deem to be too many requests or error responses, the IP address from which the requests originated will be timed out for an indeterminate amount of time, no less than 1 minute.

You will receive a `429 Too Many Requests` response code during this time. If you begin to see these responses, pause and lower your request rate until you begin to see `200 OK` returned. Should you start receiving `429 Too Many Requests`, also ensure the requests you are sending are returning `200 OK`.

## New Accounts

All new accounts are subject to review by our review team to ensure sending complies with our [Terms of Service](https://www.smtp2go.com/terms/). The review is a straightforward one-time process.

The initial sending quota for all new paid accounts is temporarily 1,000 emails per day. Once you’ve begun sending and are near that limit the account will automatically be assessed and, if sending is in accordance with our [Terms of Service](https://www.smtp2go.com/terms/), it will be fully activated. Any emails sent over the initial sending limit (1,000 emails) while in the review process will be held in the mail queue and released once fully activated.

Full details of this process including how to speed it up are covered in our [New Account Limits and the Review Process](https://support.smtp2go.com/hc/en-gb/articles/223087427-New-Account-Limits-and-the-Review-Process) support article.

## The Free Plan

The free plan allows 1,000 emails per month and has a limit of 200 emails per day (a 25-per-hour limitation also applies if no sender domains are verified). Further information and limitations can be found in our [Free Plan](https://support.smtp2go.com/hc/en-gb/articles/223087947-Free-Plan) article.

The free plan is a great way to get set up and sending before upgrading for more email volume per month, extended reporting (30 days instead of 5) and you will also gain access to extra account features such as Subaccounts, SMS Messaging, Email Overage, Scheduled Reporting, Email Testing Tools, Dedicated IPs, Activity Duration Extension and Email Archiving. Accounts on the free plan are limited to ticket support only after 14 days (paid plans have access to live chat and phone).

## Set a rate limit on API Keys

You can optionally set and manage sending rate (speed) limits individually for API Keys in the “Sending > API Keys” section of the App. If you exceed the set limit you will encounter an error such as "API key ratelimit exceeded". In this instance, an email notification will additionally be sent to your account's [team members](https://support.smtp2go.com/hc/en-gb/articles/900000030443-Team-Setup) who have "Notifications" enabled so you know the limit has been met.