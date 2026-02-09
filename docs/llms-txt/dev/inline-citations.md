# Source: https://dev.writer.com/home/inline-citations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Work with inline citations in Knowledge Graph responses

This guide shows you how to work with inline citations in Knowledge Graph responses. Inline citations show which specific sources support each part of the response, enabling you to verify information and trace claims back to their origins.

<CardGroup>
  <Card title="Response with inline citations">
    Below is an example of a response from a Knowledge Graph that includes inline citations:

    ```
    Acme Corp's flagship product line includes three
    main categories: industrial tools, consumer
    electronics, and automotive parts. The industrial
    tools division offers precision manufacturing
    equipment with advanced automation capabilities
    [Acme-Product-Catalog.pdf](a1b2c3d4-e5f6-7890-abcd-ef1234567890).
    ```
  </Card>

  <Card title="Corresponding references array">
    Below is the corresponding `references` object that contains a direct snippet from the source file that was used to support the response:

    ```json  theme={null}
    {"files": [
      {
        "text": "Industrial Tools Division: Our precision manufacturing equipment features advanced automation capabilities with real-time monitoring systems that reduce operational downtime by up to 40% through predictive maintenance algorithms.",
        "fileId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "score": 0.95,
        "page": 12,
        "cite": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
      }
    ]}
    ```
  </Card>
</CardGroup>

## Enable inline citations

To enable inline citations in Knowledge Graph responses, set `inline_citations: true` in your `query_config` parameter when making direct Knowledge Graph queries via the `/v1/graphs/question` endpoint.

