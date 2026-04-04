# Source: https://docs.hypermode.com/dgraph/guides/get-started-with-dgraph/multi-language-strings.md

# Get Started with Dgraph -  Multi-language strings

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

**Welcome to the fourth tutorial of getting started with Dgraph.**

In the [previous tutorial](./types-and-operations), we learned about Datatypes,
Indexing, Filtering, and Reverse traversals in Dgraph.

In this tutorial, we'll learn about using multi-language strings and operations
on them using the language tags.

You can see the accompanying video below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/_lDE9QXHZC0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

***

## Strings and languages

Strings values in Dgraph are of UTF-8 format. Dgraph also supports values for
string predicate types in multiple languages. The multi-lingual capability is
particularly useful to build features, which requires you to store the same
information in multiple languages.

Let's learn more about them!

Let's start with building a simple food review Graph. Here's the Graph model.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=1d0514c94d40edf52d50aa860ed1f0d3" alt="model" width="526" height="461" data-path="images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=a281d7188019fe6251c3aefa0c0aae11 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=b2f996f4177c8996fe3af07e79d8a401 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=e0e9fd2f64de3883d1828ced7310ad44 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=894439b7a39e25f76c2541f1c2926bfd 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=7bf1424145c7ec3f72c64e2dd4ec8190 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-graph-model.jpg?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=19ec71f27740dfb573eda0b62c0c4c1d 2500w" data-optimize="true" data-opv="2" />

The above Graph has three entities: Food, Comment, and Country.

The nodes in the Graph represent these entities.

For the rest of the tutorial, let's call the node representing a food item as a
`food` node. The node representing a review comment as a `review` node, and the
node representing the country of origin as a `country` node.

Here's the relationship between them:

* Every food item is connected to its reviews via the `review` edge.
* Every food item is connected to its country of origin via the `origin` edge.

Let's add some reviews for some fantastic dishes!

How about spicing it up a bit before we do that?

Let's add the reviews for these dishes in the native language of their country
of origin.

Let's go, amigos!

```json
{
  "set": [
    {
      "food_name": "Hamburger",
      "review": [
        {
          "comment": "Tastes very good"
        }
      ],
      "origin": [
        {
          "country": "United states of America"
        }
      ]
    },
    {
      "food_name": "Carrillada",
      "review": [
        {
          "comment": "Sabe muy sabroso"
        }
      ],
      "origin": [
        {
          "country": "Spain"
        }
      ]
    },
    {
      "food_name": "Pav Bhaji",
      "review": [
        {
          "comment": "स्वाद बहुत अच्छा है"
        }
      ],
      "origin": [
        {
          "country": "India"
        }
      ]
    },
    {
      "food_name": "Borscht",
      "review": [
        {
          "comment": "очень вкусно"
        }
      ],
      "origin": [
        {
          "country": "Russia"
        }
      ]
    },
    {
      "food_name": "mapo tofu",
      "review": [
        {
          "comment": "真好吃"
        }
      ],
      "origin": [
        {
          "country": "China"
        }
      ]
    }
  ]
}
```

*Note: If this mutation syntax is new to you, refer to the
[first tutorial](/introduction) to learn basics of mutation in Dgraph.*

Here's our Graph!

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-full-graph.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=3600a12036ac5e519c81a91cc120717d" alt="full graph" width="822" height="480" data-path="images/dgraph/guides/get-started-with-dgraph/a-full-graph.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-full-graph.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=fdc676c4104f23cf97f1e40ad0fafbf8 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-full-graph.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=28389c1588ab1ebef6fbc6c7abb30cc1 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-full-graph.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=dbfaed10b98e253b92085902d48aad59 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-full-graph.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=039aab3335cb251ecf4b1cdcd8674c1b 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-full-graph.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=6f9f99372913262ba04e78c2a8b80f20 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/a-full-graph.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=6387bf9a23c6fd85e5df4e22aad4f76c 2500w" data-optimize="true" data-opv="2" />

Our Graph has:

* Five blue food nodes.
* The green nodes represent the country of origin of these food items.
* The reviews of the food items are in pink.

