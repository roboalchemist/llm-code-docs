# Source: https://docs.startree.ai/thirdeye/how-tos/database/pinot-sql.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Pinot SQL as a ThirdEye Datasource

This datasource plugin is used to connect to Pinot using the [pinot-jdbc-client](https://docs.pinot.apache.org/users/clients/jdbc).

<Info>
  This datasource type is still work in progress and may not work for Pinot with ssl/tls and auth, and may also fail with some alert features.
</Info>

## Configuration

```json  theme={null}
{
  "name": "pinotDatasourceSql",
  "type": "pinot-sql",
  "properties": {
    "controllerHost": "localhost",
    "controllerPort": 9000,
    "controllerConnectionScheme": "http"
  }
}
```

Built with [Mintlify](https://mintlify.com).
