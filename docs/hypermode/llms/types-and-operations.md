# Source: https://docs.hypermode.com/dgraph/guides/get-started-with-dgraph/types-and-operations.md

# Get Started with Dgraph - Types and Operations

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

**Welcome to the third tutorial of getting started with Dgraph.**

In the [previous tutorial](./basic-operations), we learned about CRUD operations
using UIDs. We also learned about traversals and recursive traversals.

In this tutorial, we'll learn about Dgraph's basic types and how to query for
them. Specifically, we'll learn about:

* Basic data types in Dgraph.
* Querying for predicate values.
* Indexing.
* Filtering nodes.
* Reverse traversing.

Check out the accompanying video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/f401or0hg5E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

Let's start by building the graph of a simple blog app. Here's the Graph model
of our app:

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-main-graph.JPG?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=191d03ed02e9a0502cbec6104bcd27dc" alt="main graph model" width="854" height="463" data-path="images/dgraph/guides/get-started-with-dgraph/a-main-graph.JPG" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-main-graph.JPG?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=8fd563c1136bfb0b0165780013acdbe8 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-main-graph.JPG?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=7692bde4511d5038ad1bc635fab1ea84 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-main-graph.JPG?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=c321c14ed2dba864cfca94a273064e5a 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-main-graph.JPG?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=80382189feee11d5caf9d9344572d14f 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-main-graph.JPG?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=d23c82e9b8f4dad01e1534ad674dc261 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-main-graph.JPG?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=4455d33516d8ddc4a76fcf9b616d7508 2500w" data-optimize="true" data-opv="2" />

This graph has three entities, Author, Blog posts, and Tags. The nodes in the
graph represent these entities. For the rest of the tutorial, we'll call the
nodes representing a blog as a `blog post` node and the node presenting a `tag`
as a `tag node`, and so on.

You can see from the graph model that these entities are related:

* Every Author has one or more blog posts.

The `published` edge relates the blogs to their authors. These edges start from
an `author node` and point to a `blog post` node.

* Every Blog post has one or more tags.

The `tagged` edge relates the blog posts to their tags. These edges emerge from
a `blog post node` and point to a `tag node`.

Let's build our graph.

Go to Ratel, click the mutate tab, paste the following mutation, and click Run.

