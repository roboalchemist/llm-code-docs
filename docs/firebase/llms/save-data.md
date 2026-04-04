# Source: https://firebase.google.com/docs/database/unity/save-data.md.txt

# Source: https://firebase.google.com/docs/database/rest/save-data.md.txt

# Source: https://firebase.google.com/docs/database/cpp/save-data.md.txt

# Source: https://firebase.google.com/docs/database/admin/save-data.md.txt

# Source: https://firebase.google.com/docs/database/rest/save-data.md.txt

# Source: https://firebase.google.com/docs/database/cpp/save-data.md.txt

# Source: https://firebase.google.com/docs/database/admin/save-data.md.txt

<br />

This document covers the four methods for writing data to yourFirebase Realtime Database: set, update, push, and transactions support.

## Ways to Save Data

|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| set         | Write or replace data to a**defined path** , like`messages/users/<username>`                                                                                                  |
| update      | Update some of the keys for a defined path without replacing all of the data                                                                                                  |
| push        | **Add to a list of data** in the database. Every time you push a new node onto a list, your database generates a unique key, like`messages/users/<unique-user-id>/<username>` |
| transaction | Use transactions when working with complex data that could be corrupted by concurrent updates                                                                                 |

## Saving Data

The basic database write operation is a set which saves new data to the specified database reference, replacing any existing data at that path. To understand set, we'll build a simple blogging app. The data for your app is stored at this database reference:  

##### Java

```java
final FirebaseDatabase database = FirebaseDatabase.getInstance();
DatabaseReference ref = database.getReference("server/saving-data/fireblog");
```

##### Node.js

```javascript
// Import Admin SDK
const { getDatabase } = require('firebase-admin/database');

// Get a database reference to our blog
const db = getDatabase();
const ref = db.ref('server/saving-data/fireblog');
```

##### Python

```python
# Import database module.
from firebase_admin import db

# Get a database reference to our blog.
ref = db.reference('server/saving-data/fireblog')
```

##### Go

```go
// Create a database client from App.
client, err := app.Database(ctx)
if err != nil {
	log.Fatalln("Error initializing database client:", err)
}

// Get a database reference to our blog.
ref := client.NewRef("server/saving-data/fireblog")
```

Let's start by saving some user data. We'll store each user by a unique username, and we'll also store their full name and date of birth. Since each user will have a unique username, it makes sense to use the set method here instead of the push method since you already have the key and don't need to create one.

First, create a database reference to your user data. Then use`set()`/`setValue()`to save a user object to the database with the user's username, full name, and birthday. You can pass set a string, number, boolean,`null`, array or any JSON object. Passing`null`will remove the data at the specified location. In this case you'll pass it an object:  

##### Java

```java
public static class User {

  public String date_of_birth;
  public String full_name;
  public String nickname;

  public User(String dateOfBirth, String fullName) {
    // ...
  }

  public User(String dateOfBirth, String fullName, String nickname) {
    // ...
  }

}

DatabaseReference usersRef = ref.child("users");

Map<String, User> users = new HashMap<>();
users.put("alanisawesome", new User("June 23, 1912", "Alan Turing"));
users.put("gracehop", new User("December 9, 1906", "Grace Hopper"));

usersRef.setValueAsync(users);
```

##### Node.js

```javascript
const usersRef = ref.child('users');
usersRef.set({
  alanisawesome: {
    date_of_birth: 'June 23, 1912',
    full_name: 'Alan Turing'
  },
  gracehop: {
    date_of_birth: 'December 9, 1906',
    full_name: 'Grace Hopper'
  }
});
```

##### Python

```python
users_ref = ref.child('users')
users_ref.set({
    'alanisawesome': {
        'date_of_birth': 'June 23, 1912',
        'full_name': 'Alan Turing'
    },
    'gracehop': {
        'date_of_birth': 'December 9, 1906',
        'full_name': 'Grace Hopper'
    }
})
```

##### Go

```go
// User is a json-serializable type.
type User struct {
	DateOfBirth string `json:"date_of_birth,omitempty"`
	FullName    string `json:"full_name,omitempty"`
	Nickname    string `json:"nickname,omitempty"`
}

usersRef := ref.Child("users")
err := usersRef.Set(ctx, map[string]*User{
	"alanisawesome": {
		DateOfBirth: "June 23, 1912",
		FullName:    "Alan Turing",
	},
	"gracehop": {
		DateOfBirth: "December 9, 1906",
		FullName:    "Grace Hopper",
	},
})
if err != nil {
	log.Fatalln("Error setting value:", err)
}
```

