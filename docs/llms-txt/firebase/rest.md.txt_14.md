# Source: https://firebase.google.com/docs/reference/apphosting/rest.md.txt

# Firebase App Hosting API

Firebase App Hosting streamlines the development and deployment of dynamic Next.js and Angular applications, offering built-in framework support, GitHub integration, and integration with other Firebase products.

You can use this API to intervene in the Firebase App Hosting build process and add custom functionality not supported in our default Console \& CLI flows, including triggering builds from external CI/CD workflows or deploying from pre-built container images.

## Service: firebaseapphosting.googleapis.com

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

- <https://firebaseapphosting.googleapis.com/$discovery/rest?version=v1>
- <https://firebaseapphosting.googleapis.com/$discovery/rest?version=v1beta>

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

- `https://firebaseapphosting.googleapis.com`

## REST Resource: [v1.projects.locations](https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations/get` | `GET /v1/{name=projects/*/locations/*}` Gets information about a location. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations/list` | `GET /v1/{name=projects/*}/locations` Lists information about the supported locations for this service. |

## REST Resource: [v1.projects.locations.backends](https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends/create` | `POST /v1/{parent=projects/*/locations/*}/backends` Creates a new backend in a given project and location. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends/delete` | `DELETE /v1/{name=projects/*/locations/*/backends/*}` Deletes a single backend. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends/get` | `GET /v1/{name=projects/*/locations/*/backends/*}` Gets information about a backend. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends/list` | `GET /v1/{parent=projects/*/locations/*}/backends` Lists backends in a given project and location. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends/patch` | `PATCH /v1/{backend.name=projects/*/locations/*/backends/*}` Updates the information for a single backend. |

## REST Resource: [v1.projects.locations.backends.builds](https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.builds)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.builds/create` | `POST /v1/{parent=projects/*/locations/*/backends/*}/builds` Creates a new build for a backend. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.builds/delete` | `DELETE /v1/{name=projects/*/locations/*/backends/*/builds/*}` Deletes a single build. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.builds/get` | `GET /v1/{name=projects/*/locations/*/backends/*/builds/*}` Gets information about a build. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.builds/list` | `GET /v1/{parent=projects/*/locations/*/backends/*}/builds` Lists builds in a given project, location, and backend. |

## REST Resource: [v1.projects.locations.backends.domains](https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.domains)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.domains/create` | `POST /v1/{parent=projects/*/locations/*/backends/*}/domains` Links a new domain to a backend. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.domains/delete` | `DELETE /v1/{name=projects/*/locations/*/backends/*/domains/*}` Deletes a single domain. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.domains/get` | `GET /v1/{name=projects/*/locations/*/backends/*/domains/*}` Gets information about a domain. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.domains/list` | `GET /v1/{parent=projects/*/locations/*/backends/*}/domains` Lists domains of a backend. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.domains/patch` | `PATCH /v1/{domain.name=projects/*/locations/*/backends/*/domains/*}` Updates the information for a single domain. |

## REST Resource: [v1.projects.locations.backends.rollouts](https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.rollouts)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.rollouts/create` | `POST /v1/{parent=projects/*/locations/*/backends/*}/rollouts` Creates a new rollout for a backend. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.rollouts/get` | `GET /v1/{name=projects/*/locations/*/backends/*/rollouts/*}` Gets information about a rollout. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.rollouts/list` | `GET /v1/{parent=projects/*/locations/*/backends/*}/rollouts` Lists rollouts for a backend. |

## REST Resource: [v1.projects.locations.backends.traffic](https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.traffic)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.traffic/get` | `GET /v1/{name=projects/*/locations/*/backends/*/traffic}` Gets information about a backend's traffic. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.backends.traffic/patch` | `PATCH /v1/{traffic.name=projects/*/locations/*/backends/*/traffic}` Updates a backend's traffic. |

## REST Resource: [v1.projects.locations.operations](https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.operations)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.operations/cancel` | `POST /v1/{name=projects/*/locations/*/operations/*}:cancel` Starts asynchronous cancellation on a long-running operation. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.operations/delete` | `DELETE /v1/{name=projects/*/locations/*/operations/*}` Deletes a long-running operation. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.operations/get` | `GET /v1/{name=projects/*/locations/*/operations/*}` Gets the latest state of a long-running operation. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1/projects.locations.operations/list` | `GET /v1/{name=projects/*/locations/*}/operations` Lists operations that match the specified filter in the request. |

