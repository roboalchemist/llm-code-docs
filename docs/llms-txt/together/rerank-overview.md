# Source: https://docs.together.ai/docs/rerank-overview.md

# Rerank

> Learn how to improve the relevance of your search and RAG systems with reranking.

## What is a reranker?

A reranker is a specialized model that improves search relevancy by reassessing and reordering a set of retrieved documents based on their relevance to a given query. It takes a query and a set of text inputs (called 'documents'), and returns a relevancy score for each document relative to the given query. This process helps filter and prioritize the most pertinent information, enhancing the quality of search results.

In Retrieval Augmented Generation (RAG) pipelines, the reranking step sits between the initial retrieval step and the final generation phase. It acts as a quality filter, refining the selection of documents that will be used as context for language models. By ensuring that only the most relevant information is passed to the generation phase, rerankers play a crucial role in improving the accuracy of generated responses while potentially reducing processing costs.

## How does Together's Rerank API work?

Together's serverless Rerank API allows you to seamlessly integrate supported rerank models into your enterprise applications. It takes in a `query` and a number of `documents`, and outputs a relevancy score and ordering index for each document. It can also filter its response to the n most relevant documents.

Together's Rerank API is also compatible with Cohere Rerank, making it easy to try out our reranker models on your existing applications.

Key features of Together's Rerank API include:

* Flagship support for [LlamaRank](/docs/together-and-llamarank), Salesforce’s reranker model
* Support for JSON and tabular data
* Long 8K context per document
* Low latency for fast search queries
* Full compatibility with Cohere's Rerank API

[Get started building with Together Rerank today →](/docs/together-and-llamarank)

## Cohere Rerank compatibility

The Together Rerank endpoint is compatible with Cohere Rerank, making it easy to test out models like [LlamaRank](/docs/together-and-llamarank) for your existing applications. Simply switch it out by updating the `URL`, `API key` and `model`.

<CodeGroup>
  ```py Python theme={null}
  import cohere

  co = cohere.Client(
      base_url="https://api.together.xyz/v1",
      api_key=TOGETHER_API_KEY,
  )
  docs = [
      "Carson City is the capital city of the American state of Nevada.",
      "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
      "Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.",
      "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
      "Capital punishment (the death penalty) has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
  ]
  response = co.rerank(
      model="Salesforce/Llama-Rank-V1",
      query="What is the capital of the United States?",
      documents=docs,
      top_n=3,
  )
  ```

  ```ts TypeScript theme={null}
  import { CohereClient } from "cohere-ai";

  const cohere = new CohereClient({
    baseUrl: "https://api.together.xyz/",
    token: process.env.TOGETHER_API_KEY,
  });

  const docs = [
    "Carson City is the capital city of the American state of Nevada.",
    "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
    "Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.",
    "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
    "Capital punishment (the death penalty) has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
  ];

  const response = await cohere.rerank({
    model: "Salesforce/Llama-Rank-V1",
    query: "What is the capital of the United States?",
    documents: docs,
    topN: 3,
  });
  ```
</CodeGroup>

## Get Started

### Example with text

In the example below, we use the [Rerank API endpoint](/reference/rerank) to index the list of `documents` from most to least relevant to the query `What animals can I find near Peru?`.

