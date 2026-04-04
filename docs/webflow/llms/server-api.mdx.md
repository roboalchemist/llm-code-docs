# Source: https://developers.webflow.com/browser/custom-goals/off-site-conversions/server-api.mdx

***

title: Server-side API
slug: custom-goals/off-site-conversions/server-api
description: Send off-site conversion data to Webflow via the server-side API
hidden: false
'og:title': Server-side API
'og:description': Send off-site conversion data to Webflow via the server-side API
----------------------------------------------------------------------------------

The server-side API lets you send off-site conversion events to Webflow over HTTPS. Use this API to attribute conversions that happen outside your website (product signups, CRM actions, in-person sales) back to the optimizations visitors viewed.

<Note title="Set the user ID first">
  Before sending a server-side event, ensure you've called [`wf.setUserId()`](/browser/custom-goals/off-site-conversions/setUserId) on the client side to identify the visitor.
</Note>

## Endpoint

```
POST /event
Host: log.intellimize.co
```

## Authentication

Include your authorization token in the `Authorization` header:

```
Authorization: ApiKey ${apiKey}
```

The `apiKey` is the off-site conversion authorization token generated from the **Insights** > **Tracking Settings** page. [Click here to learn more]().

## Request format

```http
POST /event HTTP/1.1
Host: log.intellimize.co
Authorization: ApiKey ${apiKey}
Content-Type: application/json

{
    "customerId": "string",
    "eventName": "string",
    "userDomain": "string",
    "userId": "string",
    "actionId": "string",
    "actionTimestamp": number,
    "value": number
}
```

### Request body fields

| Field             | Type   | Required | Description                                                      |
| ----------------- | ------ | -------- | ---------------------------------------------------------------- |
| `customerId`      | string | Yes      | Your Analyze/Optimize Account ID (found in code preview snippet) |
| `eventName`       | string | Yes      | The Event name of the custom goal you created                    |
| `userDomain`      | string | Yes      | The domain used in `wf.setUserId()` (e.g., `salesforce`)         |
| `userId`          | string | Yes      | The user ID passed to `wf.setUserId()`                           |
| `actionId`        | string | Yes      | A unique identifier for this specific conversion                 |
| `actionTimestamp` | number | Yes      | UTC time when the conversion occurred, in UNIX milliseconds      |
| `value`           | number | No       | Optional monetary value associated with the conversion           |

## Response format

A successful request returns:

```http
HTTP/1.1 200 OK
```

## Example request

```http
POST /event HTTP/1.1
Host: log.intellimize.co
Authorization: ApiKey AbCdEf123456
Content-Type: application/json

{
    "customerId": "123456789",
    "eventName": "application-accepted",
    "userDomain": "salesforce",
    "userId": "72349876",
    "actionId": "23823940",
    "actionTimestamp": 1578316150000,
    "value": 149.99
}
```

## Testing with curl

Once your setup is complete, use a curl command to test your integration.

**On macOS/Linux:**

```bash
curl --location --request POST 'https://log.intellimize.co/event' \
--header 'Authorization: ApiKey ${apiKey}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "customerId": "your-account-id",
    "eventName": "your_custom_goal_event_name",
    "userDomain": "your-user-domain",
    "userId": "user-id-from-client-side",
    "actionId": "unique-conversion-id",
    "actionTimestamp": 1653514258136,
    "value": 149.99
}'
```

**On Windows (Command Prompt):**

Replace each backslash (`\`) with a caret (`^`).

<Note>
  If the request is successful, the command line returns the data you submitted.
</Note>

## Formatting actionTimestamp

The `actionTimestamp` field must be in **UTC** and formatted as **UNIX time in milliseconds**.

<Note title="Example">
  * UTC time: May 25, 2022 21:30:58
  * UNIX time: 1653514258136
</Note>

### Common timestamp issues

Conversions may be ignored or attributed incorrectly when:

* The timestamp is in the wrong format (must be formatted as UNIX time in milliseconds)
* The timestamp is not in UTC (if the timestamp is in local time, convert it to UTC before formatting as UNIX)
* The timestamp is after the API call is made
* The timestamp is older than 2 days

## Attribution requirements

For an off-site conversion to be attributed to an optimization, these conditions must be met:

<Steps>
  ### The eventName must match at the time of conversion

  The `eventName` in the request must exactly match the `eventName` of a custom goal that existed when the conversion occurred. Attribution won't happen if:

  * The custom goal was created after the conversion's timestamp
  * The custom goal had a different `eventName` when the conversion happened (even if renamed later)

  ### The conversion must fall within the attribution window

  * The view event (when the visitor saw the variation) must occur before the conversion timestamp
  * The conversion must happen during the same session:
    * Before the session expired due to 30 minutes of inactivity, OR
    * Before the 24-hour maximum session timeout
</Steps>

## When off-site conversions import

Off-site conversions are imported in batches each night at midnight UTC.

This means:

* Stats for the current day won't include new off-site conversions yet
* Once the nightly import runs, conversions appear with their actual timestamps
* Data for previous date ranges may change as new conversions are imported
