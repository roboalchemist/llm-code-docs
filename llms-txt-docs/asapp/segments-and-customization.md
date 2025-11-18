# Source: https://docs.asapp.com/autosummary/structured-data/segments-and-customization.md

# Segments and Customization

> Learn how to customize the data extracted with Structured Data.

Each business has unique needs and requirement for the type of data they want to extract from their conversations.

We offer out of the box configuration for common use cases but also offer two sets of APIs to for you customize the structured data yourself:

* Create custom `structured data fields` to expand the types of data you can extract.
* Create `segments` to customize which sets of structured data are extracted for a defined type of conversation.

## Before you Begin

Before you start integrating to Custom Structured Data Fields and Segments, you need to:

* [Get your API Key Id and Secret](/getting-started/developers)
* Ensure your API key has been configured to access AutoSummary Configuration APIs. Reach out to your ASAPP team if you unsure.

## Custom Structured Data Fields

Each structured data you extract is defined by a `structured-data-field`. You would have an initial set of structured data fields set up for you by ASAPP, but you can also query and create custom structured data fields yourself.

To create a custom structured data field, you need to create a new [`structured-data-field`](/apis/configuration/structured-data-fields/create-structured-data-field) object with the following fields:

* `id`: Your unique identifier for the structured data field. Must begin with `q_` or `e_`.
* `name`: The name of the structured data field.
* `categoryId`: The category of the structured data field. Must be either **OUTCOME** or **CUSTOM**.
* `type`: The type of the structured data field. Must be either **QUESTION** or **ENTITY**.
* `question`: The question that will be answered using the context of the conversation.
* `active`: Whether the structured data field is active.

```bash  theme={null}
curl --request POST \
  --url https://api.sandbox.asapp.com/configuration/v1/structured-data-fields \
  --header 'Content-Type: application/json' \
  --header 'asapp-api-id: <api-key>' \
  --header 'asapp-api-secret: <api-key>' \
  --data '{
  "id": "q_promotion_was_offered",
  "name": "Promotion was offered",
  "categoryId": "OUTCOME",
  "type": "QUESTION",
  "question": {
    "question": "Did the agent offer the correct promotion?"
  },
  "active": true
}'
```

A successfully created structured data field will return a `200` and the newly created `structured-data-field` object in the response body.

```json  theme={null}
{
  "id": "q_promotion_was_offered",
  "name": "Promotion was offered",
  "categoryId": "OUTCOME",
  "type": "QUESTION",
  "question": {
    "question": "Did the agent offer the correct promotion?"
  },
  "active": true
}
```

<Note>
  An inactive structured data field will not be extracted from conversations.
</Note>

You can then use the structured data field id to create a segment.

## Segments

Segments are used to configure which sets of structured data fields are extracted for a defined type of conversation. Segments are defined by two parts:

* A **query** that matches against the conversation metadata and intent.
* A list of **structured data field ids** that are included in the segment.

When you generate structured data for a conversation, the system follows these steps:

1. Checks the conversation against the queries of all segments
2. For each matching query:
   * Extracts the structured data fields defined in that segment
3. If multiple segments match:
   * Combines and extracts all structured data fields from all matching segments

