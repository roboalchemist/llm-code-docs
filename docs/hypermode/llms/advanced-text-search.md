# Source: https://docs.hypermode.com/dgraph/guides/get-started-with-dgraph/advanced-text-search.md

# Get Started with Dgraph - Advanced Text Search

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

**Welcome to the sixth tutorial of getting started with Dgraph.**

In the [previous tutorial](./string-indicies), we learned about building social
graphs in Dgraph, by modeling tweets as an example. We queried the tweets using
the `hash` and `exact` indices, and implemented a keyword-based search to find
your favorite tweets using the `term` index and its functions.

In this tutorial, we'll continue from where we left off and learn about advanced
text search features in Dgraph.

Specifically, we'll focus on two advanced feature:

* Searching for tweets using Full-text search.
* Searching for hashtags using the regular expression search.

The accompanying video of the tutorial will be out shortly, so stay tuned to
[our YouTube channel](https://www.youtube.com/channel/UCghE41LR8nkKFlR3IFTRO4w).

***

Before we dive in, let's do a quick recap of how to model the tweets in Dgraph.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=1d0514c94d40edf52d50aa860ed1f0d3" alt="tweet model" width="526" height="461" data-path="images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=a281d7188019fe6251c3aefa0c0aae11 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=b2f996f4177c8996fe3af07e79d8a401 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=e0e9fd2f64de3883d1828ced7310ad44 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=894439b7a39e25f76c2541f1c2926bfd 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=7bf1424145c7ec3f72c64e2dd4ec8190 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=19ec71f27740dfb573eda0b62c0c4c1d 2500w" data-optimize="true" data-opv="2" />

In the previous tutorial, we took three real tweets as a sample dataset and
stored them in Dgraph using the above graph as a model.

In case you haven't stored the tweets from the
[previous tutorial](./string-indicies) into Dgraph, here's the sample dataset
again.

Copy the mutation below, go to the mutation tab and click Run.

```json
{
  "set": [
    {
      "user_handle": "hackintoshrao",
      "user_name": "Karthic Rao",
      "uid": "_:hackintoshrao",
      "authored": [
        {
          "tweet": "Test tweet for the fifth episode of getting started series with @dgraphlabs. Wait for the video of the fourth one by @francesc the coming Wednesday!\n#GraphDB #GraphQL",
          "tagged_with": [
            {
              "uid": "_:graphql",
              "hashtag": "GraphQL"
            },
            {
              "uid": "_:graphdb",
              "hashtag": "GraphDB"
            }
          ],
          "mentioned": [
            {
              "uid": "_:francesc"
            },
            {
              "uid": "_:dgraphlabs"
            }
          ]
        }
      ]
    },
    {
      "user_handle": "francesc",
      "user_name": "Francesc Campoy",
      "uid": "_:francesc",
      "authored": [
        {
          "tweet": "So many good talks at #graphqlconf, next year I'll make sure to be *at least* in the audience!\nAlso huge thanks to the live tweeting by @dgraphlabs for alleviating the FOMO😊\n#GraphDB ♥️ #GraphQL",
          "tagged_with": [
            {
              "uid": "_:graphql"
            },
            {
              "uid": "_:graphdb"
            },
            {
              "hashtag": "graphqlconf"
            }
          ],
          "mentioned": [
            {
              "uid": "_:dgraphlabs"
            }
          ]
        }
      ]
    },
    {
      "user_handle": "dgraphlabs",
      "user_name": "Dgraph Labs",
      "uid": "_:dgraphlabs",
      "authored": [
        {
          "tweet": "Let's Go and catch @francesc at @Gopherpalooza today, as he scans into Go source code by building its Graph in Dgraph!\nBe there, as he Goes through analyzing Go source code, using a Go program, that stores data in the GraphDB built in Go!\n#golang #GraphDB #Databases #Dgraph ",
          "tagged_with": [
            {
              "hashtag": "golang"
            },
            {
              "uid": "_:graphdb"
            },
            {
              "hashtag": "Databases"
            },
            {
              "hashtag": "Dgraph"
            }
          ],
          "mentioned": [
            {
              "uid": "_:francesc"
            },
            {
              "uid": "_:dgraphlabs"
            }
          ]
        },
        {
          "uid": "_:gopherpalooza",
          "user_handle": "gopherpalooza",
          "user_name": "Gopherpalooza"
        }
      ]
    }
  ]
}
```

*Note: If you're new to Dgraph, and this is the first time you're running a
mutation, we highly recommend reading the
[first tutorial of the series before proceeding.](./introduction)*

Voilà! Now you have a graph with `tweets`, `users`, and `hashtags`. It is ready
for us to explore.

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=6b4c61b34865245af121d67d93d73eaf" alt="tweet graph" width="854" height="431" data-path="images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=402ac155f0cc64215de93c227eafa133 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=82f8fbac5d4e9628ed40698f78075ec3 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=fb9049ab2b58e2e4552e323ef53dee06 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=e869eabc68ab7fba47ef4db444ec8df9 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=e3e0b11a8512bb569bc6ba4417278b3f 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=a0afc339ef35a24112823a2d6b52aa6c 2500w" data-optimize="true" data-opv="2" />

*Note: If you're curious to know how we modeled the tweets in Dgraph, refer to
[the previous tutorial.](./string-indicies)*

Let's start by finding your favorite tweets using the full-text search feature
first.

## Full text search

Before we learn how to use the Full-text search feature, it's important to
understand when to use it.

The length and the number of words in a string predicate value vary based on
what the predicates represent.

Some string predicate values have only a few terms (words) in them. Predicates
representing `names`, `hashtags`, `twitter handle`, `city names` are a few good
examples. These predicates are easy to query using their exact values.

For instance, here is an example query.

*Give me all the tweets where the user name is equal to `John Campbell`*.

You can easily compose queries like these after adding either the `hash` or an
`exact` index to the string predicates.

But, some of the string predicates store sentences. Sometimes even one or more
paragraphs of text data in them. Predicates representing a tweet, a bio, a blog
post, a product description, or a movie review are just some examples. It is
relatively hard to query these predicates.

It is not practical to query such predicates using the `hash` or `exact` string
indices. A keyword-based search using the `term` index is a good starting point
to query such predicates. We used it in our
[previous tutorial](./string-indicies) to find the tweets with an exact match
for keywords like `GraphQL`, `Graphs`, and `Go`.

But, for some of the use cases, just the keyword-based search may not be
sufficient. You might need a more powerful search capability, and that's when
you should consider using Full-text search.

Let's write some queries and understand Dgraph's Full-text search capability in
detail.

To be able to do a Full-text search, you need to first set a `fulltext` index on
the `tweet` predicate.

Creating a `fulltext` index on any string predicate is similar to creating any
other string indices.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-set-index.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=e25440b4ae6250ef830ccbf0274019a0" alt="full text" width="854" height="411" data-path="images/dgraph/guides/get-started-with-dgraph/a-set-index.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-set-index.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=06a4c5b771f418322015699a0c638bcc 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-set-index.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=c933e78619411db32fe47108e61186ca 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-set-index.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=bf2d191f9d2f5e97b6ebf516a208fb75 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-set-index.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=aba8ef0e7aa5f90475d9a416302c95e4 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-set-index.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=2146f7989608427e42cd7692ee790b7a 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-set-index.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=e45f93bdd88859c37b30d1fd0654f6c5 2500w" data-optimize="true" data-opv="2" />

*Note: Refer to the [previous tutorial](./string-indicies) if you're not sure
about creating an index on a string predicate.*

Now, let's do a Full-text search query to find tweets related to the following
topic: `graph data and analyzing it in graphdb`.

You can do so by using either of `alloftext` or `anyoftext` in-built functions.
Both functions take two arguments. The first argument is the predicate to
search. The second argument is the space-separated string values to search for,
and we call these as the `search strings`.

```sh
- alloftext(predicate, "space-separated search strings")
- anyoftext(predicate, "space-separated search strings")
```

We'll look at the difference between these two functions later. For now, let's
use the `alloftext` function.

Go to the query tab, paste the query below, and click Run. Here is our search
string: `graph data and analyze it in graphdb`.

```graphql
{
  search_tweet(func: alloftext(tweet, "graph data and analyze it in graphdb")) {
    tweet
  }
}
```

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-full-text-query-1.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=457fd0d91c6c6067598ab8fa1ce610db" alt="tweet graph" width="854" height="416" data-path="images/dgraph/guides/get-started-with-dgraph/b-full-text-query-1.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-full-text-query-1.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=fadd27fd9e3a398c304b46447fc3e226 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-full-text-query-1.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=0d0b1b7ed6f186440b8037dd021e8550 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-full-text-query-1.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=c0d26281ba861851cd7ce21d57744d21 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-full-text-query-1.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=7e100c2f494d67d7a49d22e00edb6afb 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-full-text-query-1.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=22c0d795fca6d7af285b462246615621 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-full-text-query-1.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=9b91190a48378e40c3b67777fa0a5ce2 2500w" data-optimize="true" data-opv="2" />

Here's the matched tweet, which made it to the result.

```Let's Go and catch @francesc at @Gopherpalooza today, as he scans into Go source code by building its Graph in Dgraph!

Be there, as he Goes through analyzing Go source code, using a Go program, that stores data in the GraphDB built in Go!#golang #GraphDB #Databases #Dgraph pic.twitter.com/sK90DJ6rLs

— Dgraph Labs (@dgraphlabs) November 8, 2019
```

If you observe, you can see some of the words from the search strings are not
present in the matched tweet, but the tweet has still made it to the result.

To be able to use the Full-text search capability effectively, we must
understand how it works.

Let's understand it in detail.

Once you set a `fulltext` index on the tweets, internally, the tweets are
processed, and `fulltext` tokens are generated. These `fulltext` tokens are then
indexed.

The search string also goes through the same processing pipeline, and `fulltext`
tokens generated them too.

Here are the steps to generate the `fulltext` tokens:

* Split the tweets into chunks of words called tokens (tokenizing).
* Convert these tokens to lowercase.
* [Unicode-normalize](http://unicode.org/reports/tr15/#Norm_Forms) the tokens.
* Reduce the tokens to their root form, this is called
  [stemming](https://en.wikipedia.org/wiki/Stemming) (running to run, faster to
  fast and so on).
* Remove the [stop words](https://en.wikipedia.org/wiki/Stop_words).

You would have seen in [the fourth tutorial](./multi-language-strings) that
Dgraph allows you to build multi-lingual apps.

The stemming and stop words removal are not supported for all the languages.
Here is [the link to the docs](/dgraph/dql/functions#full-text-search) that
contains the list of languages and their support for stemming and stop words
removal.

Here is the table with the matched tweet and its search string in the first
column. The second column contains their corresponding `fulltext` tokens
generated by Dgraph.

| Actual text data                                                                                                                                                                                                                                                                     | fulltext tokens generated by Dgraph                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Let's Go and catch @francesc at @Gopherpalooza today, as he scans into Go source code by building its Graph in Dgraph!\nBe there, as he Goes through analyzing Go source code, using a Go program, that stores data in the GraphDB built in Go!\n#golang #GraphDB #Databases #Dgraph | \[analyz build built catch code data databas dgraph francesc go goe golang gopherpalooza graph graphdb program scan sourc store todai us] |
| graph data and analyze it in graphdb                                                                                                                                                                                                                                                 | \[analyz data graph graphdb]                                                                                                              |

From the table above, you can see that the tweets are reduced to an array of
strings or tokens.

Dgraph internally uses [Bleve package](https://github.com/blevesearch/bleve) to
do the stemming.

Here are the `fulltext` tokens generated for our search string: \[`analyz`,
`data`, `graph`, `graphdb`].

As you can see from the table above, all of the `fulltext` tokens generated for
the search string exist in the matched tweet. Hence, the `alloftext` function
returns a positive match for the tweet. It would not have returned a positive
match even if one of the tokens in the search string is missing for the tweet.
But, the `anyoftext` function would've returned a positive match as long as the
tweets and the search string have at least one of the tokens in common.

If you're interested to see Dgraph's `fulltext` tokenizer in action,
[here is the gist](https://gist.github.com/hackintoshrao/0e8d715d8739b12c67a804c7249146a3)
containing the instructions to use it.

Dgraph generates the same `fulltext` tokens even if the words in a search string
is differently ordered. Hence, using the same search string with different order
would not impact the query result.

As you can see, all three queries below are the same for Dgraph.

```graphql
{
  search_tweet(func: alloftext(tweet, "graph analyze and it in graphdb data")) {
    tweet
  }
}
```

```graphql
{
  search_tweet(func: alloftext(tweet, "data and data analyze it graphdb in")) {
    tweet
  }
}
```

```graphql
{
  search_tweet(func: alloftext(tweet, "analyze data and it in graph graphdb")) {
    tweet
  }
}
```

Now, let's move onto the next advanced text search feature of Dgraph: regular
expression based queries.

Let's use them to find all the hashtags containing the following substring:
`graph`.

## Regular expression search

[Regular expressions](https://www.geeksforgeeks.org/write-regular-expressions/)
are powerful ways of expressing search patterns. Dgraph allows you to search for
string predicates based on regular expressions. You need to set the `trigram`
index on the string predicate to be able to perform regex-based queries.

Using regular expression based search, let's match all the hashtags that have
this particular pattern:
`Starts and ends with any characters of indefinite length, but with the substring graph in it`.

Here is the regex expression we can use: `^.*graph.*$`

Check out
[this tutorial](https://www.geeksforgeeks.org/write-regular-expressions/) if
you're not familiar with writing a regular expression.

Let's first find all the hashtags in the database using the `has()` function.

```graphql
{
  hash_tags(func: has(hashtag)) {
    hashtag
  }
}
```

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/has-hashtag.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=5901422274e0c1265a1f6e6315842c95" alt="The hashtags" width="854" height="412" data-path="images/dgraph/guides/get-started-with-dgraph/has-hashtag.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/has-hashtag.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=41d96d343ed91b130a086d42acce2731 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/has-hashtag.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=ffc3814fd93d69b21978c9dca94f3d63 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/has-hashtag.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=441ee4162057a47a5d0730c43388cf34 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/has-hashtag.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=62cfc3bae742232802fe0510e2ad5891 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/has-hashtag.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=ddffea6d6211f628e805bc96f7314c0a 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/has-hashtag.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=33b0c97a2a768e774996ad3240622843 2500w" data-optimize="true" data-opv="2" />

*If you're not familiar with using the `has()` function, refer to
[the first tutorial](./introduction) of the series.*

You can see that we have six hashtags in total, and four of them have the
substring `graph` in them: `Dgraph`, `GraphQL`, `graphqlconf`, `graphDB`.

We should use the built-in function `regexp` to be able to use regular
expressions to search for predicates. This function takes two arguments, the
first is the name of the predicate, and the second one is the regular
expression.

Here is the syntax of the `regexp` function:
`regexp(predicate, /regular-expression/)`

Let's execute the following query to find the hashtags that have the substring
`graph`.

Go to the query tab, type in the query, and click Run.

```graphql
{
  reg_search(func: regexp(hashtag, /^.*graph.*$/)) {
    hashtag
  }
}
```

Oops! We have an error! It looks like we forgot to set the `trigram` index on
the `hashtag` predicate.

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/trigram-error.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=3d983d03b02115c708f65fc8baf48c48" alt="The hashtags" width="854" height="406" data-path="images/dgraph/guides/get-started-with-dgraph/trigram-error.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/trigram-error.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=1f492a8d0a758dfa79c32aa7fe197884 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/trigram-error.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=6f45c5c381b54d36c858d6345fd024c8 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/trigram-error.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=aa29c9f105cd8f2a5fb748e696a89426 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/trigram-error.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=0b1937ad9cee7de4122dce14f1361a16 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/trigram-error.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=20fccff0d0c910bf788b2c3e20567404 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/trigram-error.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=fe940e1e75dfc7ebb19bacb9629f128c 2500w" data-optimize="true" data-opv="2" />

Again, setting a `trigram` index is similar to setting any other string index,
let's do that for the `hashtag` predicate.

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/set-trigram.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=0ba790aa20db3045b7697c6a3e3ff0ad" alt="The hashtags" width="854" height="409" data-path="images/dgraph/guides/get-started-with-dgraph/set-trigram.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/set-trigram.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=d2d0f20c4af1e96268fbb1b17da58b2c 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/set-trigram.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=2255d53ed5a6c64179d99f3c8ff809c3 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/set-trigram.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=a7f4473d05f38db2e047f44da1444003 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/set-trigram.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=ec8cb174eb974e09f3a218f6fe28f163 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/set-trigram.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=65085f8d118876667d2521d489d9e924 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/set-trigram.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=ed419661be74802f67b5a3492851d583 2500w" data-optimize="true" data-opv="2" />

*Note: Refer to the [previous tutorial](./string-indicies) if you're not sure
about creating an index on a string predicate.*

Now, let's re-run the `regexp` query.

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/regex-query-1.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=c6f4341a3f6b23c92ae35b0236b4485f" alt="regex-1" width="854" height="411" data-path="images/dgraph/guides/get-started-with-dgraph/regex-query-1.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/regex-query-1.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=103ee00203ab5b80dc69e9c4eb6f05a0 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/regex-query-1.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=8485ed2ed45e0dbe4a969c72d76c5fda 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/regex-query-1.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=33bb60b6fb7dad4dd48bb01038890939 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/regex-query-1.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=224f405a747912fdfe20c1df090f9e0f 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/regex-query-1.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=7f818174515ed907e389feddd398a82c 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/regex-query-1.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=23f17a596b9e740ef23e73eaf8ad82c5 2500w" data-optimize="true" data-opv="2" />

*Note: Refer to [the first tutorial](./introduction) if you're not familiar with
the query structure in general* Success!

But we only have the following hashtags in the result: `Dgraph` and
`graphqlconf`.

That's because `regexp` function is case-sensitive by default.

Add the character `i` at the end of the second argument of the `regexp` function
to make it case insensitive: `regexp(predicate, /regular-expression/i)`

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/regex-query-2.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=84c447e2d3b6efd195c714428f51f49f" alt="regex-2" width="854" height="414" data-path="images/dgraph/guides/get-started-with-dgraph/regex-query-2.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/regex-query-2.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=997ceddfb417aef35049b7a01521c234 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/regex-query-2.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=25b0a421c14849e92aeff1ba8e7920ff 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/regex-query-2.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=c65451e868016049bcd9f10386d134da 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/regex-query-2.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=81be3372c371b1916e87d19759fc6710 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/regex-query-2.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=c0dbd28156ea43b7a777115d6db035b9 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/regex-query-2.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=125ea53ce4c9341ab795849951853dae 2500w" data-optimize="true" data-opv="2" />

Now we have the four hashtags with substring `graph` in them.

Let's modify the regular expression to match only the `hashtags` which have a
prefix called `graph`.

```graphql
{
  reg_search(func: regexp(hashtag, /^graph.*$/i)) {
    hashtag
  }
}
```

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/regex-query-3.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=0f0e89a67388dc413eeeeff9556a6c37" alt="regex-3" width="854" height="415" data-path="images/dgraph/guides/get-started-with-dgraph/regex-query-3.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/regex-query-3.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=4a0514551450649dcf560b9164d85548 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/regex-query-3.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=9f6500485ee439ffa50cfbc6d1aa9f81 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/regex-query-3.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=5f66dd8800908dead5e05f357d3dc334 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/regex-query-3.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=4fbe8068b277316ec959c22227f2086d 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/regex-query-3.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=98cd0cf36453e8a0d521c5da9875055c 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/regex-query-3.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=d7af7c7a14a074bdc00d71844f200c5e 2500w" data-optimize="true" data-opv="2" />

## Summary

In this tutorial, we learned about Full-text search and regular expression based
search capabilities in Dgraph.

Did you know that Dgraph also offers fuzzy search capabilities, which can be
used to power features like `product` search in an e-commerce store?

Let's learn about the fuzzy search in our next tutorial.

Sounds interesting?

Check out our next tutorial of the getting started series
[here](./fuzzy-search).

## Need Help

* Please use [discuss.hypermode.com](https://discuss.hypermode.com) for
  questions, feature requests, bugs, and discussions.
