# Overview - GroqDocs

## Welcome

Fast language models have gained significant attention in recent years due to their ability to process and generate human-like text quickly and efficiently. The importance of fast language models can be understood from their potential applications and benefits:

1. **Real-time Chatbots and Conversational Interfaces**: Fast language models enable the development of chatbots and conversational interfaces that can respond promptly to user queries, making them more engaging and useful.
2. **Sentiment Analysis and Opinion Mining**: Fast language models can quickly analyze text data to identify sentiments, opinions, and emotions, allowing for improved customer service, market research, and opinion mining.
3. **Language Translation and Localization**: Fast language models can quickly translate text between languages, facilitating global communication and enabling businesses to reach a broader audience.
4. **Text Summarization and Generation**: Fast language models can summarize long documents or even generate new text on a given topic, improving information retrieval and processing efficiency.
5. **Named Entity Recognition and Information Extraction**: Fast language models can rapidly recognize and extract specific entities, such as names, locations, and organizations, from unstructured text data.
6. **Recommendation Systems**: Fast language models can analyze large amounts of text data to personalize product recommendations, improve customer experience, and increase sales.
7. **Content Generation for Social Media**: Fast language models can quickly generate engaging content for social media platforms, helping businesses maintain a consistent online presence and increasing their online visibility.
8. **Sentiment Analysis for Stock Market Analysis**: Fast language models can quickly analyze social media posts, news articles, and other text data to identify sentiment trends, enabling financial analysts to make more informed investment decisions.
9. **Language Learning and Education**: Fast language models can provide instant feedback and adaptive language learning, making language education more effective and engaging.
10. **Domain-Specific Knowledge Extraction**: Fast language models can quickly extract relevant information from vast amounts of text data, enabling domain experts to focus on high-level decision-making rather than manual information gathering.

The benefits of fast language models include:

- **Increased Efficiency**: Fast language models can process large amounts of text data quickly, reducing the time and effort required for tasks such as sentiment analysis, entity recognition, and text summarization.
- **Improved Accuracy**: Fast language models can analyze and learn from large datasets, leading to more accurate results and more informed decision-making.
- **Enhanced User Experience**: Fast language models can enable real-time interactions, personalized recommendations, and timely responses, improving the overall user experience.
- **Cost Savings**: Fast language models can automate many tasks, reducing the need for manual labor and minimizing costs associated with data processing and analysis.

In summary, fast language models have the potential to transform various industries and applications by providing fast, accurate, and efficient language processing capabilities.

## External API Compatibility

- **gemma2-9b-it**
- **llama3-8b-8192**
- **llama3-70b-8192**
- **whisper-large-v3-turbo**
- **whisper-large-v3**
- **llama-guard-3-8b**
- **meta-llama/llama-4-maverick-17b-128e-instruct**
- **meta-llama/llama-4-scout-17b-16e-instruct**
- **meta-llama/llama-guard-4-12b**
- **moonshotai/kimi-k2-instruct**
- **openai/gpt-oss-120b**
- **openai/gpt-oss-20b**
- **qwen/qwen3-32b**

## Chat Completion

- **Fast language models have gained significant attention in recent years due to their ability to process and generate human-like text quickly and efficiently. The importance of fast language models can be understood from their potential applications and benefits:**
  1. **Real-time Chatbots and Conversational Interfaces**: Fast language models enable the development of chatbots and conversational interfaces that can respond promptly to user queries, making them more engaging and useful.
  2. **Sentiment Analysis and Opinion Mining**: Fast language models can quickly analyze text data to identify sentiments, opinions, and emotions, allowing for improved customer service, market research, and opinion mining.
  3. **Language Translation and Localization**: Fast language models can quickly translate text between languages, facilitating global communication and enabling businesses to reach a broader audience.
  4. **Text Summarization and Generation**: Fast language models can summarize long documents or even generate new text on a given topic, improving information retrieval and processing efficiency.
  5. **Named Entity Recognition and Information Extraction**: Fast language models can rapidly recognize and extract specific entities, such as names, locations, and organizations, from unstructured text data.
  6. **Recommendation Systems**: Fast language models can analyze large amounts of text data to personalize product recommendations, improve customer experience, and increase sales.
  7. **Content Generation for Social Media**: Fast language models can quickly generate engaging content for social media platforms, helping businesses maintain a consistent online presence and increasing their online visibility.
  8. **Sentiment Analysis for Stock Market Analysis**: Fast language models can quickly analyze social media posts, news articles, and other text data to identify sentiment trends, enabling financial analysts to make more informed investment decisions.
  9. **Language Learning and Education**: Fast language models can provide instant feedback and adaptive language learning, making language education more effective and engaging.
  10. **Domain-Specific Knowledge Extraction**: Fast language models can quickly extract relevant information from vast amounts of text data, enabling domain experts to focus on high-level decision-making rather than manual information gathering.

