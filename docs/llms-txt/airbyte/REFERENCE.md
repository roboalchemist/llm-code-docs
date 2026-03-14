# Source: https://docs.airbyte.com/ai-agents/connectors/zendesk-talk/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/zendesk-support/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/zendesk-chat/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/woocommerce/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/typeform/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/twilio/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/tiktok-marketing/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/stripe/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/snapchat-marketing/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/slack/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/shopify/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/sentry/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/sendgrid/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/salesforce/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/pylon/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/pinterest/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/paypal-transaction/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/orb/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/notion/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/monday/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/mailchimp/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/linkedin-ads/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/linear/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/klaviyo/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/jira/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/intercom/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/incident-io/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/hubspot/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/harvest/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/greenhouse/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/granola/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/google-search-console/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/google-drive/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/google-analytics-data-api/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/google-ads/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/gong/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/gmail/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/gitlab/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/github/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/freshdesk/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/facebook-marketing/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/confluence/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/clickup-api/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/chargebee/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/ashby/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/asana/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/amplitude/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/amazon-seller-partner/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/amazon-ads/REFERENCE.md

# Source: https://docs.airbyte.com/ai-agents/connectors/airtable/REFERENCE.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-airtable/latest/icon.svg)

# Airtable full reference

Copy Page

This is the full reference documentation for the Airtable agent connector.

## Supported entities and actions[​](#supported-entities-and-actions "Direct link to Supported entities and actions")

The Airtable connector supports the following entities and actions.

