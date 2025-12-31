# Source: https://firebase.google.com/docs/reference/js/ai.livegenerationconfig.md.txt

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Configuration parameters used by[LiveGenerativeModel](https://firebase.google.com/docs/reference/js/ai.livegenerativemodel.md#livegenerativemodel_class)to control live content generation.

**Signature:**  

    export interface LiveGenerationConfig 

## Properties

|                                                                     Property                                                                      |                                                                    Type                                                                     |                                                                                                                                                                                                                                                                                             Description                                                                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [frequencyPenalty](https://firebase.google.com/docs/reference/js/ai.livegenerationconfig.md#livegenerationconfigfrequencypenalty)                 | number                                                                                                                                      | ***(Public Preview)***Frequency penalties.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [inputAudioTranscription](https://firebase.google.com/docs/reference/js/ai.livegenerationconfig.md#livegenerationconfiginputaudiotranscription)   | [AudioTranscriptionConfig](https://firebase.google.com/docs/reference/js/ai.audiotranscriptionconfig.md#audiotranscriptionconfig_interface) | ***(Public Preview)*** Enables transcription of audio input.When enabled, the model will respond with transcriptions of your audio input in the`inputTranscriptions`property in[LiveServerContent](https://firebase.google.com/docs/reference/js/ai.liveservercontent.md#liveservercontent_interface)messages. Note that the transcriptions are broken up across messages, so you may only receive small amounts of text per message. For example, if you ask the model "How are you today?", the model may transcribe that input across three messages, broken up as "How a", "re yo", "u today?". |
| [maxOutputTokens](https://firebase.google.com/docs/reference/js/ai.livegenerationconfig.md#livegenerationconfigmaxoutputtokens)                   | number                                                                                                                                      | ***(Public Preview)***Specifies the maximum number of tokens that can be generated in the response. The number of tokens per word varies depending on the language outputted. Is unbounded by default.                                                                                                                                                                                                                                                                                                                                                                                              |
| [outputAudioTranscription](https://firebase.google.com/docs/reference/js/ai.livegenerationconfig.md#livegenerationconfigoutputaudiotranscription) | [AudioTranscriptionConfig](https://firebase.google.com/docs/reference/js/ai.audiotranscriptionconfig.md#audiotranscriptionconfig_interface) | ***(Public Preview)*** Enables transcription of audio input.When enabled, the model will respond with transcriptions of its audio output in the`outputTranscription`property in[LiveServerContent](https://firebase.google.com/docs/reference/js/ai.liveservercontent.md#liveservercontent_interface)messages. Note that the transcriptions are broken up across messages, so you may only receive small amounts of text per message. For example, if the model says "How are you today?", the model may transcribe that output across three messages, broken up as "How a", "re yo", "u today?".   |
| [presencePenalty](https://firebase.google.com/docs/reference/js/ai.livegenerationconfig.md#livegenerationconfigpresencepenalty)                   | number                                                                                                                                      | ***(Public Preview)***Positive penalties.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [responseModalities](https://firebase.google.com/docs/reference/js/ai.livegenerationconfig.md#livegenerationconfigresponsemodalities)             | [ResponseModality](https://firebase.google.com/docs/reference/js/ai.md#responsemodality)\[\]                                                | ***(Public Preview)***The modalities of the response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [speechConfig](https://firebase.google.com/docs/reference/js/ai.livegenerationconfig.md#livegenerationconfigspeechconfig)                         | [SpeechConfig](https://firebase.google.com/docs/reference/js/ai.speechconfig.md#speechconfig_interface)                                     | ***(Public Preview)***Configuration for speech synthesis.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [temperature](https://firebase.google.com/docs/reference/js/ai.livegenerationconfig.md#livegenerationconfigtemperature)                           | number                                                                                                                                      | ***(Public Preview)*** Controls the degree of randomness in token selection. A`temperature`value of 0 means that the highest probability tokens are always selected. In this case, responses for a given prompt are mostly deterministic, but a small amount of variation is still possible.                                                                                                                                                                                                                                                                                                        |
| [topK](https://firebase.google.com/docs/reference/js/ai.livegenerationconfig.md#livegenerationconfigtopk)                                         | number                                                                                                                                      | ***(Public Preview)*** Changes how the model selects token for output. A`topK`value of 1 means the select token is the most probable among all tokens in the model's vocabulary, while a`topK`value 3 means that the next token is selected from among the 3 most probably using probabilities sampled. Tokens are then further filtered with the highest selected`temperature`sampling. Defaults to 40 if unspecified.                                                                                                                                                                             |
| [topP](https://firebase.google.com/docs/reference/js/ai.livegenerationconfig.md#livegenerationconfigtopp)                                         | number                                                                                                                                      | ***(Public Preview)*** Changes how the model selects tokens for output. Tokens are selected from the most to least probable until the sum of their probabilities equals the`topP`value. For example, if tokens A, B, and C have probabilities of 0.3, 0.2, and 0.1 respectively and the`topP`value is 0.5, then the model will select either A or B as the next token by using the`temperature`and exclude C as a candidate. Defaults to 0.95 if unset.                                                                                                                                             |

## LiveGenerationConfig.frequencyPenalty

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Frequency penalties.

**Signature:**  

    frequencyPenalty?: number;

## LiveGenerationConfig.inputAudioTranscription

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Enables transcription of audio input.

When enabled, the model will respond with transcriptions of your audio input in the`inputTranscriptions`property in[LiveServerContent](https://firebase.google.com/docs/reference/js/ai.liveservercontent.md#liveservercontent_interface)messages. Note that the transcriptions are broken up across messages, so you may only receive small amounts of text per message. For example, if you ask the model "How are you today?", the model may transcribe that input across three messages, broken up as "How a", "re yo", "u today?".

**Signature:**  

    inputAudioTranscription?: AudioTranscriptionConfig;

## LiveGenerationConfig.maxOutputTokens

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Specifies the maximum number of tokens that can be generated in the response. The number of tokens per word varies depending on the language outputted. Is unbounded by default.

**Signature:**  

    maxOutputTokens?: number;

## LiveGenerationConfig.outputAudioTranscription

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Enables transcription of audio input.

When enabled, the model will respond with transcriptions of its audio output in the`outputTranscription`property in[LiveServerContent](https://firebase.google.com/docs/reference/js/ai.liveservercontent.md#liveservercontent_interface)messages. Note that the transcriptions are broken up across messages, so you may only receive small amounts of text per message. For example, if the model says "How are you today?", the model may transcribe that output across three messages, broken up as "How a", "re yo", "u today?".

**Signature:**  

    outputAudioTranscription?: AudioTranscriptionConfig;

## LiveGenerationConfig.presencePenalty

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Positive penalties.

**Signature:**  

    presencePenalty?: number;

## LiveGenerationConfig.responseModalities

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

The modalities of the response.

**Signature:**  

    responseModalities?: ResponseModality[];

## LiveGenerationConfig.speechConfig

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Configuration for speech synthesis.

**Signature:**  

    speechConfig?: SpeechConfig;

## LiveGenerationConfig.temperature

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Controls the degree of randomness in token selection. A`temperature`value of 0 means that the highest probability tokens are always selected. In this case, responses for a given prompt are mostly deterministic, but a small amount of variation is still possible.

**Signature:**  

    temperature?: number;

## LiveGenerationConfig.topK

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Changes how the model selects token for output. A`topK`value of 1 means the select token is the most probable among all tokens in the model's vocabulary, while a`topK`value 3 means that the next token is selected from among the 3 most probably using probabilities sampled. Tokens are then further filtered with the highest selected`temperature`sampling. Defaults to 40 if unspecified.

**Signature:**  

    topK?: number;

## LiveGenerationConfig.topP

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Changes how the model selects tokens for output. Tokens are selected from the most to least probable until the sum of their probabilities equals the`topP`value. For example, if tokens A, B, and C have probabilities of 0.3, 0.2, and 0.1 respectively and the`topP`value is 0.5, then the model will select either A or B as the next token by using the`temperature`and exclude C as a candidate. Defaults to 0.95 if unset.

**Signature:**  

    topP?: number;