The benefits of fast language models include:

- **Increased Efficiency**: Fast language models can process large amounts of text data quickly, reducing the time and effort required for tasks such as sentiment analysis, entity recognition, and text summarization.
- **Improved Accuracy**: Fast language models can analyze and learn from large datasets, leading to more accurate results and more informed decision-making.
- **Enhanced User Experience**: Fast language models can enable real-time interactions, personalized recommendations, and timely responses, improving the overall user experience.
- **Cost Savings**: Fast language models can automate many tasks, reducing the need for manual labor and minimizing costs associated with data processing and analysis.

In summary, fast language models have the potential to transform various industries and applications by providing fast, accurate, and efficient language processing capabilities.

## API Reference

- **Chat Completion**
  - **Description**: A chat completion message generated by the model.
  - **Properties**:
    - **annotations**: A list of annotations providing citations and references for the content in the message.
    - **content**: The contents of the message.
    - **executed_tools**: A list of tools that were executed during the chat completion for compound AI systems.
    - **function_call**: Controls which (if any) function is called by the model.
    - **reasoning**: The model's reasoning for a response. Only available for [models that support reasoning](https://console.groq.com/docs/reasoning) when request parameter reasoning_format has value `parsed`.
    - **role**: The role of the author of this message.
    - **tool_calls**: A list of tool calls generated by the model, such as function calls.
  - **Type**: Array of content items generated by the model.

- **Response Annotation**
  - **Description**: A citation referencing a specific document that was provided in the request.
  - **Properties**:
    - **document_id**: The ID of the document being cited, corresponding to a document provided in the request.
    - **end_index**: The character index in the message content where this citation ends.
    - **start_index**: The character index in the message content where this citation begins.
  - **Type**: Object.