<Note>
  By default, there is a [**GLOBAL** segment](#global-segment) that represents the initially configured structured data fields with a query that matches TRUE on any conversation.
</Note>

Most companies will want to create custom segments to extract structured data fields for specific types of conversations, such as a support call involving a specific product or service, or types of sales calls.

### Create a new segment

To create a new segment, you need to create a new [`segment`](/apis/configuration/segments/create-segment) object with the following fields:

* `id`: Your unique identifier for the segment.
* `name`: The name of the segment.
* `query`: The [query](#query) that defines which conversations are included in the segment.
* `structuredDataFieldIds`: The list of structured data field ids that are included in the segment.

```bash  theme={null}
curl --request POST \
  --url https://api.sandbox.asapp.com/configuration/v1/segments \
  --header 'Content-Type: application/json' \
  --header 'asapp-api-id: <api-key>' \
  --header 'asapp-api-secret: <api-key>' \
  --data '{
  "id": "USER_SUPPORT",
  "name": "Support",
  "query": {
    "type": "raw",
    "raw": "TRUE"
  },
  "structuredDataFieldIds": [
    "q_promotion_was_offered",
    "e_promotion_details"
  ]
}'
```

A successfully created segment will return a 200 and the newly created segment object in the response body.

```json  theme={null}
{
  "id": "USER_SUPPORT",
  "name": "Support",
  "query": {
    "type": "raw",
    "raw": "TRUE"
  },
  "structuredDataFieldIds": [
    "q_promotion_was_offered",
    "e_promotion_details"
  ]
}
```

### Query

The segments query defines rules for when a segment should be applied to a conversation. We currently only support a query type of `raw` that uses a SQL-like syntax with a focused set of operators for clear and precise matching.

The query language supports these key elements:

**Logical Operators**

* `AND`, `OR`, `NOT` - Combine conditions
* Parentheses `()` for grouping and precedence

**Field Comparisons**

* Equality: `field = 'value'`
* List membership: `field IN ['value1', 'value2']`

#### Available Fields

The data you can query against is the conversation metadata as uploaded as part of [metadata ingestion](/reporting/metadata-ingestion).

Specifically, you can query against the following fields:

**Conversation Metadata**

| Field                | Description                                                                                                                                                                            |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| lob\_id              | Line of business identifier                                                                                                                                                            |
| lob\_name            | Line of business name                                                                                                                                                                  |
| group\_id            | Group identifier                                                                                                                                                                       |
| group\_name          | Group name                                                                                                                                                                             |
| agent\_routing\_code | Agent's routing attribute                                                                                                                                                              |
| campaign             | Activities related to the issue                                                                                                                                                        |
| device\_type         | Client's device type (TABLET, PHONE, DESKTOP, WATCH, OTHER)                                                                                                                            |
| platform             | Client's platform type (SMS, WEB, IOS, ANDROID, APP, LOCAL, VOICE, VOICE\_IOS, VOICE\_ANDROID, VOICE\_ECHO, VOICE\_HOMEPOD, VOICE\_GGLHOME, VOICE\_WEB, APPLEBIZ, GOOGLEBIZ, GBM, WAB) |
| company\_segment     | Company's segment(s) that the issue belongs to                                                                                                                                         |
| company\_subdivision | Company's subdivision that the issue belongs to                                                                                                                                        |
| business\_rule       | Business rule to use                                                                                                                                                                   |
| entry\_type          | Way the issue started and created in the system                                                                                                                                        |
| operating\_system    | Operating system used to enter the issue (MAC\_OS, LINUX, WINDOWS, ANDROID, IOS, OTHER)                                                                                                |
| browser\_type        | Browser type used                                                                                                                                                                      |
| browser\_version     | Browser version used                                                                                                                                                                   |

**Conversation Intent**

| Field        | Description       |
| ------------ | ----------------- |
| intent\_code | Intent identifier |
| intent\_name | Intent name       |

#### Query Examples

Here are some examples of how queries can be constructed for different types of conversations.

Note that the field values used in these examples are arbitrary and for illustration purposes only. You will need to construct queries using your actual metadata fields and values based on your business needs.

<AccordionGroup>
  <Accordion title="Match conversations for mobile products AND the iOS platform">
    ```sql  theme={null}
    group_id IN ['mobile_support', 'mobile_tech'] AND platform = 'ios'
    ```
  </Accordion>

  <Accordion title="Match conversations for up-sell and cross-sell opportunities">
    ```sql  theme={null}
    intent_code IN ['UPGRADE_INQUIRY', 'ADDITIONAL_SERVICE', 'PREMIUM_FEATURES'] 
    AND company_subdivision = 'inside_sales'
    ```
  </Accordion>

  <Accordion title="Match high-priority complaints">
    ```sql  theme={null}
    intent_code = 'COMPLAINT' AND campaign = 'holiday_season' AND business_rule = 'high_priority'
    ```
  </Accordion>

  <Accordion title="Match billing conversations for wireless and broadband services">
    ```sql  theme={null}
    intent_code = 'BILLING' AND lob_id IN ['wireless_service', 'broadband_service']
    ```
  </Accordion>
</AccordionGroup>

### Global Segment

The **GLOBAL** segment is a special segment that matches all conversations. It is automatically created when you first configure your structured data fields.

You can update the **GLOBAL** segment to include new structured data fields or modify the query to change the criteria for matching conversations.

We recommend that once you start creating custom segments, you update the **GLOBAL** segment to remove the structured data fields and rely on the custom segments to extract structured data.