```json
{
  "set": [
    {
      "author_name": "John Campbell",
      "rating": 4.1,
      "published": [
        {
          "title": "Dgraph's recap of GraphQL Conf - Berlin 2019",
          "url": "https://hypermode.com/blog/graphql-conf-19/",
          "content": "We took part in the recently held GraphQL conference in Berlin. The experience was fascinating, and we were amazed by the high voltage enthusiasm in the GraphQL community. Now, we couldn’t help ourselves from sharing this with Dgraph’s community! This is the story of the GraphQL conference in Berlin.",
          "likes": 100,
          "dislikes": 4,
          "publish_time": "2018-06-25T02:30:00",
          "tagged": [
            {
              "uid": "_:graphql",
              "tag_name": "graphql"
            },
            {
              "uid": "_:devrel",
              "tag_name": "devrel"
            }
          ]
        },
        {
          "title": "Dgraph Labs wants you!",
          "url": "https://hypermode.com/blog/hiring-19/",
          "content": "We recently announced our successful Series A fundraise and, since then, many people have shown interest to join our team. We are very grateful to have so many people interested in joining our team! We also realized that the job openings were neither really up to date nor covered all of the roles that we are looking for. This is why we decided to spend some time rewriting them and the result is these six new job openings!.",
          "likes": 60,
          "dislikes": 2,
          "publish_time": "2018-08-25T03:45:00",
          "tagged": [
            {
              "uid": "_:hiring",
              "tag_name": "hiring"
            },
            {
              "uid": "_:careers",
              "tag_name": "careers"
            }
          ]
        }
      ]
    },
    {
      "author_name": "John Travis",
      "rating": 4.5,
      "published": [
        {
          "title": "How Dgraph Labs Raised Series A",
          "url": "https://hypermode.com/blog/how-dgraph-labs-raised-series-a/",
          "content": "I’m really excited to announce that Dgraph has raised $11.5M in Series A funding. This round is led by Redpoint Ventures, with investment from our previous lead, Bain Capital Ventures, and participation from all our existing investors – Blackbird, Grok and AirTree. With this round, Satish Dharmaraj joins Dgraph’s board of directors, which includes Salil Deshpande from Bain and myself. Their guidance is exactly what we need as we transition from building a product to bringing it to market. So, thanks to all our investors!.",
          "likes": 139,
          "dislikes": 6,
          "publish_time": "2019-07-11T01:45:00",
          "tagged": [
            {
              "uid": "_:announcement",
              "tag_name": "announcement"
            },
            {
              "uid": "_:funding",
              "tag_name": "funding"
            }
          ]
        },
        {
          "title": "Celebrating 10,000 GitHub Stars",
          "url": "https://hypermode.com/blog/10k-github-stars/",
          "content": "Dgraph is celebrating the milestone of reaching 10,000 GitHub stars 🎉. This wouldn’t have happened without all of you, so we want to thank the awesome community for being with us all the way along. This milestone comes at an exciting time for Dgraph.",
          "likes": 33,
          "dislikes": 12,
          "publish_time": "2017-03-11T01:45:00",
          "tagged": [
            {
              "uid": "_:devrel"
            },
            {
              "uid": "_:announcement"
            }
          ]
        }
      ]
    },
    {
      "author_name": "Katie Perry",
      "rating": 3.9,
      "published": [
        {
          "title": "Migrating data from SQL to Dgraph!",
          "url": "https://hypermode.com/blog/migrating-from-sql-to-dgraph/",
          "content": "Dgraph is rapidly gaining reputation as an easy to use database to build apps upon. Many new users of Dgraph have existing relational databases that they want to migrate from. In particular, we get asked a lot about how to migrate data from MySQL to Dgraph. In this article, we present a tool that makes this migration really easy: all a user needs to do is write a small 3 lines configuration file and type in 2 commands. In essence, this tool bridges one of the best technologies of the 20th century with one of the best ones of the 21st (if you ask us).",
          "likes": 20,
          "dislikes": 1,
          "publish_time": "2018-08-25T01:44:00",
          "tagged": [
            {
              "uid": "_:tutorial",
              "tag_name": "tutorial"
            }
          ]
        },
        {
          "title": "Building a To-Do List React App with Dgraph",
          "url": "https://hypermode.com/blog/building-todo-list-react-dgraph/",
          "content": "In this tutorial we will build a To-Do List app using React JavaScript library and Dgraph as a backend database. We will use dgraph-js-http — a library designed to greatly simplify the life of JavaScript developers when accessing Dgraph databases.",
          "likes": 97,
          "dislikes": 5,
          "publish_time": "2019-02-11T03:33:00",
          "tagged": [
            {
              "uid": "_:tutorial"
            },
            {
              "uid": "_:devrel"
            },
            {
              "uid": "_:javascript",
              "tag_name": "javascript"
            }
          ]
        }
      ]
    }
  ]
}
```

Our Graph is ready!

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-fullgraph-2.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=8c337854f75d6710fb0c8e57d01fcf42" alt="rating-blog-rating" width="812" height="480" data-path="images/dgraph/guides/get-started-with-dgraph/l-fullgraph-2.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-fullgraph-2.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=d5dffc1db56fc0574db9a930649b9099 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-fullgraph-2.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=6c8c9c73e838af1db41c2cf392c92bd4 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-fullgraph-2.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=302df6334228c9866ce857f010a39785 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-fullgraph-2.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=b1e0cd662af5ac932301d8e28ae1190c 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-fullgraph-2.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=8d0d80907d3e96a9375626e8d13dd470 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-fullgraph-2.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=eef17163c868d4fe1c749155c1079ad6 2500w" data-optimize="true" data-opv="2" />

Our Graph has:

* Three blue author nodes.
* Each author has two blog posts each - six in total - which are represented by
  the green nodes.
* The tags of the blog posts are in pink. You can see that there are 8 unique
  tags, and some of the blogs share a common tag.

## Data types for predicates

Dgraph automatically detects the data type of its predicates. You can see the
auto-detected data types using the Ratel UI.

Click on the schema tab on the left and then check the `Type` column. You'll see
the predicate names and their corresponding data types.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-initial.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=0abc8b87e782c3c8f3f1acec1b7be71b" alt="rating-blog-rating" width="854" height="374" data-path="images/dgraph/guides/get-started-with-dgraph/a-initial.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-initial.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=bf1ea31f02793539f0f7fb5bbfada4b7 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-initial.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=eafdaf9fbf080fb03bdaeab7265cf8ed 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-initial.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=6e1891052be939601ee73a51f8c0b29f 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-initial.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=57239f4228dd60ce764ddc8598926c34 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-initial.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=6b9b0414c0294a3f821891949288e72a 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-initial.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=6890b6b530ce1b62e1ce1ba967c41bd8 2500w" data-optimize="true" data-opv="2" />

