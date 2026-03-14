# Source: https://developer.cumul.io/guide/dashboard-embedding--generating-an-authorization-token.md

---
title: Generating an Embed token
description: Learn to securely authorize end-users by generating short-living Embed Authorization tokens server-side using an API key-token pair.
url: https://developer.luzmo.com/guide/dashboard-embedding--generating-an-authorization-token
type: guide
---

# Generate an Embed Authorization token

The first step to provide embedded resources in your application is to ensure you can securely authorize your application's end-users to access specific Luzmo resources & features, while also making sure they can only access the data they should have access to (e.g. [multi-tenancy](/guide/dashboard-embedding--generating-an-authorization-token.md)). To do so, you should use an API key-token pair of an Organization Owner and use that server-side to request short-living Embed Authorization tokens. The result of this request is an Embed key-token pair that can be used to securely access specific Luzmo content client-side: Embedded dashboards or the dashboard editor, Flex widgets, or even Luzmo IQ.

:::warning
This "Create Embed Authorization" request needs to happen **server-side**. This is for security reasons: you do not want to expose your API key & token client-side, as that would mean that users would be able to change filters or grant access to your securables (dashboard and/or datasets) themselves.

**Remember: Never use your API key and token client-side!**
:::

The API request is a _'create'_ request for an [Authorization](api/createAuthorization.md) resource. In the snippet below, fill in your API key & token, add the user's details and the resources (collections, dashboards and or datasets) you want to give access to.

:::info
Create your API key & token in Luzmo in your [profile settings]("https://app.luzmo.com/profile/api-tokens").
:::
:::langSpecific{lang=shell type=backend}

```shell
---
type: command
fileName:
switcher: true
switcherLanguage: shell
switcherType: backend
---
curl https://api.luzmo.com/0.1.0/authorization  -H "Content-Type: application/json" -d @- << EOF
{
  "action": "create",
  "version": "0.1.0",
  "key": "<your Luzmo API key>",
  "token": "<your Luzmo API token>",
  "properties": {
    "type": "embed",
    "username": "<A unique and immutable identifier for your user>",
    "name": "<username>",
    "email": "<user_email>",
    "suborganization": "<a suborganization name>",
    "access": {
      "collections": [
        {
          "id": "<collection_id>",
          "inheritRights": "use"
        }
      ],
      "datasets": [
        {
          "id": "<dataset_id>",
          "rights": "use"
        }
      ],
      "dashboards": [
        {
          "id": "<dashboard_id>",
          "rights": "use"
        }
      ]
    }
  }
}
EOF
```

:::

:::langSpecific{lang=javascript type=backend}

```javascript
---
type: file
fileName: embed.js
switcher: true
switcherLanguage: javascript
switcherType: backend
---
import Luzmo from '@luzmo/nodejs-sdk';
const client = new Luzmo({
  api_key: '<your Luzmo API key>',
  api_token: '<your Luzmo API token>',
  host: 'https://api.luzmo.com'
});


const response = await client.create('authorization',
  {
    type: "embed",
    username: "<A unique and immutable identifier for your user>",
    name: "<username>",
    email: "<user_email>",
    suborganization: "<a suborganization name>",
    access: {
      collections: [
        {
          id: "<collection_id>",
          inheritRights: "use"
        }
      ],
      datasets: [
        {
          id: "<dataset_id>",
          rights: "use"
        }
      ],
      dashboards: [
        {
          id: "<dashboard_id>",
          rights: "use"
        }
      ]
    }
  }
);
```

:::

:::langSpecific{lang=php type=backend}

```php
---
type: file
fileName: embed.php
switcher: true
switcherLanguage: php
switcherType: backend
---
<?php
require 'vendor/autoload.php';
use Luzmo\Luzmo;

$client = Luzmo::initialize(
  '<your Luzmo API key>',
  '<your Luzmo API token>',
  'https://api.luzmo.com'
);

$response = $client->create("authorization",
  array (
    'type' => "embed",
    'username' => "<A unique and immutable identifier for your user>",
    'name' => "<username>",
    'email' => "<user_email>",
    'suborganization' => "<a suborganization name>",
    'access' => array (
      'collections' => array (
        array (
          'id' => "<collection_id>",
          'inheritRights' => "use"
        )
      ),
      'datasets' => array (
        array (
          'id' => "<dataset_id>",
          'rights' => "use"
        )
      ),
      'dashboards' => array (
        array (
          'id' => "<dashboard_id>",
          'rights' => "use"
        )
      )
    )
  )
);
?>
```

