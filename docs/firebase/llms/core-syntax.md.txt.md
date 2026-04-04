# Source: https://firebase.google.com/docs/database/security/core-syntax.md.txt

Firebase Realtime Database Security Rules allow you to control access to data stored
in your database. The flexible rules syntax allows you to create
rules that match anything, from all writes to your database to operations
on individual nodes.

Realtime Database Security Rules are *declarative* configuration for your database. This means
that the rules are defined separately from the product logic. This
has a number of advantages: clients aren't responsible for enforcing security, buggy
implementations will not compromise your data, and perhaps most importantly,
there is no need for an intermediate referee, such as a server, to protect data
from the world.

This topic describes the basic syntax and structure Realtime Database Security Rules
used to create complete rulesets.

## Structuring Your Security Rules

Realtime Database Security Rules are made up of JavaScript-like expressions contained in a
JSON document. The structure of your rules should follow the structure of the
data you have stored in your database.

Basic rules *identify a set of nodes* to be secured, the *access methods* (e.g., read,
write) involved, and *conditions* under which access is either allowed or denied.
In the following examples, our *conditions* will be simple `true` and
`false` statements, but in the next topic we'll cover more dynamic ways to
express conditions.

So, for example, if we are trying to secure a `child_node` under a `parent_node`,
the general syntax to follow is:

```
{
  "rules": {
    "parent_node": {
      "child_node": {
        ".read": <condition>,
        ".write": <condition>,
        ".validate": <condition>,
      }
    }
  }
}
```

Let's apply this pattern. For example, let's say you are keeping track of a list
of messages and have data that looks like this:

```
{
  "messages": {
    "message0": {
      "content": "Hello",
      "timestamp": 1405704370369
    },
    "message1": {
      "content": "Goodbye",
      "timestamp": 1405704395231
    },
    ...
  }
}
```

Your rules should be structured in a similar manner. Here's a set of
rules for read-only security that might make sense for this data structure. This
example illustrates how we specify database nodes to which rules apply and the
conditions for evaluating rules at those nodes.

```
{
  "rules": {
    // For requests to access the 'messages' node...
    "messages": {
      // ...and the individual wildcarded 'message' nodes beneath
      // (we'll cover wildcarding variables more a bit later)....
      "$message": {

        // For each message, allow a read operation if <condition>. In this
        // case, we specify our condition as "true", so read access is always granted.
        ".read": "true",

        // For read-only behavior, we specify that for write operations, our
        // condition is false.
        ".write": "false"
      }
    }
  }
}
```

## Basic Rules Operations

There are three types of rules for enforcing security based on the type of
operation being performed on the data: `.write`, `.read`, and `.validate`. Here
is a quick summary of their purposes:

| Rule Types ||
|---|---|
| **.read** | Describes if and when data is allowed to be read by users. |
| **.write** | Describes if and when data is allowed to be written. |
| **.validate** | Defines what a correctly formatted value will look like, whether it has child attributes, and the data type. |

> [!NOTE]
> **Note:** Access is disallowed by default. If no `.write` or `.read` rule is specified at or above a path, access will be denied.

### Wildcard Capture Variables

All rules statements point to nodes. A statement can point to a specific
node or use `$` wildcard *capture variables* to point to sets of nodes at a
level of the hierarchy. Use these capture variables to store the value of node
keys for use inside subsequent rules statements. This technique lets you write
more complex Security Rules *conditions*, something we'll cover in more detail
in the next topic.

```
{
  "rules": {
    "rooms": {
      // this rule applies to any child of /rooms/, the key for each room id
      // is stored inside $room_id variable for reference
      "$room_id": {
        "topic": {
          // the room's topic can be changed if the room id has "public" in it
          ".write": "$room_id.contains('public')"
        }
      }
    }
  }
}
```

The dynamic `$` variables can also be used in parallel with constant path
names. In this example, we're using the `$other` variable to declare
a `.validate` rule that ensures that
`widget` has no children other than `title` and `color`.
Any write that would result in additional children being created would fail.

```
{
  "rules": {
    "widget": {
      // a widget can have a title or color attribute
      "title": { ".validate": true },
      "color": { ".validate": true },

      // but no other child paths are allowed
      // in this case, $other means any key excluding "title" and "color"
      "$other": { ".validate": false }
    }
  }
}
```

> [!NOTE]
> **Note:** Path keys are always strings. For this reason, it's important to keep in mind that when we attempt to compare a `$` variable to a number, this will always fail. This can be corrected by converting the number to a string (e.g. `$key === newData.val()+''`)

## Read and Write Rules Cascade

> [!NOTE]
> **Note:** Shallower security rules override rules at deeper paths. Child rules can only grant additional privileges to what parent nodes have already declared. They cannot revoke a read or write privilege.

`.read` and `.write` rules work from top-down, with shallower
rules overriding deeper rules. If a rule grants read or write permissions at a particular
path, then it also grants access to
*all child nodes under it.* Consider the following structure:

```
{
  "rules": {
     "foo": {
        // allows read to /foo/*
        ".read": "data.child('baz').val() === true",
        "bar": {
          /* ignored, since read was allowed already */
          ".read": false
        }
     }
  }
}
```

This security structure allows `/bar/` to be read from whenever
`/foo/` contains a child `baz` with value `true`.
The `".read": false` rule under `/foo/bar/` has no
effect here, since access cannot be revoked by a child path.

