# Workato Documentation

Source: https://workato.docs.buildwithfern.com/llms-full.txt

---

***

title: Welcome to our documentation
description: Here you'll find everything you need to make Workato work for you.
layout: overview
----------------

Workato helps you automate business workflows across cloud and on-premises apps, combining an enterprise-grade workflow automation platform with the ease of use expected from consumer apps. This website helps you navigate and utilize those features to the fullest extent.

## Getting Started

<Cards>
  <Card title="Getting Started" icon="fa-regular fa-play" href="/get-started/intro">
    Everything you need to get up and running with Workato.
  </Card>

  <Card title="API Clients" icon="fa-solid fa-book" href="/get-started/clients">
    Enforce security best practices with configurable clients.
  </Card>

  <Card title="API Reference" icon="fa-solid fa-code" href="/api-reference">
    Access the Workato API endpoints.
  </Card>

  <Card title="Get Workato Certified" icon="fa-solid fa-shield-halved" href="https://academy.workato.com/?_gl=1*1eoamh3*_gcl_au*MTQ0MzIzMjkxNC4xNzEzODA5NDYz">
    Training & Certification in using Workato.
  </Card>
</Cards>

## Get support

Want to get in touch with the Workato team? Reach out to us via [email](mailto:info@workato.com). We're here to help!


***

title: Introduction to Workato's API
description: Learn about the key concepts of the Workato API.
-------------------------------------------------------------

# Developer API

Workato's developer API provides access to various Workato resources, through which you can manage recipes, connections, and jobs. This allows your to automate all aspects of your Workato workspace - from deploying recipe manifests from development to production or deploying new on-prem agents within your network landscape.

## Base URL

The Workato API is a collection of API endpoints for interacting with Workato users, recipes, and much more. Each endpoint contains the **base URL** and the **resource path** to the object.

The base URL of the API endpoint depends on the [data center](/get-started) that you use. Here are Workato data centers:

* US Data Center: `https://www.workato.com/api/`
* EU Data Center: `https://app.eu.workato.com/api/`
* JP Data Center: `https://app.jp.workato.com/api/`
* SG Data Center: `https://app.sg.workato.com/api/`
* AU Data Center: `https://app.au.workato.com/api/`

## Authentication

Workato API uses API tokens to authenticate requests. You may generate an API token by creating an API client under Workspace admin and assigning it both a client role and project scopes.

<Callout intent="warning" title="Legacy API key deprecation">
  Prior to API clients, Workato's API used a legacy full access API key and email in **request headers** or the **query parameters** to authenticate requests. This will continue to be supported with your legacy migrated API client that represents your API key and email. We strongly recommend migrating over to API Clients for authentication to Workato APIs. [Learn more](/get-started)

  Legacy API keys will be supported until 1/1/2024 and will be deprecated thereafter. All API requests authenticated via legacy API keys will start to be rejected after this point in time.
</Callout>

### Provide API Tokens as a Bearer Token

Provide your API client's API token in the request headers as a `bearer` token.

<CodeBlocks>
  ```curl title=""
  curl -X GET https://www.workato.com/api/users/me \
        -H 'Authorization: Bearer <api_token>'
  ```
</CodeBlocks>

### Supported Formats

Workato API supports sending request body with the `application/json` content-type. All replies are also encoded in `application/json; charset=utf-8`.

## How to Generate an API Token

<Callout intent="note" title="Permission Requirements">
  To create or edit API clients, you'll need the [**Workspace Owner** or **Admin** system role](./docs/pages/todo), or [**API Clients** privileges found under Workspace admin](/get-started)
</Callout>

You can generate an API token by creating an API Client under Workspace admin and under the API Clients tab. [Find out more about configuring API clients and roles.](/get-started/clients)

## HTTP Response Codes

| Name  | Description  | Sample reply                                |
| ----- | ------------ | ------------------------------------------- |
| `200` | Success      | `{"Success": true}`                         |
| `400` | Bad request  | `{"message": "Bad request"}`                |
| `401` | Unauthorized | `{"message": "Unauthorized"}`               |
| `404` | Not found    | `{"message": "Not found"}`                  |
| `500` | Server error | `{"message":"Server error","id":"3188..."}` |


***

title: API Clients
description: Providing customizable access to API endpoints for improved security
---------------------------------------------------------------------------------

