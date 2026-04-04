# Source: https://firebase.google.com/docs/database/admin/retrieve-data.md.txt

This document covers the basics of retrieving database data, how data is ordered, and how to perform
simple queries on data. Data retrieval in the Admin SDK is implemented slightly differently across different
programming languages.

1. **Asynchronous listeners:** Data stored in a Firebase Realtime Database is retrieved by attaching an asynchronous listener to a database reference. The listener is triggered once for the initial state of the data and again anytime the data changes. An event listener may receive several different [types of events](https://firebase.google.com/docs/database/admin/retrieve-data#section-event-types). This mode of data retrieval is supported in Java, Node.js and Python Admin SDKs.
2. **Blocking reads:** Data stored in a Firebase Realtime Database is retrieved by invoking a blocking method on a database reference, which returns the data stored at the reference. Each method call is a onetime operation. That means the SDK does not register any callbacks that listen to subsequent data updates. This model of data retrieval is supported in Python and Go Admin SDKs.

> [!NOTE]
> The Go Admin SDK currently only supports blocking reads. It cannot be used to add event listeners
> that receive realtime update notifications.

## Getting Started


Let's revisit the blogging example from the previous article to understand how to read data from a Firebase database. Recall
that the blog posts in the example app are stored at the database URL
[https://docs-examples.firebaseio.com/server/saving-data/fireblog/posts.json](https://docs-examples.firebaseio.com/server/saving-data/fireblog/posts).
To read your post data, you can do the following:

##### Java

```java
public static class Post {

  public String author;
  public String title;

  public Post(String author, String title) {
    // ...
  }

}

// Get a reference to our posts
final FirebaseDatabase database = FirebaseDatabase.getInstance();
DatabaseReference ref = database.getReference("server/saving-data/fireblog/posts");

// Attach a listener to read the data at our posts reference
ref.addValueEventListener(new ValueEventListener() {
  @Override
  public void onDataChange(DataSnapshot dataSnapshot) {
    Post post = dataSnapshot.getValue(Post.class);
    System.out.println(post);
  }

  @Override
  public void onCancelled(DatabaseError databaseError) {
    System.out.println("The read failed: " + databaseError.getCode());
  }
});
```

##### Node.js

```javascript
// Get a database reference to our posts
const db = getDatabase();
const ref = db.ref('server/saving-data/fireblog/posts');

// Attach an asynchronous callback to read the data at our posts reference
ref.on('value', (snapshot) => {
  console.log(snapshot.val());
}, (errorObject) => {
  console.log('The read failed: ' + errorObject.name);
}); 
```

##### Python

```python
# Import database module.
from firebase_admin import db

# Get a database reference to our posts
ref = db.reference('server/saving-data/fireblog/posts')

# Read the data at the posts reference (this is a blocking operation)
print(ref.get())
```

##### Go

```go
// Post is a json-serializable type.
type Post struct {
	Author string `json:"author,omitempty"`
	Title  string `json:"title,omitempty"`
}

// Create a database client from App.
client, err := app.Database(ctx)
if err != nil {
	log.Fatalln("Error initializing database client:", err)
}

// Get a database reference to our posts
ref := client.NewRef("server/saving-data/fireblog/posts")

// Read the data at the posts reference (this is a blocking operation)
var post Post
if err := ref.Get(ctx, &post); err != nil {
	log.Fatalln("Error reading value:", err)
}
```
In Java and Node.js, you can pass an optional cancel callback to an event subscription that is called if the read is ever cancelled. A read would be cancelled if the app client doesn't have permission to read from that database reference. This callback is passed an `error` object indicating why the failure occurred. In Python and Go, the `get()` / `Get()` operation fails by raising an exception in case of an error.

If you run the above code, you'll see an object containing all your posts logged to the console. **In case of Node.js and Java, the listener function is called anytime new data is added to your database reference, and you don't need to write any extra code to make this happen.**

In Java and Node.js, the callback function receives a `DataSnapshot`, which is a snapshot of the data. A snapshot is a picture of the data at a particular database reference at a single point in time. Calling `val()` / `getValue()` on a snapshot returns a language-specific object representation of the data. If no data exists at the reference's location, the snapshot's value is `null`. The `get()` method in Python returns a Python representation of the data directly. The `Get()` function in Go unmarshals the data into a given data structure.

Notice that we used the `value` event type in the example above, which reads the entire contents of a Firebase database reference, even if only one piece of data changed. `value` is one of the five different event types listed below that you can use to read data from the database.

## Read Event Types in Java and Node.js

### Value


The `value` event is used to read a static snapshot of the contents at a given database path, as they existed at the time of the read event. It is triggered once with the initial data and again every time the data changes. The event callback is passed a snapshot containing all data at that location, including child data. In the code example above, `value` returned all of the blog posts in your app. Everytime a new blog post is added, the callback function will return all of the posts.

### Child Added


The `child_added` event is typically used when retrieving a list of items from the database. Unlike `value` which returns the entire contents of the location, `child_added` is triggered once for each existing child and then again every time a new child is added to the specified path. The event callback is passed a snapshot containing the new child's data. For ordering purposes, it is also passed a second argument containing the key of the previous child.

If you want to retrieve only the data on each new post added to your blogging app, you could use `child_added`:

##### Java

```java
ref.addChildEventListener(new ChildEventListener() {
  @Override
  public void onChildAdded(DataSnapshot dataSnapshot, String prevChildKey) {
    Post newPost = dataSnapshot.getValue(Post.class);
    System.out.println("Author: " + newPost.author);
    System.out.println("Title: " + newPost.title);
    System.out.println("Previous Post ID: " + prevChildKey);
  }

  @Override
  public void onChildChanged(DataSnapshot dataSnapshot, String prevChildKey) {}

  @Override
  public void onChildRemoved(DataSnapshot dataSnapshot) {}

  @Override
  public void onChildMoved(DataSnapshot dataSnapshot, String prevChildKey) {}

  @Override
  public void onCancelled(DatabaseError databaseError) {}
});
```

##### Node.js

```javascript
// Retrieve new posts as they are added to our database
ref.on('child_added', (snapshot, prevChildKey) => {
  const newPost = snapshot.val();
  console.log('Author: ' + newPost.author);
  console.log('Title: ' + newPost.title);
  console.log('Previous Post ID: ' + prevChildKey);
});
```

In this example the snapshot will contain an object with an individual blog post. Because the SDK converts posts to objects by retrieving the value, you have access to the post's author and title properties by calling `author` and `title` respectively. You also have access to the previous post ID from the second `prevChildKey` argument.

### Child Changed


The `child_changed` event is triggered any time a child node is modified. This includes any
modifications to descendants of the child node. It is typically used in conjunction with `child_added`
and `child_removed` to respond to changes to a list of items. The snapshot passed to the event callback contains the updated data for the child.

You can use `child_changed` to read updated data on blog posts when they are edited:

##### Java

```java
ref.addChildEventListener(new ChildEventListener() {
  @Override
  public void onChildAdded(DataSnapshot dataSnapshot, String prevChildKey) {}

  @Override
  public void onChildChanged(DataSnapshot dataSnapshot, String prevChildKey) {
    Post changedPost = dataSnapshot.getValue(Post.class);
    System.out.println("The updated post title is: " + changedPost.title);
  }

  @Override
  public void onChildRemoved(DataSnapshot dataSnapshot) {}

  @Override
  public void onChildMoved(DataSnapshot dataSnapshot, String prevChildKey) {}

  @Override
  public void onCancelled(DatabaseError databaseError) {}
});
```

##### Node.js

```javascript
// Get the data on a post that has changed
ref.on('child_changed', (snapshot) => {
  const changedPost = snapshot.val();
  console.log('The updated post title is ' + changedPost.title);
});
```

### Child Removed


The `child_removed` event is triggered when an immediate child is removed. It is typically used in conjunction with `child_added` and `child_changed`. The snapshot passed to the event callback contains the data for the removed child.

In the blog example, you can use `child_removed` to log a notification about the deleted post to the console:

##### Java

```java
ref.addChildEventListener(new ChildEventListener() {
  @Override
  public void onChildAdded(DataSnapshot dataSnapshot, String prevChildKey) {}

  @Override
  public void onChildChanged(DataSnapshot dataSnapshot, String prevChildKey) {}

  @Override
  public void onChildRemoved(DataSnapshot dataSnapshot) {
    Post removedPost = dataSnapshot.getValue(Post.class);
    System.out.println("The blog post titled " + removedPost.title + " has been deleted");
  }

  @Override
  public void onChildMoved(DataSnapshot dataSnapshot, String prevChildKey) {}

  @Override
  public void onCancelled(DatabaseError databaseError) {}
});
```

##### Node.js

```javascript
// Get a reference to our posts
const ref = db.ref('server/saving-data/fireblog/posts');

// Get the data on a post that has been removed
ref.on('child_removed', (snapshot) => {
  const deletedPost = snapshot.val();
  console.log('The blog post titled \'' + deletedPost.title + '\' has been deleted');
});
```

### Child Moved


The `child_moved` event is used when working with ordered data, which is covered in the [next section](https://firebase.google.com/docs/database/admin/retrieve-data#section-ordered-data).

## Event Guarantees

The Firebase database makes several important guarantees regarding events:

| Database Event Guarantees |
|:---:|
| Events will always be triggered when local state changes. |
| Events will always eventually reflect the correct state of the data, even in cases where local operations or timing cause temporary differences, such as in the temporary loss of network connection. |
| Writes from a single client will always be written to the server and broadcast out to other users in-order. |
| Value events are always triggered last and are guaranteed to contain updates from any other events which occurred before that snapshot was taken. |


Since value events are always triggered last, the following example will always work:

##### Java

```java
final AtomicInteger count = new AtomicInteger();

ref.addChildEventListener(new ChildEventListener() {
  @Override
  public void onChildAdded(DataSnapshot dataSnapshot, String prevChildKey) {
    // New child added, increment count
    int newCount = count.incrementAndGet();
    System.out.println("Added " + dataSnapshot.getKey() + ", count is " + newCount);
  }

  // ...
});

// The number of children will always be equal to 'count' since the value of
// the dataSnapshot here will include every child_added event triggered before this point.
ref.addListenerForSingleValueEvent(new ValueEventListener() {
  @Override
  public void onDataChange(DataSnapshot dataSnapshot) {
    long numChildren = dataSnapshot.getChildrenCount();
    System.out.println(count.get() + " == " + numChildren);
  }

  @Override
  public void onCancelled(DatabaseError databaseError) {}
});
```

##### Node.js

```javascript
let count = 0;

ref.on('child_added', (snap) => {
  count++;
  console.log('added:', snap.key);
});

// length will always equal count, since snap.val() will include every child_added event
// triggered before this point
ref.once('value', (snap) => {
  console.log('initial data loaded!', snap.numChildren() === count);
});
```

## Detaching Callbacks

Callbacks are removed by specifying the event type and the callback function to be removed, like the following:

##### Java

```java
// Create and attach listener
ValueEventListener listener = new ValueEventListener() {
    // ...
};
ref.addValueEventListener(listener);

// Remove listener
ref.removeEventListener(listener);
```

##### Node.js

```javascript
ref.off('value', originalCallback);
```

If you passed a scope context into `on()`, it must be passed when detaching the callback:

##### Java

```java
// Not applicable for Java
```

##### Node.js

```javascript
ref.off('value', originalCallback, ctx);
```

> [!IMPORTANT]
> If a callback has been added multiple times to a data location, it is called multiple times for each event and you must detach it multiple times in order to remove it completely.

If you would like to remove all callbacks at a location, you can do the following:

##### Java

```java
// No Java equivalent, listeners must be removed individually.
```

##### Node.js

```javascript
// Remove all value callbacks
ref.off('value');

// Remove all callbacks of any type
ref.off();
```

## Reading Data Once


In some cases it may be useful for a callback to be called once and then immediately removed. We've created a helper
function to make this easy:

##### Java

```java
ref.addListenerForSingleValueEvent(new ValueEventListener() {
  @Override
  public void onDataChange(DataSnapshot dataSnapshot) {
    // ...
  }

  @Override
  public void onCancelled(DatabaseError databaseError) {
    // ...
  }
});
```

##### Node.js

```javascript
ref.once('value', (data) => {
  // do some stuff once
});
```

##### Python

```python
# Import database module.
from firebase_admin import db

# Get a database reference to our posts
ref = db.reference('server/saving-data/fireblog/posts')

# Read the data at the posts reference (this is a blocking operation)
print(ref.get())
```

##### Go

```go
// Create a database client from App.
client, err := app.Database(ctx)
if err != nil {
	log.Fatalln("Error initializing database client:", err)
}

// Get a database reference to our posts
ref := client.NewRef("server/saving-data/fireblog/posts")

// Read the data at the posts reference (this is a blocking operation)
var post Post
if err := ref.Get(ctx, &post); err != nil {
	log.Fatalln("Error reading value:", err)
}
```

## Querying Data


With Firebase database queries, you can selectively retrieve data based on various factors. To construct a query in your database, you start by specifying how you want your data to be ordered using one of the ordering functions: `orderByChild()`, `orderByKey()`, or `orderByValue()`. You can then combine these with five other methods to conduct complex queries: `limitToFirst()`,
`limitToLast()`, `startAt()`, `endAt()`, and `equalTo()`.

Since all of us at Firebase think dinosaurs are pretty cool, we'll use a snippet from a sample database of dinosaur facts to demonstrate how you can query data in your Firebase database.:

```
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

You can order data in three ways: by **child key** , by **key** , or by **value**. A basic database query starts with one of these ordering functions, each of which are explained below.

### Ordering by a specified child key

You can order nodes by a common child key by passing that key to `orderByChild()`. For example, to read all dinosaurs ordered by height, you can do
the following:

##### Java

```java
public static class Dinosaur {

  public int height;
  public int weight;

  public Dinosaur(int height, int weight) {
    // ...
  }

}

final DatabaseReference dinosaursRef = database.getReference("dinosaurs");
dinosaursRef.orderByChild("height").addChildEventListener(new ChildEventListener() {
  @Override
  public void onChildAdded(DataSnapshot dataSnapshot, String prevChildKey) {
    Dinosaur dinosaur = dataSnapshot.getValue(Dinosaur.class);
    System.out.println(dataSnapshot.getKey() + " was " + dinosaur.height + " meters tall.");
  }

  // ...
});
```

##### Node.js

```javascript
const ref = db.ref('dinosaurs');

ref.orderByChild('height').on('child_added', (snapshot) => {
  console.log(snapshot.key + ' was ' + snapshot.val().height + ' meters tall');
});
```

##### Python

```python
ref = db.reference('dinosaurs')
snapshot = ref.order_by_child('height').get()
for key, val in snapshot.items():
    print(f'{key} was {val} meters tall')
```

##### Go

```go
// Dinosaur is a json-serializable type.
type Dinosaur struct {
	Height int `json:"height"`
	Width  int `json:"width"`
}

ref := client.NewRef("dinosaurs")

results, err := ref.OrderByChild("height").GetOrdered(ctx)
if err != nil {
	log.Fatalln("Error querying database:", err)
}
for _, r := range results {
	var d Dinosaur
	if err := r.Unmarshal(&d); err != nil {
		log.Fatalln("Error unmarshaling result:", err)
	}
	fmt.Printf("%s was %d meteres tall", r.Key(), d.Height)
}
```


Any node which does not have the child key we're querying on is sorted with a value of `null`, meaning it will come first in the ordering. For details on how data is ordered, see the [How Data is Ordered section](https://firebase.google.com/docs/database/admin/retrieve-data#section-ordered-data).


Queries can also be ordered by deeply nested children, rather than only children one level down. This is useful if you have deeply nested data like this:

```
{
  "lambeosaurus": {
    "dimensions": {
      "height" : 2.1,
      "length" : 12.5,
      "weight": 5000
    }
  },
  "stegosaurus": {
    "dimensions": {
      "height" : 4,
      "length" : 9,
      "weight" : 2500
    }
  }
}
```


To query the height now, you can use the full path to the object rather than a single key:

##### Java

```java
dinosaursRef.orderByChild("dimensions/height").addChildEventListener(new ChildEventListener() {
  @Override
  public void onChildAdded(DataSnapshot dataSnapshot, String prevChildKey) {
    // ...
  }

  // ...
});
```

##### Node.js

```javascript
const ref = db.ref('dinosaurs');
ref.orderByChild('dimensions/height').on('child_added', (snapshot) => {
  console.log(snapshot.key + ' was ' + snapshot.val().height + ' meters tall');
});
```

##### Python

```python
ref = db.reference('dinosaurs')
snapshot = ref.order_by_child('dimensions/height').get()
for key, val in snapshot.items():
    print(f'{key} was {val} meters tall')
```

##### Go

```go
ref := client.NewRef("dinosaurs")

results, err := ref.OrderByChild("dimensions/height").GetOrdered(ctx)
if err != nil {
	log.Fatalln("Error querying database:", err)
}
for _, r := range results {
	var d Dinosaur
	if err := r.Unmarshal(&d); err != nil {
		log.Fatalln("Error unmarshaling result:", err)
	}
	fmt.Printf("%s was %d meteres tall", r.Key(), d.Height)
}
```


Queries can only order by one key at a time. Calling `orderByChild()`
multiple times on the same query throws an error.

> [!IMPORTANT]
>
> #### Using Indexes For Improved Performance
>
>
> If you want to use `orderByChild()` on a production app, you should define the
> keys you are indexing on via the `.indexOn` rule in your Security and
> Firebase Rules. While you are allowed to create these queries ad-hoc on the client, you
> will see greatly improved performance when using `.indexOn`.
> [Read the documentation](https://firebase.google.com/docs/database/security/indexing-data) on the
> `.indexOn` rule for more information.

### Ordering by key


You can also order nodes by their keys using the `orderByKey()` method. The
following example reads all dinosaurs in alphabetical order:

##### Java

```java
dinosaursRef.orderByKey().addChildEventListener(new ChildEventListener() {
  @Override
  public void onChildAdded(DataSnapshot dataSnapshot, String prevChildKey) {
    System.out.println(dataSnapshot.getKey());
  }

  // ...
});
```

##### Node.js

```javascript
var ref = db.ref('dinosaurs');
ref.orderByKey().on('child_added', (snapshot) => {
  console.log(snapshot.key);
});
```

##### Python

```python
ref = db.reference('dinosaurs')
snapshot = ref.order_by_key().get()
print(snapshot)
```

##### Go

```go
ref := client.NewRef("dinosaurs")

results, err := ref.OrderByKey().GetOrdered(ctx)
if err != nil {
	log.Fatalln("Error querying database:", err)
}
snapshot := make([]Dinosaur, len(results))
for i, r := range results {
	var d Dinosaur
	if err := r.Unmarshal(&d); err != nil {
		log.Fatalln("Error unmarshaling result:", err)
	}
	snapshot[i] = d
}
fmt.Println(snapshot)
```

### Ordering by value

You can order nodes by the value of their child keys using the `orderByValue()` method. Let's say the dinosaurs are having a dino sports competition and you're keeping track of their scores in the following format:

```
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

To sort the dinosaurs by their score, you could construct the following query:

##### Java

```java
DatabaseReference scoresRef = database.getReference("scores");
scoresRef.orderByValue().addChildEventListener(new ChildEventListener() {
  @Override
  public void onChildAdded(DataSnapshot dataSnapshot, String prevChildKey) {
    System.out.println("The " + dataSnapshot.getKey() + " score is " + dataSnapshot.getValue());
  }

  // ...
});
```

##### Node.js

```javascript
const scoresRef = db.ref('scores');
scoresRef.orderByValue().on('value', (snapshot) => {
  snapshot.forEach((data) => {
    console.log('The ' + data.key + ' dinosaur\'s score is ' + data.val());
  });
});
```

##### Python

```python
ref = db.reference('scores')
snapshot = ref.order_by_value().get()
for key, val in snapshot.items():
    print(f'The {key} dinosaur\'s score is {val}')
```

##### Go

```go
ref := client.NewRef("scores")

results, err := ref.OrderByValue().GetOrdered(ctx)
if err != nil {
	log.Fatalln("Error querying database:", err)
}
for _, r := range results {
	var score int
	if err := r.Unmarshal(&score); err != nil {
		log.Fatalln("Error unmarshaling result:", err)
	}
	fmt.Printf("The %s dinosaur's score is %d\n", r.Key(), score)
}
```

See the [How Data is Ordered](https://firebase.google.com/docs/database/admin/retrieve-data#section-ordered-data) section for an explanation on how `null`, boolean, string, and object values are sorted when using `orderByValue()`.

> [!IMPORTANT]
>
> #### Indexing on Values for Improved Performance
>
>
> If you want to use `orderByValue()` in a production app, you should add `.value` to your rules at the appropriate index. [Read the documentation](https://firebase.google.com/docs/database/security/indexing-data) on the
> `.indexOn` rule for more information.

## Complex Queries

Now that it is clear how your data is ordered, you can use the **limit** or **range** methods described below to construct more complex queries.

### Limit Queries


The `limitToFirst()` and `limitToLast()` queries are used to set a
maximum number of children to be synced for a given callback. If you set a limit of 100, you
will initially only receive up to 100 `child_added` events. If you have fewer than
100 messages stored in your database, a `child_added` event will fire for each
message. However, if you have over 100 messages, you will only receive a `child_added`
event for 100 of those messages. These are the first 100 ordered messages if you are using
`limitToFirst()` or the last 100 ordered messages if you are using
`limitToLast()`. As items change, you will receive `child_added` events
for items that enter the query and `child_removed` events for items that leave it,
so that the total number stays at 100.


Using the dinosaur facts database and `orderByChild()`, you can find the two heaviest
dinosaurs:

##### Java

```java
dinosaursRef.orderByChild("weight").limitToLast(2).addChildEventListener(new ChildEventListener() {
  @Override
  public void onChildAdded(DataSnapshot dataSnapshot, String prevChildKey) {
    System.out.println(dataSnapshot.getKey());
  }

  // ...
});
```

##### Node.js

```javascript
const ref = db.ref('dinosaurs');
ref.orderByChild('weight').limitToLast(2).on('child_added', (snapshot) => {
  console.log(snapshot.key);
});
```

##### Python

```python
ref = db.reference('dinosaurs')
snapshot = ref.order_by_child('weight').limit_to_last(2).get()
for key in snapshot:
    print(key)
```

##### Go

```go
ref := client.NewRef("dinosaurs")

results, err := ref.OrderByChild("weight").LimitToLast(2).GetOrdered(ctx)
if err != nil {
	log.Fatalln("Error querying database:", err)
}
for _, r := range results {
	fmt.Println(r.Key())
}
```


The `child_added` callback is triggered exactly two times, unless there are
less than two dinosaurs stored in the database. It will also get fired for every new, heavier dinosaur that gets added to the database.
In Python, the query directly returns an `OrderedDict` containing the two heaviest dinosaurs.


Similarly, you can find the two shortest dinosaurs by using `limitToFirst()`:

##### Java

```java
dinosaursRef.orderByChild("weight").limitToFirst(2).addChildEventListener(new ChildEventListener() {
  @Override
  public void onChildAdded(DataSnapshot dataSnapshot, String prevChildKey) {
    System.out.println(dataSnapshot.getKey());
  }

  // ...
});
```

##### Node.js

```javascript
const ref = db.ref('dinosaurs');
ref.orderByChild('height').limitToFirst(2).on('child_added', (snapshot) => {
  console.log(snapshot.key);
});
```

##### Python

```python
ref = db.reference('dinosaurs')
snapshot = ref.order_by_child('height').limit_to_first(2).get()
for key in snapshot:
    print(key)
```

##### Go

```go
ref := client.NewRef("dinosaurs")

results, err := ref.OrderByChild("height").LimitToFirst(2).GetOrdered(ctx)
if err != nil {
	log.Fatalln("Error querying database:", err)
}
for _, r := range results {
	fmt.Println(r.Key())
}
```


The `child_added` callback is triggered exactly two times, unless there are less than two dinosaurs stored in the database. It will also get fired again if one of the first two dinosaurs is removed from the database, as a new dinosaur will now be the second shortest. In Python, the query directly returns an `OrderedDict` containing the shortest dinosaurs.

You can also conduct limit queries with `orderByValue()`. If you want to create a leaderboard with the top 3 highest scoring dino sports dinosaurs, you could do the following:

##### Java

```java
scoresRef.orderByValue().limitToFirst(3).addChildEventListener(new ChildEventListener() {
  @Override
  public void onChildAdded(DataSnapshot dataSnapshot, String prevChildKey) {
    System.out.println("The " + dataSnapshot.getKey() + " score is " + dataSnapshot.getValue());
  }

  // ...
});
```

##### Node.js

```javascript
const scoresRef = db.ref('scores');
scoresRef.orderByValue().limitToLast(3).on('value', (snapshot)  =>{
  snapshot.forEach((data) => {
    console.log('The ' + data.key + ' dinosaur\'s score is ' + data.val());
  });
});
```

##### Python

```python
scores_ref = db.reference('scores')
snapshot = scores_ref.order_by_value().limit_to_last(3).get()
for key, val in snapshot.items():
    print(f'The {key} dinosaur\'s score is {val}')
```

##### Go

```go
ref := client.NewRef("scores")

results, err := ref.OrderByValue().LimitToLast(3).GetOrdered(ctx)
if err != nil {
	log.Fatalln("Error querying database:", err)
}
for _, r := range results {
	var score int
	if err := r.Unmarshal(&score); err != nil {
		log.Fatalln("Error unmarshaling result:", err)
	}
	fmt.Printf("The %s dinosaur's score is %d\n", r.Key(), score)
}
```

### Range Queries


Using `startAt()`, `endAt()`, and `equalTo()` allows you to
choose arbitrary starting and ending points for your queries. For example, if you wanted to
find all dinosaurs that are at least three meters tall, you can combine `orderByChild()`
and `startAt()`:

##### Java

```java
dinosaursRef.orderByChild("height").startAt(3).addChildEventListener(new ChildEventListener() {
  @Override
  public void onChildAdded(DataSnapshot dataSnapshot, String prevChildKey) {
    System.out.println(dataSnapshot.getKey());
  }

  // ...
});
```

##### Node.js

```javascript
const ref = db.ref('dinosaurs');
ref.orderByChild('height').startAt(3).on('child_added', (snapshot) => {
  console.log(snapshot.key);
});
```

##### Python

```python
ref = db.reference('dinosaurs')
snapshot = ref.order_by_child('height').start_at(3).get()
for key in snapshot:
    print(key)
```

##### Go

```go
ref := client.NewRef("dinosaurs")

results, err := ref.OrderByChild("height").StartAt(3).GetOrdered(ctx)
if err != nil {
	log.Fatalln("Error querying database:", err)
}
for _, r := range results {
	fmt.Println(r.Key())
}
```


You can use `endAt()` to find all dinosaurs whose names come before Pterodactyl
lexicographically:

##### Java

```java
dinosaursRef.orderByKey().endAt("pterodactyl").addChildEventListener(new ChildEventListener() {
  @Override
  public void onChildAdded(DataSnapshot dataSnapshot, String prevChildKey) {
    System.out.println(dataSnapshot.getKey());
  }

  // ...
});
```

##### Node.js

```javascript
const ref = db.ref('dinosaurs');
ref.orderByKey().endAt('pterodactyl').on('child_added', (snapshot) => {
  console.log(snapshot.key);
});
```

##### Python

```python
ref = db.reference('dinosaurs')
snapshot = ref.order_by_key().end_at('pterodactyl').get()
for key in snapshot:
    print(key)
```

##### Go

```go
ref := client.NewRef("dinosaurs")

results, err := ref.OrderByKey().EndAt("pterodactyl").GetOrdered(ctx)
if err != nil {
	log.Fatalln("Error querying database:", err)
}
for _, r := range results {
	fmt.Println(r.Key())
}
```

> [!IMPORTANT]
> `startAt()` and `endAt()` are inclusive, meaning "pterodactyl" will match the query above.


You can combine `startAt()` and `endAt()` to limit both ends of your
query. The following example finds all dinosaurs whose name starts with the letter "b":

##### Java

```java
dinosaursRef.orderByKey().startAt("b").endAt("b\uf8ff").addChildEventListener(new ChildEventListener() {
  @Override
  public void onChildAdded(DataSnapshot dataSnapshot, String prevChildKey) {
    System.out.println(dataSnapshot.getKey());
  }

  // ...
});
```

##### Node.js

```javascript
var ref = db.ref('dinosaurs');
ref.orderByKey().startAt('b').endAt('b\uf8ff').on('child_added', (snapshot) => {
  console.log(snapshot.key);
});
```

##### Python

```python
ref = db.reference('dinosaurs')
snapshot = ref.order_by_key().start_at('b').end_at('b\uf8ff').get()
for key in snapshot:
    print(key)
```

##### Go

```go
ref := client.NewRef("dinosaurs")

results, err := ref.OrderByKey().StartAt("b").EndAt("b\uf8ff").GetOrdered(ctx)
if err != nil {
	log.Fatalln("Error querying database:", err)
}
for _, r := range results {
	fmt.Println(r.Key())
}
```

> [!IMPORTANT]
> The `\uf8ff` character used in the query above is a very high code point in the Unicode range. Because it is after most regular characters in Unicode, the query matches all values that start with a b.


The `equalTo()` method allows you to filter based on exact matches. As is the case
with the other range queries, it will fire for each matching child node. For example, you can
use the following query to find all dinosaurs which are 25 meters tall:

##### Java

```java
dinosaursRef.orderByChild("height").equalTo(25).addChildEventListener(new ChildEventListener() {
  @Override
  public void onChildAdded(DataSnapshot dataSnapshot, String prevChildKey) {
    System.out.println(dataSnapshot.getKey());
  }

  // ...
});
```

##### Node.js

```javascript
const ref = db.ref('dinosaurs');
ref.orderByChild('height').equalTo(25).on('child_added', (snapshot) => {
  console.log(snapshot.key);
});
```

##### Python

```python
ref = db.reference('dinosaurs')
snapshot = ref.order_by_child('height').equal_to(25).get()
for key in snapshot:
    print(key)
```

##### Go

```go
ref := client.NewRef("dinosaurs")

results, err := ref.OrderByChild("height").EqualTo(25).GetOrdered(ctx)
if err != nil {
	log.Fatalln("Error querying database:", err)
}
for _, r := range results {
	fmt.Println(r.Key())
}
```


Range queries are also useful when you need to paginate your data.

> [!IMPORTANT]
> You can also combine `orderByValue()` with `startAt()` and `endAt()` to construct range queries.

### Putting it all together


You can combine all of these techniques to create complex queries. For example, you can find
the name of the dinosaur that is just shorter than Stegosaurus:

##### Java

```java
dinosaursRef.child("stegosaurus").child("height").addValueEventListener(new ValueEventListener() {
  @Override
  public void onDataChange(DataSnapshot stegoHeightSnapshot) {
    Integer favoriteDinoHeight = stegoHeightSnapshot.getValue(Integer.class);
    Query query = dinosaursRef.orderByChild("height").endAt(favoriteDinoHeight).limitToLast(2);
    query.addValueEventListener(new ValueEventListener() {
      @Override
      public void onDataChange(DataSnapshot dataSnapshot) {
        // Data is ordered by increasing height, so we want the first entry
        DataSnapshot firstChild = dataSnapshot.getChildren().iterator().next();
        System.out.println("The dinosaur just shorter than the stegosaurus is: " + firstChild.getKey());
      }

      @Override
      public void onCancelled(DatabaseError databaseError) {
        // ...
      }
    });
  }

  @Override
  public void onCancelled(DatabaseError databaseError) {
    // ...
  }
});
```

##### Node.js

```javascript
  const ref = db.ref('dinosaurs');
  ref.child('stegosaurus').child('height').on('value', (stegosaurusHeightSnapshot) => {
    const favoriteDinoHeight = stegosaurusHeightSnapshot.val();

    const queryRef = ref.orderByChild('height').endAt(favoriteDinoHeight).limitToLast(2);
    queryRef.on('value', (querySnapshot) => {
      if (querySnapshot.numChildren() === 2) {
        // Data is ordered by increasing height, so we want the first entry
        querySnapshot.forEach((dinoSnapshot) => {
          console.log('The dinosaur just shorter than the stegasaurus is ' + dinoSnapshot.key);

          // Returning true means that we will only loop through the forEach() one time
          return true;
        });
      } else {
        console.log('The stegosaurus is the shortest dino');
      }
    });
});
```

##### Python

```python
ref = db.reference('dinosaurs')
favotire_dino_height = ref.child('stegosaurus').child('height').get()
query = ref.order_by_child('height').end_at(favotire_dino_height).limit_to_last(2)
snapshot = query.get()
if len(snapshot) == 2:
    # Data is ordered by increasing height, so we want the first entry.
    # Second entry is stegosarus.
    for key in snapshot:
        print(f'The dinosaur just shorter than the stegosaurus is {key}')
        return
else:
    print('The stegosaurus is the shortest dino')
```

##### Go

```go
ref := client.NewRef("dinosaurs")

var favDinoHeight int
if err := ref.Child("stegosaurus").Child("height").Get(ctx, &favDinoHeight); err != nil {
	log.Fatalln("Error querying database:", err)
}

query := ref.OrderByChild("height").EndAt(favDinoHeight).LimitToLast(2)
results, err := query.GetOrdered(ctx)
if err != nil {
	log.Fatalln("Error querying database:", err)
}
if len(results) == 2 {
	// Data is ordered by increasing height, so we want the first entry.
	// Second entry is stegosarus.
	fmt.Printf("The dinosaur just shorter than the stegosaurus is %s\n", results[0].Key())
} else {
	fmt.Println("The stegosaurus is the shortest dino")
}
```

## How Data is Ordered


This section explains how your data is ordered when using each of the four ordering functions.

### orderByChild

When using `orderByChild()`, data that contains the specified child key is ordered as follows:

1. Children with a `null` value for the specified child key come first.
2. Children with a value of `false` for the specified child key come next. If multiple children have a value of `false`, they are sorted [lexicographically](http://en.wikipedia.org/wiki/Lexicographical_order) by key.
3. Children with a value of `true` for the specified child key come next. If multiple children have a value of `true`, they are sorted lexicographically by key.
4. Children with a numeric value come next, sorted in ascending order. If multiple children have the same numerical value for the specified child node, they are sorted by key.
5. Strings come after numbers, and are sorted lexicographically in ascending order. If multiple children have the same value for the specified child node, they are ordered lexicographically by key.
6. Objects come last, and sorted lexicographically by key in ascending order.

### orderByKey

When using `orderByKey()` to sort your data, data is returned in ascending order by key as follows. Keep in mind that keys can only be strings.

1. Children with a key that can be parsed as a 32-bit integer come first, sorted in ascending order.
2. Children with a string value as their key come next, sorted lexicographically in ascending order.

### orderByValue

When using `orderByValue()`, children are ordered by their value. The ordering criteria is the same as in `orderByChild()`, except the value of the node is used instead of the value of a specified child key.

<br />

<br />