:::

:::langSpecific{lang=java type=backend}

```java
---
type: file
fileName: embed.java
switcher: true
switcherLanguage: java
switcherType: backend
---
Luzmo client = new Luzmo(
  "<your Luzmo API key>",
  "<your Luzmo API token>",
  "https://api.luzmo.com"
);


JSONObject response = client.create("authorization",
  ImmutableMap.of(
    "type" , "embed",
    "username" , "<A unique and immutable identifier for your user>",
    "name" , "<username>",
    "email" , "<user_email>",
    "suborganization" , "<a suborganization name>",
    "access" , ImmutableMap.of(
      "collections" , ImmutableList.of(
        ImmutableMap.of(
          "id" , "<collection_id>",
          "inheritRights" , "use"
        )
      ),
      "datasets" , ImmutableList.of(
        ImmutableMap.of(
          "id" , "<dataset_id>",
          "rights" , "use"
        )
      ),
      "dashboards" , ImmutableList.of(
        ImmutableMap.of(
          "id" , "<dashboard_id>",
          "rights" , "use"
        )
      )
    )
  )
);
```

:::

:::langSpecific{lang=csharp type=backend}

```csharp
---
type: file
fileName: embed.net
switcher: true
switcherLanguage: csharp
switcherType: backend
---
Luzmo client = new Luzmo(
  "<your Luzmo API key>",
  "<your Luzmo API token>",
  "https://api.luzmo.com"
);

dynamic properties = new ExpandoObject();
properties.type = "embed";
properties.username = "<A unique and immutable identifier for your user>";
properties.name = "<username>";
properties.email = "<user_email>";
properties.suborganization = "<a suborganization name>";
properties.access = new {
  collections = new List<Object> {
      new {
      id = "<collection_id>",
      inheritRights = "use"
    }
    },
  datasets = new List<Object> {
      new {
      id = "<dataset_id>",
      rights = "use"
    }
    },
  dashboards = new List<Object> {
      new {
      id = "<dashboard_id>",
      rights = "use"
    }
    }
};

dynamic response = client.create("authorization", properties);
```

:::

:::langSpecific{lang=python type=backend}

```python
---
type: file
fileName: embed.py
switcher: true
switcherLanguage: python
switcherType: backend
---
from luzmo.luzmo import Luzmo
client = Luzmo(
  "<your Luzmo API key>",
  "<your Luzmo API token>",
  "https://api.luzmo.com"
)

response = client.create("authorization",
  {
    "type": "embed",
    "username": "<A unique and immutable identifier for your user>",
    "name": "<username>",
    "email": "<user_email>",
    "suborganization": "<a suborganization name>",
    "access": {
      "collections": [
        {
          "id": "<collection_id>",
          "inheritRights": "use"
        }
      ],
      "datasets": [
        {
          "id": "<dataset_id>",
          "rights": "use"
        }
      ],
      "dashboards": [
        {
          "id": "<dashboard_id>",
          "rights": "use"
        }
      ]
    }
  }
)
```

:::

Below you can find an initial list of properties you can specify here:

:::info
For a complete list of all possible properties you can specify in the Authorization request, check out [the Authorization API resource](/api/createAuthorization.md).
:::