These data types include `string`, `float`, and `int`, and `uid`. Besides them,
Dgraph also offers three more basic data types: `geo`, `dateTime`, and `bool`.

The `uid` types represent predicates between two nodes. In other words, they
represent edges connecting two nodes.

You might have noticed that the `published` and `tagged` predicates are of type
`uid` array (`[uid]`). UID arrays represent a collection of UIDs. This is used
to represent one to many relationships.

For instance, we know that an author can publish more than one blog. Hence,
there could be more than one `published` edge emerging from a given `author`
node, each pointing to a different blog post of the author.

Dgraph's [v1.1 release](https://hypermode.com/blog/release-v1.1.0/) introduced
the type system feature. This feature made it possible to create custom data
types by grouping one or more predicates. But in this tutorial, we'll only focus
on the basic data types.

Also, notice that there are no entries in the indexes column. We'll talk about
indexes in detail shortly.

## Querying for predicate values

First, let's query for all the Authors and their ratings:

```dql
{
  authors_and_ratings(func: has(author_name)) {
    uid
    author_name
    rating
  }
}
```

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-find-rating-2.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=e2a9dcf8f6a73bee526f901f153caab9" alt="authors" width="846" height="480" data-path="images/dgraph/guides/get-started-with-dgraph/a-find-rating-2.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-find-rating-2.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=b0e0e9e05aaae35b23863b6f494a7733 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-find-rating-2.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=fcc9ba2feca5bad4a945b67c48139fa5 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-find-rating-2.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=d9336837b457fcbd6c69a5eb3ad37b27 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-find-rating-2.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=6bdca41c53ef1e74af4604920465777e 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-find-rating-2.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=63abfca1d760b66957e5314a7b10d535 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-find-rating-2.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=7a68367122c0a3a55d8dc5e26831a710 2500w" data-optimize="true" data-opv="2" />

Refer to the [first episode](./introduction) if you have any questions related
to the structure of the query in general.

There are three authors in total in our dataset. Now, let's find the best
authors. Let's query for authors whose rating is 4.0 or more.

In order to achieve our goal, we need a way to select nodes that meets certain
criteria (for example, rating > 4.0). You can do this by using Dgraph's built-in
comparator functions. Here's the list of comparator functions available in
Dgraph:

| comparator function name | Full form                |
| ------------------------ | ------------------------ |
| `eq`                     | equals to                |
| `lt`                     | less than                |
| `le`                     | less than or equal to    |
| `gt`                     | greater than             |
| `ge`                     | greater than or equal to |

There are a total of five comparator functions in Dgraph. You can use any of
them alongside the `func` keyword in your queries.

The comparator function takes two arguments. One is the predicate name and the
other is its comparable value. Here are a few examples.

| Example usage          | Description                                                                  |
| ---------------------- | ---------------------------------------------------------------------------- |
| func: eq(age, 60)      | Return nodes with `age` predicate equal to 60.                               |
| func: gt(likes, 100)   | Return nodes with a value of `likes` predicate greater than 100.             |
| func: le(dislikes, 10) | Return nodes with a value of `dislikes` predicates less than or equal to 10. |

Now, guess the comparator function we should use to select `author nodes` with a
rating of 4.0 or more.

If you think it should be the `greater than or equal to(ge)` function, then
you're right!

Let's try it out.

```graphql
{
  best_authors(func: ge(rating, 4.0)) {
    uid
    author_name
    rating
  }
}
```

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-index-missing.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=833580f2c2348e4e9f2ca6410125c7b5" alt="index missing" width="854" height="431" data-path="images/dgraph/guides/get-started-with-dgraph/b-index-missing.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-index-missing.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=02f3aa99c75e5ab7aabed5125c60de61 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-index-missing.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=f072fd74e39bf4e8675e11322d3b07e1 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-index-missing.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=ddc94177a5349e6b5b083b1e47165317 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-index-missing.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=d4a348f305794b85e7298d31e485b8d8 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-index-missing.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=f17320cdff56c2ca5bf690aba2115a3a 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-index-missing.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=12c67fe6463f0b78ce4a13f61af43752 2500w" data-optimize="true" data-opv="2" />

