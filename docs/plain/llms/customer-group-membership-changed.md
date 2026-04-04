# Source: https://www.plain.com/docs/webhooks/customer-group-membership-changed.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.plain.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Customer Group Membership Changed Event

This event is fired whenever a customer is added or removed from a customer group.

The `changeType` field allows you to know what kind of change has occurred. It can be one of the following:

* `ADDED`: a customer group membership was added
* `REMOVED`: a customer group membership was removed

## Schema

[**View JSON Schema →**](https://core-api.uk.plain.com/webhooks/schema/latest.json)

Example:

<Snippet file="webhooks/customer-group-changed.mdx" />