While it may not seem immediately intuitive, this is a powerful part of the rules language
and allows for very complex access privileges to be implemented with minimal effort. This
will be illustrated when we get into user-based security later in this guide.

Note that `.validate` rules do not cascade. All validate rules
must be satisfied at all levels of the hierarchy in order for a write to be allowed.

## Rules Are Not Filters

Rules are applied in an atomic manner. That means that a read or write
operation is failed immediately if there isn't a rule at that location or at a
parent location that grants access. Even if every affected child path is accessible,
reading at the parent location will fail completely. Consider this structure:

```
{
  "rules": {
    "records": {
      "rec1": {
        ".read": true
      },
      "rec2": {
        ".read": false
      }
    }
  }
}
```

Without understanding that rules are evaluated atomically, it might seem
like fetching the `/records/` path would return `rec1`
but not `rec2`. The actual result, however, is an error:

##### JavaScript

```javascript
var db = firebase.database();
db.ref("records").once("value", function(snap) {
  // success method is not called
}, function(err) {
  // error callback triggered with PERMISSION_DENIED
});
```

##### Objective-C

**Note:** This Firebase product is not available on the App Clip target.

```objective-c
FIRDatabaseReference *ref = [[FIRDatabase database] reference];
[[_ref child:@"records"] observeSingleEventOfType:FIRDataEventTypeValue withBlock:^(FIRDataSnapshot *snapshot) {
  // success block is not called
} withCancelBlock:^(NSError * _Nonnull error) {
  // cancel block triggered with PERMISSION_DENIED
}];
```

##### Swift

**Note:** This Firebase product is not available on the App Clip target.

```swift
var ref = FIRDatabase.database().reference()
ref.child("records").observeSingleEventOfType(.Value, withBlock: { snapshot in
    // success block is not called
}, withCancelBlock: { error in
    // cancel block triggered with PERMISSION_DENIED
})
```

##### Java

```java
FirebaseDatabase database = FirebaseDatabase.getInstance();
DatabaseReference ref = database.getReference("records");
ref.addListenerForSingleValueEvent(new ValueEventListener() {
  @Override
  public void onDataChange(DataSnapshot snapshot) {
    // success method is not called
  }

  @Override
  public void onCancelled(FirebaseError firebaseError) {
    // error callback triggered with PERMISSION_DENIED
  });
});
```

##### REST

```
curl https://docs-examples.firebaseio.com/rest/records/
# response returns a PERMISSION_DENIED error
```

Since the read operation at `/records/` is atomic, and there's no
read rule that grants access to all of the data under `/records/`,
this will throw a `PERMISSION_DENIED` error. If we evaluate this
rule in the security simulator in our [Firebase console](https://console.firebase.google.com/), we can see that
the read operation was denied because no read rule allowed access to the
`/records/` path. However, note that the rule for `rec1`
was never evaluated because it wasn't in the path we requested. To fetch
`rec1`, we would need to access it directly:

##### JavaScript

```javascript
var db = firebase.database();
db.ref("records/rec1").once("value", function(snap) {
  // SUCCESS!
}, function(err) {
  // error callback is not called
});
```

##### Objective-C

**Note:** This Firebase product is not available on the App Clip target.

```objective-c
FIRDatabaseReference *ref = [[FIRDatabase database] reference];
[[ref child:@"records/rec1"] observeSingleEventOfType:FEventTypeValue withBlock:^(FIRDataSnapshot *snapshot) {
    // SUCCESS!
}];
```

##### Swift

**Note:** This Firebase product is not available on the App Clip target.

```swift
var ref = FIRDatabase.database().reference()
ref.child("records/rec1").observeSingleEventOfType(.Value, withBlock: { snapshot in
    // SUCCESS!
})
```

##### Java

```java
FirebaseDatabase database = FirebaseDatabase.getInstance();
DatabaseReference ref = database.getReference("records/rec1");
ref.addListenerForSingleValueEvent(new ValueEventListener() {
  @Override
  public void onDataChange(DataSnapshot snapshot) {
    // SUCCESS!
  }

  @Override
  public void onCancelled(FirebaseError firebaseError) {
    // error callback is not called
  }
});
```

##### REST

```
curl https://docs-examples.firebaseio.com/rest/records/rec1
# SUCCESS!
```

## Overlapping Statements

It's possible for a more than one rule to apply to a node. In the
case where multiple rules expressions identify a node, the access method is
denied if **any** of the conditions is `false`:

```
{
  "rules": {
    "messages": {
      // A rule expression that applies to all nodes in the 'messages' node
      "$message": {
        ".read": "true",
        ".write": "true"
      },
      // A second rule expression applying specifically to the 'message1` node
      "message1": {
        ".read": "false",
        ".write": "false"
      }
    }
  }
}
```

In the example above, reads to the `message1` node will be
denied because the second rules is always `false`, even though the first
rule is always `true`.

## Next steps

You can deepen your understanding of Firebase Realtime Database Security Rules:

- Learn the next major concept of the Security Rules language, dynamic
  [conditions](https://firebase.google.com/docs/database/security/rules-conditions), which let your Security Rules check user
  authorization, compare existing and incoming data, validate incoming data, check
  the structure of queries coming from the client, and more.

- Review typical security use cases and the [Firebase Security Rules definitions that address them](https://firebase.google.com/docs/rules/basics).