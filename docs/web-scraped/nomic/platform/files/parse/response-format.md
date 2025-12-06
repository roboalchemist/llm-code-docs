# Nomic Documentation

Source: https://docs.nomic.ai/platform/files/parse/response-format/

Learn about the response format for our parsing endpoint.

The parsing response format is optimized for flexibility with retrieval augmented generation and structured data extraction.

## Attribute Breakdown​

### task_id​

```
task_id
```

string

Unique identifier of the parse task.

### duration​

```
duration
```

number

The time it took for the parse task to complete, in seconds.

### result​

```
result
```

object

The object containing the parsed result.

Child attributes:

- chunks array - List of parsed document chunks.
```
chunks
```

## Code Snippet Example​

### Full Response Example​

```
{  "task_id": "4df647cd-acc5-42af-97e2-d917a211f4be",  "duration": 5.31453,  "result": {    "chunks": [      {        "content": "Detailed content for full LLM usage.",        "embed": "Summarized content optimized for embeddings.",        "blocks": [          {            "type": "Section Header",            "bbox": {              "left": 0.1,              "top": 0.05,              "width": 0.8,              "height": 0.1,              "page": 1,            },            "content": "Text content",          } ...        ] ...      } ...    ]  }}
```

## Chunk Structure​

Each chunk in the chunks array contains:

```
chunks
```

- content - The actual text content of the chunk
```
content
```

- embed - The embedding-tuned text content of the chunk
```
embed
```

- blocks - The blocks that make up a given chunk
```
blocks
```

## Next Steps​

After understanding the response format, you can:

- Generate embeddings from the structured content
- Create semantic search applications with the chunked data
- Build RAG (Retrieval Augmented Generation) systems using the optimized format
- Attribute Breakdowntask_iddurationresult
- task_id
```
task_id
```

- duration
```
duration
```

- result
```
result
```

- Code Snippet ExampleFull Response Example
- Full Response Example
- Chunk Structure
- Next Steps