You can also see that Dgraph has auto-detected the data types of the predicates.
You can check that out from the schema tab.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-schema.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=a0a4773923134dcf1bc7109ff0341697" alt="full graph" width="854" height="459" data-path="images/dgraph/guides/get-started-with-dgraph/c-schema.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-schema.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=a9b12af76a16c3bc401052b1d3bc148b 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-schema.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=2e2ace784aebd725093a7f69fa3fb12c 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-schema.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=c144e144cffcc738d55246db0c7f5e4d 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-schema.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=7a024f7a4720984b7383890e99c1bcfd 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-schema.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=26b605f703158289d326e57a6d2f2257 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/c-schema.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=b8f2e7c4f16244b286874a0f53d2c020 2500w" data-optimize="true" data-opv="2" />

*Note: Check out the [previous tutorial](./types-and-operations) to know more
about data types in Dgraph.*

Let's write a query to fetch all the food items, their reviews, and their
country of origin.

Go to the query tab, paste the query, and click Run.

```graphql
{
  food_review(func: has(food_name)) {
    food_name
      review {
        comment
      }
      origin {
        country
      }
  }
}
```

*Note: Check the [second tutorial](./basic-operations) if you want to learn more
about traversal queries like the above one*

Now, Let's fetch only the food items and their reviews,

```graphql
{
  food_review(func: has(food_name)) {
    food_name
      review {
        comment
      }
  }
}
```

As expected, these comments are in different languages.

<img src="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-comments.png?fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=123d69641509c7aa434facecab2fe61c" alt="full graph" width="854" height="462" data-path="images/dgraph/guides/get-started-with-dgraph/b-comments.png" srcset="https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-comments.png?w=280&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=bcca40e84881e2d2a636e9ac8ca0693c 280w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-comments.png?w=560&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=95611e31868fd0e179b412b4f323fe66 560w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-comments.png?w=840&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=4e6d97579e9272598308470bbc887ac8 840w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-comments.png?w=1100&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=dbd34596141eb0a8efc9e0b34bbe244f 1100w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-comments.png?w=1650&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=cc3c387c0d51a9f2c213cb9025bea3d9 1650w, https://mintcdn.com/hypermode/mx5jPijweyuId04r/images/dgraph/guides/get-started-with-dgraph/b-comments.png?w=2500&fit=max&auto=format&n=mx5jPijweyuId04r&q=85&s=b154b933874ed3fcff1a78826444e68a 2500w" data-optimize="true" data-opv="2" />

But can we fetch the reviews based on their language? Can we write a query which
says: *Hey Dgraph, can you give me only the reviews written in Chinese?*

That's possible, but only if you provide additional information about the
language of the string data. You can do so by using language tags. While adding
the string data using mutations, you can use the language tags to specify the
language of the string predicates.

Let's see the language tags in action!

I've heard that Sushi is yummy! Let's add a review for `Sushi` in more than one
language. We'll be writing the review in three different languages: English,
Japanese, and Russian.

Here's the mutation to do so.

```json
{
  "set": [
    {
      "food_name": "Sushi",
      "review": [
        {
          "comment": "Tastes very good",
          "comment@jp": "とても美味しい",
          "comment@ru": "очень вкусно"
        }
      ],
      "origin": [
        {
          "country": "Japan"
        }
      ]
    }
  ]
}
```

Let's take a closer look at how we assigned values for the `comment` predicate
in different languages.

We used the language tags (@ru, @jp) as a suffix for the `comment` predicate.

In the above mutation:

* We used the `@ru` language tag to add the comment in Russian:
  `"comment@ru": "очень вкусно"`.

* We used the `@jp` language tag to add the comment in Japanese:
  `"comment@jp": "とても美味しい"`.

* The comment in `English` is untagged: `"comment": "Tastes very good"`.

In the mutation above, Dgraph creates a new node for the reviews, and stores
`comment`, `comment@ru`, and `comment@jp` in different predicates inside the
same node.

*Note: If you're not clear about basic terminology like `predicates`, do read
the [first tutorial](./introduction).*

Let's run the above mutation.

