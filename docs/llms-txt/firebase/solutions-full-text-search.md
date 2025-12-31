# Source: https://firebase.google.com/docs/data-connect/solutions-full-text-search.md.txt

<br />

Firebase Data Connectsupports full-text search, powered by PostgreSQL. Full-text search lets you quickly and efficiently locate information within large datasets by searching for keywords and phrases across multiple columns at once.

You can add full-text search to your service. First add the`@searchable`directive to the`String`in your schema that you want to search over. For example:  

    type Movie
      @table {

      # The fields you want to search over
      title: String! @searchable
      genre: String @searchable
      description: String @searchable
      tags: [String]

      # Some other fields that we won't search over
      rating: Float
      imageUrl: String!
      releaseYear: Int
    }

Once you add this directive, you can then perform full-text search by adding the`<pluralType>_search`field to a query. In this case, it'll be`movies_search`:  

    query SearchMovies($query: String) @auth(level: PUBLIC) {
      movies_search(query: $query) {
        id
        title
        imageUrl
        releaseYear
        genre
        rating
        tags
        description
      }
    }

## Fine-tuning full-text search results

You can fine-tune full-text search results by adding arguments to the`@searchable`directive and`_search`field;

### Shared arguments

You can control search results with many of the same arguments used for basic list fields`<pluralType>`:

- `order`lets you change the order of results. If omitted, results will be ordered by descending relevance.
- `where`lets you add extra filters to search (e.g. search for only movies of a specific genre).
- `limit`makes the query only return the top X results.
- `offset`makes the query skip the first X results.
- `distinct`adds the DISTINCT operator to the generated SQL.

### Language choice

By default, full-text search parses documents in English. You can change this with the language argument on the`@searchable`directive:  

    type Movie
      @table {
      title: String! @searchable(language: "french")
      ...
    }

Specifying the right language will let PostgreSQL perform accurate lexical stemming and help make sure that your search does not miss relevant results. If you are searching over multiple columns, they must all be set to the same language.

|                                                                                               Languages                                                                                               |||
|------------------------------------------------------------------|-------------------------------------------------------------------|------------------------------------------------------------------|
| - simple - arabic - armenian - basque - catalan - danish - dutch | - english - finnish - french - german - greek - hindi - hungarian | - indonesian - irish - italian - lithuanian - nepali - norwegian |

Using`psql`, you can get the full list with the following query.  

    SELECT cfgname FROM pg_ts_config;

### Query format

By default, full-text search uses web semantics for queries (similar to Google search). You can change this behavior with the`queryFormat`argument on the`<pluralType>_search`field.  

    query SearchMovies($query: String) @auth(level: PUBLIC) {
      movies_search(query: $query, queryFormat: PHRASE) {
        ...
      }
    }

There are four options for query format:

- **QUERY**gives familiar semantics to web search engines (e.g. quoted strings, AND and OR). It is the default.
- **PLAIN**matches all of the words, but not necessarily together ("brown dog" will match " the brown and white dog" or "the white and brown dog").
- **PHRASE**matches an exact phrase ( "brown dog" will match "the white and brown dog", but won't match "brown and white dog").
- **ADVANCED** lets you create complex queries using[the full set of tsquery operators](https://www.cockroachlabs.com/docs/stable/tsquery).

### Relevance threshold

Setting a relevance threshold means that your search will only return results above a certain relevance value. In many cases, you won't need to set this - any result that has a relevance greater than 0 will be a relevant result.

However, if you find that your search is returning results that don't feel relevant, relevance threshold can filter them out for you.

To figure out an appropriate value for relevance threshold, you should perform a few test searches and look at the`_metadata.relevance`:  

    query SearchMovies($query: String) @auth(level: PUBLIC) {
      movies_search(query: $query) {
        id
        title
        _metadata {
          relevance
        }
        ...
      }
    }

Choose a threshold that omits results that you feel are irrelevant. To do so:  

    query SearchMovies($query: String) @auth(level: PUBLIC) {
      movies_search(query: $query, relevanceThreshold: 0.05) {
        id
        title
        ...
      }
    }

| **Note:** When you change other search configuration (particularly`rankFunction`or`normalization`), you will likely need to retune this threshold.

## Choosing between full-text search, vector similarity search, and string pattern filters

Data Connectoffers a few different ways to search over your database.

Use this table to help you choose the right one for your use case.

|                                     Full-text search                                      |                                   Vector similarity search                                    |                                      String pattern filters                                      |
|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Good for implementing general search functionality                                        | Good for finding semantically similar rows (for example, recommendations or 'More like this') | Good for exact text matches or regular expression searches                                       |
| Performs lexical stemming, which helps match different forms or tenses of the same word   | Requires Vertex AI                                                                            | Uses the least memory and disk space, since it does not require any indexes or generated columns |
| Can be performed over multiple columns in a table                                         | Only works for a single column at a time                                                      | Can be performed over multiple columns in a table by using OR filters                            |
| Performant over larger documents                                                          | Performant over large documents                                                               | Less performant when searching larger documents                                                  |
| Adds memory and storage overhead to store a generated column and an index for each search |                                                                                               |                                                                                                  |