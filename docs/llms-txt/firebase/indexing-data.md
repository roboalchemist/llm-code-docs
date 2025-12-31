# Source: https://firebase.google.com/docs/database/security/indexing-data.md.txt

<br />

Firebase allows you to do ad-hoc queries on your data using an arbitrary child key. If you know in advance what your indexes will be, you can define them via the`.indexOn`rule in your Firebase Realtime Database Security Rules to improve query performance.

## Defining Data Indexes

Firebase provides powerful tools for[ordering](https://firebase.google.com/docs/database/web/lists-of-data#sorting_and_filtering_data)and[querying](https://firebase.google.com/docs/database/web/lists-of-data#data-order)your data. Specifically, Firebase allows you to do ad-hoc queries on a collection of nodes using any common child key. As your app grows, the performance of this query degrades. However, if you tell Firebase about the keys you will be querying, Firebase will index those keys at the servers, improving the performance of your queries.
| A node's key is indexed automatically, so there is no need to index it explicitly.

## Indexing with orderByChild

The easiest way to explain this is through an example. All of us at Firebase agree that dinosaurs are pretty cool. Here's a snippet from a sample database of dinosaur facts. We will use it to explain how`.indexOn`works with`orderByChild()`.  

```text
{
  "lambeosaurus": {
    "height" : 2.1,
    "length" : 12.5,
    "weight": 5000
  },
  "stegosaurus": {
    "height" : 4,
    "length" : 9,
    "weight" : 2500
  }
}
```

Let's imagine that in our app, we often need to order the dinosaurs by name, height, and length, but never by weight. We can improve the performance of our queries by telling Firebase this information. Since the name of the dinosaurs are just the keys, Firebase already optimizes for queries by dinosaur name, since this is the key of the record. We can use`.indexOn`to tell Firebase to optimize queries for height and length as well:  

```text
{
  "rules": {
    "dinosaurs": {
      ".indexOn": ["height", "length"]
    }
  }
}
```

Like other rules, you can specify an`.indexOn`rule at any level in your rules. We placed it at the root level for the example above because all the dinosaur data is stored at the root of the database.

## Indexing with orderByValue

In this example, we'll demonstrate how`.indexOn`works with`orderByValue()`. Let's say we're making a leaderboard of dino sports scores with the following data:  

```text
{
  "scores": {
    "bruhathkayosaurus" : 55,
    "lambeosaurus" : 21,
    "linhenykus" : 80,
    "pterodactyl" : 93,
    "stegosaurus" : 5,
    "triceratops" : 22
  }
}
```

Since we're using orderByValue() to create the leaderboard, we can optimize our queries by adding a`.value`rule at our`/scores`node:  

```text
{
  "rules": {
    "scores": {
      ".indexOn": ".value"
    }
  }
}
```
| **Indexes are not required for development** :
|
| Indexes are not required for development unless you are using the REST API. The realtime client libraries can execute ad-hoc queries without specifying indexes. Performance will degrade as the data you query grows, so it is important to add indexes before you launch your app if you anticipate querying a large set of data.