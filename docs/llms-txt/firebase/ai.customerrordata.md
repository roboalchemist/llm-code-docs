# Source: https://firebase.google.com/docs/reference/js/ai.customerrordata.md.txt

# CustomErrorData interface

Details object that contains data originating from a bad HTTP response.

**Signature:**  

    export interface CustomErrorData 

## Properties

|                                                    Property                                                     |                                                                   Type                                                                   |                                                                      Description                                                                      |
|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [errorDetails](https://firebase.google.com/docs/reference/js/ai.customerrordata.md#customerrordataerrordetails) | [ErrorDetails](https://firebase.google.com/docs/reference/js/ai.errordetails.md#errordetails_interface)\[\]                              | Optional additional details about the error.                                                                                                          |
| [response](https://firebase.google.com/docs/reference/js/ai.customerrordata.md#customerrordataresponse)         | [GenerateContentResponse](https://firebase.google.com/docs/reference/js/ai.generatecontentresponse.md#generatecontentresponse_interface) | Response from a [GenerateContentRequest](https://firebase.google.com/docs/reference/js/ai.generatecontentrequest.md#generatecontentrequest_interface) |
| [status](https://firebase.google.com/docs/reference/js/ai.customerrordata.md#customerrordatastatus)             | number                                                                                                                                   | HTTP status code of the error response.                                                                                                               |
| [statusText](https://firebase.google.com/docs/reference/js/ai.customerrordata.md#customerrordatastatustext)     | string                                                                                                                                   | HTTP status text of the error response.                                                                                                               |

## CustomErrorData.errorDetails

Optional additional details about the error.

**Signature:**  

    errorDetails?: ErrorDetails[];

## CustomErrorData.response

Response from a [GenerateContentRequest](https://firebase.google.com/docs/reference/js/ai.generatecontentrequest.md#generatecontentrequest_interface)

**Signature:**  

    response?: GenerateContentResponse;

## CustomErrorData.status

HTTP status code of the error response.

**Signature:**  

    status?: number;

## CustomErrorData.statusText

HTTP status text of the error response.

**Signature:**  

    statusText?: string;