<Callout intent="note" title="Page Summary">
  * Workato API clients provide customizable access to API endpoints for improved security.
  * You must define a client role and access level to create an API client. After you create a view-once API token, save and store it securely.
  * Client and role updates take effect immediately. Deleting a client or role immediately rejects associated API requests.
  * API client tokens can be refreshed for security.
</Callout>

API clients allow you to enforce security best practices by creating multiple clients with configurable access to each endpoint. API client requests require a single header for authentication.

<Callout intent="warning" title="Legacy Full Access API Keys">
  Prior to API clients, Workato's API used a legacy full-access API key and email in **request headers** or the **query parameters** to authenticate requests. This legacy feature is still supported, however we strongly recommend that you migrate to API clients for authentication. [Learn more](/get-started)

  Note that migration is different from deletion. If you delete the legacy API client, your API key and email cannot be recovered and requests using this API key and email will be rejected.
</Callout>

## API Client Benefits

Workato's developer and embedded APIs allow you to automate your Workato workspace, including deploying recipe manifests from development to production and deploying new on-prem agents within your network landscape. API clients allow you to improve your organization's security by provisioning API access specific to each application's use case.

API clients and assignable roles allow you to scope API access on different levels:

* API clients are assigned roles that define the API endpoints they can interact with.
* API clients are assigned environments, for example DEV, TEST, or PROD, that they are allowed to make API calls to. **Environments are an add-on feature and may not be available to your workspace**.
* API clients are assigned projects. This limits API access to specific assets within those projects.

You can create individual clients specific to API endpoints and to various projects within your workspace. Workato Developer API client tokens are integrated with [Github Secret Scanning](/get-started).

## Create a Client Role

You must create a client role before you create an API client. The client role allows you to configure which endpoints the API client can access.

To create a client role:

