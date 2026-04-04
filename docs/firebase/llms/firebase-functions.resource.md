# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.resource.md.txt

# Resource interface

Resource is a standard format for defining a resource (google.rpc.context.AttributeContext.Resource). In Cloud Functions, it is the resource that triggered the function - such as a storage bucket.

**Signature:**  

    export interface Resource 

## Properties

|                                                    Property                                                    |             Type             |                                                                                      Description                                                                                      |
|----------------------------------------------------------------------------------------------------------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [labels](https://firebase.google.com/docs/reference/functions/firebase-functions.resource.md#resourcelabels)   | { \[tag: string\]: string; } | Map of Resource's labels.                                                                                                                                                             |
| [name](https://firebase.google.com/docs/reference/functions/firebase-functions.resource.md#resourcename)       | string                       | The stable identifier (name) of a resource on the service. A resource can be logically identified as "//{resource.service}/{resource.name}"                                           |
| [service](https://firebase.google.com/docs/reference/functions/firebase-functions.resource.md#resourceservice) | string                       | The name of the service that this resource belongs to.                                                                                                                                |
| [type](https://firebase.google.com/docs/reference/functions/firebase-functions.resource.md#resourcetype)       | string                       | The type of the resource. The syntax is platform-specific because different platforms define their resources differently. For Google APIs, the type format must be "{service}/{kind}" |

## Resource.labels

Map of Resource's labels.

**Signature:**  

    labels?: {
            [tag: string]: string;
        };

## Resource.name

The stable identifier (name) of a resource on the service. A resource can be logically identified as "//{resource.service}/{resource.name}"

**Signature:**  

    name: string;

## Resource.service

The name of the service that this resource belongs to.

**Signature:**  

    service: string;

## Resource.type

The type of the resource. The syntax is platform-specific because different platforms define their resources differently. For Google APIs, the type format must be "{service}/{kind}"

**Signature:**  

    type?: string;