- **Embedding**
  - **Description**: Represents an embedding vector returned by embedding endpoint.
  - **Properties**:
    - **embedding**: A list of floats representing the embedding vector. The length of vector depends on the model as listed in the [embedding guide](https://console.groq.com/docs/guides/embeddings).
    - **index**: The index of the embedding in the list of embeddings.
    - **object**: The object type, which is always `embedding`.
  - **Type**: Object.

- **Error**
  - **Description**: An error object if the response failed.
  - **Properties**:
    - **code**: The error code.
    - **debug**: An error string indicating why a stream was stopped early.
    - **message**: A human-readable error message.
    - **param**: Optional.
    - **schema_code**: Optional.
    - **schema_kind**: Optional.
    - **schema_path**: Optional.
    - **schema_path_segments**: Optional.
  - **Type**: Object.

- **ErrorResponse**
  - **Description**: Returns an error response.
  - **Properties**:
    - **error**: An error object.
  - **Type**: Object.

- **File**
  - **Description**: The `File` object represents a document that has been uploaded.
  - **Properties**:
    - **bytes**: The size of the file, in bytes.
    - **created_at**: The Unix timestamp (in seconds) for when the file was created.
    - **filename**: The name of the file.
    - **id**: The file identifier, which can be referenced in the API endpoints.
    - **object**: The object type, which is always `file`.
    - **purpose**: The intended purpose of the file. Supported values are `batch` and `batch_output`.
  - **Type**: Object.

- **FunctionCitation**
  - **Description**: A citation referencing the result of a function or tool call.
  - **Properties**:
    - **end_index**: The character index in the message content where this citation ends.
    - **start_index**: The character index in the message content where this citation begins.
    - **tool_call_id**: The ID of the tool call being cited, corresponding to a tool call made during the conversation.
  - **Type**: Object.

- **FunctionObject**
  - **Description**: Describes the function's purpose. The model uses this to determine when to invoke the function.
  - **Properties**:
    - **description**: A description of what the function does.
    - **name**: The name of the function to be called.
    - **parameters**: A JSON schema describing the function's input parameters.
    - **strict**: Whether to enable strict schema adherence when generating the output.
  - **Type**: Object.

- **FunctionParameters**
  - **Description**: Function parameters defined as a JSON Schema object.
  - **Type**: Object.

- **ListBatchesResponse**
  - **Description**: A list of batches.
  - **Properties**:
    - **data**: A list of batches.
  - **Type**: Array.

- **ListFilesResponse**
  - **Description**: A list of files.
  - **Properties**:
    - **data**: A list of files.
  - **Type**: Array.

- **ListFineTuningsResponse**
  - **Description**: A list of fine tunings.
  - **Properties**:
    - **data**: A list of fine tunings.
  - **Type**: Array.

- **ListModelsResponse**
  - **Description**: A list of models.
  - **Properties**:
    - **data**: A list of models.
  - **Type**: Array.

- **Model**
  - **Description**: Describes an OpenAI model offering that can be used with the API.
  - **Properties**:
    - **created**: The Unix timestamp (in seconds) when the model was created.
    - **id**: The model identifier, which can be referenced in the API endpoints.
    - **object**: The object type, which is always `model`.
    - **owned_by**: The organization that owns the model.
  - **Type**: Object.

- **ReadFineTuningResponse**
  - **Description**: Returns a fine tune object.
  - **Properties**:
    - **data**: A fine tune object.
  - **Type**: Object.

- **ReadTranslationResponse**
  - **Description**: Returns a translation object.
  - **Properties**:
    - **text**: The translated text.
  - **Type**: Object.

- **ResponseAnnotation**
  - **Description**: A citation referencing a file.
  - **Properties**:
    - **end_index**: The character index of the last character of the URL citation in the message.
    - **start_index**: The character index of the first character of the URL citation in the message.
    - **title**: The title of the URL resource.
    - **type**: The type of the annotation. Always `url_citation`.
  - **Type**: Object.

- **ResponseEasyInputMessage**
  - **Description**: A message input to the model with a role indicating instruction following hierarchy.
  - **Properties**:
    - **content**: A list of one or many input content items.
    - **role**: The role of the message input. One of `user`, `assistant`, `system`, or `developer`.
    - **status**: The status of the item. Populated when items are returned via API.
  - **Type**: Object.

- **ResponseFileCitation**
  - **Description**: A citation to a file.
  - **Properties**:
    - **end_index**: The character index of the last character of the URL citation in the message.
    - **start_index**: The character index of the first character of the URL citation in the message.
    - **title**: The title of the file resource.
    - **type**: The type of the annotation. Always `file_citation`.
  - **Type**: Object.

- **ResponseFormatConfiguration**
  - **Description**: An object specifying the format that the model must output.
  - **Properties**:
    - **description**: A description of what the response format is for, used by the model to determine how to respond in the format.
    - **name**: The name of the response format. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.
    - **schema**: A JSON Schema object describing the response format.
    - **strict**: Whether to enable strict schema adherence when generating the output.
  - **Type**: Object.

- **ResponseFormatJsonSchema**
  - **Description**: JSON Schema response format.
  - **Properties**:
    - **type**: The type of response format being defined. Always `json_schema`.
  - **Type**: Object.

- **ResponseFormatText**
  - **Description**: Default response format.
  - **Properties**:
    - **type**: The type of response format being defined. Always `text`.
  - **Type**: Object.

- **ResponseFunctionCall**
  - **Description**: A function call generated by the model.
  - **Properties**:
    - **arguments**: A JSON string of the arguments to pass to the function.
    - **call_id**: The unique ID of the function tool call generated by the model.
    - **id**: The unique ID of the function tool call.
    - **name**: The name of the function to call.
    - **status**: The status of the function call.
  - **Type**: Object.

- **ResponseOutputContent**
  - **Description**: A text output from the model.
  - **Properties**:
    - **annotations**: The annotations of the text output.
    - **logprobs**: Log probability information for the output.
    - **text**: The text output from the model.
    - **type**: The type of the output text. Always `output_text`.
  - **Type**: Object.

- **ResponseTool**
  - **Description**: A function call generated by the model.
  - **Properties**:
    - **arguments**: A JSON string of the arguments to pass to the function.
    - **call_id**: The unique ID of the function tool call generated by the model.
    - **id**: The unique ID of the function tool call.
    - **name**: The name of the function to call.
    - **status**: The status of the function call.
  - **Type**: Object.

- **ResponseToolChoiceOption**
  - **Description**: Controls which (if any) tool is called by the model.
  - **Properties**:
    - **function**: Controls which (if any) tool is called by the model.
    - **type**: The type of the tool. Currently, only `function` is supported.
  - **Type**: Object.

- **ResponseUrlCitation**
  - **Description**: A citation for a web resource.
  - **Properties**:
    - **end_index**: The character index of the URL citation in the message.
    - **start_index**: The character index of the first character of the URL citation in the message.
    - **title**: The title of the web resource.
    - **type**: The type of the annotation. Always `url_citation`.
  - **Type**: Object.

- **ResponseUsage**
  - **Description**: Usage statistics for the response request.
  - **Properties**:
    - **input_tokens**: Number of tokens in the input.
    - **input_tokens_details**: Breakdown of input tokens.
    - **output_tokens**: Number of tokens in the generated output.
    - **output_tokens_details**: Breakdown of output tokens.
    - **total_tokens**: Total number of tokens used in the request (input + output).
  - **Type**: Object.

- **TextResponseFormatJsonSchema**
  - **Description**: JSON Schema response format.
  - **Properties**:
    - **description**: A description of what the response format is for, used by the model to determine how to respond in the format.
    - **name**: The name of the response format. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.
    - **schema**: A JSON Schema object describing the response format.
    - **strict**: Whether to enable strict schema adherence when generating the output.
  - **Type**: Object.

- **TranscriptionSegment**
  - **Description**: A segment of the audio.
  - **Properties**:
    - **audio_text**: Transcribed text for the entire chunk.
    - **avg_logprob**: Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.
    - **chunk_end**: End chunk timestamp.
    - **chunk_start**: Start chunk timestamp.
    - **compression_ratio**: Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.
    - **end**: End time of the segment in seconds.
    - **id**: Unique identifier of the segment.
    - **no_speech_prob**: Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.
    - **seek**: Seek offset of the segment.
    - **start**: Start time of the segment in seconds.
    - **temperature**: Temperature parameter used for generating the segment.
    - **text**: Text content of the segment.
    - **token_scores**: Token-level scores.
    - **tokens**: Array of token IDs for the text content.
  - **Type**: Object.

- **XGroq**
  - **Description**: Groq-specific metadata for streaming responses.
  - **Properties**:
    - **debug**: An error string indicating why a stream was stopped early.
    - **id**: A groq request ID which can be used to refer to a specific request to groq support.
    - **seed**: The seed used for the request. Sent in the final chunk.
    - **usage**: Additional Groq-specific usage metrics (hardware cache statistics).
  - **Type**: Object.

- **XGroqNonStreaming**
  - **Description**: Groq-specific metadata for non-streaming chat completion responses.
  - **Properties**:
    - **debug**: An error string indicating why a stream was stopped early.
    - **id**: A groq request ID which can be used to refer to a specific request to groq support.
    - **seed**: The seed used for the request. See the seed property on CreateChatCompletionRequest for more details.
    - **usage**: Additional Groq-specific usage metrics (hardware cache statistics).
  - **Type**: Object.

## Chat Completion

- **Description**: A chat completion message generated by the model.
- **Properties**:
  - **annotations**: A list of annotations providing citations and references for the content in the message.
  - **content**: The contents of the message.
  - **executed_tools**: A list of tools that were executed during the chat completion for compound AI systems.
  - **function_call**: Controls which (if any) function is called by the model.
  - **reasoning**: The model's reasoning for a response. Only available for [models that support reasoning](https://console.groq.com/docs/reasoning) when request parameter reasoning_format has value `parsed`.
  - **role**: The role of the author of this message.
  - **tool_calls**: A list of tool calls generated by the model, such as function calls.
- **Type**: Array of content items generated by the model.

## Response

- **Description**: A message input to the model with explicit type field.
- **Properties**:
  - **content**: A list of one or many input content items.
  - **role**: The role of the message input. One of `user`, `assistant`, `system`, or `developer`.
  - **status**: The status of item. Populated when items are returned via API.
- **Type**: Object.

## Fine Tuning

- **Description**: A fine tuning for the already uploaded files.
- **Properties**:
  - **input_file_id**: The ID of an uploaded file that contains requests for the new batch.
  - **model**: The name of the fine tuned model.
  - **type**: The type of fine tuning format such as `lora`.
- **Type**: Object.

## Model

- **Description**: Describes an OpenAI model offering that can be used with the API.
- **Properties**:
  - **created**: The Unix timestamp (in seconds) when the model was created.
  - **id**: The model identifier, which can be referenced in the API endpoints.
  - **object**: The object type, which is always `model`.
  - **owned_by**: The organization that owns the model.
- **Type**: Object.

## Embedding

- **Description**: Represents an embedding vector representing the input text.
- **Properties**:
  - **embedding**: A list of floats representing the embedding vector. The length of vector depends on the model as listed in the [embedding guide](https://console.groq.com/docs/guides/embeddings).
  - **index**: The index of the embedding in the list of embeddings.
- **Type**: Object.

## File

- **Description**: The `File` object represents a document that has been uploaded.
- **Properties**:
  - **bytes**: The size of the file, in bytes.
  - **created_at**: The Unix timestamp (in seconds) for when the file was created.
  - **filename**: The name of the file.
  - **id**: The file identifier, which can be referenced in the API endpoints.
  - **object**: The object type, which is always `file`.
  - **purpose**: The intended purpose of the file. Supported values are `batch` and `batch_output`.
- **Type**: Object.

## Batch

- **Description**: List your organization's batches.
- **Properties**:
  - **data**: A list of batches.
- **Type**: Array.

## Batch

- **Description**: Creates and executes a batch from an uploaded file of requests.
- **Properties**:
  - **input_file_id**: The ID of an uploaded file that contains requests for the new batch.
  - **endpoint**: The endpoint to be used for all requests in the batch.
  - **completion_window**: The time frame within which the batch should be processed.
- **Type**: Object.

## Batch

- **Description**: Cancels a batch.
- **Properties**:
  - **input_file_id**: The ID of the batch to cancel.
- **Type**: Object.

## Batch

- **Description**: Returns a list of batches.
- **Properties**:
  - **object**: `list`.
  - **data**: `data`.
- **Type**: Array.

## Batch

- **Description**: Returns a batch object.
- **Properties**:
  - **id**: `batch_01jh6xa7reempvjyh6n3yst2zw`.
  - **object**: `batch`.
  - **endpoint**: `/v1/chat/completions`.
  - **errors**: `null`.
  - **input_file_id**: `file_01jh6x76wtemjr74t1fh0faj5t`.
  - **completion_window**: `24h`.
  - **status**: `validating`.
  - **output_file_id**: `null`.
  - **error_file_id**: `null`.
  - **finalizing_at**: `null`.
  - **failed_at**: `null`.
  - **expired_at**: `null`.
  - **cancelled_at**: `null`.
  - **request_counts**: `{ total: 0, completed: 0, failed: 0 }`.
  - **metadata**: `null`.
  - **created_at**: `1736472600`.
  - **expires_at**: `1736559000`.
  - **cancelling_at**: `null`.
  - **completed_at**: `null`.
  - **in_progress_at**: `null`.
- **Type**: Object.

## Batch

- **Description**: Returns an audio transcription object.
- **Properties**:
  - **text**: `Your transcribed text appears here...`.
- **Type**: Object.

## Batch

- **Description**: Returns an audio translation object.
- **Properties**:
  - **text**: `Your translated text appears here...`.
- **Type**: Object.

## Batch

- **Description**: Returns a batch object.
- **Properties**:
  - **id**: `batch_01jh6xa7reempvjyh6n3yst2zw`.
  - **object**: `batch`.
  - **endpoint**: `/v1/chat/completions`.
  - **errors**: `null`.
  - **input_file_id**: `file_01jh6x76wtemjr74t1fh0faj5t`.
  - **completion_window**: `24h`.
  - **status**: `validating`.
  - **output_file_id**: `null`.
  - **error_file_id**: `null`.
  - **finalizing_at**: `null`.
  - **failed_at**: `null`.
  - **expired_at**: `null`.
  - **cancelled_at**: `null`.
  - **request_counts**: `{ total: 0, completed: 0, failed: 0 }`.
  - **metadata**: `null`.
  - **created_at**: `1736472600`.
  - **expires_at**: `1736559000`.
  - **cancelling_at**: `null`.
  - **completed_at**: `null`.
  - **in_progress_at**: `null`.
- **Type**: Object.

## Batch

- **Description**: Returns a batch object.
- **Properties**:
  - **id**: `batch_01jh6xa7reempvjyh6n3yst2zw`.
  - **object**: `batch`.
  - **endpoint**: `/v1/chat/completions`.
  - **errors**: `null`.
  - **input_file_id**: `file_01jh6x76wtemjr74t1fh0faj5t`.
  - **completion_window**: `24h`.
  - **status**: `validating`.
  - **output_file_id**: `null`.
  - **error_file_id**: `null`.
  - **finalizing_at**: `null`.
  - **failed_at**: `null`.
  - **expired_at**: `null`.
  - **cancelled_at**: `null`.
  - **request_counts**: `{ total: 0, completed: 0, failed: 0 }`.
  - **metadata**: `null`.
  - **created_at**: `1736472600`.
  - **expires_at**: `1736559000`.
  - **cancelling_at**: `null`.
  - **completed_at**: `null`.
  - **in_progress_at**: `null`.
- **Type**: Object.

## Batch

- **Description**: Returns a batch object.
- **Properties**:
  - **id**: `batch_01jh6xa7reempvjyh6n3yst2zw`.
  - **object**: `batch`.
  - **endpoint**: `/v1/chat/completions`.
  - **errors**: `null`.
  - **input_file_id**: `file_01jh6x76wtemjr74t1fh0faj5t`.
  - **completion_window**: `24h`.
  - **status**: `validating`.
  - **output_file_id**: `null`.
  - **error_file_id**: `null`.
  - **finalizing_at**: `null`.
  - **failed_at**: `null`.
  - **expired_at**: `null`.
  - **cancelled_at**: `null`.
  - **request_counts**: `{ total: 0, completed: 0, failed: 0 }`.
  - **metadata**: `null`.
  - **created_at**: `1736472600`.
  - **expires_at**: `1736559000`.
  - **cancelling_at**: `null`.
  - **completed_at**: `null`.
  - **in_progress_at**: `null`.
- **Type**: Object.

## Batch

- **Description**: Returns a batch object.
- **Properties**:
  - **id**: `batch_01jh6xa7reempvjyh6n3yst2zw`.
  - **object**: `batch`.
  - **endpoint**: `/v1/chat/completions`.
  - **errors**: `null`.
  - **input_file_id**: `file_01jh6x76wtemjr74t1fh0faj5t`.
  - **completion_window**: `24h`.
  - **status**: `validating`.
  - **output_file_id**: `null`.
  - **error_file_id**: `null`.
  - **finalizing_at**: `null`.
  - **failed_at**: `null`.
  - **expired_at**: `null`.
  - **cancelled_at**: `null`.
  - **request_counts**: `{ total: 0, completed: 0, failed: 0 }`.
  - **metadata**: `null`.
  - **created_at**: `1736472600`.
  - **expires_at**: `1736559000`.
  - **cancelling_at**: `null`.
  - **completed_at**: `null`.
  - **in_progress_at**: `null`.
- **Type**: Object.

## Batch

- **Description**: Returns a batch object.
- **Properties**:
  - **id**: `batch_01jh6xa7reempvjyh6n3yst2zw`.
  - **object**: `batch`.
  - **endpoint**: `/v1/chat/completions`.
  - **errors**: `null`.
  - **input_file_id**: `file_01jh6x76wtemjr74t1fh0faj5t`.
  - **completion_window**: `24h`.
  - **status**: `validating`.
  - **output_file_id**: `null`.
  - **error_file_id**: `null`.
  - **finalizing_at**: `null`.
  - **failed_at**: `null`.
  - **expired_at**: `null`.
  - **cancelled_at**: `null`.
  - **request_counts**: `{ total: 0, completed: 0, failed: 0 }`.
  - **metadata**: `null`.
  - **created_at**: `1736472600`.
  - **expires_at**: `1736559000`.
  - **cancelling_at**: `null`.
  - **completed_at**: `null`.
  - **in_progress_at**: `null`.
- **Type**: Object.

## Batch

- **Description**: Returns a batch object.
- **Properties**:
  - **id**: `batch_01jh6xa7reempvjyh6n3yst2zw`.
  - **object**: `batch`.
  - **endpoint**: `/v1/chat/completions`.
  - **errors**: `null`.
  - **input_file_id**: `file_01jh6x76wtemjr74t1fh0faj5t`.
  - **completion_window**: `24h`.
  - **status**: `validating`.
  - **output_file_id**: `null`.
  - **error_file_id**: `null`.
  - **finalizing_at**: `null`.
  - **failed_at**: `null`.
  - **expired_at**: `null`.
  - **cancelled_at**: `null`.
  - **request_counts**: `{ total: 0, completed: 0, failed: 0 }`.
  - **metadata**: `null`.
  - **created_at**: `1736472600`.
  - **expires_at**: `1736559000`.
  - **cancelling_at**: `null`.
  - **completed_at**: `null`.
  - **in_progress_at**: `null`.
- **Type**: Object.

## Batch

- **Description**: Returns a batch object.
- **Properties**:
  - **id**: `batch_01jh6xa7reempvjyh6n3yst2zw`.
  - **object**: `batch`.
  - **endpoint**: `/v1/chat/completions`.
  - **errors**: `null`.
  - **input_file_id**: `file_01jh6x76wtemjr74t1fh0faj5t`.
  - **completion_window**: `24h`.
  - **status**: `validating`.
  - **output_file_id**: `null`.
  - **error_file_id**: `null`.
  - **finalizing_at**: `null`.
  - **failed_at**: `null`.
  - **expired_at**: `null`.
  - **cancelled_at**: `null`.
  - **request_counts**: `{ total: 0, completed: 0, failed: 0 }`.
  - **metadata**: `null`.
  - **created_at**: `1736472600`.
  - **expires_at**: `1736559000`.
  - **cancelling_at**: `null`.
  - **completed_at**: `null`.
  - **in_progress_at**: `null`.
- **Type**: Object.

## Batch

- **Description**: Returns a batch object.
- **Properties**:
  - **id**: `batch_01jh6xa7reempvjyh6n3yst2zw`.
  - **object**: `batch`.
  - **endpoint**: `/v1/chat/completions`.
  - **errors**: `null`.
  - **input_file_id**: `file_01jh6x76wtemjr74t1fh0faj5t`.
  - **completion_window**: `24h`.
  - **status**: `validating`.
  - **output_file_id**: `null`.
  - **error_file_id**: `null`.
  - **finalizing_at**: `null`.
  - **failed_at**: `null`.
  - **expired_at**: `null`.
  - **cancelled_at**: `null`.
  - **request_counts**: `{ total: 0, completed: 0, failed: 0 }`.
  - **metadata**: `null`.
  - **created_at**: `1736472600`.
  - **expires_at**: `1736559000`.
  - **cancelling_at**: `null`.
  - **completed_at**: `null`.
  - **in_progress_at**: `null`.
- **Type**: Object.

## Batch

- **Description**: Returns a batch object.
- **Properties**:
  - **id**: `batch_01jh6xa7reempvjyh6n3yst2zw`.
  - **object**: `batch`.
  - **endpoint**: `/v1/chat/completions`.
  - **errors**: `null`.
  - **input_file_id**: `file_01jh6x76wtemjr74t1fh0faj5t`.
  - **completion_window**: `24h`.
  - **status**: `validating`.
  - **output_file_id**: `null`.
  - **error_file_id**: `null`.
  - **finalizing_at**: `null`.
  - **failed_at**: `null`.
  - **expired_at**: `null`.
  - **cancelled_at**: `null`.
  - **request_counts**: `{ total: 0, completed: 0, failed: 0 }`.
  - **metadata**: `null`.
  - **created_at**: `1736472600`.
  - **expires_at**: `1736559000`.
  - **cancelling_at**: `null`.
  - **completed_at**: `null`.
  - **in_progress_at**: `null`.
- **Type**: Object.

## Batch

- **Description**: Returns a batch object.
- **Properties**:
  - **id**: `batch_01jh6xa7reempvjyh6n3yst2zw`.
  - **object**: `batch`.
  - **endpoint**: `/v1/chat/completions`.
  - **errors**: `null`.
  - **input_file_id**: `file_01jh6x76wtemjr74t1fh0faj5t`.
  - **completion_window**: `24h`.