When a JSON object is saved to the database, the object properties are automatically mapped to database child locations in a nested fashion. Now if you navigate to the URL<https://docs-examples.firebaseio.com/server/saving-data/fireblog/users/alanisawesome/full_name>, we'll see the value "Alan Turing". You can also save data directly to a child location:  

##### Java

```java
usersRef.child("alanisawesome").setValueAsync(new User("June 23, 1912", "Alan Turing"));
usersRef.child("gracehop").setValueAsync(new User("December 9, 1906", "Grace Hopper"));
```

##### Node.js

```javascript
const usersRef = ref.child('users');
usersRef.child('alanisawesome').set({
  date_of_birth: 'June 23, 1912',
  full_name: 'Alan Turing'
});
usersRef.child('gracehop').set({
  date_of_birth: 'December 9, 1906',
  full_name: 'Grace Hopper'
});
```

##### Python

```python
users_ref.child('alanisawesome').set({
    'date_of_birth': 'June 23, 1912',
    'full_name': 'Alan Turing'
})
users_ref.child('gracehop').set({
    'date_of_birth': 'December 9, 1906',
    'full_name': 'Grace Hopper'
})
```

##### Go

```go
if err := usersRef.Child("alanisawesome").Set(ctx, &User{
	DateOfBirth: "June 23, 1912",
	FullName:    "Alan Turing",
}); err != nil {
	log.Fatalln("Error setting value:", err)
}

if err := usersRef.Child("gracehop").Set(ctx, &User{
	DateOfBirth: "December 9, 1906",
	FullName:    "Grace Hopper",
}); err != nil {
	log.Fatalln("Error setting value:", err)
}
```

The above two examples - writing both values at the same time as an object and writing them separately to child locations - will result in the same data being saved to your database:  

```scdoc
{
  "users": {
    "alanisawesome": {
      "date_of_birth": "June 23, 1912",
      "full_name": "Alan Turing"
    },
    "gracehop": {
      "date_of_birth": "December 9, 1906",
      "full_name": "Grace Hopper"
    }
  }
}
```

The first example will only trigger one event on clients that are watching the data, whereas the second example will trigger two. It is important to note that if data already existed at`usersRef`, the first approach would overwrite it, but the second method would only modify the value of each separate child node while leaving other children of`usersRef`unchanged.
| Setting the value will overwrite the data at the specified location, including any child nodes.

## Updating Saved Data

If you want to write to multiple children of a database location at the same time without overwriting other child nodes, you can use the update method as shown below:  

##### Java

```java
DatabaseReference hopperRef = usersRef.child("gracehop");
Map<String, Object> hopperUpdates = new HashMap<>();
hopperUpdates.put("nickname", "Amazing Grace");

hopperRef.updateChildrenAsync(hopperUpdates);
```

##### Node.js

```javascript
const usersRef = ref.child('users');
const hopperRef = usersRef.child('gracehop');
hopperRef.update({
  'nickname': 'Amazing Grace'
});
```

##### Python

```python
hopper_ref = users_ref.child('gracehop')
hopper_ref.update({
    'nickname': 'Amazing Grace'
})
```

##### Go

```go
hopperRef := usersRef.Child("gracehop")
if err := hopperRef.Update(ctx, map[string]interface{}{
	"nickname": "Amazing Grace",
}); err != nil {
	log.Fatalln("Error updating child:", err)
}
```

This will update Grace's data to include her nickname. If you had used set here instead of update, it would have deleted both`full_name`and`date_of_birth`from your`hopperRef`.