| Property | Description |
| **type** `STRING` required | `embed` Use the value **'embed'** for the token type you're requesting. |
| **username** `STRING` required | Identifies the user uniquely and immutably. This should correspond to eg. the primary key for the user on your end. If it changes, the user will not have access to their previously created content anymore. So don't use eg. an e-mail address if those can change in your platform! This will also be used to uniquely identify a Monthly Active Viewer (MAV) or Monthly Active Designer (MAD), depending on the token's role, for your Organization. |
| **name** `STRING` required | The full name of the user (i.e. First name and Last name). This will be used in our UI. |
| **email** `STRING` required | The email address of the user. This will be used in our UI. |
| **suborganization** `STRING` | Each Embed token should be in a suborganization. The suborganization determines which other users they can see & interact with. This is typically a one-to-one mapping to your application's customer base; each end-user from a given customer would have the same `suborganization` value. If you want totally isolated users, set it to the unique username; if not specified, it will default to the `username` property of the token.<br> ⚠ If set explicitly to `null`, the token will be in your main Luzmo organization rather than a suborganization, and would thus be able to see all users for your org and all suborgs; only use this for internal embed users that should be able to e.g. create dashboards in the embedded dashboard editor and share them across suborganizations via our UI! ⚠ |
| **access** `Object` required | The access that the Embed token should have to a set of specific Dashboards and Datasets, optionally through one or more Collections. You must provide access to at least one resource. It's strongly recommended to always give the "maximum" access to resources, as some periodically triggered features (e.g. exports, alerts) make use of the access in the last requested Embed token for that end-user's "username". |
| → **collections** `OBJECT` | List of Collections that contain one or more securables (dashboards and/or datasets), to which the token should have access to. Note that the token will not have access to the Collection itself, but rather uses the Collection to access the underlying resources. If a securable is added or removed from a collection, you must generate a new token (i.e the token gets access to securables inside the collection at the time of creation). If you specify a securable in the dashboards / datasets property which is also accessible through a Collection that includes this dashboard / dataset, the more specific right is applied (i.e the right specified in the dashboards / datasets property overrides the inherited right via the Collection). |
| → → **collection_id** `UUID` | ID of the collection through which you'd like to provide access to its underlying securables (i.e. dashboards & datasets). |
| → → **inheritRights** `STRING` | The access rights the token should have to the dashboard(s) and/or dataset(s) inside the specified collection.<br> Note that the API token used to generate the embed token must have equal or higher access to the securables in the collection! If not, a warning message will be returned in the response to indicate that the embed token doesn't have access to one or more of the collection's securables.<br><br> Provides the following access to the securables inside the collection: `read`: dashboards: Can only view and interact with the dashboard and its items. datasets: Can only query the dataset in the context of an existing dashboard item. `use`: dashboards: Can view and interact with the dashboard, as well as duplicate it or create variants in the embedded editor. datasets: Can query the dataset freely (within the embed token's context). This is the minimal access required to be able to use the dataset in the embedded editor or in Luzmo Flex. `modify`: dashboards: Can view, interact, and modify this dashboard. datasets: Can modify the dataset, e.g. creating new columns, changing column types, etc. `own`: dashboards: Can view, interact, modify, share, and delete the dashboard. datasets: Can share and delete the dataset. |
| → **datasets** `OBJECT` | List of datasets the Embed token should have access to, with their individual access rights. If dataset(s) are specified which are also accessible through a specified Collection, the explicit dataset access rights specified here will override the inherited access right from the Collection. |
| → → **dataset_id** `UUID` | Id of the dataset to which the Embed token should have access to |
| → → **rights** `STRING` | The access right the embed token should have to the specified dataset. Note that the API token used to generate the embed token must have equal or higher access to the dataset!<br><br> Provides the following access to the dataset: `read`: Can only query the dataset in the context of an existing dashboard item. `use`: Can query the dataset freely (within the embed token's context). This is the minimal access required to be able to use the dataset in the embedded editor or in Luzmo Flex. `modify`: Can modify the dataset, e.g. creating new columns, changing column types, etc. `own`: Can share and delete the dataset. |
| → **dashboards** `OBJECT` | List of dashboards the token should have access to, with their individual access rights. If dashboard(s) are specified which are also accessible through a specified Collection, the explicit dashboard access rights specified here will override the inherited access right from the Collection. |
| → → **collection_id** `UUID` | ID of the dashboard to which your token should have access to |
| → → **inheritRights** `STRING` | The access rights the Embed token should have to the dashboard(s) and/or dataset(s) inside the specified collection.<br> Note that the API token used to generate the embed token must have equal or higher access to the securables in the collection! If not, a warning message will be returned in the response to indicate that the embed token doesn't have access to one or more of the collection's securables.<br><br> Provides the following access to the securables inside the collection: `read`: Can only view and interact with the dashboard and its items. `use`: Can view and interact with the dashboard, as well as duplicate it or create variants in the embedded editor. `modify`: Can view, interact, and modify this dashboard. `own`: Can view, interact, modify, share, and delete the dashboard. |
| **expiry** `DATE (RFC 3339)` | Date/time when this authorization will cease working. To promote better security practices this property is required and enforced with a maximum expiry date of 1 year. It is advised to only use short-living token for maximum security. If not specified, defaults to 24 hours from token creation. |
| **inactivity_interval** `INTEGER` | Duration of inactivity in seconds after which the token is prematurely invalidated. You can use this to invalidate tokens quickly when the session is ended (eg. all open dashboards are closed). If specified, a minimum value of 2 minutes is enforced to avoid undesired invalidation of a token due to e.g. missing a heartbeat signal sent by our server. <br> Defaults to 0 (i.e. no inactivity_interval). |
| **role** `STRING` | The role of the Embed token. Defaults to role `viewer` if not specified. This is an important property for the embedded dashboard editor:<br><br> **"viewer"**<br> Embed token should only be able to **view and interact** with one or more dashboards, variants, and duplicates.<br><br> **"designer"**<br> Embed token should be able to **create, edit, view and interact**> with one or more dashboards, variants, and duplicates.<br><br> **"owner"**<br> Embed token should be able to **create, edit, view and interact** with one or more dashboards, variants, and duplicates. Next to that, they should be able to **favorite dashboard variants for other Embed users within their suborganization.**<br><br> More info under [Embedded Dashboard Editor](/guide/dashboard-embedding--embedded-dashboard-editor.md). <br> |
This returns a JSON object with an id/token combination that you can use to securely embed Luzmo content in your application/platform:

```json
---
type: file
fileName: Response
switcher: false
---
{
  "type": "embed",
  "id": "< the embed authorization key >",
  "token": "< the embed authorization token >",
  "user_id": "< a uuid used on Luzmo's end to identify the embed user >"
  // ...
}
```


## Section Index

This reference is split into separate files. **For LLM agents**: Match the user's question to the headers below and read only the relevant sub-file(s).

### [Handling multi-tenant data](https://developer.luzmo.com/guide/dashboard-embedding--generating-an-authorization-token--handling-multi-tenant-data.md)


### [Allowing or denying access to a set of Luzmo features](https://developer.luzmo.com/guide/dashboard-embedding--generating-an-authorization-token--allowing-or-denying-access-to-a-set-of-luzmo-features.md)


### [Prematurely invalidating Embed tokens](https://developer.luzmo.com/guide/dashboard-embedding--generating-an-authorization-token--prematurely-invalidating-embed-tokens.md)



---

## Related Pages

- [Handling multi-tenant data](https://developer.luzmo.com/guide/dashboard-embedding--handling-multi-tenant-data.md): Configure Luzmo for multi-tenant data setups with dynamic row-level filtering using parameterized filters and connection overrides for secure data access.
- [Embedding dashboards](https://developer.luzmo.com/guide/dashboard-embedding--embed-into-application.md): Learn to securely embed Luzmo dashboards into your application using Embed Authorization tokens with Web, React, Angular, Vue, and React Native components.
- [Embedding the dashboard editor](https://developer.luzmo.com/guide/dashboard-embedding--embedded-dashboard-editor.md): Empower users to create and alter dashboards within your application by embedding the Luzmo dashboard editor with 'designer' or 'owner' roles.
- [Embedding AI Assistant](https://developer.luzmo.com/guide/iq--introduction.md): Luzmo IQ enables AI-powered answers to data questions. Embed a chat component for interactive queries or an answer component to display AI responses.
- [Code-first visualizations](https://developer.luzmo.com/guide/flex--introduction.md): Luzmo Flex SDK allows you to create customizable visualizations entirely from code for building powerful, hyper-personalized data analytics products.


---

## Sitemap

- [Official best practices and implementation guidelines](https://developer.luzmo.com/AGENTS.md)
- [Overview of all docs pages](https://developer.luzmo.com/llms.txt)
