# Source: https://documentation.mailgun.com/docs/inspect/api-reference/openapi-final.md

# Source: https://documentation.mailgun.com/docs/validate/oas/openapi-final.md

# Alerts

Our alerting solution is centered around two concepts: events and channels. The occurrence of an event can be configured to trigger an alert. A channel describes the delivery method for an alert. Every configured alert consists of an event type / channel pair. This level of granularity allows alerting to be configured to your exact preference.

Version: 0.0.1

## Servers

US Mailgun
```
https://api.mailgun.net
```

EU Mailgun
```
https://api.eu.mailgun.net
```

## Security

### basicAuth

HTTP Basic auth using api:YOUR_API_KEY. See [documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/authentication/)

Type: http
Scheme: basic

### Inbox_Ready_basicAuth

HTTP Basic auth using api:YOUR_API_KEY. See [documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/authentication/)

Type: http
Scheme: basic

### Domain_Blocklist_Monitoring_basicAuth

HTTP Basic auth using api:YOUR_API_KEY. See [documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/authentication/)

Type: http
Scheme: basic

### Spamtraps_Analytics_Service_basicAuth

HTTP Basic auth using api:YOUR_API_KEY. See [documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/authentication/)

Type: http
Scheme: basic

### Inbox_Placement_Testing_basicAuth

HTTP Basic auth using api:YOUR_API_KEY. See [documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/authentication/)

Type: http
Scheme: basic

### Maverick_Score_basicAuth

HTTP Basic auth using api:YOUR_API_KEY. See [documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/authentication/)

Type: http
Scheme: basic

### DMARC_Reports_basicAuth

HTTP Basic auth using api:YOUR_API_KEY. See [documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/authentication/)

Type: http
Scheme: basic

### reputationanalytics_basicAuth

HTTP Basic auth using api:YOUR_API_KEY. See [documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/authentication/)

Type: http
Scheme: basic

## Download OpenAPI description