We got an error! The index for the `rating` predicate is missing. You can't
query for the value of a predicate unless you've added an index for it.

Let's learn more about indexes in Dgraph and also how to add them.

## Indexing in Dgraph

Indexes are used to speed up your queries on predicates. They have to be
explicitly added to a predicate when required (only when you need to query for
the value of a predicate).

Also, there's no need to anticipate the indexes to be added right at the
beginning. You can add them as you go along.

Dgraph offers different types of indexes. The choice of index depends on the
data type of the predicate.

Here is the table containing data types and the set of indexes that can be
applied to them.

| Data type  | Available index types                          |
| ---------- | ---------------------------------------------- |
| `int`      | `int`                                          |
| `float`    | `float`                                        |
| `string`   | `hash`, `exact`, `term`, `fulltext`, `trigram` |
| `bool`     | `bool`                                         |
| `geo`      | `geo`                                          |
| `dateTime` | `year`, `month`, `day`, `hour`                 |

Only `string` and `dateTime` data types have an option for more than one index
type.

Let's create an index on the rating predicate. Ratel UI makes it super simple to
add an index.

Here's the sequence of steps:

* Go to the schema tab on the left.
* Click on the `rating` predicate from the list.
* Tick the index option in the Properties UI on the right.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-add-schema.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=3fb2b4a6b7c2d4066a6375ceac3ff389" alt="Add schema" width="854" height="402" data-path="images/dgraph/guides/get-started-with-dgraph/c-add-schema.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-add-schema.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=37d014a83399d151a9d8e12e91cc53c1 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-add-schema.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=863deb82f0b1163c63b5108eb14d3f83 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-add-schema.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=f29f36e7b6c6ce8029f8ee6a64982242 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-add-schema.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=53bba2812e6626e27f916459432415a6 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-add-schema.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=27b75721037b5827e8edaba2266915b9 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-add-schema.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=706b21105e50ee285e45e2eea4c5902f 2500w" data-optimize="true" data-opv="2" />

We successfully added the index for `rating` predicate! Let's rerun our previous
query.

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-rating-query.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=60667acafabf6c4a873416ac8618f2b7" alt="rating" width="854" height="338" data-path="images/dgraph/guides/get-started-with-dgraph/d-rating-query.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-rating-query.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=784859b6b5707072a0391cc781440ac4 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-rating-query.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=6967513b2634c27c05d8c00019da0812 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-rating-query.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=c2ef4ec09f6eccf6c4d5b10c91c8ddc5 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-rating-query.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=e20886f138f5502174a3eafa52bba469 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-rating-query.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=7fc3a9113b3adfaf33a89b44b74520f6 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-rating-query.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=f4d6f245ec11fe9c490c54cf6b12d0a0 2500w" data-optimize="true" data-opv="2" />

We successfully queried for Author nodes with a rating of 4.0 or more. How about
we also fetch the Blog posts of these authors?

We already know that the `published` edge points from an `author` node to a
`blog post` node. So fetching the blog posts of the `author` nodes is simple. We
need to traverse the `published` edge starting from the `author` nodes.

```graphql
{
  authors_and_ratings(func: ge(rating, 4.0)) {
    uid
    author_name
    rating
    published {
      title
      content
      dislikes
    }
  }
}
```

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-rating-blog.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=15d6c02bd373d79e60c8d4388fca9981" alt="rating-blog-rating" width="854" height="424" data-path="images/dgraph/guides/get-started-with-dgraph/e-rating-blog.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-rating-blog.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=c9ddb7da09e0f7742731b6f6e16076b1 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-rating-blog.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=a3fb896bc8d3ebacbb23cf14d6a6e41b 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-rating-blog.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=10f83fe1e451febe4eca2b8a569a0ab9 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-rating-blog.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=f66fda33f32c615a99b7766fe48ee5b8 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-rating-blog.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=8d4da009c609335ed4acf59d86111790 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-rating-blog.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=3d9a14b46eb40ec17d04f2e2d1381b49 2500w" data-optimize="true" data-opv="2" />

*Check out our [previous tutorial](./basic-operations) if you have questions
around graph traversal queries.*

Similarly, let's extend our previous query to fetch the tags of these blog
posts.

