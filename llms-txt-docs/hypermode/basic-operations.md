# Source: https://docs.hypermode.com/dgraph/guides/get-started-with-dgraph/basic-operations.md

# Get Started with Dgraph - Basic Operations

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

**Welcome to the second tutorial of getting started with Dgraph.**

In the [previous tutorial](./introduction) of getting started, we learned some
of the basics of Dgraph. Including how to run the database, add new nodes and
predicates, and query them back.

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/graph-1.jpg?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=e355a75d592de67aaec2b45458f16ffb" alt="Graph" width="768" height="480" data-path="images/dgraph/guides/get-started-with-dgraph/graph-1.jpg" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/graph-1.jpg?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=9b6b3fc28d13718fffc6a877ac77e7bb 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/graph-1.jpg?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=4b368ad22834cac46e983b8a8d98d08f 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/graph-1.jpg?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=d24bfadaef8c19ffd232210c151091a3 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/graph-1.jpg?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=d6237fc43d9cd0a4ed9c39fd381110e5 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/graph-1.jpg?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=3bcbc43e6ff8d71b5a6aca3131311bf0 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/graph-1.jpg?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=db219a14aaa19aa291828ebbca287271 2500w" data-optimize="true" data-opv="2" />

In this tutorial, we'll build the above Graph and learn more about operations
using the UID (Universal Identifier) of the nodes. Specifically, we'll learn
about:

* Querying and updating nodes, deleting predicates using their UIDs.
* Adding an edge between existing nodes.
* Adding a new predicate to an existing node.
* Traversing the Graph.

You can see the accompanying video below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/8TKD-FFBVgE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

***

First, let's create our Graph.

Go to Ratel's mutate tab, paste the mutation below in the text area, and click
Run.

```json
{
  "set": [
    {
      "name": "Michael",
      "age": 40,
      "follows": {
        "name": "Pawan",
        "age": 28,
        "follows": {
          "name": "Leyla",
          "age": 31
        }
      }
    }
  ]
}
```

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-add-data.gif?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=caac231afc6312cff1a82305bcc818c3" alt="mutation-1" width="600" height="338" data-path="images/dgraph/guides/get-started-with-dgraph/a-add-data.gif" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-add-data.gif?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=a3b0ded24fcdaa8ba4db8dac61f8e546 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-add-data.gif?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=fd74d24e06a4dc7c2ac1738f822b0dba 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-add-data.gif?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=556bd7a765cc5f79156ad744c830c6c5 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-add-data.gif?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=0cda1c852d48e0ccdf3c6a6d03289630 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-add-data.gif?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=9c016fdc63a673f5bbee5348894e6c4e 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-add-data.gif?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=65ee64d2144eea375c63d4efe8a85319 2500w" data-optimize="true" data-opv="2" />

## Query using UIDs

The UID of the nodes can be used to query them back. The built-in function `uid`
takes a list of UIDs as an argument, so you can pass one (`uid(0x1)`) or as many
as you need (`uid(0x1, 0x2)`).

It returns the same UIDs that were passed as input, no matter whether they exist
in the database or not. But the predicates requested are returned only if both
the UIDs and their predicates exist.

Let's see the `uid` function in action.

First, let's copy the UID of the node created for `Michael`.

Go to the query tab, type in the query below, and click Run.

```graphql
{
  people(func: has(name)) {
    uid
    name
    age
  }
}
```

Now, from the result, copy the UID of Michael's node.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-get-uid-1.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=5af5e61f69020f3817022d8c07782bd8" alt="Get UID" width="854" height="478" data-path="images/dgraph/guides/get-started-with-dgraph/b-get-uid-1.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-get-uid-1.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=2401247f4fff255ee8eb9672257eae64 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-get-uid-1.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=3e90e5b760152de4f6f26b53ec16eee8 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-get-uid-1.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=69cd148e4ccca69d6fc887bbeba12a04 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-get-uid-1.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=1a185c502d56de78fbccc7928b7a8170 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-get-uid-1.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=0695803113dab3bb52c20581c9578cc1 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-get-uid-1.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=3105ee43791029ee3907667155d0d16a 2500w" data-optimize="true" data-opv="2" />

In the query below, replace the placeholder `MICHAELS_UID` with the UID you just
copied, and run the query.

