# Source: https://docs.hypermode.com/dgraph/guides/message-board-app/graphql/design-app-schema.md

# Design a Schema for the App

> Build a Message Board App in React with Dgraph Learn. Step 2: GraphQL schema design - how graph schemas and graph queries work.

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

In this section, you'll start designing the schema of the message board app and
look at how graph schemas and graph queries work.

To design the schema, you won't think in terms of tables or joins or documents,
you'll think in terms of entities in your app and how they're linked to make a
graph. Any requirements or design analysis needs iteration and thinking from a
number of perspectives, so you'll work through some of that process and sketch
out where you are going.

Graphs tend to model domains like your app really nicely because they naturally
model things like the subgraph of a `user`, their `posts`, and the `comments` on
those posts, or the network of friends of a user, or the kinds of posts a user
tends to like.

## UI requirements

Most apps are more than what you can see on the screen, but UI is what you are
focusing on here, and thinking about the UI you want to kick-off your design
process. So, let's at start by looking at what you would like to build for your
app's UI

Although a single GraphQL query can save you lots of calls and return you a
subgraph of data, a complete page might be built up of blocks that have
different data requirements. For example, in a sketch of your app's UI you can
already see these data requirements forming.

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/message-board-app/UI-components.gif?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=307284203e5107be5dab5cbd790bfd08" alt="App UI requirements" width="1600" height="900" data-path="images/dgraph/guides/message-board-app/UI-components.gif" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/message-board-app/UI-components.gif?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=abacd2430129dd9e199c45e64b7093f4 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/message-board-app/UI-components.gif?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=1069874a1bf8ee37ce5c252f11c92e9a 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/message-board-app/UI-components.gif?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=012565d8a3ae214dffebc796a64fd878 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/message-board-app/UI-components.gif?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=4c5673066881f8886e8d6c340da3260a 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/message-board-app/UI-components.gif?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=548e0d6015a2dd32e47c305dc49a9114 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/message-board-app/UI-components.gif?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=564f2fc3d323cbee67cea3bd90dc4b89 2500w" data-optimize="true" data-opv="2" />

You can start to see the building blocks of the UI and some of the entities
(users, categories, and posts) that will form the data in your app.

## Thinking in graphs

Designing a graph schema is about designing the things, or entities, that form
nodes in the graph, and designing the shape of the graph, or what links those
entities have to other entities.

There's really two concepts in play here. One is the data itself, often called
the app data graph. The other is the schema, which is itself graph shaped but
really forms the pattern for the data graph. You can think of the difference as
somewhat similar to objects (or data structure definitions) versus instances in
a program, or a relational database schema versus rows of actual data.

Already you can start to tease out what some of the types of data and
relationships in your graph are. There's users who post posts, so you know
there's a relationship between users and the posts they've made. You know the
posts are going to be assigned to some set of categories and that each post
might have a list of comments posted by users.

So your schema is going to have these kinds of entities and relationships
between them.
<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/schema-inital-sketch.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=ab454dbae449d6bb5e4bf35dc556a70f" alt="Graph schema sketch" width="3200" height="1800" data-path="images/dgraph/guides/message-board-app/schema-inital-sketch.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/schema-inital-sketch.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=48ae42b0a911ce78bed3b7cfafaa82fc 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/schema-inital-sketch.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=30f8c30da2f36dcabc4d84d5f4d8019b 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/schema-inital-sketch.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=8d6ebf570a79d9c993951c54ea8e3eb4 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/schema-inital-sketch.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=741c8913defc33a127755234025c1422 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/schema-inital-sketch.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=dc65d22fb6a526a726f636a2586dbedc 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/schema-inital-sketch.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=a7e2f3080e2a4250212a513a96512a84 2500w" data-optimize="true" data-opv="2" />

I've borrowed some notation from other data modeling patterns here. That's
pretty much the modeling capability GraphQL allows, so let's start sketching
with it for now.

A `user` is going to have some number of `posts` and a `post` can have exactly
one `author`. A `post` can be in only a single `category`, which, in turn, can
contain many `posts`.

How does that translate into the app data graph? Let's sketch out some examples.

