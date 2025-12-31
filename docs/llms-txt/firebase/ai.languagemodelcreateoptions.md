# Source: https://firebase.google.com/docs/reference/js/ai.languagemodelcreateoptions.md.txt

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Configures the creation of an on-device language model session.

**Signature:**  

    export interface LanguageModelCreateOptions extends LanguageModelCreateCoreOptions 

**Extends:** [LanguageModelCreateCoreOptions](https://firebase.google.com/docs/reference/js/ai.languagemodelcreatecoreoptions.md#languagemodelcreatecoreoptions_interface)

## Properties

|                                                                 Property                                                                  |                                                                Type                                                                 |      Description       |
|-------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| [initialPrompts](https://firebase.google.com/docs/reference/js/ai.languagemodelcreateoptions.md#languagemodelcreateoptionsinitialprompts) | [LanguageModelMessage](https://firebase.google.com/docs/reference/js/ai.languagemodelmessage.md#languagemodelmessage_interface)\[\] | ***(Public Preview)*** |
| [signal](https://firebase.google.com/docs/reference/js/ai.languagemodelcreateoptions.md#languagemodelcreateoptionssignal)                 | AbortSignal                                                                                                                         | ***(Public Preview)*** |

## LanguageModelCreateOptions.initialPrompts

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**  

    initialPrompts?: LanguageModelMessage[];

## LanguageModelCreateOptions.signal

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**  

    signal?: AbortSignal;