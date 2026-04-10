# Source: https://dev.writer.com/home/changelog.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Changelog

> Stay up to date with the latest changes to the Writer API and SDKs.

<Tip>To see the latest features and major improvements across the Writer platform, check out [What's new at Writer](https://support.writer.com/article/40-whats-new-at-writer).</Tip>

<Update label="2025-12-02" description="External models and guardrails">
  ## External models and guardrails now available

  You can now add external models from providers like AWS Bedrock to use alongside Palmyra models in AI Studio. You can also configure guardrails from third-party providers such as AWS Bedrock to monitor and filter agent inputs and outputs, helping enforce content safety and compliance.

  ### External models

  Add models from AWS Bedrock directly in the AI Studio UI. Once configured, external models appear in the [list models endpoint](/api-reference/completion-api/list-models) and can be used in chat completions by specifying the model ID.

  To use an external model, pass its model ID to the `model` parameter in your API requests:

  ```bash  theme={null}
  curl -X POST https://api.writer.com/v1/chat \
    -H "Authorization: Bearer $WRITER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "your-external-model-id",
      "messages": [{"role": "user", "content": "Hello!"}]
    }'
  ```

  For setup instructions, see the [external models guide](/home/external-models).

  ### Guardrails

  Configure AWS Bedrock Guardrails to enforce content safety, PII protection, and compliance policies across your AI agents. Guardrails can evaluate requests before, during, or after model calls.

  For setup instructions, see the [guardrails guide](/home/guardrails).
</Update>

<Update label="2025-10-03" description="Python and Node SDK v2.3.2">
  ## Released version 2.3.2 of the Python and Node SDKs

  Version 2.3.2 of the [Python](https://github.com/writer/writer-python) and [Node](https://github.com/writer/writer-node) SDKs adds support for the following new features:

  ### Knowledge Graph query configuration

  Added support for the `query_config` parameter in both chat completions with Knowledge Graph tools and direct Knowledge Graph queries. This parameter allows you to fine-tune search behavior and control response generation.

  Key configuration options:

  * **`inline_citations`**: Enable inline citations within response text
  * **`search_weight`**: Control the balance between keyword and semantic search
  * **`grounding_level`**: Control how closely responses match source material
  * **`max_snippets`**: Set the number of text snippets to retrieve
  * **`keyword_threshold`**: Set keyword matching strictness
  * **`semantic_threshold`**: Set semantic similarity requirements

  ### Inline citations

  SDK support for inline citations in Knowledge Graph responses, allowing you to programmatically extract and correlate citations with their source material. Citations appear in the format `[filename](cite_id)` within response text and you can match them with source data from the `references` object.

  ### Upload types for no-code applications

  Added support for the `upload_types` parameter in no-code applications, allowing you to see which file types you can upload through file input fields.

  For more details on these features:

  * Knowledge Graph query configuration: [Knowledge Graph query configuration guide](/home/knowledge-graph-query-config)
  * Inline citations: [Work with inline citations](/home/inline-citations)
  * Upload types: [No-code applications API reference](/api-reference/application-api/application-details)
</Update>

<Update label="2025-09-11" description="Knowledge Graph query configuration and inline citations">
  ## Knowledge Graph query configuration and inline citations

  Added comprehensive query configuration options for Knowledge Graph operations, allowing you to fine-tune search behavior and enable inline citations in responses from the [Knowledge Graph chat completions tool](/home/kg-chat) and [direct Knowledge Graph queries](/home/kg-query).

  ### New query configuration parameters

  The `query_config` parameter is now available for both chat completions with Knowledge Graph tools and direct Knowledge Graph queries. This parameter includes:

  * **`inline_citations`**: Enable inline citations within response text, showing which sources support each part of the response
  * **`search_weight`**: Control the balance between keyword and semantic search (0-100, default: 50)
  * **`max_subquestions`**: Set the maximum number of sub-questions for complex queries (1-10, default: 6)
  * **`grounding_level`**: Control how closely responses match source material (0.0-1.0, default: 0.0)
  * **`max_snippets`**: Set the number of text snippets to retrieve (5-25 recommended, default: 30)
  * **`max_tokens`**: Control the maximum response length (100-8000, default: 4000)
  * **`keyword_threshold`**: Set keyword matching strictness (0.0-1.0, default: 0.7)
  * **`semantic_threshold`**: Set semantic similarity requirements (0.0-1.0, default: 0.7)

  For detailed information about all configuration options and their effects, see the [Knowledge Graph query configuration guide](/home/knowledge-graph-query-config). For more information about inline citations, see the [Work with inline citations in Knowledge Graph responses](/home/inline-citations) guide.
</Update>

<Update label="2025-08-20" description="Python and Node SDK v2.3.1">
  ## Released version 2.3.1 of the Python and Node SDKs

  This patch release fixes a bug introduced in version 2.3.0 where the `Graph` class wasn't accessible. The `Graph` class is now available in the Python and Node SDKs as it was previously.

  For more information on working with Knowledge Graphs with the Python and Node SDKs, see the [Knowledge Graphs usage guide](/home/knowledge-graph).
</Update>

<Update label="2025-08-19" description="langchain-writer v0.3.3">
  ## langchain-writer v0.3.3

  The [langchain-writer](https://github.com/writer/langchain-writer) package now includes the [web search tool](/home/web-search-tool) for chat completions. This tool allows you to search the web for current information during a conversation with a Palmyra model.

  For more details, see the [langchain-writer changelog](https://github.com/writer/langchain-writer/releases/tag/v0.3.3).
</Update>

<Update label="2025-08-14" description="Python and Node SDK v2.3.0">
  ## Released version 2.3.0 of the Python and Node SDKs

  Version 2.3.0 of the [Python](https://github.com/writer/writer-python) and [Node](https://github.com/writer/writer-node) SDKs adds support for the following new features:

  * [Web search API](#web-search-api)
  * [Web search tool for chat completions](#web-search-tool-for-chat-completions)
  * [Web connector URLs for Knowledge Graphs](#web-connector-urls-for-knowledge-graphs)
  * [Image support in chat completions](#image-support-in-chat-completions)

  See below for more details about each of these features.

  ### Web search and web connector URLs

  Three new features are now available to enhance your AI applications with web content and search capabilities:

  * [Web search tool API](#web-search-tool-api)
  * [Web search tool for chat completions](#web-search-tool-for-chat-completions)
  * [Web connector URLs for Knowledge Graphs](#web-connector-urls-for-knowledge-graphs)

  #### Web search API

  The new [web search tool API](/home/web-search) allows you to search the web for current information and get real-time results. This tool is useful for finding factual information, news, and data that may not be available in your model's training data.

  Key features:

  * Search for current information and news
  * Filter results by domain, time range, and geographic location
  * Control search depth and result comprehensiveness
  * Support for both general and news-specific searches

  #### Web search tool for chat completions

  The [web search prebuilt tool](/home/web-search-tool) for chat completions enables your AI assistant to search the web during conversations with Palmyra models. This allows your AI to provide up-to-date information and answer questions about current events.

  #### Web connector URLs for Knowledge Graphs

  [Web connector URLs](/home/web-connector-url) allow you to automatically extract and index content from websites into your Knowledge Graphs. This enables you to:

  * Process single pages or entire sub-pages
  * Monitor the status of URL processing
  * Exclude specific URLs from processing
  * Query web content through your Knowledge Graph

  ### Image support in chat completions

  Added support for [mixed content in chat completions](/home/chat-with-images) with Palmyra X5, allowing you to include images directly in your chat messages. This feature enables rich visual conversations without needing to use the separate Vision tool.

  ### References

  For more information, see the following API reference docs and guides:

  * Web search tool: [API reference](/api-reference/tool-api/web-search) and [guide](/home/web-search)
  * Web search tool for chat completions: [API reference](/api-reference/completion-api/chat-completion#body-tools) and [guide](/home/web-search-tool)
  * Web connector URLs for Knowledge Graphs: [API reference](/api-reference/kg-api/update-graph#body-urls) and [guide](/home/web-connector-url)
  * Chat with images: [API reference](/api-reference/completion-api/chat-completion#body-messages-content) and [guide](/home/chat-with-images)
</Update>

<Update label="2025-08-12" description="Vision chat support for Palmyra X5">
  ### Vision chat support for Palmyra X5

  Added support for [mixed content in chat completions](/home/chat-with-images) with Palmyra X5, allowing you to include images directly in your chat messages. This feature enables rich visual conversations without needing to use the separate Vision tool.

  Key capabilities:

  * Send messages containing both text and images
  * Support for multiple images in a single message
  * Use of data URLs for local images
  * Natural conversation flow with visual context

  Below is an example of a chat completion request that includes a message with both text and an image.

  <CodeGroup>
    ```bash cURL theme={null}
    curl --location 'https://api.writer.com/v1/chat' \
    --header 'Content-Type: application/json' \
    --header "Authorization: Bearer $WRITER_API_KEY" \
    --data '{
      "model": "palmyra-x5",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "What do you see in this image?"
            },
            {
              "type": "image_url",
              "image_url": {
                "url": "https://example.com/image.jpg"
              }
            }
          ]
        }
      ]
    }'
    ```

    ```python Python theme={null}
    from writerai import Writer

    # Initialize the client. If you don't pass the `apiKey` parameter,
    # the client looks for the `WRITER_API_KEY` environment variable.
    client = Writer()

    response = client.chat.chat(
      model="palmyra-x5",
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "What do you see in this image?"
            },
            {
              "type": "image_url",
              "image_url": {
                "url": "https://example.com/image.jpg"
              }
            }
          ]
        }
      ]
    )

    print(response.choices[0].message.content)
    ```

    ```javascript JavaScript theme={null}
    import { Writer } from "writer-sdk";

    // Initialize the client. If you don't pass the `apiKey` parameter,
    // the client looks for the `WRITER_API_KEY` environment variable.
    const client = new Writer();

    const response = await client.chat.chat({
      model: "palmyra-x5",
      messages: [
        {
          role: "user",
          content: [
            {
              type: "text",
              text: "What do you see in this image?"
            },
            {
              type: "image_url",
              image_url: {
                url: "https://example.com/image.jpg"
              }
            }
          ]
        }
      ]
    });

    console.log(response.choices[0].message.content);
    ```
  </CodeGroup>
</Update>

<Update label="2025-01-27" description="Web search and web connector URLs released">
  ## Web search and web connector URLs released

  Three new features are now available to enhance your AI applications with web content and search capabilities:

  * [Web search tool API](#web-search-tool-api)
  * [Web search tool for chat completions](#web-search-tool-for-chat-completions)
  * [Web connector URLs for Knowledge Graphs](#web-connector-urls-for-knowledge-graphs)

  ### Web search tool API

  The new [web search tool API](/home/web-search) allows you to search the web for current information and get real-time results. This tool is useful for finding factual information, news, and data that may not be available in your model's training data.

  Key features:

  * Search for current information and news
  * Filter results by domain, time range, and geographic location
  * Control search depth and result comprehensiveness
  * Support for both general and news-specific searches

  ### Web search tool for chat completions

  The [web search prebuilt tool](/home/web-search-tool) for chat completions enables your AI assistant to search the web during conversations with Palmyra models. This allows your AI to provide up-to-date information and answer questions about current events.

  ### Web connector URLs for Knowledge Graphs

  [Web connector URLs](/home/web-connector-url) allow you to automatically extract and index content from websites into your Knowledge Graphs. This enables you to:

  * Process single pages or entire sub-pages
  * Monitor the status of URL processing
  * Exclude specific URLs from processing
  * Query web content through your Knowledge Graph

  For more information, see the following guides:

  * [Web search tool API documentation](/api-reference/tool-api/web-search)
  * [Web search tool for chat completions](/home/web-search-tool)
  * [Web connector URLs for Knowledge Graphs](/home/web-connector-url)
</Update>

<Update label="2025-07-16" description="Writer Strands Agents integration released">
  ## Writer Strands Agents integration released

  You can now use Writer's models with [AWS' Strands Agents](https://github.com/strands-agents/sdk-python), an open-source SDK for building and deploying AI agents. See the new [Strands integration guide](/home/integrations/strands) for setup instructions, configuration, and examples.
</Update>

<Update label="2025-07-16" description="2.2.1 of the Python and Node SDKs">
  ## Released version 2.2.1 of the Python and Node SDKs

  Version 2.2.1 of the [Python](https://github.com/writer/writer-python) and [Node](https://github.com/writer/writer-node) SDKs adds support for filtering files by file type.

  To filter files by type, use the `file_types` parameter to pass a comma-separated string of file extensions (without the dot) to the `files.list` method. The following code shows how to filter for only PDF and DOCX files:

  <CodeGroup>
    ```python Python theme={null}
    files = client.files.list(file_types="pdf,docx")
    ```

    ```javascript JavaScript theme={null}
    const files = await client.files.list({ file_types: 'pdf,docx' });
    ```
  </CodeGroup>

  For more information on the `files.list` method and its parameters, refer to the [List Files API documentation](/api-reference/file-api/get-all-files).
</Update>

<Update label="2025-07-10" description="instructor-writer supports JSON output">
  ## Writer Instructor integration now supports JSON output

  Added support for the `WRITER_JSON` mode in the [Instructor integration](/home/integrations/instructor#json-mode). This mode allows you to receive structured output directly as JSON, following your specified schema, making it easier to work with validated, structured data from LLM responses.
</Update>

<Update label="2025-05-12" description="langchain-writer v0.3.1">
  ## langchain-writer v0.3.1

  The [langchain-writer](https://github.com/writer/langchain-writer) package now includes the [translation tool](/home/translation-tool) for chat completions. This tool allows you to translate text between languages during chats with Palmyra LLMs.

  For more details, see the [langchain-writer changelog](https://github.com/writer/langchain-writer/releases/tag/v0.3.1).
</Update>

<Update label="2025-05-02" description="Filter files by type">
  ## Filter files by type

  The [`/v1/files` endpoint](/api-reference/file-api/get-all-files#parameter-file-types) now supports filtering files by extension type.

  To filter files by type, pass a comma-separated string of file extensions to the `file_types` query parameter. For example, `file_types=txt,pdf,docx`.

  <CodeGroup>
    ```bash cURL theme={null}
    curl --location --request GET "https://api.writer.com/v1/files?file_types=txt,pdf,docx" \
      --header "Authorization: Bearer $WRITER_API_KEY" \
    ```
  </CodeGroup>

  The `file_types` parameter will be available in the next version of the Python and Node SDKs.
</Update>

<Update label="2025-04-30" description="Python and Node SDK v2.2.0">
  ## Released version 2.2.0 of the Python and Node SDKs

  Version 2.2.0 of the [Python](https://github.com/writer/writer-python) and [Node](https://github.com/writer/writer-node) SDKs adds support the following features:

  * [Structured output](/home/structured-output) for the chat completions endpoint
  * [AI detection endpoint](/home/ai-detect)
  * [Text translation endpoint](/home/translation)
  * [The text translation tool](/home/translation-tool) for chat completions

  The [langchain-writer](https://github.com/writer/langchain-writer) package has been updated to support structured output. See the [langchain-writer changelog](https://github.com/writer/langchain-writer/releases/tag/v0.3.0) for more details.

  See the API reference documentation for information about the new endpoints and tools:

  * [Structured output for chat completions](/api-reference/completion-api/chat-completion#body-response-format)
  * [AI detection](/api-reference/tool-api/ai-detect)
  * [Text translation](/api-reference/translation-api/translate)
  * [The text translation tool](/api-reference/completion-api/chat-completion#body-tools)
</Update>

<Update label="2025-04-29" description="Palmyra X5 and X4 on Amazon Bedrock">
  ## Palmyra X5 and X4 now available on Amazon Bedrock

  Palmyra X5 and X4 are now available on [Amazon Bedrock](https://aws.amazon.com/bedrock/).

  Amazon Bedrock is a fully managed service from AWS that enables developers to build and scale generative AI applications using foundation models from leading AI companies. This integration allows you to use Palmyra X5 and X4 in Amazon's serverless environment.

  See the following resources for more information:

  * [Guide for setting up and using Palmyra X5 and X4 on Amazon Bedrock](/home/integrations/bedrock)
  * [AWS blog post about using Palmyra X5 and X4 on Amazon Bedrock](https://aws.amazon.com/blogs/aws/writer-palmyra-x5-and-x4-foundation-models-are-now-available-in-amazon-bedrock/)
</Update>

<Update label="2025-04-28" description="Palmyra X5">
  ## Palmyra X5 model now available

  The [Palmyra X5 model](/home/models#palmyra-x5) is now available via the API and SDKs.

  Palmyra X5 is Writer's newest and most advanced model for building and scaling AI agents, featuring a 1 million token context window, adaptive reasoning, and industry-leading speed and cost efficiency.

  <Info>As part of this release, Palmyra X 004 is now called Palmyra X4.</Info>

  Palmyra X5's 1M token context window further streamlines enterprise workflows and unlocks complex, multi-step use cases that weren't possible before, such as:

  **Multi-step agentic workflows**

  * **Support documentation**: Classify requests, assess urgency, assign a human review, stage updates in a CMS, and publish after approval.
  * **Fund reporting**: Streamline the analysis and preparation of detailed reports on the performance and status of investment funds, using reporting and research data pulled in from third-party systems
  * **Content lifecycle management**: Flag content that could be outdated, generate suggested revisions, and share them for human review.

  **Large data requirements**:

  * **Customer feedback analysis**: Analyze large volumes of customer feedback to identify common themes, summarize sentiments, and generate actionable insights.
  * **Research and development**: Process and summarize multiple technical reports, research papers, and experimental data, accelerating innovation and product development.
  * **Financial reporting**: Process and summarize annual reports, SEC filings, and market analysis reports together at once to extract financial data, identify trends, and generate executive summaries.
  * **Legal document analysis**: Analyze lengthy legal documents, including contracts, patents, and compliance reports, to identify key clauses, flag potential risks, and ensure regulatory compliance.
  * **Medical records analysis**: Analyze and summarize large files of medical records containing structured and unstructured data, including patient records, clinical trial reports, audit reports, and more.

  See the [Palmyra X5 model overview](/home/models#palmyra-x5) for more details and [examples of using Palmyra X5 with the text generation and chat completion endpoints](/home/models#using-models-with-the-writer-api).
</Update>

<Update label="2025-04-15" description="langchain-writer supports Python 3.9">
  ## Writer LangChain integration now supports Python 3.9

  The [Writer LangChain integration](/home/integrations/langchain) now supports versions of Python 3.9 and higher, as of [version 0.2.0](https://github.com/writer/langchain-writer/releases/tag/v0.2.0).
</Update>

<Update label="2025-04-10" description="Terminology updates">
  ## Terminology updates

  As part of Writer's [recent product announcement](https://writer.com/blog/writer-ai-hq), no-code applications are now called [no-code agents](/no-code/introduction). The [Applications API](api-reference/application-api/applications), which you can use to programmatically interact with no-code agents, still uses the term `application` to minimize breaking changes.

  The guides for [invoking no-code apps](/home/applications), [async applications](/home/async-applications), and [using no-code apps as tools](/home/applications-tool-calling) have been updated to reflect the new terminology. However, the [Applications API](/api-reference/application-api/applications) reference documentation still reflects previous terminology.
</Update>

<Update label="2025-04-04" description="Python and Node SDK v2.1.0">
  ## Released version 2.1.0 of the Python and Node SDKs

  This release adds support for the [vision endpoint](/api-reference/vision-api/analyze-images) and the [vision tool](/home/vision-tool) for chat completions.

  It also adds streaming helper methods to process streaming responses from the chat completions endpoint.

  * [Streaming helpers in Python](https://github.com/writer/writer-python?tab=readme-ov-file#streaming-helpers)
  * [Streaming helpers in Node](https://github.com/writer/writer-node?tab=readme-ov-file#streaming-helpers)
</Update>

<Update label="2025-03-26" description="New cookbooks">
  ## New cookbooks for Palmyra models

  We've added three new [cookbooks](/home/cookbooks#palmyra-models) to help you explore domain-specific Palmyra models for creative, financial, and medical use cases.

  * [Palmyra Creative](https://github.com/writer/cookbooks/blob/main/models/palmyra_creative.ipynb)
  * [Palmyra Fin](https://github.com/writer/cookbooks/blob/main/models/palmyra_fin.ipynb)
  * [Palmyra Med](https://github.com/writer/cookbooks/blob/main/models/palmyra_med.ipynb)
</Update>

<Update label="2025-03-20" description="New vision endpoint">
  ## Palmyra Vision now available via the API

  The [Palmyra Vision model](/home/models#palmyra-vision) is now available via the API with the [`/vision` endpoint](/api-reference/vision-api/analyze-images).

  <CodeGroup>
    ```bash cURL theme={null}
    curl -X POST \
      'https://api.writer.com/v1/vision' \
      -H 'Content-Type: application/json' \
      -H "Authorization: Bearer $WRITER_API_KEY" \
      --data-raw '{
        "model": "palmyra-vision",
        "prompt": "What's the difference between the image {{image_1}} and the image {{image_2}}?",
        "variables": [
          {"name": "image_1", "file_id": "f1234"},
          {"name": "image_2", "file_id": "f5678"}
        ]
      }'
    ```
  </CodeGroup>

  The `/vision` endpoint analyzes images based on a prompt. You can use the endpoint for a variety of use cases, including:

  * Extracting handwritten text
  * Interpreting charts and graphs
  * Generating product descriptions

  Find additional use cases in the [Palmyra Vision overview](https://writer.com/llms/palmyra-vision/).

  See the [vision API guide](/home/analyze-images) for a detailed walkthrough of uploading images and passing them to the `/vision` endpoint, or check out the full [vision API reference](/api-reference/vision-api/analyze-images).
</Update>

<Update label="2025-03-10" description="langchain-writer v0.1.0">
  ## Released langchain-writer v0.1.0

  * Updated tool binding to align with standard LangChain tool calling conventions.
  * Added a new `NoCodeAppTool` tool for using no-code applications as tools.
  * Added a new `LLMTool` tool for delegating to a specific Palmyra model.

  See the [guide to using the LangChain integration](/home/integrations/langchain) and the [package documentation](https://github.com/writer/langchain-writer/tree/main/docs) for more details.
</Update>

<Update label="2025-03-05" description="New cookbooks">
  ## New cookbooks for tool calling and no-code applications

  We've added three new [cookbooks](/home/cookbooks) to help you get started with no-code applications and tool calling.

  * [Generating content from no-code applications with the SDK](https://github.com/writer/cookbooks/blob/main/applications/application_basic_usage.ipynb)
  * [Delegating a medical question to the `palmyra-med` model](https://github.com/writer/cookbooks/blob/main/tool_calling/tool_calling_llm.ipynb)
  * [Using the Knowledge Graph chat tool](https://github.com/writer/cookbooks/blob/main/tool_calling/tool_calling_kg.ipynb)
</Update>

<Update label="2025-03-03" description="palmyra-fin">
  ## Palmyra Fin model updates

  [Palmyra Fin](/home/models#palmyra-fin), our financial model, now has a 128k context window, up from 32k.

  To use the Palmyra Fin model in the API and SDKs, use the `palmyra-fin` model ID. The `palmyra-fin-32k` model ID is now deprecated.
</Update>

<Update label="2025-02-28" description="langchain-writer v0.0.3">
  ## Released Writer LangChain integration

  We're excited to announce the first release of `langchain-writer`, the official Writer LangChain integration. This release includes:

  * The `ChatWriter` model for text generation
  * Tool calling capabilities, including the `GraphTool` for retrieving information from a Knowledge Graph
  * Additional tools like the `PDFParser` for parsing PDFs and the `WriterTextSplitter` for intelligent text splitting

  Check out the [tutorial](/home/integrations/langchain) to get started and the full [integration documentation](https://github.com/writer/langchain-writer/blob/main/docs/) for more details.
</Update>

<Update label="2025-02-27" description="Python and Node SDK v2.0.0">
  ## Released version 2.0.0 of the Python and Node SDKs

  The 2.0.0 release includes new functionality for the Writer SDKs for Python and Node:

  * **Model delegation tool**: A prebuilt, remotely executed tool that lets you delegate domain-specific requests to the appropriate Palmyra model. For example, if your application has finance questions, you can use the tool to allow Palmyra X4 to delegate these questions to Palmyra Financial. Read more in our [model delegation guide](/home/model-delegation).
  * **Retrieve application details**: Retrieve details for all of your no-code applications. Programmatically retrieve application inputs rather than relying on the AI Studio UI. This pairs well with our guide on [using no-code applications as tools](/home/applications).
  * **Async jobs**: Trigger no-code application content generation asynchronously and retrieve or retry the job at a later time. This is great for long-running no-code applications, such as research assistant applications. To learn more, check out the [guide on async jobs](/home/async-applications).
  * **Associate Knowledge Graphs with chat applications**: Retrieve or update which Knowledge Graphs are associated with no-code chat applications.

  <Warning>
    The 2.0.0 release includes some breaking changes to the underlying models used in chat completion. This won't affect you if you are only using chat completion via the `Writer.chat.chat` method, but it will if you are importing specific types directly. See below for more details about changes in each SDK.
  </Warning>

  See the SDK repositories for the full changelogs:

  * [Python](https://github.com/writer/writer-python/releases)
  * [Node](https://github.com/writer/writer-node/releases)

  ### Python SDK

  See below for the mapping of old types to new types:

  | Old                                                 | New                                                  |
  | --------------------------------------------------- | ---------------------------------------------------- |
  | `chat_chat_params.Tool`                             | `types.shared_params.tool_param.ToolParam`           |
  | `types.Chat`                                        | `types.chat_completion.ChatCompletion`               |
  | `types.chat.ChoiceMessageGraphDataSource`           | `types.shared.source.Source`                         |
  | `types.chat.ChoiceMessageGraphDataSubquerySource`   | `types.shared.source.Source`                         |
  | `types.chat_completion_chunk.ChoiceDeltaGraphData`  | `types.shared.graph_data.GraphData`                  |
  | `types.chat_completion_chunk.Usage`                 | `types.chat_completion_usage`                        |
  | `types.chat_completion_chunk.ChoiceMessageToolCall` | `types.shared.tool_call_streaming.ToolCallStreaming` |
  | `types.question.Source`                             | `types.shared.source.Source`                         |
  | `types.question.SubquerySource`                     | `types.shared.source.Source`                         |

  Additionally:

  * The `types.chat_completion_chunk.Message` type has been moved to its own model: `types.chat_completion_message`.

  * `types.chat.ChoiceLogprobsContent`, `ChoiceLogprobsRefusal`, `ChoiceLogprobsContentTopLogprob`, and `ChoiceLogprobsRefusalTopLogprob` have all been deduplicated and replaced by a shared model `types.shared.logprobs_token.LogprobsToken`.

  ### Node SDK

  See below for the mapping of old types to new types:

  | Old                                          | New                                |
  | -------------------------------------------- | ---------------------------------- |
  | `ChatResource`                               | `Chat`                             |
  | `Chat`                                       | `ChatCompletion`                   |
  | `Chat.Choice`                                | `ChatCompletionChoice`             |
  | `Chat.Choice.Message`                        | `ChatCompletionMessage`            |
  | `Chat.Choice.Logprobs`                       | `Shared.Logprobs`                  |
  | `Chat.Choice.Logprobs.Content`               | `Shared.LogprobsToken`             |
  | `Chat.Choice.Logprobs.Refusal`               | `Shared.LogprobsToken`             |
  | `Chat.Usage`                                 | `ChatCompletionUsage`              |
  | `ChatCompletionChunk.Choice.Message`         | `ChatCompletionMessage`            |
  | `ChatCompletionChunk.Choice.Delta`           | `ChatCompletionChunk.Choice.Delta` |
  | `ChatCompletionChunk.Choice.Delta.GraphData` | `Shared.GraphData`                 |
  | `ChatCompletionChunk.Choice.Delta.ToolCall`  | `Shared.ToolCallStreaming`         |
  | `ChatCompletionChunk.Choice.Logprobs`        | `Shared.Logprobs`                  |
  | `ChatCompletionChunk.Usage`                  | `ChatCompletionUsage`              |
  | `ChatChatParams.Message.GraphData`           | `Shared.GraphData`                 |
  | `ChatChatParams.Message.ToolCall`            | `Shared.ToolCall`                  |
  | `ChatChatParams.StringToolChoice`            | `Shared.ToolChoiceString`          |
  | `ChatChatParams.JsonObjectToolChoice`        | `Shared.ToolChoiceJsonObject`      |
  | `ChatChatParams.FunctionTool`                | `Shared.ToolParam.FunctionTool`    |
  | `ChatChatParams.GraphTool`                   | `Shared.ToolParam.GraphTool`       |
  | `StreamingData`                              | `CompletionChunk`                  |
  | `Completion.Choice.LogProbs`                 | `Shared.Logprobs`                  |

  The Node SDK includes developer experience improvements from [Stainless](https://www.stainlessapi.com/), including using the native `fetch` API, resulting in zero SDK dependencies.
</Update>

<Update label="2024-12-20" description="Python SDK v1.6.1">
  ## Released version 1.6.1 of the Python SDK

  * Fixed a typing bug where the `content` field in the `File` did not accept the correct `FileTypes` values.
</Update>

<Update label="2024-12-16" description="Python SDK v1.6.0; Node SDK v1.5.0">
  ## Released Python SDK version 1.6.0 and Node SDK version 1.5.0

  * Added streaming support to the [applications content generation endpoint](/api-reference/application-api/applications) and updated the [No-code applications guide](/home/applications) to reflect this.
</Update>

<Update label="2024-11-29" description="Python SDK v.1.5.0">
  ## Released Python SDK version 1.5.0

  * Added new functionality via manual API updates
  * Fixed compatibility with the latest `httpx` 0.28.0 release
  * Improved handling of deprecated arguments (`transport`, `proxies`) to maintain backward compatibility
  * Fixed compatibility issues with Pydantic `model_dump` method when warnings are passed
  * Removed the now unused `cached-property` dependency, as we now rely on the standard library implementation for Python 3.8+
  * Enhanced logging documentation in README, adding information about the 'info' log level
  * Updated the recommended log level from 'debug' to 'info' for standard usage
  * Fixed code formatting for better readability and consistency
  * Excluded test files from `mypy` checks to avoid false positives
  * Updated internal compatibility layer for better type checking
  * Improved error handling for deprecated client configuration options
</Update>

<Update label="2024-11-14" description="Python and Node SDK v1.4.0">
  ## Released Python and Node SDK versions 1.4.0

  * Updated the default timeout on the Writer client to three minutes.
</Update>