Let's start with a single user who's posted three posts into a couple of
different categories. Your graph might start looking like this.

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/first-posts-in-graph.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=2b37c80b26395d3b7047f9d469c56044" alt="first-posts-in-graph" width="3200" height="1800" data-path="images/dgraph/guides/message-board-app/first-posts-in-graph.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/first-posts-in-graph.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=586224b10698e860ceab47e932b65ae9 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/first-posts-in-graph.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=fd3bf29b0ffbb5e3fe5109b3321714d5 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/first-posts-in-graph.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=786327f2ee124c2d28acbfc7ef58146e 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/first-posts-in-graph.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=a253775412422b423f0cf60c77efd04d 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/first-posts-in-graph.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=6246ba9a945294458bfe5bc49e7e47bd 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/first-posts-in-graph.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=9e55377d129f69e2400a0995a9391cce 2500w" data-optimize="true" data-opv="2" />

Then another user joins and makes some posts. Your graph gets a bit bigger and
more interesting, but the types of things in the graph and the links they can
have follow what the schema sets out as the pattern --- for example you aren't
linking users to categories.
<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/user2-posts-in-graph.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=bdd1250e2d55923a8b00ee1b246aa492" alt="more users and posts" width="3200" height="1800" data-path="images/dgraph/guides/message-board-app/user2-posts-in-graph.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/user2-posts-in-graph.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=1af1b32894a4a54a2c2dd42231f1f936 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/user2-posts-in-graph.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=3b69499301041fc6891db22a8e47a4a5 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/user2-posts-in-graph.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=dce9157187a59ee25a6e1a434e8746c9 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/user2-posts-in-graph.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=c23bfc9b6d6e05fcaedda64de9f55435 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/user2-posts-in-graph.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=772b5e0564f6aa991c3d6d9bc216f82b 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/user2-posts-in-graph.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=0a0715ccaabf9a3bd0ca2c075457701d 2500w" data-optimize="true" data-opv="2" />

Next the users read some posts and start making and replying to comments.
<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/comments-in-graph.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=74198661b0934cacb1f00572006fe3dd" alt="users, posts and comments" width="3200" height="1800" data-path="images/dgraph/guides/message-board-app/comments-in-graph.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/comments-in-graph.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=dcb799757bf60390d69256ace19e90e0 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/comments-in-graph.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=f99ed9ae4d46f95ac5a15074fee82b38 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/comments-in-graph.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=7bd8f66d79dca4f76c3a6b9bccaf4f6d 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/comments-in-graph.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=5342dad3820f3932723fc231422c7a8b 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/comments-in-graph.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=780f5e3e0c238313f422385bc9450f5e 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/comments-in-graph.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=86a22fde66d9f970cc9f4c5ae7e53e0e 2500w" data-optimize="true" data-opv="2" />

Each node in the graph has the data (a bit like a document) that the schema says
it can have, such as a username for users and title, text and date published for
posts, and the links to other nodes (the shape of the graph).

While you are still sketching things out here, let's take a look at how queries
work.

## How graph queries work

Graph queries in GraphQL are really about entry points and traversals. A query
picks certain nodes as a starting point and then selects data from the nodes or
follows edges to traverse to other nodes.

For example, to render a user's information, you might need only to find the
user. So your use of the graph might be like in the following sketch --- you'll
find the user as an entry point into the graph, perhaps from searching users by
username, query some of their data, but not traverse any further.
<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/user1-search-in-graph.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=8893b51f2aae6b1109b541c9ba2ace1b" alt="query a user" width="3200" height="1800" data-path="images/dgraph/guides/message-board-app/user1-search-in-graph.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/user1-search-in-graph.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=386b024458cb06ea11c13f1892a5682f 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/user1-search-in-graph.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=db081cd27e08ae40c917860825bd0884 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/user1-search-in-graph.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=35b2717911ee401e9763341e2d9a4202 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/user1-search-in-graph.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=4c4eee94851137cc1cae92affff0652e 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/user1-search-in-graph.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=da1e6c07b0561e8747356810a094819e 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/user1-search-in-graph.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=2d52ae89dde82b8d5837b7d34e98296e 2500w" data-optimize="true" data-opv="2" />

