# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/createopenaiembeddings.md

# CreateOpenAiEmbeddings 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-openai-nar

## Description

Uses OpenAI to create embeddings for text. The input text can be provided as a single FlowFile or as a record-oriented FlowFile.

## Tags

chatbot, embeddings, gen ai, generative ai, llm, nlp, openai, openflow, text

## Input Requirement

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Dimensions | The number of dimensions to request the resulting output embeddings have. This is only supported in text-embedding-3 and later models. |
| Embeddings Model | The model to use for embeddings |
| Embeddings Record Path | The path to the field in the record where the embeddings are to be written. |
| Max Batch Size | The maximum number of records to include in each batch sent to OpenAI |
| OpenAI API Key | The API Key for authenticating to OpenAI |
| OpenAI Organization | The organization to use for OpenAI |
| Record Reader | The record reader to use for reading record-oriented data. If the incoming data is to be treated as plaintext, this property should be left unset. |
| Record Writer | The Record Writer to use for writing the output |
| Text Record Path | The path to the field in the record that contains the text to be embedded. If the incoming data is to be treated as plaintext, this property should be left unset. |
| User | An identifier for the remote user on whose behalf the request is being made; OpenAI uses this to detect and prevent abuse. |
| Web Client Service | The Web Client Service to use for communicating with OpenAI |

## Relationships

| Name | Description |
| --- | --- |
| failure | The original FlowFile will be routed to this relationship if the embeddings could not be created |
| success | The embeddings will be routed to this relationship |

## Writes attributes

| Name | Description |
| --- | --- |
| record.count | The number of records written to the output |
| mime.type | The MIME type of the output data, based on the chosen Record Writer |

## Use cases

|  |
| --- |
| Create embeddings for text using OpenAI’s Embeddings |

## See also

* [com.snowflake.openflow.runtime.processors.openai.CreateAzureOpenAiEmbeddings](createazureopenaiembeddings.md)
* [com.snowflake.openflow.runtime.processors.openai.PromptOpenAI](promptopenai.md)