| Entity  | Actions                                        |
| ------- | ---------------------------------------------- |
| Bases   | [List](#bases-list), [Search](#bases-search)   |
| Tables  | [List](#tables-list), [Search](#tables-search) |
| Records | [List](#records-list), [Get](#records-get)     |

## Bases[​](#bases "Direct link to Bases")

### Bases List[​](#bases-list "Direct link to Bases List")

Returns a list of all bases the user has access to

#### Python SDK[​](#python-sdk "Direct link to Python SDK")

```
await airtable.bases.list()
```

#### API[​](#api "Direct link to API")

```
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "bases",
    "action": "list"
}'
```

#### Parameters[​](#parameters "Direct link to Parameters")

| Parameter Name | Type     | Required | Description                              |
| -------------- | -------- | -------- | ---------------------------------------- |
| `offset`       | `string` | No       | Pagination offset from previous response |

**Response Schema**

#### Records[​](#records "Direct link to Records")

| Field Name        | Type             | Description |
| ----------------- | ---------------- | ----------- |
| `id`              | `string`         |             |
| `name`            | `string \| null` |             |
| `permissionLevel` | `string \| null` |             |

### Bases Search[​](#bases-search "Direct link to Bases Search")

Search and filter bases records powered by Airbyte's data sync. This often provides additional fields and operators beyond what the API natively supports, making it easier to narrow down results before performing further operations. Only available in hosted mode.

#### Python SDK[​](#python-sdk-1 "Direct link to Python SDK")

```
await airtable.bases.search(
    query={"filter": {"eq": {"id": "<str>"}}}
)
```

#### API[​](#api-1 "Direct link to API")

```
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "bases",
    "action": "search",
    "params": {
        "query": {"filter": {"eq": {"id": "<str>"}}}
    }
}'
```

#### Parameters[​](#parameters-1 "Direct link to Parameters")

| Parameter Name | Type      | Required | Description                                                                                                       |
| -------------- | --------- | -------- | ----------------------------------------------------------------------------------------------------------------- |
| `query`        | `object`  | Yes      | Filter and sort conditions. Supports operators: eq, neq, gt, gte, lt, lte, in, like, fuzzy, keyword, not, and, or |
| `query.filter` | `object`  | No       | Filter conditions                                                                                                 |
| `query.sort`   | `array`   | No       | Sort conditions                                                                                                   |
| `limit`        | `integer` | No       | Maximum results to return (default 1000)                                                                          |
| `cursor`       | `string`  | No       | Pagination cursor from previous response's `meta.cursor`                                                          |
| `fields`       | `array`   | No       | Field paths to include in results                                                                                 |

#### Searchable Fields[​](#searchable-fields "Direct link to Searchable Fields")

| Field Name        | Type     | Description                    |
| ----------------- | -------- | ------------------------------ |
| `id`              | `string` | Unique identifier for the base |
| `name`            | `string` | Name of the base               |
| `permissionLevel` | `string` | Permission level for the base  |

**Response Schema**

| Field Name               | Type             | Description                            |
| ------------------------ | ---------------- | -------------------------------------- |
| `data`                   | `array`          | List of matching records               |
| `meta`                   | `object`         | Pagination metadata                    |
| `meta.has_more`          | `boolean`        | Whether additional pages are available |
| `meta.cursor`            | `string \| null` | Cursor for next page of results        |
| `meta.took_ms`           | `number \| null` | Query execution time in milliseconds   |
| `data[].id`              | `string`         | Unique identifier for the base         |
| `data[].name`            | `string`         | Name of the base                       |
| `data[].permissionLevel` | `string`         | Permission level for the base          |

## Tables[​](#tables "Direct link to Tables")

### Tables List[​](#tables-list "Direct link to Tables List")

Returns a list of all tables in the specified base with their schema information

#### Python SDK[​](#python-sdk-2 "Direct link to Python SDK")

```
await airtable.tables.list(
    base_id="<str>"
)
```

#### API[​](#api-2 "Direct link to API")

```
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "tables",
    "action": "list",
    "params": {
        "base_id": "<str>"
    }
}'
```

#### Parameters[​](#parameters-2 "Direct link to Parameters")

| Parameter Name | Type     | Required | Description        |
| -------------- | -------- | -------- | ------------------ |
| `base_id`      | `string` | Yes      | The ID of the base |

**Response Schema**

#### Records[​](#records-1 "Direct link to Records")

| Field Name         | Type             | Description |
| ------------------ | ---------------- | ----------- |
| `id`               | `string`         |             |
| `name`             | `string \| null` |             |
| `primaryFieldId`   | `string \| null` |             |
| `fields`           | `array \| null`  |             |
| `fields[].id`      | `string \| null` |             |
| `fields[].name`    | `string \| null` |             |
| `fields[].type`    | `string \| null` |             |
| `fields[].options` | `object \| null` |             |
| `views`            | `array \| null`  |             |
| `views[].id`       | `string \| null` |             |
| `views[].name`     | `string \| null` |             |
| `views[].type`     | `string \| null` |             |

### Tables Search[​](#tables-search "Direct link to Tables Search")

Search and filter tables records powered by Airbyte's data sync. This often provides additional fields and operators beyond what the API natively supports, making it easier to narrow down results before performing further operations. Only available in hosted mode.

#### Python SDK[​](#python-sdk-3 "Direct link to Python SDK")

```
await airtable.tables.search(
    query={"filter": {"eq": {"id": "<str>"}}}
)
```

#### API[​](#api-3 "Direct link to API")

```
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "tables",
    "action": "search",
    "params": {
        "query": {"filter": {"eq": {"id": "<str>"}}}
    }
}'
```

#### Parameters[​](#parameters-3 "Direct link to Parameters")

| Parameter Name | Type      | Required | Description                                                                                                       |
| -------------- | --------- | -------- | ----------------------------------------------------------------------------------------------------------------- |
| `query`        | `object`  | Yes      | Filter and sort conditions. Supports operators: eq, neq, gt, gte, lt, lte, in, like, fuzzy, keyword, not, and, or |
| `query.filter` | `object`  | No       | Filter conditions                                                                                                 |
| `query.sort`   | `array`   | No       | Sort conditions                                                                                                   |
| `limit`        | `integer` | No       | Maximum results to return (default 1000)                                                                          |
| `cursor`       | `string`  | No       | Pagination cursor from previous response's `meta.cursor`                                                          |
| `fields`       | `array`   | No       | Field paths to include in results                                                                                 |

#### Searchable Fields[​](#searchable-fields-1 "Direct link to Searchable Fields")

| Field Name       | Type     | Description                     |
| ---------------- | -------- | ------------------------------- |
| `id`             | `string` | Unique identifier for the table |
| `name`           | `string` | Name of the table               |
| `primaryFieldId` | `string` | ID of the primary field         |
| `fields`         | `array`  | List of fields in the table     |
| `views`          | `array`  | List of views in the table      |

**Response Schema**

| Field Name              | Type             | Description                            |
| ----------------------- | ---------------- | -------------------------------------- |
| `data`                  | `array`          | List of matching records               |
| `meta`                  | `object`         | Pagination metadata                    |
| `meta.has_more`         | `boolean`        | Whether additional pages are available |
| `meta.cursor`           | `string \| null` | Cursor for next page of results        |
| `meta.took_ms`          | `number \| null` | Query execution time in milliseconds   |
| `data[].id`             | `string`         | Unique identifier for the table        |
| `data[].name`           | `string`         | Name of the table                      |
| `data[].primaryFieldId` | `string`         | ID of the primary field                |
| `data[].fields`         | `array`          | List of fields in the table            |
| `data[].views`          | `array`          | List of views in the table             |

## Records[​](#records-2 "Direct link to Records")

### Records List[​](#records-list "Direct link to Records List")

Returns a paginated list of records from the specified table

#### Python SDK[​](#python-sdk-4 "Direct link to Python SDK")

```
await airtable.records.list(
    base_id="<str>",
    table_id_or_name="<str>"
)
```

#### API[​](#api-4 "Direct link to API")

```
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "records",
    "action": "list",
    "params": {
        "base_id": "<str>",
        "table_id_or_name": "<str>"
    }
}'
```

#### Parameters[​](#parameters-4 "Direct link to Parameters")

| Parameter Name     | Type      | Required | Description                              |
| ------------------ | --------- | -------- | ---------------------------------------- |
| `base_id`          | `string`  | Yes      | The ID of the base                       |
| `table_id_or_name` | `string`  | Yes      | The ID or name of the table              |
| `offset`           | `string`  | No       | Pagination offset from previous response |
| `pageSize`         | `integer` | No       | Number of records per page (max 100)     |
| `view`             | `string`  | No       | Name or ID of a view to filter records   |
| `filterByFormula`  | `string`  | No       | Airtable formula to filter records       |
| `sort`             | `string`  | No       | Sort configuration as JSON array         |

**Response Schema**

#### Records[​](#records-3 "Direct link to Records")

| Field Name    | Type             | Description |
| ------------- | ---------------- | ----------- |
| `id`          | `string`         |             |
| `createdTime` | `string \| null` |             |
| `fields`      | `object \| null` |             |

### Records Get[​](#records-get "Direct link to Records Get")

Returns a single record by ID from the specified table

#### Python SDK[​](#python-sdk-5 "Direct link to Python SDK")

```
await airtable.records.get(
    base_id="<str>",
    table_id_or_name="<str>",
    record_id="<str>"
)
```

#### API[​](#api-5 "Direct link to API")

```
curl --location 'https://api.airbyte.ai/api/v1/integrations/connectors/{your_connector_id}/execute' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {your_auth_token}' \
--data '{
    "entity": "records",
    "action": "get",
    "params": {
        "base_id": "<str>",
        "table_id_or_name": "<str>",
        "record_id": "<str>"
    }
}'
```

#### Parameters[​](#parameters-5 "Direct link to Parameters")

| Parameter Name     | Type     | Required | Description                 |
| ------------------ | -------- | -------- | --------------------------- |
| `base_id`          | `string` | Yes      | The ID of the base          |
| `table_id_or_name` | `string` | Yes      | The ID or name of the table |
| `record_id`        | `string` | Yes      | The ID of the record        |

**Response Schema**

#### Records[​](#records-4 "Direct link to Records")

| Field Name    | Type             | Description |
| ------------- | ---------------- | ----------- |
| `id`          | `string`         |             |
| `createdTime` | `string \| null` |             |
| `fields`      | `object \| null` |             |