```graphql
{
    find_using_uid(func: uid(MICHAELS_UID)){
        uid
        name
        age
    }
}
```

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-query-uid.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=5eda66949cccabed4d3ffc34f833e7b9" alt="Get node from UID" width="854" height="478" data-path="images/dgraph/guides/get-started-with-dgraph/c-query-uid.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-query-uid.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=fdbffb59b5e5ee026c4fb065a2feaf47 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-query-uid.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=f3d8a660e8413a659ece75566514ae6c 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-query-uid.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=cebea9f475ca9d0d1663b338207dd9a3 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-query-uid.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=3d0d25deb28dc4e98385ad61c88dbb32 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-query-uid.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=9ff90c29f1c165e968a51e37486bf4da 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-query-uid.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=b2b2a05cb76126d287f568f116fcda24 2500w" data-optimize="true" data-opv="2" />

*Note: `MICHAELS_UID` appears as `0x8` in the images. The UID you get on your
machine might have a different value.*

You can see that the `uid` function returns the node matching the UID for
Michael's node.

Refer to the [previous tutorial](./introduction) if you have questions related
to the structure of the query in general.

## Updating predicates

You can also update one or more predicates of a node using its UID.

Michael recently celebrated his birthday. Let's update his age to 41.

Go to the mutate tab and execute the mutation. Again, don't forget to replace
the placeholder `MICHAELS_UID` with the actual UID of the node for `Michael`.

```json
{
  "set": [
    {
      "uid": "MICHAELS_UID",
      "age": 41
    }
  ]
}
```

We had earlier used `set` to create new nodes. But on using the UID of an
existing node, it updates its predicates, instead of creating a new node.

You can see that Michael's age is updated to 41.

```graphql
{
    find_using_uid(func: uid(MICHAELS_UID)){
        name
        age
    }
}
```

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-update-check.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=f50c1d798b9c642a5309e9f3e47f4a82" alt="update check" width="854" height="478" data-path="images/dgraph/guides/get-started-with-dgraph/d-update-check.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-update-check.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=dfabbd5b5bd4fafbb9d224eb2c800c39 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-update-check.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=64ace3af1c1c28b517292bc8254e0fa4 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-update-check.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=666b414f032a1fa0863133b8cad5f6b5 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-update-check.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=de2fea9a6ab610fa706c569dd64ef91a 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-update-check.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=c76e29f1012235c24a31480971b517b9 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-update-check.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=8b1bc4c01591c5495bcea4de38ebae88 2500w" data-optimize="true" data-opv="2" />

Similarly, you can also add new predicates to an existing node. Since the
predicate `country` doesn't exist for the node for `Michael`, it creates a new
one.

```json
{
  "set": [
    {
      "uid": "MICHAELS_UID",
      "country": "Australia"
    }
  ]
}
```

## Adding an edge between existing nodes

You can also add an edge between existing nodes using their UIDs.

Let's say, `Leyla` starts to follow `Michael`.

We know that this relationship between them has to represented by creating the
`follows` edge between them.

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/graph-2.jpg?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=93b24de42cf56f417b96ec20e14ac4b9" alt="Graph" width="797" height="480" data-path="images/dgraph/guides/get-started-with-dgraph/graph-2.jpg" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/graph-2.jpg?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=c15a7761100c0aae3c5aa6e16d0637f0 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/graph-2.jpg?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=911af99e02862e2e30ae9438dbfc1312 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/graph-2.jpg?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=4f548c197f97dc95444d873af3aee68f 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/graph-2.jpg?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=4af3d7480c87e559bbb8ca1bf080100c 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/graph-2.jpg?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=b0c25fb2f111543c25b17fbf73dd0c4f 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/graph-2.jpg?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=3aa74fa2fd18ec69f58e63ddf38031b2 2500w" data-optimize="true" data-opv="2" />

First, let's copy the UIDs of nodes for `Leyla` and `Michael` from Ratel.

Now, replace the placeholders `LEYLAS_UID` and `MICHAELS_UID` with the ones you
copied, and execute the mutation.

```json
{
  "set": [
    {
      "uid": "LEYLAS_UID",
      "follows": {
        "uid": "MICHAELS_UID"
      }
    }
  ]
}
```

## Traversing the edges

Graph databases offer many distinct capabilities. `Traversals` are among them.

Traversals answer questions or queries related to the relationship between the
nodes. Hence, queries like, `who does Michael follow?` are answered by
traversing the `follows` relationship.

