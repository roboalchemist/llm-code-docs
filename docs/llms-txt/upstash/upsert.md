# Source: https://upstash.com/docs/vector/sdks/ts/commands/upsert.md

# Source: https://upstash.com/docs/vector/sdks/py/example_calls/upsert.md

# Source: https://upstash.com/docs/vector/api/endpoints/upsert.md

# Source: https://upstash.com/docs/search/sdks/ts/commands/upsert.md

# Source: https://upstash.com/docs/search/sdks/py/commands/upsert.md

# Source: https://upstash.com/docs/vector/sdks/ts/commands/upsert.md

# Source: https://upstash.com/docs/vector/sdks/py/example_calls/upsert.md

# Source: https://upstash.com/docs/vector/api/endpoints/upsert.md

# Source: https://upstash.com/docs/search/sdks/ts/commands/upsert.md

# Source: https://upstash.com/docs/search/sdks/py/commands/upsert.md

# Source: https://upstash.com/docs/vector/sdks/ts/commands/upsert.md

# Source: https://upstash.com/docs/vector/sdks/py/example_calls/upsert.md

# Source: https://upstash.com/docs/vector/api/endpoints/upsert.md

# Source: https://upstash.com/docs/search/sdks/ts/commands/upsert.md

# Source: https://upstash.com/docs/search/sdks/py/commands/upsert.md

# Source: https://upstash.com/docs/qstash/api/queues/upsert.md

# Source: https://upstash.com/docs/vector/sdks/ts/commands/upsert.md

# Source: https://upstash.com/docs/vector/sdks/py/example_calls/upsert.md

# Source: https://upstash.com/docs/vector/api/endpoints/upsert.md

# Source: https://upstash.com/docs/search/sdks/ts/commands/upsert.md

# Source: https://upstash.com/docs/search/sdks/py/commands/upsert.md

# Source: https://upstash.com/docs/qstash/api/queues/upsert.md

# Source: https://upstash.com/docs/vector/sdks/ts/commands/upsert.md

# Source: https://upstash.com/docs/vector/sdks/py/example_calls/upsert.md

# Source: https://upstash.com/docs/vector/api/endpoints/upsert.md

# Source: https://upstash.com/docs/search/sdks/ts/commands/upsert.md

# Source: https://upstash.com/docs/search/sdks/py/commands/upsert.md

# Source: https://upstash.com/docs/qstash/api/queues/upsert.md

# Source: https://upstash.com/docs/vector/sdks/ts/commands/upsert.md

# Upsert

Used to add new vectors or update an existing vector.

<Note>
  You can only upsert vectors with same dimension count(size) as your index.
</Note>

## Arguments

There are two ways to use the upsert method. You can either create the vectors on your own and pass them directly.
Or you can pass the data and create the embeddings using Upstash Embedding. The possible payloads are:

<ResponseField name="VectorPayload" type="Vector | Vector[]" required>
  <Expandable>
    <ResponseField name="id" type="string | number" required>
      The ID of the vector
    </ResponseField>

    <ResponseField name="vector" type="number[]" required>
      The vectors to add to the store
    </ResponseField>

    <ResponseField name="metadata" type="Record<string, unknown>">
      Metadata of the vector
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="Namespace" type="{ namespace?: string }">
  Namespace to upsert to. If not set, default namespace is used.
</ResponseField>

**OR**

<ResponseField name="DataPayload" type="Data | Data[]" required>
  <Expandable>
    <ResponseField name="id" type="string | number" required>
      The ID of the vector
    </ResponseField>

    <ResponseField name="data" type="string" required>
      The vectors to add to the store
    </ResponseField>

    <ResponseField name="metadata" type="Record<string, unknown>">
      Metadata of the vector
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="Namespace" type="{ namespace?: string }">
  Namespace to upsert to. If not set, default namespace is used.
</ResponseField>

## Response

<ResponseField type="str" required>
  `'Success'` on successful operation.
</ResponseField>

<RequestExample>
  ```typescript Single Vector theme={"system"}
  await index.upsert({
    id: "1234",
    vector: [0.1, 0.2, 0.3, 0.4, 0.5],
    metadata: {
      title: "Lord of The Rings",
      genre: "drama",
      category: "classic",
    },
  });
  ```

  ```typescript Multiple Vectors theme={"system"}
  await index.upsert([
    {
      id: "6789",
      vector: [0.6, 0.7, 0.8, 0.9, 0.9],
    },
    {
      id: "1234",
      vector: [0.1, 0.2, 0.3, 0.4, 0.5],
      metadata: {
        title: "Lord of The Rings",
        genre: "drama",
        category: "classic",
      },
    },
  ]);
  ```

  ```typescript Namespace theme={"system"}
  await index.upsert([
    {
      id: "6789",
      vector: [0.6, 0.7, 0.8, 0.9, 0.9],
    },
  ], { namespace: "my-namespace" });
  ```

  ```typescript Update Vector theme={"system"}
  await index.upsert({
  	id: "1234",
  	vector: [0.1, 0.2, 0.3, 0.4, 0.5]
  	metadata: {
  		title: "Redis"
  	}
  })

  await index.update({
  	id: "1234",
  	metadata: {
  		title: "QStash"
  	}
  })
  ```

  ```typescript Single Data theme={"system"}
  await index.upsert({
    id: "1234",
    data: "'The Lord of the Rings' follows Frodo Baggins and his allies on a quest to destroy a powerful ring and save Middle-earth from the dark lord Sauron.",
    metadata: {
      title: "Lord of The Rings",
      genre: "drama",
      category: "classic",
    },
  });
  ```

  ```typescript Multiple Data theme={"system"}
  await index.upsert([
    {
      id: "6789",
      data: "'Harry Potter' follows the journey of a young wizard, Harry Potter, as he attends Hogwarts School of Witchcraft and Wizardry, forms deep friendships, and confronts the dark wizard Voldemort, who seeks immortality and domination over the magical world.",
    },
    {
      id: "1234",
      data: "'The Lord of the Rings' follows Frodo Baggins and his allies on a quest to destroy a powerful ring and save Middle-earth from the dark lord Sauron.",
      metadata: {
        title: "Lord of The Rings",
        genre: "drama",
        category: "classic",
      },
    },
  ]);
  ```

  ```typescript Update data theme={"system"}
  await index.upsert({
  	id: "1234",
  	data: "Upstash product"
  	metadata: {
  		title: "Redis"
  	}
  })

  await index.upsert({
  	id: "1234",
  	metadata: {
  		title: "QStash"
  	}
  })
  ```
</RequestExample>
