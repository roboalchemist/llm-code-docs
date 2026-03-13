# Source: https://developers.kit.com/api-reference/dates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dates

> Working with dates

We return date values throughout our API. These are all returned in UTC, ISO8601 format such as: `"2023-07-17T16:48:20Z"`.

In order to make this data more user friendly, we recommend using the `timezone.utc_offset` found on the [Get current account endpoint](/api-reference/accounts/get-current-account) to convert the date to the timezone set on the Kit account level of the creator.


Built with [Mintlify](https://mintlify.com).