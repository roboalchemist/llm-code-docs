# Source: https://clickhouse.ferndocs.com/cloud/manage/openapi.md

---
sidebar_label: Managing API keys
slug: /cloud/manage/openapi
title: Managing API Keys
description: >-
  ClickHouse Cloud provides an API utilizing OpenAPI that allows you to
  programmatically manage your account and aspects of your services.
doc_type: guide
keywords:

- api
- openapi
- rest api
- documentation
- cloud management

---

ClickHouse Cloud provides an API utilizing OpenAPI that allows you to programmatically manage your account and aspects of your services.

<Note>
This document covers the ClickHouse Cloud API. For database API endpoints, please see [Cloud Endpoints API](/cloud/get-started/query-endpoints)
</Note>

1. You can use the **API Keys** tab on the left menu to create and manage your API keys.

  <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/70d3933d64ac346f4db597611e34795d4caedce27514d1e04e48757bb61c9e8e/images/cloud/manage/openapi1.png" alt="API Keys tab"/>

1. The **API Keys** page will initially display a prompt to create your first API key as shown below. After your first key is created, you can create new keys using the `New API Key` button that appears in the top right corner.

  <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/325ad9b622e3fc25dc4decc9f502d38b6c13e4a8b6b5e5a2366d3f50ad3adfdf/images/cloud/manage/openapi2.png" alt="API Keys page"/>
  
1. To create an API key, specify the key name, permissions for the key, and expiration time, then click `Generate API Key`.
<br/>

<Note>
Permissions align with ClickHouse Cloud [predefined roles](/cloud/security/console-roles). The developer role has read-only permissions for assigned services and the admin role has full read and write permissions.
</Note>

  <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/5659f8415d0887b37df3a4e1a2ab6995583e4999da14544cd186488329f73b07/images/cloud/manage/openapi3.png" alt="Create API key form"/>

1. The next screen will display your Key ID and Key secret. Copy these values and put them somewhere safe, such as a vault. The values will not be displayed after you leave this screen.

  <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/e93cf012fde304f8c096088b1133f5267864be5579fffbc405089c0a68a61276/images/cloud/manage/openapi4.png" alt="API key details"/>

1. The ClickHouse Cloud API uses [HTTP Basic Authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication) to verify the validity of your API keys. Here is an example of how to use your API keys to send requests to the ClickHouse Cloud API using `curl`:

```bash
KEY_ID=mykeyid
KEY_SECRET=mykeysecret

curl --user $KEY_ID:$KEY_SECRET https://api.clickhouse.cloud/v1/organizations
```

1. Returning to the **API Keys** page, you will see the key name, last four characters of the Key ID, permissions, status, expiration date, and creator. You are able to edit the key name, permissions, and expiration from this screen. Keys may also be disabled or deleted form this screen.
<br/>

<Note>
Deleting an API key is a permanent action. Any services using the key will immediately lose access to ClickHouse Cloud.
</Note>

  <img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/a976e6fcc34c156133a05a7873e90ee04a99faa4a9e2bcd2561586a6405017cf/images/cloud/manage/openapi5.png" alt="API Keys management page"/>

## Endpoints [#endpoints]

Refer details on endpoints, refer to the [API reference](https://clickhouse.com/docs/cloud/manage/api/swagger).
Use your API Key and API Secret with the base URL `https://api.clickhouse.cloud/v1`.
