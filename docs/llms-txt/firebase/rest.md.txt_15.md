# Source: https://firebase.google.com/docs/reference/data-connect/rest.md.txt

# Firebase Data Connect API

## Service: firebasedataconnect.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

- <https://firebasedataconnect.googleapis.com/$discovery/rest?version=v1beta>

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

- `https://firebasedataconnect.googleapis.com`

## REST Resource: [v1beta.projects.locations](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations/get` | `GET /v1beta/{name=projects/*/locations/*}` Gets information about a location. |
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations/list` | `GET /v1beta/{name=projects/*}/locations` Lists information about the supported locations for this service. |

## REST Resource: [v1beta.projects.locations.operations](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.operations)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.operations/cancel` | `POST /v1beta/{name=projects/*/locations/*/operations/*}:cancel` Starts asynchronous cancellation on a long-running operation. |
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.operations/delete` | `DELETE /v1beta/{name=projects/*/locations/*/operations/*}` Deletes a long-running operation. |
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.operations/get` | `GET /v1beta/{name=projects/*/locations/*/operations/*}` Gets the latest state of a long-running operation. |
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.operations/list` | `GET /v1beta/{name=projects/*/locations/*}/operations` Lists operations that match the specified filter in the request. |

## REST Resource: [v1beta.projects.locations.services](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services/create` | `POST /v1beta/{parent=projects/*/locations/*}/services` Creates a new Service in a given project and location. |
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services/delete` | `DELETE /v1beta/{name=projects/*/locations/*/services/*}` Deletes a single Service. |
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services/executeGraphql` | `POST /v1beta/{name=projects/*/locations/*/services/*}:executeGraphql` Execute any GraphQL query and mutation against the Firebase Data Connect's generated GraphQL schema. |
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services/executeGraphqlRead` | `POST /v1beta/{name=projects/*/locations/*/services/*}:executeGraphqlRead` Execute any GraphQL query against the Firebase Data Connect's generated GraphQL schema. |
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services/get` | `GET /v1beta/{name=projects/*/locations/*/services/*}` Gets details of a single Service. |
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services/list` | `GET /v1beta/{parent=projects/*/locations/*}/services` Lists Services in a given project and location. |
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services/patch` | `PATCH /v1beta/{service.name=projects/*/locations/*/services/*}` Updates the parameters of a single Service. |

## REST Resource: [v1beta.projects.locations.services.connectors](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.connectors)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.connectors/create` | `POST /v1beta/{parent=projects/*/locations/*/services/*}/connectors` Creates a new Connector in a given project and location. |
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.connectors/delete` | `DELETE /v1beta/{name=projects/*/locations/*/services/*/connectors/*}` Deletes a single Connector. |
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.connectors/executeMutation` | `POST /v1beta/{name=projects/*/locations/*/services/*/connectors/*}:executeMutation` Execute a predefined mutation in a Connector. |
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.connectors/executeQuery` | `POST /v1beta/{name=projects/*/locations/*/services/*/connectors/*}:executeQuery` Execute a predefined query in a Connector. |
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.connectors/get` | `GET /v1beta/{name=projects/*/locations/*/services/*/connectors/*}` Gets details of a single Connector. |
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.connectors/list` | `GET /v1beta/{parent=projects/*/locations/*/services/*}/connectors` Lists Connectors in a given project and location. |
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.connectors/patch` | `PATCH /v1beta/{connector.name=projects/*/locations/*/services/*/connectors/*}` Updates the parameters of a single Connector, and creates a new ConnectorRevision with the updated Connector. |

## REST Resource: [v1beta.projects.locations.services.schemas](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas/create` | `POST /v1beta/{parent=projects/*/locations/*/services/*}/schemas` Creates a new Schema in a given project and location. |
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas/delete` | `DELETE /v1beta/{name=projects/*/locations/*/services/*/schemas/*}` Deletes a single Schema. |
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas/get` | `GET /v1beta/{name=projects/*/locations/*/services/*/schemas/*}` Gets details of a single Schema. |
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas/list` | `GET /v1beta/{parent=projects/*/locations/*/services/*}/schemas` Lists Schemas in a given project and location. |
| `https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas/patch` | `PATCH /v1beta/{schema.name=projects/*/locations/*/services/*/schemas/*}` Updates the parameters of a single Schema, and creates a new SchemaRevision with the updated Schema. |