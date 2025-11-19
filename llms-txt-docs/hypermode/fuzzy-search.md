# Source: https://docs.hypermode.com/dgraph/guides/get-started-with-dgraph/fuzzy-search.md

# Get Started with Dgraph - Fuzzy Search

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

**Welcome to the seventh tutorial of getting started with Dgraph.**

In the [previous tutorial](./advanced-text-search), we learned about building
advanced text searches on social graphs in Dgraph, by modeling tweets as an
example. We queried the tweets using the `fulltext` and `trigram` indices and
implemented full-text and regular expression search on the tweets.

In this tutorial, we'll continue exploring Dgraph's string querying capabilities
using the twitter model from [the fifth](./string-indicies) and
[the sixth](./advanced-text-search) tutorials. In particular, we'll implement a
`twitter username` search feature using the Dgraph's fuzzy search function.

The accompanying video of the tutorial will be out shortly, so stay tuned to
[our YouTube channel](https://www.youtube.com/channel/UCghE41LR8nkKFlR3IFTRO4w).

***

Before we dive in, let's review of how we modeled the tweets in the previous two
tutorials:

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=1d0514c94d40edf52d50aa860ed1f0d3" alt="tweet model" width="526" height="461" data-path="images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=a281d7188019fe6251c3aefa0c0aae11 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=b2f996f4177c8996fe3af07e79d8a401 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=e0e9fd2f64de3883d1828ced7310ad44 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=894439b7a39e25f76c2541f1c2926bfd 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=7bf1424145c7ec3f72c64e2dd4ec8190 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=19ec71f27740dfb573eda0b62c0c4c1d 2500w" data-optimize="true" data-opv="2" />

We used three real-life example tweets as a sample dataset and stored them in
Dgraph using the above graph as a model.

Here is the sample dataset again if you skipped the previous tutorials. Copy the
mutation below, go to the mutation tab and click Run.

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
[first tutorial of the series before proceeding](./introduction).*

Now you should have a graph with tweets, users, and hashtags, and it's ready for
us to explore.

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=6b4c61b34865245af121d67d93d73eaf" alt="tweet graph" width="854" height="431" data-path="images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=402ac155f0cc64215de93c227eafa133 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=82f8fbac5d4e9628ed40698f78075ec3 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=fb9049ab2b58e2e4552e323ef53dee06 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=e869eabc68ab7fba47ef4db444ec8df9 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=e3e0b11a8512bb569bc6ba4417278b3f 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=a0afc339ef35a24112823a2d6b52aa6c 2500w" data-optimize="true" data-opv="2" />

*Note: If you're curious to know how we modeled the tweets in Dgraph, refer to
[the fifth tutorial](./string-indicies).*

Before we show you the fuzzy search in action, let's first understand what it's
and how does it work.

## Fuzzy search

Providing search capabilities on products or usernames requires searching for
the closest match to a string, if a full match doesn't exist. This feature helps
you get relevant results even if there's a typo or the user doesn't search based
on the exact name it's stored. This is exactly what the fuzzy search does: it
compares the string values and returns the nearest matches. Hence, it's ideal
for our use case of implementing search on the `twitter usernames`.

The functioning of the fuzzy search is based on the `Levenshtein distance`
between the value of the user name stored in Dgraph and the search string.

[`Levenshtein distance`](https://en.wikipedia.org/wiki/Levenshtein_distance) is
a metric that defines the closeness of two strings. `Levenshtein distance`
between two words is the minimum number of single-character edits (insertions,
deletions or substitutions) required to change one word into the other.

For instance, the `Levenshtein Distance` between the strings `book` and `back`
is 2. The value of 2 is justified because by changing two characters, we changed
the word `book` to `back`.

Now you've understood what the fuzzy search is and what it can do. Next, let's
learn how to use it on string predicates in Dgraph.

## Implement Fuzzy Search in Dgraph

To use the fuzzy search on a string predicate in Dgraph, you first set the
`trigram` index.

Go to the Schema tab and set the `trigram` index on the `user_name` predicate.

After setting the `trigram` index on the `user_name` predicate, you can use
Dgraph's built-in function `match` to run a fuzzy search query.

Here is the syntax of the `match` function:
`match(predicate, search string, distance)`

The [match function](/dgraph/dql/functions#fuzzy-matching) takes in three
parameters:

1. The name of the string predicate used for querying.
2. The search string provided by the user
3. An integer that represents the maximum `Levenshtein Distance` between the
   first two parameters. This value should be greater than 0. For example, when
   having an integer of 8 returns predicates with a distance value of less than
   or equal to 8.

Using a greater value for the `distance` parameter can potentially match more
string predicates, but it also yields less accurate results.

Before we use the `match` function, let's first get the list of user names
stored in the database.

```graphql
{
    names(func: has(user_name)) {
        user_name
    }
}
```

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-names.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=0e425974e8f80abdc2f19604d3c7bea9" alt="tweet graph" width="854" height="411" data-path="images/dgraph/guides/get-started-with-dgraph/e-names.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-names.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=3503a170710a5d024fdaddf6afcc9f32 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-names.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=386c66a34e78325d29b54d39fe1a9774 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-names.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=0eb2bba16d18ac9204f26674c3e8ab37 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-names.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=80ee22a371ac9ed67cdad330679bd379 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-names.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=a22cdb46e1d677f9e55e04e069f15c8b 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-names.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=03b3d6a762c55643afcb0ecc491ee198 2500w" data-optimize="true" data-opv="2" />

As you can see from the result, we have four user names: `Gopherpalooza`,
`Karthic Rao`, `Francesc Campoy`, and `Dgraph Labs`.

First, we set the `Levenshtein Distance` parameter to 3. We expect to see Dgraph
returns all the `username` predicates with three or fewer distances from the
provided searching string.

Then, we set the second parameter, the search string provided by the user, as
`graphLabs`.

Go to the query tab, paste the query below and click Run.

```graphql
{
    user_names_Search(func: match(user_name, "graphLabs", 3)) {
        user_name
    }
}
```

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-one.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=41ea8de84408bbff8ccb880ee6c10a46" alt="first query" width="854" height="409" data-path="images/dgraph/guides/get-started-with-dgraph/h-one.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-one.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=9b9ec187575880faf2257fea6cbaf53c 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-one.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=c1b3a721cc82419eb4e64dc4854ccd14 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-one.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=ca1199f24797a761ebc2ba70593b02c6 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-one.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=502ecc1f4ac3b173b10c5943c12b1fa8 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-one.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=b4ca75c69e34ea5f57f6cc241a022c30 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-one.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=c58be8c61dc05e56bb6eb2cd81d7e22c 2500w" data-optimize="true" data-opv="2" />

We got a positive match! Because the search string `graphLabs` is at a distance
of two from the predicate value of `Dgraph Labs`, so we see it in the search
result.

If you are interested in learning more about how to find the Levenshtein
Distance between two strings,
[here is a useful site](https://planetcalc.com/1721/).

Let's run the above query again, but this time we will use the search string
`graphLab` instead. Go to the query tab, paste the query below and click Run.

```graphql
{
    user_names_Search(func: match(user_name, "graphLab", 3)) {
        user_name
    }
}
```

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-two.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=0a154bb9f27410921878aa7da08b873a" alt="first query" width="854" height="410" data-path="images/dgraph/guides/get-started-with-dgraph/i-two.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-two.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=798af53ef04edad3cbda1aff21bf3081 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-two.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=c941a22d6c7f063f18c4686f546800d0 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-two.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=76d87f52f7c907d8087380cd090ebdf5 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-two.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=61b0b464dcf11e1d78b101003728d76e 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-two.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=4daec66fe11e17fa089c4639bf179f3b 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-two.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=ec53f113673575ea76a6dbe82eaf48e0 2500w" data-optimize="true" data-opv="2" />

We still got a positive match with the `user_name` predicate with the value
`Dgraph Labs`! That's because the search string `graphLab` is at a distance of
three from the predicate value of `Dgraph Labs`, so we see it in the search
result.

In this case, the `Levenshtein Distance` between the search string `graphLab`
and the predicate `Dgraph Labs` is 3, hence the match.

For the last run of the query, let's change the search string to `Dgraph` but
keep the Levenshtein Distance at 3.

```graphql
{
    user_names_Search(func: match(user_name, "Dgraph", 3)) {
        user_name
    }
}
```

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/j-three.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=ef39eb5d26f6eefe9f3eb2c5570cb182" alt="first query" width="854" height="412" data-path="images/dgraph/guides/get-started-with-dgraph/j-three.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/j-three.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=ceb36b1ca4723092b9cf80f0d1041632 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/j-three.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=c6fc0a7c1124dbcc8e2429feff5590ae 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/j-three.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=c002a3ab5e119dc78ec252b7da9e460b 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/j-three.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=470d3aebc2c1bce8c93e393aabdd91dc 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/j-three.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=590c8078e0fafe8cbb5f842394d10cf7 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/j-three.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=bfae7861d1fdef4d3e81d1bb27f0bab1 2500w" data-optimize="true" data-opv="2" />

Now you no longer see Dgraph Labs appears in the search result because the
distance between the word `Dgraph` and `Dgraph Labs` is larger than 3. But based
on normal human rationales, you would naturally expect Dgraph Labs appears in
the search result while using Dgraph as the search string.

This is one of the downsides of the fuzzy search based on the
`Levenshtein Distance` algorithm. The effectiveness of the fuzzy search reduces
as the value of the distance parameter decreases, and it also reduces with an
increase in the number of words included in the string predicate.

Therefore it's not recommended to use the fuzzy search on the string predicates
which could contain many words, for instance, predicates which store the values
for `blog posts`, `bio`, `product description` and so on. Hence, the ideal
candidates to use fuzzy search are predicates like `names`, `zipcodes`,
`places`, where the number of words in the string predicate would generally
between 1-3.

Also, based on the use case, tuning the `distance` parameter is crucial for the
effectiveness of fuzzy search.

## Fuzzy search scoring because you asked for it

At Dgraph, we're committed to improving the all-round capabilities of the
distributed Graph database. As part of one of our recent efforts to improve the
database features, we've taken note of the
[request on Github](https://github.com/hypermodeinc/dgraph/issues/3211) by one
of our community members to integrate a `tf-idf` score based text search. This
integration will further enhance the search capabilities of Dgraph.

We've prioritized the resolve of the issue in our product roadmap. We would like
to take this opportunity to say thank you to our community of users for helping
us make the product better.

## Summary

Fuzzy search is a simple and yet effective search technique for a wide range of
use cases. Along with the existing features to query and search string
predicates, the addition of `tf-idf` based search will further improve Dgraph's
capabilities.

This marks the end of our three tutorial streak exploring string indices and
their queries using the graph model of tweets.

Check out our next tutorial of the getting started series [here](./geolocation).

Remember to click the “Join our community” button below and subscribe to our
newsletter to get the latest tutorial right to your inbox.

## Need Help

* Please use [discuss.hypermode.com](https://discuss.hypermode.com) for
  questions, feature requests, bugs, and discussions.