<CodeGroup>
  ```py Python theme={null}
  from together import Together

  client = Together()

  query = "What animals can I find near Peru?"

  documents = [
      "The giant panda (Ailuropoda melanoleuca), also known as the panda bear or simply panda, is a bear species endemic to China.",
      "The llama is a domesticated South American camelid, widely used as a meat and pack animal by Andean cultures since the pre-Columbian era.",
      "The wild Bactrian camel (Camelus ferus) is an endangered species of camel endemic to Northwest China and southwestern Mongolia.",
      "The guanaco is a camelid native to South America, closely related to the llama. Guanacos are one of two wild South American camelids; the other species is the vicuña, which lives at higher elevations.",
  ]

  response = client.rerank.create(
      model="Salesforce/Llama-Rank-V1",
      query=query,
      documents=documents,
      top_n=2,
  )

  for result in response.results:
      print(f"Document Index: {result.index}")
      print(f"Document: {documents[result.index]}")
      print(f"Relevance Score: {result.relevance_score}")
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const documents = [
    "The giant panda (Ailuropoda melanoleuca), also known as the panda bear or simply panda, is a bear species endemic to China.",
    "The llama is a domesticated South American camelid, widely used as a meat and pack animal by Andean cultures since the pre-Columbian era.",
    "The wild Bactrian camel (Camelus ferus) is an endangered species of camel endemic to Northwest China and southwestern Mongolia.",
    "The guanaco is a camelid native to South America, closely related to the llama. Guanacos are one of two wild South American camelids; the other species is the vicuña, which lives at higher elevations.",
  ];

  const response = await client.rerank.create({
    model: "Salesforce/Llama-Rank-V1",
    query: "What animals can I find near Peru?",
    documents,
    top_n: 2,
  });

  for (const result of response.results) {
    console.log(`Document index: ${result.index}`);
    console.log(`Document: ${documents[result.index]}`);
    console.log(`Relevance score: ${result.relevance_score}`);
  }
  ```

  ```sh cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/rerank" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "Salesforce/Llama-Rank-v1",
         "query": "What animals can I find near Peru?",
         "documents": [{
            "title": "Llama",
            "text": "The llama is a domesticated South American camelid, widely used as a meat and pack animal by Andean cultures since the pre-Columbian era."
          },
          {
            "title": "Panda",
            "text": "The giant panda (Ailuropoda melanoleuca), also known as the panda bear or simply panda, is a bear species endemic to China."
          },
          {
            "title": "Guanaco",
            "text": "The guanaco is a camelid native to South America, closely related to the llama. Guanacos are one of two wild South American camelids; the other species is the vicuña, which lives at higher elevations."
          },
          {
            "title": "Wild Bactrian camel",
            "text": "The wild Bactrian camel (Camelus ferus) is an endangered species of camel endemic to Northwest China and southwestern Mongolia."
          }]
       }'
  ```
</CodeGroup>

### Example with JSON Data

Alternatively, you can pass in a JSON object and specify the fields you’d like to rank over, and the order they should be considered in. If you do not pass in any `rank_fields`, it will default to the text key.

The example below shows passing in some emails, with the query `Which pricing did we get from Oracle?`.

