# Source: https://firebase.google.com/docs/reference/js/remote-config.remoteconfigoptions.md.txt

# RemoteConfigOptions interface

Options for Remote Config initialization.

**Signature:**  

    export interface RemoteConfigOptions 

## Properties

|                                                                      Property                                                                      |                                                         Type                                                          |                               Description                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [initialFetchResponse](https://firebase.google.com/docs/reference/js/remote-config.remoteconfigoptions.md#remoteconfigoptionsinitialfetchresponse) | [FetchResponse](https://firebase.google.com/docs/reference/js/remote-config.fetchresponse.md#fetchresponse_interface) | Hydrates the state with an initial fetch response.                      |
| [templateId](https://firebase.google.com/docs/reference/js/remote-config.remoteconfigoptions.md#remoteconfigoptionstemplateid)                     | string                                                                                                                | The ID of the template to use. If not provided, defaults to "firebase". |

## RemoteConfigOptions.initialFetchResponse

Hydrates the state with an initial fetch response.

**Signature:**  

    initialFetchResponse?: FetchResponse;

## RemoteConfigOptions.templateId

The ID of the template to use. If not provided, defaults to "firebase".

**Signature:**  

    templateId?: string;