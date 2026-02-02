# Overview - GroqDocs

## Welcome

Fast LLM inference, OpenAI-compatible. Simple to integrate, easy to scale. Start building in minutes.

## External API Compatibility

- **OpenAI base URL:** [https://api.groq.com/openai/v1](https://api.groq.com/openai/v1)
- **Gemma2-9b-it:** [https://console.groq.com/docs/models/gemma2-9b-it](https://console.groq.com/docs/models/gemma2-9b-it)
- **Llama3-8b-8192:** [https://console.groq.com/docs/models/llama3-8b-8192](https://console.groq.com/docs/models/llama3-8b-8192)
- **Llama3-70b-8192:** [https://console.groq.com/docs/models/llama3-70b-8192](https://console.groq.com/docs/models/llama3-70b-8192)
- **Whisper-large-v3-turbo:** [https://console.groq.com/docs/models/whisper-large-v3-turbo](https://console.groq.com/docs/models/whisper-large-v3-turbo)
- **Whisper-large-v3:** [https://console.groq.com/docs/models/whisper-large-v3](https://console.groq.com/docs/models/whisper-large-v3)
- **Llama Guard-3-8b:** [https://console.groq.com/docs/models/llama-guard-3-8b](https://console.groq.com/docs/models/llama-guard-3-8b)
- **Meta Llama/llama-4-maverick-17b-128e-instruct:** [https://console.groq.com/docs/models/meta-llama/llama-4-maverick-17b-128e-instruct](https://console.groq.com/docs/models/meta-llama/llama-4-maverick-17b-128e-instruct)
- **Meta Llama/llama-4-scout-17b-16e-instruct:** [https://console.groq.com/docs/models/meta-llama/llama-4-scout-17b-16e-instruct](https://console.groq.com/docs/models/meta-llama/llama-4-scout-17b-16e-instruct)
- **Meta Llama/llama-guard-4-12b:** [https://console.groq.com/docs/models/meta-llama/llama-guard-4-12b](https://console.groq.com/docs/models/meta-llama/llama-guard-4-12b)
- **Moonshot AI/Kimi-K2-Instruct:** [https://console.groq.com/docs/models/moonshotai/kimi-k2-instruct](https://console.groq.com/docs/models/moonshotai/kimi-k2-instruct)
- **OpenAI/gpt-oss-120b:** [https://console.groq.com/docs/models/openai/gpt-oss-120b](https://console.groq.com/docs/models/openai/gpt-oss-120b)
- **OpenAI/gpt-oss-20b:** [https://console.groq.com/docs/models/openai/gpt-oss-20b](https://console.groq.com/docs/models/openai/gpt-oss-20b)
- **Qwen/Qwen3-32b:** [https://console.groq.com/docs/models/qwen/qwen3-32b](https://console.groq.com/docs/models/qwen/qwen3-32b)

## Chat Completion

- **Description:** Fast language models have gained significant attention in recent years due to their ability to process and generate human-like text quickly and efficiently. The importance of fast language models can be understood from their potential applications and benefits:
  1. **Real-time Chatbots and Conversational Interfaces:** Fast language models enable the development of chatbots and conversational interfaces that can respond promptly to user queries, making them more engaging and useful.
  2. **Sentiment Analysis and Opinion Mining:** Fast language models can quickly analyze text data to identify sentiments, opinions, and emotions, allowing for improved customer service, market research, and opinion mining.
  3. **Language Translation and Localization:** Fast language models can quickly translate text between languages, facilitating global communication and enabling businesses to reach a broader audience.
  4. **Text Summarization and Generation:** Fast language models can summarize long documents or even generate new text on a given topic, improving information retrieval and processing efficiency.
  5. **Named Entity Recognition and Information Extraction:** Fast language models can rapidly recognize and extract specific entities, such as names, locations, and organizations, from unstructured text data.
  6. **Recommendation Systems:** Fast language models can analyze large amounts of text data to personalize product recommendations, improve customer experience, and increase sales.
  7. **Content Generation for Social Media:** Fast language models can quickly generate engaging content for social media platforms, helping businesses maintain a consistent online presence and increasing their online visibility.
  8. **Sentiment Analysis for Stock Market Analysis:** Fast language models can quickly analyze social media posts, news articles, and other text data to identify sentiment trends, enabling financial analysts to make more informed investment decisions.
  9. **Language Learning and Education:** Fast language models can provide instant feedback and adaptive language learning, making language education more effective and engaging.
  10. **Domain-Specific Knowledge Extraction:** Fast language models can quickly extract relevant information from vast amounts of text data, enabling domain experts to focus on high-level decision-making rather than manual information gathering.

- **Benefits:** 
  - **Increased Efficiency:** Fast language models can process large amounts of text data quickly, reducing the time and effort required for tasks such as sentiment analysis, entity recognition, and text summarization.
  - **Improved Accuracy:** Fast language models can analyze and learn from large datasets, leading to more accurate results and more informed decision-making.
  - **Enhanced User Experience:** Fast language models can enable real-time interactions, personalized recommendations, and timely responses, improving the overall user experience.
  - **Cost Savings:** Fast language models can automate many tasks, reducing the need for manual labor and minimizing costs associated with data processing and analysis.

- **In summary:** Fast language models have the potential to transform various industries and applications by providing fast, accurate, and efficient language processing capabilities.

## Chat Completion Request

- **Description:** A document that can be referenced by the model while generating responses.
- **Properties:**
  - **Document Citation:** An optional citation referencing a specific document that was provided in the request.
  - **Source:** The source of the document. Only text and JSON sources are currently supported.
- **Type:** `document_citation` or `function_citation`.

## Chat Completion Response

- **Description:** A chat completion message generated by the model.
- **Properties:**
  - **Annotation:** A list of annotations providing citations and references for the content in the message.
  - **Content:** The contents of the message.
  - **Executed Tools:** A list of tools that were executed during the chat completion for compound AI systems.
  - **Function Call:** Controls which (if any) tool is called by the model.
  - **Reasoning:** The model's reasoning for a response. Only available for [models that support reasoning](https://console.groq.com/docs/reasoning) when request parameter reasoning_format has value `parsed`.
  - **Role:** The role of the messages author, in this case `assistant`.
  - **Tool Calls:** A list of tool calls generated by the model, such as function calls.

## Chat Completion Role

- **Description:** The role of the author of a message.
- **Options:**
  - `system`
  - `user`
  - `assistant`
  - `tool`
  - `function`

## Chat Completion Stream

- **Description:** A chat completion delta generated by streamed model responses.
- **Properties:**
  - **Annotation:** A list of annotations providing citations and references for the content in the message.
  - **Content:** The contents of the chunk message.
  - **Executed Tools:** Log probability information for the choice.
  - **Reasoning:** The model's reasoning for a response. Only available for [models that support reasoning](https://console.groq.com/docs/reasoning) when request parameter reasoning_format has value `parsed`.
  - **Role:** The role of the author of this message.
  - **Tool Calls:** The tool calls that were available to the model.
  - **Top Log Probabilities:** The number of most likely tokens at each token position, each with an associated log probability.

## Chat Completion Usage Breakdown

- **Description:** Usage statistics for compound AI completion requests.
- **Properties:**
  - **Models:** List of models used in the request and their individual usage statistics.
  - **Type:** `list`.

## Chat Completion Function Call

- **Description:** A function call generated by the model.
- **Properties:**
  - **Arguments:** The arguments to call the function with, as generated by the model in JSON format.
  - **Name:** The name of the function to call.
  - **Type:** `function`.

## Chat Completion Message Tool Call

- **Description:** Controls which (if any) tool is called by the model.
- **Properties:**
  - **Function:** The function that the model called.
  - **Name:** The name of the function to call.
  - **Type:** `function`.

## Chat Completion Message Tool Call Chunk

- **Description:** Controls which (if any) tool is called by the model.
- **Properties:**
  - **Function:** The function that the model called.
  - **Name:** The name of the function to call.
  - **Type:** `function`.

## Chat Completion Message Tool Calls

- **Description:** The tool calls generated by the model, such as function calls.

## Chat Completion Message Tool Choice Option

- **Description:** Controls which (if any) tool is called by the model.
- **Properties:**
  - **Function:** The function that the model called.
  - **Name:** The name of the function to call.
  - **Type:** `function`.

## Chat Completion Response Message

- **Description:** A message input to the model with a role indicating instruction following hierarchy.
- **Properties:**
  - **Content:** Text input to the model.
  - **Role:** The role of the message input.
  - **Status:** The status of the message.

## Chat Completion Response Output

- **Description:** A function call generated by the model.
- **Properties:**
  - **Arguments:** A JSON string of the arguments to pass to the function.
  - **Call ID:** The unique ID of the function tool call generated by the model.
  - **ID:** The unique ID of the function tool call.
  - **Name:** The name of the function to call.
  - **Status:** The status of the function call.

## Chat Completion Response Message

- **Description:** An output message from the model.
- **Properties:**
  - **Content:** The content of the output message.
  - **ID:** The unique ID of the output message.
  - **Role:** The role of the output message.
  - **Status:** The status of the message.

## Chat Completion Response Reasoning

- **Description:** A reasoning output from the model. Available for [models that support reasoning](https://console.groq.com/docs/reasoning).
- **Properties:**
  - **ID:** The unique ID of the reasoning output.
  - **Summary:** Summary items (currently empty).
  - **Type:** The type of the reasoning output. Always `reasoning`.

## Chat Completion Response Text

- **Description:** A text output from the model.
- **Properties:**
  - **Annotations:** The annotations of the text output.
  - **Log Probabilities:** Log probability information for the output.
  - **Text:** The text output from the model.
  - **Type:** The type of the output text. Always `output_text`.

## Chat Completion Response Function Call

- **Description:** A function call generated by the model.
- **Properties:**
  - **Arguments:** A JSON string of the arguments to pass to the function.
  - **Call ID:** The unique ID of the function tool call generated by the model.
  - **ID:** The unique ID of the function tool call.
  - **Name:** The name of the function to call.
  - **Status:** The status of the function call.

## Chat Completion Response Message

- **Description:** An output message from the model.
- **Properties:**
  - **Content:** The content of the output message.
  - **ID:** The unique ID of the output message.
  - **Role:** The role of the output message.
  - **Status:** The status of the message.

## Chat Completion Response Reasoning

- **Description:** A reasoning output from the model. Available for [models that support reasoning](https://console.groq.com/docs/reasoning).
- **Properties:**
  - **ID:** The unique ID of the reasoning output.
  - **Summary:** Summary items (currently empty).
  - **Type:** The type of the reasoning output. Always `reasoning`.

## Chat Completion Response Text

- **Description:** A text output from the model.
- **Properties:**
  - **Annotations:** The annotations of the text output.
  - **Log Probabilities:** Log probability information for the output.
  - **Text:** The text output from the model.
  - **Type:** The type of the output text. Always `output_text`.

## Chat Completion Response Function Call

- **Description:** A function call generated by the model.
- **Properties:**
  - **Arguments:** A JSON string of the arguments to pass to the function.
  - **Call ID:** The unique ID of the function tool call generated by the model.
  - **ID:** The unique ID of the function tool call.
  - **Name:** The name of the function to call.
  - **Status:** The status of the function call.

## Chat Completion Response Message

- **Description:** An output message from the model.
- **Properties:**
  - **Content:** The content of the output message.
  - **ID:** The unique ID of the output message.
  - **Role:** The role of the output message.
  - **Status:** The status of the message.

## Chat Completion Response Reasoning

- **Description:** A reasoning output from the model. Available for [models that support reasoning](https://console.groq.com/docs/reasoning).
- **Properties:**
  - **ID:** The unique ID of the reasoning output.
  - **Summary:** Summary items (currently empty).
  - **Type:** The type of the reasoning output. Always `reasoning`.

## Chat Completion Response Text

- **Description:** A text output from the model.
- **Properties:**
  - **Annotations:** The annotations of the text output.
  - **Log Probabilities:** Log probability information for the output.
  - **Text:** The text output from the model.
  - **Type:** The type of the output text. Always `output_text`.

## Chat Completion Response Function Call

- **Description:** A function call generated by the model.
- **Properties:**
  - **Arguments:** A JSON string of the arguments to pass to the function.
  - **Call ID:** The unique ID of the function tool call generated by the model.
  - **ID:** The unique ID of the function tool call.
  - **Name:** The name of the function to call.
  - **Status:** The status of the function call.

## Chat Completion Response Message

- **Description:** An output message from the model.
- **Properties:**
  - **Content:** The content of the output message.
  - **ID:** The unique ID of the output message.
  - **Role:** The role of the output message.
  - **Status:** The status of the message.

## Chat Completion Response Reasoning

- **Description:** A reasoning output from the model. Available for [models that support reasoning](https://console.groq.com/docs/reasoning).
- **Properties:**
  - **ID:** The unique ID of the reasoning output.
  - **Summary:** Summary items (currently empty).
  - **Type:** The type of the reasoning output. Always `reasoning`.

## Chat Completion Response Text

- **Description:** A text output from the model.
- **Properties:**
  - **Annotations:** The annotations of the text output.
  - **Log Probabilities:** Log probability information for the output.
  - **Text:** The text output from the model.
  - **Type:** The type of the output text. Always `output_text`.

## Chat Completion Response Function Call

- **Description:** A function call generated by the model.
- **Properties:**
  - **Arguments:** A JSON string of the arguments to pass to the function.
  - **Call ID:** The unique ID of the function tool call generated by the model.
  - **ID:** The unique ID of the function tool call.
  - **Name:** The name of the function to call.
  - **Status:** The status of the function call.

## Chat Completion Response Message

- **Description:** An output message from the model.
- **Properties:**
  - **Content:** The content of the output message.
  - **ID:** The unique ID of the output message.
  - **Role:** The role of the output message.
  - **Status:** The status of the message.

## Chat Completion Response Reasoning

- **Description:** A reasoning output from the model. Available for [models that support reasoning](https://console.groq.com/docs/reasoning).
- **Properties:**
  - **ID:** The unique ID of the reasoning output.
  - **Summary:** Summary items (currently empty).
  - **Type:** The type of the reasoning output. Always `reasoning`.

## Chat Completion Response Text

- **Description:** A text output from the model.
- **Properties:**
  - **Annotations:** The annotations of the text output.
  - **Log Probabilities:** Log probability information for the output.
  - **Text:** The text output from the model.
  - **Type:** The type of the output text. Always `output_text`.

## Chat Completion Response Function Call

- **Description:** A function call generated by the model.
- **Properties:**
  - **Arguments:** A JSON string of the arguments to pass to the function.
  - **Call ID:** The unique ID of the function tool call generated by the model.
  - **ID:** The unique ID of the function tool call.
  - **Name:** The name of the function to call.
  - **Status:** The status of the function call.

## Chat Completion Response Message

- **Description:** An output message from the model.
- **Properties:**
  - **Content:** The content of the output message.
  - **ID:** The unique ID of the output message.
  - **Role:** The role of the output message.
  - **Status:** The status of the message.

## Chat Completion Response Reasoning

- **Description:** A reasoning output from the model. Available for [models that support reasoning](https://console.groq.com/docs/reasoning).
- **Properties:**
  - **ID:** The unique ID of the reasoning output.
  - **Summary:** Summary items (currently empty).
  - **Type:** The type of the reasoning output. Always `reasoning`.

## Chat Completion Response Text

- **Description:** A text output from the model.
- **Properties:**
  - **Annotations:** The annotations of the text output.
  - **Log Probabilities:** Log probability information for the output.
  - **Text:** The text output from the model.
  - **Type:** The type of the output text. Always `output_text`.

## Chat Completion Response Function Call

- **Description:** A function call generated by the model.
- **Properties:**
  - **Arguments:** A JSON string of the arguments to pass to the function.
  - **Call ID:** The unique ID of the function tool call generated by the model.
  - **ID:** The unique ID of the function tool call.
  - **Name:** The name of the function to call.
  - **Status:** The status of the function call.

## Chat Completion Response Message

- **Description:** An output message from the model.
- **Properties:**
  - **Content:** The content of the output message.
  - **ID:** The unique ID of the output message.
  - **Role:** The role of the output message.
  - **Status:** The status of the message.

## Chat Completion Response Reasoning

- **Description:** A reasoning output from the model. Available for [models that support reasoning](https://console.groq.com/docs/reasoning).
- **Properties:**
  - **ID:** The unique ID of the reasoning output.
  - **Summary:** Summary items (currently empty).
  - **Type:** The type of the reasoning output. Always `reasoning`.

## Chat Completion Response Text

- **Description:** A text output from the model.
- **Properties:**
  - **Annotations:** The annotations of the text output.
  - **Log Probabilities:** Log probability information for the output.
  - **Text:** The text output from the model.
  - **Type:** The type of the output text. Always `output_text`.

## Chat Completion Response Function Call

- **Description:** A function call generated by the model.
- **Properties:**
  - **Arguments:** A JSON string of the arguments to pass to the function.
  - **Call ID:** The unique ID of the function tool call generated by the model.
  - **ID:** The unique ID of the function tool call.
  - **Name:** The name of the function to call.
  - **Status:** The status of the function call.

## Chat Completion Response Message

- **Description:** An output message from the model.
- **Properties:**
  - **Content:** The content of the output message.
  - **ID:** The unique ID of the output message.
  - **Role:** The role of the output message.
  - **Status:** The status of the message.

## Chat Completion Response Reasoning

- **Description:** A reasoning output from the model. Available for [models that support reasoning](https://console.groq.com/docs/reasoning).
- **Properties:**
  - **ID:** The unique ID of the reasoning output.
  - **Summary:** Summary items (currently empty).
  - **Type:** The type of the reasoning output. Always `reasoning`.

## Chat Completion Response Text

- **Description:** A text output from the model.
- **Properties:**
  - **Annotations:** The annotations of the text output.
  - **Log Probabilities:** Log probability information for the output.
  - **Text:** The text output from the model.
  - **Type:** The type of the output text. Always `output_text`.

## Chat Completion Response Function Call

- **Description:** A function call generated by the model.
- **Properties:**
  - **Arguments:** A JSON string of the arguments to pass to the function.
  - **Call ID:** The unique ID of the function tool call generated by the model.
  - **ID:** The unique ID of the function tool call.
  - **Name:** The name of the function to call.
  - **Status:** The status of the function call.

## Chat Completion Response Message

- **Description:** An output message from the model.
- **Properties:**
  - **Content:** The content of the output message.
  - **ID:** The unique ID of the output message.
  - **Role:** The role of the output message.
  - **Status:** The status of the message.

## Chat Completion Response Reasoning

- **Description:** A reasoning output from the model. Available for [models that support reasoning](https://console.groq.com/docs/reasoning).
- **Properties:**
  - **ID:** The unique ID of the reasoning output.
  - **Summary:** Summary items (currently empty).
  - **Type:** The type of the reasoning output. Always `reasoning`.

## Chat Completion Response Text

- **Description:** A text output from the model.
- **Properties:**
  - **Annotations:** The annotations of the text output.
  - **Log Probabilities:** Log probability information for the output.
  - **Text:** The text output from the model.
  - **Type:** The type of the output text. Always `output_text`.

## Chat Completion Response Function Call

- **Description:** A function call generated by the model.
- **Properties:**
  - **Arguments:** A JSON string of the arguments to pass to the function.
  - **Call ID:** The unique ID of the function tool call generated by the model.
  - **ID:** The unique ID of the function tool call.
  - **Name:** The name of the function to call.
  - **Status:** The status of the function call.

## Chat Completion Response Message

- **Description:** An output message from the model.
- **Properties:**
  - **Content:** The content of the output message.
  - **ID:** The unique ID of the output message.
  - **Role:** The role of the output message.
  - **Status:** The status of the message.

## Chat Completion Response Reasoning

- **Description:** A reasoning output from the model. Available for [models that support reasoning](https://console.groq.com/docs/reasoning).
- **Properties:**
  - **ID:** The unique ID of the reasoning output.
  - **Summary:** Summary items (currently empty).
  - **Type:** The type of the reasoning output. Always `reasoning`.

## Chat Completion Response Text

- **Description:** A text output from the model.
- **Properties:**
  - **Annotations:** The annotations of the text output.
  - **Log Probabilities:** Log probability information for the output.
  - **Text:** The text output from the model.
  - **Type:** The type of the output text. Always `output_text`.

## Chat Completion Response Function Call

- **Description:** A function call generated by the model.
- **Properties:**
  - **Arguments:** A JSON string of the arguments to pass to the function.
  - **Call ID:** The unique ID of the function tool call generated by the model.
  - **ID:** The unique ID of the function tool call.
  - **Name:** The name of the function to call.
  - **Status:** The status of the function call.

## Chat Completion Response Message

- **Description:** An output message from the model.
- **Properties:**
  - **Content:** The content of the output message.
  - **ID:** The unique ID of the output message.
  - **Role:** The role of the output message.
  - **Status:** The status of the message.

## Chat Completion Response Reasoning

- **Description:** A reasoning output from the model. Available for [models that support reasoning](https://console.groq.com/docs/reasoning).
- **Properties:**
  - **ID:** The unique ID of the reasoning output.
  - **Summary:** Summary items (currently empty).
  - **Type:** The type of the reasoning output. Always `reasoning`.

## Chat Completion Response Text

- **Description:** A text output from the model.
- **Properties:**
  - **Annotations:** The annotations of the text output.
  - **Log Probabilities:** Log probability information for the output.
  - **Text:** The text output from the model.
  - **Type:** The type of the output text. Always `output_text`.

## Chat Completion Response Function Call

- **Description:** A function call generated by the model.
- **Properties:**
  - **Arguments:** A JSON string of the arguments to pass to the function.
  - **Call ID:** The unique ID of the function tool call generated by the model.
  - **ID:** The unique ID of the function tool call.
  - **Name:** The name of the function to call.
  - **Status:** The status of the function call.

## Chat Completion Response Message

- **Description:** An output message from the model.
- **Properties:**
  - **Content:** The content of the output message.
  - **ID:** The unique ID of the output message.
  - **Role:** The role of the output message.
  - **Status:** The status of the message.

## Chat Completion Response Reasoning

- **Description:** A reasoning output from the model. Available for [models that support reasoning](https://console.groq.com/docs/reasoning).
- **Properties:**
  - **ID:** The unique ID of the reasoning output.
  - **Summary:** Summary items (currently empty).
  - **Type:** The type of the reasoning output. Always `reasoning`.

## Chat Completion Response Text

- **Description:** A text output from the model.
- **Properties:**
  - **Annotations:** The annotations of the text output.
  - **Log Probabilities:** Log probability information for the output.
  - **Text:** The text output from the model.
  - **Type:** The type of the output text. Always `output_text`.

## Chat Completion Response Function Call

- **Description:** A function call generated by the model.
- **Properties:**
  - **Arguments:** A JSON string of the arguments to pass to the function.
  - **Call ID:** The unique ID of the function tool call generated by the model.
  - **ID:** The unique ID of the function tool call.
  - **Name:** The name of the function to call.
  - **Status:** The status of the function call.

## Chat Completion Response Message

- **Description:** An output message from the model.
- **Properties:**
  - **Content:** The content of the output message.
  - **ID:** The unique ID of the output message.
  - **Role:** The role of the output message.
  - **Status:** The status of the message.

## Chat Completion Response Reasoning

- **Description:** A reasoning output from the model. Available for [models that support reasoning](https://console.groq.com/docs/reasoning).
- **Properties:**
  - **ID:** The unique ID of the reasoning output.
  - **Summary:** Summary items (currently empty).
  - **Type:** The type of the reasoning output. Always `reasoning`.

## Chat Completion Response Text

- **Description:** A text output from the model.
- **Properties:**
  - **Annotations:** The annotations of the text output.
  - **Log Probabilities:** Log probability information for the output.
  - **Text:** The text output from the model.
  - **Type:** The type of the output text. Always `output_text`.

## Chat Completion Response Function Call

- **Description:** A function call generated by the model.
- **Properties:**
  - **Arguments:** A JSON string of the arguments to pass to the function.
  - **Call ID:** The unique ID of the function tool call generated by the model.
  - **ID:** The unique ID of the function tool call.
  - **Name:** The name of the function to call.
  - **Status:** The status of the function call.

## Chat Completion Response Message

- **Description:** An output message from the model.
- **Properties:**
  - **Content:** The content of the output message.
  - **ID:** The unique ID of the output message.
  - **Role:** The role of the output message.
  - **Status:** The status of the message.

## Chat Completion Response Reasoning

- **Description:** A reasoning output from the model. Available for [models that support reasoning](https://console.groq.com/docs/reasoning).
- **Properties:**
  - **ID:** The unique ID of the reasoning output.
  - **Summary:** Summary items (currently empty).
  - **Type:** The type of the reasoning output. Always `reasoning`.

## Chat Completion Response Text

- **Description:** A text output from the model.
- **Properties:**
  - **Annotations:** The annotations of the text output.
  - **Log Probabilities:** Log probability information for the output.
  - **Text:** The text output from the model.
  - **Type:** The type of the output text. Always `output_text`.

## Chat Completion Response Function Call

- **Description:** A function call generated by the model.
- **Properties:**
  - **Arguments:** A JSON string of the arguments to pass to the function.
  - **Call ID:** The unique ID of the function tool call generated by the model.
  - **ID:** The unique ID of the function tool call.
  - **Name:** The name of the function to call.
  - **Status:** The status of the function call.

## Chat Completion Response Message

- **Description:** An output message from the model.
- **Properties:**
  - **Content:** The content of the output message.
  - **ID:** The unique ID of the output message.
  - **Role:** The role of the output message.
  - **Status:** The status of the message.

## Chat Completion Response Reasoning

- **Description:** A reasoning output from the model. Available for [models that support reasoning](https://console.groq.com/docs/reasoning).
- **Properties:**
  - **ID:** The unique ID of the reasoning output.
  - **Summary:** Summary items (currently empty).
  - **Type:** The type of the reasoning output. Always `reasoning`.

## Chat Completion Response Text

- **Description:** A text output from the model.
- **Properties:**
  - **Annotations:** The annotations of the text output.
  - **Log Probabilities:** Log probability information for the output.
  - **Text:** The text output from the model.
  - **Type:** The type of the output text. Always `output_text`.

## Chat Completion Response Function Call

- **Description:** A function call generated by the model.
- **Properties:**
  - **Arguments:** A JSON string of the arguments to pass to the function.
  - **Call ID:** The unique ID of the function tool call generated by the model.
  - **ID:** The unique ID of the function tool call.
  - **Name:** The name of the function to call.
  - **Status:** The status of the function call.

## Chat Completion Response Message

- **Description:** An output message from the model.
- **Properties:**
  - **Content:** The content of the output message.
  - **ID:** The unique ID of the output message.
  - **Role:** The role of the output message.
  - **Status:** The status of the message.

## Chat Completion Response Reasoning

- **Description:** A reasoning output from the model. Available for [models that support reasoning](https://console.groq.com/docs/reasoning).
- **Properties:**
  - **ID:** The unique ID of the reasoning output.
  - **Summary:** Summary items (currently empty).
  - **Type:** The type of the reasoning output. Always `reasoning`.

## Chat Completion Response Text

- **Description:** A text output from the model.
- **Properties:**
  - **Annotations:** The annotations of the text output.
  - **Log Probabilities:** Log probability information for the output.
  - **Text:** The text output from the model.
  - **Type:** The type of the output text. Always `output_text`.

## Chat Completion Response Function Call

- **Description:** A function call generated by the model.
- **Properties:**
  - **Arguments:** A JSON string of the arguments to pass to the function.
  - **Call ID:** The unique ID of the function tool call generated by the model.
  - **ID:** The unique ID of the function tool call.
  - **Name:** The name of the function to call.
  - **Status:** The status of the function call.

## Chat Completion Response Message

- **Description:** An output message from the model.
- **Properties:**
  - **Content:** The content of the output message.
  - **ID:** The unique ID of the output message.
  - **Role:** The role of the output message.
  - **Status:** The status of the message.

## Chat Completion Response Reasoning

- **Description:** A reasoning output from the model. Available for [models that support reasoning](https://console.groq.com/docs/reasoning).
- **Properties:**
  - **ID:** The unique ID of the reasoning output.
  - **Summary:** Summary items (currently empty).
  - **Type:** The type of the reasoning output. Always `reasoning`.

## Chat Completion Response Text

- **Description:** A text output from the model.
- **Properties:**
  - **Annotations:** The annotations of the text output.
  - **Log Probabilities:** Log probability information for the output.
  - **Text:** The text output from the model.
  - **Type:** The type of the output text. Always `output_text`.

## Chat Completion Response Function Call

- **Description:** A function call generated by the model.
- **Properties:**
  - **Arguments:** A JSON string of the arguments to pass to the function.
  - **Call ID:** The unique ID of the function tool call generated by the model.
  - **ID:** The unique ID of the function tool call.
  - **Name:** The name of the function to call.
  - **Status:** The status of the function call.

## Chat Completion Response Message

- **Description:** An output message from the model.
- **Properties:**
  - **Content:** The content of the output message.
  - **ID:** The unique ID of the output message.
  - **Role:** The role of the output message.
  - **Status:** The status of the message.

## Chat Completion Response Reasoning

- **Description:** A reasoning output from the model. Available for [models that support reasoning](https://console.groq.com/docs/reasoning).
- **Properties:**
  - **ID:** The unique ID of the reasoning output.
  - **Summary:** Summary items (currently empty).
  - **Type:** The type of the reasoning output. Always `reasoning`.

## Chat Completion Response Text

- **Description:** A text output from the model.
- **Properties:**
  - **Annotations:** The annotations of the text output.