TheFirebase Realtime Databasealso supports multi-path updates. This means that update can now update values at multiple locations in your database at the same time, a powerful feature which allows helps you[denormalize your data](https://firebase.googleblog.com/2013/04/denormalizing-your-data-is-normal.html). Using multi-path updates, you can add nicknames to both Grace and Alan at the same time:  

##### Java

```java
Map<String, Object> userUpdates = new HashMap<>();
userUpdates.put("alanisawesome/nickname", "Alan The Machine");
userUpdates.put("gracehop/nickname", "Amazing Grace");

usersRef.updateChildrenAsync(userUpdates);
```

##### Node.js

```javascript
const usersRef = ref.child('users');
usersRef.update({
  'alanisawesome/nickname': 'Alan The Machine',
  'gracehop/nickname': 'Amazing Grace'
});
```

##### Python

```python
users_ref.update({
    'alanisawesome/nickname': 'Alan The Machine',
    'gracehop/nickname': 'Amazing Grace'
})
```

##### Go

```go
if err := usersRef.Update(ctx, map[string]interface{}{
	"alanisawesome/nickname": "Alan The Machine",
	"gracehop/nickname":      "Amazing Grace",
}); err != nil {
	log.Fatalln("Error updating children:", err)
}
```

After this update, both Alan and Grace have had their nicknames added:  

```scdoc
{
  "users": {
    "alanisawesome": {
      "date_of_birth": "June 23, 1912",
      "full_name": "Alan Turing",
      "nickname": "Alan The Machine"
    },
    "gracehop": {
      "date_of_birth": "December 9, 1906",
      "full_name": "Grace Hopper",
      "nickname": "Amazing Grace"
    }
  }
}
```

Note that trying to update objects by writing objects with the paths included will result in different behavior. Let's take a look at what happens if you instead try to update Grace and Alan this way:  

##### Java

```java
Map<String, Object> userNicknameUpdates = new HashMap<>();
userNicknameUpdates.put("alanisawesome", new User(null, null, "Alan The Machine"));
userNicknameUpdates.put("gracehop", new User(null, null, "Amazing Grace"));

usersRef.updateChildrenAsync(userNicknameUpdates);
```

##### Node.js

```javascript
const usersRef = ref.child('users');
usersRef.update({
  'alanisawesome': {
    'nickname': 'Alan The Machine'
  },
  'gracehop': {
    'nickname': 'Amazing Grace'
  }
});
```

##### Python

```python
users_ref.update({
    'alanisawesome': {
        'nickname': 'Alan The Machine'
    },
    'gracehop': {
        'nickname': 'Amazing Grace'
    }
})
```

##### Go

```go
if err := usersRef.Update(ctx, map[string]interface{}{
	"alanisawesome": &User{Nickname: "Alan The Machine"},
	"gracehop":      &User{Nickname: "Amazing Grace"},
}); err != nil {
	log.Fatalln("Error updating children:", err)
}
```

This results in different behavior, namely overwriting the entire`/users`node:  

```text
{
  "users": {
    "alanisawesome": {
      "nickname": "Alan The Machine"
    },
    "gracehop": {
      "nickname": "Amazing Grace"
    }
  }
}
```
|
| #### Updating Nested Data
|
| Given a single key path like`alanisawesome`, only the data at the first child level are updated, and any data passed in beyond the first child level is a treated as a set operation. Multi-path behavior allows longer paths (like`alanisawesome/nickname`) to be used without overwriting data. This is why the first example differs from the second example.

### Adding a Completion Callback

In Node.js and Java Admin SDKs, if you'd like to know when your data has been committed, you can add a completion callback. Both set and update methods in these SDKs take an optional completion callback that is called when the write has been committed to the database. If the call was unsuccessful for some reason, the callback is passed an error object indicating why the failure occurred. In Python and Go Admin SDKs, all write methods are blocking. That is, the write methods do not return until the writes are committed to the database.  

##### Java

```java
DatabaseReference dataRef = ref.child("data");
dataRef.setValue("I'm writing data", new DatabaseReference.CompletionListener() {
  @Override
  public void onComplete(DatabaseError databaseError, DatabaseReference databaseReference) {
    if (databaseError != null) {
      System.out.println("Data could not be saved " + databaseError.getMessage());
    } else {
      System.out.println("Data saved successfully.");
    }
  }
});
```

##### Node.js

```javascript
dataRef.set('I\'m writing data', (error) => {
  if (error) {
    console.log('Data could not be saved.' + error);
  } else {
    console.log('Data saved successfully.');
  }
});
```

## Saving Lists of Data

When creating lists of data, it is important to keep in mind the multi-user nature of most applications and adjust your list structure accordingly. Expanding on the example above, let's add blog posts to your app. Your first instinct might be to use set to store children with auto-incrementing integer indexes, like the following:  

```scilab
// NOT RECOMMENDED - use push() instead!
{
  "posts": {
    "0": {
      "author": "gracehop",
      "title": "Announcing COBOL, a New Programming Language"
    },
    "1": {
      "author": "alanisawesome",
      "title": "The Turing Machine"
    }
  }
}
```
|
| #### Push vs Transaction
|
| When working with lists of data`push()`ensures a unique and chronological key. You may be tempted to use transactions instead to generate your own keys, but push is a far better choice. Transactions are slower and more complex. They require one or more round trips to the server. A key generated by \`push()\` on the client works while offline and is optimized for performance.

If a user adds a new post it would be stored as`/posts/2`. This would work if only a single author were adding posts, but in your collaborative blogging application many users may add posts at the same time. If two authors write to`/posts/2`simultaneously, then one of the posts would be deleted by the other.

To solve this, the**Firebase clients provide a`push()`function that generates a unique*key*for each new child**. By using unique child keys, several clients can add children to the same location at the same time without worrying about write conflicts.  

##### Java

```java
public static class Post {

  public String author;
  public String title;

  public Post(String author, String title) {
    // ...
  }

}

DatabaseReference postsRef = ref.child("posts");

DatabaseReference newPostRef = postsRef.push();
newPostRef.setValueAsync(new Post("gracehop", "Announcing COBOL, a New Programming Language"));

// We can also chain the two calls together
postsRef.push().setValueAsync(new Post("alanisawesome", "The Turing Machine"));
```

##### Node.js

```javascript
const newPostRef = postsRef.push();
newPostRef.set({
  author: 'gracehop',
  title: 'Announcing COBOL, a New Programming Language'
});

// we can also chain the two calls together
postsRef.push().set({
  author: 'alanisawesome',
  title: 'The Turing Machine'
});
```

##### Python

```python
posts_ref = ref.child('posts')

new_post_ref = posts_ref.push()
new_post_ref.set({
    'author': 'gracehop',
    'title': 'Announcing COBOL, a New Programming Language'
})

# We can also chain the two calls together
posts_ref.push().set({
    'author': 'alanisawesome',
    'title': 'The Turing Machine'
})
```

##### Go

```go
// Post is a json-serializable type.
type Post struct {
	Author string `json:"author,omitempty"`
	Title  string `json:"title,omitempty"`
}

postsRef := ref.Child("posts")

newPostRef, err := postsRef.Push(ctx, nil)
if err != nil {
	log.Fatalln("Error pushing child node:", err)
}

if err := newPostRef.Set(ctx, &Post{
	Author: "gracehop",
	Title:  "Announcing COBOL, a New Programming Language",
}); err != nil {
	log.Fatalln("Error setting value:", err)
}

// We can also chain the two calls together
if _, err := postsRef.Push(ctx, &Post{
	Author: "alanisawesome",
	Title:  "The Turing Machine",
}); err != nil {
	log.Fatalln("Error pushing child node:", err)
}
```

The unique key is based on a timestamp, so list items will automatically be ordered chronologically. Because Firebase generates a unique key for each blog post, no write conflicts will occur if multiple users add a post at the same time. Your database data now looks like this:  

```text
{
  "posts": {
    "-JRHTHaIs-jNPLXOQivY": {
      "author": "gracehop",
      "title": "Announcing COBOL, a New Programming Language"
    },
    "-JRHTHaKuITFIhnj02kE": {
      "author": "alanisawesome",
      "title": "The Turing Machine"
    }
  }
}
```

In JavaScript, Python and Go, the pattern of calling`push()`and then immediately calling`set()`is so common that the Firebase SDK lets you combine them by passing the data to be set directly to`push()`as follows:  

##### Java

```java
// No Java equivalent
```

##### Node.js

```javascript
// This is equivalent to the calls to push().set(...) above
postsRef.push({
  author: 'gracehop',
  title: 'Announcing COBOL, a New Programming Language'
});;
```

##### Python

```python
# This is equivalent to the calls to push().set(...) above
posts_ref.push({
    'author': 'gracehop',
    'title': 'Announcing COBOL, a New Programming Language'
})
```

##### Go

```go
if _, err := postsRef.Push(ctx, &Post{
	Author: "gracehop",
	Title:  "Announcing COBOL, a New Programming Language",
}); err != nil {
	log.Fatalln("Error pushing child node:", err)
}
```

### Getting the unique key generated by push()

Calling`push()`will return a reference to the new data path, which you can use to get the key or set data to it. The following code will result in the same data as the above example, but now we'll have access to the unique key that was generated:  

##### Java

```java
// Generate a reference to a new location and add some data using push()
DatabaseReference pushedPostRef = postsRef.push();

// Get the unique ID generated by a push()
String postId = pushedPostRef.getKey();
```

##### Node.js

```javascript
// Generate a reference to a new location and add some data using push()
const newPostRef = postsRef.push();

// Get the unique key generated by push()
const postId = newPostRef.key;
```

##### Python

```python
# Generate a reference to a new location and add some data using push()
new_post_ref = posts_ref.push()

# Get the unique key generated by push()
post_id = new_post_ref.key
```

##### Go

```go
// Generate a reference to a new location and add some data using Push()
newPostRef, err := postsRef.Push(ctx, nil)
if err != nil {
	log.Fatalln("Error pushing child node:", err)
}

// Get the unique key generated by Push()
postID := newPostRef.Key
```

As you can see, you can get the value of the unique key from your`push()`reference.

In the next section on[Retrieving Data](https://firebase.google.com/docs/database/admin/retrieve-data), we'll learn how to read this data from a Firebase database.

## Saving Transactional Data

When working with complex data that could be corrupted by concurrent modifications, such as incremental counters, the SDK provides a[transaction operation](https://firebase.google.com/docs/reference/node/firebase.database.Reference#transaction).

In Java and Node.js, you give the transaction operation two callbacks: an update function and an optional completion callback. In Python and Go, the transaction operation is blocking and therefore it only accepts the update function.

The update function takes the current state of the data as an argument and should return the new desired state you would like to write. For example, if you wanted to increment the number of upvotes on a specific blog post, you would write a transaction like the following:  

##### Java

```java
DatabaseReference upvotesRef = ref.child("server/saving-data/fireblog/posts/-JRHTHaIs-jNPLXOQivY/upvotes");
upvotesRef.runTransaction(new Transaction.Handler() {
  @Override
  public Transaction.Result doTransaction(MutableData mutableData) {
    Integer currentValue = mutableData.getValue(Integer.class);
    if (currentValue == null) {
      mutableData.setValue(1);
    } else {
      mutableData.setValue(currentValue + 1);
    }

    return Transaction.success(mutableData);
  }

  @Override
  public void onComplete(
      DatabaseError databaseError, boolean committed, DataSnapshot dataSnapshot) {
    System.out.println("Transaction completed");
  }
});
```

##### Node.js

```javascript
const upvotesRef = db.ref('server/saving-data/fireblog/posts/-JRHTHaIs-jNPLXOQivY/upvotes');
upvotesRef.transaction((current_value) => {
  return (current_value || 0) + 1;
});
```

##### Python

```python
def increment_votes(current_value):
    return current_value + 1 if current_value else 1

upvotes_ref = db.reference('server/saving-data/fireblog/posts/-JRHTHaIs-jNPLXOQivY/upvotes')
try:
    new_vote_count = upvotes_ref.transaction(increment_votes)
    print('Transaction completed')
except db.TransactionAbortedError:
    print('Transaction failed to commit')
```

##### Go

```go
fn := func(t db.TransactionNode) (interface{}, error) {
	var currentValue int
	if err := t.Unmarshal(&currentValue); err != nil {
		return nil, err
	}
	return currentValue + 1, nil
}

ref := client.NewRef("server/saving-data/fireblog/posts/-JRHTHaIs-jNPLXOQivY/upvotes")
if err := ref.Transaction(ctx, fn); err != nil {
	log.Fatalln("Transaction failed to commit:", err)
}
```

The above example checks to see if the counter is`null`or hasn't been incremented yet, since transactions can be called with`null`if no default value was written.

If the above code had been run without a transaction function and two clients attempted to increment it simultaneously, they would both write`1`as the new value, resulting in one increment instead of two.
|
| #### Transaction Function is Called Multiple Times
|
| Your transaction handler is called multiple times and must be able to handle`null`data. Even if there is existing data in your database it may not be locally cached when the transaction function is run.

## Network Connectivity and Offline Writes

| In Node.js and Java if a client loses network connection, your app will continue functioning correctly. The Python and Go Admin SDKs require network connectivity as they use the[Firebase REST API](https://firebase.google.com/docs/database/rest/start)to communicate with the database server. Invoking database operations on Python or Go Admin SDKs without network connectivity results in exceptions.

Firebase Node.js and Java clients maintain their own internal version of any active data. When data is written, it is written to this local version first. The client then synchronizes that data with the database and with other clients on a 'best-effort' basis.

As a result, all writes to the database will trigger local events immediately, before any data has even been written to the database. This means that when you write an application using Firebase,**your app will remain responsive regardless of network latency or Internet connectivity.**

Once connectivity is reestablished, we'll receive the appropriate set of events so that the client "catches up" with the current server state, without having to write any custom code.

## Securing Your Data

TheFirebase Realtime Databasehas a security language that lets you define which users have read and write access to different nodes of your data. You can read more about it in[Secure Your Data](https://firebase.google.com/docs/database/security/securing-data).