<CodeGroup>
  ```bash cURL highlight={7-9} theme={null}
  curl --location --request POST 'https://api.writer.com/v1/graphs/question' \
    --header "Authorization: Bearer $WRITER_API_KEY" \
    --header 'Content-Type: application/json' \
    --data-raw '{
      "graph_ids": ["<GRAPH_ID>"],
      "question": "What are the key features of our product?",
      "query_config": {
        "inline_citations": true
      }
    }'
  ```

  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client
  client = Writer()

  # Query Knowledge Graph with inline citations enabled
  response = client.graphs.question(
      graph_ids=["<GRAPH_ID>"],
      question="What are the key features of our product?",
      query_config={
          "inline_citations": True
      }
  )

  print(f"Answer: {response.answer}")
  print(f"\nFile references: {response.references.files}")
  print(f"\nWeb references: {response.references.web}")
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from 'writer-sdk';

  // Initialize the Writer client
  const client = new Writer();

  // Query Knowledge Graph with inline citations enabled
  const response = await client.graphs.question({
      graph_ids: ["<GRAPH_ID>"],
      question: "What are the key features of our product?",
      query_config: {
          inline_citations: true
      }
  });

  console.log(`Answer: ${response.answer}`);
  console.log(`\nFile references: ${response.references.files}`);
  console.log(`\nWeb references: ${response.references.web}`);
  ```
</CodeGroup>

## Citation format and correlation

### Citation format

Inline citations appear in the answer from the LLM as `[source_name](identifier)`, where:

* `source_name` is the display name of the source: either the filename for files, or the page title for web sources
* `identifier` is the unique identifier used to correlate with the references array

The identifier format depends on the source type:

* **File sources**: Uses the `cite` field value, for example, `[document.pdf](a1b2c3d4-e5f6-7890-abcd-ef1234567890)`
* **Web sources**: Uses the `url` field value, for example, `[Web Page Title](https://example.com/page)`

### Correlate citations with references

Inline citations correspond to entries in the `references` object. Correlation differs by source type:

* **File sources**: Citations use the `cite` field from the file reference object as their identifier
* **Web sources**: Citations use the `url` field from the web reference object as their identifier

**Example correlation**:

Here's an example showing how inline citations correlate with the references array for both file and web sources:

**Response text**:

```
Acme Corp's flagship product line includes three main categories: industrial tools, consumer electronics, and automotive parts.
The industrial tools division offers precision manufacturing equipment with advanced automation capabilities
[Acme-Product-Catalog.pdf](a1b2c3d4-e5f6-7890-abcd-ef1234567890). According to recent industry analysis,
smart manufacturing adoption has increased by 40% across similar companies [Industry Trends Report](https://example.com/industry-trends).
```

**References object**:

```json  theme={null}
{
  "files": [
    {
      "text": "Industrial Tools Division: Our precision manufacturing equipment features advanced automation capabilities with real-time monitoring systems that reduce operational downtime by up to 40% through predictive maintenance algorithms.",
      "fileId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "score": 0.95,
      "page": 12,
      "cite": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
  ],
  "web": [
    {
      "text": "Smart manufacturing adoption rates have increased by 40% across mid-size manufacturing companies, driven by automation and IoT integration.",
      "url": "https://example.com/industry-trends",
      "title": "Industry Trends Report",
      "score": 0.88
    }
  ]
}
```

**Citation mapping**:

* Citation `[Acme-Product-Catalog.pdf](a1b2c3d4-e5f6-7890-abcd-ef1234567890)` uses the `cite` field from the file reference object
* Citation `[Industry Trends Report](https://example.com/industry-trends)` uses the `url` field from the web reference object

## Link citations to source text with SDKs

When working with inline citations in SDK responses, you can programmatically link citation IDs to their corresponding source text. This enables you to build applications that display citations with their source material.

### Extract and correlate citations

These code samples demonstrate how to extract inline citations from Knowledge Graph responses and correlate them with their source material. The code parses citation markers in the answer text (like `[filename](citation-id)`) and matches them to the corresponding source text in the references object. Using similar patterns, you can extract citations and build applications that display citations with their source material.

<CodeGroup>
  ```python Python theme={null}
  from writerai import Writer
  import re

  # Initialize the Writer client
  client = Writer()

  # Query Knowledge Graph with inline citations
  response = client.graphs.question(
      graph_ids=["<GRAPH_ID>"],
      question="What are the key features of our product?",
      query_config={
          "inline_citations": True
      }
  )

  def extract_citations_with_sources(answer_text, references):
      '''Extract citations from answer text and link them to source material.
      
      This function parses inline citations from Knowledge Graph responses and correlates
      them with their source material from the references object.
      
      Args:
          answer_text (str): The response text containing inline citations
          references (object): The references object containing files and web sources
          
      Returns:
          list: Array of citation objects with source text and metadata
      '''
      # Use regex to find all citations in the format [display_text](identifier)
      # This pattern matches markdown-style links like [filename](citation-id)
      citation_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
      citations = re.findall(citation_pattern, answer_text)
      
      citation_data = []
      
      # Process each citation found in the answer text
      for display_text, identifier in citations:
          # Initialize citation info structure
          citation_info = {
              "display_text": display_text,  # The text shown in the citation (e.g., filename)
              "identifier": identifier,  # The unique citation ID
              "source_text": None,  # The actual source text
              "source_type": None   # The source type: "file" or "web"
          }
          
          # Search through file references to find matching citation
          if references and hasattr(references, 'files') and references.files:
              for file_ref in references.files:
                  # Match citation ID with the 'cite' field in file references
                  if hasattr(file_ref, 'cite') and file_ref.cite == identifier:
                      citation_info["source_text"] = file_ref.text  # Extract source text snippet
                      citation_info["source_type"] = "file"  # Mark as file source
                      citation_info["file_id"] = file_ref.file_id  # Store file ID for reference
                      citation_info["page"] = file_ref.page  # Store page number if available
                      break
          
          # Search through web references to find matching citation
          if references and hasattr(references, 'web') and references.web:
              for web_ref in references.web:
                  # Match citation ID with the 'url' field in web references
                  if hasattr(web_ref, 'url') and web_ref.url == identifier:
                      citation_info["source_text"] = web_ref.text  # Extract source text snippet
                      citation_info["source_type"] = "web"  # Mark as web source
                      citation_info["url"] = web_ref.url  # Store URL for reference
                      citation_info["title"] = web_ref.title  # Store page title
                      break
          
          citation_data.append(citation_info)
      
      return citation_data

  # Extract citations with their source text
  # This processes the response and creates a structured list of citations with their source material
  citations = extract_citations_with_sources(response.answer, response.references)

  # Display citations with source material
  # Loop through each citation and print its details along with the source text
  for citation in citations:
      print(f"Citation: [{citation['display_text']}]({citation['identifier']})")
      print(f"Source type: {citation['source_type']}")
      print(f"Source text: {citation['source_text']}")
      
      # Show additional metadata based on source type
      if citation['source_type'] == 'file':
          print(f"File ID: {citation['file_id']}, Page: {citation['page']}")
      elif citation['source_type'] == 'web':
          print(f"URL: {citation['url']}, Title: {citation['title']}")
      
      print("-" * 50)  # Separator between citations
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from 'writer-sdk';

  // Initialize the Writer client
  const client = new Writer();

  // Query Knowledge Graph with inline citations
  const response = await client.graphs.question({
      graph_ids: ["<GRAPH_ID>"],
      question: "What are the key features of our product?",
      query_config: {
          inline_citations: true
      }
  });

  function extractCitationsWithSources(answerText, references) {
      /**
       * Extract citations from answer text and link them to source material.
       * 
       * This function parses inline citations from Knowledge Graph responses and correlates
       * them with their source material from the references object.
       * 
       * @param {string} answerText - The response text containing inline citations
       * @param {object} references - The references object containing files and web sources
       * @returns {Array} Array of citation objects with source text and metadata
       */
      
      // Use regex to find all citations in the format [display_text](identifier)
      // This pattern matches markdown-style links like [filename](citation-id)
      const citationPattern = /\[([^\]]+)\]\(([^)]+)\)/g;
      const citations = [];
      let match;
      
      // Process each citation found in the answer text
      while ((match = citationPattern.exec(answerText)) !== null) {
          const [fullMatch, displayText, identifier] = match;
          
          // Initialize citation info structure
          const citationInfo = {
              displayText: displayText,    // The text shown in the citation (e.g., filename)
              identifier: identifier,      // The unique citation ID
              sourceText: null,          // The actual source text
              sourceType: null           // The source type: "file" or "web"
          };
          
          // Search through file references to find matching citation
          if (references?.files) {
              for (const fileRef of references.files) {
                  // Match citation ID with the 'cite' field in file references
                  if (fileRef.cite === identifier) {
                      citationInfo.sourceText = fileRef.text;      // Extract source text snippet
                      citationInfo.sourceType = "file";            // Mark as file source
                      citationInfo.fileId = fileRef.fileId;        // Store file ID for reference
                      citationInfo.page = fileRef.page;            // Store page number if available
                      break;
                  }
              }
          }
          
          // Search through web references to find matching citation
          if (references?.web) {
              for (const webRef of references.web) {
                  // Match citation ID with the 'url' field in web references
                  if (webRef.url === identifier) {
                      citationInfo.sourceText = webRef.text;       // Extract source text snippet
                      citationInfo.sourceType = "web";            // Mark as web source
                      citationInfo.url = webRef.url;              // Store URL for reference
                      citationInfo.title = webRef.title;          // Store page title
                      break;
                  }
              }
          }
          
          citations.push(citationInfo);
      }
      
      return citations;
  }

  // Extract citations with their source text
  // This processes the response and creates a structured list of citations with their source material
  const citations = extractCitationsWithSources(response.answer, response.references);

  // Display citations with source material
  // Loop through each citation and print its details along with the source text
  citations.forEach(citation => {
      console.log(`Citation: [${citation.displayText}](${citation.identifier})`);
      console.log(`Source type: ${citation.sourceType}`);
      console.log(`Source text: ${citation.sourceText}`);
      
      // Show additional metadata based on source type
      if (citation.sourceType === 'file') {
          console.log(`File ID: ${citation.fileId}, Page: ${citation.page}`);
      } else if (citation.sourceType === 'web') {
          console.log(`URL: ${citation.url}, Title: ${citation.title}`);
      }
      
      console.log("-".repeat(50));  // Separator between citations
  });
  ```
</CodeGroup>

## Response format

Knowledge Graph responses include a `references` object with `files` and `web` arrays. The `files` array contains file reference objects for file-based sources, and the `web` array contains web reference objects for web-based sources.

### File sources

File sources appear in the `references.files` array.

| Field    | Type      | Description                                                                                  |
| -------- | --------- | -------------------------------------------------------------------------------------------- |
| `text`   | `string`  | The actual text snippet from the source document that supports the response                  |
| `fileId` | `string`  | Unique identifier for the source file                                                        |
| `score`  | `number`  | Internal score used during the retrieval process for ranking and selecting relevant snippets |
| `page`   | `integer` | Page number where the snippet was found in the source document                               |
| `cite`   | `string`  | Unique identifier used in inline citations within the response text                          |

### Web sources

Web sources appear in the `references.web` array.

| Field   | Type     | Description                                                                                  |
| ------- | -------- | -------------------------------------------------------------------------------------------- |
| `text`  | `string` | The exact text snippet from the web source that was used to support the response             |
| `url`   | `string` | The URL of the web page where this content was found                                         |
| `title` | `string` | The title of the web page where this content was found                                       |
| `score` | `number` | Internal score used during the retrieval process for ranking and selecting relevant snippets |

## Streaming responses

When using streaming responses with Knowledge Graph tools, the `references` object containing sources and citations appears in the last chunk of the stream. This means:

* **Content chunks**: The response text with inline citations is streamed progressively
* **Final chunk**: Contains the graph data with the complete `references` object
* **Citation processing**: You need to collect all chunks and process the final one to access source text

### Stream responses with SDKs

<CodeGroup>
  ```python Python theme={null}
  from writerai import Writer

  # Initialize the Writer client
  client = Writer()

  # Configure Knowledge Graph tool with inline citations
  tools = [{
      "type": "graph",
      "function": {
          "description": "Search company knowledge base",
          "graph_ids": ["<GRAPH_ID>"],
          "subqueries": True,
          "query_config": {
              "inline_citations": True
          }
      }
  }]

  messages = [{'role': 'user', 'content': 'What are the key features of our product?'}]

  # Stream the response
  stream = client.chat.chat(
      model="palmyra-x5",
      messages=messages,
      tools=tools,
      tool_choice="auto",
      stream=True
  )

  # Collect streaming content and references
  references = None

  for chunk in stream:
      if chunk.choices[0].delta.content is not None:
          # Stream content progressively
          content = chunk.choices[0].delta.content
          print(content, end='', flush=True)
      
      # Check for graph data in the message
      if hasattr(chunk.choices[0], 'message') and chunk.choices[0].message:
          if hasattr(chunk.choices[0].message, 'graph_data') and chunk.choices[0].message.graph_data:
              # References are in the graph_data.references object
              references = chunk.choices[0].message.graph_data.references

  print("\nFile references:", references.files)
  print("\nWeb references:", references.web)
  ```

  ```javascript JavaScript theme={null}
  import { Writer } from 'writer-sdk';

  // Initialize the Writer client
  const client = new Writer();

  // Configure Knowledge Graph tool with inline citations
  const tools = [{
      type: "graph",
      function: {
          description: "Search company knowledge base",
          graph_ids: ["<GRAPH_ID>"],
          subqueries: true,
          query_config: {
              inline_citations: true
          }
      }
  }];

  const messages = [{ role: "user", content: "What are the key features of our product?" }];

  // Stream the response
  const stream = await client.chat.chat({
      model: "palmyra-x5",
      messages: messages,
      tools: tools,
      tool_choice: "auto",
      stream: true
  });

  // Collect streaming content and references
  let references = null;

  for await (const chunk of stream) {
      if (chunk.choices[0].delta.content) {
          // Stream content progressively
          const content = chunk.choices[0].delta.content;
          process.stdout.write(content);
      }
      
      // Check for graph data in the message
      if (chunk.choices[0].message && chunk.choices[0].message.graph_data) {
          // References are in the graph_data.references object
          references = chunk.choices[0].message.graph_data.references;
      }
  }

  console.log(`\nFile references: ${references.files}`);
  console.log(`\nWeb references: ${references.web}`);
  ```
</CodeGroup>

## Next steps

* Learn about [Knowledge Graph query configuration](/home/knowledge-graph-query-config) for tuning search parameters
* Explore [Knowledge Graph tools](/home/kg-chat) for chat completions
* Check out [direct Knowledge Graph queries](/home/kg-query) for programmatic access
