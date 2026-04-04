# Source: https://firebase.google.com/docs/rules/rules-behavior.md.txt

<br />

Security can be one of the most complex pieces of the app development puzzle. In most applications, developers must build and run a server that handles authentication (who a user is) and authorization (what a user can do).

Firebase Security Rulesremove the middle (server) layer and allow you to specify path-based permissions for clients that connect to your data directly. Use this guide to learn more about how rules are applied to incoming requests.

Select a product to learn more about its rules.

<br />

### Cloud Firestore

<br />

## Basic structure

Firebase Security RulesinCloud FirestoreandCloud Storageuse the following structure and syntax:  

    service <<name>> {
      // Match the resource path.
      match <<path>> {
        // Allow the request if the following conditions are true.
        allow <<methods>> : if <<condition>>
      }
    }

The following key concepts are important to understand as you build the rules:

- **Request:** The method or methods invoked in the`allow`statement. These are methods you're allowing to run. The standard methods are:`get`,`list`,`create`,`update`, and`delete`. The`read`and`write`convenience methods enable broad read and write access on the specified database or storage path.
- **Path:**The database or storage location, represented as a URI path.
- **Rule:** The`allow`statement, which includes a condition that permits a request if it evaluates to true.

### Security rules version 2

As of May 2019, version 2 of theFirebasesecurity rules is now available. Version 2 of the rules changes the behavior of[recursive wildcards](https://firebase.google.com/docs/rules/rules-behavior#recursive_wildcards)`{name=**}`. You must use version 2 if you plan to use[collection group queries](https://firebase.google.com/docs/firestore/query-data/queries#collection-group-query). You must opt-in to version 2 by making`rules_version = '2';`the first line in your security rules:  

    rules_version = '2';
    service cloud.firestore {
      match /databases/{database}/documents {

| Avoid using recursive wildcards unless you intend for permissive security rules to propagate to all nested subcollections.

## Matching paths

All match statements should point to documents, not collections. A match statement can point to a specific document, as in`match /cities/SF`or use wildcards to point to any document in the specified path, as in`match /cities/{city}`.

In the example, the match statement uses the`{city}`wildcard syntax. This means the rule applies to any document in the`cities`collection, such as`/cities/SF`or`/cities/NYC`. When the`allow`expressions in the match statement are evaluated, the`city`variable will resolve to the city document name, such as`SF`or`NYC`.
| **Note:** You can only access documents that your security rules specifically allow you to access. For example, the rules shown allow access only to documents in the`cities`collection; as a result, they also deny access to documents in all other collections.

### Matching subcollections

Data inCloud Firestoreis organized into collections of documents, and each document may extend the hierarchy through subcollections. It is important to understand how security rules interact with hierarchical data.

Consider the situation where each document in the`cities`collection contains a`landmarks`subcollection. Security rules apply only at the matched path, so the access controls defined on the`cities`collection don't apply to the`landmarks`subcollection. Instead, write explicit rules to control access to subcollections:  

    service cloud.firestore {
      match /databases/{database}/documents {
        match /cities/{city} {
          allow read, write: if <condition>;

          // Explicitly define rules for the 'landmarks' subcollection
          match /landmarks/{landmark} {
            allow read, write: if <condition>;
          }
        }
      }
    }

When nesting`match`statements, the path of the inner`match`statement is always relative to the path of the outer`match`statement. The following rulesets are therefore equivalent:  

    service cloud.firestore {
      match /databases/{database}/documents {
        match /cities/{city} {
          match /landmarks/{landmark} {
            allow read, write: if <condition>;
          }
        }
      }
    }

    service cloud.firestore {
      match /databases/{database}/documents {
        match /cities/{city}/landmarks/{landmark} {
          allow read, write: if <condition>;
        }
      }
    }

#### Overlapping match statements

It's possible for a document to match more than one`match`statement. In the case where multiple`allow`expressions match a request, the access is allowed if**any** of the conditions is`true`:  

    service cloud.firestore {
      match /databases/{database}/documents {
        // Matches any document in the 'cities' collection.
        match /cities/{city} {
          allow read, write: if false;
        }

        // Matches any document in the 'cities' collection.
        match /cities/{document} {
          allow read, write: if true;
        }
      }
    }

In the example, all reads and writes to the`cities`collection will be allowed because the second rule is always`true`, even though the first rule is always`false`.

#### Recursive wildcards

If you want rules to apply to an arbitrarily deep hierarchy, use the recursive wildcard syntax,`{name=**}`:  

    service cloud.firestore {
      match /databases/{database}/documents {
        // Matches any document in the cities collection as well as any document
        // in a subcollection.
        match /cities/{document=**} {
          allow read, write: if <condition>;
        }
      }
    }

When using the recursive wildcard syntax, the wildcard variable will contain the entire matching path segment, even if the document is located in a deeply nested subcollection. For example, the rules listed would match a document located at`/cities/SF/landmarks/coit_tower`, and the value of the`document`variable would be`SF/landmarks/coit_tower`.

Note, however, that the behavior of recursive wildcards depends on the rules version.  

### Version 1

Security rules use version 1 by default. In version 1, recursive wildcards match one or more path items. They don't match an empty path, so`match /cities/{city}/{document=**}`matches documents in subcollections but not in the`cities`collection, whereas`match /cities/{document=**}`matches both documents in the`cities`collection and subcollections.

Recursive wildcards must come at the end of a match statement.

### Version 2

In version 2 of the security rules, recursive wildcards match zero or more path items.`match/cities/{city}/{document=**}`matches documents in any subcollections as well as documents in the`cities`collection.

You must opt-in to version 2 by adding`rules_version = '2';`at the top of your security rules:  

    rules_version = '2';
    service cloud.firestore {
      match /databases/{database}/documents {
        // Matches any document in the cities collection as well as any document
        // in a subcollection.
        match /cities/{city}/{document=**} {
          allow read, write: if <condition>;
        }
      }
    }

You can have at most one recursive wildcard per match statement, but in version 2, you can place this wildcard anywhere in the match statement. For example:  

    rules_version = '2';
    service cloud.firestore {
      match /databases/{database}/documents {
        // Matches any document in the songs collection group
        match /{path=**}/songs/{song} {
          allow read, write: if <condition>;
        }
      }
    }

If you use[collection group queries](https://firebase.google.com/docs/firestore/query-data/queries#collection-group-query), you must use version 2, see[securing collection group queries](https://firebase.google.com/docs/firestore/security/rules-query).

## Security rule limits

As you work with security rules, note the following limits:

|                                          Limit                                           |                                                                                                                                                                                                                                                                                                            Details                                                                                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Maximum number of`exists()`,`get()`, and`getAfter()`calls per request                    | - 10 for single-document requests and query requests. - 20 for multi-document reads, transactions, and batched writes. The previous limit of 10 also applies to each operation. For example, imagine you create a batched write request with 3 write operations and that your security rules use 2 document access calls to validate each write. In this case, each write uses 2 of its 10 access calls and the batched write request uses 6 of its 20 access calls. Exceeding either limit results in a permission denied error. Some document access calls may be cached, and cached calls do not count towards the limits. |
| Maximum nested`match`statement depth                                                     | 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Maximum path length, in path segments, allowed within a set of nested`match`statements   | 100                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Maximum number of path capture variables allowed within a set of nested`match`statements | 20                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Maximum function call depth                                                              | 20                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Maximum number of function arguments                                                     | 7                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Maximum number of`let`variable bindings per function                                     | 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Maximum number of recursive or cyclical function calls                                   | 0 (not permitted)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Maximum number of expressions evaluated per request                                      | 1,000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Maximum size of a ruleset                                                                | Rulesets must obey two size limits: - a 256 KB limit on the size of the ruleset text source published from theFirebaseconsole or from the CLI using`firebase deploy`. - a 250 KB limit on the size of the compiled ruleset that results when Firebase processes the source and makes it active on the back-end.                                                                                                                                                                                                                                                                                                               |

<br />

### Cloud Storage

<br />

## Basic structure

Firebase Security RulesinCloud FirestoreandCloud Storageuse the following structure and syntax:  

    service <<name>> {
      // Match the resource path.
      match <<path>> {
        // Allow the request if the following conditions are true.
        allow <<methods>> : if <<condition>>
      }
    }

The following key concepts are important to understand as you build the rules:

- **Request:** The method or methods invoked in the`allow`statement. These are methods you're allowing to run. The standard methods are:`get`,`list`,`create`,`update`, and`delete`. The`read`and`write`convenience methods enable broad read and write access on the specified database or storage path.
- **Path:**The database or storage location, represented as a URI path.
- **Rule:** The`allow`statement, which includes a condition that permits a request if it evaluates to true.

## Matching paths

Cloud StorageSecurity Rules`match`the file paths used to access files inCloud Storage. Rules can`match`exact paths or wildcard paths, and rules can also be nested. If no match rule allows an request method, or the condition evaluates to`false`, the request is denied.

### Exact matches

```scilab
// Exact match for "images/profilePhoto.png"
match /images/profilePhoto.png {
  allow write: if <condition>;
}

// Exact match for "images/croppedProfilePhoto.png"
match /images/croppedProfilePhoto.png {
  allow write: if <other_condition>;
}
```

### Nested matches

```scilab
// Partial match for files that start with "images"
match /images {
  // Exact match for "images/profilePhoto.png"
  match /profilePhoto.png {
    allow write: if <condition>;
  }

  // Exact match for "images/croppedProfilePhoto.png"
  match /croppedProfilePhoto.png {
    allow write: if <other_condition>;
  }
}
```

### Wildcard matches

Rules can also be used to`match`a pattern using wildcards. A wildcard is a named variable that represents either a single string such as`profilePhoto.png`, or multiple path segments, such as`images/profilePhoto.png`.

A wildcard is created by adding curly braces around the wildcard name, like`{string}`. A multiple segment wildcard can be declared by adding`=**`to the wildcard name, like`{path=**}`:
Avoid using recursive wildcards unless you intend for permissive security rules to propagate to all nested folders.  

```scilab
// Partial match for files that start with "images"
match /images {
  // Exact match for "images/*"
  // e.g. images/profilePhoto.png is matched
  match /{imageId} {
    // This rule only matches a single path segment (*)
    // imageId is a string that contains the specific segment matched
    allow read: if <condition>;
  }

  // Exact match for "images/**"
  // e.g. images/users/user:12345/profilePhoto.png is matched
  // images/profilePhoto.png is also matched!
  match /{allImages=**} {
    // This rule matches one or more path segments (**)
    // allImages is a path that contains all segments matched
    allow read: if <other_condition>;
  }
}
```

If multiple rules match a file, the result is the`OR`of the result of all rules evaluations. That is, if any rule the file matches evaluates to`true`, the result is`true`.

In the rules, the file "images/profilePhoto.png" can be read if either`condition`or`other_condition`evaluate to true, while the file "images/users/user:12345/profilePhoto.png" is only subject to the result of`other_condition`.

A wildcard variable can be referenced from within the`match`provide filename or path authorization:  

```scilab
// Another way to restrict the name of a file
match /images/{imageId} {
  allow read: if imageId == "profilePhoto.png";
}
```

Cloud StorageSecurity Rulesdon't cascade, and rules are only evaluated when the request path matches a path with rules specified.

## Request evaluation

Uploads, downloads, metadata changes, and deletes are evaluated using the`request`sent toCloud Storage. The`request`variable contains the path where the request is being performed, the time when the request is received, and the new`resource`value if the request is a write. HTTP headers and authentication state are also included.

The`request`object also contains the user's unique ID and theFirebase Authenticationpayload in the`request.auth`object, which will be explained further in the[Authentication](https://firebase.google.com/docs/storage/security/rules-conditions#authentication)section of the docs.

A full list of properties in the`request`object is available below:

|  Property  |         Type          |                                                                    Description                                                                     |
|------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `auth`     | map\<string, string\> | When a user is logged in, provides`uid`, the user's unique ID, and`token`, a map ofFirebase AuthenticationJWT claims. Otherwise, it will be`null`. |
| `params`   | map\<string, string\> | Map containing the query parameters of the request.                                                                                                |
| `path`     | path                  | A`path`representing the path the request is being performed at.                                                                                    |
| `resource` | map\<string, string\> | The new resource value, present only on`write`requests.                                                                                            |
| `time`     | timestamp             | A timestamp representing the server time the request is evaluated at.                                                                              |

| **Note:** Detailed documentation for these properties is available in the[Firebase Security RulesforCloud StorageAPI reference](https://firebase.google.com/docs/reference/security/storage#request).

## Resource evaluation

When evaluating rules, you may also want to evaluate the metadata of the file being uploaded, downloaded, modified, or deleted. This lets you create complex and powerful rules that do things like only allow files with certain content types to be uploaded, or only files greater than a certain size to be deleted.

Firebase Security RulesforCloud Storageprovides file metadata in the`resource`object, which contains key/value pairs of the metadata surfaced in aCloud Storageobject. These properties can be inspected on`read`or`write`requests to ensure data integrity.

On`write`requests (such as uploads, metadata updates, and deletes), in addition to the`resource`object, which contains file metadata for the file that exists at the request path, you also have the ability to use the`request.resource`object, which contains a subset of the file metadata to be written if the write is allowed. You can use these two values to ensure data integrity or enforce application constraints such as file type or size.

A full list of properties in the`resource`object is available:

|       Property       |         Type          |                                                       Description                                                       |
|----------------------|-----------------------|-------------------------------------------------------------------------------------------------------------------------|
| `name`               | string                | The full name of the object                                                                                             |
| `bucket`             | string                | The name of the bucket this object resides in.                                                                          |
| `generation`         | int                   | The[Google Cloud Storageobject generation](https://cloud.google.com/storage/docs/object-versioning)of this object.      |
| `metageneration`     | int                   | The[Google Cloud Storageobject meta generation](https://cloud.google.com/storage/docs/object-versioning)of this object. |
| `size`               | int                   | The size of the object in bytes.                                                                                        |
| `timeCreated`        | timestamp             | A timestamp representing the time an object was created.                                                                |
| `updated`            | timestamp             | A timestamp representing the time an object was last updated.                                                           |
| `md5Hash`            | string                | An MD5 hash of the object.                                                                                              |
| `crc32c`             | string                | A crc32c hash of the object.                                                                                            |
| `etag`               | string                | The etag associated with this object.                                                                                   |
| `contentDisposition` | string                | The content disposition associated with this object.                                                                    |
| `contentEncoding`    | string                | The content encoding associated with this object.                                                                       |
| `contentLanguage`    | string                | The content language associated with this object.                                                                       |
| `contentType`        | string                | The content type associated with this object.                                                                           |
| `metadata`           | map\<string, string\> | Key/value pairs of additional, developer specified custom metadata.                                                     |

`request.resource`contains all of these with the exception of`generation`,`metageneration`,`etag`,`timeCreated`, and`updated`.
| **Note:** Detailed documentation for these properties is available in the[Firebase Security RulesforCloud StorageAPI reference](https://firebase.google.com/docs/reference/security/storage#resource).

## Security Rules limits

As you work with security rules, note the following limits:

|                                   Limit                                    |                                                                                                     Details                                                                                                      |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Maximum number of`firestore.exists()`and`firestore.get()`calls per request | 2 for single-document requests and query requests. Exceeding this limit results in a permission denied error. Access calls to the same documents may be cached, and cached calls don't count towards the limits. |

## Full Example

Putting it all together, you can create a full example of rules for an image storage solution:  

```gdscript
service firebase.storage {
 match /b/{bucket}/o {
   match /images {
     // Allow write files to the path "images/*", subject to the constraints:
     // 1) File is less than 5MB
     // 2) Content type is an image
     // 3) Uploaded content type matches existing content type
     // 4) Filename (stored in imageId wildcard variable) is less than 32 characters
     match /{imageId} {
       allow read;
       allow write: if request.resource.size < 5 * 1024 * 1024
                    && request.resource.contentType.matches('image/.*')
                    && request.resource.contentType == resource.contentType
                    && imageId.size() < 32
     }
   }
 }
}
```

<br />

### Realtime Database

<br />

## Basic structure

InRealtime Database,Firebase Security Rulesconsist of JavaScript-like expressions contained in a JSON document.

They use the following syntax:  

    {
      "rules": {
        "<<path>>": {
        // Allow the request if the condition for each method is true.
          ".read": <<condition>>,
          ".write": <<condition>>,
          ".validate": <<condition>>
        }
      }
    }

There are three basic elements in the rule:

- **Path:**The database location. This mirrors your database's JSON structure.
- **Request:** These are the methods the rule uses to grant access. The`read`and`write`rules grant broad read and write access, while`validate`rules act as a secondary verification to grant access based on incoming or existing data.
- **Condition:**The condition that permits a request if it evaluates to true.

## How rules apply to paths

InRealtime Database,Rulesapply atomically, meaning that rules at higher-level parent nodes override rules at more granular child nodes and rules at a deeper node can't grant access to a parent path. You can't refine or revoke access at a deeper path in your database structure if you've already granted it for one of the parent paths.

Consider the following rules:  

```scdoc
{
  "rules": {
     "foo": {
        // allows read to /foo/*
        ".read": "data.child('baz').val() === true",
        "bar": {
          // ignored, since read was allowed already
          ".read": false
        }
     }
  }
}
```

This security structure allows`/bar/`to be read from whenever`/foo/`contains a child`baz`with value`true`. The`".read": false`rule under`/foo/bar/`has no effect here, since access cannot be revoked by a child path.

While it may not seem immediately intuitive, this is a powerful part of the rules language and allows for very complex access privileges to be implemented with minimal effort. This is particularly useful for[user-based security](https://firebase.google.com/docs/rules/rules-and-auth).

However,[`.validate`rules](https://firebase.google.com/docs/rules/data-validation)do not cascade. All validate rules must be satisfied at all levels of the hierarchy for a write to be allowed.

Additionally, because rules do not apply back to a parent path, read or write operation fail if there isn't a rule at the requested location or at a parent location that grants access. Even if every affected child path is accessible, reading at the parent location will fail completely. Consider this structure:  

```text
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

Without understanding that rules are evaluated atomically, it might seem like fetching the`/records/`path would return`rec1`but not`rec2`. The actual result, however, is an error:  

##### JavaScript

```gdscript
var db = firebase.database();
db.ref("records").once("value", function(snap) {
  // success method is not called
}, function(err) {
  // error callback triggered with PERMISSION_DENIED
});
```

##### Objective-C

**Note:**This Firebase product is not available on the App Clip target.  

```objective-c
FIRDatabaseReference *ref = [[FIRDatabase database] reference];
[[_ref child:@"records"] observeSingleEventOfType:FIRDataEventTypeValue withBlock:^(FIRDataSnapshot *snapshot) {
  // success block is not called
} withCancelBlock:^(NSError * _Nonnull error) {
  // cancel block triggered with PERMISSION_DENIED
}];
```

##### Swift

**Note:**This Firebase product is not available on the App Clip target.  

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

Since the read operation at`/records/`is atomic, and there's no read rule that grants access to all of the data under`/records/`, this will throw a`PERMISSION_DENIED`error. If we evaluate this rule in the security simulator in our[Firebaseconsole](https://console.firebase.google.com/), we can see that the read operation was denied:  

```
Attempt to read /records with auth=Success(null)
    /
    /records

No .read rule allowed the operation.
Read was denied.
```

The operation was denied because no read rule allowed access to the`/records/`path, but note that the rule for`rec1`was never evaluated because it wasn't in the path we requested. To fetch`rec1`, we would need to access it directly:  

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

**Note:**This Firebase product is not available on the App Clip target.  

```objective-c
FIRDatabaseReference *ref = [[FIRDatabase database] reference];
[[ref child:@"records/rec1"] observeSingleEventOfType:FEventTypeValue withBlock:^(FIRDataSnapshot *snapshot) {
    // SUCCESS!
}];
```

##### Swift

**Note:**This Firebase product is not available on the App Clip target.  

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

## Location variable

Realtime DatabaseRulessupport a`$location`variable to match path segments. Use the`$`prefix in front of your path segment to match your rule to any child nodes along the path.  

      {
        "rules": {
          "rooms": {
            // This rule applies to any child of /rooms/, the key for each room id
            // is stored inside $room_id variable for reference
            "$room_id": {
              "topic": {
                // The room's topic can be changed if the room id has "public" in it
                ".write": "$room_id.contains('public')"
              }
            }
          }
        }
      }

You can also use the`$variable`in parallel with constant path names.  

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

<br />

<br />