## REST Resource: [v1beta.projects.locations](https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations/get` | `GET /v1beta/{name=projects/*/locations/*}` Gets information about a location. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations/list` | `GET /v1beta/{name=projects/*}/locations` Lists information about the supported locations for this service. |

## REST Resource: [v1beta.projects.locations.backends](https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends/create` | `POST /v1beta/{parent=projects/*/locations/*}/backends` Creates a new backend in a given project and location. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends/delete` | `DELETE /v1beta/{name=projects/*/locations/*/backends/*}` Deletes a single backend. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends/get` | `GET /v1beta/{name=projects/*/locations/*/backends/*}` Gets information about a backend. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends/list` | `GET /v1beta/{parent=projects/*/locations/*}/backends` Lists backends in a given project and location. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends/patch` | `PATCH /v1beta/{backend.name=projects/*/locations/*/backends/*}` Updates the information for a single backend. |

## REST Resource: [v1beta.projects.locations.backends.builds](https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends.builds)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends.builds/create` | `POST /v1beta/{parent=projects/*/locations/*/backends/*}/builds` Creates a new build for a backend. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends.builds/delete` | `DELETE /v1beta/{name=projects/*/locations/*/backends/*/builds/*}` Deletes a single build. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends.builds/get` | `GET /v1beta/{name=projects/*/locations/*/backends/*/builds/*}` Gets information about a build. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends.builds/list` | `GET /v1beta/{parent=projects/*/locations/*/backends/*}/builds` Lists builds in a given project, location, and backend. |

## REST Resource: [v1beta.projects.locations.backends.domains](https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends.domains)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends.domains/create` | `POST /v1beta/{parent=projects/*/locations/*/backends/*}/domains` Links a new domain to a backend. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends.domains/delete` | `DELETE /v1beta/{name=projects/*/locations/*/backends/*/domains/*}` Deletes a single domain. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends.domains/get` | `GET /v1beta/{name=projects/*/locations/*/backends/*/domains/*}` Gets information about a domain. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends.domains/list` | `GET /v1beta/{parent=projects/*/locations/*/backends/*}/domains` Lists domains of a backend. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends.domains/patch` | `PATCH /v1beta/{domain.name=projects/*/locations/*/backends/*/domains/*}` Updates the information for a single domain. |

## REST Resource: [v1beta.projects.locations.backends.rollouts](https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends.rollouts)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends.rollouts/create` | `POST /v1beta/{parent=projects/*/locations/*/backends/*}/rollouts` Creates a new rollout for a backend. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends.rollouts/get` | `GET /v1beta/{name=projects/*/locations/*/backends/*/rollouts/*}` Gets information about a rollout. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends.rollouts/list` | `GET /v1beta/{parent=projects/*/locations/*/backends/*}/rollouts` Lists rollouts for a backend. |

## REST Resource: [v1beta.projects.locations.backends.traffic](https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends.traffic)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends.traffic/get` | `GET /v1beta/{name=projects/*/locations/*/backends/*/traffic}` Gets information about a backend's traffic. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.backends.traffic/patch` | `PATCH /v1beta/{traffic.name=projects/*/locations/*/backends/*/traffic}` Updates a backend's traffic. |

## REST Resource: [v1beta.projects.locations.operations](https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.operations)

| Methods ||
|---|---|
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.operations/cancel` | `POST /v1beta/{name=projects/*/locations/*/operations/*}:cancel` Starts asynchronous cancellation on a long-running operation. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.operations/delete` | `DELETE /v1beta/{name=projects/*/locations/*/operations/*}` Deletes a long-running operation. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.operations/get` | `GET /v1beta/{name=projects/*/locations/*/operations/*}` Gets the latest state of a long-running operation. |
| `https://firebase.google.com/docs/reference/apphosting/rest/v1beta/projects.locations.operations/list` | `GET /v1beta/{name=projects/*/locations/*}/operations` Lists operations that match the specified filter in the request. |