# Source: https://firebase.google.com/docs/reference/apphosting/rest/v1beta/errors.md.txt

# Firebase App Hosting API Version v1beta: Error Catalog

Firebase App Hosting streamlines the development and deployment of dynamic Next.js and Angular applications, offering built-in framework support, GitHub integration, and integration with other Firebase products.

You can use this API to intervene in the Firebase App Hosting build process and add custom functionality not supported in our default Console \& CLI flows, including triggering builds from external CI/CD workflows or deploying from pre-built container images.

## Service: firebaseapphosting.googleapis.com

When facing errors, refer to this catalog alongside using our [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If you're using your own libraries, keep this guide handy for debugging and error resolution. To know more about the error response structure, visit [the error overview page](https://cloud.google.com/apis/design/errors)

## Error codes

Below is a detailed list of HTTP status codes and associated errors you may encounter when interacting with our API. Each status code is defined along with a reason and a description to help you troubleshoot and handle errors effectively in your application.

<br />

> [!NOTE]
> **Note:**This listing contains some error messages related to its API, but is not a complete listing of those messages.

<br />

| Reason | HTTP Status Code | Description |
| `OUT_DATED_ETAG` | `409` | Etag is out of date |
| `INVALID_ETAG` | `409` | Provided etag is out of date |
| `FAILED_TENANT_PROJECT_CREATION` | `409` | Failed to perform tenant project creation |
| `INVALID_JVS` | `403` | Structured justification provided is incorrect |
| `TOO_MANY_OPERATIONS` | `429` | Too many operations are currently being executed, try again later. |
| `TOO_MANY_REQUESTS` | `429` | Too many requests are currently being executed, try again later. |
| `RESOURCE_ALREADY_EXISTS` | `409` | Resource {resource_path} already exists |
| `RESOURCE_NOT_FOUND` | `404` | Resource {resource_path} was not found |
| `CHILD_RESOURCE_EXISTS` | `400` | Resource {resource_path} has nested resources. If the API supports cascading delete, set 'force' to true to delete it and its nested resources. |
| `INVALID_RESOURCE_NAME_LENGTH` | `400` | Resource name '{resource_name}' length ({resource_name_length}) exceeds the limit {limit} |
| `RESOURCE_REFERENCES_EXIST` | `400` | Resource '{resource_path}' is already being used by resource(s) '{source_resources}' |
| `LOCATION_ACCESS_DENIED` | `403` | Location {location} is not found or access is unauthorized. |
| `INVALID_NAME` | `400` | Malformed name: '{name}' |
| `INVALID_RESOURCE_PATH` | `400` | Invalid argument: 'unable to parse resource path name {resource_path}' |
| `CANNOT_PARSE_RESOURCE_PATH` | `400` | Invalid argument: 'Cannot parse path name' |
| `INVALID_LOCATION` | `400` | Invalid argument: 'unable to parse location from resource name {resource_path}' |
| `INVALID_PAGE_SIZE` | `400` | Invalid argument: 'page_size' |
| `INVALID_ENVIRONMENT_SERVICE_NAME` | `400` | Invalid argument: 'unable to resolve environment service name {env_service_name}' |
| `IAM_INVALID_ARGUMENT` | `400` | Invalid argument: 'An invalid argument was specified. Please check the fields and try again.' |
| `INVALID_REQUEST_UUID` | `400` | The request was invalid: Must be a valid UUID |
| `INCOMPATIBLE_REQUEST_ID` | `400` | The request was invalid: attempted to reuse 'request_id' for incompatible requests |
| `INVALID_UPDATE_MASK` | `400` | The request was invalid: invalid update mask |
| `INVALID_COLLECTION_PATH_FOR_AGGREGATED_LIST` | `400` | The request was invalid: given collection path not supported for aggregated list |
| `PROJECT_UNSPECIFIED` | `400` | The request was invalid: project unspecified, human access across projects not supported for this producer list |
| `INVALID_COLLECTION_PATH_FOR_PRODUCER_LIST` | `400` | The request was invalid: given collection path not supported for producer list |
| `INVALID_COLLECTION_PATTERN` | `400` | The request was invalid: given collection pattern is not supported for list |
| `MISSING_PERMISSION` | `400` | The request was invalid: at least one permission to test is required |
| `ORDER_BY_CREATE_TIME_UNSUPPORTED` | `400` | The request was invalid: sorting by create_time not supported when listing resources across locations |
| `INVALID_PAGINATION_TOKEN` | `400` | The request was invalid: invalid pagination token |
| `INVALID_PAGE_TOKEN` | `400` | The request was invalid: invalid page token |
| `SORTING_UNSUPPORTED` | `400` | The request was invalid: sorting not supported when listing resources across containers |
| `SORTING_NOT_SUPPORTED` | `400` | The request was invalid: sorting is not supported |
| `CANNOT_PARSE_LIST_FILTER` | `400` | The request was invalid: invalid list filter: {error} |
| `INVALID_LIST_FILTER` | `400` | The request was invalid: invalid list filter |
| `ORDER_BY_FIELD_UNSUPPORTED` | `400` | The request was invalid: sort order {field} is unsupported |
| `QUOTA_EXHAUSTED` | `429` | Quota limit '{quota_names}' has been exceeded. Limit: {limit} in {location}. |
| `INVALID_RESOURCE_LABEL` | `400` | resource {resource_label} are invalid: {reason} |
|---|---|---|