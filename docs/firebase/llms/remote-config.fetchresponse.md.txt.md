# Source: https://firebase.google.com/docs/reference/js/remote-config.fetchresponse.md.txt

# FetchResponse interface

Defines a successful response (200 or 304).

<br />

Modeled after the native `Response` interface, but simplified for Remote Config's use case.

**Signature:**

    export interface FetchResponse 

## Properties

| Property | Type | Description |
|---|---|---|
| [config](https://firebase.google.com/docs/reference/js/remote-config.fetchresponse.md#fetchresponseconfig) | [FirebaseRemoteConfigObject](https://firebase.google.com/docs/reference/js/remote-config.firebaseremoteconfigobject.md#firebaseremoteconfigobject_interface) | Defines the map of parameters returned as "entries" in the fetch response body. Only defined for 200 responses. |
| [eTag](https://firebase.google.com/docs/reference/js/remote-config.fetchresponse.md#fetchresponseetag) | string | Defines the ETag response header value. Only defined for 200 and 304 responses. |
| [experiments](https://firebase.google.com/docs/reference/js/remote-config.fetchresponse.md#fetchresponseexperiments) | [FirebaseExperimentDescription](https://firebase.google.com/docs/reference/js/remote-config.firebaseexperimentdescription.md#firebaseexperimentdescription_interface)\[\] | Metadata for A/B testing and Remote Config Rollout experiments. |
| [status](https://firebase.google.com/docs/reference/js/remote-config.fetchresponse.md#fetchresponsestatus) | number | The HTTP status, which is useful for differentiating success responses with data from those without. The Remote Config client is modeled after the native `Fetch` interface, so HTTP status is first-class. Disambiguation: the fetch response returns a legacy "state" value that is redundant with the HTTP status code. The former is normalized into the latter. |
| [templateVersion](https://firebase.google.com/docs/reference/js/remote-config.fetchresponse.md#fetchresponsetemplateversion) | number | The version number of the config template fetched from the server. |

## FetchResponse.config

Defines the map of parameters returned as "entries" in the fetch response body.

<br />

Only defined for 200 responses.

**Signature:**

    config?: FirebaseRemoteConfigObject;

## FetchResponse.eTag

Defines the ETag response header value.

<br />

Only defined for 200 and 304 responses.

**Signature:**

    eTag?: string;

## FetchResponse.experiments

Metadata for A/B testing and Remote Config Rollout experiments.

Only defined for 200 responses.

**Signature:**

    experiments?: FirebaseExperimentDescription[];

## FetchResponse.status

The HTTP status, which is useful for differentiating success responses with data from those without.

<br />

The Remote Config client is modeled after the native `Fetch` interface, so HTTP status is first-class.

<br />

Disambiguation: the fetch response returns a legacy "state" value that is redundant with the HTTP status code. The former is normalized into the latter.

**Signature:**

    status: number;

## FetchResponse.templateVersion

The version number of the config template fetched from the server.

**Signature:**

    templateVersion?: number;