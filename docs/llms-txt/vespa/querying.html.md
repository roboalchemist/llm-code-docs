# Source: https://docs.vespa.ai/en/basics/querying.html.md

# Querying

 

An introduction to querying with Vespa.

## Queries

Queries in Vespa are expressed as a YQL string: A query language identical to SQL for structured data, with additions for vector and full-text search, for example:

```
select * from mySchema where myTextField contains 'someWord' and myNumber > 10.0
```

You can also search multiple fields with one query item (like "contains"), by defining[fieldset](../reference/schemas/schemas.html#fieldset) in the schema.

Any nested combination of and/or and so on is supported, see the full syntax in the[query language reference](../reference/querying/yql.html).

## Query requests

Queries are sent as HTTP requests, to the endpoint of a container cluster having \<search\> in services.xml. The YQL query is sent as the `yql` parameter (HTTP Encoded):

```
endpoint-url/search/?yql=select+%2A+from+sources+%2A+where+true
```

The Vespa CLI can do this for you:

```
vespa query "select * from sources * where true"
```

You can add the `-v` option to see the HTTP request that this becomes.

You can also send the query parameters[as a JSON payload](../querying/query-api.html#http) instead of as request parameters:

```
$ curl -H "Content-Type: application/json" \
--data '{"yql" : "select * from sources * where true"}' \
endpoint-url/search/
```

## Query request parameters

In addition to the YQL parameter, you can send other query request parameters to supply data such as user/llm query text, vectors, and parameters controlling the query execution. These are added to HTTP requests in the obvious way, and passed to Vespa CLI by adding multiple arguments:

```
vespa query -v "select * from sources * where true" "timeout=100ms"
```

To see all the parameters accepted, see the [query API reference](../reference/api/query.html).

You may end up wanting to set many query parameters in your queries. Instead of passing them in the request, you can create a query profile in the application package containing all the parameters and just specify the profile in the request, see [query profiles](../querying/query-profiles.html).

## Querying with text

You often want to send text directly from users or language models to Vespa to retrieve/rank by full-text match. Such text can be inserted into a YQL query using the `userInput` parameter. This will process the text and (by default) search it using the [WeakAnd](../ranking/wand.html#weakand) text search operator.

You can pass the text directly, or refer to a separate request parameter (using `@parameter`):

```
$ vespa query "select * from sources * where myNumber > 10.0 and userInput(@query)" \
  "query=Some text, from a user/llm"
```

You can set options controlling how the user input is to be parsed and executed, see the [userInput reference documentation](../reference/querying/yql.html#userinput).

## Querying with vectors

Querying by vectors is done using the nearestNeighbor YQL operator, which takes a document and query vector:

```
$ vespa query 'select * from sources * where {targetHits: 10}nearestNeighbor(my_vector_field, my_query_vector)' \
  ranking=my_rank_profile \
  'input.query(my_query_vector)'='[1,2,3]'
```

Read more in [nearest neighbor search](../querying/nearest-neighbor-search).

You can combine multiple nearestNeighbor, userInput and other parameters in any way:

```
$ vespa query "select * from sources * where (({targetHits: 10}nearestNeighbor(my_title_embedding, my_query_vector)) \
                                              or ({targetHits: 10}nearestNeighbor(my_body_embeddings, my_query_vector)) \
                                              or userInput(@query) or ({defaultIndex:'ngramFields'}userInput(@query))) \
                                             and range(title, 0.0, 500.0) and category in ('c1', 'c2') \
                                             and ! blacklisted=true" \
  "input.query(my_query_vector)=embed(@query)" \
  "query=Hello, world! "
```
  

#### Next: [Ranking](ranking.html)

 Copyright © 2025 - [Cookie Preferences](#)

### On this page:

- [Queries](#queries)
- [Query requests](#query-requests)
- [Query request parameters](#query-request-parameters)
- [Querying with text](#querying-with-text)
- [Querying with vectors](#querying-with-vectors)