[Alerts](https://documentation.mailgun.com/_spec/docs/validate/oas/openapi-final.yaml)

## Domains

### Returns Domains on Mailgun Optimize services

 - [GET /v1/inboxready/domains](https://documentation.mailgun.com/docs/validate/oas/openapi-final/domains/get-v1-inboxready-domains.md): Will return details on an Mailgun Optimize Domain. If no Domain is provided, then a list of all Mailgun Optimize Domains on an account will be returned.

### Add a single domain to an account

 - [POST /v1/inboxready/domains](https://documentation.mailgun.com/docs/validate/oas/openapi-final/domains/post-v1-inboxready-domains.md)

### Deletes a single domain from an account

 - [DELETE /v1/inboxready/domains](https://documentation.mailgun.com/docs/validate/oas/openapi-final/domains/delete-v1-inboxready-domains.md)

### Queues a domain to be processed for verification

 - [PUT /v1/inboxready/domains/verify](https://documentation.mailgun.com/docs/validate/oas/openapi-final/domains/put-v1-inboxready-domains-verify.md)

## DMARC Reports

DMARC reporting provides valuable insights into your infrastructure, helping you identify potential issues like senders, misconfigured email servers, or phishing attempts.

### Retrieves the DMARC DNS records to be used for configuration

 - [GET /v1/dmarc/records/{domain}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/dmarc-reports/get-v1-dmarc-records-domain-.md)

### Checks if DMARC has been setup for user

 - [GET /v1/dmarc/setup](https://documentation.mailgun.com/docs/validate/oas/openapi-final/dmarc-reports/get-v1-dmarc-setup-.md)

### Gets referral link to redsift

 - [POST /v1/dmarc/referral](https://documentation.mailgun.com/docs/validate/oas/openapi-final/dmarc-reports/post-v1-dmarc-referral-.md)

### Retrieves the list of domains that have DMARC monitoring.

 - [GET /v1/dmarc/domains](https://documentation.mailgun.com/docs/validate/oas/openapi-final/dmarc-reports/get-v1-dmarc-domains-.md)

### Retrieve DMARC reporting data for a domain.

 - [GET /v1/dmarc/domains/{domain}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/dmarc-reports/get-v1-dmarc-domains-domain-.md)

### Retrieve DMARC reporting data from a specific source.

 - [GET /v1/dmarc/domains/{domain}/s/{source}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/dmarc-reports/get-v1-dmarc-domains-domain-s-source-.md)

### Retrieve DMARC reporting data for a hostname.

 - [GET /v1/dmarc/domains/{domain}/s/{source}/h/{host}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/dmarc-reports/get-v1-dmarc-domains-domain-s-source-h-host-.md)

### Retrieve DMARC reporting data for an IP Address.

 - [GET /v1/dmarc/domains/{domain}/s/{source}/h/{host}/ip/{ip}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/dmarc-reports/get-v1-dmarc-domains-domain-s-source-h-host-ip-ip-.md)

## Inbox Placement

Inbox Placement testing allows you to see the likely deliverability of your email campaigns.

### List Seed Lists

 - [GET /v4/inbox/seedlists](https://documentation.mailgun.com/docs/validate/oas/openapi-final/inbox-placement/get-v4-inbox-seedlists.md)

### Generate a New Seed List

 - [POST /v4/inbox/seedlists](https://documentation.mailgun.com/docs/validate/oas/openapi-final/inbox-placement/post-v4-inbox-seedlists.md)

### List Available Attributes for Seed Lists

 - [GET /v4/inbox/seedlists/a](https://documentation.mailgun.com/docs/validate/oas/openapi-final/inbox-placement/get-v4-inbox-seedlists-a.md)

### Get List of Values for Seed List Attribute

 - [GET /v4/inbox/seedlists/a/{attribute}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/inbox-placement/get-v4-inbox-seedlists-a--attribute-.md)

### Get List of Available Seed List Filters

 - [GET /v4/inbox/seedlists/_filters](https://documentation.mailgun.com/docs/validate/oas/openapi-final/inbox-placement/get-v4-inbox-seedlists--filters.md)

### Get Seed List

 - [GET /v4/inbox/seedlists/{address}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/inbox-placement/get-v4-inbox-seedlists--address-.md)

### Update Seed List

 - [PUT /v4/inbox/seedlists/{address}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/inbox-placement/put-v4-inbox-seedlists--address-.md)

### Delete a Seed List

 - [DELETE /v4/inbox/seedlists/{address}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/inbox-placement/delete-v4-inbox-seedlists--address-.md)

### List Results

 - [GET /v4/inbox/results](https://documentation.mailgun.com/docs/validate/oas/openapi-final/inbox-placement/get-v4-inbox-results.md): Get the details for all placement test results.

### List Available Attributes for Results

 - [GET /v4/inbox/results/a](https://documentation.mailgun.com/docs/validate/oas/openapi-final/inbox-placement/get-v4-inbox-results-a.md): The attributes that can have values listed (for autocomplete).

### Get List of Values for a Result Attribute

 - [GET /v4/inbox/results/a/{attribute}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/inbox-placement/get-v4-inbox-results-a--attribute-.md): For the given attribute list the known values (for autocomplete).

### List available filters for Results

 - [GET /v4/inbox/results/_filters](https://documentation.mailgun.com/docs/validate/oas/openapi-final/inbox-placement/get-v4-inbox-results--filters.md): The filters that can be used when querying for results.

### Get Result Details

 - [GET /v4/inbox/results/{result}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/inbox-placement/get-v4-inbox-results--result-.md): Get the details for a single result.

### Delete Result

 - [DELETE /v4/inbox/results/{result}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/inbox-placement/delete-v4-inbox-results--result-.md): Delete the result and all associated information.

### Get Result Sharing Status

 - [GET /v4/inbox/sharing/{result}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/inbox-placement/get-v4-inbox-sharing--result-.md): The sharing status of a result.

### Update Result Sharing Status

 - [PUT /v4/inbox/sharing/{result}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/inbox-placement/put-v4-inbox-sharing--result-.md): Change the sharing status of a result or create a new share URL

### Get Result by a Share ID

 - [GET /v4/inbox/sharing/public/{shareid}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/inbox-placement/get-v4-inbox-sharing-public--shareid-.md): Get a result by the share ID.

### Run Inbox Placement Test

 - [POST /v4/inbox/tests](https://documentation.mailgun.com/docs/validate/oas/openapi-final/inbox-placement/post-v4-inbox-tests.md): Create and run a new inbox placement test. 

Either 'html' or 'template_name' field should be provided.

'variables' are Template variables,
which could be used in html or template.
You can use next recipient variables inside Template variables, 
which will be filled for every seed automatically:
%recipient.first_name%, %recipient.last_name%.

### List Email Providers

 - [GET /v4/inbox/providers](https://documentation.mailgun.com/docs/validate/oas/openapi-final/inbox-placement/get-v4-inbox-providers.md): List all available email providers.

## Spam Traps Monitoring

Our spam trap monitoring service surfaces how much of your email is being sent to known spam traps.

### Get Spam Trap Hits

 - [GET /v1/spamtraps](https://documentation.mailgun.com/docs/validate/oas/openapi-final/spam-traps-monitoring/get-v1-spamtraps.md): Use this endpoint to understand how much of your mail being sent to known spam traps. This endpoint returns daily spam trap hit counts for a provided timerange, categorized by trap type.

## Email Health Score

### Get Email Health score and rates for account and subaccounts

 - [GET /v1/maverick-score/total](https://documentation.mailgun.com/docs/validate/oas/openapi-final/email-health-score/get-v1-maverick-score-total.md)

### List Email Health score and rates grouped by domains/ips/subaccounts/timestamps

 - [GET /v1/maverick-score/grouped](https://documentation.mailgun.com/docs/validate/oas/openapi-final/email-health-score/get-v1-maverick-score-grouped.md)

## IP Blocklist Monitoring

### Lists monitored IP addresses

 - [GET /v1/inboxready/ip_addresses](https://documentation.mailgun.com/docs/validate/oas/openapi-final/ip-blocklist-monitoring/get-v1-inboxready-ip-addresses.md)

### Register an IP address

 - [POST /v1/inboxready/ip_addresses](https://documentation.mailgun.com/docs/validate/oas/openapi-final/ip-blocklist-monitoring/post-v1-inboxready-ip-addresses.md)

### Get the IP address

 - [GET /v1/inboxready/ip_addresses/{ip}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/ip-blocklist-monitoring/get-v1-inboxready-ip-addresses--ip-.md)

### Update the IP address

 - [PUT /v1/inboxready/ip_addresses/{ip}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/ip-blocklist-monitoring/put-v1-inboxready-ip-addresses--ip-.md)

### Removes IP from monitoring

 - [DELETE /v1/inboxready/ip_addresses/{ip}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/ip-blocklist-monitoring/delete-v1-inboxready-ip-addresses--ip-.md)

## Domain Blocklist Monitoring

Blocklist Monitoring enables you to keep an eye on your reputation. Monitor your domains against our curated list of blocklist providers to make sure you aren't being blocked.

### Get Monitored Domains

 - [GET /v1/monitoring/domains](https://documentation.mailgun.com/docs/validate/oas/openapi-final/domain-blocklist-monitoring/get-v1-monitoring-domains.md): Gets all domains that are being monitored for blocklisting

### Get All Events

 - [GET /v1/monitoring/domains/events](https://documentation.mailgun.com/docs/validate/oas/openapi-final/domain-blocklist-monitoring/get-v1-monitoring-domains-events.md): Get all events for all domains monitored

### Get Lists Domain is Listed in

 - [GET /v1/monitoring/domains/{domain}/blocklists](https://documentation.mailgun.com/docs/validate/oas/openapi-final/domain-blocklist-monitoring/get-v1-monitoring-domains--domain--blocklists.md): Get blocklists that the domain is listed in

### Get Events for Domain

 - [GET /v1/monitoring/domains/{domain}/events](https://documentation.mailgun.com/docs/validate/oas/openapi-final/domain-blocklist-monitoring/get-v1-monitoring-domains--domain--events.md): Get events for a specific domain

## Google Postmaster Tools

This API provides access to Google Postmaster data.

### Get GPT Domain

 - [GET /v1/reputationanalytics/gpt/domains/{domain}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/google-postmaster-tools/get-v1-reputationanalytics-gpt-domains--domain-.md): Returns domain records for a single domain on the account. Each domain record is for a single domain on a single day.

### Get GPT Domains

 - [GET /v1/reputationanalytics/gpt/domains](https://documentation.mailgun.com/docs/validate/oas/openapi-final/google-postmaster-tools/get-v1-reputationanalytics-gpt-domains.md): Returns a list of all domain records for an account. Each domain record is for a single domain on a single day.

### Get GPT Domains

 - [GET /v1/reputationanalytics/gpt/domains_list](https://documentation.mailgun.com/docs/validate/oas/openapi-final/google-postmaster-tools/get-v1-reputationanalytics-gpt-domains-list.md): Returns a list of all domains for an account

### Get GPT FBL

 - [GET /v1/reputationanalytics/gpt/domainsfbl](https://documentation.mailgun.com/docs/validate/oas/openapi-final/google-postmaster-tools/get-v1-reputationanalytics-gpt-domainsfbl.md): Returns the FBL for the account or domain

### Get GPT FBL

 - [GET /v1/reputationanalytics/gpt/domainsfbl/{domain}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/google-postmaster-tools/get-v1-reputationanalytics-gpt-domainsfbl--domain-.md): Returns the FBL for the account or domain

### Get GPT Address

 - [GET /v1/reputationanalytics/gpt/addresses/{address}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/google-postmaster-tools/get-v1-reputationanalytics-gpt-addresses--address-.md): Returns address records for an single address on the account. Each address record is for a single address on a single day.

### Get GPT Addresses

 - [GET /v1/reputationanalytics/gpt/addresses](https://documentation.mailgun.com/docs/validate/oas/openapi-final/google-postmaster-tools/get-v1-reputationanalytics-gpt-addresses.md): Returns a list of all address records for an account. Each address record is for a single address on a single day.

### Get all GPT Addresses

 - [GET /v1/reputationanalytics/gpt/addresses_list](https://documentation.mailgun.com/docs/validate/oas/openapi-final/google-postmaster-tools/get-v1-reputationanalytics-gpt-addresses-list.md): Returns a list of all addresses for an account

### Get GPT Domain Addresses

 - [GET /v1/reputationanalytics/gpt/domains/{domain}/addresses](https://documentation.mailgun.com/docs/validate/oas/openapi-final/google-postmaster-tools/get-v1-reputationanalytics-gpt-domains--domain--addresses.md): Returns a list of all address records for an account belonging to a specific domain. Each address record is for a single address on a single day.

### Get GPT Summary

 - [GET /v1/reputationanalytics/gpt/summary](https://documentation.mailgun.com/docs/validate/oas/openapi-final/google-postmaster-tools/get-v1-reputationanalytics-gpt-summary.md): Returns a list of all summary records for an account. Each record is for a single domain's summary and error summary data.

### Get GPT Domains Summary

 - [GET /v1/reputationanalytics/gpt/summary/domains](https://documentation.mailgun.com/docs/validate/oas/openapi-final/google-postmaster-tools/get-v1-reputationanalytics-gpt-summary-domains.md): Returns a list of all domain summary records for an account. Each record is for a single domain's summary data.

### Get GPT Domains Error Summary

 - [GET /v1/reputationanalytics/gpt/summary/errors](https://documentation.mailgun.com/docs/validate/oas/openapi-final/google-postmaster-tools/get-v1-reputationanalytics-gpt-summary-errors.md): Returns a list of all domain error summary records for an account. Each record is for a single domain's error summary data.

### Get GPT Addresses Summary

 - [GET /v1/reputationanalytics/gpt/summary/addresses](https://documentation.mailgun.com/docs/validate/oas/openapi-final/google-postmaster-tools/get-v1-reputationanalytics-gpt-summary-addresses.md): Returns a list of all address summary records for an account. Each record is for a single address's summary data.

## Microsoft SNDS

This API provides access to Microsoft SNDS data.

### Get SNDS Address Info

 - [GET /v1/reputationanalytics/snds](https://documentation.mailgun.com/docs/validate/oas/openapi-final/microsoft-snds/get-v1-reputationanalytics-snds.md): Returns a list of all address summary records for an account. Each record is for a single address's summary data.

### Get SNDS Address Info

 - [GET /v1/reputationanalytics/snds/{ip}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/microsoft-snds/get-v1-reputationanalytics-snds--ip-.md): Returns a list of all address summary records for an account and a single address

## Alerts

### List events

 - [GET /v1/alerts/events](https://documentation.mailgun.com/docs/validate/oas/openapi-final/alerts/get-v1-alerts-events.md): The current list of events that you can chose to receive alerts for.

### Add Alert

 - [POST /v1/alerts/settings/events](https://documentation.mailgun.com/docs/validate/oas/openapi-final/alerts/post-v1-alerts-settings-events.md): Use this endpoint to add new alert settings record.

### Webhooks

This section covers details around consuming Mailgun Optimize alerts via webhooks. If you are familiar with Mailgun Send webhooks, 
there is a lot of overlapping similarity, however, there are also a few minor nuances to account for.

#### Securing Webhooks

HMAC is used to verified to integrity as well as the authenticity of received webhooks. To verify the origin of a webhook:

1. Encode the webhookâs entire POST request body with the HMAC algorithm (using your webhook signing key and SHA256 digest mode)
2. Compare the resulting hexdigest to the signature provided in the POST requestâs X-Sign header.

NOTE: If youâre consuming Mailgun Send webhooks, please note that your Mailgun Send webhook signing key differs 
from your Mailgun Optimize alerts webhook signing key. 
Your Mailgun Optimize alerts webhook signing key is available within the Mailgun Optimize UI.

#### Webhook URL Validation

When adding or updating a webhook URL for alerts, we will ensure the endpoint is reachable by sending a GET request to the provided URL. If a 200 response is not returned from your endpoint, the request will be rejected and your alert setting will not be saved. We intentionally chose to send a GET request instead of a POST when validating URLs so that your webhook endpoint does not have to account for test requests.

Additionally, when a POST request is sent to your webhook URL, if a 2xx is not returned, we will attempt retries via an exponential backoff strategy for up to ~8 hours. If the max retry count is reached, the alert will be disabled and the related alert settings recordâs disabled_at field will be populated.

### Update Alert

 - [PUT /v1/alerts/settings/events/{id}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/alerts/put-v1-alerts-settings-events--id-.md): Use this endpoint to update an existing alert setting record.

NOTE: When updating a webhook alert, we will ensure the endpoint is reachable by sending a GET request to the provided URL. If a 200 response is not returned, a 400 will be returned and the alert setting update will be rejected.

### Remove Alert

 - [DELETE /v1/alerts/settings/events/{id}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/alerts/delete-v1-alerts-settings-events--id-.md)

### List Alerts

 - [GET /v1/alerts/settings](https://documentation.mailgun.com/docs/validate/oas/openapi-final/alerts/get-v1-alerts-settings.md): This endpoint returns a list of all configured alert settings for your account.

### Update Slack settings

 - [PUT /v1/alerts/settings/slack](https://documentation.mailgun.com/docs/validate/oas/openapi-final/alerts/put-v1-alerts-settings-slack.md)

### Delete Slack settings

 - [DELETE /v1/alerts/settings/slack](https://documentation.mailgun.com/docs/validate/oas/openapi-final/alerts/delete-v1-alerts-settings-slack.md): Delete Slack settings and Slack event settings for the Mailgun account.

To revoke the Slack access token, use DELETE /v1/alerts/slack/oauth.

To completely remove the Slack App from Slack Workspace, go into App Configuration in Slack.

### Reset Webhook Signing Key

 - [PUT /v1/alerts/settings/webhooks/signing_key](https://documentation.mailgun.com/docs/validate/oas/openapi-final/alerts/put-v1-alerts-settings-webhooks-signing-key.md)

### Test webhook

 - [POST /v1/alerts/webhooks/test](https://documentation.mailgun.com/docs/validate/oas/openapi-final/alerts/post-v1-alerts-webhooks-test.md): Sends test webhook request to specified url with dummy data.

### Test message

 - [POST /v1/alerts/email/test](https://documentation.mailgun.com/docs/validate/oas/openapi-final/alerts/post-v1-alerts-email-test.md): Sends test message to emails with dummy data.

### Test message

 - [POST /v1/alerts/slack/test](https://documentation.mailgun.com/docs/validate/oas/openapi-final/alerts/post-v1-alerts-slack-test.md): Sends test message to slack channels with dummy data.

### Revoke Slack access token

 - [DELETE /v1/alerts/slack/oauth](https://documentation.mailgun.com/docs/validate/oas/openapi-final/alerts/delete-v1-alerts-slack-oauth.md): Revoke Slack access token, delete Slack settings and Slack event settings.

NOTE: All Mailgun accounts connected to the same Slack workspace share the same token.

To completely remove the Slack App from Slack Workspace, go into App Configuration in Slack.

### Get Slack channel

 - [GET /v1/alerts/slack/channels/{id}](https://documentation.mailgun.com/docs/validate/oas/openapi-final/alerts/get-v1-alerts-slack-channels--id-.md): Returns Slack channel.

### List Slack channels

 - [GET /v1/alerts/slack/channels](https://documentation.mailgun.com/docs/validate/oas/openapi-final/alerts/get-v1-alerts-slack-channels.md): List Slack channels for the connected Slack workspace.

