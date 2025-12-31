# Source: https://firebase.google.com/docs/reference/js/ai.requestoptions.md.txt

# RequestOptions interface

Params passed to [getGenerativeModel()](https://firebase.google.com/docs/reference/js/ai.md#getgenerativemodel_c63f46a).

**Signature:**  

    export interface RequestOptions 

## Properties

|                                              Property                                               |  Type  |                                                                                                                           Description                                                                                                                           |
|-----------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [baseUrl](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptionsbaseurl) | string | Base url for endpoint. Defaults to https://firebasevertexai.googleapis.com, which is the [Firebase AI Logic API](https://console.cloud.google.com/apis/library/firebasevertexai.googleapis.com?project=_) (used regardless of your chosen Gemini API provider). |
| [timeout](https://firebase.google.com/docs/reference/js/ai.requestoptions.md#requestoptionstimeout) | number | Request timeout in milliseconds. Defaults to 180 seconds (180000ms).                                                                                                                                                                                            |

## RequestOptions.baseUrl

Base url for endpoint. Defaults to https://firebasevertexai.googleapis.com, which is the [Firebase AI Logic API](https://console.cloud.google.com/apis/library/firebasevertexai.googleapis.com?project=_) (used regardless of your chosen Gemini API provider).

**Signature:**  

    baseUrl?: string;

## RequestOptions.timeout

Request timeout in milliseconds. Defaults to 180 seconds (180000ms).

**Signature:**  

    timeout?: number;