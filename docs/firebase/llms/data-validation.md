# Source: https://firebase.google.com/docs/rules/data-validation.md.txt

<br />

You can useFirebase Security Rulesto conditionally write new data based on existing data in your database or storage bucket. You can also write rules that enforce data validations by restricting writes based on the new data being written. Read on to learn more about rules that use existing data to create security conditions.

Select a product in each section to learn more about data validation rules.

## Restrictions on new data

<br />

### Cloud Firestore

<br />

If you want to make sure that a document that contains a specific field isn't created, you can include the field in the`allow`condition. For example, if you want to deny creation of any documents that contain the`ranking`field, you would disallow it in the`create`condition.  

      service cloud.firestore {
        match /databases/{database}/documents {
          // Disallow
          match /cities/{city} {
            allow create: if !("ranking" in request.resource.data)
          }
        }
      }

<br />

### Realtime Database

<br />

If you want to make sure that data that contains certain values isn't added to your database, you'd include that value in your rules and disallow it for writes. For example, if you want to deny any writes that contain`ranking`values, you would disallow writes for any documents with`ranking`values.  

      {
        "rules": {
          // Write is allowed for all paths
          ".write": true,
          // Allows writes only if new data doesn't include a `ranking` child value
          ".validate": "!newData.hasChild('ranking')
        }
      }

<br />

### Cloud Storage

<br />

If you want to make sure that a file that contains specific metadata isn't created, you can include the metadata in the`allow`condition. For example, if you want to deny creation of any files that contain`ranking`metadata, you would disallow it in the`create`condition.  

      service firebase.storage {
        match /b/{bucket}/o {
          match /files/{fileName} {
          // Disallow
            allow create: if !("ranking" in request.resource.metadata)
          }
        }
      }

<br />

<br />

## Use existing data inFirebase Security Rules

<br />

### Cloud Firestore

<br />

Many apps store access control information as fields on documents in the database.Cloud FirestoreSecurity Rulescan dynamically allow or deny access based on document data:  

      service cloud.firestore {
        match /databases/{database}/documents {
          // Allow the user to read data if the document has the 'visibility'
          // field set to 'public'
          match /cities/{city} {
            allow read: if resource.data.visibility == 'public';
          }
        }
      }