```graphql
{
  authors_and_ratings(func: ge(rating, 4.0)) {
    uid
    author_name
    rating
    published {
      title
      content
      dislikes
      tagged {
        tag_name
      }
    }
  }
}
```

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-four-blogs.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=df81b7ed31a8bab8b8b3261591fc79ee" alt="rating-blog-rating" width="854" height="428" data-path="images/dgraph/guides/get-started-with-dgraph/m-four-blogs.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-four-blogs.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=ac33fc9ac9ebb209dadfa425e944f9fe 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-four-blogs.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=b1c750e2beb54548c13d85337cfde418 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-four-blogs.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=29d4f09c3d172848c07a96bbcdfb48b8 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-four-blogs.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=adfde1babf9ada1ee9a737a033557248 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-four-blogs.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=8224c8f2199a680facd9df7d083f8bf9 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-four-blogs.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=d7c81a7fcd4a4163e29b3a9634556653 2500w" data-optimize="true" data-opv="2" />

Note: author nodes are in blue, blogs posts in green, and tags in pink.

There are two authors, four blog posts, and their tags in the result. If you
take a closer look at the result, there's a blog post with 12 dislikes.

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-dislikes-2.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=a7e2b1d4d6a03163a63f9260f14724d7" alt="Dislikes" width="854" height="459" data-path="images/dgraph/guides/get-started-with-dgraph/i-dislikes-2.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-dislikes-2.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=de1115ab982452b2a9579825283a8ca0 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-dislikes-2.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=59d413861ae00904f11de35a10f9186f 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-dislikes-2.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=7cef27e05fbbb0f8bc341017548b51a5 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-dislikes-2.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=6d4f87144b82db4fb91c84c00d06cd04 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-dislikes-2.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=5aa53116e431cf5b3fd49178e87e2bf1 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-dislikes-2.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=933c7a10f4474c8af8e55abf5c58d35f 2500w" data-optimize="true" data-opv="2" />

Let's filter and fetch only the popular blog posts. Let's query for only those
blog posts with fewer than 10 dislikes.

To achieve that, we need to express the following statement as a query to
Dgraph:

*Hey, traverse the `published` edge, but only return those blogs with fewer than
10 dislikes*

Can we also filter the nodes during traversals? Yes, we can! Let's learn how to
do that in our next section.

## Filtering traversals

We can filter the result of traversals by using the `@filter` directive. You can
use any of the Dgraph's comparator functions with the `@filter` directive. You
should use the `lt` comparator to filter for only those blog posts with fewer
than 10 dislikes.

Here's the query.

```graphql
{
  authors_and_ratings(func: ge(rating, 4.0)) {
    author_name
    rating

    published @filter(lt(dislikes, 10)) {
      title
      likes
      dislikes
      tagged {
        tag_name
      }
    }
  }
}
```

The query returns:

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/n-three-blogs.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=f7a5a4aa4059da8fcaabff379a4cb4ef" alt="rating-blog-rating" width="854" height="423" data-path="images/dgraph/guides/get-started-with-dgraph/n-three-blogs.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/n-three-blogs.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=370a2d19b75c501cb5b8ca6db9c20211 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/n-three-blogs.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=1582b0dd3aaf23d89059ff3acb218e11 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/n-three-blogs.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=17dfa6af0705e947d8ba23553fd3d7f4 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/n-three-blogs.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=d93e891ace6fd21415129d87dd18b40e 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/n-three-blogs.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=9973401aa66e074a25c530ff21958002 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/n-three-blogs.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=76d21b1efdb5e8179a94a8f253f7f0fb 2500w" data-optimize="true" data-opv="2" />

Now, we only have three blogs in the result. The blog with 12 dislikes is
filtered out.

Notice that the blog posts are associated with a series of tags.

Let's run the following query and find all the tags in the database.

```sh
{
  all_tags(func: has(tag_name)) {
    tag_name
  }
}
```

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/o-tags.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=b6ebf1349dee64dd809dad5bb7418533" alt="tags" width="834" height="480" data-path="images/dgraph/guides/get-started-with-dgraph/o-tags.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/o-tags.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=939df625995bd5f28c82352faea31c03 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/o-tags.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=aef74debb492e2fbf93c6cb1a722bede 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/o-tags.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=b573792c4c382165fdcf47e52cafa48e 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/o-tags.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=a24d4f604177307282d3842ee54fe510 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/o-tags.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=c3d7adb2665ca4fc1d0c86a8c05f4cad 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/o-tags.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=69100d8fb899ba5a5e4784dd7fd60f95 2500w" data-optimize="true" data-opv="2" />