<CodeGroup>
  ```py Python theme={null}
  from together import Together

  client = Together()

  query = "Which pricing did we get from Oracle?"

  documents = [
      {
          "from": "Paul Doe <paul_fake_doe@oracle.com>",
          "to": ["Steve <steve@me.com>", "lisa@example.com"],
          "date": "2024-03-27",
          "subject": "Follow-up",
          "text": "We are happy to give you the following pricing for your project.",
      },
      {
          "from": "John McGill <john_fake_mcgill@microsoft.com>",
          "to": ["Steve <steve@me.com>"],
          "date": "2024-03-28",
          "subject": "Missing Information",
          "text": "Sorry, but here is the pricing you asked for for the newest line of your models.",
      },
      {
          "from": "John McGill <john_fake_mcgill@microsoft.com>",
          "to": ["Steve <steve@me.com>"],
          "date": "2024-02-15",
          "subject": "Commited Pricing Strategy",
          "text": "I know we went back and forth on this during the call but the pricing for now should follow the agreement at hand.",
      },
      {
          "from": "Generic Airline Company<no_reply@generic_airline_email.com>",
          "to": ["Steve <steve@me.com>"],
          "date": "2023-07-25",
          "subject": "Your latest flight travel plans",
          "text": "Thank you for choose to fly Generic Airline Company. Your booking status is confirmed.",
      },
      {
          "from": "Generic SaaS Company<marketing@generic_saas_email.com>",
          "to": ["Steve <steve@me.com>"],
          "date": "2024-01-26",
          "subject": "How to build generative AI applications using Generic Company Name",
          "text": "Hey Steve! Generative AI is growing so quickly and we know you want to build fast!",
      },
      {
          "from": "Paul Doe <paul_fake_doe@oracle.com>",
          "to": ["Steve <steve@me.com>", "lisa@example.com"],
          "date": "2024-04-09",
          "subject": "Price Adjustment",
          "text": "Re: our previous correspondence on 3/27 we'd like to make an amendment on our pricing proposal. We'll have to decrease the expected base price by 5%.",
      },
  ]

  response = client.rerank.create(
      model="Salesforce/Llama-Rank-V1",
      query=query,
      documents=documents,
      return_documents=True,
      rank_fields=["from", "to", "date", "subject", "text"],
  )

  print(response)
  ```

  ```ts TypeScript theme={null}
  import Together from "together-ai";

  const client = new Together();

  const documents = [
    {
      from: "Paul Doe <paul_fake_doe@oracle.com>",
      to: ["Steve <steve@me.com>", "lisa@example.com"],
      date: "2024-03-27",
      subject: "Follow-up",
      text: "We are happy to give you the following pricing for your project.",
    },
    {
      from: "John McGill <john_fake_mcgill@microsoft.com>",
      to: ["Steve <steve@me.com>"],
      date: "2024-03-28",
      subject: "Missing Information",
      text: "Sorry, but here is the pricing you asked for for the newest line of your models.",
    },
    {
      from: "John McGill <john_fake_mcgill@microsoft.com>",
      to: ["Steve <steve@me.com>"],
      date: "2024-02-15",
      subject: "Commited Pricing Strategy",
      text: "I know we went back and forth on this during the call but the pricing for now should follow the agreement at hand.",
    },
    {
      from: "Generic Airline Company<no_reply@generic_airline_email.com>",
      to: ["Steve <steve@me.com>"],
      date: "2023-07-25",
      subject: "Your latest flight travel plans",
      text: "Thank you for choose to fly Generic Airline Company. Your booking status is confirmed.",
    },
    {
      from: "Generic SaaS Company<marketing@generic_saas_email.com>",
      to: ["Steve <steve@me.com>"],
      date: "2024-01-26",
      subject:
        "How to build generative AI applications using Generic Company Name",
      text: "Hey Steve! Generative AI is growing so quickly and we know you want to build fast!",
    },
    {
      from: "Paul Doe <paul_fake_doe@oracle.com>",
      to: ["Steve <steve@me.com>", "lisa@example.com"],
      date: "2024-04-09",
      subject: "Price Adjustment",
      text: "Re: our previous correspondence on 3/27 we'd like to make an amendment on our pricing proposal. We'll have to decrease the expected base price by 5%.",
    },
  ];

  const response = await client.rerank.create({
    model: "Salesforce/Llama-Rank-V1",
    query: "Which pricing did we get from Oracle?",
    documents,
    return_documents: true,
    rank_fields: ["from", "to", "date", "subject", "text"],
  });

  console.log(response);
  ```

  ```sh cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/rerank" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "Salesforce/Llama-Rank-v1",
         "query": "Which pricing did we get from Oracle?",
         "documents": [
           {
             "from": "Paul Doe <paul_fake_doe@oracle.com>",
             "to": ["Steve <steve@me.com>", "lisa@example.com"],
             "date": "2024-03-27",
             "subject": "Follow-up",
             "text": "We are happy to give you the following pricing for your project."
           },
           {
             "from": "John McGill <john_fake_mcgill@microsoft.com>",
             "to": ["Steve <steve@me.com>"],
             "date": "2024-03-28",
             "subject": "Missing Information",
             "text": "Sorry, but here is the pricing you asked for for the newest line of your models."
           },
           {
             "from": "John McGill <john_fake_mcgill@microsoft.com>",
             "to": ["Steve <steve@me.com>"],
             "date": "2024-02-15",
             "subject": "Commited Pricing Strategy",
             "text": "I know we went back and forth on this during the call but the pricing for now should follow the agreement at hand."
           },
           {
             "from": "Generic Airline Company<no_reply@generic_airline_email.com>",
             "to": ["Steve <steve@me.com>"],
             "date": "2023-07-25",
             "subject": "Your latest flight travel plans",
             "text": "Thank you for choose to fly Generic Airline Company. Your booking status is confirmed."
           },
           {
             "from": "Generic SaaS Company<marketing@generic_saas_email.com>",
             "to": ["Steve <steve@me.com>"],
             "date": "2024-01-26",
             "subject": "How to build generative AI applications using Generic Company Name",
             "text": "Hey Steve! Generative AI is growing so quickly and we know you want to build fast!"
           },
           {
             "from": "Paul Doe <paul_fake_doe@oracle.com>",
             "to": ["Steve <steve@me.com>", "lisa@example.com"],
             "date": "2024-04-09",
             "subject": "Price Adjustment",
             "text": "Re: our previous correspondence on 3/27 we'\''d like to make an amendment on our pricing proposal. We'\''ll have to decrease the expected base price by 5%."
           }
         ],
         "return_documents": true,
         "rank_fields": ["from", "to", "date", "subject", "text"]
       }'
  ```
