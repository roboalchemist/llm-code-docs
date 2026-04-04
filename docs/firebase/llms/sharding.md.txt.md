# Source: https://firebase.google.com/docs/database/usage/sharding.md.txt

The best way to optimize performance and scale your data in Firebase Realtime Database
is to split your data across multiple Realtime Database instances, also known as
database sharding. Sharding gives you the flexibility to scale beyond the
[limits](https://firebase.google.com/docs/database/usage/limits) that apply to individual database
instances, in addition to load balancing and performance optimization.

## When to shard your data

You might want to shard your data across multiple databases if you're using
Realtime Database and fit into any of the following scenarios:

- You want to scale beyond the limit of 200,000 simultaneous connections, 1,000 write operations/second, or any of the other [limits](https://firebase.google.com/docs/database/usage/limits) for a single database instance.
- You have multiple, discrete data sets and want to optimize performance (for example, a chat app that serves separate, independent groups of users).
- You want to balance load across multiple databases to improve uptime and reduce the risk of overloading a single database instance.

## How to shard your data

To shard your data, follow these steps (described in greater detail below):

1. Map your data to multiple databases according to your app's specific needs.
2. Create multiple database instances.
3. Configure your app so it connects to the Realtime Database instance necessary for each data set.

### Map your data

When you're mapping your data to multiple databases, try to satisfy the
following conditions:

- Each query only runs against a single database instance. Realtime Database doesn't support queries across database instances.
- No sharing or duplication of data across database instances (or minimal sharing or duplication).
- Each app instance only connects to one database at any given moment.

As you're mapping your data, consider applying the following strategies:

#### Create a "master shard"

Store a map of how your data is stored across
database instances. This way, you can programmatically look up which database
instance corresponds to the connecting client. Keep in mind that this might
have more overhead than directly connecting to the particular database
instance you need, when you need it.

#### Bucket data by categories or by customer

Store data in siloed database instances, grouped by user or data type.
For example, if you build a chat application that serves multiple organizations,
you can create a database instance for each organization and store all the chat
data in unique database instances.

In this case, organization A and organization B don't share data, there isn't
any duplicate data in your databases, and you only perform queries against a
single database instance. Additionally, users in each organization only
connect to their organization's database when they use the chat app.

You can then create several database instances in advance and use the
organization's ID to map a team to its database instance. For example,
organization A maps to Realtime Database A.

The way you map data for your app depends on your particular use case, but the
conditions and strategies outlined above can help you define what works for your
data.

### Create multiple Realtime Database instances

If you're on the [Blaze pricing plan](https://firebase.google.com/pricing), you can create up to 1,000
database instances in the same Firebase project.

![create a database in the <span class=](https://firebase.google.com/static/docs/database/usage/create_database.png)Firebase console with the context menu in the databases section" /\>

1. In the Firebase console, go to the **Data** tab in the [**Develop \> Database**](https://console.firebase.google.com/project/_/database/data) section.
2. Select **Create new database** from the menu in the **Realtime Database** section.
3. Customize your **Database reference** and [**Security rules**](https://firebase.google.com/docs/database/security), then click **Got
   it**.

Repeat the process to create as many database instances as you need. Each
database instance has its own set of Firebase Realtime Database Security Rules, so you can
fine-tune access to your data.

You can create and manage database instances in the Firebase console or using
the [Realtime Database Management REST API](https://firebase.google.com/docs/reference/rest/database/database-management/rest).

> [!NOTE]
> **Note:** If you downgrade from the Blaze plan to the Spark plan, your secondary database instances will be disabled, but not deleted. You can enable them again by upgrading to the Blaze plan.

### Manage and interact with specific instances using the CLI

You can manage and interact with specific Realtime Database instances using the
Firebase CLI.

By default, CLI commands interact with your *default*
database instance. However, you can interact with a *non-default* database
instance by using the
`--instance DATABASE_NAME` flag.

For example, use the following command to run
the profiler for a database instance named `my-example-shard.firebaseio.com`:

```
firebase database:profile --instance "my-example-shard"
```

The following commands support the `--instance` flag:

- `firebase database:get`
- `firebase database:profile`
- `firebase database:push`
- `firebase database:remove`
- `firebase database:set`
- `firebase database:update`

### Edit and deploy Realtime Database Security Rules for each instance

Make sure that your Realtime Database Security Rules allow appropriate access to each
database instance in your project. Each database has its own set of rules,
which you can edit and deploy from the Firebase console, or using the
[Firebase CLI to deploy targets](https://firebase.google.com/docs/cli/targets).

- To edit and deploy rules from the Firebase console, follow these steps:

  1. Go to the [**Rules** tab](https://console.firebase.google.com/project/_/database/rules) in the **Develop \> Database** section.
  2. Select the database you want to edit, then modify the rules.
- To edit and deploy rules from the Firebase CLI, follow these steps:

  1. Modify the rules in the rules files for your database instances (for example, `foo.rules.json`).
  2. Create and apply deploy targets to associate databases that use the same rules file. For example:

     ```
     firebase target:apply database main my-db-1 my-db-2
     ```

     ```
     firebase target:apply database other my-other-db-3
     ```
  3. Update your [`firebase.json`](https://firebase.google.com/docs/cli#the_firebasejson_file) configuration file with the deploy targets:

         {
           "database": [
             {"target": "main", "rules": "foo.rules.json"},
             {"target": "other", "rules": "bar.rules.json"}
           ]
         }

  4. Run the deploy command:

     ```
     firebase deploy
     ```

     <br />

Make sure you consistently edit and deploy rules from the same place. Deploying
rules from the Firebase CLI overrides any edits you've made in the
Firebase console, and editing rules directly in the Firebase console
overrides any recent changes you've deployed through the Firebase CLI.

### Connect your app to multiple database instances

Use the database reference to access data stored in secondary database instances.
You can get the reference for a specific database instance by URL or app. If
you don't specify a URL, you'll get the reference for the app's
default database instance.

### Web

```javascript
import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";

const app1 = initializeApp({
  databaseURL: "https://testapp-1234-1.firebaseio.com"
});

const app2 = initializeApp({
  databaseURL: "https://testapp-1234-2.firebaseio.com"
}, 'app2');

// Get the default database instance for an app1
const database1 = getDatabase(app1);

// Get a database instance for app2
const database2 = getDatabase(app2);
```

### Web

> [!NOTE]
> [Learn
> more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.

```javascript
const app1 = firebase.initializeApp({
  databaseURL: "https://testapp-1234-1.firebaseio.com"
});

const app2 = firebase.initializeApp({
  databaseURL: "https://testapp-1234-2.firebaseio.com"
}, 'app2');

// Get the default database instance for an app1
var database1 = firebase.database();

// Get a database instance for app2
var database2 = firebase.database(app2);
```

##### Swift

**Note:** This Firebase product is not available on the App Clip target.

```swift
// Get the default database instance for an app
var ref: DatabaseReference!

ref = Database.database().reference()
// Get a secondary database instance by URL
var ref: DatabaseReference!

ref = Database.database("https://testapp-1234.firebaseio.com").reference()
```

##### Objective-C

**Note:** This Firebase product is not available on the App Clip target.

```objective-c
// Get the default database instance for an app
@property (strong, nonatomic) FIRDatabaseReference *ref;

self.ref = [[FIRDatabase database] reference];
// Get a secondary database instance by URL
@property (strong, nonatomic) FIRDatabaseReference *ref;

self.ref = [[FIRDatabase databaseWithURL:@"https://testapp-1234.firebaseio.com"] reference];
  
```

### Kotlin

```kotlin
// Get the default database instance for an app
val primary = Firebase.database.reference

// Get a secondary database instance by URL
val secondary = Firebase.database("https://testapp-1234.firebaseio.com").referencehttps://github.com/firebase/snippets-android/blob/a413b0658ff2fc7a72c4b0c59e84a889ff7fac45/database/app/src/main/java/com/google/firebase/referencecode/database/kotlin/ShardingActivity.kt#L11-L15
```

### Java

```java
// Get the default database instance for an app
DatabaseReference primary = FirebaseDatabase.getInstance()
        .getReference();

// Get a secondary database instance by URL
DatabaseReference secondary = FirebaseDatabase.getInstance("https://testapp-1234.firebaseio.com")
        .getReference();
```

#### Optimize the connections on each database

If each client needs to connect to multiple databases during a session, you can
reduce the number of simultaneous connections to each database instance by
connecting to each database instance for only as long as is necessary.

## Get more advice

If you need more help sharding your data across multiple database instances,
reach out to the Firebase experts on our
[Slack channel](https://firebase.community/)
or on [Stack Overflow](https://stackoverflow.com/questions/tagged/firebase).