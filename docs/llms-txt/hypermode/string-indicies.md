# Source: https://docs.hypermode.com/dgraph/guides/get-started-with-dgraph/string-indicies.md

# Get Started with Dgraph - String Indices

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

**Welcome to the fifth tutorial of getting started with Dgraph.**

In the [previous tutorial](./multi-language-strings), we learned about using
multi-language strings and operations on them using
[language tags](https://www.w3schools.com/tags/ref_language_codes.asp).

In this tutorial, we'll model tweets in Dgraph and, using it, we'll learn more
about string indices in Dgraph.

We'll specifically learn about:

* Modeling tweets in Dgraph.
* Using String indices in Dgraph
  * Querying twitter users using the `hash` index.
  * Comparing strings using the `exact` index.
  * Searching for tweets based on keywords using the `term` index.

Here's the complimentary video for this blog post. It'll walk you through the
steps of this getting started episode.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ww5cwixwkHo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

Let's start analyzing the anatomy of a real tweet and figure out how to model it
in Dgraph.

The accompanying video of the tutorial will be out shortly, so stay tuned to
[our YouTube channel](https://www.youtube.com/channel/UCghE41LR8nkKFlR3IFTRO4w).

## Modeling a tweet in Dgraph

Here's a sample tweet.

```Test tweet for the fifth episode of getting started series with @dgraphlabs.
Wait for the video of the fourth one by @francesc the coming Wednesday! #GraphDB #GraphQL

— Karthic Rao | karthic.eth (@hackintoshrao) November 13, 2019
```

Let's dissect the tweet above. Here are the components of the tweet:

* **The Author**

  The author of the tweet is the user `@hackintoshrao`.

* **The Body**

  This component is the content of the tweet.

  > Test tweet for the fifth episode of getting started series with @dgraphlabs.
  > Wait for the video of the fourth one by @francesc the coming Wednesday!
  > \#GraphDB #GraphQL

* **The Hashtags**

  Here are the hashtags in the tweet: `#GraphQL` and `#GraphDB`.

* **The Mentions**

  A tweet can mention other twitter users.

  Here are the mentions in the tweet above: `@dgraphlabs` and `@francesc`.

Before we model tweets in Dgraph using these components, let's recap the design
principles of a graph model:

> `Nodes` and `Edges` are the building blocks of a graph model. May it be a
> sale, a tweet, user info, any concept or an entity is represented as a node.
> If any two nodes are related, represent that by creating an edge between them.

With the above design principles in mind, let's go through components of a tweet
and see how we could fit them into Dgraph.

**The Author**

The Author of a tweet is a twitter user. We should use a node to represent this.

**The Body**

We should represent every tweet as a node.

**The Hashtags**

It is advantageous to represent a hashtag as a node of its own. It gives us
better flexibility while querying.

Though you can search for hashtags from the body of a tweet, it's not efficient
to do so. Creating unique nodes to represent a hashtag, allows you to write
performant queries like the following: *Hey Dgraph, give me all the tweets with
hashtag #graphql*

**The Mentions**

A mention represents a twitter user, and we've already modeled a user as a node.
Therefore, we represent a mention as an edge between a tweet and the users
mentioned.

### The Relationships

We have three types of nodes: `User`, `Tweet,` and `Hashtag`.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-nodes.jpg?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=55dc6165eafd7160a3b618257ec62452" alt="graph nodes" width="541" height="421" data-path="images/dgraph/guides/get-started-with-dgraph/a-nodes.jpg" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-nodes.jpg?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=fd5014cb955e81b601b10828bd754dd8 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-nodes.jpg?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=8e8ed987c92eee3308e7f7843cb4054e 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-nodes.jpg?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=73157f6abee84bc49368b23bfb567470 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-nodes.jpg?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=e6037ed704e0208ba6728e269e645295 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-nodes.jpg?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=106beab344e14ab6af4062922773f042 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-nodes.jpg?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=9d09f05a16ccbdc35686a6a500974656 2500w" data-optimize="true" data-opv="2" />

Let's look at how these nodes might be related to each other and model their
relationship as an edge between them.

**The User and Tweet nodes**

There's a two-way relationship between a `Tweet` and a `User` node.

* Every tweet is authored by a user, and a user can author many tweets.

Let's name the edge representing this relationship as `authored` .

An `authored` edge points from a `User` node to a `Tweet` node.

* A tweet can mention many users, and users can be mentioned in many tweets.

Let's name the edge which represents this relationship as `mentioned`.

A `mentioned` edge points from a `Tweet` node to a `User` node. These users are
the ones who are mentioned in the tweet.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-tweet-user.jpg?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=2a32be34df093f16bf922c66730682b5" alt="graph nodes" width="731" height="261" data-path="images/dgraph/guides/get-started-with-dgraph/a-tweet-user.jpg" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-tweet-user.jpg?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=12c2adb2dc481537b87a3fa00f9f1d20 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-tweet-user.jpg?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=f419f12da51474ce6d64eae19b9fdff1 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-tweet-user.jpg?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=7ca3d3b4676881c44c9d0b7801552352 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-tweet-user.jpg?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=7b02b1b8a9855a7cb0274c3bec7ddcb4 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-tweet-user.jpg?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=41fe38709f586f15fe06a4c733717cf9 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-tweet-user.jpg?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=3cf686ee187afa7adb143df0a5a632d8 2500w" data-optimize="true" data-opv="2" />

**The tweet and the hashtag nodes**

A tweet can have one or more hashtags. Let's name the edge, which represents
this relationship as `tagged_with`.

A `tagged_with` edge points from a `Tweet` node to a `Hashtag` node. These
hashtag nodes correspond to the hashtags in the tweets.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-tagged.jpg?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=f60bc4a992c7f6b75f25cd920e6fd69b" alt="graph nodes" width="351" height="421" data-path="images/dgraph/guides/get-started-with-dgraph/a-tagged.jpg" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-tagged.jpg?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=6dad94c7b151b66a0ed14c2157a9244c 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-tagged.jpg?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=d20f755ff5bd1fa86c2ff4614e97942a 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-tagged.jpg?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=ff7727381a0dcdd0694980050d2724b7 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-tagged.jpg?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=5bbcbef2744917ba9a371ba023e9b94b 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-tagged.jpg?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=ad1b2e6472f84afe32c845f8d227a6e8 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-tagged.jpg?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=7a57b6bb10738cdf55f3b4aa5bb7b31f 2500w" data-optimize="true" data-opv="2" />

**The Author and hashtag nodes**

There's no direct relationship between an author and a hashtag node. Hence, we
don't need a direct edge between them.

Our graph model of a tweet is ready! Here's it's.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model-2.jpg?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=015b7b4a7968e3671e14637e5e9b000b" alt="tweet model" width="535" height="480" data-path="images/dgraph/guides/get-started-with-dgraph/a-graph-model-2.jpg" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model-2.jpg?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=abec03daa811efa6e8d06bf9b265ed53 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model-2.jpg?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=de6db0e1e91f01ff562083ffc7c8e1b1 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model-2.jpg?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=dd4659fc4fddb16f5d249e481c7996ac 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model-2.jpg?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=bb9f3aaf3728e47bbf9bdc147f811da1 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model-2.jpg?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=7374da73ab742b30244dd063c4c2411a 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model-2.jpg?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=975ee4cc3be47b505175a0a3fd64afb4 2500w" data-optimize="true" data-opv="2" />

Here is the graph of our sample tweet.

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/c-tweet-model.jpg?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=3efc13be70a265889763b5c6ac222663" alt="tweet model" width="694" height="480" data-path="images/dgraph/guides/get-started-with-dgraph/c-tweet-model.jpg" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/c-tweet-model.jpg?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=d93872976b3784da36f6cbc81ea5e82b 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/c-tweet-model.jpg?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=467a186a4ca805b4e996eb385ef4ccee 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/c-tweet-model.jpg?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=191e42b688857dbe5318b3886388167b 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/c-tweet-model.jpg?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=c37f4fd6f7afb2fa9237487f74ed2530 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/c-tweet-model.jpg?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=cecf0e6c61effac243df83a4305d4ca7 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/c-tweet-model.jpg?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=04697a3335e8d1d03373ea2acdf12b1a 2500w" data-optimize="true" data-opv="2" />

Let's add a couple of tweets to the list.

```
So many good talks at #graphqlconf, next year I'll make sure to be *at least* in the audience!

Also huge thanks to the live tweeting by @dgraphlabs for alleviating the FOMO 😊#GraphDB ♥️ #GraphQL https://t.co/5uDpbswFZi

— francesc (@francesc) June 21, 2019
Let's Go and catch @francesc at @Gopherpalooza today, as he scans into Go source code by building its Graph in Dgraph!

Be there, as he Goes through analyzing Go source code, using a Go program, that stores data in the GraphDB built in Go!#golang #GraphDB #Databases #Dgraph pic.twitter.com/sK90DJ6rLs

— Dgraph Labs (@dgraphlabs) November 8, 2019
```

We'll be using these two tweets and the sample tweet, which we used in the
beginning as our dataset. Open Ratel, go to the mutate tab, paste the mutation,
and click Run.

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

<Note>
  {" "}

  If you're new to Dgraph, and yet to figure out how to run the database and use
  Ratel, we highly recommend reading the [first article of the
  series](/introduction)
</Note>

Here is the graph we built.

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=6b4c61b34865245af121d67d93d73eaf" alt="tweet graph" width="854" height="431" data-path="images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=402ac155f0cc64215de93c227eafa133 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=82f8fbac5d4e9628ed40698f78075ec3 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=fb9049ab2b58e2e4552e323ef53dee06 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=e869eabc68ab7fba47ef4db444ec8df9 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=e3e0b11a8512bb569bc6ba4417278b3f 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/x-all-tweets.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=a0afc339ef35a24112823a2d6b52aa6c 2500w" data-optimize="true" data-opv="2" />

Our graph has:

* Five blue twitter user nodes.
* The green nodes are the tweets.
* The blue ones are the hashtags.

Let's start our tweet exploration by querying for the twitter users in the
database.

```
{
  tweet_graph(func: has(user_handle)) {
     user_handle
  }
}
```

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/j-users.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=20ae3a11a5663014b316b641352003a3" alt="tweet model" width="854" height="428" data-path="images/dgraph/guides/get-started-with-dgraph/j-users.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/j-users.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=c218a0b7b970681f1809ef4c84845e6e 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/j-users.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=7d41d92b675b7e14d143daa75c135209 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/j-users.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=d1b094fa143920ae158ade1da0ac279b 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/j-users.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=ddc7c25b607be3f9060d4318e2b17d97 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/j-users.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=320afd9fe398003ef8c79ddaf15aba03 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/j-users.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=3d046cc776b4aca5c230ad4cdd1a6a97 2500w" data-optimize="true" data-opv="2" />

*Note: If the query syntax above looks not so familiar to you, check out the
[first tutorial](./introduction).*

We have four twitter users: `@hackintoshrao`, `@francesc`, `@dgraphlabs`, and
`@gopherpalooza`.

Now, let's find their tweets and hashtags too.

```graphql
{
  tweet_graph(func: has(user_handle)) {
     user_name
     authored {
      tweet
      tagged_with {
        hashtag
      }
    }
  }
}
```

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/y-author-tweet.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=5f1283d878e763dd83606bf3bfb6fc7f" alt="tweet model" width="854" height="408" data-path="images/dgraph/guides/get-started-with-dgraph/y-author-tweet.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/y-author-tweet.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=c0bd38981d811b24a401159f87a10009 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/y-author-tweet.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=9a1a35726895b52210204d965f0377b4 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/y-author-tweet.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=05326473c7daacee378c429cc6af4e1e 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/y-author-tweet.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=c91c4d736dc5cd299cc66ee0ec6f4a57 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/y-author-tweet.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=7a9970c92d5961e75c7eca6dff1f09b5 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/y-author-tweet.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=454ec2b3d0953b6c22454a55976eeb31 2500w" data-optimize="true" data-opv="2" />

*Note: If the traversal query syntax in the above query is not familiar to you,
[check out the third tutorial](./types-and-operations) of the series.*

Before we start querying our graph, let's learn a bit about database indices
using a simple analogy.

### What are indices?

Indexing is a way to optimize the performance of a database by minimizing the
number of disk accesses required when a query is processed.

Consider a "Book" of 600 pages, divided into 30 sections. Let's say each section
has a different number of pages in it.

Now, without an index page, to find a particular section that starts with the
letter "F", you have no other option than scanning through the entire book. i.e:
600 pages.

But with an index page at the beginning makes it easier to access the intended
information. You just need to look over the index page, after finding the
matching index, you can efficiently jump to the section by skipping other
sections.

But remember that the index page also takes disk space! Use them only when
necessary.

In our next section,let's learn some interesting queries on our twitter graph.

## String indices and querying

### Hash index

Let's compose a query which says: *Hey Dgraph, find me the tweets of user with
twitter handle equals to `hackintoshrao`.*

Before we do so, we need first to add an index has to the `user_handle`
predicate. We know that there are 5 types of string indices: `hash`, `exact`,
`term`, `full-text`, and `trigram`.

The type of string index to be used depends on the kind of queries you want to
run on the string predicate.

In this case, we want to search for a node based on the exact string value of a
predicate. For a use case like this one, the `hash` index is recommended.

Let's first add the `hash` index to the `user_handle` predicate.

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/k-hash.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=1dff2da7d0bfef059e67fb78ad466ccc" alt="tweet model" width="854" height="425" data-path="images/dgraph/guides/get-started-with-dgraph/k-hash.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/k-hash.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=333e67ba135b5a6eb6d3c2c249557f5d 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/k-hash.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=6b3487f716dd14efff826336efe44446 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/k-hash.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=4a71e6f69b057a1ff873dfe8b81fefe2 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/k-hash.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=20a50718d7873baeec0153e5d168d45f 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/k-hash.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=0403fabadd127cd446444aa029a3cd8c 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/k-hash.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=35cad25945bc847946070f39514a1384 2500w" data-optimize="true" data-opv="2" />

Now, let's use the `eq` comparator to find all the tweets of `hackintoshrao`.

Go to the query tab, type in the query, and click Run.

```graphql
 {
  tweet_graph(func: eq(user_handle, "hackintoshrao")) {
     user_name
     authored {
    tweet
    }
  }
}
```

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/z-exact.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=da8d1fe1b11c057c5e595f1dfba6487c" alt="tweet model" width="854" height="403" data-path="images/dgraph/guides/get-started-with-dgraph/z-exact.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/z-exact.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=c7122a7e473e6ef33fd8a614d451b092 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/z-exact.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=dd5c953428a2a1c223cad7964fb9e8da 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/z-exact.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=0e9fe68273b18dcaec0e00b648fca1b4 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/z-exact.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=870d61d8d7635b7c373fcecfa6409958 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/z-exact.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=c9524eba4468a102cca40e5bf3d572c4 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/z-exact.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=b019003db0530e8129be6f5731420a42 2500w" data-optimize="true" data-opv="2" />

*Note: Refer to [the third tutorial](./types-and-operations), if you want to
know about comparator functions like `eq` in detail.*

Let's extend the last query also to fetch the hashtags and the mentions.

```graphql
{
  tweet_graph(func: eq(user_handle, "hackintoshrao")) {
     user_name
     authored {
      tweet
      tagged_with {
        hashtag
      }
      mentioned {
        user_name
      }
    }
  }
}
```

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-hash-query.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=dab811d5ebc1bfae8e1227cf0c1b00f6" alt="tweet model" width="854" height="428" data-path="images/dgraph/guides/get-started-with-dgraph/l-hash-query.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-hash-query.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=632077b26ca0f5d9df99d2f1061e05dd 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-hash-query.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=b5de96c05f5220db10ec215f4927d5af 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-hash-query.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=8e8eebe594408b163330ad8825e405ed 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-hash-query.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=70b1d4f4313782ab2d8d7e94e460c716 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-hash-query.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=66ac451256f52e4162212f555a0bea5e 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-hash-query.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=56f6699331a76a50ef9d88f04e17db21 2500w" data-optimize="true" data-opv="2" />

*Note: If the traversal query syntax in the above query is not familiar to you,
[check out the third tutorial](./types-and-operations) of the series.*

Did you know that string values in Dgraph can also be compared using comparators
like greater-than or less-than?

In our next section, let's see how to run the comparison functions other than
`equals to (eq)` on the string predicates.

### Exact Index

We discussed in the [third tutorial](./types-and-operations) that there five
comparator functions in Dgraph.

Here's a quick recap:

| comparator function name | Full form                |
| ------------------------ | ------------------------ |
| eq                       | equals to                |
| lt                       | less than                |
| le                       | less than or equal to    |
| gt                       | greater than             |
| ge                       | greater than or equal to |

All five comparator functions can be applied to the string predicates.

We have already used the `eq` operator. The other four are useful for
operations, which depend on the alphabetical ordering of the strings.

Let's learn about it with a simple example.

Let's find the twitter accounts which come after `dgraphlabs` in alphabetically
sorted order.

```graphql
{
  using_greater_than(func: gt(user_handle, "dgraphlabs")) {
    user_handle
  }
}
```

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/n-exact-error.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=4d651cd99972e962aa068e6f776eaa77" alt="tweet model" width="854" height="404" data-path="images/dgraph/guides/get-started-with-dgraph/n-exact-error.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/n-exact-error.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=b970ce6efbcf6acbdb796bf224d7f642 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/n-exact-error.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=1064ffdbee8262efa558d27a3ec7e9c7 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/n-exact-error.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=a4bd19534bb8a6499d4efe82d7247f3f 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/n-exact-error.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=fed43dcacfb5983b9df0192fd68f8b09 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/n-exact-error.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=23cd8e367dbef3c908066ad1b97d866b 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/n-exact-error.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=802ffcf9e409d536b125a35ca84b43f5 2500w" data-optimize="true" data-opv="2" />

Oops, we have an error!

You can see from the error that the current `hash` index on the `user_handle`
predicate doesn't support the `gt` function.

To be able to do string comparison operations like the one above, you need first
set the `exact` index on the string predicate.

The `exact` index is the only string index that allows you to use the `ge`,
`gt`, `le`, `lt` comparators on the string predicates.

Remind you that the `exact` index also allows you to use `equals to (eq)`
comparator. But, if you want to just use the `equals to (eq)` comparator on
string predicates, using the `exact` index would be an overkill. The `hash`
index would be a better option, as it's, in general, much more space-efficient.

Let's see the `exact` index in action.

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/o-exact-conflict.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=bedb06b006d9d07a0b43153542529346" alt="set exact" width="854" height="414" data-path="images/dgraph/guides/get-started-with-dgraph/o-exact-conflict.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/o-exact-conflict.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=5aa007e194f074166d95df180f50ed1c 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/o-exact-conflict.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=57a15e9c5b3d7b41ea7a6a017eaaa9dd 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/o-exact-conflict.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=437c6cdae7db879da4335a2393e695d2 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/o-exact-conflict.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=a5da3d34e817bd60d3c010afb622dfe2 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/o-exact-conflict.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=32d949ad2c814994c96f42dc3d980080 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/o-exact-conflict.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=2a30fa76b4627e4fee94c02d7b8c8717 2500w" data-optimize="true" data-opv="2" />

We again have an error!

Though a string predicate can have more than one index, some of them are not
compatible with each other. One such example is the combination of the `hash`
and the `exact` indices.

The `user_handle` predicate already has the `hash` index, so trying to set the
`exact` index gives you an error.

Let's uncheck the `hash` index for the `user_handle` predicate, select the
`exact` index, and click update.

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/p-set-exact.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=01cd62df6f23bcf4fd7bd6acac6707b7" alt="set exact" width="854" height="412" data-path="images/dgraph/guides/get-started-with-dgraph/p-set-exact.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/p-set-exact.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=25d97774c427b158b9855e3175fde164 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/p-set-exact.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=f74a4e42163c57b762fb050bc08e8d68 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/p-set-exact.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=4f83366b8464ee37f4294ebf5e96e96c 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/p-set-exact.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=4aa34b78f32b507ff7b4aa3fb71f03f9 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/p-set-exact.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=db56789699b2297f1216dd11b28fb8db 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/p-set-exact.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=9ecb3905207ced019f79d17d10066482 2500w" data-optimize="true" data-opv="2" />

Though Dgraph allows you to change the index type of a predicate, do it only if
it's necessary. When the indices are changed, the data needs to be re-indexed,
and this takes some computing, so it could take a bit of time. While the
re-indexing operation is running, all mutations will be put on hold.

Now, let's re-run the query.

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/q-exact-gt.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=83be689798ef1fce5ea37bd61aebd0d0" alt="tweet model" width="854" height="398" data-path="images/dgraph/guides/get-started-with-dgraph/q-exact-gt.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/q-exact-gt.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=d712fe74d8e96da7df019c9b92e276a8 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/q-exact-gt.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=d220cb7a7630595669f0cd475f0ddfe8 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/q-exact-gt.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=0c7fc0aff9348bb5e6b0f694be273490 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/q-exact-gt.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=eae36bd910d4823a28a1ae0a87ed8912 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/q-exact-gt.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=a810685907bc5b6e8e57ca5b6929b84c 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/q-exact-gt.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=a76219d6c87547eb2bd1061e56089551 2500w" data-optimize="true" data-opv="2" />

The result contains three twitter handles: `francesc`, `gopherpalooza`, and
`hackintoshrao`.

In the alphabetically sorted order, these twitter handles are greater than
`dgraphlabs`.

Some tweets appeal to us better than others. For instance, I love `Graphs` and
`Go`. Hence, I would surely enjoy tweets that are related to these topics. A
keyword-based search is a useful way to find relevant information.

Can we search for tweets based on one or more keywords related to your
interests?

Yes, we can! Let's do that in our next section.

### The Term index

The `term` index lets you search string predicates based on one or more
keywords. These keywords are called terms.

To be able to search tweets with specific keywords or terms, we need to first
set the `term` index on the tweets.

Adding the `term` index is similar to adding any other string index.

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/r-term-set.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=079e43393277db2c7b30ef7eda8fa687" alt="term set" width="854" height="413" data-path="images/dgraph/guides/get-started-with-dgraph/r-term-set.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/r-term-set.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=2684cf7f8e00cd2dca9c71fda0a06da3 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/r-term-set.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=e01228be4e5f4f7430018a5825ca4d97 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/r-term-set.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=78fbfbc6c8454631c8d2de56daba413e 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/r-term-set.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=1d8bb0bdbaff59fbf91f5d78819ce2cd 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/r-term-set.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=95cdb005d5015ecbdd4eeb647183b5a7 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/r-term-set.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=40680e07e8923ad1e0c0c9c8e04c2f92 2500w" data-optimize="true" data-opv="2" />

Dgraph provides two built-in functions specifically to search for terms:
`allofterms` and `anyofterms`.

Apart from these two functions, the `term` index only supports the `eq`
comparator. This means any other query functions (like lt, gt, le...) fails when
run on string predicates with the `term` index.

We'll soon take a look at the table containing the string indices and their
supporting query functions. But first, let's learn how to use `anyofterms` and
`allofterms` query functions. Let's write a query to find all tweets with terms
or keywords `Go` or `Graph` in them.

Go the query tab, paste the query, and click Run.

```graphql
{
  find_tweets(func: anyofterms(tweet, "Go Graph")) {
    tweet
  }
}
```

Here's the matched tweet from the query response:

```json
{
  "tweet": "Let's Go and catch @francesc at @Gopherpalooza today, as he scans into Go source code by building its Graph in Dgraph!\nBe there, as he Goes through analyzing Go source code, using a Go program, that stores data in the GraphDB built in Go!\n#golang #GraphDB #Databases #Dgraph "
}
```

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/s-go-graph.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=84d1f9b5239291bab3dd56373b424297" alt="go graph set" width="854" height="426" data-path="images/dgraph/guides/get-started-with-dgraph/s-go-graph.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/s-go-graph.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=7d698c9e6207dc075d387642d41c59ce 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/s-go-graph.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=3919708803654f1538ac729580d1eb55 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/s-go-graph.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=f744044d750f3a8f98d46e38231e1211 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/s-go-graph.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=26105b8e302f1b6ab8c9b8d48cb9e624 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/s-go-graph.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=2f869b7d37321e01042f207aacd733f1 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/s-go-graph.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=9944df0ae7a02bf1ce6e5b94ce6818ab 2500w" data-optimize="true" data-opv="2" />

*Note: Check out [the first tutorial](./introduction) if the query syntax, in
general, is not familiar to you*

The `anyofterms` function returns tweets which have either of `Go` or `Graph`
keyword.

In this case, we've used only two terms to search for (`Go` and `Graph`), but
you can extend for any number of terms to be searched or matched.

The result has one of the three tweets in the database. The other two tweets
don't make it to the result since they don't have either of the terms `Go` or
`Graph`.

It is also important to notice that the term search functions (`anyofterms` and
`allofterms`) are insensitive to case and special characters.

This means, if you search for the term `GraphQL`, the query returns a positive
match for all of the following terms found in the tweets: `graphql`, `graphQL`,
`#graphql`, `#GraphQL`.

Now, let's find tweets that have either of the terms `Go` or `GraphQL` in them.

```graphql
{
  find_tweets(func: anyofterms(tweet, "Go GraphQL")) {
    tweet
  }
}
```

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/t-go-graphql-all.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=8bca7e0047b26164fbf152e6e8efe7f8" alt="Go Graphql" width="854" height="428" data-path="images/dgraph/guides/get-started-with-dgraph/t-go-graphql-all.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/t-go-graphql-all.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=506dde1fcbe6a01e910940abc4fda984 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/t-go-graphql-all.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=963854e3468c6fabf097f7c70d91d758 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/t-go-graphql-all.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=60cca857303aa677c07df64de690a3d7 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/t-go-graphql-all.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=3e4893e7348e42143fbc0d229dd2b3f9 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/t-go-graphql-all.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=496ec4896212be103f3990764f0b60d6 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/t-go-graphql-all.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=4b2d76ecb8a4a1cf93b8f005fe68cb1c 2500w" data-optimize="true" data-opv="2" />

Oh wow, we have all the three tweets in the result. This means, all of the three
tweets have either of the terms `Go` or `GraphQL`.

Now, how about finding tweets that contain both the terms `Go` and `GraphQL` in
them. We can do it by using the `allofterms` function.

```graphql
{
  find_tweets(func: allofterms(tweet, "Go GraphQL")) {
    tweet
  }
}
```

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/u-allofterms.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=75630580fcdf7ac4b33a2bfa57aa3de8" alt="Go Graphql" width="854" height="426" data-path="images/dgraph/guides/get-started-with-dgraph/u-allofterms.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/u-allofterms.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=5e9aef60822963d9ac25cb17b6c50e19 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/u-allofterms.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=c6bfb0a628ad7ec56de92761d341d425 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/u-allofterms.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=8f92c8801439c4b26f5f10e83455c3b4 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/u-allofterms.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=e14a14752a8de5a37483e6cf0cc993e6 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/u-allofterms.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=00fde9ecf92bb33393a76a4834467fdf 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/u-allofterms.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=455776ec26fdd8a7ece3922ace758a33 2500w" data-optimize="true" data-opv="2" />

We have an empty result. None of the tweets have both the terms `Go` and
`GraphQL` in them.

Besides `Go` and `Graph`, I'm also a big fan of `GraphQL` and `GraphDB`.

Let's find out tweets that contain both the keywords `GraphQL` and `GraphDB` in
them.

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/v-graphdb-graphql.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=03e3ee5eb2d549cae40ea3df09ce2f37" alt="Graphdb-GraphQL" width="854" height="427" data-path="images/dgraph/guides/get-started-with-dgraph/v-graphdb-graphql.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/v-graphdb-graphql.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=2549ff3588be1be5b1fdea1bbe8a608c 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/v-graphdb-graphql.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=178ce57c678ab8adbeb53ba83309b591 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/v-graphdb-graphql.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=a60d1a5151e000cd0a4a5dd39cbb4182 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/v-graphdb-graphql.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=2559a4973773e28b0d819825139c26bd 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/v-graphdb-graphql.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=8f1569f5e70324e904d39cb58c4d21cf 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/v-graphdb-graphql.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=ecac1b7d4f5ec798db653573cbc1b612 2500w" data-optimize="true" data-opv="2" />

We have two tweets in a result which has both the terms `GraphQL` and `GraphDB`.

```
{
  "tweet": "Test tweet for the fifth episode of getting started series with @dgraphlabs. Wait for the video of the fourth one by @francesc the coming Wednesday!\n#GraphDB #GraphQL"
},
{
  "tweet": "So many good talks at #graphqlconf, next year I'll make sure to be *at least* in the audience!\nAlso huge thanks to the live tweeting by @dgraphlabs for alleviating the FOMO😊\n#GraphDB ♥️ #GraphQL"
}
```

Before we wrap up, here's the table containing the three string indices we
learned about, and their compatible built-in functions.

| Index | Valid query functions      |
| ----- | -------------------------- |
| hash  | eq                         |
| exact | eq, lt, gt, le, ge         |
| term  | eq, allofterms, anyofterms |

## Summary

In this tutorial, we modeled a series of tweets and set up the exact, term, and
hash indices in order to query them.

Did you know that Dgraph also offers more powerful search capabilities like
full-text search and regular expressions based search?

In the next tutorial, we'll explore these features and learn about more powerful
ways of searching for your favorite tweets!

Sounds interesting? Then see you all soon in the next tutorial. Till then, happy
Graphing!

Check out our next tutorial of the getting started series
[here](./advanced-text-search).

## Need Help

* Please use [discuss.hypermode.com](https://discuss.hypermode.com) for
  questions, feature requests, bugs, and discussions.