Let's run a traversal query and then understand it in detail.

```graphql
{
    find_follower(func: uid(MICHAELS_UID)){
        name
        age
        follows {
          name
          age
        }
    }
}
```

Here's the result.

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-traversal.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=4ce8f4f9b707cb87d4d37037eda1e8cd" alt="traversal-result" width="854" height="477" data-path="images/dgraph/guides/get-started-with-dgraph/e-traversal.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-traversal.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=90aa87c8298039726d83b28a51b221db 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-traversal.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=ee8f0ce7d1749cdc3e8a0fb35e23cf15 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-traversal.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=563791b62debc2bd0e45ce11a2c31574 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-traversal.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=74a0600545513a953a7cc0010cad0a79 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-traversal.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=45c8a3d874d6683db5609551ed3990f4 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-traversal.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=20c0adf616a3316321fcf3bf96064d59 2500w" data-optimize="true" data-opv="2" />

The query has three parts:

* **Selecting the root nodes.**

First, you need to select one or more nodes as the starting point for
traversals. These are called the root nodes. In the preceding query, we use the
`uid()` function to select the node created for `Michael` as the root node.

* **Choosing the edge to be traversed**

You need to specify the edge to be traversed, starting from the selected root
nodes. And then, the traversal, travels along these edges, from one end to the
nodes at the other end.

In our query, we chose to traverse the `follows` edge starting from the node for
`Michael`. The traversal returns all the nodes connected to the node for
`Michael` via the `follows` edge.

* **Specify the predicates to get back**

Since Michael follows only one person, the traversal returns just one node.
These are `level-2` nodes. The root nodes constitute the nodes for `level-1`.
Again, we need to specify which predicates you want to get back from `level-2`
nodes.

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/j-explain.JPG?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=08cc7adb239b4e297b9fb2ae55d6ba11" alt="Get node from UID" width="854" height="310" data-path="images/dgraph/guides/get-started-with-dgraph/j-explain.JPG" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/j-explain.JPG?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=b371a1032f52efca28b1d045edd6f6bb 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/j-explain.JPG?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=b28df4d395889a817536fe2949475c56 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/j-explain.JPG?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=06a454feb0c34fe192a498c3a672b9a6 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/j-explain.JPG?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=02242dd246c02090be1e9cfe0bcd2db5 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/j-explain.JPG?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=a5ebb602b6bf9c6798bc25eadf947bdf 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/j-explain.JPG?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=5b02026917db09653bf4dcc40c8a15f3 2500w" data-optimize="true" data-opv="2" />

You can extend the query to make use of `level-2` nodes and traverse the Graph
further and deeper. Let's explore that in the next section.

### Multi-level traversals

The first level of traversal returns people followed by Michael. The next level
of traversal further returns the people they in-turn follow.

This pattern can be repeated multiple times to achieve multi-level traversals.
The depth of the query increases by one as we traverse each level of the Graph.
That's when we say that the query is deep!

```graphql
{
  find_follower(func: uid(MICHAELS_UID)) {
    name
    age
    follows {
      name
      age
      follows {
        name
        age
      }
    }
  }
}
```

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/f-level-3-traverse.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=67ccb15df19cdab529dfe27ea08c0afa" alt="level-3-query" width="854" height="477" data-path="images/dgraph/guides/get-started-with-dgraph/f-level-3-traverse.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/f-level-3-traverse.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=eefd186b88285f2ed69a0f9ca8eb6a70 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/f-level-3-traverse.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=42e5270c981949d360ac990c1bdc2ce2 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/f-level-3-traverse.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=581e069719d56a6704ed0a0391913563 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/f-level-3-traverse.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=ecd27e38bc22836b3be1ef0d5037d49a 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/f-level-3-traverse.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=e0bfe44a78b6c65fbd8171807530c689 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/f-level-3-traverse.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=78c90e37502fd93199a42d9a6f5c8f4d 2500w" data-optimize="true" data-opv="2" />

Here is one more example from the extension of the last query.

