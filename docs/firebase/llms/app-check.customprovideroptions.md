# Source: https://firebase.google.com/docs/reference/js/app-check.customprovideroptions.md.txt

# CustomProviderOptions interface

Options when creating a [CustomProvider](https://firebase.google.com/docs/reference/js/app-check.customprovider.md#customprovider_class).

**Signature:**  

    export interface CustomProviderOptions 

## Properties

|                                                          Property                                                          |                                                                Type                                                                 |                              Description                              |
|----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [getToken](https://firebase.google.com/docs/reference/js/app-check.customprovideroptions.md#customprovideroptionsgettoken) | () =\> Promise\<[AppCheckToken](https://firebase.google.com/docs/reference/js/app-check.appchecktoken.md#appchecktoken_interface)\> | Function to get an App Check token through a custom provider service. |

## CustomProviderOptions.getToken

Function to get an App Check token through a custom provider service.

**Signature:**  

    getToken: () => Promise<AppCheckToken>;