We got all the tags in the database.

In our next section, let's find all the blog posts which are tagged `devrel`.

## Querying string predicates

The `tag_name` predicate represents the name of a tag. It is of type `string`.
Here are the steps to fetch all blog posts which are tagged `devrel`.

* Find the root node with the value of `tag_name` predicate set to `devrel`. We
  can use the `eq` comparator function to do so.
* Don't forget to add an index to the `tag_name` predicate before you run the
  query.
* Traverse starting from the node for `devrel` tag along the `tagged` edge.

Let's start by adding an index to the `tag_name` predicate. Go to Ratel, click
`tag_name` predicate from the list.

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/p-string-index-2.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=3420784d50ae72634f28eaca74fcaf9f" alt="string index" width="854" height="422" data-path="images/dgraph/guides/get-started-with-dgraph/p-string-index-2.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/p-string-index-2.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=3689f500083354c5372a532bc5908fb0 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/p-string-index-2.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=79d0e4ef7786e3b26e0ffa24033f86d2 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/p-string-index-2.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=10a8704ee40a73f270674361bda45062 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/p-string-index-2.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=716bb4a7956e353cf560275824bffba3 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/p-string-index-2.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=bac6a9392e1c27477095ab1b8e4316e6 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/p-string-index-2.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=199b2e882f50b03cf404f214df65b42d 2500w" data-optimize="true" data-opv="2" />

You can see that there are five choices for indexes that can be applied to any
`string` predicate. The `fulltext`, `term`, and `trigram` are advanced string
indexes. We'll discuss them in detail in our next episode.

There are a few constraints around the use of string type indexes and the
comparator functions.

For example, only the `exact` index is compatible with the `le`, `ge`,`lt`, and
`gt` built-in functions. If you set a string predicate with any other index and
run the these comparators, the query fails.

Although, any of the five string type indexes are compatible with the `eq`
function, the `hash` index used with the `eq` comparator would normally yield
the best performance.

Let's add the `hash` index to the `tag_name` predicate.

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-hash.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=0efc21669f1c48e41828a7f31ac5c0fb" alt="string index" width="854" height="460" data-path="images/dgraph/guides/get-started-with-dgraph/m-hash.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-hash.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=98a96c832ab0d9c009bfd87c7e169f6f 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-hash.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=ce1d634be92c2c9413e12aefabdc76b8 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-hash.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=fe1357a313d0d45734658fd86a1c7233 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-hash.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=05508845df0284f4403d15981c0bb8a2 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-hash.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=a51597be054892ffba2f2c846ab65f5c 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-hash.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=a2da7b307f8c798caf172f096c8c3b13 2500w" data-optimize="true" data-opv="2" />

Let's use the `eq` comparator and fetch the root node with `tag_name` set to
`devrel`.

```graphql
{
  devrel_tag(func: eq(tag_name,"devrel")) {
    tag_name
  }
}
```

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/q-devrel-2.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=5a1fd876a142362601d3983f38d73293" alt="string index" width="851" height="480" data-path="images/dgraph/guides/get-started-with-dgraph/q-devrel-2.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/q-devrel-2.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=96cbfcf168c480051d859497c85c4f1b 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/q-devrel-2.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=309d83ca1b7ffdc63a5e921c7221fad7 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/q-devrel-2.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=b892267b02b43a220b36d8c8151e1020 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/q-devrel-2.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=c792fcc17ea6bcbc7533d3e547d5ac42 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/q-devrel-2.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=07d57d684972778790061cf6fdda158c 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/q-devrel-2.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=fb6d846f489234cc7e080441f9f78d1a 2500w" data-optimize="true" data-opv="2" />

We finally have the node we wanted!

We know that the `blog post` nodes are connected to their `tag nodes` via the
`tagged` edges. Do you think that a traversal from the node for `devrel` tag
should give us the blog posts? Let's try it out!

```graphql
{
  devrel_tag(func: eq(tag_name,"devrel")) {
    tag_name
      tagged {
        title
        content
    }
  }
}
```

Looks like the query didn't work! It didn't return us the blog posts! Don't be
surprised as this is expected.

Let's observe our Graph model again.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-main-graph.JPG?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=191d03ed02e9a0502cbec6104bcd27dc" alt="main graph model" width="854" height="463" data-path="images/dgraph/guides/get-started-with-dgraph/a-main-graph.JPG" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-main-graph.JPG?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=8fd563c1136bfb0b0165780013acdbe8 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-main-graph.JPG?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=7692bde4511d5038ad1bc635fab1ea84 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-main-graph.JPG?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=c321c14ed2dba864cfca94a273064e5a 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-main-graph.JPG?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=80382189feee11d5caf9d9344572d14f 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-main-graph.JPG?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=d23c82e9b8f4dad01e1534ad674dc261 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-main-graph.JPG?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=4455d33516d8ddc4a76fcf9b616d7508 2500w" data-optimize="true" data-opv="2" />

We know that the edges in Dgraph have directions. You can see that the `tagged`
edge points from a `blog post` node to a `tag` node.

Traversing along the direction of an edge is natural to Dgraph. Hence, you can
traverse from any `blog post node` to its `tag node` via the `tagged` edge.

But to traverse the other way around requires you to move opposite to the
direction of the edge. You can still do so by adding a tilde(~~) sign in your
query. The tilde(~~) has to be added at the beginning of the name of the edge to
be traversed.

Let's add the `tilde (~)` at the beginning of the `tagged` edge and initiate a
reverse edge traversal.

```graphql
{
  devrel_tag(func: eq(tag_name,"devrel")) {
    tag_name

    ~tagged {
      title
      content
    }
  }
}
```

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/r-reverse-2.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=d59b3bd08e9512dee7e6a942e38dd40e" alt="string index" width="854" height="325" data-path="images/dgraph/guides/get-started-with-dgraph/r-reverse-2.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/r-reverse-2.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=74ff93df38aefe1220442c59f2c4da8a 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/r-reverse-2.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=04ae18d2407110210292ff12d45155f3 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/r-reverse-2.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=4dbede3d6c3bc2268be97010a21c2a6e 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/r-reverse-2.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=f3aa33faa49c934c73c03c2c8832dde2 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/r-reverse-2.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=9e8dda3a9caba3a2e5d4db52dfed0de0 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/r-reverse-2.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=e68ae76f9cfcf9b4d0347f97ec3fbf7e 2500w" data-optimize="true" data-opv="2" />

We got an error!

Reverse traversals require an index on their predicate.

Let's go to Ratel and add the `reverse` index to the edge.

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/r-reverse-1.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=c7dd5af1ae775e13a9274a1509ccdcdb" alt="string index" width="854" height="457" data-path="images/dgraph/guides/get-started-with-dgraph/r-reverse-1.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/r-reverse-1.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=4fe697ddcbb8231eabfc96637a052aa3 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/r-reverse-1.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=3f8bbf5915d22dac32eaee0ba765ddcb 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/r-reverse-1.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=84f079cacdbb46e4914a35df6e38d2f2 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/r-reverse-1.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=44f99a3c465a11408406f0a3675ff84c 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/r-reverse-1.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=e76840a2abebd8f0ce37d9ae3ac3c5dc 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/r-reverse-1.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=4f2d276caa9ba0860f3e9ac3d5e221fc 2500w" data-optimize="true" data-opv="2" />

Let's re-run the reverse edge traversal.

```graphql
{
  devrel_tag(func: eq(tag_name, "devrel")) {
    tag_name

    ~tagged {
      title
      content
    }
  }
}
```

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/s-devrel-blogs.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=91119d1c5712da709dbfd4f88a6115cf" alt="UID index" width="768" height="480" data-path="images/dgraph/guides/get-started-with-dgraph/s-devrel-blogs.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/s-devrel-blogs.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=4bdc70ea4a0ff398b672b4f4d749cedf 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/s-devrel-blogs.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=629be6deceef4060c77fc45b7f2e15ef 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/s-devrel-blogs.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=3caf6804a8bf9f603f6b7f115efc043d 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/s-devrel-blogs.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=95915ad8344d9eb1fb3220a7cef0b1d5 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/s-devrel-blogs.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=e265dd365fd569fee7dc7f10f5eed235 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/s-devrel-blogs.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=416eeac4b115863e03e28ebbcad33be4 2500w" data-optimize="true" data-opv="2" />

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/s-devrel-blogs-2.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=e39538f3ac0b920cb2fbfd350fe7cec7" alt="UID index" width="787" height="480" data-path="images/dgraph/guides/get-started-with-dgraph/s-devrel-blogs-2.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/s-devrel-blogs-2.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=2c8fb7106443da9c2a05ffa1967fe813 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/s-devrel-blogs-2.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=437d5ef0a937e1b061b2681c4a34dfed 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/s-devrel-blogs-2.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=b9e3b702b8d2e6170da60b502ccd21a2 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/s-devrel-blogs-2.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=27d2c7760b99131fd6e547f02eea2b2e 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/s-devrel-blogs-2.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=0500f7f5f99976fc5f38aaed83e2c019 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/s-devrel-blogs-2.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=20a8dba05081f02aeffa28ffda51e6d0 2500w" data-optimize="true" data-opv="2" />

Phew! Now we got all the blog posts that are tagged `devrel`.

Similarly, you can extend the query to also find the authors of these blog
posts. It requires you to reverse traverse the `published` predicate.

Let's add the reverse index to the `published` edge.

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/t-reverse-published.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=27a96e2104d426159572322f753ecfc2" alt="UID index" width="854" height="428" data-path="images/dgraph/guides/get-started-with-dgraph/t-reverse-published.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/t-reverse-published.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=2090f2e12af7071ad2ff783b11dbc889 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/t-reverse-published.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=5d9103b6f1ed111d97dd569c6b53446d 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/t-reverse-published.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=223cbd6dacc2f9cdbc414215e6afd580 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/t-reverse-published.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=5e30d6b12ca62dcd60bc8edaeea992a9 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/t-reverse-published.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=fe37c4f969da6725e3fdfbcf1f2231a4 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/t-reverse-published.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=2dfb99f3ea3ef09c6529f2346a745e22 2500w" data-optimize="true" data-opv="2" />

Now, let's run the following query.

```graphql
{
  devrel_tag(func: eq(tag_name,"devrel")) {
    tag_name

    ~tagged {
      title
      content

      ~published {
        author_name
      }
    }
  }
}
```

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/u-author-reverse-1.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=7df3f756e625c9a9cf39825a9b857b4b" alt="UID index" width="805" height="480" data-path="images/dgraph/guides/get-started-with-dgraph/u-author-reverse-1.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/u-author-reverse-1.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=ffc22a64c9f9a21984be31b67aa1238f 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/u-author-reverse-1.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=2e0db4cd1e34ca6032baf0d5de5eb551 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/u-author-reverse-1.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=8752750ec5baa51bb55fa25d06490afb 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/u-author-reverse-1.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=ad3d131bb0659b723cb0f7af26cf0b5a 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/u-author-reverse-1.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=01d84488d9fb969638ab5c70fef23fa8 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/u-author-reverse-1.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=c6e12f23c982823e11135a8cc267c3f6 2500w" data-optimize="true" data-opv="2" />

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/u-author-reverse-2.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=c2c79158c48495f99a842de19a41b16e" alt="UID index" width="796" height="480" data-path="images/dgraph/guides/get-started-with-dgraph/u-author-reverse-2.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/u-author-reverse-2.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=95e043e0d1e63f38c161ee28632e8dce 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/u-author-reverse-2.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=fcabde6d28fe6e2ebea39e9353c393c4 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/u-author-reverse-2.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=7d0e7c68ce5f8aa5bdddd4b0043d626b 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/u-author-reverse-2.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=88e355d832ed7afe5c8aabcf5a0e13e6 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/u-author-reverse-2.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=75d1f5006ec5a4c5705bfffdb53327c6 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/u-author-reverse-2.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=a5edd460d1f22c2213dfbe76edfc9476 2500w" data-optimize="true" data-opv="2" />

With our previous query, we traversed the entire graph in reverse order.
Starting from the tag nodes, we traversed up to the author nodes.

## Summary

In this tutorial, we learned about basic types, indexes, filtering, and reverse
edge traversals.

Before we wrap up, here’s a sneak peek into our next tutorial.

Did you know that Dgraph offers advanced text search capabilities? How about the
geo-location querying capabilities?

Sounds interesting?

Check out our next tutorial of the getting started series
[here](./multi-language-strings).

## Need help

* Please use [discuss.hypermode.com](https://discuss.hypermode.com) for
  questions, feature requests, bugs, and discussions.