```graphql
{
  find_follower(func: uid(MICHAELS_UID)) {
    name
    age
    follows {
      name
      age
      follows {
        name
        age
        follows {
          name
          age
        }
      }
    }
  }
}
```

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/g-level-4-traversal.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=4f5d43740969b129f08a16aff62f3795" alt="level 3" width="854" height="477" data-path="images/dgraph/guides/get-started-with-dgraph/g-level-4-traversal.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/g-level-4-traversal.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=c6561bd476bceffd52a2194a5d394fba 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/g-level-4-traversal.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=d23fda9e7f72777ae5b8f291f66f7bb5 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/g-level-4-traversal.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=0cb883ef50c80b68300f9edf5ae1e8d0 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/g-level-4-traversal.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=1a22eaa8a21786df9ee869d7e66708d7 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/g-level-4-traversal.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=cca24a992b860526a520321eb9a92559 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/g-level-4-traversal.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=954e9ae164d151e0067b8b24b28c3cb1 2500w" data-optimize="true" data-opv="2" />

This query is really long! The query is four levels deep. In other words, the
depth of the query is four. If you ask, isn't there an in-built function that
makes multi-level deep queries or traversals easy?

The answer is Yes! That's what the `recurse()` function does. Let's explore that
in our next section.

#### Recursive traversals

Recursive queries makes it easier to perform multi-level deep traversals. They
let you easily traverse a subset of the Graph.

With the following recursive query, we achieve the same result as our last
query. But, with a much better querying experience.

```graphql
{
  find_follower(func: uid(MICHAELS_UID)) @recurse(depth: 4) {
    name
    age
    follows
  }
}
```

In the query, the `recurse` function traverses the graph starting from the node
for `Michael`. You can choose any other node to be the starting point. The depth
parameter specifies the maximum depth the traversal query should consider.

Let's run the recursive traversal query after replacing the placeholder with the
UID of node for Michael.

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-recursive-traversal.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=c0afd1afef7db365e46e317e73324b7d" alt="recurse" width="854" height="426" data-path="images/dgraph/guides/get-started-with-dgraph/h-recursive-traversal.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-recursive-traversal.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=93a8bbf6538a2a4a7875e21b8605e5ab 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-recursive-traversal.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=bb3714b5bbb63b5310fc207351e9286c 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-recursive-traversal.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=3719d12ff149c664e738019020435711 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-recursive-traversal.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=062e4447c4901d693561d7734102babe 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-recursive-traversal.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=f7ad1c2ea0e5052c85e83f0f902265db 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-recursive-traversal.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=695c7d3432f954c2e5208f8f245e9a72 2500w" data-optimize="true" data-opv="2" />

[Check out the docs](/dgraph/dql/recurse#recurse) for detailed instructions on
using the `recurse` directive.

#### Edges have directions

Edges in Dgraph have directions.

For instance, the `follows` edge emerging from the node for `Michael`, points at
the node for `Pawan`. They have a notion of direction.

Traversing along the direction of an edge is natural to Dgraph. We'll learn
about traversing edges in reverse direction in our next tutorial.

## Deleting a predicate

Predicates of a node can be deleted using the `delete` mutation. Here's the
syntax of the delete mutation to delete any predicate of a node,

```graphql
{
    delete {
        <UID> <predicate_name> * .
    }
}
```

Using the mutation syntax, let's compose a delete mutation. Let's delete the
`age` predicate of the node for `Michael`.

```graphql
{
  delete {
    <MICHAELS_UID> <age> * .
  }
}
```

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-delete.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=efabb181861bb152942201bf94fa2931" alt="recurse" width="854" height="477" data-path="images/dgraph/guides/get-started-with-dgraph/i-delete.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-delete.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=e72654d34c63a5a71d6bc289d8c19a1a 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-delete.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=3a3afffa06724c545ae06c80053ff150 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-delete.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=be74194550dee24e5835f6c0fc3361dd 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-delete.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=1d7fcc7a76d8ccf8cdceba464b2caa2f 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-delete.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=ce66ba221c96521f459427d9c82655f7 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-delete.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=d90a96ecf984ddb4abd32702baa696c7 2500w" data-optimize="true" data-opv="2" />

## Wrapping up

In this tutorial, we learned about the CRUD operations using UIDs. We also
learned about `recurse()` function.

Before we wrap, here's a sneak peek into our next tutorial.

Did you know that you could search predicates based on their value?

Sounds interesting?

Check out our next tutorial of the getting started series
[here](./types-and-operations).

## Need help

* Please use [discuss.hypermode.com](https://discuss.hypermode.com) for
  questions, feature requests, bugs, and discussions.