</CodeGroup>

In the `documents` parameter, we are passing in a list of objects which have the key values: `['from', 'to', 'date', 'subject', 'text']`. As part of the Rerank call, under `rank_fields` we are specifying which keys to rank over, as well as the order in which the key value pairs should be considered.

When the model returns rankings, we'll also receive each email in the response because the `return_documents` option is set to true.

```json JSON theme={null}
{
  "model": "Salesforce/Llama-Rank-v1",
  "choices": [
    {
      "index": 0,
      "document": {
        "text": "{\"from\":\"Paul Doe <paul_fake_doe@oracle.com>\",\"to\":[\"Steve <steve@me.com>\",\"lisa@example.com\"],\"date\":\"2024-03-27\",\"subject\":\"Follow-up\",\"text\":\"We are happy to give you the following pricing for your project.\"}"
      },
      "relevance_score": 0.606349439153678
    },
    {
      "index": 5,
      "document": {
        "text": "{\"from\":\"Paul Doe <paul_fake_doe@oracle.com>\",\"to\":[\"Steve <steve@me.com>\",\"lisa@example.com\"],\"date\":\"2024-04-09\",\"subject\":\"Price Adjustment\",\"text\":\"Re: our previous correspondence on 3/27 we'd like to make an amendment on our pricing proposal. We'll have to decrease the expected base price by 5%.\"}"
      },
      "relevance_score": 0.5059948716207964
    },
    {
      "index": 1,
      "document": {
        "text": "{\"from\":\"John McGill <john_fake_mcgill@microsoft.com>\",\"to\":[\"Steve <steve@me.com>\"],\"date\":\"2024-03-28\",\"subject\":\"Missing Information\",\"text\":\"Sorry, but here is the pricing you asked for for the newest line of your models.\"}"
      },
      "relevance_score": 0.2271930688841643
    },
    {
      "index": 2,
      "document": {
        "text": "{\"from\":\"John McGill <john_fake_mcgill@microsoft.com>\",\"to\":[\"Steve <steve@me.com>\"],\"date\":\"2024-02-15\",\"subject\":\"Commited Pricing Strategy\",\"text\":\"I know we went back and forth on this during the call but the pricing for now should follow the agreement at hand.\"}"
      },
      "relevance_score": 0.2229844295907072
    },
    {
      "index": 4,
      "document": {
        "text": "{\"from\":\"Generic SaaS Company<marketing@generic_saas_email.com>\",\"to\":[\"Steve <steve@me.com>\"],\"date\":\"2024-01-26\",\"subject\":\"How to build generative AI applications using Generic Company Name\",\"text\":\"Hey Steve! Generative AI is growing so quickly and we know you want to build fast!\"}"
      },
      "relevance_score": 0.0021253144747196517
    },
    {
      "index": 3,
      "document": {
        "text": "{\"from\":\"Generic Airline Company<no_reply@generic_airline_email.com>\",\"to\":[\"Steve <steve@me.com>\"],\"date\":\"2023-07-25\",\"subject\":\"Your latest flight travel plans\",\"text\":\"Thank you for choose to fly Generic Airline Company. Your booking status is confirmed.\"}"
      },
      "relevance_score": 0.0010322494264659
    }
  ]
}
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt