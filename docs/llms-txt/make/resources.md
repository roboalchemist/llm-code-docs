# Source: https://developers.make.com/api-documentation/getting-started/resources.md

# Resources

API resources are grouped into sections corresponding with Make features and components.

Each endpoint resource contains the following details:

## Methods and endpoints

[Methods](https://developers.make.com/api-documentation/getting-started/http-methods) define the allowed interaction and endpoints define how to access the resource — what URI should be used to interact with a resource.

**Example:** `GET /data-stores`

## Required scopes

Defines what resources you are allowed to interact with based on scopes you selected when creating your [API access token](https://developers.make.com/api-documentation/authentication/create-authentication-token).

**Example:** `datastores:write`

## Resource description

Describes the expected outcome when using an endpoint, and what Make features the resource relates to.

## Parameters

These are options you can include with a request to modify the response. Each parameter specifies whether it is required or not. Parameters are divided into two main groups:

* **Path parameters** — path parameters are always required. They are used to identify or specify the resource (usually by indicating its ID) and they should be placed inside the endpoint URI.

  **Example:** `/data-stores/54`
* **Query parameters** — query parameters are often optional. They can be used to specify the resource but they are usually used as [parameters to sort or filter resources](https://developers.make.com/api-documentation/pagination-sorting-filtering). They are placed at the end of the endpoint URI, after a question mark. Separate multiple parameters with an ampersand symbol. If a parameter contains square brackets, encode them.

  **Example:** `/data-stores?teamId=123&pg%5Boffset%5D=10`
* **Request body** — for some endpoints (mainly connected with the POST, PUT, or PATCH HTTP methods), you can also see the Request body section in the endpoint details. This section contains the description of the payload properties that are needed to modify the resource.

**Example:**

```json
{
  "name": "Customers",
  "teamId": 123,
  "datastructureId": 178,
  "maxSizeMB": 1
}
```

## Request examples

These are request samples that show how to make a request to the endpoint. They consist of the request URL and authentication token (if needed) and other elements required to make a request in the selected language.

Example of request for creating a data store:

```bash
curl -X POST https://eu1.make.dev/api/v2/data-stores 
--header 'Content-Type: application/json' 
--header 'Authorization: Token 93dc8837-2911-4711-a766-59c1167a974d' 
-d '{"name":"Customers","teamId":123,"datastructureId":1234,"maxSizeMB":1}'
```

## Response examples

These are response samples you would receive when calling the request in real life. The outcome strictly depends on the request sample. The response schema contains all possible elements available in the response. Each response has its [status code](https://developers.make.com/api-documentation/troubleshooting/http-status-codes). Example of created data store:

```json
{
  "dataStore": {
    "id": 20024,
    "name": "Customers",
    "teamId": "123",
    "datastructureId": 1234,
    "records": 0,
    "size": "0",
    "maxSize": "1048576"
  }
}
```
