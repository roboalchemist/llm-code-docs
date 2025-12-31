# Source: https://firebase.google.com/docs/data-connect/solutions-vector-similarity-search.md.txt

<br />

Welcome toFirebase Data Connect's vector similarity search --- Firebase's implementation of semantic search that integrates with[Google Vertex AI](https://cloud.google.com/vertex-ai/docs/vector-search/overview).

At the core of this feature are vector embeddings, which are arrays of floating point numbers representing the semantic meaning of text or media. By running a nearest neighbor search using an input vector embedding, you can find all semantically similar content.Data Connectuses PostgreSQL's`pgvector`extension for this capability.

This powerful semantic search can drive use cases like recommendation engines and search engines. It's also a key component in[retrieval-augmented generation](https://developers.google.com/machine-learning/glossary#retrieval-augmented-generation-rag)in generative AI flows. The Vertex AI documentation is a great place to[learn more](https://cloud.google.com/vertex-ai/docs/vector-search/overview).

You can rely onData Connect's built-in support for generating vector embeddings automatically using[Vertex AI's Embeddings API](https://cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings), or use that API to generate them manually.

## Prerequisites

- [Set up Data Connect](https://firebase.google.com/docs/data-connect/quickstart)for your project.

  | **Note:** As you work through the setup flow, be aware thatData Connect's Vertex AI integration is supported only for certain Cloud SQL for PostgreSQL locations. See the[location list](https://firebase.google.com/docs/data-connect/manage-services-and-databases#vertex-ai-limitations).
- Enable[Vertex AI APIs](https://cloud.google.com/vertex-ai/docs/start/cloud-environment#enable_vertexai_apis).

  | **Note:** You don't need to create a separate Google Cloud project or install the Google Cloud CLI.

## Setup

You can choose between a local development flow (if you're a web, Kotlin Android, or iOS developer) or an IDX flow (for web developers). You can use a local database or your productionData Connectproject and its Cloud SQL for PostgreSQL instance for development.
| **Note:** Whether you work locally or with your production project, you are using Vertex AI, and you will incur[Vertex AI usage costs](https://cloud.google.com/vertex-ai/pricing#vectorsearch).

These instructions assume you have created yourData Connectproject[following the quickstart guide](https://firebase.google.com/docs/data-connect/quickstart).

### Integrate with local PostgreSQL

1. Set up a local PostgreSQL instance.
2. [Grant](https://cloud.google.com/iam/docs/grant-role-console)yourself the[Vertex AI user IAM role](https://cloud.google.com/vertex-ai/docs/general/access-control#aiplatform.user).
3. Set up[Google Cloud Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc)in your environment.
4. Install the[`pgvector`extension](https://github.com/pgvector/pgvector)in your local PostgreSQL instance.
5. Enable the extension using`CREATE EXTENSION vector`per the`pgvector`repository instructions.

### Integrate with IDX

1. Set up your IDX workspace using the Data Connect template.
2. [Grant](https://cloud.google.com/iam/docs/grant-role-console)yourself the[Vertex AI user IAM role](https://cloud.google.com/vertex-ai/docs/general/access-control#aiplatform.user).
3. Enable the extension using`CREATE EXTENSION vector`per the`pgvector`repository instructions.

## Design your schema

To perform vector search, add a new field of`Vector`type in your schema. For example, if you want to do a semantic search using movie descriptions, add a field to hold the vector embeddings associated with the movie description. In this schema,`descriptionEmbedding`is added to store vector embeddings for the`description`field.  

    type Movie @table {
     id: ID! @col(name: "movie_id") @default(id: ID! @col(name: "movie_id") @default(expr: "uuidV4()")
     title: String!
     description: String
     descriptionEmbedding: Vector! @col(size:768)
     // ...
    }

| **Note:** Ensure that the vector embedding dimension is provided using the`@col(size: X)`schema directive, since vector embedding search can only compare vectors of the same dimensions. The vector embeddings generated using Vertex AI are of size 768.

## Generate and retrieve embeddings

Data Connectbrings integrated support for vector embeddings with the`_embed`server value. This directsData Connectto generate vector embeddings by internally calling Vertex AI's Embedding APIs. The`_embed`server value can be used in both mutations and queries.
| **Note:** Vector embeddings generated from different model versions are generally considered to be incompatible. Thus, for all operations on a field (queries or mutations), it is the best practice to use vector embeddings generated using the same model. The list of supported Vertex AI models is available in[the documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings#model_versions).

### Mutations

#### Generate and store an embedding throughData Connect

In your vector search app, you'll likely want to request that embeddings be generated as soon as you add records to your database. Here's a`createMovie`mutation adds a movie record to the`Movie`table and also passes a movie description with a specified embedding`model`.  

    mutation createMovie($title: String!, $description: String!) {
      movie_insert(data: {
        title: $title,
        description: $description,
        descriptionEmbedding_embed: {model: "textembedding-gecko@003", text: $description}
      })
    }

In some cases, you may want to update the movie description and embedding.  

    mutation updateDescription($id: String!, $description: String!) {
      movie_update(id: $id, data: {
        description: $description,
        descriptionEmbedding_embed: {model: "textembedding-gecko@003", text: $description}
      })
    }

To call the latter mutation from a client:  

    import { updateMovieDescription } from 'lib/dataconnect-sdk/';

    await updateMovieDescription({ id: movieId, description: description});

    // Use the response

### Queries

Fetch vector embeddings using a query like the following. Note that the`descriptionEmbedding`returned by the query is an array of floats, which is typically not human-readable. Thus,Data Connectgenerated SDKs don't support returning it directly.

You can use returned vector embeddings to do similarity search, as described in the next section.  

    query getMovieDescription($id: String!) @auth(level: PUBLIC) {
     movie(id: $id)
       id
       description
       descriptionEmbedding
    }

## Perform similarity search

Now we can perform similarity search.

For each`Vector`field,Data Connectgenerates a GraphQL function that implements the similarity search. The name of this generated function is`${pluralType}_${vectorFieldName}_similarity`. It supports a few parameters as shown in the following examples and in the[reference list](https://firebase.google.com/docs/data-connect/solutions-vector-similarity-search#parameters-similarity).

You can define a GraphQL function that invokes the similarity search. As mentioned above, the`_embed`server value directsData Connectto generate the vector embeddings using Vertex AI's Embedding APIs, in this case to create embeddings for the search string used for comparison with movie description embeddings.

In this example, the similarity search will return up to 5 movies whose description is semantically closest to the input query. The result set is sorted in the ascending order of the distance - closest to furthest.  

    query searchMovieDescriptionUsingL2Similarity ($query: String!) @auth(level: PUBLIC) {
        movies_descriptionEmbedding_similarity(
          compare_embed: {model: "textembedding-gecko@003", text: $query},
          where: {content: {ne: "No info available for this movie."}}, limit: 5)
          {
            id
            title
            description
          }
      }

### Tune the similarity query

Default values for search parameters like`method`and`within`perform well for most use cases. However, if you notice that your query returns results that are too dissimilar, or is missing results that you want included, try tuning these parameters.

To find an appropriate value for`within`, we can add`_metadata.distance`to the selected fields to see how far from the query vector each result is. Based on the returned`distance`values, we can set the`within`parameter; only results with distance less than the value of`within`will be included:  

    query searchMovieDescriptionUsingL2Similarity ($query: String!) @auth(level: PUBLIC) {
        movies_descriptionEmbedding_similarity(
          compare_embed: {model: "textembedding-gecko@003", text: $query},
          within: 2,
          where: {content: {ne: "No info available for this movie."}}, limit: 5)
          {
            id
            title
            description
            _metadata {
              distance
            }
          }
      }

You can also experiment with different distance functions by setting the`method`parameter.  

    query searchMovieDescriptionUsingL2Similarity ($query: String!) @auth(level: PUBLIC) {
        movies_descriptionEmbedding_similarity(
          compare_embed: {model: "textembedding-gecko@003", text: $query},
          within: .5,
          method: COSINE,
          where: {content: {ne: "No info available for this movie."}}, limit: 5)
          {
            id
            title
            description
            _metadata {
              distance
            }
          }
      }

Note that different methods return very different values for distance: if you've set`within`, you will need to tune that value again after changing`method`.

### Call the similarity query

To call a similarity search from client code:  

    import { searchMovieDescriptionUsingL2similarity} from 'lib/dataconnect-sdk';

    const response = await searchMovieDescriptionUsingL2similarity({ query });

    // Use the response

## Use custom embeddings

Data Connectalso lets you work with embeddings directly as`Vector`s rather than using the`_embed`server value to generate them.

### Store a custom embedding

Using the Vertex Embeddings API, specify a matching model and request embedding results of the correct dimension.

Then, cast the returned array of floats to a`Vector`to pass to the update operation for storage.  

    mutation updateDescription($id: String!, $description: String!, $descriptionEmbedding: Vector!) {
      movie_update(id: $id, data: {
        // title, genre...
        description: $description,
        descriptionEmbedding: $descriptionEmbedding
      })
    }

### Perform similarity search using custom embeddings

Carry out the same operation to retrieve embeddings for search terms and cast them to`Vectors`.

Then, call the`_similarity`query to perform each search.  

    query searchMovieDescriptionUsingL2Similarity($compare: Vector!, $within: Float, $excludesContent: String, $limit: Int) @auth(level: PUBLIC) {
        movies_descriptionEmbedding_similarity(
          compare: $compare,
          method: L2,
          within: $within,
          where: {content: {ne: $excludesContent}}, limit: $limit)
          {
            id
            title
            description
          }
      }

## Deploy to production

### Deploy your schema and connector

The last step in a typicalData Connectiteration is to deploy your assets to production.

When deploying your schema containing`Vector`types to CloudSQL using the`firebase deploy`command, theFirebaseCLI takes the necessary steps to enable Vertex AI-based embedding generation on your CloudSQL instance.  

    firebase deploy --only dataconnect

if you wish to enable embedding support in your CloudSQL instance manually, or encounter a CLI error, follow[these instructions](https://cloud.google.com/sql/docs/postgres/integrate-cloud-sql-with-vertex-ai).

## Vector search syntax

### Schema extensions

Data Connect's`Vector`data type maps to PostgreSQL's`vector`type as defined by the[`pgvector`extension](https://github.com/pgvector/pgvector). pgvector's`vector`type is stored as an array of single precision floating point numbers in PostgreSQL.

InData Connect, the`Vector`type is represented as an array of JSON numbers. Inputs are coerced into an array of`float32`values. If coercion fails, an error is raised.
| **Note:** JavaScript numerics are compatible with float coercion.

Use the size parameter of the`@col`directive to set the dimensions of the vector.  

    type Question @table {
        text: String!
        category: String!
        textEmbedding: Vector! @col(size: 768)
    }

`size`is only supported for`Vector`types.`Vector`operations, such as similarity-search, necessitate that all the`Vector`s have the same number of dimensions.  

    directive @col(
      # ... existing args
      """
      Defines a fixed column size for certain scalar types.

      - For Vector, size is required.
      - For all other types, size is currently unsupported and hence supplying it will result in a schema error.
      """
      size: Int
    ) on FIELD_DEFINITION

### `_embed`server value for queries and mutations

    _embed

This server value directs theData Connectservice to generate and store embeddings using[Vertex AI's Embedding APIs](https://cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings). This server value can be used on both queries and mutations.

### Parameters For similarity search

    method: COSINE|INNER_PRODUCT|L2

The distance function used to search for nearby neighbors. Currently-supported algorithms are a subset of[pgvector search algorithms](https://github.com/pgvector/pgvector?tab=readme-ov-file#vector-functions).  

    within: float

A constraint on the distance within which the nearest neighbor search is performed.  

    where: FDC filter condition

See the[schemas, queries and mutations guide](https://firebase.google.com/docs/data-connect/schemas-queries-mutations).  

    limit: int

The number of results to return.