Go to the mutate tab, paste the mutation, and click Run.

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-lang-error.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=828ed89fc3f2dcf93cf3fac5dd7b935d" alt="lang error" width="854" height="449" data-path="images/dgraph/guides/get-started-with-dgraph/d-lang-error.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-lang-error.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=2f5b70ee4f2f8e3d8e0c324794f27f90 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-lang-error.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=19f0d4a0f65aa8c290d5c3cae3382fd4 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-lang-error.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=f9d44ec45626b562311fe0b54bde97ba 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-lang-error.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=6e3e62b7bbd165cc249f387ee8b01fc1 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-lang-error.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=cb5adb99407287becc2025339c6955be 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/d-lang-error.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=3e4015ee1d5ac0226b6582177d79f518 2500w" data-optimize="true" data-opv="2" />

We got an error! Using the language tag requires you to add the `@lang`
directive to the schema.

Follow the instructions below to add the `@lang` directive to the `comment`
predicate.

* Go to the Schema tab.
* Click on the `comment` predicate.
* Tick mark the `lang` directive.
* Click on the `Update` button.

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-update-lang.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=3cbeddbb3c60e4a206fc461c62bcdf00" alt="lang error" width="854" height="423" data-path="images/dgraph/guides/get-started-with-dgraph/e-update-lang.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-update-lang.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=b9ab617f5aa18fa03734e059b270749f 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-update-lang.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=eb4729a4f3706182f83c12ea0a7c159f 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-update-lang.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=1493b05f7f7c34fd744cacd3d09dbfd2 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-update-lang.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=62453c829c96dae8befcc3ff3c5d378f 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-update-lang.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=52d38274f78d41636042dcdbe9a7bada 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/e-update-lang.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=5baddb679b9e48c8db701afeab04d642 2500w" data-optimize="true" data-opv="2" />

Let's re-run the mutation.

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/f-mutation-success.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=8812c4f92643b8d90247945e6af216d5" alt="lang error" width="854" height="446" data-path="images/dgraph/guides/get-started-with-dgraph/f-mutation-success.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/f-mutation-success.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=dce0c422d010d77c1e3cb3c31b38ecbd 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/f-mutation-success.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=d512dd70f7629a14e6155c1674057c57 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/f-mutation-success.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=389d0d780100614240b6439bf335d11b 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/f-mutation-success.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=f794ea5b413e565673a46fe22725e2c0 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/f-mutation-success.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=52d1ebc9086a2a0a26e9f516f7379fda 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/f-mutation-success.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=ac86662549f21ba2ec5e451d00c0b5e9 2500w" data-optimize="true" data-opv="2" />

Success!

Again, remember that using the above mutation, we have added only one review for
Sushi, not three different reviews!

But, if you want to add three different reviews, here's how you do it.

Adding the review in the format below creates three nodes, one for each of the
comments. But, do it only when you're adding a new review, not to represent the
same review in different languages.

```json
"review": [
  {
    "comment": "Tastes very good"
  },
  {
    "comment@jp": "とても美味しい"
  },
  {
    "comment@ru": "очень вкусно"
  }
]
```

Dgraph allows any strings to be used as language tags. But, it's highly
recommended only to use the ISO standard code for language tags.