Often, though, even in just presenting a user's information, you need to present
information like most recent activity or sum up interest in recent posts. So
it's more likely that you'll start by finding the user as an entry point and
then traversing some edges in the graph to explore a subgraph of interesting
data. That might look like this traversal, starting at the user and then
following edges to their posts.

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/user1-post-search-in-graph.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=f3811b23540859efc0ca548ec4db437e" alt="query a user and their posts" width="3200" height="1800" data-path="images/dgraph/guides/message-board-app/user1-post-search-in-graph.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/user1-post-search-in-graph.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=43bd56502f257ef638670caa2a3100c2 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/user1-post-search-in-graph.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=099bfa1e314d1428ad5a0c989fe303c4 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/user1-post-search-in-graph.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=3d2e061e0d743c7d19b68598eeef818b 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/user1-post-search-in-graph.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=8c0da90d7652091259c247b5d2aa19ed 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/user1-post-search-in-graph.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=06e859b697a579ae6af7ca741c91a4ab 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/user1-post-search-in-graph.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=1d928b00c19185cb4dbb148bc543c3d1 2500w" data-optimize="true" data-opv="2" />

You can really start to see that traversal when it comes to rendering an
individual post. You'll need to find the post, probably by its id when a user
navigates to a url like `/post/0x2`, then you'll follow edges to the post's
author and category, but you'll also need to follow the edges to all the
comments, and from there to the authors of the comments. That'll be a multi-step
traversal like the following sketch.
<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/post2-search-in-graph.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=a70f72dbc0ff9cce48c0b87da309e27e" alt="query a post and follow edges" width="3200" height="1800" data-path="images/dgraph/guides/message-board-app/post2-search-in-graph.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/post2-search-in-graph.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=8ec080cbd03f370f92a435ee017d7125 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/post2-search-in-graph.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=ca05f84ff75dcd5b2e0f3c70d2b79a5c 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/post2-search-in-graph.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=7ce422d108ea5f89d8b7ce446109606b 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/post2-search-in-graph.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=b3d6081566bd87736c29a5b3fa9d9304 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/post2-search-in-graph.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=21994d953bcb2558a7721fbf4981e8c9 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/post2-search-in-graph.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=fdcd38250e93b03fe862180b571e00bc 2500w" data-optimize="true" data-opv="2" />

Graphs make these kinds of data traversals really clear, as compared to table
joins or navigating your way through a RESTful API. It can also really help to
jot down a quick sketch.

It is also possible for a query to have multiple entry points and traversals
from all of those entry points. Imagine, for example, the query that renders the
post list on the main page. That's a query that finds multiple posts, maybe
ordered by date or from particular categories, and then, for each, traverses to
the author, category, etc.

You can now begin to see the GraphQL queries needed to fill out the UI. For
example, in the sketch at the top, there is a query starting at the logged in
user to find their details, a query finding all the category nodes to fill out
the category dropdown, and a more complex query that finds a number of posts and
make traversals to find the posts' authors and categories.

## Schema

Now that you have investigated and considered what you are going to show for
posts and users, you can start to flesh out your schema some more.

Posts, for example, are going to need a title and some text for the post, both
string valued. Posts also need some sort of date to record when they were
uploaded. They'll also need links to the author, category, and a list of
comments.

The next iteration of your schema might look like this sketch.
<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/schema-sketch.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=d8580d4d83a5dbc186aaf3cf090c2a2c" alt="Graph schema sketch with data" width="3200" height="1800" data-path="images/dgraph/guides/message-board-app/schema-sketch.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/schema-sketch.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=58fc54b68c5729cb5b79b54363951f8c 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/schema-sketch.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=190511c77f796b1dcf022bb312ae6aca 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/schema-sketch.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=6d3335b36f2d12b93f571649b3667502 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/schema-sketch.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=265e9bc4d9d0d5b8d6194537c956a796 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/schema-sketch.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=0c1062a1d1a3b50d18888babd7eb6a7d 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/schema-sketch.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=54535d6a0f14bd86baa4eab341e2bf03 2500w" data-optimize="true" data-opv="2" />

That's your first cut at a schema --- the pattern your app data graph follows.

You'll keep iterating on this as you work through the tutorial, that's what
you'd do in building an app, no use pretending like you have all the answers at
the start. Eventually, you'll want to add likes and dislikes on the posts, maybe
also tags, and you'll also layer in a permissions system so some categories
require permissions to view. But, those topics are for later sections in the
tutorial. This is enough to start building with.

## What's next

Next you'll make your design concrete, by writing it down as a
[GraphQL schema](./graphql-schema), and upload that to Dgraph. That'll give you
a running GraphQL API and you'll look at the queries and mutations that form the
data of your app.
