# Source: https://docs.rootly.com/ai/data-privacy-for-ai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data Privacy for AI

> Learn about Rootly's data privacy and security safeguards for AI features, including what data is shared with OpenAI and how your incident information is protected.

Rootly is dedicated to maintaining the highest standards of privacy and security. [Read more about our data philosophy](https://rootly.com/blog/building-a-privacy-first-ai-for-incident-management).

* Rootly AI, driven by OpenAI, incorporates multiple safeguards to ensure the security of your data, providing you with peace of mind.
* Data sent to OpenAI is solely used to provide Rootly AI services and is neither stored nor used for training purposes by OpenAI.
* We automatically redact the following PII before sending any data to OpenAI:
  * email, addresses, phone numbers, credit card numbers, social security numbers (SSNs) and passwords in URLs
* Private incident data is **never** sent to OpenAI.
* Rootly AI never uses your data (even if anonymously) to improve results for other customers; it stays within the walls of your organization and is only used there.
* You may opt-out at any time via the [AI configuration page](https://rootly.com/account/ai/configurations). No future changes to how your data is used will change without your explicit approval.
* Optionally, organizations may [integrate their OpenAI account](https://rootly.com/account/integrations/open_ai_accounts/new) to take advantage of any organization specific data retention policies.

**Data from the incident that will be considered includes:**

* Built-in and custom fields
* Human-created timeline events
* Completed action items
* Timestamps
* Alert source
* Mitigated and resolved messages
* Slack messages from the incident channel (depending upon [Slack channel message visibility](https://rootly.com/account/ai/configurations))

**Data that is not considered includes:**

* Incident feedback
* Automated timeline events relating to action items, workflow runs and playbooks.
* Any data from private incidents

<Note>
  Note: To enable higher quality output [Slack Scope Updates](/ai/slack-scope-updates) are required.
</Note>


Built with [Mintlify](https://mintlify.com).