# Source: https://firebase.google.com/docs/reference/js/vertexai.requestoptions.md.txt

# RequestOptions interface

Params passed to [getGenerativeModel()](https://firebase.google.com/docs/reference/js/vertexai.md#getgenerativemodel_80bd839).

**Signature:**  

    export interface RequestOptions 

## Properties

|                                                 Property                                                  |  Type  |                                Description                                 |
|-----------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------------------------|
| [baseUrl](https://firebase.google.com/docs/reference/js/vertexai.requestoptions.md#requestoptionsbaseurl) | string | Base url for endpoint. Defaults to https://firebasevertexai.googleapis.com |
| [timeout](https://firebase.google.com/docs/reference/js/vertexai.requestoptions.md#requestoptionstimeout) | number | Request timeout in milliseconds. Defaults to 180 seconds (180000ms).       |

## RequestOptions.baseUrl

Base url for endpoint. Defaults to https://firebasevertexai.googleapis.com

**Signature:**  

    baseUrl?: string;

## RequestOptions.timeout

Request timeout in milliseconds. Defaults to 180 seconds (180000ms).

**Signature:**  

    timeout?: number;