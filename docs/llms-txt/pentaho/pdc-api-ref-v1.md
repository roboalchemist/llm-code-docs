# Source: https://docs.pentaho.com/pdc-api-docs/v1/pdc-api-ref-v1.md

# PDC API Reference

The Pentaho Data Catalog (PDC) API exposes a set of RESTful endpoints that allow you to interact programmatically with your catalog. The reference is organized into logical groups so you can quickly find the endpoints you need. Each endpoint page includes details about request methods, parameters, request/response schemas, error codes, and code examples.

## How to use this reference

This API Reference is designed to help you explore and use the PDC API effectively. Each endpoint page provides the information you need to build, test, and integrate requests into your workflows.

* **Navigation:** Endpoints are organized into logical groups (such as *Health*, *Auth*, *Search*, and *Data Sources*) so you can quickly locate the functionality you need. Use the sidebar to browse by domain.
* **Schemas:** Every endpoint includes request and response schemas, with clear field descriptions, data types, and example payloads. This helps you understand exactly what to send and what to expect back.
* **Error codes:** Standard error responses are listed for each endpoint. These include sample error objects with status codes, messages, and possible causes.
* **Code examples:** Ready-to-use code snippets are provided in multiple languages. All endpoints include a `curl` example, and some also provide JavaScript, Python, or Java examples for quick integration.
* **Authorization:** All endpoints (except the `Health` check) require a valid bearer token in the `Authorization` header. Refer to the Authentication page to learn how to obtain and use tokens.

## Endpoint groups

The following groups of endpoints are available:

<table data-view="cards"><thead><tr><th>Group</th><th>Description</th><th data-hidden>Endpoint(s)</th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><a data-mention href="pdc-api-ref-v1/auth">auth</a></td><td>Authenticate with username and password to obtain a bearer token for secure API access.</td><td><code>/api/public/v1/auth</code></td><td><a href="auth#post-api-public-v1-auth">#post-api-public-v1-auth</a></td></tr><tr><td><a data-mention href="pdc-api-ref-v1/data-entities">data-entities</a></td><td>Get, update, or filter entities and fetch profiling information for metadata analysis.</td><td><code>/api/public/v1/entities/...</code> (single, bulk, filter, profiling)</td><td><a href="data-entities#get-api-public-v1-entities-id">#get-api-public-v1-entities-id</a></td></tr><tr><td><a data-mention href="pdc-api-ref-v1/data-sources">data-sources</a></td><td>Create, retrieve, and manage data source connections across databases, files, and cloud stores.</td><td><code>/api/public/v1/data-sources</code></td><td><a href="data-sources#get-api-public-v1-data-sources-id">#get-api-public-v1-data-sources-id</a></td></tr><tr><td><a data-mention href="pdc-api-ref-v1/data-collections">data-collections</a></td><td>Manage datasets, collections, categories, and groups to organize catalog content.</td><td><code>/api/public/v1/data-collections</code></td><td><a href="data-collections#get-api-public-v1-data-collections-id">#get-api-public-v1-data-collections-id</a></td></tr><tr><td><a data-mention href="pdc-api-ref-v1/jobs">jobs</a></td><td>Run and monitor background jobs such as profiling, ingestion, or schema scanning.</td><td><code>/api/public/v1/job/execution</code></td><td><a href="jobs#get-api-public-v1-jobs-id-status">#get-api-public-v1-jobs-id-status</a></td></tr><tr><td><a data-mention href="pdc-api-ref-v1/licensing">licensing</a></td><td>Retrieve licensing information and manage offline licenses in Data Catalog.</td><td><code>/api/public/v1/licensing/licenses</code></td><td><a href="pdc-api-ref-v1/licensing">licensing</a></td></tr><tr><td><a data-mention href="pdc-api-ref-v1/notifications">notifications</a></td><td>Retrieve or create notifications to track system events, data changes, or catalog activity.</td><td><code>/api/public/v1/notifications</code></td><td><a href="notifications#get-api-public-v1-notifications">#get-api-public-v1-notifications</a></td></tr><tr><td><a data-mention href="pdc-api-ref-v1/search">search</a></td><td>Search catalog assets and retrieve facets to filter results for discovery and analytics.</td><td><code>/api/public/v1/search</code>, <code>/api/public/v1/search/facets</code></td><td><a href="search#post-api-public-v1-search">#post-api-public-v1-search</a></td></tr></tbody></table>

## Conventions

All PDC API endpoints follow these conventions:

* **Base path**: All endpoints are hosted under:

  ```
  https://<your-domain>/api/public/v1/
  ```
* **Authentication**: Except for the Health endpoint, all requests require a bearer token. Add the token to your request headers:

  ```
  Authorization: Bearer <accessToken>
  ```
* **Request/response format**: JSON
* **Errors**: Consistent error objects are returned across endpoints.
