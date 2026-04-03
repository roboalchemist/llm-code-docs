# Source: https://firebase.google.com/docs/storage/security/secure-filesBAK.md.txt

Cloud Storage for Firebaseprovides a declarative path-based security model calledFirebase Security RulesforCloud Storagewhich allows you to quickly and easily secure your files.

## Understand Rules

Firebase Security RulesforCloud Storageare used to determine who has read and write access to files stored inCloud Storage, as well as how files are structured and what metadata they contain. The basic type of rule is the`allow`rule, which allows`read`and`write`requests if an optionally specified condition is specified, for example:  

```scilab
// If no condition is specified, the rule evaluates to true
allow read;

// Rules can optionally specify a condition
allow write: if <condition>;

// Rules can also specify multiple request methods
allow read, write: if <condition>;
```

## Matching Paths

Cloud StorageSecurity Rules`match`the file paths used to access files inCloud Storage. Rules can`match`exact paths or wildcard paths, and rules can also be nested. If no match rule allows a request method, or the condition evaluates to`false`, the request is denied.

### Exact Matches

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

### Nested Matches

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

### Wildcard Matches

Rules can also be used to`match`a pattern using wildcards. A wildcard is a named variable that represents either a single string such as`profilePhoto.png`, or multiple path segments, such as`images/profilePhoto.png`.

A wildcard is created by adding curly braces around the wildcard name, like`{string}`. A multiple segment wildcard can be declared by adding`=**`to the wildcard name, like`{path=**}`:  

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

In the rules above, the file "images/profilePhoto.png" can be read if either`condition`or`other_condition`evaluate to true, while the file "images/users/user:12345/profilePhoto.png" is only subject to the result of`other_condition`.

A wildcard variable can be referenced from within the`match`provide file name or path authorization:  

```scilab
// Another way to restrict the name of a file
match /images/{imageId} {
  allow read: if imageId == "profilePhoto.png";
}
```

Cloud StorageSecurity Rulesdo not cascade, and rules are only evaluated when the request path matches a path with rules specified.

## Request Evaluation

Uploads, downloads, metadata changes, and deletes are evaluated using the`request`sent toCloud Storage. The`request`variable contains the file path where the request is being performed, the time when the request is received, and the new`resource`value if the request is a write. HTTP headers and authentication state are also included.

The`request`object also contains the user's unique ID and theFirebase Authenticationpayload in the`request.auth`object, which will be explained further in the[User-Based Security](https://firebase.google.com/docs/storage/security/user-security)section of the docs.

A full list of properties in the`request`object is available below:

|  Property  |         Type          |                                                                    Description                                                                     |
|------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `auth`     | map\<string, string\> | When a user is logged in, provides`uid`, the user's unique ID, and`token`, a map ofFirebase AuthenticationJWT claims. Otherwise, it will be`null`. |
| `params`   | map\<string, string\> | Map containing the query parameters of the request.                                                                                                |
| `path`     | path                  | A`path`representing the path the request is being performed at.                                                                                    |
| `resource` | map\<string, string\> | The new resource value, present only on`write`requests.                                                                                            |
| `time`     | timestamp             | A timestamp representing the server time the request is evaluated at.                                                                              |

| **Note:** Detailed documentation for these properties is available in the[Firebase Security RulesforCloud StorageAPI reference](https://firebase.google.com/docs/reference/security/storage#request).

## Resource Evaluation

When evaluating rules, you may also want to evaluate the metadata of the file being uploaded, downloaded, modified, or deleted. This allows you to create complex and powerful rules that do things like only allow files with certain content types to be uploaded, or only files greater than a certain size to be deleted.

Firebase Security RulesforCloud Storageprovides file metadata in the`resource`object, which contains key/value pairs of the metadata surfaced in aCloud Storageobject. These properties can be inspected on`read`or`write`requests to ensure data integrity.

On`write`requests (such as uploads, metadata updates, and deletes), in addition to the`resource`object, which contains file metadata for the file that currently exists at the request path, you also have the ability to use the`request.resource`object, which contains a subset of the file metadata to be written if the write is allowed. You can use these two values to ensure data integrity or enforce application constraints such as file type or size.

A full list of properties in the`resource`object is available below:

|       Property       |         Type          |                                              Description                                               |
|----------------------|-----------------------|--------------------------------------------------------------------------------------------------------|
| `name`               | string                | The full name of the object                                                                            |
| `bucket`             | string                | The name of the bucket this object resides in.                                                         |
| `generation`         | int                   | The[GCS object generation](https://cloud.google.com/storage/docs/object-versioning)of this object.     |
| `metageneration`     | int                   | The[GCS object metageneration](https://cloud.google.com/storage/docs/object-versioning)of this object. |
| `size`               | int                   | The size of the object in bytes.                                                                       |
| `timeCreated`        | timestamp             | A timestamp representing the time an object was created.                                               |
| `updated`            | timestamp             | A timestamp representing the time an object was last updated.                                          |
| `md5Hash`            | string                | An MD5 hash of the object.                                                                             |
| `crc32c`             | string                | A crc32c hash of the object.                                                                           |
| `etag`               | string                | The etag associated with this object.                                                                  |
| `contentDisposition` | string                | The content disposition associated with this object.                                                   |
| `contentEncoding`    | string                | The content encoding associated with this object.                                                      |
| `contentLanguage`    | string                | The content language associated with this object.                                                      |
| `contentType`        | string                | The content type associated with this object.                                                          |
| `metadata`           | map\<string, string\> | Key/value pairs of additional, developer specified custom metadata.                                    |

`request.resource`contains all of these with the exception of`generation`,`metageneration`,`etag`,`timeCreated`, and`updated`.
| **Note:** Detailed documentation for these properties is available in the[Firebase Security RulesforCloud StorageAPI reference](https://firebase.google.com/docs/reference/security/storage#resource).

## Full Example

Putting it all together, you can create a full example of rules for an image storage solution:  

```gdscript
service firebase.storage {
 match /b/{bucket}/o {
   match /images {
     // Cascade read to any image type at any path
     match /{allImages=**} {
       allow read;
     }

     // Allow write files to the path "images/*", subject to the constraints:
     // 1) File is less than 5MB
     // 2) Content type is an image
     // 3) Uploaded content type matches existing content type (if it exists)
     // 4) File name (stored in imageId wildcard variable) is less than 32 characters
     match /{imageId} {
       allow write: if request.resource.size < 5 * 1024 * 1024
                    && request.resource.contentType.matches('image/.*')
                    && (resource == null || request.resource.contentType == resource.contentType)
                    && imageId.size() < 32
     }
   }
 }
}
```

Now, let's integrateFirebase Authenticationfor granular per user file access in the[User Security](https://firebase.google.com/docs/storage/security/user-security)section.