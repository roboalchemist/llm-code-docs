# Source: https://docs.datadoghq.com/api/latest/organizations.md

---
title: Organizations
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Organizations
---

# Organizations

Create, edit, and manage your organizations. Read more about [multi-org accounts](https://docs.datadoghq.com/account_management/multi_organization).

## Create a child organization{% #create-a-child-organization %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                  |
| ----------------- | --------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/org |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/org |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/org      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/org      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/org     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/org |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/org |

### Overview



Create a child organization.

This endpoint requires the [multi-organization account](https://docs.datadoghq.com/account_management/multi_organization/) feature and must be enabled by [contacting support](https://docs.datadoghq.com/help/).

Once a new child organization is created, you can interact with it by using the `org.public_id`, `api_key.key`, and `application_key.hash` provided in the response.
This endpoint requires the `org_management` permission.


### Request

#### Body Data (required)

Organization object that needs to be created

{% tab title="Model" %}

| Parent field | Field                  | Type   | Description                                                            |
| ------------ | ---------------------- | ------ | ---------------------------------------------------------------------- |
|              | billing                | object | **DEPRECATED**: A JSON array of billing type.                          |
| billing      | type                   | string | The type of billing. Only `parent_billing` is supported.               |
|              | name [*required*] | string | The name of the new child-organization, limited to 32 characters.      |
|              | subscription           | object | **DEPRECATED**: Subscription definition.                               |
| subscription | type                   | string | The subscription type. Types available are `trial`, `free`, and `pro`. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "billing": {
    "type": "string"
  },
  "name": "New child org",
  "subscription": {
    "type": "string"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object for an organization creation.

| Parent field                  | Field                         | Type     | Description                                                                                                                                                                                               |
| ----------------------------- | ----------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                               | api_key                       | object   | Datadog API key.                                                                                                                                                                                          |
| api_key                       | created                       | string   | Date of creation of the API key.                                                                                                                                                                          |
| api_key                       | created_by                    | string   | Datadog user handle that created the API key.                                                                                                                                                             |
| api_key                       | key                           | string   | API key.                                                                                                                                                                                                  |
| api_key                       | name                          | string   | Name of your API key.                                                                                                                                                                                     |
|                               | application_key               | object   | An application key with its associated metadata.                                                                                                                                                          |
| application_key               | hash                          | string   | Hash of an application key.                                                                                                                                                                               |
| application_key               | name                          | string   | Name of an application key.                                                                                                                                                                               |
| application_key               | owner                         | string   | Owner of an application key.                                                                                                                                                                              |
|                               | org                           | object   | Create, edit, and manage organizations.                                                                                                                                                                   |
| org                           | billing                       | object   | **DEPRECATED**: A JSON array of billing type.                                                                                                                                                             |
| billing                       | type                          | string   | The type of billing. Only `parent_billing` is supported.                                                                                                                                                  |
| org                           | created                       | string   | Date of the organization creation.                                                                                                                                                                        |
| org                           | description                   | string   | Description of the organization.                                                                                                                                                                          |
| org                           | name                          | string   | The name of the child organization, limited to 32 characters.                                                                                                                                             |
| org                           | public_id                     | string   | The `public_id` of the organization you are operating within.                                                                                                                                             |
| org                           | settings                      | object   | A JSON array of settings.                                                                                                                                                                                 |
| settings                      | private_widget_share          | boolean  | Whether or not the organization users can share widgets outside of Datadog.                                                                                                                               |
| settings                      | saml                          | object   | Set the boolean property enabled to enable or disable single sign on with SAML. See the SAML documentation for more information about all SAML settings.                                                  |
| saml                          | enabled                       | boolean  | Whether or not SAML is enabled for this organization.                                                                                                                                                     |
| settings                      | saml_autocreate_access_role   | enum     | The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR`                                                 |
| settings                      | saml_autocreate_users_domains | object   | Has two properties, `enabled` (boolean) and `domains`, which is a list of domains without the @ symbol.                                                                                                   |
| saml_autocreate_users_domains | domains                       | [string] | List of domains where the SAML automated user creation is enabled.                                                                                                                                        |
| saml_autocreate_users_domains | enabled                       | boolean  | Whether or not the automated user creation based on SAML domain is enabled.                                                                                                                               |
| settings                      | saml_can_be_enabled           | boolean  | Whether or not SAML can be enabled for this organization.                                                                                                                                                 |
| settings                      | saml_idp_endpoint             | string   | Identity provider endpoint for SAML authentication.                                                                                                                                                       |
| settings                      | saml_idp_initiated_login      | object   | Has one property enabled (boolean).                                                                                                                                                                       |
| saml_idp_initiated_login      | enabled                       | boolean  | Whether SAML IdP initiated login is enabled, learn more in the [SAML documentation](https://docs.datadoghq.com/account_management/saml/#idp-initiated-login).                                             |
| settings                      | saml_idp_metadata_uploaded    | boolean  | Whether or not a SAML identity provider metadata file was provided to the Datadog organization.                                                                                                           |
| settings                      | saml_login_url                | string   | URL for SAML logging.                                                                                                                                                                                     |
| settings                      | saml_strict_mode              | object   | Has one property enabled (boolean).                                                                                                                                                                       |
| saml_strict_mode              | enabled                       | boolean  | Whether or not the SAML strict mode is enabled. If true, all users must log in with SAML. Learn more on the [SAML Strict documentation](https://docs.datadoghq.com/account_management/saml/#saml-strict). |
| org                           | subscription                  | object   | **DEPRECATED**: Subscription definition.                                                                                                                                                                  |
| subscription                  | type                          | string   | The subscription type. Types available are `trial`, `free`, and `pro`.                                                                                                                                    |
| org                           | trial                         | boolean  | Only available for MSP customers. Allows child organizations to be created on a trial plan.                                                                                                               |
|                               | user                          | object   | Create, edit, and disable users.                                                                                                                                                                          |
| user                          | access_role                   | enum     | The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR`                                                 |
| user                          | disabled                      | boolean  | The new disabled status of the user.                                                                                                                                                                      |
| user                          | email                         | string   | The new email of the user.                                                                                                                                                                                |
| user                          | handle                        | string   | The user handle, must be a valid email.                                                                                                                                                                   |
| user                          | icon                          | string   | Gravatar icon associated to the user.                                                                                                                                                                     |
| user                          | name                          | string   | The name of the user.                                                                                                                                                                                     |
| user                          | verified                      | boolean  | Whether or not the user logged in Datadog at least once.                                                                                                                                                  |

{% /tab %}

{% tab title="Example" %}

```json
{
  "api_key": {
    "created": "2019-08-02 15:31:07",
    "created_by": "john@example.com",
    "key": "1234512345123456abcabc912349abcd",
    "name": "example user"
  },
  "application_key": {
    "hash": "1234512345123459cda4eb9ced49a3d84fd0138c",
    "name": "example user",
    "owner": "example.com"
  },
  "org": {
    "billing": {
      "type": "string"
    },
    "created": "2019-09-26T17:28:28Z",
    "description": "some description",
    "name": "New child org",
    "public_id": "abcdef12345",
    "settings": {
      "private_widget_share": false,
      "saml": {
        "enabled": false
      },
      "saml_autocreate_access_role": "ro",
      "saml_autocreate_users_domains": {
        "domains": [
          "example.com"
        ],
        "enabled": false
      },
      "saml_can_be_enabled": false,
      "saml_idp_endpoint": "https://my.saml.endpoint",
      "saml_idp_initiated_login": {
        "enabled": false
      },
      "saml_idp_metadata_uploaded": false,
      "saml_login_url": "https://my.saml.login.url",
      "saml_strict_mode": {
        "enabled": false
      }
    },
    "subscription": {
      "type": "string"
    },
    "trial": false
  },
  "user": {
    "access_role": "ro",
    "disabled": false,
    "email": "test@datadoghq.com",
    "handle": "test@datadoghq.com",
    "icon": "/path/to/matching/gravatar/icon",
    "name": "test user",
    "verified": true
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/org" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "name": "New child org"
}
EOF

#####

```python
"""
Create a child organization returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.organizations_api import OrganizationsApi
from datadog_api_client.v1.model.organization_billing import OrganizationBilling
from datadog_api_client.v1.model.organization_create_body import OrganizationCreateBody
from datadog_api_client.v1.model.organization_subscription import OrganizationSubscription

body = OrganizationCreateBody(
    billing=OrganizationBilling(
        type="parent_billing",
    ),
    name="New child org",
    subscription=OrganizationSubscription(
        type="pro",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    response = api_instance.create_child_org(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Create a child organization returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::OrganizationsAPI.new

body = DatadogAPIClient::V1::OrganizationCreateBody.new({
  billing: DatadogAPIClient::V1::OrganizationBilling.new({
    type: "parent_billing",
  }),
  name: "New child org",
  subscription: DatadogAPIClient::V1::OrganizationSubscription.new({
    type: "pro",
  }),
})
p api_instance.create_child_org(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Create a child organization returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    body := datadogV1.OrganizationCreateBody{
        Billing: &datadogV1.OrganizationBilling{
            Type: datadog.PtrString("parent_billing"),
        },
        Name: "New child org",
        Subscription: &datadogV1.OrganizationSubscription{
            Type: datadog.PtrString("pro"),
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewOrganizationsApi(apiClient)
    resp, r, err := api.CreateChildOrg(ctx, body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `OrganizationsApi.CreateChildOrg`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `OrganizationsApi.CreateChildOrg`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Create a child organization returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.OrganizationsApi;
import com.datadog.api.client.v1.model.OrganizationBilling;
import com.datadog.api.client.v1.model.OrganizationCreateBody;
import com.datadog.api.client.v1.model.OrganizationCreateResponse;
import com.datadog.api.client.v1.model.OrganizationSubscription;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);

    OrganizationCreateBody body =
        new OrganizationCreateBody()
            .billing(new OrganizationBilling().type("parent_billing"))
            .name("New child org")
            .subscription(new OrganizationSubscription().type("pro"));

    try {
      OrganizationCreateResponse result = apiInstance.createChildOrg(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#createChildOrg");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// Create a child organization returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_organizations::OrganizationsAPI;
use datadog_api_client::datadogV1::model::OrganizationBilling;
use datadog_api_client::datadogV1::model::OrganizationCreateBody;
use datadog_api_client::datadogV1::model::OrganizationSubscription;

#[tokio::main]
async fn main() {
    let body = OrganizationCreateBody::new("New child org".to_string())
        .billing(OrganizationBilling::new().type_("parent_billing".to_string()))
        .subscription(OrganizationSubscription::new().type_("pro".to_string()));
    let configuration = datadog::Configuration::new();
    let api = OrganizationsAPI::with_config(configuration);
    let resp = api.create_child_org(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Create a child organization returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.OrganizationsApi(configuration);

const params: v1.OrganizationsApiCreateChildOrgRequest = {
  body: {
    billing: {
      type: "parent_billing",
    },
    name: "New child org",
    subscription: {
      type: "pro",
    },
  },
};

apiInstance
  .createChildOrg(params)
  .then((data: v1.OrganizationCreateResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## List your managed organizations{% #list-your-managed-organizations %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                 |
| ----------------- | -------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/org |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/org |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/org      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/org      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/org     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/org |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/org |

### Overview

This endpoint returns data on your top-level organization. This endpoint requires the `org_management` permission.

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with the list of organizations.

| Parent field                  | Field                         | Type     | Description                                                                                                                                                                                               |
| ----------------------------- | ----------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                               | orgs                          | [object] | Array of organization objects.                                                                                                                                                                            |
| orgs                          | billing                       | object   | **DEPRECATED**: A JSON array of billing type.                                                                                                                                                             |
| billing                       | type                          | string   | The type of billing. Only `parent_billing` is supported.                                                                                                                                                  |
| orgs                          | created                       | string   | Date of the organization creation.                                                                                                                                                                        |
| orgs                          | description                   | string   | Description of the organization.                                                                                                                                                                          |
| orgs                          | name                          | string   | The name of the child organization, limited to 32 characters.                                                                                                                                             |
| orgs                          | public_id                     | string   | The `public_id` of the organization you are operating within.                                                                                                                                             |
| orgs                          | settings                      | object   | A JSON array of settings.                                                                                                                                                                                 |
| settings                      | private_widget_share          | boolean  | Whether or not the organization users can share widgets outside of Datadog.                                                                                                                               |
| settings                      | saml                          | object   | Set the boolean property enabled to enable or disable single sign on with SAML. See the SAML documentation for more information about all SAML settings.                                                  |
| saml                          | enabled                       | boolean  | Whether or not SAML is enabled for this organization.                                                                                                                                                     |
| settings                      | saml_autocreate_access_role   | enum     | The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR`                                                 |
| settings                      | saml_autocreate_users_domains | object   | Has two properties, `enabled` (boolean) and `domains`, which is a list of domains without the @ symbol.                                                                                                   |
| saml_autocreate_users_domains | domains                       | [string] | List of domains where the SAML automated user creation is enabled.                                                                                                                                        |
| saml_autocreate_users_domains | enabled                       | boolean  | Whether or not the automated user creation based on SAML domain is enabled.                                                                                                                               |
| settings                      | saml_can_be_enabled           | boolean  | Whether or not SAML can be enabled for this organization.                                                                                                                                                 |
| settings                      | saml_idp_endpoint             | string   | Identity provider endpoint for SAML authentication.                                                                                                                                                       |
| settings                      | saml_idp_initiated_login      | object   | Has one property enabled (boolean).                                                                                                                                                                       |
| saml_idp_initiated_login      | enabled                       | boolean  | Whether SAML IdP initiated login is enabled, learn more in the [SAML documentation](https://docs.datadoghq.com/account_management/saml/#idp-initiated-login).                                             |
| settings                      | saml_idp_metadata_uploaded    | boolean  | Whether or not a SAML identity provider metadata file was provided to the Datadog organization.                                                                                                           |
| settings                      | saml_login_url                | string   | URL for SAML logging.                                                                                                                                                                                     |
| settings                      | saml_strict_mode              | object   | Has one property enabled (boolean).                                                                                                                                                                       |
| saml_strict_mode              | enabled                       | boolean  | Whether or not the SAML strict mode is enabled. If true, all users must log in with SAML. Learn more on the [SAML Strict documentation](https://docs.datadoghq.com/account_management/saml/#saml-strict). |
| orgs                          | subscription                  | object   | **DEPRECATED**: Subscription definition.                                                                                                                                                                  |
| subscription                  | type                          | string   | The subscription type. Types available are `trial`, `free`, and `pro`.                                                                                                                                    |
| orgs                          | trial                         | boolean  | Only available for MSP customers. Allows child organizations to be created on a trial plan.                                                                                                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "orgs": [
    {
      "billing": {
        "type": "string"
      },
      "created": "2019-09-26T17:28:28Z",
      "description": "some description",
      "name": "New child org",
      "public_id": "abcdef12345",
      "settings": {
        "private_widget_share": false,
        "saml": {
          "enabled": false
        },
        "saml_autocreate_access_role": "ro",
        "saml_autocreate_users_domains": {
          "domains": [
            "example.com"
          ],
          "enabled": false
        },
        "saml_can_be_enabled": false,
        "saml_idp_endpoint": "https://my.saml.endpoint",
        "saml_idp_initiated_login": {
          "enabled": false
        },
        "saml_idp_metadata_uploaded": false,
        "saml_login_url": "https://my.saml.login.url",
        "saml_strict_mode": {
          "enabled": false
        }
      },
      "subscription": {
        "type": "string"
      },
      "trial": false
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/org" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List your managed organizations returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.organizations_api import OrganizationsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    response = api_instance.list_orgs()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# List your managed organizations returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::OrganizationsAPI.new
p api_instance.list_orgs()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// List your managed organizations returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewOrganizationsApi(apiClient)
    resp, r, err := api.ListOrgs(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `OrganizationsApi.ListOrgs`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `OrganizationsApi.ListOrgs`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// List your managed organizations returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.OrganizationsApi;
import com.datadog.api.client.v1.model.OrganizationListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);

    try {
      OrganizationListResponse result = apiInstance.listOrgs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#listOrgs");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// List your managed organizations returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_organizations::OrganizationsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = OrganizationsAPI::with_config(configuration);
    let resp = api.list_orgs().await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * List your managed organizations returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.OrganizationsApi(configuration);

apiInstance
  .listOrgs()
  .then((data: v1.OrganizationListResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get organization information{% #get-organization-information %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                             |
| ----------------- | -------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v1/org/{public_id} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v1/org/{public_id} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v1/org/{public_id}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v1/org/{public_id}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v1/org/{public_id}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v1/org/{public_id} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v1/org/{public_id} |

### Overview

Get organization information.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                                                   |
| --------------------------- | ------ | ------------------------------------------------------------- |
| public_id [*required*] | string | The `public_id` of the organization you are operating within. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with an organization.

| Parent field                  | Field                         | Type     | Description                                                                                                                                                                                               |
| ----------------------------- | ----------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                               | org                           | object   | Create, edit, and manage organizations.                                                                                                                                                                   |
| org                           | billing                       | object   | **DEPRECATED**: A JSON array of billing type.                                                                                                                                                             |
| billing                       | type                          | string   | The type of billing. Only `parent_billing` is supported.                                                                                                                                                  |
| org                           | created                       | string   | Date of the organization creation.                                                                                                                                                                        |
| org                           | description                   | string   | Description of the organization.                                                                                                                                                                          |
| org                           | name                          | string   | The name of the child organization, limited to 32 characters.                                                                                                                                             |
| org                           | public_id                     | string   | The `public_id` of the organization you are operating within.                                                                                                                                             |
| org                           | settings                      | object   | A JSON array of settings.                                                                                                                                                                                 |
| settings                      | private_widget_share          | boolean  | Whether or not the organization users can share widgets outside of Datadog.                                                                                                                               |
| settings                      | saml                          | object   | Set the boolean property enabled to enable or disable single sign on with SAML. See the SAML documentation for more information about all SAML settings.                                                  |
| saml                          | enabled                       | boolean  | Whether or not SAML is enabled for this organization.                                                                                                                                                     |
| settings                      | saml_autocreate_access_role   | enum     | The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR`                                                 |
| settings                      | saml_autocreate_users_domains | object   | Has two properties, `enabled` (boolean) and `domains`, which is a list of domains without the @ symbol.                                                                                                   |
| saml_autocreate_users_domains | domains                       | [string] | List of domains where the SAML automated user creation is enabled.                                                                                                                                        |
| saml_autocreate_users_domains | enabled                       | boolean  | Whether or not the automated user creation based on SAML domain is enabled.                                                                                                                               |
| settings                      | saml_can_be_enabled           | boolean  | Whether or not SAML can be enabled for this organization.                                                                                                                                                 |
| settings                      | saml_idp_endpoint             | string   | Identity provider endpoint for SAML authentication.                                                                                                                                                       |
| settings                      | saml_idp_initiated_login      | object   | Has one property enabled (boolean).                                                                                                                                                                       |
| saml_idp_initiated_login      | enabled                       | boolean  | Whether SAML IdP initiated login is enabled, learn more in the [SAML documentation](https://docs.datadoghq.com/account_management/saml/#idp-initiated-login).                                             |
| settings                      | saml_idp_metadata_uploaded    | boolean  | Whether or not a SAML identity provider metadata file was provided to the Datadog organization.                                                                                                           |
| settings                      | saml_login_url                | string   | URL for SAML logging.                                                                                                                                                                                     |
| settings                      | saml_strict_mode              | object   | Has one property enabled (boolean).                                                                                                                                                                       |
| saml_strict_mode              | enabled                       | boolean  | Whether or not the SAML strict mode is enabled. If true, all users must log in with SAML. Learn more on the [SAML Strict documentation](https://docs.datadoghq.com/account_management/saml/#saml-strict). |
| org                           | subscription                  | object   | **DEPRECATED**: Subscription definition.                                                                                                                                                                  |
| subscription                  | type                          | string   | The subscription type. Types available are `trial`, `free`, and `pro`.                                                                                                                                    |
| org                           | trial                         | boolean  | Only available for MSP customers. Allows child organizations to be created on a trial plan.                                                                                                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "org": {
    "billing": {
      "type": "string"
    },
    "created": "2019-09-26T17:28:28Z",
    "description": "some description",
    "name": "New child org",
    "public_id": "abcdef12345",
    "settings": {
      "private_widget_share": false,
      "saml": {
        "enabled": false
      },
      "saml_autocreate_access_role": "ro",
      "saml_autocreate_users_domains": {
        "domains": [
          "example.com"
        ],
        "enabled": false
      },
      "saml_can_be_enabled": false,
      "saml_idp_endpoint": "https://my.saml.endpoint",
      "saml_idp_initiated_login": {
        "enabled": false
      },
      "saml_idp_metadata_uploaded": false,
      "saml_login_url": "https://my.saml.login.url",
      "saml_strict_mode": {
        "enabled": false
      }
    },
    "subscription": {
      "type": "string"
    },
    "trial": false
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport public_id="abc123"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/org/${public_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get organization information returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.organizations_api import OrganizationsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    response = api_instance.get_org(
        public_id="abc123",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get organization information returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::OrganizationsAPI.new
p api_instance.get_org("abc123")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get organization information returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewOrganizationsApi(apiClient)
    resp, r, err := api.GetOrg(ctx, "abc123")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `OrganizationsApi.GetOrg`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `OrganizationsApi.GetOrg`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get organization information returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.OrganizationsApi;
import com.datadog.api.client.v1.model.OrganizationResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);

    try {
      OrganizationResponse result = apiInstance.getOrg("abc123");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#getOrg");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// Get organization information returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_organizations::OrganizationsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = OrganizationsAPI::with_config(configuration);
    let resp = api.get_org("abc123".to_string()).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Get organization information returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.OrganizationsApi(configuration);

const params: v1.OrganizationsApiGetOrgRequest = {
  publicId: "abc123",
};

apiInstance
  .getOrg(params)
  .then((data: v1.OrganizationResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Update your organization{% #update-your-organization %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                             |
| ----------------- | -------------------------------------------------------- |
| ap1.datadoghq.com | PUT https://api.ap1.datadoghq.com/api/v1/org/{public_id} |
| ap2.datadoghq.com | PUT https://api.ap2.datadoghq.com/api/v1/org/{public_id} |
| app.datadoghq.eu  | PUT https://api.datadoghq.eu/api/v1/org/{public_id}      |
| app.ddog-gov.com  | PUT https://api.ddog-gov.com/api/v1/org/{public_id}      |
| app.datadoghq.com | PUT https://api.datadoghq.com/api/v1/org/{public_id}     |
| us3.datadoghq.com | PUT https://api.us3.datadoghq.com/api/v1/org/{public_id} |
| us5.datadoghq.com | PUT https://api.us5.datadoghq.com/api/v1/org/{public_id} |

### Overview

Update your organization.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                                                   |
| --------------------------- | ------ | ------------------------------------------------------------- |
| public_id [*required*] | string | The `public_id` of the organization you are operating within. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field                  | Field                         | Type     | Description                                                                                                                                                                                               |
| ----------------------------- | ----------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                               | billing                       | object   | **DEPRECATED**: A JSON array of billing type.                                                                                                                                                             |
| billing                       | type                          | string   | The type of billing. Only `parent_billing` is supported.                                                                                                                                                  |
|                               | created                       | string   | Date of the organization creation.                                                                                                                                                                        |
|                               | description                   | string   | Description of the organization.                                                                                                                                                                          |
|                               | name                          | string   | The name of the child organization, limited to 32 characters.                                                                                                                                             |
|                               | public_id                     | string   | The `public_id` of the organization you are operating within.                                                                                                                                             |
|                               | settings                      | object   | A JSON array of settings.                                                                                                                                                                                 |
| settings                      | private_widget_share          | boolean  | Whether or not the organization users can share widgets outside of Datadog.                                                                                                                               |
| settings                      | saml                          | object   | Set the boolean property enabled to enable or disable single sign on with SAML. See the SAML documentation for more information about all SAML settings.                                                  |
| saml                          | enabled                       | boolean  | Whether or not SAML is enabled for this organization.                                                                                                                                                     |
| settings                      | saml_autocreate_access_role   | enum     | The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR`                                                 |
| settings                      | saml_autocreate_users_domains | object   | Has two properties, `enabled` (boolean) and `domains`, which is a list of domains without the @ symbol.                                                                                                   |
| saml_autocreate_users_domains | domains                       | [string] | List of domains where the SAML automated user creation is enabled.                                                                                                                                        |
| saml_autocreate_users_domains | enabled                       | boolean  | Whether or not the automated user creation based on SAML domain is enabled.                                                                                                                               |
| settings                      | saml_can_be_enabled           | boolean  | Whether or not SAML can be enabled for this organization.                                                                                                                                                 |
| settings                      | saml_idp_endpoint             | string   | Identity provider endpoint for SAML authentication.                                                                                                                                                       |
| settings                      | saml_idp_initiated_login      | object   | Has one property enabled (boolean).                                                                                                                                                                       |
| saml_idp_initiated_login      | enabled                       | boolean  | Whether SAML IdP initiated login is enabled, learn more in the [SAML documentation](https://docs.datadoghq.com/account_management/saml/#idp-initiated-login).                                             |
| settings                      | saml_idp_metadata_uploaded    | boolean  | Whether or not a SAML identity provider metadata file was provided to the Datadog organization.                                                                                                           |
| settings                      | saml_login_url                | string   | URL for SAML logging.                                                                                                                                                                                     |
| settings                      | saml_strict_mode              | object   | Has one property enabled (boolean).                                                                                                                                                                       |
| saml_strict_mode              | enabled                       | boolean  | Whether or not the SAML strict mode is enabled. If true, all users must log in with SAML. Learn more on the [SAML Strict documentation](https://docs.datadoghq.com/account_management/saml/#saml-strict). |
|                               | subscription                  | object   | **DEPRECATED**: Subscription definition.                                                                                                                                                                  |
| subscription                  | type                          | string   | The subscription type. Types available are `trial`, `free`, and `pro`.                                                                                                                                    |
|                               | trial                         | boolean  | Only available for MSP customers. Allows child organizations to be created on a trial plan.                                                                                                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "billing": {
    "type": "string"
  },
  "description": "some description",
  "name": "New child org",
  "public_id": "abcdef12345",
  "settings": {
    "private_widget_share": false,
    "saml": {
      "enabled": false
    },
    "saml_autocreate_access_role": "ro",
    "saml_autocreate_users_domains": {
      "domains": [
        "example.com"
      ],
      "enabled": false
    },
    "saml_can_be_enabled": false,
    "saml_idp_endpoint": "https://my.saml.endpoint",
    "saml_idp_initiated_login": {
      "enabled": false
    },
    "saml_idp_metadata_uploaded": false,
    "saml_login_url": "https://my.saml.login.url",
    "saml_strict_mode": {
      "enabled": false
    }
  },
  "subscription": {
    "type": "string"
  },
  "trial": false
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response with an organization.

| Parent field                  | Field                         | Type     | Description                                                                                                                                                                                               |
| ----------------------------- | ----------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                               | org                           | object   | Create, edit, and manage organizations.                                                                                                                                                                   |
| org                           | billing                       | object   | **DEPRECATED**: A JSON array of billing type.                                                                                                                                                             |
| billing                       | type                          | string   | The type of billing. Only `parent_billing` is supported.                                                                                                                                                  |
| org                           | created                       | string   | Date of the organization creation.                                                                                                                                                                        |
| org                           | description                   | string   | Description of the organization.                                                                                                                                                                          |
| org                           | name                          | string   | The name of the child organization, limited to 32 characters.                                                                                                                                             |
| org                           | public_id                     | string   | The `public_id` of the organization you are operating within.                                                                                                                                             |
| org                           | settings                      | object   | A JSON array of settings.                                                                                                                                                                                 |
| settings                      | private_widget_share          | boolean  | Whether or not the organization users can share widgets outside of Datadog.                                                                                                                               |
| settings                      | saml                          | object   | Set the boolean property enabled to enable or disable single sign on with SAML. See the SAML documentation for more information about all SAML settings.                                                  |
| saml                          | enabled                       | boolean  | Whether or not SAML is enabled for this organization.                                                                                                                                                     |
| settings                      | saml_autocreate_access_role   | enum     | The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR`                                                 |
| settings                      | saml_autocreate_users_domains | object   | Has two properties, `enabled` (boolean) and `domains`, which is a list of domains without the @ symbol.                                                                                                   |
| saml_autocreate_users_domains | domains                       | [string] | List of domains where the SAML automated user creation is enabled.                                                                                                                                        |
| saml_autocreate_users_domains | enabled                       | boolean  | Whether or not the automated user creation based on SAML domain is enabled.                                                                                                                               |
| settings                      | saml_can_be_enabled           | boolean  | Whether or not SAML can be enabled for this organization.                                                                                                                                                 |
| settings                      | saml_idp_endpoint             | string   | Identity provider endpoint for SAML authentication.                                                                                                                                                       |
| settings                      | saml_idp_initiated_login      | object   | Has one property enabled (boolean).                                                                                                                                                                       |
| saml_idp_initiated_login      | enabled                       | boolean  | Whether SAML IdP initiated login is enabled, learn more in the [SAML documentation](https://docs.datadoghq.com/account_management/saml/#idp-initiated-login).                                             |
| settings                      | saml_idp_metadata_uploaded    | boolean  | Whether or not a SAML identity provider metadata file was provided to the Datadog organization.                                                                                                           |
| settings                      | saml_login_url                | string   | URL for SAML logging.                                                                                                                                                                                     |
| settings                      | saml_strict_mode              | object   | Has one property enabled (boolean).                                                                                                                                                                       |
| saml_strict_mode              | enabled                       | boolean  | Whether or not the SAML strict mode is enabled. If true, all users must log in with SAML. Learn more on the [SAML Strict documentation](https://docs.datadoghq.com/account_management/saml/#saml-strict). |
| org                           | subscription                  | object   | **DEPRECATED**: Subscription definition.                                                                                                                                                                  |
| subscription                  | type                          | string   | The subscription type. Types available are `trial`, `free`, and `pro`.                                                                                                                                    |
| org                           | trial                         | boolean  | Only available for MSP customers. Allows child organizations to be created on a trial plan.                                                                                                               |

{% /tab %}

{% tab title="Example" %}

```json
{
  "org": {
    "billing": {
      "type": "string"
    },
    "created": "2019-09-26T17:28:28Z",
    "description": "some description",
    "name": "New child org",
    "public_id": "abcdef12345",
    "settings": {
      "private_widget_share": false,
      "saml": {
        "enabled": false
      },
      "saml_autocreate_access_role": "ro",
      "saml_autocreate_users_domains": {
        "domains": [
          "example.com"
        ],
        "enabled": false
      },
      "saml_can_be_enabled": false,
      "saml_idp_endpoint": "https://my.saml.endpoint",
      "saml_idp_initiated_login": {
        "enabled": false
      },
      "saml_idp_metadata_uploaded": false,
      "saml_login_url": "https://my.saml.login.url",
      "saml_strict_mode": {
        "enabled": false
      }
    },
    "subscription": {
      "type": "string"
    },
    "trial": false
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport public_id="abc123"\# Curl commandcurl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/org/${public_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF

#####

```python
"""
Update your organization returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.organizations_api import OrganizationsApi
from datadog_api_client.v1.model.access_role import AccessRole
from datadog_api_client.v1.model.organization import Organization
from datadog_api_client.v1.model.organization_billing import OrganizationBilling
from datadog_api_client.v1.model.organization_settings import OrganizationSettings
from datadog_api_client.v1.model.organization_settings_saml import OrganizationSettingsSaml
from datadog_api_client.v1.model.organization_settings_saml_autocreate_users_domains import (
    OrganizationSettingsSamlAutocreateUsersDomains,
)
from datadog_api_client.v1.model.organization_settings_saml_idp_initiated_login import (
    OrganizationSettingsSamlIdpInitiatedLogin,
)
from datadog_api_client.v1.model.organization_settings_saml_strict_mode import OrganizationSettingsSamlStrictMode
from datadog_api_client.v1.model.organization_subscription import OrganizationSubscription

body = Organization(
    billing=OrganizationBilling(
        type="parent_billing",
    ),
    description="some description",
    name="New child org",
    public_id="abcdef12345",
    settings=OrganizationSettings(
        private_widget_share=False,
        saml=OrganizationSettingsSaml(
            enabled=False,
        ),
        saml_autocreate_access_role=AccessRole.READ_ONLY,
        saml_autocreate_users_domains=OrganizationSettingsSamlAutocreateUsersDomains(
            domains=[
                "example.com",
            ],
            enabled=False,
        ),
        saml_can_be_enabled=False,
        saml_idp_endpoint="https://my.saml.endpoint",
        saml_idp_initiated_login=OrganizationSettingsSamlIdpInitiatedLogin(
            enabled=False,
        ),
        saml_idp_metadata_uploaded=False,
        saml_login_url="https://my.saml.login.url",
        saml_strict_mode=OrganizationSettingsSamlStrictMode(
            enabled=False,
        ),
    ),
    subscription=OrganizationSubscription(
        type="pro",
    ),
    trial=False,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    response = api_instance.update_org(public_id="abc123", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Update your organization returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::OrganizationsAPI.new

body = DatadogAPIClient::V1::Organization.new({
  billing: DatadogAPIClient::V1::OrganizationBilling.new({
    type: "parent_billing",
  }),
  description: "some description",
  name: "New child org",
  public_id: "abcdef12345",
  settings: DatadogAPIClient::V1::OrganizationSettings.new({
    private_widget_share: false,
    saml: DatadogAPIClient::V1::OrganizationSettingsSaml.new({
      enabled: false,
    }),
    saml_autocreate_access_role: DatadogAPIClient::V1::AccessRole::READ_ONLY,
    saml_autocreate_users_domains: DatadogAPIClient::V1::OrganizationSettingsSamlAutocreateUsersDomains.new({
      domains: [
        "example.com",
      ],
      enabled: false,
    }),
    saml_can_be_enabled: false,
    saml_idp_endpoint: "https://my.saml.endpoint",
    saml_idp_initiated_login: DatadogAPIClient::V1::OrganizationSettingsSamlIdpInitiatedLogin.new({
      enabled: false,
    }),
    saml_idp_metadata_uploaded: false,
    saml_login_url: "https://my.saml.login.url",
    saml_strict_mode: DatadogAPIClient::V1::OrganizationSettingsSamlStrictMode.new({
      enabled: false,
    }),
  }),
  subscription: DatadogAPIClient::V1::OrganizationSubscription.new({
    type: "pro",
  }),
  trial: false,
})
p api_instance.update_org("abc123", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Update your organization returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    body := datadogV1.Organization{
        Billing: &datadogV1.OrganizationBilling{
            Type: datadog.PtrString("parent_billing"),
        },
        Description: datadog.PtrString("some description"),
        Name:        datadog.PtrString("New child org"),
        PublicId:    datadog.PtrString("abcdef12345"),
        Settings: &datadogV1.OrganizationSettings{
            PrivateWidgetShare: datadog.PtrBool(false),
            Saml: &datadogV1.OrganizationSettingsSaml{
                Enabled: datadog.PtrBool(false),
            },
            SamlAutocreateAccessRole: *datadogV1.NewNullableAccessRole(datadogV1.ACCESSROLE_READ_ONLY.Ptr()),
            SamlAutocreateUsersDomains: &datadogV1.OrganizationSettingsSamlAutocreateUsersDomains{
                Domains: []string{
                    "example.com",
                },
                Enabled: datadog.PtrBool(false),
            },
            SamlCanBeEnabled: datadog.PtrBool(false),
            SamlIdpEndpoint:  datadog.PtrString("https://my.saml.endpoint"),
            SamlIdpInitiatedLogin: &datadogV1.OrganizationSettingsSamlIdpInitiatedLogin{
                Enabled: datadog.PtrBool(false),
            },
            SamlIdpMetadataUploaded: datadog.PtrBool(false),
            SamlLoginUrl:            datadog.PtrString("https://my.saml.login.url"),
            SamlStrictMode: &datadogV1.OrganizationSettingsSamlStrictMode{
                Enabled: datadog.PtrBool(false),
            },
        },
        Subscription: &datadogV1.OrganizationSubscription{
            Type: datadog.PtrString("pro"),
        },
        Trial: datadog.PtrBool(false),
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewOrganizationsApi(apiClient)
    resp, r, err := api.UpdateOrg(ctx, "abc123", body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `OrganizationsApi.UpdateOrg`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `OrganizationsApi.UpdateOrg`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Update your organization returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.OrganizationsApi;
import com.datadog.api.client.v1.model.AccessRole;
import com.datadog.api.client.v1.model.Organization;
import com.datadog.api.client.v1.model.OrganizationBilling;
import com.datadog.api.client.v1.model.OrganizationResponse;
import com.datadog.api.client.v1.model.OrganizationSettings;
import com.datadog.api.client.v1.model.OrganizationSettingsSaml;
import com.datadog.api.client.v1.model.OrganizationSettingsSamlAutocreateUsersDomains;
import com.datadog.api.client.v1.model.OrganizationSettingsSamlIdpInitiatedLogin;
import com.datadog.api.client.v1.model.OrganizationSettingsSamlStrictMode;
import com.datadog.api.client.v1.model.OrganizationSubscription;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);

    Organization body =
        new Organization()
            .billing(new OrganizationBilling().type("parent_billing"))
            .description("some description")
            .name("New child org")
            .publicId("abcdef12345")
            .settings(
                new OrganizationSettings()
                    .privateWidgetShare(false)
                    .saml(new OrganizationSettingsSaml().enabled(false))
                    .samlAutocreateAccessRole(AccessRole.READ_ONLY)
                    .samlAutocreateUsersDomains(
                        new OrganizationSettingsSamlAutocreateUsersDomains()
                            .domains(Collections.singletonList("example.com"))
                            .enabled(false))
                    .samlCanBeEnabled(false)
                    .samlIdpEndpoint("https://my.saml.endpoint")
                    .samlIdpInitiatedLogin(
                        new OrganizationSettingsSamlIdpInitiatedLogin().enabled(false))
                    .samlIdpMetadataUploaded(false)
                    .samlLoginUrl("https://my.saml.login.url")
                    .samlStrictMode(new OrganizationSettingsSamlStrictMode().enabled(false)))
            .subscription(new OrganizationSubscription().type("pro"))
            .trial(false);

    try {
      OrganizationResponse result = apiInstance.updateOrg("abc123", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#updateOrg");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// Update your organization returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_organizations::OrganizationsAPI;
use datadog_api_client::datadogV1::model::AccessRole;
use datadog_api_client::datadogV1::model::Organization;
use datadog_api_client::datadogV1::model::OrganizationBilling;
use datadog_api_client::datadogV1::model::OrganizationSettings;
use datadog_api_client::datadogV1::model::OrganizationSettingsSaml;
use datadog_api_client::datadogV1::model::OrganizationSettingsSamlAutocreateUsersDomains;
use datadog_api_client::datadogV1::model::OrganizationSettingsSamlIdpInitiatedLogin;
use datadog_api_client::datadogV1::model::OrganizationSettingsSamlStrictMode;
use datadog_api_client::datadogV1::model::OrganizationSubscription;

#[tokio::main]
async fn main() {
    let body = Organization::new()
        .billing(OrganizationBilling::new().type_("parent_billing".to_string()))
        .description("some description".to_string())
        .name("New child org".to_string())
        .public_id("abcdef12345".to_string())
        .settings(
            OrganizationSettings::new()
                .private_widget_share(false)
                .saml(OrganizationSettingsSaml::new().enabled(false))
                .saml_autocreate_access_role(Some(AccessRole::READ_ONLY))
                .saml_autocreate_users_domains(
                    OrganizationSettingsSamlAutocreateUsersDomains::new()
                        .domains(vec!["example.com".to_string()])
                        .enabled(false),
                )
                .saml_can_be_enabled(false)
                .saml_idp_endpoint("https://my.saml.endpoint".to_string())
                .saml_idp_initiated_login(
                    OrganizationSettingsSamlIdpInitiatedLogin::new().enabled(false),
                )
                .saml_idp_metadata_uploaded(false)
                .saml_login_url("https://my.saml.login.url".to_string())
                .saml_strict_mode(OrganizationSettingsSamlStrictMode::new().enabled(false)),
        )
        .subscription(OrganizationSubscription::new().type_("pro".to_string()))
        .trial(false);
    let configuration = datadog::Configuration::new();
    let api = OrganizationsAPI::with_config(configuration);
    let resp = api.update_org("abc123".to_string(), body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Update your organization returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.OrganizationsApi(configuration);

const params: v1.OrganizationsApiUpdateOrgRequest = {
  body: {
    billing: {
      type: "parent_billing",
    },
    description: "some description",
    name: "New child org",
    publicId: "abcdef12345",
    settings: {
      privateWidgetShare: false,
      saml: {
        enabled: false,
      },
      samlAutocreateAccessRole: "ro",
      samlAutocreateUsersDomains: {
        domains: ["example.com"],
        enabled: false,
      },
      samlCanBeEnabled: false,
      samlIdpEndpoint: "https://my.saml.endpoint",
      samlIdpInitiatedLogin: {
        enabled: false,
      },
      samlIdpMetadataUploaded: false,
      samlLoginUrl: "https://my.saml.login.url",
      samlStrictMode: {
        enabled: false,
      },
    },
    subscription: {
      type: "pro",
    },
    trial: false,
  },
  publicId: "abc123",
};

apiInstance
  .updateOrg(params)
  .then((data: v1.OrganizationResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Upload IdP metadata{% #upload-idp-metadata %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/org/{public_id}/idp_metadata |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/org/{public_id}/idp_metadata |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/org/{public_id}/idp_metadata      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/org/{public_id}/idp_metadata      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/org/{public_id}/idp_metadata     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/org/{public_id}/idp_metadata |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/org/{public_id}/idp_metadata |

### Overview



There are a couple of options for updating the Identity Provider (IdP) metadata from your SAML IdP.

- **Multipart Form-Data**: Post the IdP metadata file using a form post.

- **XML Body:** Post the IdP metadata file as the body of the request.



### Arguments

#### Path Parameters

| Name                        | Type   | Description                                                |
| --------------------------- | ------ | ---------------------------------------------------------- |
| public_id [*required*] | string | The `public_id` of the organization you are operating with |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Field                      | Type   | Description                                           |
| -------------------------- | ------ | ----------------------------------------------------- |
| idp_file [*required*] | binary | The path to the XML metadata file you wish to upload. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "idp_file": ""
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The IdP response object.

| Field                     | Type   | Description                 |
| ------------------------- | ------ | --------------------------- |
| message [*required*] | string | Identity provider response. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "message": "IdP metadata successfully uploaded for example org"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="415" %}
Unsupported Media Type
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport public_id="abc123"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/org/${public_id}/idp_metadata" \
-H "Accept: application/json" \
-H "Content-Type: multipart/form-data" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-F idp_file=@string

#####

```python
"""
Upload IdP metadata returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.organizations_api import OrganizationsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    response = api_instance.upload_idp_for_org(
        public_id="abc123",
        idp_file=open("./idp_metadata.xml", "rb"),
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Upload IdP metadata returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::OrganizationsAPI.new
p api_instance.upload_idp_for_org("abc123", File.open("./idp_metadata.xml", "r"))
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Upload IdP metadata returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "io"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewOrganizationsApi(apiClient)
    resp, r, err := api.UploadIdPForOrg(ctx, "abc123", func() io.Reader { fp, _ := os.Open("./idp_metadata.xml"); return fp }())

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `OrganizationsApi.UploadIdPForOrg`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `OrganizationsApi.UploadIdPForOrg`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Upload IdP metadata returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.OrganizationsApi;
import com.datadog.api.client.v1.model.IdpResponse;
import java.io.File;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);

    try {
      IdpResponse result = apiInstance.uploadIdPForOrg("abc123", new File("./idp_metadata.xml"));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#uploadIdPForOrg");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// Upload IdP metadata returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_organizations::OrganizationsAPI;
use std::fs;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = OrganizationsAPI::with_config(configuration);
    let resp = api
        .upload_idp_for_org(
            "abc123".to_string(),
            fs::read("./idp_metadata.xml").unwrap(),
        )
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Upload IdP metadata returns "OK" response
 */

import * as fs from "fs";
import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.OrganizationsApi(configuration);

const params: v1.OrganizationsApiUploadIdPForOrgRequest = {
  publicId: "abc123",
  idpFile: {
    data: Buffer.from(fs.readFileSync("./idp_metadata.xml", "utf8")),
    name: "./idp_metadata.xml",
  },
};

apiInstance
  .uploadIdPForOrg(params)
  .then((data: v1.IdpResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/saml_configurations/idp_metadata |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/saml_configurations/idp_metadata |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/saml_configurations/idp_metadata      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/saml_configurations/idp_metadata      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/saml_configurations/idp_metadata     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/saml_configurations/idp_metadata |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/saml_configurations/idp_metadata |

### Overview



Endpoint for uploading IdP metadata for SAML setup.

Use this endpoint to upload or replace IdP metadata for SAML login configuration.
This endpoint requires the `org_management` permission.


### Request

#### Body Data (required)



{% tab title="Model" %}

| Field    | Type   | Description               |
| -------- | ------ | ------------------------- |
| idp_file | binary | The IdP metadata XML file |

{% /tab %}

{% tab title="Example" %}

```json
{
  "idp_file": "string"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/saml_configurations/idp_metadata" \
-H "Accept: application/json" \
-H "Content-Type: multipart/form-data" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-F idp_file=@string

#####

```python
"""
Upload IdP metadata returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.organizations_api import OrganizationsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    api_instance.upload_idp_metadata(
        idp_file=open("fixtures/organizations/saml_configurations/valid_idp_metadata.xml", "rb"),
    )
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Upload IdP metadata returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OrganizationsAPI.new
opts = {
  idp_file: File.open("fixtures/organizations/saml_configurations/valid_idp_metadata.xml", "r"),
}
p api_instance.upload_idp_metadata(opts)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Upload IdP metadata returns "OK" response

package main

import (
    "context"
    "fmt"
    "io"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewOrganizationsApi(apiClient)
    r, err := api.UploadIdPMetadata(ctx, *datadogV2.NewUploadIdPMetadataOptionalParameters().WithIdpFile(func() io.Reader {
        fp, _ := os.Open("fixtures/organizations/saml_configurations/valid_idp_metadata.xml")
        return fp
    }()))

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `OrganizationsApi.UploadIdPMetadata`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Upload IdP metadata returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OrganizationsApi;
import com.datadog.api.client.v2.api.OrganizationsApi.UploadIdPMetadataOptionalParameters;
import java.io.File;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);

    try {
      apiInstance.uploadIdPMetadata(
          new UploadIdPMetadataOptionalParameters()
              .idpFile(
                  new File("fixtures/organizations/saml_configurations/valid_idp_metadata.xml")));
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#uploadIdPMetadata");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// Upload IdP metadata returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_organizations::OrganizationsAPI;
use datadog_api_client::datadogV2::api_organizations::UploadIdPMetadataOptionalParams;
use std::fs;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = OrganizationsAPI::with_config(configuration);
    let resp = api
        .upload_idp_metadata(UploadIdPMetadataOptionalParams::default().idp_file(
            fs::read("fixtures/organizations/saml_configurations/valid_idp_metadata.xml").unwrap(),
        ))
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Upload IdP metadata returns "OK" response
 */

import * as fs from "fs";
import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OrganizationsApi(configuration);

const params: v2.OrganizationsApiUploadIdPMetadataRequest = {
  idpFile: {
    data: Buffer.from(
      fs.readFileSync(
        "fixtures/organizations/saml_configurations/valid_idp_metadata.xml",
        "utf8"
      )
    ),
    name: "fixtures/organizations/saml_configurations/valid_idp_metadata.xml",
  },
};

apiInstance
  .uploadIdPMetadata(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Spin-off Child Organization{% #spin-off-child-organization %}

{% tab title="v1" %}

| Datadog site      | API endpoint                                                        |
| ----------------- | ------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v1/org/{public_id}/downgrade |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v1/org/{public_id}/downgrade |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v1/org/{public_id}/downgrade      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v1/org/{public_id}/downgrade      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v1/org/{public_id}/downgrade     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v1/org/{public_id}/downgrade |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v1/org/{public_id}/downgrade |

### Overview

Only available for MSP customers. Removes a child organization from the hierarchy of the master organization and places the child organization on a 30-day trial.

### Arguments

#### Path Parameters

| Name                        | Type   | Description                                                   |
| --------------------------- | ------ | ------------------------------------------------------------- |
| public_id [*required*] | string | The `public_id` of the organization you are operating within. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Status of downgrade

| Field   | Type   | Description                                                  |
| ------- | ------ | ------------------------------------------------------------ |
| message | string | Information pertaining to the downgraded child organization. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "message": "string"
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
Error response object.

| Field                    | Type     | Description                          |
| ------------------------ | -------- | ------------------------------------ |
| errors [*required*] | [string] | Array of errors returned by the API. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport public_id="abc123"\# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/org/${public_id}/downgrade" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Spin-off Child Organization returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.organizations_api import OrganizationsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    response = api_instance.downgrade_org(
        public_id="abc123",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Spin-off Child Organization returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::OrganizationsAPI.new
p api_instance.downgrade_org("abc123")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Spin-off Child Organization returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV1"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV1.NewOrganizationsApi(apiClient)
    resp, r, err := api.DowngradeOrg(ctx, "abc123")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `OrganizationsApi.DowngradeOrg`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `OrganizationsApi.DowngradeOrg`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Spin-off Child Organization returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v1.api.OrganizationsApi;
import com.datadog.api.client.v1.model.OrgDowngradedResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);

    try {
      OrgDowngradedResponse result = apiInstance.downgradeOrg("abc123");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#downgradeOrg");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// Spin-off Child Organization returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV1::api_organizations::OrganizationsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = OrganizationsAPI::with_config(configuration);
    let resp = api.downgrade_org("abc123".to_string()).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Spin-off Child Organization returns "OK" response
 */

import { client, v1 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v1.OrganizationsApi(configuration);

const params: v1.OrganizationsApiDowngradeOrgRequest = {
  publicId: "abc123",
};

apiInstance
  .downgradeOrg(params)
  .then((data: v1.OrgDowngradedResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## List Org Configs{% #list-org-configs %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                         |
| ----------------- | ---------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/org_configs |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/org_configs |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/org_configs      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/org_configs      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/org_configs     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/org_configs |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/org_configs |

### Overview

Returns all Org Configs (name, description, and value).

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A response with multiple Org Configs.

| Parent field | Field                         | Type      | Description                                                    |
| ------------ | ----------------------------- | --------- | -------------------------------------------------------------- |
|              | data [*required*]        | [object]  | An array of Org Configs.                                       |
| data         | attributes [*required*]  | object    | Readable attributes of an Org Config.                          |
| attributes   | description [*required*] | string    | The description of an Org Config.                              |
| attributes   | modified_at                   | date-time | The timestamp of the last Org Config update (if any).          |
| attributes   | name [*required*]        | string    | The machine-friendly name of an Org Config.                    |
| attributes   | value [*required*]       |           | The value of an Org Config.                                    |
| attributes   | value_type [*required*]  | string    | The type of an Org Config value.                               |
| data         | id [*required*]          | string    | A unique identifier for an Org Config.                         |
| data         | type [*required*]        | enum      | Data type of an Org Config. Allowed enum values: `org_configs` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "description": "Frobulate the turbo encabulator manifold",
        "modified_at": "2019-09-19T10:00:00.000Z",
        "name": "monitor_timezone",
        "value": "undefined",
        "value_type": "bool"
      },
      "id": "abcd1234",
      "type": "org_configs"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/org_configs" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
List Org Configs returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.organizations_api import OrganizationsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    response = api_instance.list_org_configs()

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# List Org Configs returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OrganizationsAPI.new
p api_instance.list_org_configs()
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// List Org Configs returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewOrganizationsApi(apiClient)
    resp, r, err := api.ListOrgConfigs(ctx)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `OrganizationsApi.ListOrgConfigs`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `OrganizationsApi.ListOrgConfigs`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// List Org Configs returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OrganizationsApi;
import com.datadog.api.client.v2.model.OrgConfigListResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);

    try {
      OrgConfigListResponse result = apiInstance.listOrgConfigs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#listOrgConfigs");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// List Org Configs returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_organizations::OrganizationsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = OrganizationsAPI::with_config(configuration);
    let resp = api.list_org_configs().await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * List Org Configs returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OrganizationsApi(configuration);

apiInstance
  .listOrgConfigs()
  .then((data: v2.OrgConfigListResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Get a specific Org Config value{% #get-a-specific-org-config-value %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                           |
| ----------------- | ---------------------------------------------------------------------- |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/org_configs/{org_config_name} |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/org_configs/{org_config_name} |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/org_configs/{org_config_name}      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/org_configs/{org_config_name}      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/org_configs/{org_config_name}     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/org_configs/{org_config_name} |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/org_configs/{org_config_name} |

### Overview

Return the name, description, and value of a specific Org Config.

### Arguments

#### Path Parameters

| Name                              | Type   | Description                |
| --------------------------------- | ------ | -------------------------- |
| org_config_name [*required*] | string | The name of an Org Config. |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A response with a single Org Config.

| Parent field | Field                         | Type      | Description                                                    |
| ------------ | ----------------------------- | --------- | -------------------------------------------------------------- |
|              | data [*required*]        | object    | A single Org Config.                                           |
| data         | attributes [*required*]  | object    | Readable attributes of an Org Config.                          |
| attributes   | description [*required*] | string    | The description of an Org Config.                              |
| attributes   | modified_at                   | date-time | The timestamp of the last Org Config update (if any).          |
| attributes   | name [*required*]        | string    | The machine-friendly name of an Org Config.                    |
| attributes   | value [*required*]       |           | The value of an Org Config.                                    |
| attributes   | value_type [*required*]  | string    | The type of an Org Config value.                               |
| data         | id [*required*]          | string    | A unique identifier for an Org Config.                         |
| data         | type [*required*]        | enum      | Data type of an Org Config. Allowed enum values: `org_configs` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "description": "Frobulate the turbo encabulator manifold",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "monitor_timezone",
      "value": "undefined",
      "value_type": "bool"
    },
    "id": "abcd1234",
    "type": "org_configs"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                  \# Path parametersexport org_config_name="monitor_timezone"\# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/org_configs/${org_config_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"

#####

```python
"""
Get a specific Org Config value returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.organizations_api import OrganizationsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    response = api_instance.get_org_config(
        org_config_name="custom_roles",
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Get a specific Org Config value returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OrganizationsAPI.new
p api_instance.get_org_config("custom_roles")
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```go
// Get a specific Org Config value returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewOrganizationsApi(apiClient)
    resp, r, err := api.GetOrgConfig(ctx, "custom_roles")

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `OrganizationsApi.GetOrgConfig`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `OrganizationsApi.GetOrgConfig`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Get a specific Org Config value returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OrganizationsApi;
import com.datadog.api.client.v2.model.OrgConfigGetResponse;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);

    try {
      OrgConfigGetResponse result = apiInstance.getOrgConfig("custom_roles");
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#getOrgConfig");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```rust
// Get a specific Org Config value returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_organizations::OrganizationsAPI;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = OrganizationsAPI::with_config(configuration);
    let resp = api.get_org_config("custom_roles".to_string()).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Get a specific Org Config value returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OrganizationsApi(configuration);

const params: v2.OrganizationsApiGetOrgConfigRequest = {
  orgConfigName: "custom_roles",
};

apiInstance
  .getOrgConfig(params)
  .then((data: v2.OrgConfigGetResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}

## Update a specific Org Config{% #update-a-specific-org-config %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                             |
| ----------------- | ------------------------------------------------------------------------ |
| ap1.datadoghq.com | PATCH https://api.ap1.datadoghq.com/api/v2/org_configs/{org_config_name} |
| ap2.datadoghq.com | PATCH https://api.ap2.datadoghq.com/api/v2/org_configs/{org_config_name} |
| app.datadoghq.eu  | PATCH https://api.datadoghq.eu/api/v2/org_configs/{org_config_name}      |
| app.ddog-gov.com  | PATCH https://api.ddog-gov.com/api/v2/org_configs/{org_config_name}      |
| app.datadoghq.com | PATCH https://api.datadoghq.com/api/v2/org_configs/{org_config_name}     |
| us3.datadoghq.com | PATCH https://api.us3.datadoghq.com/api/v2/org_configs/{org_config_name} |
| us5.datadoghq.com | PATCH https://api.us5.datadoghq.com/api/v2/org_configs/{org_config_name} |

### Overview

Update the value of a specific Org Config. This endpoint requires the `org_management` permission.

### Arguments

#### Path Parameters

| Name                              | Type   | Description                |
| --------------------------------- | ------ | -------------------------- |
| org_config_name [*required*] | string | The name of an Org Config. |

### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                        | Type   | Description                                                    |
| ------------ | ---------------------------- | ------ | -------------------------------------------------------------- |
|              | data [*required*]       | object | An Org Config write operation.                                 |
| data         | attributes [*required*] | object | Writable attributes of an Org Config.                          |
| attributes   | value [*required*]      |        | The value of an Org Config.                                    |
| data         | type [*required*]       | enum   | Data type of an Org Config. Allowed enum values: `org_configs` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "value": "UTC"
    },
    "type": "org_configs"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
A response with a single Org Config.

| Parent field | Field                         | Type      | Description                                                    |
| ------------ | ----------------------------- | --------- | -------------------------------------------------------------- |
|              | data [*required*]        | object    | A single Org Config.                                           |
| data         | attributes [*required*]  | object    | Readable attributes of an Org Config.                          |
| attributes   | description [*required*] | string    | The description of an Org Config.                              |
| attributes   | modified_at                   | date-time | The timestamp of the last Org Config update (if any).          |
| attributes   | name [*required*]        | string    | The machine-friendly name of an Org Config.                    |
| attributes   | value [*required*]       |           | The value of an Org Config.                                    |
| attributes   | value_type [*required*]  | string    | The type of an Org Config value.                               |
| data         | id [*required*]          | string    | A unique identifier for an Org Config.                         |
| data         | type [*required*]        | enum      | Data type of an Org Config. Allowed enum values: `org_configs` |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "attributes": {
      "description": "Frobulate the turbo encabulator manifold",
      "modified_at": "2019-09-19T10:00:00.000Z",
      "name": "monitor_timezone",
      "value": "undefined",
      "value_type": "bool"
    },
    "id": "abcd1234",
    "type": "org_configs"
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="404" %}
Not Found
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

#####
                          \# Path parametersexport org_config_name="monitor_timezone"\# Curl commandcurl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/org_configs/${org_config_name}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "value": "UTC"
    },
    "type": "org_configs"
  }
}
EOF

#####

```go
// Update a specific Org Config returns "OK" response

package main

import (
    "context"
    "encoding/json"
    "fmt"
    "os"

    "github.com/DataDog/datadog-api-client-go/v2/api/datadog"
    "github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
    body := datadogV2.OrgConfigWriteRequest{
        Data: datadogV2.OrgConfigWrite{
            Attributes: datadogV2.OrgConfigWriteAttributes{
                Value: "UTC",
            },
            Type: datadogV2.ORGCONFIGTYPE_ORG_CONFIGS,
        },
    }
    ctx := datadog.NewDefaultContext(context.Background())
    configuration := datadog.NewConfiguration()
    apiClient := datadog.NewAPIClient(configuration)
    api := datadogV2.NewOrganizationsApi(apiClient)
    resp, r, err := api.UpdateOrgConfig(ctx, "monitor_timezone", body)

    if err != nil {
        fmt.Fprintf(os.Stderr, "Error when calling `OrganizationsApi.UpdateOrgConfig`: %v\n", err)
        fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
    }

    responseContent, _ := json.MarshalIndent(resp, "", "  ")
    fmt.Fprintf(os.Stdout, "Response from `OrganizationsApi.UpdateOrgConfig`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"
#####

```java
// Update a specific Org Config returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.OrganizationsApi;
import com.datadog.api.client.v2.model.OrgConfigGetResponse;
import com.datadog.api.client.v2.model.OrgConfigType;
import com.datadog.api.client.v2.model.OrgConfigWrite;
import com.datadog.api.client.v2.model.OrgConfigWriteAttributes;
import com.datadog.api.client.v2.model.OrgConfigWriteRequest;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);

    OrgConfigWriteRequest body =
        new OrgConfigWriteRequest()
            .data(
                new OrgConfigWrite()
                    .attributes(new OrgConfigWriteAttributes().value("UTC"))
                    .type(OrgConfigType.ORG_CONFIGS));

    try {
      OrgConfigGetResponse result = apiInstance.updateOrgConfig("monitor_timezone", body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#updateOrgConfig");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"
#####

```python
"""
Update a specific Org Config returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.organizations_api import OrganizationsApi
from datadog_api_client.v2.model.org_config_type import OrgConfigType
from datadog_api_client.v2.model.org_config_write import OrgConfigWrite
from datadog_api_client.v2.model.org_config_write_attributes import OrgConfigWriteAttributes
from datadog_api_client.v2.model.org_config_write_request import OrgConfigWriteRequest

body = OrgConfigWriteRequest(
    data=OrgConfigWrite(
        attributes=OrgConfigWriteAttributes(
            value="UTC",
        ),
        type=OrgConfigType.ORG_CONFIGS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    response = api_instance.update_org_config(org_config_name="monitor_timezone", body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"
#####

```ruby
# Update a specific Org Config returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OrganizationsAPI.new

body = DatadogAPIClient::V2::OrgConfigWriteRequest.new({
  data: DatadogAPIClient::V2::OrgConfigWrite.new({
    attributes: DatadogAPIClient::V2::OrgConfigWriteAttributes.new({
      value: "UTC",
    }),
    type: DatadogAPIClient::V2::OrgConfigType::ORG_CONFIGS,
  }),
})
p api_instance.update_org_config("monitor_timezone", body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"
#####

```rust
// Update a specific Org Config returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_organizations::OrganizationsAPI;
use datadog_api_client::datadogV2::model::OrgConfigType;
use datadog_api_client::datadogV2::model::OrgConfigWrite;
use datadog_api_client::datadogV2::model::OrgConfigWriteAttributes;
use datadog_api_client::datadogV2::model::OrgConfigWriteRequest;
use serde_json::Value;

#[tokio::main]
async fn main() {
    let body = OrgConfigWriteRequest::new(OrgConfigWrite::new(
        OrgConfigWriteAttributes::new(Value::from("UTC")),
        OrgConfigType::ORG_CONFIGS,
    ));
    let configuration = datadog::Configuration::new();
    let api = OrganizationsAPI::with_config(configuration);
    let resp = api
        .update_org_config("monitor_timezone".to_string(), body)
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run
#####

```typescript
/**
 * Update a specific Org Config returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.OrganizationsApi(configuration);

const params: v2.OrganizationsApiUpdateOrgConfigRequest = {
  body: {
    data: {
      attributes: {
        value: "UTC",
      },
      type: "org_configs",
    },
  },
  orgConfigName: "monitor_timezone",
};

apiInstance
  .updateOrgConfig(params)
  .then((data: v2.OrgConfigGetResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"
{% /tab %}
