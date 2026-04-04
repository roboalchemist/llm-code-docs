# Source: https://firebase.google.com/docs/reference/js/ai.livegenerativemodel.md.txt

# LiveGenerativeModel class

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Class for Live generative model APIs. The Live API enables low-latency, two-way multimodal interactions with Gemini.

This class should only be instantiated with [getLiveGenerativeModel()](https://firebase.google.com/docs/reference/js/ai.md#getlivegenerativemodel_f2099ac).

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `LiveGenerativeModel` class.

**Signature:**  

    export declare class LiveGenerativeModel extends AIModel 

**Extends:** [AIModel](https://firebase.google.com/docs/reference/js/ai.aimodel.md#aimodel_class)

## Properties

|                                                             Property                                                              | Modifiers |                                                              Type                                                               |      Description       |
|-----------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------|------------------------|
| [generationConfig](https://firebase.google.com/docs/reference/js/ai.livegenerativemodel.md#livegenerativemodelgenerationconfig)   |           | [LiveGenerationConfig](https://firebase.google.com/docs/reference/js/ai.livegenerationconfig.md#livegenerationconfig_interface) | ***(Public Preview)*** |
| [systemInstruction](https://firebase.google.com/docs/reference/js/ai.livegenerativemodel.md#livegenerativemodelsysteminstruction) |           | [Content](https://firebase.google.com/docs/reference/js/ai.content.md#content_interface)                                        | ***(Public Preview)*** |
| [toolConfig](https://firebase.google.com/docs/reference/js/ai.livegenerativemodel.md#livegenerativemodeltoolconfig)               |           | [ToolConfig](https://firebase.google.com/docs/reference/js/ai.toolconfig.md#toolconfig_interface)                               | ***(Public Preview)*** |
| [tools](https://firebase.google.com/docs/reference/js/ai.livegenerativemodel.md#livegenerativemodeltools)                         |           | [Tool](https://firebase.google.com/docs/reference/js/ai.md#tool)\[\]                                                            | ***(Public Preview)*** |

## Methods

|                                                     Method                                                      | Modifiers |                                                            Description                                                            |
|-----------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------|
| [connect()](https://firebase.google.com/docs/reference/js/ai.livegenerativemodel.md#livegenerativemodelconnect) |           | ***(Public Preview)*** Starts a [LiveSession](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesession_class). |

## LiveGenerativeModel.generationConfig

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**  

    generationConfig: LiveGenerationConfig;

## LiveGenerativeModel.systemInstruction

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**  

    systemInstruction?: Content;

## LiveGenerativeModel.toolConfig

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**  

    toolConfig?: ToolConfig;

## LiveGenerativeModel.tools

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**  

    tools?: Tool[];

## LiveGenerativeModel.connect()

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Starts a [LiveSession](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesession_class).

**Signature:**  

    connect(): Promise<LiveSession>;

**Returns:**

Promise\<[LiveSession](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesession_class)\>

A [LiveSession](https://firebase.google.com/docs/reference/js/ai.livesession.md#livesession_class).

#### Exceptions

If the connection failed to be established with the server.