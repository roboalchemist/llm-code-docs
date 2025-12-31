# Source: https://firebase.google.com/docs/database/rest/retrieve-data.md.txt

# Source: https://firebase.google.com/docs/database/cpp/retrieve-data.md.txt

# Source: https://firebase.google.com/docs/database/admin/retrieve-data.md.txt

# Source: https://firebase.google.com/docs/database/unity/retrieve-data.md.txt

<br />

This document covers the basics of retrieving data and how to order and filter Firebase data.

## Before you begin

Before you can use[Realtime Database](https://firebase.google.com/docs/reference/unity/namespace/firebase/database), you need to:

- Register your Unity project and configure it to use Firebase.

  - If your Unity project already uses Firebase, then it's already registered and configured for Firebase.

  - If you don't have a Unity project, you can download a[sample app](https://github.com/google/mechahamster).

- Add the[FirebaseUnitySDK](https://firebase.google.com/download/unity)(specifically,`FirebaseDatabase.unitypackage`) to your Unity project.

| **Find detailed instructions for these initial setup tasks in[Add Firebase to your Unity project](https://firebase.google.com/docs/unity/setup#prerequisites).**

Note that adding Firebase to your Unity project involves tasks both in the[Firebaseconsole](https://console.firebase.google.com/)and in your open Unity project (for example, you download Firebase config files from the console, then move them into your Unity project).

## Retrieving Data

Firebase data is retrieved by either a one time call to GetValueAsync() or attaching to an event on a`FirebaseDatabase`reference. The event listener is called once for the initial state of the data and again anytime the data changes.
| **Note:** By default, read and write access to your database is restricted so only authenticated users can read or write data. To get started without setting up[Authentication](https://firebase.google.com/docs/auth), you can[configure your rules for public access](https://firebase.google.com/docs/rules/basics#default_rules_locked_mode). This does make your database open to anyone, even people not using your app, so be sure to restrict your database again when you set up authentication.

## Get a DatabaseReference

To read data from the database, you need an instance of[`DatabaseReference`](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference):  

```c#
using Firebase;
using Firebase.Database;
using Firebase.Extensions.TaskExtension; // for ContinueWithOnMainThread

public class MyScript: MonoBehaviour {
  void Start() {
    // Get the root reference location of the database.
    DatabaseReference reference = FirebaseDatabase.DefaultInstance.RootReference;
  }
}
```

## Read data once

You can use the[`GetValueAsync`](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#getvalueasync)method to read a static snapshot of the contents at a given path once. The task result will contain a[snapshot](https://firebase.google.com/docs/reference/unity/class/firebase/database/data-snapshot)containing all data at that location, including child data. If there is no data, the snapshot returned is`null`.  

```c#
    FirebaseDatabase.DefaultInstance
      .GetReference("Leaders")
      .GetValueAsync().ContinueWithOnMainThread(task =&gt {
        if (task.IsFaulted) {
          // Handle the error...
        }
        else if (task.IsCompleted) {
          DataSnapshot snapshot = task.Result;
          // Do something with snapshot...
        }
      });
```

## Listen for events

You can add event listeners to subscribe on changes to data:

|     Event      |                                                                                            Typical usage                                                                                            |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ValueChanged` | Read and listen for changes to the entire contents of a path.                                                                                                                                       |
| `ChildAdded`   | Retrieve lists of items or listen for additions to a list of items. Suggested use with`ChildChanged`and`ChildRemoved`to monitor changes to lists.                                                   |
| `ChildChanged` | Listen for changes to the items in a list. Use with`ChildAdded`and`ChildRemoved`to monitor changes to lists.                                                                                        |
| `ChildRemoved` | Listen for items being removed from a list. Use with`ChildAdded`and`ChildChanged`to monitor changes to lists.                                                                                       |
| `ChildMoved`   | Listen for changes to the order of items in an ordered list.`ChildMoved`events always follow the`ChildChanged`event that caused the item's order to change (based on your current order-by method). |

### ValueChanged event

You can use the[`ValueChanged`](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#valuechanged)event to subscribe on changes of the contents at a given path. This event is triggered once when the listener is attached and again every time the data, including children, changes. The event callback is passed a snapshot containing all data at that location, including child data. If there is no data, the snapshot returned is`null`.
| **Important:** The`ValueChanged`event is raised every time data is changed at the specified database reference, including changes to children. To limit the size of your snapshots, attach only at the highest level needed for watching changes. For example, attaching an event listener to the root of your database is not recommended.

The following example demonstrates a game retrieving the scores of a leaderboard from the database:  

```c#
      FirebaseDatabase.DefaultInstance
        .GetReference("Leaders")
        .ValueChanged += HandleValueChanged;
    }

    void HandleValueChanged(object sender, ValueChangedEventArgs args) {
      if (args.DatabaseError != null) {
        Debug.LogError(args.DatabaseError.Message);
        return;
      }
      // Do something with the data in args.Snapshot
    }
```

[`ValueChangedEventArgs`](https://firebase.google.com/docs/reference/unity/class/firebase/database/value-changed-event-args)contains a`DataSnapshot`that contains the data at the specified location in the database at the time of the event. Calling`Value`on a snapshot returns a`Dictionary<string, object>`representing the data. If no data exists at the location, calling`Value`returns`null`.

In this example,`args.DatabaseError`is also examined to see if the read is canceled. For example, a read can be canceled if the client doesn't have permission to read from a Firebase database location. The`DatabaseError`will indicate why the failure occurred.

You can later unsubscribe from the event using any`DatabaseReference`that has the same path.`DatabaseReference`instances are ephemeral and can be thought of as a way to access any path and query.  

```c#
      FirebaseDatabase.DefaultInstance
        .GetReference("Leaders")
        .ValueChanged -= HandleValueChanged; // unsubscribe from ValueChanged.
    }
```

### Child events

Child events are triggered in response to specific operations that happen to the children of a node from an operation such as a new child added through the[`Push()`](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#push)method or a child being updated through the[`UpdateChildrenAsync()`](https://firebase.google.com/docs/reference/unity/class/firebase/database/database-reference#updatechildrenasync)method. Each of these together can be useful for listening to changes to a specific node in a database. For example, a game might use these methods together to monitor activity in the comments of a game session, as shown below:  

```c#
      var ref = FirebaseDatabase.DefaultInstance
      .GetReference("GameSessionComments");

      ref.ChildAdded += HandleChildAdded;
      ref.ChildChanged += HandleChildChanged;
      ref.ChildRemoved += HandleChildRemoved;
      ref.ChildMoved += HandleChildMoved;
    }

    void HandleChildAdded(object sender, ChildChangedEventArgs args) {
      if (args.DatabaseError != null) {
        Debug.LogError(args.DatabaseError.Message);
        return;
      }
      // Do something with the data in args.Snapshot
    }

    void HandleChildChanged(object sender, ChildChangedEventArgs args) {
      if (args.DatabaseError != null) {
        Debug.LogError(args.DatabaseError.Message);
        return;
      }
      // Do something with the data in args.Snapshot
    }

    void HandleChildRemoved(object sender, ChildChangedEventArgs args) {
      if (args.DatabaseError != null) {
        Debug.LogError(args.DatabaseError.Message);
        return;
      }
      // Do something with the data in args.Snapshot
    }

    void HandleChildMoved(object sender, ChildChangedEventArgs args) {
      if (args.DatabaseError != null) {
        Debug.LogError(args.DatabaseError.Message);
        return;
      }
      // Do something with the data in args.Snapshot
    }
```

The[`ChildAdded`](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#childadded)event is typically used to retrieve a list of items in a Firebase database. The`ChildAdded`event is raised once for each existing child and then again every time a new child is added to the specified path. The listener is passed a snapshot containing the new child's data.

The[`ChildChanged`](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#childchanged)event is raised any time a child node is modified. This includes any modifications to descendants of the child node. It is typically used in conjunction with the`ChildAdded`and`ChildRemoved`events to respond to changes to a list of items. The snapshot passed to the event listener contains the updated data for the child.

The[`ChildRemoved`](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#childremoved)event is triggered when an immediate child is removed. It is typically used in conjunction with the`ChildAdded`and`ChildChanged`callbacks. The snapshot passed to the event callback contains the data for the removed child.

The[`ChildMoved`](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#childmoved)event is triggered whenever the`ChildChanged`event is raised by an update that causes reordering of the child. It is used with data that is ordered with`OrderByChild`or`OrderByValue`.

## Sorting and filtering data

You can use theRealtime Database[`Query`](https://firebase.google.com/docs/reference/unity/class/firebase/database/query)class to retrieve data sorted by key, by value, or by value of a child. You can also filter the sorted result to a specific number of results or a range of keys or values.
| **Note:** Filtering and sorting can be expensive, especially when done on the client. If your app uses queries, define the`.indexOn`rule to index those keys on the server and improve query performance as described in[Indexing Your Data](https://firebase.google.com/docs/database/security/indexing-data).

### Sort data

To retrieve sorted data, start by specifying one of the order-by methods to determine how results are ordered:

|      Method      |                        Usage                         |
|------------------|------------------------------------------------------|
| `OrderByChild()` | Order results by the value of a specified child key. |
| `OrderByKey()`   | Order results by child keys.                         |
| `OrderByValue()` | Order results by child values.                       |

You can only use**one**order-by method at a time. Calling an order-by method multiple times in the same query throws an error.

The following example demonstrates how you could subscribe on a score leaderboard ordered by score.  

```c#
      FirebaseDatabase.DefaultInstance
        .GetReference("Leaders").OrderByChild("score")
        .ValueChanged += HandleValueChanged;
    }

    void HandleValueChanged(object sender, ValueChangedEventArgs args) {
      if (args.DatabaseError != null) {
        Debug.LogError(args.DatabaseError.Message);
        return;
      }
      // Do something with the data in args.Snapshot
    }
```

This defines a query that when combined with a[valuechanged event listener](https://firebase.google.com/docs/database/unity/retrieve-data#value-events)synchronizes the client with the leaderboard in the database, ordered by the score of each entry. You can read more about structuring your data efficiently in[Structure Your Database](https://firebase.google.com/docs/database/unity/structure-data#fanout).

The call to the`OrderByChild()`method specifies the child key to order the results by. In this case, results are sorted by the value of the`"score"`value in each child. For more information on how other data types are ordered, see[How query data is ordered](https://firebase.google.com/docs/database/unity/retrieve-data#data-order).

### Filtering data

To filter data, you can combine any of the limit or range methods with an order-by method when constructing a query.

|      Method      |                                                   Usage                                                   |
|------------------|-----------------------------------------------------------------------------------------------------------|
| `LimitToFirst()` | Sets the maximum number of items to return from the beginning of the ordered list of results.             |
| `LimitToLast()`  | Sets the maximum number of items to return from the end of the ordered list of results.                   |
| `StartAt()`      | Return items greater than or equal to the specified key or value depending on the order-by method chosen. |
| `EndAt()`        | Return items less than or equal to the specified key or value depending on the order-by method chosen.    |
| `EqualTo()`      | Return items equal to the specified key or value depending on the order-by method chosen.                 |

Unlike the order-by methods, you can combine multiple limit or range functions. For example, you can combine the`StartAt()`and`EndAt()`methods to limit the results to a specified range of values.

Even when there is only a single match for the query, the snapshot is still a list; it just contains a single item.

#### Limit the number of results

You can use the[`LimitToFirst()`](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#limittofirst)and[`LimitToLast()`](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#limittolast)methods to set a maximum number of children to be synced for a given callback. For example, if you use`LimitToFirst()`to set a limit of 100, you initially only receive up to 100`ChildAdded`callbacks. If you have fewer than 100 items stored in your Firebase database, an`ChildAdded`callback fires for each item.

As items change, you receive`ChildAdded`callbacks for items that enter the query and`ChildRemoved`callbacks for items that drop out of it so that the total number stays at 100.

For example, the code below returns the top score from a leaderboard:  

```c#
      FirebaseDatabase.DefaultInstance
        .GetReference("Leaders").OrderByChild("score").LimitToLast(1)
        .ValueChanged += HandleValueChanged;
    }

    void HandleValueChanged(object sender, ValueChangedEventArgs args) {
      if (args.DatabaseError != null) {
        Debug.LogError(args.DatabaseError.Message);
        return;
      }
      // Do something with the data in args.Snapshot
    }
```

#### Filter by key or value

You can use[`StartAt()`](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#startat),[`EndAt()`](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#endat), and[`EqualTo()`](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#equalto)to choose arbitrary starting, ending, and equivalence points for queries. This can be useful for paginating data or finding items with children that have a specific value.

### How query data is ordered

This section explains how data is sorted by each of the order-by methods in the`Query`class.

#### `OrderByChild`

When using[`OrderByChild()`](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#orderbychild), data that contains the specified child key is ordered as follows:

1. Children with a`null`value for the specified child key come first.
2. Children with a value of`false`for the specified child key come next. If multiple children have a value of`false`, they are sorted[lexicographically](http://en.wikipedia.org/wiki/Lexicographical_order)by key.
3. Children with a value of`true`for the specified child key come next. If multiple children have a value of`true`, they are sorted lexicographically by key.
4. Children with a numeric value come next, sorted in ascending order. If multiple children have the same numerical value for the specified child node, they are sorted by key.
5. Strings come after numbers and are sorted lexicographically in ascending order. If multiple children have the same value for the specified child node, they are ordered lexicographically by key.
6. Objects come last and are sorted lexicographically by key in ascending order.

#### `OrderByKey`

When using[`OrderByKey()`](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#orderbykey)to sort your data, data is returned in ascending order by key.

1. Children with a key that can be parsed as a 32-bit integer come first, sorted in ascending order.
2. Children with a string value as their key come next, sorted lexicographically in ascending order.

#### `OrderByValue`

When using[`OrderByValue()`](https://firebase.google.com/docs/reference/unity/class/firebase/database/query#orderbyvalue), children are ordered by their value. The ordering criteria are the same as in`OrderByChild()`, except the value of the node is used instead of the value of a specified child key.