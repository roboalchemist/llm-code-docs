# Source: https://firebase.google.com/docs/database/cpp/retrieve-data.md.txt

This document covers the basics of retrieving data and how to order and filter
Firebase data.

## Before you begin

Make sure you've setup your app and can access the database as covered in
the [`Get Started`](https://firebase.google.com/docs/database/cpp/start) guide.

## Retrieving Data

Firebase data is retrieved by either a one time call to `GetValue()` or
attaching to a `ValueListener` on a `FirebaseDatabase` reference. The value
listener is called once for the initial state of the data and again anytime the
data changes.

## Get a DatabaseReference

To write data to the Database, you need an instance of `DatabaseReference`:

```c++
    // Get the root reference location of the database.
    firebase::database::DatabaseReference dbref = database->GetReference();
```

## Read data once

You can use the `GetValue()` method to read a static snapshot of the
contents at a given path once. The task result will contain a snapshot
containing all data at that location, including child data. If there is no data,
the snapshot returned is `null`.

```c++
  firebase::Future&ltfirebase::database::DataSnapshot&gt result =
    dbRef.GetReference("Leaders").GetValue();
```

At the point the request has been made but we have to wait for the Future to
complete before we can read the value. Since games typically run in a loop, and
are less callback driven than other applications, you'll typically poll for
completion.

```c++
  // In the game loop that polls for the result...

  if (result.status() != firebase::kFutureStatusPending) {
    if (result.status() != firebase::kFutureStatusComplete) {
      LogMessage("ERROR: GetValue() returned an invalid result.");
      // Handle the error...
    } else if (result.error() != firebase::database::kErrorNone) {
      LogMessage("ERROR: GetValue() returned error %d: %s", result.error(),
                 result.error_message());
      // Handle the error...
    } else {
      firebase::database::DataSnapshot snapshot = result.result();
      // Do something with the snapshot...
    }
  }
```

This shows some basic error checking, see the
[firebase::Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future) reference for more
information on error checking, and ways to determine when the result is ready.

## Listen for events

You can add listeners to subscribe on changes to data:

### `ValueListener` base class

| Callback | Typical usage |
|---|---|
| `OnValueChanged` | Read and listen for changes to the entire contents of a path. |

### `OnChildListener` base class

|---|---|
| `OnChildAdded` | Retrieve lists of items or listen for additions to a list of items. Suggested use with `OnChildChanged` and `OnChildRemoved` to monitor changes to lists. |
| `OnChildChanged` | Listen for changes to the items in a list. Use with `OnChildAdded` and `OnChildRemoved` to monitor changes to lists. |
| `OnChildRemoved` | Listen for items being removed from a list. Use with `OnChildAdded` and `OnChildChanged` to monitor changes to lists. |
| `OnChildMoved` | Listen for changes to the order of items in an ordered list. `OnChildMoved` callbacks always follow the `OnChildChanged` callbacks due to the item's order changing (based on your current order-by method). |

### ValueListener class

You can use the `OnValueChanged` callbacks to subscribe to changes to the
contents at a given path. This callback is triggered once when the listener is
attached and again every time the data, including children, changes. The
callback is passed a snapshot containing all data at that location, including
child data. If there is no data, the snapshot returned is `null`.

> [!IMPORTANT]
> **Important:** The `OnValueChanged` event is called every time data is changed at the specified database reference, including changes to children. To limit the size of your snapshots, attach only at the highest level needed for watching changes. For example, attaching a listener to the root of your database is not recommended.

The following example demonstrates a game retrieving the scores of a leaderboard
from the database:

```c++
  class LeadersValueListener : public firebase::database::ValueListener {
   public:
    void OnValueChanged(
        const firebase::database::DataSnapshot& snapshot) override {
      // Do something with the data in snapshot...
    }
    void OnCancelled(const firebase::database::Error& error_code,
                     const char* error_message) override {
      LogMessage("ERROR: LeadersValueListener canceled: %d: %s", error_code,
                 error_message);
    }
  };

  // Elsewhere in the code...

  LeadersValueListener* listener = new LeadersValueListener();
  firebase::Future&ltfirebase::database::DataSnapshot&gt result =
    dbRef.GetReference("Leaders").AddValueListener(listener);
```

The `Future&ltDataSnapshot&gt` result contains the data at the specified location
in the database at the time of the event. Calling `value()` on a snapshot
returns a `Variant` representing the data.

In this example, the `OnCancelled` method is also overridden to see if the read
is canceled. For example, a read can be canceled if the client doesn't have
permission to read from a Firebase database location. The `database::Error` will
indicate why the failure occurred.

### ChildListener class

Child events are triggered in response to specific operations that happen to the
children of a node from an operation such as a new child added through the
`PushChild()` method or a child being updated through the `UpdateChildren()`
method. Each of these together can be useful for listening to changes to a
specific node in a database. For example, a game might use these methods
together to monitor activity in the comments of a game session, as shown below:

```c++
  class SessionCommentsChildListener : public firebase::database::ChildListener {
   public:
    void OnChildAdded(const firebase::database::DataSnapshot& snapshot,
                      const char* previous_sibling) override {
      // Do something with the data in snapshot ...
    }
    void OnChildChanged(const firebase::database::DataSnapshot& snapshot,
                        const char* previous_sibling) override {
      // Do something with the data in snapshot ...
    }
    void OnChildRemoved(
        const firebase::database::DataSnapshot& snapshot) override {
      // Do something with the data in snapshot ...
    }
    void OnChildMoved(const firebase::database::DataSnapshot& snapshot,
                      const char* previous_sibling) override {
      // Do something with the data in snapshot ...
    }
    void OnCancelled(const firebase::database::Error& error_code,
                     const char* error_message) override {
      LogMessage("ERROR: SessionCommentsChildListener canceled: %d: %s",
                 error_code, error_message);
    }
  };

  // elsewhere ....

  SessionCommentsChildListener* listener = new SessionCommentsChildListener();
  firebase::Future&ltfirebase::database::DataSnapshot&gt result =
    dbRef.GetReference("GameSessionComments").AddChildListener(listener);
```

The `OnChildAdded` callback is typically used to retrieve a list of
items in a Firebase database. The `OnChildAdded` callback is called once
for each existing child and then again every time a new child is added to the
specified path. The listener is passed a snapshot containing the new child's
data.

The `OnChildChanged` callback is called any time a child node is modified.
This includes any modifications to descendants of the child node. It is
typically used in conjunction with the `OnChildAdded` and `OnChildRemoved`
calls to respond to changes to a list of items. The snapshot passed to the
listener contains the updated data for the child.

The `OnChildRemoved` callback is triggered when an immediate child is removed.
It is typically used in conjunction with the `OnChildAdded` and
`OnChildChanged` callbacks. The snapshot passed to the callback contains
the data for the removed child.

The `OnChildMoved` callback is triggered whenever the `OnChildChanged`
call is raised by an update that causes reordering of the child. It is
used with data that is ordered with `OrderByChild` or `OrderByValue`.

## Sorting and filtering data

You can use the Realtime Database `Query` class to retrieve data sorted by
key, by value, or by value of a child. You can also filter
the sorted result to a specific number of results or a range of keys or
values.

> [!NOTE]
> **Note:** Filtering and sorting can be expensive, especially when done on the client. If your app uses queries, define the `.indexOn` rule to index those keys on the server and improve query performance as described in [Indexing Your Data](https://firebase.google.com/docs/database/security/indexing-data).

### Sort data

To retrieve sorted data, start by specifying one of the order-by methods to
determine how results are ordered:

| Method | Usage |
|---|---|
| `OrderByChild()` | Order results by the value of a specified child key. |
| `OrderByKey()` | Order results by child keys. |
| `OrderByValue()` | Order results by child values. |

You can only use **one** order-by method at a time. Calling an order-by method
multiple times in the same query throws an error.

The following example demonstrates how you could subscribe to a score
leaderboard ordered by score.

```c++
  firebase::database::Query query =
    dbRef.GetReference("Leaders").OrderByChild("score");

  // To get the resulting DataSnapshot either use query.GetValue() and poll the
  // future, or use query.AddValueListener() and register to handle the
  // OnValueChanged callback.
```

This defines a `firebase::Query` that when combined with a
[ValueListener](https://firebase.google.com/docs/database/cpp/retrieve-data#value-callbacks) synchronizes the client with the leaderboard
in the database, ordered by the score of each entry.
You can read more about structuring your data efficiently in
[Structure Your Database](https://firebase.google.com/docs/database/android/structure-data#fanout).

The call to the `OrderByChild()` method specifies the child key to order the
results by. In this case, results are sorted by the value of the `"score"`
value in each child. For more information on how other data types are ordered,
see [How query data is ordered](https://firebase.google.com/docs/database/cpp/retrieve-data#data-order).

### Filtering data

To filter data, you can combine any of the limit or range methods with an
order-by method when constructing a query.

| Method | Usage |
|---|---|
| `LimitToFirst()` | Sets the maximum number of items to return from the beginning of the ordered list of results. |
| `LimitToLast()` | Sets the maximum number of items to return from the end of the ordered list of results. |
| `StartAt()` | Return items greater than or equal to the specified key or value depending on the order-by method chosen. |
| `EndAt()` | Return items less than or equal to the specified key or value depending on the order-by method chosen. |
| `EqualTo()` | Return items equal to the specified key or value depending on the order-by method chosen. |

Unlike the order-by methods, you can combine multiple limit or range functions.
For example, you can combine the `StartAt()` and `EndAt()` methods to limit
the results to a specified range of values.

Even when there is only a single match for the query, the snapshot is still
a list; it just contains a single item.

#### Limit the number of results

You can use the `LimitToFirst()` and `LimitToLast()` methods to set a
maximum number of children to be synced for a given callback. For example, if
you use `LimitToFirst()` to set a limit of 100, you initially only receive up
to 100 `OnChildAdded` callbacks. If you have fewer than 100 items stored in your
Firebase database, an `OnChildAdded` callback fires for each item.

As items change, you receive `OnChildAdded` callbacks for items that enter the
query and `OnChildRemoved` callbacks for items that drop out of it so that
the total number stays at 100.

For example, the code below returns the top score from a leaderboard:

```c++
  firebase::database::Query query =
    dbRef.GetReference("Leaders").OrderByChild("score").LimitToLast(1);

  // To get the resulting DataSnapshot either use query.GetValue() and poll the
  // future, or use query.AddValueListener() and register to handle the
  // OnValueChanged callback.
```

#### Filter by key or value

You can use `StartAt()`, `EndAt()`, and `EqualTo()` to choose arbitrary
starting, ending, and equivalence points for queries. This can be useful for
paginating data or finding items with children that have a specific value.

### How query data is ordered

This section explains how data is sorted by each of the order-by methods in the
`Query` class.

#### `OrderByChild`

When using `OrderByChild()`, data that contains the specified child key is
ordered as follows:

1. Children with a `null` value for the specified child key come first.
2. Children with a value of `false` for the specified child key come next. If multiple children have a value of `false`, they are sorted [lexicographically](http://en.wikipedia.org/wiki/Lexicographical_order) by key.
3. Children with a value of `true` for the specified child key come next. If multiple children have a value of `true`, they are sorted lexicographically by key.
4. Children with a numeric value come next, sorted in ascending order. If multiple children have the same numerical value for the specified child node, they are sorted by key.
5. Strings come after numbers and are sorted lexicographically in ascending order. If multiple children have the same value for the specified child node, they are ordered lexicographically by key.
6. Objects come last and are sorted lexicographically by key in ascending order.

#### `OrderByKey`

When using `OrderByKey()` to sort your data, data is returned in ascending order
by key.

1. Children with a key that can be parsed as a 32-bit integer come first, sorted in ascending order.
2. Children with a string value as their key come next, sorted lexicographically in ascending order.

#### `OrderByValue`

When using `OrderByValue()`, children are ordered by their value. The ordering
criteria are the same as in `OrderByChild()`, except the value of the node is
used instead of the value of a specified child key.

## Next Steps

- [Saving Data](https://firebase.google.com/docs/database/cpp/save-data)