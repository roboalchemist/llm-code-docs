# Source: https://developers.webflow.com/data/reference/versioning.mdx

***

title: Versioning
slug: data/reference/versioning
hidden: false
-------------

API v2 versioning is **explicit** as part of the API endpoint URI.

## Versions

API v2 is composed of two version namespaces:

| Namespace | Description                                          |
| :-------- | :--------------------------------------------------- |
| `/beta/`  | A monolithic version that houses all new APIs.       |
| `/v2/`    | A subset of v2 APIs that are considered "production" |

Auth tokens will be compatible across the v2 beta and v2 production namespaces

## URL

An example of an API request to v2 beta:

<CodeBlocks>
  ```curl cURL
  curl --request GET \
       --url https://api.webflow.com/beta/token/authorized_by \
       --header 'accept: application/json'
  ```
</CodeBlocks>

## Webflow SDK

Currently, the Webflow SDK doesn't support requests to beta endpoints. For access to these endpoints, please refer to the Webflow API documentation and make requests directly through an HTTP client or your preferred API tool.