<Steps toc={false}>
  ### Step 1

  Navigate to **Workspace admin**.

  ### Step 2

  Select **API clients > Client roles > Add client role**.

  <img src="https://lh3.googleusercontent.com/d/1iyt3ArX4u2KbDVaDlMTXjB7DgQkzBSPJ=s2200" alt="Creating a new client role" width={1000} />

  ### Step 3

  Enter a **name** for the new client role. For example, "Recipe Operator" for a role that can interact with Recipe API endpoints.

  ### Step 4

  Select the **required endpoints** for the role under each section. All Workato API endpoints available to your workspace are listed under these sections.

  ### Step 5

  **Save** your role after you are done with your selections. You can [edit the client role](#edit-a-client-role) later if needed.
</Steps>

## Create an API Client

To create an API client:

<Steps toc={false}>
  ### Step 1

  Navigate to **Workspace admin**.

  ### Step 2

  Select **API clients > Create API client**.

  <img src="https://lh3.googleusercontent.com/d/1mf5JQPi_n4a3Wii8dBfQEpkRngIU6hNr=s2200" alt="Creating a new API client" width={1000} />

  ### Step 3

  Enter a **name** for the new client that reflects its purpose. For example, "Sales and Marketing - Recipe Operator" for an API client that will be used by the Sales and Marketing team to operate their recipes through the API.

  ### Step 4

  Select the appropriate **client role**. The client role determines which endpoints the API client can access.

  ### Step 5

  If your workspace has **environments** enabled, select the environment the API client is allowed to access.

  ### Step 6

  Select the **projects** the API client is allowed to access. Choose only the projects that are related to the team that will use this API client. Project access rules apply to all assets that can be scoped to projects including: `connections`, `recipes`, `folders`, `lookup tables`, `properties`, `API Platform collections` and `API Platform API Clients`.

  <Callout intent="warning" title="Client Access">
    API clients for Embedded partners with access to embedded APIs can access all customer workspaces and projects.
  </Callout>

  ### Step 7

  Optionally, add **allowed IP ranges** that API requests using this token can originate from. If you call our APIs from a static server, this further secures access to Workato's developer APIs.

  ### Step 8

  **Store the API token** that displays after creating your API client in a secure location, such as AWS Secrets Manager. You will not be able to retrieve the API token again.

  ### Step 9

  **Save** the API client when you done with your configurations. You can [edit the API client](#edit-an-api-client) later if needed.
</Steps>

<img src="https://lh3.googleusercontent.com/d/1bW7NaWyiKGtCcdkJElMtg72AUSkDFk0P=s2200" alt="New view-once API token" width={1000} />

## Edit a Client Role

Edits made to client roles are immediately enforced.

To edit an API client role:

<Steps toc={false}>
  ### Step 1

  Navigate to **Workspace admin**.

  ### Step 2

  Select **API clients > Client roles >** select the client role you want to edit.

  ### Step 3

  Add or remove privileges to the client role, and/or edit project access. This immediately impacts all incoming API requests from associated API clients.

  ### Step 4

  **Save** your changes.
</Steps>

## Edit an API Client

Edits made to an API client are immediately enforced.

To edit an API client:

<Steps toc={false}>
  ### Step 1

  Navigate to **Workspace admin**.

  ### Step 2

  Select **API clients >** select the API client you want to edit.

  ### Step 3

  Change the client role, and/or edit project access. This immediately impacts all incoming API requests from associated API clients.

  ### Step 4

  **Save** your changes.
</Steps>

## Refresh API Client Tokens

After creating an API client, you can regenerate a new API token for the existing client. To refresh an API client token:

<Steps toc={false}>
  ### Step 1

  Navigate to **Workspace admin**.

  ### Step 2

  Select **API clients >** select the API client you want to edit.

  ### Step 3

  Select the **refresh** icon located in the top right corner of the page.

  <img src="https://lh3.googleusercontent.com/d/13ohBqvIaEDeQFjr7PANg658szy-yI5tI=s2200" alt="Selecting the refresh icon to refresh the API client token" width={1000} />

  ### Step 4

  In the **Regenerate API token** modal, select **Regenerate token**. When you regenerate an API token, API calls using your previous API token will fail.

  ### Step 5

  Store your new API token in a secure location, such as AWS Secrets Manager. You will not be able to retrieve this API token again.

  ### Step 6

  Select **Done** to return to editing the API client.
</Steps>

Generating a new token invalidates the previous API token. **Legacy API client tokens cannot be regenerated.**

User error can cause compromised tokens when dealing with custom scripts or applications that upload tokens in plain text to public websites, such as GitHub public repositories or documentation.

## Delete an API Client or Client Role

Use caution when deleting an API client or client role.

* **Deleted API client:** All incoming requests that use the API token of the deleted API client will be rejected.

* **Deleted client role:** All incoming requests from associated API clients will be rejected.

## FAQs for Managing API Clients and Client Roles

<AccordionGroup toc={false}>
  <Accordion title="How should I configure client roles?">
    Client roles should be configured with use cases in mind. For example, a "Recipe Operator" client role might have endpoint access to start/stop recipes whereas a "Project Deployment" client role might have access to Recipe Lifecycle Management and Environment Properties endpoints. This can be used in conjunction with project scoping on the API client level to achieve access scoped to both use cases and projects.

    As a best practice, the principle of least privilege should be employed when defining client roles.
  </Accordion>

  <Accordion title="How should I configure API clients?">
    Configure API clients with the use case and project in mind. For example, a "Sales and Marketing - Recipe Operator" API client can be provisioned specifically for the Sales and Marketing team. API client configuration allows you to be specific when you define permissions as this increases security, however this also increases complexity as you have to manage more API tokens.
  </Accordion>

  <Accordion title="Where should I store my API client tokens?">
    API client tokens are view-once, meaning that if they are misplaced, they are lost forever. To recover the API client, you must regenerate the token.

    Ensure that you store your API tokens in a secure location with controlled access. We recommend you consider tools like AWS Secrets Manager as a way to manage these tokens, especially if you are planning to generate multiple tokens for different teams.
  </Accordion>

  <Accordion title="Who has access to API clients and how do I control access?">
    All admins in your workspace have access to API clients. This privilege is defined in the "Workspace admin" Admin role. Use caution when adding users as Admins as they have the ability to create, edit, and delete API clients which may impact existing automated workflows using Workato's APIs.

    When creating custom roles in your team, you can define access to API clients under the **Workspace admin** section and selecting API clients. Any user assigned this custom role will have full access to the API clients tool.
  </Accordion>

  <Accordion title="Why are some endpoints not compatible in my &#x22;TEST&#x22; and &#x22;PROD&#x22; environments?">
    Certain API endpoints in Workato are only available in the "DEV" environment such as "Project deployments" and "Workspace Collaborators". This is because you can only manage these tools from your "DEV" environment.
  </Accordion>
</AccordionGroup>


# List

GET https://api.workato.com/api/recipes/{recipe_id}/jobs

Returns aggregated job information as well as detailed job information for a specified recipe in Workato.

Reference: https://workato.docs.buildwithfern.com/api-reference/jobs/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: api
  version: 1.0.0
paths:
  /recipes/{recipe_id}/jobs:
    get:
      operationId: list
      summary: List
      description: >-
        Returns aggregated job information as well as detailed job information
        for a specified recipe in Workato.
      tags:
        - subpackage_jobs
      parameters:
        - name: recipe_id
          in: path
          description: The ID of the recipe for which you want to retrieve job information.
          required: false
          schema:
            type: string
        - name: offset_job_id
          in: query
          description: >-
            The ID of the job from which you want to start retrieving job
            information.
          required: false
          schema:
            type: string
        - name: prev
          in: query
          description: >-
            Defaults to `false`. When prev=false, this call returns jobs
            completed prior to the offset_job_id. If prev=true, jobs newer than
            the offset_job_id are returned.
          required: false
          schema:
            type: boolean
        - name: status
          in: query
          description: Filter by status - succeeded, failed, or pending.
          required: false
          schema:
            type: string
        - name: rerun_only
          in: query
          description: If true, returns jobs that were rerun only.
          required: false
          schema:
            type: boolean
        - name: offset_run_id
          in: query
          description: Offset run ID. This parameter has been deprecated.
          required: false
          schema:
            type: integer
        - name: failed
          in: query
          description: >-
            If true, returns failed jobs only. This parameter has been
            deprecated.
          required: false
          schema:
            type: boolean
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Response with status 200
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_jobs:ListJobsResponse'
servers:
  - url: https://api.workato.com/api
components:
  schemas:
    type_jobs:error_part:
      type: object
      properties:
        adapter:
          type: string
          description: Adapter involved in the error.
        error_type:
          type: string
          description: Type of error encountered.
        message:
          type: string
          description: Description of the error.
        error_id:
          type: string
          description: Unique identifier for the error.
        error_at:
          type: string
          description: Timestamp when the error occurred.
        input:
          type: string
          description: Input involved in the error, content redacted.
        inner_message:
          type: string
          description: More detailed internal message if available.
      required:
        - adapter
        - error_type
        - message
        - error_id
        - error_at
        - input
      description: Detailed breakdown of the error.
      title: error_part
    type_jobs:item:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for the job.
        flow_run_id:
          type: integer
          description: Flow run identifier.
        completed_at:
          type: string
          description: Timestamp when the job was completed.
        started_at:
          type: string
          description: Timestamp when the job was started.
        title:
          type: string
          description: Detailed description of the job.
        is_poll_error:
          type: boolean
          description: Indicates if there was a polling error.
        error:
          $ref: '#/components/schemas/type_jobs:error_part'
          description: Detailed error message if an error occurred.
        is_error:
          type: boolean
          description: Indicates if the job encountered an error.
      required:
        - id
        - flow_run_id
        - completed_at
        - started_at
        - title
        - is_poll_error
      title: item
    type_jobs:ListJobsResponse:
      type: object
      properties:
        job_succeeded_count:
          type: integer
          description: Number of succeeded jobs.
        job_failed_count:
          type: integer
          description: Number of failed jobs.
        job_count:
          type: integer
          description: Total number of jobs returned.
        items:
          type: array
          items:
            $ref: '#/components/schemas/type_jobs:item'
          description: List of job details.
      required:
        - job_succeeded_count
        - job_failed_count
        - job_count
        - items
      title: ListJobsResponse
  securitySchemes:
    BearerAuthScheme:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.workato.com/api/recipes/recipe_1/jobs"

querystring = {"offset_job_id":"job_1","prev":"false","status":"failed","rerun_only":"true"}

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'https://api.workato.com/api/recipes/recipe_1/jobs?offset_job_id=job_1&prev=false&status=failed&rerun_only=true';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.workato.com/api/recipes/recipe_1/jobs?offset_job_id=job_1&prev=false&status=failed&rerun_only=true"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.workato.com/api/recipes/recipe_1/jobs?offset_job_id=job_1&prev=false&status=failed&rerun_only=true")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.workato.com/api/recipes/recipe_1/jobs?offset_job_id=job_1&prev=false&status=failed&rerun_only=true")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.workato.com/api/recipes/recipe_1/jobs?offset_job_id=job_1&prev=false&status=failed&rerun_only=true', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.workato.com/api/recipes/recipe_1/jobs?offset_job_id=job_1&prev=false&status=failed&rerun_only=true");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.workato.com/api/recipes/recipe_1/jobs?offset_job_id=job_1&prev=false&status=failed&rerun_only=true")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