By following the standard, you eliminate the need to communicate the tags to
your team or to document it somewhere.
[Click here](https://www.w3schools.com/tags/ref_language_codes.asp) to see the
list of ISO standard codes for language tags.

In our next section, let's make use of the language tags in our queries.

## Querying using language tags

Let's obtain the review comments only for `Sushi`.

In the [previous article](./types-and-operations), we learned about using the
`eq` operator and the `hash` index to query for string predicate values.

Using that knowledge, let's first add the `hash` index for the `food_name`
predicate.

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/g-hash.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=3e15590bec5fa403352f008a3d273923" alt="hash index" width="854" height="460" data-path="images/dgraph/guides/get-started-with-dgraph/g-hash.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/g-hash.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=2a8dd83be2f14e824c9a099eea7d6583 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/g-hash.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=8bd3af1bd0f81d50b0a1b64edbc4ad4a 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/g-hash.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=ee30d2d5b6dceade526036acb0ed0a48 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/g-hash.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=afe1decb3759f72722b4c1e6058301c0 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/g-hash.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=a97b20c5d597a8f26b5ab37ea69b08aa 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/g-hash.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=9c1bfd30e153425e44f2e9749c173f1b 2500w" data-optimize="true" data-opv="2" />

Now, go to the query tab, paste the query in the text area, and click Run.

```graphql
{
  food_review(func: eq(food_name,"Sushi")) {
    food_name
      review {
        comment
      }
  }
}
```

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-comment.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=8ae7aa45479615e2a7abb966f79beae0" alt="hash index" width="854" height="454" data-path="images/dgraph/guides/get-started-with-dgraph/h-comment.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-comment.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=b63a7b6d8503e70b2cb290f885f74f5b 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-comment.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=ad00740cd61deac6fdcea866f890b07d 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-comment.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=88d6fb3681fca03ca51181be97663a86 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-comment.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=217953e9cd36f4b09493b65c96206b16 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-comment.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=f5e9d9941a84b8c5cca949bd7034be32 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/h-comment.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=9d450a57e4d3edc090619e5fabaa83d4 2500w" data-optimize="true" data-opv="2" />

By default, the query only returns the untagged comment.

But you can use the language tag to query specifically for a review comment in a
given language.

Let's query for a review for `Sushi` in Japanese.

```graphql
{
  food_review(func: eq(food_name,"Sushi")) {
    food_name
    review {
      comment@jp
    }
  }
}
```

<img src="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-japanese.png?fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=0153046c974feccc3d937fb58b46a8ef" alt="Japanese" width="854" height="457" data-path="images/dgraph/guides/get-started-with-dgraph/i-japanese.png" srcset="https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-japanese.png?w=280&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=f1d3602e39fae6197f9429b577a39c3c 280w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-japanese.png?w=560&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=42119a7cb6e935f7566b147ea6fe008e 560w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-japanese.png?w=840&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=854db22b8f86905f6a1db13c2f85c740 840w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-japanese.png?w=1100&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=92a2206a0d7b7f00f549ce02e58a0d83 1100w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-japanese.png?w=1650&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=dd1ea1a0e7e5bd6b696ad5cb92b2fcbe 1650w, https://mintcdn.com/hypermode/X5Ug2alo-iTX3DD4/images/dgraph/guides/get-started-with-dgraph/i-japanese.png?w=2500&fit=max&auto=format&n=X5Ug2alo-iTX3DD4&q=85&s=3f92220f52e2999a55b62374dba952b0 2500w" data-optimize="true" data-opv="2" />

Now, let's query for a review for `Sushi` in Russian.

```graphql
{
  food_review(func: eq(food_name,"Sushi")) {
    food_name
    review {
      comment@ru
    }
  }
}
```

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/j-russian.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=4c817e22e6098be73216d1644feca2fa" alt="Russian" width="854" height="459" data-path="images/dgraph/guides/get-started-with-dgraph/j-russian.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/j-russian.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=4fc01cdc68a894957550c48f752b082c 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/j-russian.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=b3da2eaff4fdd61263adcc2ccc21aa96 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/j-russian.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=7ad1d0564fe24793c46bc1fcf143610a 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/j-russian.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=4028648fe5e229250c82fde20e9d5508 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/j-russian.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=0a967565eda3d662067baa6c1c0872aa 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/j-russian.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=66c86564ff2339c8f1f5cf3f3bb6871b 2500w" data-optimize="true" data-opv="2" />

You can also fetch all the comments for `Sushi` written in any language.

```graphql
{
  food_review(func: eq(food_name,"Sushi")) {
    food_name
    review {
      comment@*
    }
  }
}
```

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/k-star.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=ca7f873440a8f4871dbdb8b5837e4540" alt="Russian" width="854" height="458" data-path="images/dgraph/guides/get-started-with-dgraph/k-star.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/k-star.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=83b2bd3070c4c34e6ae44be62dfce24e 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/k-star.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=db7ad886a46d7a374c6623687103aeee 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/k-star.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=41b39b97bbb3247532321604e7546e5c 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/k-star.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=10624e4ff0fc67f454094e140f57d6f7 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/k-star.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=a99381e6b805e62287f30d14e22a7287 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/k-star.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=e652e99703cebf7d64f517d38491ced7 2500w" data-optimize="true" data-opv="2" />

Here is the table with the syntax for various ways of making use of language
tags while querying.

| Syntax           | Result                                                                                                                                                        |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| comment          | Look for an untagged string; return nothing if no untagged review exists.                                                                                     |
| comment\@.       | Look for an untagged string, if not found, then return review in any language. But, this returns only a single value.                                         |
| comment\@jp      | Look for comment tagged `@jp`. If not found, the query returns nothing.                                                                                       |
| comment\@ru      | Look for comment tagged `@ru`. If not found, the query returns nothing.                                                                                       |
| comment\@jp:.    | Look for comment tagged `@jp` first. If not found, then find the untagged comment. If that's not found too, return anyone comment in other languages.         |
| comment\@jp:ru   | Look for comment tagged `@jp`, then `@ru`. If neither is found, it returns nothing.                                                                           |
| comment\@jp:ru:. | Look for comment tagged `@jp`, then `@ru`. If both not found, then find the untagged comment. If that's not found too, return any other comment if it exists. |
| comment@\*       | Return all the language tags, including the untagged.                                                                                                         |

If you remember, we had initially added a Russian dish `Borscht` with its review
in `Russian`.

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-russian.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=6933607bde45ef15b7ed776e6f1cd154" alt="Russian" width="841" height="480" data-path="images/dgraph/guides/get-started-with-dgraph/l-russian.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-russian.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=edfe82dac2e853c8f6d0045a0f98d23e 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-russian.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=5c4ba3d6235e10dde327065960d86dfe 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-russian.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=f0e51c244dda5801511a3998d9bf5e45 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-russian.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=fe0c76cc3aeab6d1bb81cc68308e881b 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-russian.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=02607be14f414b787c92b8f35419a7f6 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/l-russian.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=8fe35b49a11cf282505667ee12fdad27 2500w" data-optimize="true" data-opv="2" />

If you notice, we haven't used the language tag `@ru` for the review written in
Russian.

Hence, if we query for all the reviews written in `Russian`, the review for
`Borscht` doesn't make it to the list.

Only the review for `Sushi,` written in `Russian`, makes it to the list.

<img src="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-sushi.png?fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=9e49b02718b249b6b3b5538cd8626568" alt="Russian" width="845" height="480" data-path="images/dgraph/guides/get-started-with-dgraph/m-sushi.png" srcset="https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-sushi.png?w=280&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=44258deca7ccbb418e51947c184c0645 280w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-sushi.png?w=560&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=c52bc3b0f1d93fdc9895769ac14c6a37 560w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-sushi.png?w=840&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=f93529dc51732d3d2001c2b0f5ae40a5 840w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-sushi.png?w=1100&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=af4f75e227041e85592d122ec9d0fa0f 1100w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-sushi.png?w=1650&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=ceddc1a53e3553129bfcd388335e13cf 1650w, https://mintcdn.com/hypermode/vCcShAQutnKZdkcC/images/dgraph/guides/get-started-with-dgraph/m-sushi.png?w=2500&fit=max&auto=format&n=vCcShAQutnKZdkcC&q=85&s=44b1d690a9071df36cb611a7ab9ba54c 2500w" data-optimize="true" data-opv="2" />

So, here's the lesson of the day!

> If you are representing the same information in different languages, don't
> forget to add your language tags!

## Summary

In this tutorial, we learned about using multi-language string and operations on
them using the language tags.

The usage of tags is not just restricted to multi-lingual strings. Language tags
are just a use case of Dgraph's capability to tag data.

In the next tutorial, we'll continue our quest into the string types in Dgraph.
We'll explore the string type indices in detail.

Sounds interesting?

Check out our next tutorial of the getting started series
[here](./string-indicies).

## Need Help

* Please use [discuss.hypermode.com](https://discuss.hypermode.com) for
  questions, feature requests, bugs, and discussions.
