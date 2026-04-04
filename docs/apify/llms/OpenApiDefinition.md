# Source: https://docs.apify.com/api/client/js/reference/interface/OpenApiDefinition.md

# OpenApiDefinition<!-- -->

OpenAPI specification for an Actor.

Defines the Actor's API interface in OpenAPI 3.0 format, useful for integration with tools like ChatGPT plugins and other API consumers.

## Index[**](#Index)

### Properties

* [**components](#components)
* [**info](#info)
* [**openapi](#openapi)
* [**paths](#paths)
* [**servers](#servers)

## Properties<!-- -->[**](#Properties)

### [**](#components)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L286)components

**components: { schemas: {} }

#### Type declaration

* ##### schemas: {}



### [**](#info)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L278)info

**info: { description?

<!-- -->

: string; title: string; version?

<!-- -->

: string; x-build-id: string }

#### Type declaration

* ##### optionaldescription?<!-- -->: string
* ##### title: string
* ##### optionalversion?<!-- -->: string
* ##### x-build-id: string

### [**](#openapi)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L277)openapi

**openapi: string

### [**](#paths)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L285)paths

**paths:

<!-- -->

{}

#### Type declaration



### [**](#servers)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L284)servers

**servers: { url: string }\[]
