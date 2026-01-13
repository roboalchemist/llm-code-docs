# Source: https://docs.datadoghq.com/api/latest/organizations/

# Organizations
Create, edit, and manage your organizations. Read more about [multi-org accounts](https://docs.datadoghq.com/account_management/multi_organization).
## [Create a child organization](https://docs.datadoghq.com/api/latest/organizations/#create-a-child-organization)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/organizations/#create-a-child-organization-v1)


POST https://api.ap1.datadoghq.com/api/v1/orghttps://api.ap2.datadoghq.com/api/v1/orghttps://api.datadoghq.eu/api/v1/orghttps://api.ddog-gov.com/api/v1/orghttps://api.datadoghq.com/api/v1/orghttps://api.us3.datadoghq.com/api/v1/orghttps://api.us5.datadoghq.com/api/v1/org
### Overview
Create a child organization.
This endpoint requires the [multi-organization account](https://docs.datadoghq.com/account_management/multi_organization/) feature and must be enabled by [contacting support](https://docs.datadoghq.com/help/).
Once a new child organization is created, you can interact with it by using the `org.public_id`, `api_key.key`, and `application_key.hash` provided in the response.
This endpoint requires the `org_management` permission.
### Request
#### Body Data (required)
Organization object that needs to be created
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Field
Type
Description
billing
object
**DEPRECATED** : A JSON array of billing type.
type
string
The type of billing. Only `parent_billing` is supported.
name [_required_]
string
The name of the new child-organization, limited to 32 characters.
subscription
object
**DEPRECATED** : Subscription definition.
type
string
The subscription type. Types available are `trial`, `free`, and `pro`.
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/organizations/#CreateChildOrg-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/organizations/#CreateChildOrg-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/organizations/#CreateChildOrg-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/organizations/#CreateChildOrg-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Response object for an organization creation.
Field
Type
Description
api_key
object
Datadog API key.
created
string
Date of creation of the API key.
created_by
string
Datadog user handle that created the API key.
key
string
API key.
name
string
Name of your API key.
application_key
object
An application key with its associated metadata.
hash
string
Hash of an application key.
name
string
Name of an application key.
owner
string
Owner of an application key.
org
object
Create, edit, and manage organizations.
billing
object
**DEPRECATED** : A JSON array of billing type.
type
string
The type of billing. Only `parent_billing` is supported.
created
string
Date of the organization creation.
description
string
Description of the organization.
name
string
The name of the child organization, limited to 32 characters.
public_id
string
The `public_id` of the organization you are operating within.
settings
object
A JSON array of settings.
private_widget_share
boolean
Whether or not the organization users can share widgets outside of Datadog.
saml
object
Set the boolean property enabled to enable or disable single sign on with SAML. See the SAML documentation for more information about all SAML settings.
enabled
boolean
Whether or not SAML is enabled for this organization.
saml_autocreate_access_role
enum
The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR`
saml_autocreate_users_domains
object
Has two properties, `enabled` (boolean) and `domains`, which is a list of domains without the @ symbol.
domains
[string]
List of domains where the SAML automated user creation is enabled.
enabled
boolean
Whether or not the automated user creation based on SAML domain is enabled.
saml_can_be_enabled
boolean
Whether or not SAML can be enabled for this organization.
saml_idp_endpoint
string
Identity provider endpoint for SAML authentication.
saml_idp_initiated_login
object
Has one property enabled (boolean).
enabled
boolean
Whether SAML IdP initiated login is enabled, learn more in the [SAML documentation](https://docs.datadoghq.com/account_management/saml/#idp-initiated-login).
saml_idp_metadata_uploaded
boolean
Whether or not a SAML identity provider metadata file was provided to the Datadog organization.
saml_login_url
string
URL for SAML logging.
saml_strict_mode
object
Has one property enabled (boolean).
enabled
boolean
Whether or not the SAML strict mode is enabled. If true, all users must log in with SAML. Learn more on the [SAML Strict documentation](https://docs.datadoghq.com/account_management/saml/#saml-strict).
subscription
object
**DEPRECATED** : Subscription definition.
type
string
The subscription type. Types available are `trial`, `free`, and `pro`.
trial
boolean
Only available for MSP customers. Allows child organizations to be created on a trial plan.
user
object
Create, edit, and disable users.
access_role
enum
The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR`
disabled
boolean
The new disabled status of the user.
email
string
The new email of the user.
handle
string
The user handle, must be a valid email.
icon
string
Gravatar icon associated to the user.
name
string
The name of the user.
verified
boolean
Whether or not the user logged in Datadog at least once.
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/organizations/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/organizations/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/organizations/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/organizations/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/organizations/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/organizations/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/organizations/?code-lang=typescript)


#####  Create a child organization
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/org" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "name": "New child org"
}
EOF  

                
```

#####  Create a child organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Create a child organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Create a child organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Create a child organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Create a child organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Create a child organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [List your managed organizations](https://docs.datadoghq.com/api/latest/organizations/#list-your-managed-organizations)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/organizations/#list-your-managed-organizations-v1)


GET https://api.ap1.datadoghq.com/api/v1/orghttps://api.ap2.datadoghq.com/api/v1/orghttps://api.datadoghq.eu/api/v1/orghttps://api.ddog-gov.com/api/v1/orghttps://api.datadoghq.com/api/v1/orghttps://api.us3.datadoghq.com/api/v1/orghttps://api.us5.datadoghq.com/api/v1/org
### Overview
This endpoint returns data on your top-level organization. This endpoint requires the `org_management` permission.
### Response
  * [200](https://docs.datadoghq.com/api/latest/organizations/#ListOrgs-200-v1)
  * [403](https://docs.datadoghq.com/api/latest/organizations/#ListOrgs-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/organizations/#ListOrgs-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Response with the list of organizations.
Field
Type
Description
orgs
[object]
Array of organization objects.
billing
object
**DEPRECATED** : A JSON array of billing type.
type
string
The type of billing. Only `parent_billing` is supported.
created
string
Date of the organization creation.
description
string
Description of the organization.
name
string
The name of the child organization, limited to 32 characters.
public_id
string
The `public_id` of the organization you are operating within.
settings
object
A JSON array of settings.
private_widget_share
boolean
Whether or not the organization users can share widgets outside of Datadog.
saml
object
Set the boolean property enabled to enable or disable single sign on with SAML. See the SAML documentation for more information about all SAML settings.
enabled
boolean
Whether or not SAML is enabled for this organization.
saml_autocreate_access_role
enum
The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR`
saml_autocreate_users_domains
object
Has two properties, `enabled` (boolean) and `domains`, which is a list of domains without the @ symbol.
domains
[string]
List of domains where the SAML automated user creation is enabled.
enabled
boolean
Whether or not the automated user creation based on SAML domain is enabled.
saml_can_be_enabled
boolean
Whether or not SAML can be enabled for this organization.
saml_idp_endpoint
string
Identity provider endpoint for SAML authentication.
saml_idp_initiated_login
object
Has one property enabled (boolean).
enabled
boolean
Whether SAML IdP initiated login is enabled, learn more in the [SAML documentation](https://docs.datadoghq.com/account_management/saml/#idp-initiated-login).
saml_idp_metadata_uploaded
boolean
Whether or not a SAML identity provider metadata file was provided to the Datadog organization.
saml_login_url
string
URL for SAML logging.
saml_strict_mode
object
Has one property enabled (boolean).
enabled
boolean
Whether or not the SAML strict mode is enabled. If true, all users must log in with SAML. Learn more on the [SAML Strict documentation](https://docs.datadoghq.com/account_management/saml/#saml-strict).
subscription
object
**DEPRECATED** : Subscription definition.
type
string
The subscription type. Types available are `trial`, `free`, and `pro`.
trial
boolean
Only available for MSP customers. Allows child organizations to be created on a trial plan.
```
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

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/organizations/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/organizations/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/organizations/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/organizations/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/organizations/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/organizations/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/organizations/?code-lang=typescript)


#####  List your managed organizations
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/org" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List your managed organizations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List your managed organizations
```
# List your managed organizations returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::OrganizationsAPI.new
p api_instance.list_orgs()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List your managed organizations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List your managed organizations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  List your managed organizations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  List your managed organizations
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Get organization information](https://docs.datadoghq.com/api/latest/organizations/#get-organization-information)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/organizations/#get-organization-information-v1)


GET https://api.ap1.datadoghq.com/api/v1/org/{public_id}https://api.ap2.datadoghq.com/api/v1/org/{public_id}https://api.datadoghq.eu/api/v1/org/{public_id}https://api.ddog-gov.com/api/v1/org/{public_id}https://api.datadoghq.com/api/v1/org/{public_id}https://api.us3.datadoghq.com/api/v1/org/{public_id}https://api.us5.datadoghq.com/api/v1/org/{public_id}
### Overview
Get organization information.
### Arguments
#### Path Parameters
Name
Type
Description
public_id [_required_]
string
The `public_id` of the organization you are operating within.
### Response
  * [200](https://docs.datadoghq.com/api/latest/organizations/#GetOrg-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/organizations/#GetOrg-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/organizations/#GetOrg-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/organizations/#GetOrg-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Response with an organization.
Field
Type
Description
org
object
Create, edit, and manage organizations.
billing
object
**DEPRECATED** : A JSON array of billing type.
type
string
The type of billing. Only `parent_billing` is supported.
created
string
Date of the organization creation.
description
string
Description of the organization.
name
string
The name of the child organization, limited to 32 characters.
public_id
string
The `public_id` of the organization you are operating within.
settings
object
A JSON array of settings.
private_widget_share
boolean
Whether or not the organization users can share widgets outside of Datadog.
saml
object
Set the boolean property enabled to enable or disable single sign on with SAML. See the SAML documentation for more information about all SAML settings.
enabled
boolean
Whether or not SAML is enabled for this organization.
saml_autocreate_access_role
enum
The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR`
saml_autocreate_users_domains
object
Has two properties, `enabled` (boolean) and `domains`, which is a list of domains without the @ symbol.
domains
[string]
List of domains where the SAML automated user creation is enabled.
enabled
boolean
Whether or not the automated user creation based on SAML domain is enabled.
saml_can_be_enabled
boolean
Whether or not SAML can be enabled for this organization.
saml_idp_endpoint
string
Identity provider endpoint for SAML authentication.
saml_idp_initiated_login
object
Has one property enabled (boolean).
enabled
boolean
Whether SAML IdP initiated login is enabled, learn more in the [SAML documentation](https://docs.datadoghq.com/account_management/saml/#idp-initiated-login).
saml_idp_metadata_uploaded
boolean
Whether or not a SAML identity provider metadata file was provided to the Datadog organization.
saml_login_url
string
URL for SAML logging.
saml_strict_mode
object
Has one property enabled (boolean).
enabled
boolean
Whether or not the SAML strict mode is enabled. If true, all users must log in with SAML. Learn more on the [SAML Strict documentation](https://docs.datadoghq.com/account_management/saml/#saml-strict).
subscription
object
**DEPRECATED** : Subscription definition.
type
string
The subscription type. Types available are `trial`, `free`, and `pro`.
trial
boolean
Only available for MSP customers. Allows child organizations to be created on a trial plan.
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/organizations/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/organizations/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/organizations/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/organizations/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/organizations/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/organizations/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/organizations/?code-lang=typescript)


#####  Get organization information
Copy
```
                  # Path parameters  
export public_id="abc123"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/org/${public_id}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get organization information
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get organization information
```
# Get organization information returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::OrganizationsAPI.new
p api_instance.get_org("abc123")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get organization information
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get organization information
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get organization information
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get organization information
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Update your organization](https://docs.datadoghq.com/api/latest/organizations/#update-your-organization)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/organizations/#update-your-organization-v1)


PUT https://api.ap1.datadoghq.com/api/v1/org/{public_id}https://api.ap2.datadoghq.com/api/v1/org/{public_id}https://api.datadoghq.eu/api/v1/org/{public_id}https://api.ddog-gov.com/api/v1/org/{public_id}https://api.datadoghq.com/api/v1/org/{public_id}https://api.us3.datadoghq.com/api/v1/org/{public_id}https://api.us5.datadoghq.com/api/v1/org/{public_id}
### Overview
Update your organization.
### Arguments
#### Path Parameters
Name
Type
Description
public_id [_required_]
string
The `public_id` of the organization you are operating within.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Field
Type
Description
billing
object
**DEPRECATED** : A JSON array of billing type.
type
string
The type of billing. Only `parent_billing` is supported.
created
string
Date of the organization creation.
description
string
Description of the organization.
name
string
The name of the child organization, limited to 32 characters.
public_id
string
The `public_id` of the organization you are operating within.
settings
object
A JSON array of settings.
private_widget_share
boolean
Whether or not the organization users can share widgets outside of Datadog.
saml
object
Set the boolean property enabled to enable or disable single sign on with SAML. See the SAML documentation for more information about all SAML settings.
enabled
boolean
Whether or not SAML is enabled for this organization.
saml_autocreate_access_role
enum
The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR`
saml_autocreate_users_domains
object
Has two properties, `enabled` (boolean) and `domains`, which is a list of domains without the @ symbol.
domains
[string]
List of domains where the SAML automated user creation is enabled.
enabled
boolean
Whether or not the automated user creation based on SAML domain is enabled.
saml_can_be_enabled
boolean
Whether or not SAML can be enabled for this organization.
saml_idp_endpoint
string
Identity provider endpoint for SAML authentication.
saml_idp_initiated_login
object
Has one property enabled (boolean).
enabled
boolean
Whether SAML IdP initiated login is enabled, learn more in the [SAML documentation](https://docs.datadoghq.com/account_management/saml/#idp-initiated-login).
saml_idp_metadata_uploaded
boolean
Whether or not a SAML identity provider metadata file was provided to the Datadog organization.
saml_login_url
string
URL for SAML logging.
saml_strict_mode
object
Has one property enabled (boolean).
enabled
boolean
Whether or not the SAML strict mode is enabled. If true, all users must log in with SAML. Learn more on the [SAML Strict documentation](https://docs.datadoghq.com/account_management/saml/#saml-strict).
subscription
object
**DEPRECATED** : Subscription definition.
type
string
The subscription type. Types available are `trial`, `free`, and `pro`.
trial
boolean
Only available for MSP customers. Allows child organizations to be created on a trial plan.
```
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

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/organizations/#UpdateOrg-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/organizations/#UpdateOrg-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/organizations/#UpdateOrg-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/organizations/#UpdateOrg-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Response with an organization.
Field
Type
Description
org
object
Create, edit, and manage organizations.
billing
object
**DEPRECATED** : A JSON array of billing type.
type
string
The type of billing. Only `parent_billing` is supported.
created
string
Date of the organization creation.
description
string
Description of the organization.
name
string
The name of the child organization, limited to 32 characters.
public_id
string
The `public_id` of the organization you are operating within.
settings
object
A JSON array of settings.
private_widget_share
boolean
Whether or not the organization users can share widgets outside of Datadog.
saml
object
Set the boolean property enabled to enable or disable single sign on with SAML. See the SAML documentation for more information about all SAML settings.
enabled
boolean
Whether or not SAML is enabled for this organization.
saml_autocreate_access_role
enum
The access role of the user. Options are **st** (standard user), **adm** (admin user), or **ro** (read-only user). Allowed enum values: `st,adm,ro,ERROR`
saml_autocreate_users_domains
object
Has two properties, `enabled` (boolean) and `domains`, which is a list of domains without the @ symbol.
domains
[string]
List of domains where the SAML automated user creation is enabled.
enabled
boolean
Whether or not the automated user creation based on SAML domain is enabled.
saml_can_be_enabled
boolean
Whether or not SAML can be enabled for this organization.
saml_idp_endpoint
string
Identity provider endpoint for SAML authentication.
saml_idp_initiated_login
object
Has one property enabled (boolean).
enabled
boolean
Whether SAML IdP initiated login is enabled, learn more in the [SAML documentation](https://docs.datadoghq.com/account_management/saml/#idp-initiated-login).
saml_idp_metadata_uploaded
boolean
Whether or not a SAML identity provider metadata file was provided to the Datadog organization.
saml_login_url
string
URL for SAML logging.
saml_strict_mode
object
Has one property enabled (boolean).
enabled
boolean
Whether or not the SAML strict mode is enabled. If true, all users must log in with SAML. Learn more on the [SAML Strict documentation](https://docs.datadoghq.com/account_management/saml/#saml-strict).
subscription
object
**DEPRECATED** : Subscription definition.
type
string
The subscription type. Types available are `trial`, `free`, and `pro`.
trial
boolean
Only available for MSP customers. Allows child organizations to be created on a trial plan.
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/organizations/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/organizations/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/organizations/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/organizations/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/organizations/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/organizations/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/organizations/?code-lang=typescript)


#####  Update your organization
Copy
```
                  # Path parameters  
export public_id="abc123"  
# Curl command  
curl -X PUT "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/org/${public_id}" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{}
EOF  

                
```

#####  Update your organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update your organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update your organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update your organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Update your organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Update your organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Upload IdP metadata](https://docs.datadoghq.com/api/latest/organizations/#upload-idp-metadata)
  * [v1](https://docs.datadoghq.com/api/latest/organizations/#upload-idp-metadata-v1)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/organizations/#upload-idp-metadata-v2)


POST https://api.ap1.datadoghq.com/api/v1/org/{public_id}/idp_metadatahttps://api.ap2.datadoghq.com/api/v1/org/{public_id}/idp_metadatahttps://api.datadoghq.eu/api/v1/org/{public_id}/idp_metadatahttps://api.ddog-gov.com/api/v1/org/{public_id}/idp_metadatahttps://api.datadoghq.com/api/v1/org/{public_id}/idp_metadatahttps://api.us3.datadoghq.com/api/v1/org/{public_id}/idp_metadatahttps://api.us5.datadoghq.com/api/v1/org/{public_id}/idp_metadata
### Overview
There are a couple of options for updating the Identity Provider (IdP) metadata from your SAML IdP.
  * **Multipart Form-Data** : Post the IdP metadata file using a form post.
  * **XML Body:** Post the IdP metadata file as the body of the request.


### Arguments
#### Path Parameters
Name
Type
Description
public_id [_required_]
string
The `public_id` of the organization you are operating with
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Expand All
Field
Type
Description
idp_file [_required_]
binary
The path to the XML metadata file you wish to upload.
```
{
  "idp_file": ""
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/organizations/#UploadIdPForOrg-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/organizations/#UploadIdPForOrg-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/organizations/#UploadIdPForOrg-403-v1)
  * [415](https://docs.datadoghq.com/api/latest/organizations/#UploadIdPForOrg-415-v1)
  * [429](https://docs.datadoghq.com/api/latest/organizations/#UploadIdPForOrg-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


The IdP response object.
Expand All
Field
Type
Description
message [_required_]
string
Identity provider response.
```
{
  "message": "IdP metadata successfully uploaded for example org"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Unsupported Media Type
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/organizations/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/organizations/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/organizations/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/organizations/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/organizations/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/organizations/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/organizations/?code-lang=typescript)


#####  Upload IdP metadata
Copy
```
                  # Path parameters  
export public_id="abc123"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/org/${public_id}/idp_metadata" \
-H "Accept: application/json" \
-H "Content-Type: multipart/form-data" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-F idp_file=@string  

                
```

#####  Upload IdP metadata
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Upload IdP metadata
```
# Upload IdP metadata returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::OrganizationsAPI.new
p api_instance.upload_idp_for_org("abc123", File.open("./idp_metadata.xml", "r"))

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Upload IdP metadata
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Upload IdP metadata
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Upload IdP metadata
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Upload IdP metadata
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

POST https://api.ap1.datadoghq.com/api/v2/saml_configurations/idp_metadatahttps://api.ap2.datadoghq.com/api/v2/saml_configurations/idp_metadatahttps://api.datadoghq.eu/api/v2/saml_configurations/idp_metadatahttps://api.ddog-gov.com/api/v2/saml_configurations/idp_metadatahttps://api.datadoghq.com/api/v2/saml_configurations/idp_metadatahttps://api.us3.datadoghq.com/api/v2/saml_configurations/idp_metadatahttps://api.us5.datadoghq.com/api/v2/saml_configurations/idp_metadata
### Overview
Endpoint for uploading IdP metadata for SAML setup.
Use this endpoint to upload or replace IdP metadata for SAML login configuration.
This endpoint requires the `org_management` permission.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Expand All
Field
Type
Description
idp_file
binary
The IdP metadata XML file
```
{
  "idp_file": "string"
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/organizations/#UploadIdPMetadata-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/organizations/#UploadIdPMetadata-400-v2)
  * [403](https://docs.datadoghq.com/api/latest/organizations/#UploadIdPMetadata-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/organizations/#UploadIdPMetadata-429-v2)


OK
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/organizations/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/organizations/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/organizations/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/organizations/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/organizations/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/organizations/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/organizations/?code-lang=typescript)


#####  Upload IdP metadata
Copy
```
                  # Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/saml_configurations/idp_metadata" \
-H "Accept: application/json" \
-H "Content-Type: multipart/form-data" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-F idp_file=@string  

                
```

#####  Upload IdP metadata
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Upload IdP metadata
```
# Upload IdP metadata returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OrganizationsAPI.new
opts = {
  idp_file: File.open("fixtures/organizations/saml_configurations/valid_idp_metadata.xml", "r"),
}
p api_instance.upload_idp_metadata(opts)

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Upload IdP metadata
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Upload IdP metadata
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Upload IdP metadata
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Upload IdP metadata
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Spin-off Child Organization](https://docs.datadoghq.com/api/latest/organizations/#spin-off-child-organization)
  * [v1 (latest)](https://docs.datadoghq.com/api/latest/organizations/#spin-off-child-organization-v1)


POST https://api.ap1.datadoghq.com/api/v1/org/{public_id}/downgradehttps://api.ap2.datadoghq.com/api/v1/org/{public_id}/downgradehttps://api.datadoghq.eu/api/v1/org/{public_id}/downgradehttps://api.ddog-gov.com/api/v1/org/{public_id}/downgradehttps://api.datadoghq.com/api/v1/org/{public_id}/downgradehttps://api.us3.datadoghq.com/api/v1/org/{public_id}/downgradehttps://api.us5.datadoghq.com/api/v1/org/{public_id}/downgrade
### Overview
Only available for MSP customers. Removes a child organization from the hierarchy of the master organization and places the child organization on a 30-day trial.
### Arguments
#### Path Parameters
Name
Type
Description
public_id [_required_]
string
The `public_id` of the organization you are operating within.
### Response
  * [200](https://docs.datadoghq.com/api/latest/organizations/#DowngradeOrg-200-v1)
  * [400](https://docs.datadoghq.com/api/latest/organizations/#DowngradeOrg-400-v1)
  * [403](https://docs.datadoghq.com/api/latest/organizations/#DowngradeOrg-403-v1)
  * [429](https://docs.datadoghq.com/api/latest/organizations/#DowngradeOrg-429-v1)


OK
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Status of downgrade
Expand All
Field
Type
Description
message
string
Information pertaining to the downgraded child organization.
```
{
  "message": "string"
}
```

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Error response object.
Expand All
Field
Type
Description
errors [_required_]
[string]
Array of errors returned by the API.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/organizations/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/organizations/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/organizations/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/organizations/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/organizations/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/organizations/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/organizations/?code-lang=typescript)


#####  Spin-off Child Organization
Copy
```
                  # Path parameters  
export public_id="abc123"  
# Curl command  
curl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v1/org/${public_id}/downgrade" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Spin-off Child Organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Spin-off Child Organization
```
# Spin-off Child Organization returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V1::OrganizationsAPI.new
p api_instance.downgrade_org("abc123")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Spin-off Child Organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Spin-off Child Organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Spin-off Child Organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Spin-off Child Organization
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [List Org Configs](https://docs.datadoghq.com/api/latest/organizations/#list-org-configs)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/organizations/#list-org-configs-v2)


GET https://api.ap1.datadoghq.com/api/v2/org_configshttps://api.ap2.datadoghq.com/api/v2/org_configshttps://api.datadoghq.eu/api/v2/org_configshttps://api.ddog-gov.com/api/v2/org_configshttps://api.datadoghq.com/api/v2/org_configshttps://api.us3.datadoghq.com/api/v2/org_configshttps://api.us5.datadoghq.com/api/v2/org_configs
### Overview
Returns all Org Configs (name, description, and value).
### Response
  * [200](https://docs.datadoghq.com/api/latest/organizations/#ListOrgConfigs-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/organizations/#ListOrgConfigs-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/organizations/#ListOrgConfigs-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/organizations/#ListOrgConfigs-403-v2)
  * [429](https://docs.datadoghq.com/api/latest/organizations/#ListOrgConfigs-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


A response with multiple Org Configs.
Field
Type
Description
data [_required_]
[object]
An array of Org Configs.
attributes [_required_]
object
Readable attributes of an Org Config.
description [_required_]
string
The description of an Org Config.
modified_at
date-time
The timestamp of the last Org Config update (if any).
name [_required_]
string
The machine-friendly name of an Org Config.
value [_required_]
The value of an Org Config.
value_type [_required_]
string
The type of an Org Config value.
id [_required_]
string
A unique identifier for an Org Config.
type [_required_]
enum
Data type of an Org Config. Allowed enum values: `org_configs`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/organizations/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/organizations/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/organizations/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/organizations/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/organizations/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/organizations/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/organizations/?code-lang=typescript)


#####  List Org Configs
Copy
```
                  # Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/org_configs" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  List Org Configs
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  List Org Configs
```
# List Org Configs returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OrganizationsAPI.new
p api_instance.list_org_configs()

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  List Org Configs
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  List Org Configs
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  List Org Configs
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  List Org Configs
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Get a specific Org Config value](https://docs.datadoghq.com/api/latest/organizations/#get-a-specific-org-config-value)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/organizations/#get-a-specific-org-config-value-v2)


GET https://api.ap1.datadoghq.com/api/v2/org_configs/{org_config_name}https://api.ap2.datadoghq.com/api/v2/org_configs/{org_config_name}https://api.datadoghq.eu/api/v2/org_configs/{org_config_name}https://api.ddog-gov.com/api/v2/org_configs/{org_config_name}https://api.datadoghq.com/api/v2/org_configs/{org_config_name}https://api.us3.datadoghq.com/api/v2/org_configs/{org_config_name}https://api.us5.datadoghq.com/api/v2/org_configs/{org_config_name}
### Overview
Return the name, description, and value of a specific Org Config.
### Arguments
#### Path Parameters
Name
Type
Description
org_config_name [_required_]
string
The name of an Org Config.
### Response
  * [200](https://docs.datadoghq.com/api/latest/organizations/#GetOrgConfig-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/organizations/#GetOrgConfig-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/organizations/#GetOrgConfig-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/organizations/#GetOrgConfig-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/organizations/#GetOrgConfig-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/organizations/#GetOrgConfig-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


A response with a single Org Config.
Field
Type
Description
data [_required_]
object
A single Org Config.
attributes [_required_]
object
Readable attributes of an Org Config.
description [_required_]
string
The description of an Org Config.
modified_at
date-time
The timestamp of the last Org Config update (if any).
name [_required_]
string
The machine-friendly name of an Org Config.
value [_required_]
The value of an Org Config.
value_type [_required_]
string
The type of an Org Config value.
id [_required_]
string
A unique identifier for an Org Config.
type [_required_]
enum
Data type of an Org Config. Allowed enum values: `org_configs`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/organizations/?code-lang=curl)
  * [Python](https://docs.datadoghq.com/api/latest/organizations/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/organizations/?code-lang=ruby)
  * [Go](https://docs.datadoghq.com/api/latest/organizations/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/organizations/?code-lang=java)
  * [Rust](https://docs.datadoghq.com/api/latest/organizations/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/organizations/?code-lang=typescript)


#####  Get a specific Org Config value
Copy
```
                  # Path parameters  
export org_config_name="monitor_timezone"  
# Curl command  
curl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/org_configs/${org_config_name}" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"  

                
```

#####  Get a specific Org Config value
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Get a specific Org Config value
```
# Get a specific Org Config value returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::OrganizationsAPI.new
p api_instance.get_org_config("custom_roles")

```

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Get a specific Org Config value
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Get a specific Org Config value
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Get a specific Org Config value
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Get a specific Org Config value
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
## [Update a specific Org Config](https://docs.datadoghq.com/api/latest/organizations/#update-a-specific-org-config)
  * [v2 (latest)](https://docs.datadoghq.com/api/latest/organizations/#update-a-specific-org-config-v2)


PATCH https://api.ap1.datadoghq.com/api/v2/org_configs/{org_config_name}https://api.ap2.datadoghq.com/api/v2/org_configs/{org_config_name}https://api.datadoghq.eu/api/v2/org_configs/{org_config_name}https://api.ddog-gov.com/api/v2/org_configs/{org_config_name}https://api.datadoghq.com/api/v2/org_configs/{org_config_name}https://api.us3.datadoghq.com/api/v2/org_configs/{org_config_name}https://api.us5.datadoghq.com/api/v2/org_configs/{org_config_name}
### Overview
Update the value of a specific Org Config. This endpoint requires the `org_management` permission.
### Arguments
#### Path Parameters
Name
Type
Description
org_config_name [_required_]
string
The name of an Org Config.
### Request
#### Body Data (required)
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


Field
Type
Description
data [_required_]
object
An Org Config write operation.
attributes [_required_]
object
Writable attributes of an Org Config.
value [_required_]
The value of an Org Config.
type [_required_]
enum
Data type of an Org Config. Allowed enum values: `org_configs`
```
{
  "data": {
    "attributes": {
      "value": "UTC"
    },
    "type": "org_configs"
  }
}
```

Copy
### Response
  * [200](https://docs.datadoghq.com/api/latest/organizations/#UpdateOrgConfig-200-v2)
  * [400](https://docs.datadoghq.com/api/latest/organizations/#UpdateOrgConfig-400-v2)
  * [401](https://docs.datadoghq.com/api/latest/organizations/#UpdateOrgConfig-401-v2)
  * [403](https://docs.datadoghq.com/api/latest/organizations/#UpdateOrgConfig-403-v2)
  * [404](https://docs.datadoghq.com/api/latest/organizations/#UpdateOrgConfig-404-v2)
  * [429](https://docs.datadoghq.com/api/latest/organizations/#UpdateOrgConfig-429-v2)


OK
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


A response with a single Org Config.
Field
Type
Description
data [_required_]
object
A single Org Config.
attributes [_required_]
object
Readable attributes of an Org Config.
description [_required_]
string
The description of an Org Config.
modified_at
date-time
The timestamp of the last Org Config update (if any).
name [_required_]
string
The machine-friendly name of an Org Config.
value [_required_]
The value of an Org Config.
value_type [_required_]
string
The type of an Org Config value.
id [_required_]
string
A unique identifier for an Org Config.
type [_required_]
enum
Data type of an Org Config. Allowed enum values: `org_configs`
```
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

Copy
Bad Request
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Unauthorized
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Forbidden
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Not Found
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
Too many requests
  * [Model](https://docs.datadoghq.com/api/latest/organizations/)
  * [Example](https://docs.datadoghq.com/api/latest/organizations/)


API error response.
Expand All
Field
Type
Description
errors [_required_]
[string]
A list of errors.
```
{
  "errors": [
    "Bad Request"
  ]
}
```

Copy
### Code Example
  * [Curl](https://docs.datadoghq.com/api/latest/organizations/?code-lang=curl)
  * [Go](https://docs.datadoghq.com/api/latest/organizations/?code-lang=go)
  * [Java](https://docs.datadoghq.com/api/latest/organizations/?code-lang=java)
  * [Python](https://docs.datadoghq.com/api/latest/organizations/?code-lang=python)
  * [Ruby](https://docs.datadoghq.com/api/latest/organizations/?code-lang=ruby)
  * [Rust](https://docs.datadoghq.com/api/latest/organizations/?code-lang=rust)
  * [Typescript](https://docs.datadoghq.com/api/latest/organizations/?code-lang=typescript)


#####  Update a specific Org Config returns "OK" response
Copy
```
                          # Path parameters  
export org_config_name="monitor_timezone"  
# Curl command  
curl -X PATCH "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/org_configs/${org_config_name}" \
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

                        
```

#####  Update a specific Org Config returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" go run "main.go"


```

#####  Update a specific Org Config returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" java "Example.java"


```

#####  Update a specific Org Config returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" python3 "example.py"


```

#####  Update a specific Org Config returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" rb "example.rb"


```

#####  Update a specific Org Config returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" cargo run


```

#####  Update a specific Org Config returns "OK" response
```
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

Copy
#### Instructions
First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
```
    

DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" tsc "example.ts"


```

* * *
![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=e180c467-c59a-4ecc-bc01-8aa5c1f58f3a&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=3b28bc21-1483-4bbf-a1e6-27c4ffc6b4da&pt=Organizations&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Forganizations%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=e180c467-c59a-4ecc-bc01-8aa5c1f58f3a&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=3b28bc21-1483-4bbf-a1e6-27c4ffc6b4da&pt=Organizations&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Forganizations%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=f95442e9-5045-451e-92c8-a7df85e77281&bo=2&sid=ca97aff0f0bf11f0b225ebe7018368cd&vid=ca980060f0bf11f09385b797b877861f&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Organizations&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Forganizations%2F&r=&lt=2167&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=940443)
