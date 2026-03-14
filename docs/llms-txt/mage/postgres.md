# Source: https://docs.mage.ai/guides/streaming/destinations/postgres.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Postgres

## Basic config

```yaml  theme={"system"}
connector_type: postgres
database: database
host: host
password: password
port: 5432
schema: schema
username: username
table: table
```

## Upsert record

To upsert records to Postgres, you can define `unique_conflict_method` and `unique_constraints` params
in the config.

```yaml  theme={"system"}
unique_conflict_method: UPDATE
unique_constraints:
- col1
- col2
allow_reserved_words: False
auto_clean_name: True
case_sensitive: False
```


Built with [Mintlify](https://mintlify.com).