The`resource`variable refers to the requested document, and`resource.data`is a map of all of the fields and values stored in the document. For more information on the`resource`variable, see[the reference documentation](https://firebase.google.com/docs/reference/rules/rules.firestore.Resource).

When writing data, you may want to compare incoming data to existing data. This lets you do things like ensure a field hasn't changed, that a field has only incremented by one, or that the new value is at least a week in the future. In this case, if your ruleset allows the pending write, the`request.resource`variable contains the future state of the document. For`update`operations that only modify a subset of the document fields, the`request.resource`variable will contain the pending document state after the operation. You can check the field values in`request.resource`to prevent unwanted or inconsistent data updates:  

       service cloud.firestore {
         match /databases/{database}/documents {
          // Make sure all cities have a positive population and
          // the name is not changed
          match /cities/{city} {
            allow update: if request.resource.data.population > 0
                          && request.resource.data.name == resource.data.name;
          }
        }
      }

<br />

### Realtime Database

<br />

InRealtime Database, use`.validate`rules to enforce data structures and validate the format and content of data.Rulesrun`.validate`rules after verifying that a`.write`rule grants access.

The`.validate`rules do not cascade. If any validation rule fails on any path or subpath in the rule, the entire write operation will be rejected. Additionally, the validate definitions only check for non-null values, and subsequently ignore any requests that are deleting data.

Consider the following`.validate`rules:  

      {
        "rules": {
          // write is allowed for all paths
          ".write": true,
          "widget": {
            // a valid widget must have attributes "color" and "size"
            // allows deleting widgets (since .validate is not applied to delete rules)
            ".validate": "newData.hasChildren(['color', 'size'])",
            "size": {
              // the value of "size" must be a number between 0 and 99
              ".validate": "newData.isNumber() &&
                            newData.val() >= 0 &&
                            newData.val() <= 99"
            },
            "color": {
              // the value of "color" must exist as a key in our mythical
              // /valid_colors/ index
              ".validate": "root.child('valid_colors/' + newData.val()).exists()"
            }
          }
        }
      }

Write requests to a database with the rules above would have the following results:  

##### JavaScript

```gdscript
var ref = db.ref("/widget");

// PERMISSION_DENIED: does not have children color and size
ref.set('foo');

// PERMISSION DENIED: does not have child color
ref.set({size: 22});

// PERMISSION_DENIED: size is not a number
ref.set({ size: 'foo', color: 'red' });

// SUCCESS (assuming 'blue' appears in our colors list)
ref.set({ size: 21, color: 'blue'});

// If the record already exists and has a color, this will
// succeed, otherwise it will fail since newData.hasChildren(['color', 'size'])
// will fail to validate
ref.child('size').set(99);
```

##### Objective-C

**Note:**This Firebase product is not available on the App Clip target.  

```objective-c
FIRDatabaseReference *ref = [[[FIRDatabase database] reference] child: @"widget"];

// PERMISSION_DENIED: does not have children color and size
[ref setValue: @"foo"];

// PERMISSION DENIED: does not have child color
[ref setValue: @{ @"size": @"foo" }];

// PERMISSION_DENIED: size is not a number
[ref setValue: @{ @"size": @"foo", @"color": @"red" }];

// SUCCESS (assuming 'blue' appears in our colors list)
[ref setValue: @{ @"size": @21, @"color": @"blue" }];

// If the record already exists and has a color, this will
// succeed, otherwise it will fail since newData.hasChildren(['color', 'size'])
// will fail to validate
[[ref child:@"size"] setValue: @99];
```

##### Swift

**Note:**This Firebase product is not available on the App Clip target.  

```swift
var ref = FIRDatabase.database().reference().child("widget")

// PERMISSION_DENIED: does not have children color and size
ref.setValue("foo")

// PERMISSION DENIED: does not have child color
ref.setValue(["size": "foo"])

// PERMISSION_DENIED: size is not a number
ref.setValue(["size": "foo", "color": "red"])

// SUCCESS (assuming 'blue' appears in our colors list)
ref.setValue(["size": 21, "color": "blue"])

// If the record already exists and has a color, this will
// succeed, otherwise it will fail since newData.hasChildren(['color', 'size'])
// will fail to validate
ref.child("size").setValue(99);
```

##### Java

```java
FirebaseDatabase database = FirebaseDatabase.getInstance();
DatabaseReference ref = database.getReference("widget");

// PERMISSION_DENIED: does not have children color and size
ref.setValue("foo");

// PERMISSION DENIED: does not have child color
ref.child("size").setValue(22);

// PERMISSION_DENIED: size is not a number
Map<String,Object> map = new HashMap<String, Object>();
map.put("size","foo");
map.put("color","red");
ref.setValue(map);

// SUCCESS (assuming 'blue' appears in our colors list)
map = new HashMap<String, Object>();
map.put("size", 21);
map.put("color","blue");
ref.setValue(map);

// If the record already exists and has a color, this will
// succeed, otherwise it will fail since newData.hasChildren(['color', 'size'])
// will fail to validate
ref.child("size").setValue(99);
```

##### REST

```restructuredtext
# PERMISSION_DENIED: does not have children color and size
curl -X PUT -d 'foo' \
https://docs-examples.firebaseio.com/rest/securing-data/example.json

# PERMISSION DENIED: does not have child color
curl -X PUT -d '{"size": 22}' \
https://docs-examples.firebaseio.com/rest/securing-data/example.json

# PERMISSION_DENIED: size is not a number
curl -X PUT -d '{"size": "foo", "color": "red"}' \
https://docs-examples.firebaseio.com/rest/securing-data/example.json

# SUCCESS (assuming 'blue' appears in our colors list)
curl -X PUT -d '{"size": 21, "color": "blue"}' \
https://docs-examples.firebaseio.com/rest/securing-data/example.json

# If the record already exists and has a color, this will
# succeed, otherwise it will fail since newData.hasChildren(['color', 'size'])
# will fail to validate
curl -X PUT -d '99' \
https://docs-examples.firebaseio.com/rest/securing-data/example/size.json
```
| **Note:** Validation rules are not meant to completely replace data validation code in your app. We recommend that you also perform input validation client-side for best performance and best user experience when your app is offline.

<br />

### Cloud Storage

<br />

When evaluating rules, you may also want to evaluate the metadata of the file being uploaded, downloaded, modified, or deleted. This lets you create complex and powerful rules that do things like only allow files with certain content types to be uploaded, or only files greater than a certain size to be deleted.

The`resource`object contains key-value pairs with file metadata surfaced in aCloud Storageobject. These properties can be inspected on`read`or`write`requests to ensure data integrity. The`resource`object checks metadata on existing files in yourCloud Storagebucket.  

      service firebase.storage {
        match /b/{bucket}/o {
          match /images {
            match /{fileName} {
              // Allow reads if a custom 'visibility' field is set to 'public'
              allow read: if resource.metadata.visibility == 'public';
            }
          }
        }
      }

You can also use the`request.resource`object on`write`requests (such as uploads, metadata updates, and deletes. The`request.resource`object gets metadata from the file that will be written if the`write`is allowed.

You can use these two values to prevent unwanted or inconsistent updates or to enforce application constraints, such as file type or size.  

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

A full list of properties in the`resource`object is available in the[reference documentation](https://firebase.google.com/docs/reference/security/storage#resource).

<br />

<br />