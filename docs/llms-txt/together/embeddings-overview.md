# Source: https://docs.together.ai/docs/embeddings-overview.md

# Embeddings

> Learn how to get an embedding vector for a given text input.

Together's Embeddings API lets you turn some input text (the *input*) into an array of numbers (the *embedding*). The resulting embedding can be compared against other embeddings to determine how closely related the two input strings are.

Embeddings from large datasets can be stored in vector databases for later retrieval or comparison. Common use cases for embeddings are search, classification, and recommendations. They're also used for building Retrieval Augmented Generation (RAG) applications.

## Generating a single embedding

Use `client.embeddings.create` to generate an embedding for some input text, passing in a model name and input string:

<CodeGroup>
  ```py Python theme={null}
  from together import Together

  client = Together()

  response = client.embeddings.create(
      model="BAAI/bge-base-en-v1.5",
      input="Our solar system orbits the Milky Way galaxy at about 515,000 mph",
  )
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const together = new Together();

  const response = await client.embeddings.create({
    model: "BAAI/bge-base-en-v1.5",
    input: "Our solar system orbits the Milky Way galaxy at about 515,000 mph",
  });
  ```

  ```sh cURL theme={null}
  curl -X POST https://api.together.xyz/v1/embeddings \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
           "input": "Our solar system orbits the Milky Way galaxy at about 515,000 mph.",
           "model": "BAAI/bge-base-en-v1.5"
          }'
  ```
</CodeGroup>

The response will be an object that contains the embedding under the `data` key, as well as some metadata:

```json JSON theme={null}
{
  model: 'BAAI/bge-base-en-v1.5',
  object: 'list',
  data: [
    {
      index: 0,
      object: 'embedding',
      embedding: [0.2633975, 0.13856208, ..., 0.04331574],
    },
  ],
};
```

## Generating multiple embeddings

You can also pass an array of input strings to the `input` option:

<CodeGroup>
  ```py Python theme={null}
  from together import Together

  client = Together()

  response = client.embeddings.create(
      model="BAAI/bge-base-en-v1.5",
      input=[
          "Our solar system orbits the Milky Way galaxy at about 515,000 mph",
          "Jupiter's Great Red Spot is a storm that has been raging for at least 350 years.",
      ],
  )
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const response = await client.embeddings.create({
    model: "BAAI/bge-base-en-v1.5",
    input: [
      "Our solar system orbits the Milky Way galaxy at about 515,000 mph",
      "Jupiter's Great Red Spot is a storm that has been raging for at least 350 years.",
    ],
  });
  ```

  ```sh cURL theme={null}
  curl -X POST https://api.together.xyz/v1/embeddings \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
           "model": "BAAI/bge-base-en-v1.5",
           "input": [
              "Our solar system orbits the Milky Way galaxy at about 515,000 mph",
              "Jupiter'\''s Great Red Spot is a storm that has been raging for at least 350 years."
           ]
          }'
  ```
</CodeGroup>

The `response.data` key will contain an array of objects for each input string you provide:

```json JSON theme={null}
{
  model: 'BAAI/bge-base-en-v1.5',
  object: 'list',
  data: [
    {
      index: 0,
      object: 'embedding',
      embedding: [0.2633975, 0.13856208, ..., 0.04331574],
    },
    {
      index: 1,
      object: 'embedding',
      embedding: [-0.14496337, 0.21044481, ..., -0.16187587]
    },
  ],
};
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt