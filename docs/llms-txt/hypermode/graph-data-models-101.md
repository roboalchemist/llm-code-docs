# Source: https://docs.hypermode.com/dgraph/guides/graph-data-models-101.md

# Graph Data Models 101

> Graphs provide an alternative to tabular data structures, allowing for a more natural way to store and retrieve data

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

When building an app, you might wonder which database is the best choice. A
traditional relational database that you can query using SQL is a familiar
choice, but does a relational database really provide a natural fit to your data
model, and the performance that you need if your app goes viral and needs to
scale up rapidly?

This tutorial takes a deeper look at data modeling using relational databases
compared to graph databases like Dgraph, to give you a better understanding of
the advantages of using a graph database to power your app. If you aren't
familiar with graph data models or graph databases, this tutorial was written
for you.

## Learning goals

In this tutorial, you'll learn about graphs, and how a graph database is
different from a database built on a relational data model. This tutorial
doesn't include any code or syntax, but rather a comparison of graphs and
relational data models. By the end of this tutorial, you should be able to
answer the following questions:

* What's a graph?
* How are graphs different from relational models?
* How's data modeled in a graph?
* How's data queried from a graph?

Along the way, you might find that a graph is the right fit for the data model
used by your app. Any data model that tracks lots of different relationships (or
*edges*) between various data types is a good candidate for a graph model.

Whether this is the first time you are learning about graphs or looking to
deepen your understanding of graphs with some concrete examples, this tutorial
should help you along your journey.

If you are already familiar with graphs, you can jump right into our coding
example for [React](/dgraph/guides/message-board-app/introduction).

## Graphs and natural data modeling

Graphs provide an alternative to tabular data structures, allowing for a more
natural way to store and retrieve data.

For example, you could imagine that we're modeling a conversation within a
family:

* A `father`, who starts a conversation about going to get ice cream.
* A `mother`, who comments that she would also like ice cream.
* A `child`, who likes the idea of the family going to get ice cream.

This conversation could easily occur in the context of a modern social media or
messaging app, so you can imagine the data model for such an app as follows:

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-3.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=07173adcf027c36f1e34531874a50cae" alt="A graph diagram for a social media app's data model" width="1080" height="387" data-path="images/dgraph/guides/data-model-101/evolution-3.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-3.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=e9fd4d456c65cd9e3b478c093771af73 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-3.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=65bbccc807fbd19fd16f6f4af01314e7 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-3.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=08f9b370747ac46b1ffe87cd991c25fe 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-3.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=c4762f6b80466fca71e0c5acf37add26 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-3.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=055c4801105840e47b5a91479bef1a5e 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-3.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=bea246509fc2946a27f6b67a9f65302e 2500w" data-optimize="true" data-opv="2" />

For the remainder of this guide, we use this as our example app: a basic social
media or messaging app, with a data model that includes `people`, `posts`,
`comments`, and `reactions`.

A graph data model is different from a relational model. A graph focuses on the
relationships between information, whereas a relational model focuses on storing
similar information in a list. The graph model received its name because it
resembles a graph when illustrated.

* Data objects are called *nodes* and are illustrated with a circle.
* Properties of nodes are called *predicates* and are illustrated as a panel on
  the node.
* Relationships between nodes are called *edges* and are illustrated as
  connecting lines. Edges are named to describe the relationship between two
  nodes. A `reaction` is an example of an edge, in which a person reacts to a
  post.

Some illustrations omit the predicates panel and show only the nodes and edges.

Referring back to the example app, the `father`, `mother`, `child`, `post`, and
`comment` are nodes. The name of the people, the post's title, and text of the
comment are the predicates. The natural relationships between the authors of the
posts, authors of the comments, and the comments' topics are edges.

As you can see, a graph models data in a natural way that shows the
relationships (edges) between the entities (nodes) that contain predicates.

## Relational Data Modeling

This section considers the example social media app introduced in the previous
section and discusses how it could be modeled with a traditional relational data
model, such as those used by SQL databases.

With relational data models, you create lists of each type of data in tables,
and then add columns in those tables to track the attributes of that table's
data. Looking back on our data, we remember that there are three main types,
`People`, `Posts`, and `Comments`

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-4.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=1847d282c9783bc990326dbbca9073dd" alt="Three tables" width="1080" height="336" data-path="images/dgraph/guides/data-model-101/evolution-4.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-4.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=230419f17ba12a7d618e2cedd71e56bf 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-4.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=07c25f7e448686171461303e4b97d398 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-4.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=880778d15cb6b98c8000071279a28b8e 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-4.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=22316a34d1c6c009cf73207e3ebf841c 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-4.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=6110f4c1fa40f781614a6d9a5308add4 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-4.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=275ef20115dfc6268ccdac6f5937e743 2500w" data-optimize="true" data-opv="2" />

To define relationships between records in two tables, a relational data model
uses numeric identifiers called *foreign keys*, that take the form of table
columns. Foreign keys can only model one-to-many relationship types, such as the
following:

* The relationship from `Posts` to `People`, to track contributors (authors,
  editors, etc.) of a `Post`
* The relationship from `Comments` to `People`, to track the author of the
  comment
* The relationship from `Comments` to `Posts`, to track on which post comments
  were made
* The relationship between rows in the `Comments` table, to track comments made
  in reply to other comments (a self-reference relationship)

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-5.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=cf758d0d45cc09d85459920264a94830" alt="Relationships between rows in tables" width="1080" height="336" data-path="images/dgraph/guides/data-model-101/evolution-5.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-5.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=a493d61a600a0a8521b71b1f43d03fe8 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-5.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=a8adb6122ae91e33329a2633abc1029c 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-5.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=1fd3fe5c198a6a17bad86c6fa88c6df4 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-5.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=dd1ab058a15dac6e8ad99a7cf45717c4 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-5.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=3a1df3efc821386ed846afcf2d8d30b0 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-5.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=e6f76c852de8fd133f0ad33aa3914c75 2500w" data-optimize="true" data-opv="2" />

The limitations of foreign keys become apparent when your app requires you to
model many-to-many relationships. In our example app, a person can like many
posts or comments, and posts and comments can be liked by many people. The only
way to model this relationship in a relational database is to create a new
table. This so-called *pivot table* usually doesn't store any information
itself, it just stores links between two other tables.

In our example app, we decided to limit the number of tables by having a single
“Likes” table instead of having `people_like_posts` and `people_like_comments`
tables. None of these solutions is perfect, though, and there is a trade-off
between having a lower table count or having more empty fields in our tables
(also known as "sparse data").

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-6.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=3711cca6c0fd0114bdb94582a4adbca1" alt="An illustration of sparse data when creating a Likes table" width="1080" height="336" data-path="images/dgraph/guides/data-model-101/evolution-6.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-6.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=2ce5705c3294d3b5f85b48b566c7e0b1 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-6.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=e05a8ab9a3c64f09e433e472b51e8f83 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-6.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=b6918c60b80ce8ead29eb027db043618 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-6.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=48124b21167c756c88009236d8654224 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-6.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=c38f67aa1172508eae43e99938471a94 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-6.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=12ec9f47d0d6b8cfd04cdf9e49283f2b 2500w" data-optimize="true" data-opv="2" />

Because foreign keys can't be added in reference to entities that don't exist,
adding new posts and authors requires additional work. To add a new post and a
new author at the same time (in the Posts and People tables), we must first add
a row to the `People` table and then retrieve their primary key and associate it
with the new row in the `Posts` table.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-7.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=5de4fe4b0a3d3662049fb5827b00587f" alt="Adding a post and an author at the same time" width="1080" height="336" data-path="images/dgraph/guides/data-model-101/evolution-7.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-7.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=09d945fa441eec1ca2be58c92e6df633 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-7.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=c44376571dc3af2f43db9a2d29759f93 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-7.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=eceabe8c00c9167eea4c891d66d48a1c 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-7.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=7c1b0aadd5910002bd33895bfa350d2c 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-7.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=2d9824dedec610c4f45711473efa5b54 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-7.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=b59aa94af3434da7745c8f07a90a6282 2500w" data-optimize="true" data-opv="2" />

By now, you might ask yourself: how does a relational model expand to handle new
data, new types of data, and new data relationships?

When new data is added to the model, the model changes to accept the data. The
simplest type of change is when you add a new row to a table. The new row adopts
all of the columns from the table. When you add a new property to a table, the
model changes and adds the new property as a column on every existing and future
row for the table. And when you add a new data type to the database, you create
a new table with its own pre-defined columns. This new data type might link to
existing tables or need more pivot tables for a new many-to-many relationship.
So, with each data type added to your relational data model, the need to add
foreign keys and pivot tables increases, making support for querying every
potential data relationship increasingly unwieldy.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-8.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=8b854a98f382fac277f8daa918cb6ac7" alt="Expanding a relational data model means more pivot tables" width="1080" height="538" data-path="images/dgraph/guides/data-model-101/evolution-8.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-8.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=8ed094a175949b821fb4e7135225e343 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-8.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=d16fd9116e3d0eaeda7792eb970644ab 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-8.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=e3a00a15e1e892b36e810feecee85924 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-8.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=658f6870d215f189e8784ca8338a7856 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-8.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=77c1b133212af685d341a59a101461a4 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-8.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=7e2e7150fbc3b80840065c2d49c34d1b 2500w" data-optimize="true" data-opv="2" />

Properties are stored as new columns and relationships require new columns and
sometimes new pivot tables. Changing the schema in a relational model directly
effects the data that's held by the model, and can impact database query
performance.

## Graph Data Modeling

In this section we take our example social media app and see how it could be
modeled in a graph.

The concept of modeling data in a graph starts by placing dots, which represent
nodes. Nodes can have one or more predicates (properties). A `person` may have
predicates for their name, age, and gender. A `post` might have a predicate
value showing when it was posted, and a value containing the contents of the
post. A `comment` would most likely have a predicate containing the comment
string. However, any one node could have other predicates that aren't contained
on any other node. Each node represents an individual item, hence the singular
naming structure.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-9.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=5b2e5042a3a102e5b15bc8f0d485d521" alt="Nodes used in the example social media app" width="395" height="512" data-path="images/dgraph/guides/data-model-101/evolution-9.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-9.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=107a4931c1077a7b2a08b723b55c19fe 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-9.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=ba4f341023f3048af8d0c3b04ef401be 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-9.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=cc64189c7590efbebf839e5c067f7825 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-9.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=2fb0a5782e44fd25c109e5cf0ab6bc59 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-9.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=cfa0ca6575cbeb0063e5228794fc0a03 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-9.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=a5350d6c8daaec8ae3cfb6650d6f3726 2500w" data-optimize="true" data-opv="2" />

As graphs naturally resemble the data you are modeling, the individual nodes can
be moved around this conceptual space to clearly show the relationships between
these data nodes. Relationships are formed in graphs by creating an edge between
them. In our app, a post has an author, a post can have comments, a comment has
an author, and a comment can have a reply.

For sake of illustration we also show the family tree information. The `father`
and the `mother` are linked together with a `spouse` edge, and both parents are
related to the child along a `child` edge.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-10.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=e43872169967457c54b5c86ac2466116" alt="Illustration of relationships as edges" width="423" height="512" data-path="images/dgraph/guides/data-model-101/evolution-10.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-10.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=e54a871c02d9e6a5c0b8197813e21727 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-10.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=1e70a44441d70406f421068f2fec8953 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-10.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=31c2e89abddc6deb9cd66e3d714f1ede 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-10.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=9d9ba3f2d0dc607af5e9d43870672b42 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-10.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=75eff05b9ce01792dc845e699b4fedad 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-10.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=67cd7898dde319cb7e254ae5681daf07 2500w" data-optimize="true" data-opv="2" />

With a graph, you can also name the inverse relations. From here we can quickly
see the inverse relationships. A `Post` has an `Author` and a `Person` has
`Posts`. A `Post` has `Comments` and a `Comment` is on a `Post`. A `Comment` has
an `Author`, and a `Person` has `Comments`. A `Parent` has a `Child`, and a
`Child` has a `Parent`.

You create many-to-many relationships in the same way that you make one-to-many
relationships, with an edge between nodes.

Adding groups of related data occurs naturally within a graph. The data is sent
as a complete object instead of separate pieces of information that needs to be
connected afterwards. Adding a new person and a new post to our graph is a
one-step process. New data coming in doesn't have to be related to any existing
data. You can insert this whole data object with 3 people, a post, and a comment
all in one step.

When new data is added to the model, the model changes to accept the data. Every
change to a graph model is received naturally. When you add a new node with a
data type, you are simply creating a new dot in space and applying a type to it.
The new node doesn't include any predicates or relationships other than what you
define for it. When you want to add a new predicate onto an existing data type,
the model changes and adds the new property onto the items that you define.
Other items not specifically given the new property type aren't changed. When
you add a new data type to the database, a new node is created, ready to receive
new edges and predicates.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-11.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=6b1b268b8e40350c16a334165ccc51d0" alt="Illustration of expanding a graph data model" width="723" height="1080" data-path="images/dgraph/guides/data-model-101/evolution-11.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-11.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=b200dc5e7797c0ed592b899959b17ddc 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-11.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=892b951afb2a7816dadd6eaff5aecde0 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-11.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=1a9d41f8f93e601c64112547118c44c7 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-11.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=1c69e4812a700f833526049ad22ed54a 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-11.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=baa61f5d4842079a009e2f2530da64e7 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-11.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=ec884898f904ccf8ea117529af1ef5ce 2500w" data-optimize="true" data-opv="2" />

The key to remember when modeling a graph is to focus on the relationships
between nodes. In a graph you can change the model without affecting the
underlying data. Because the graph is stored as individual nodes, you can adjust
predicates of individual nodes, create edges between sets of nodes, and add new
node types without affecting any of the other nodes.

## Query Data in a Relational Model

Storing our data is great, but the best data model would be useless without the
ability to query the data our app requires. So, how does information get
retrieved in a relational model compared to a graph model?

In a relational model, tables are stored in files. To support the sample social
media app described in this tutorial, you would need four files: `People`,
`Posts`, `Comments`, and `Likes`.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-12.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=87011ff05777f2878c6ff6a63e05c0e4" alt="Visualization of four files" width="512" height="167" data-path="images/dgraph/guides/data-model-101/evolution-12.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-12.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=37030da0809194aefa5284885a7b1884 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-12.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=4d111d58b70bf2466cbe41409dcc2c4b 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-12.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=c6324c1180911387ecb9d9777d007f06 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-12.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=31052940f079e681ca7453c3b8b5ad57 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-12.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=41f989a9d892b4a0980e735443fbb9ca 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-12.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=6e68552e33bab7c6c914d1407ec97858 2500w" data-optimize="true" data-opv="2" />

When you request data from a file, one of two things happens: either a table
scan takes place or an index is invoked. To find this data, the whole file must
be read until the data is found or the end of the file is reached. In our
example app there is a post titled, “Ice Cream?”. If the title isn't indexed,
every post in the file would need to be read until the database finds the post
entitled, “Ice Cream?”. This method would be like reading the entire dictionary
to find the definition of a single word: very time-consuming. This process could
be optimized by creating an index on the post’s title column. Using an index
speeds up searches for data, but it can still be time-consuming.

### What's an index?

An index is an algorithm used to find the location of data. Instead of scanning
an entire file looking for a piece of data, an index is used to aggregate the
data into "chunks" and then create a decision tree pointing to the individual
chunks of data. Such a decision tree could look like the following:

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-13.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=5299ba7da64425fd3d5e073f6039d7ee" alt="Image showing a tree to lookup the term graph from an index. The tree should be in a “graph” type format with circles instead of squares." width="512" height="230" data-path="images/dgraph/guides/data-model-101/evolution-13.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-13.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=82b68857e0528313bf744a621df3f380 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-13.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=d29dcc4d4fea65cb28c940a20a55bdc9 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-13.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=d051ee2bcc3fd356e9b2323301286c2e 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-13.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=3aa884b198a88ee8261de349fe96c6ca 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-13.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=d5545b603901d4ab456c84a9ed73409e 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-13.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=ef19d399ba67feb1c63953747e4eee09 2500w" data-optimize="true" data-opv="2" />

Relational data models rely heavily on indexes to quickly find the requested
data. Because the data required to answer a single question usually lives in
multiple tables, you must use multiple indexes each time that related data is
joined together. And because you can't index every column, some types of queries
won't benefit from indexing.

### How data is joined in a relational model

In a relational model, the request's response must be returned as a single table
consisting of columns and rows. To form this single table response, data from
multiple tables must be joined together. In our app example, we found the post
entitled “Ice Cream?” and also found the comments, “Yes!”, “When?”, and “After
Lunch”. Each of these comments also has a corresponding author: `Mother`,
`Child`, and `Father`. Because there is only one post as the root of the join,
the post is duplicated to join to each comment.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-15.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=376376bd8e40725dd2e3425864cac7b7" alt="Joins in a relational model" width="1080" height="238" data-path="images/dgraph/guides/data-model-101/evolution-15.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-15.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=da9c3f6dcb22bc0b3cf3968f95b1e6f4 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-15.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=9ddb409f80ec4b79d923f733fb5f859e 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-15.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=f2978e649a12c561fda0ed9c3c608da6 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-15.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=f7497d42bf7295303a47f3ca28159cfe 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-15.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=3f0927d3f71f0d07705cac609c603a08 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-15.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=3ef999a606038358b1b9448cae0690c4 2500w" data-optimize="true" data-opv="2" />

Flattening query results can lead to many duplicate rows. Consider the case
where you also want to query which people liked the comments on this example
post. This query requires mapping a many-to-many relationship, which invokes two
additional index searches to get the list of likes by `person`.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-16.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=248210a7384635bf403b44d0e16ea13a" alt="Flattening in a relational model" width="1080" height="238" data-path="images/dgraph/guides/data-model-101/evolution-16.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-16.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=87c66d94c8cd212c6e091d0439c540a7 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-16.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=1ce7c90fa5a1d0d697d458b94af26ea3 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-16.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=661bc832b7e30e2ecedaa7823585fb47 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-16.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=523ce3b57a81a7989736c293170d47f8 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-16.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=a58af4c353c6434c07adc39e7d00c5e3 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-16.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=120d648422cbbd150f9b75987fc91854 2500w" data-optimize="true" data-opv="2" />

Joining all of this together would form a single table containing many
duplicates: duplicate `posts` and duplicate `comments`. Another side effect of
this response approach is that it's likely that empty data exists in the
response.

In the next section, you'll see that querying a graph data model avoids the
issues that you would face when querying a relational data model.

## Query Data in a Graph Model

As you'll see in this section, the data model we use determines the ease with
which we can query for different types of data. The more your app relies on
queries about the relationships between different types of data, the more you
benefit from querying data using a graph data model.

In a graph data model, each record (a `person`, `post` or `comment`) is stored
as a data *object* (sometimes also called a *node*). In the example social media
app described in this tutorial, there are objects for individual people, posts,
and comments.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-18.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=6476936e6425440ce97f5328fc6739ef" alt="Image of many objects of people, posts, and comments(not showing the relationships for clarity of the objects themselves)" width="1080" height="476" data-path="images/dgraph/guides/data-model-101/evolution-18.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-18.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=cee5ed384c33555a0accae5cf6494f0e 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-18.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=2f5628f4912a989641022e0d34346e91 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-18.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=fb0e613ef2aae91beaf1e5ec73150350 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-18.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=22837914bd185acd8f5ef2fdb04e0a19 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-18.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=ef653bc8eac67326901034b6bff80655 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-18.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=768fd73e57a0961a54869c1fda8ea34a 2500w" data-optimize="true" data-opv="2" />

When data is requested from the graph, a root function determines which nodes
are selected for the starting points. This root function uses indexes to
determine which nodes match quickly. In our app example, we want to start with
the root being the post with the title “Ice Cream?”. This type of lookup evokes
an index on the post's title, much like indexes work in a relational model. The
indexes at the root of the graph use the full index tree to find the data.

Connecting edges together to form a connected graph is called *traversal*. After
arriving at our `post`, “Ice Cream?”, we traverse the graph to arrive at the
post's `comments`. To find the post's `author`, we traverse the next step to
arrive at the people who authored the comment. This process follows the natural
progression of related data, and graph data models allow us to query our data to
follow this progression efficiently.

What do we mean by efficiently? A graph data model lets you traverse from one
node to a distantly related node without the need for anything like pivot
tables. This means that queries based on edges can be updated easily, with no
need to change the schema to support new many-to-many relationships. And, with
no need to build tables specifically for query optimization, you can adjust your
schema quickly to accommodate new types of data without adversely impacting
existing queries.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-19.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=083004596bfda00d08b2e431888b4b4d" alt="Image of post with connected comments and author" width="1080" height="476" data-path="images/dgraph/guides/data-model-101/evolution-19.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-19.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=2a54bf6af8ffedc3e7c299b6e34d23a0 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-19.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=a243d8fbc478a82e1e5d73201e8ddcb0 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-19.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=f58763d8086d0445ec2f69589e02f749 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-19.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=dc50e2b11c74bb3af85878d01eeda719 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-19.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=dcf975bc1e4984e605d85c6ab143f6f7 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-19.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=b4147996e89bf9c26f5b1c70c656a5ee 2500w" data-optimize="true" data-opv="2" />

A feature of a graph model is that related edges can be filtered anywhere within
the graph's traversing. When you want to know the most recent `comment` on your
post or the last `person` to like the comment, filters can be applied to the
edge.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-21.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=00f0f98ed536faef449880c2335e094f" alt="Image of filters along an edge" width="1080" height="476" data-path="images/dgraph/guides/data-model-101/evolution-21.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-21.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=aabd5b0638dc5f6dab5ba110c7c2fccb 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-21.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=9acd73434e68e80850fc7944aeb8aaaf 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-21.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=f57088e22b9cdfda9fac2ebfa253d113 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-21.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=6aa37ca3ec146a41c7d731e4c80d34de 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-21.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=3434abeb6c46310d865ece0eeeb946f3 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/data-model-101/evolution-21.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=0110fc8e2593fba36cd12e0857bae3d0 2500w" data-optimize="true" data-opv="2" />

When filters get applied along an edge, only the nodes that match the edge are
filtered - not all of the nodes in the graph. Applying this logic reduces the
size of the graph and makes index trees smaller. The smaller an index tree is,
the faster that it can be resolved.

In a graph model, data is returned in an object-oriented format. Any related
data is joined to its parent within the object in a nested structure.

```json
{
  "title": "IceCream?",
  "comments": [
    {
      "title": "Yes!",
      "author": {
        "name": "Mother"
      }
    },
    {
      "title": "When?",
      "author": {
        "name": "Child"
      }
    },
    {
      "title": "After Lunch",
      "author": {
        "name": "Father"
      }
    }
  ]
}
```

This object-oriented structure allows data to be joined without duplication.

## Conclusion

Congratulations on finishing the Dgraph learn course **Graph Data Models 101**!

Now that you have an overview and understanding of

* what a graph is
* how a graph differs from a relational model
* how to model a graph
* and how to query a graph

you are ready to jump into using Dgraph, the only truly native distributed graph
database.
