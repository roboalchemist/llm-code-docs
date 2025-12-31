# Source: https://firebase.google.com/docs/firestore/security/rules-conditions.md.txt

# Source: https://firebase.google.com/docs/database/security/rules-conditions.md.txt

# Source: https://firebase.google.com/docs/storage/security/rules-conditions.md.txt

<br />

This guide builds on the[learn the core syntax of theFirebase Security Ruleslanguage](https://firebase.google.com/docs/storage/security/core-syntax)guide to show how to add conditions to yourFirebase Security RulesforCloud Storage.

The primary building block ofCloud StorageSecurity Rulesis the**condition** . A condition is a boolean expression that determines whether a particular operation should be allowed or denied. For basic rules, using`true`and`false`literals as conditions works perfectly well. But theFirebase Security RulesforCloud Storagelanguage gives you ways to write more complex conditions that can:

- Check user authentication
- Validate incoming data

## Authentication

Firebase Security RulesforCloud Storageintegrates withFirebase Authenticationto provide powerful user based authentication toCloud Storage. This allows for granular access control based on claims of aFirebase Authenticationtoken.

When an authenticated user performs a request againstCloud Storage, the`request.auth`variable is populated with the user's`uid`(`request.auth.uid`) as well as the claims of theFirebase AuthenticationJWT (`request.auth.token`).

Additionally, when using custom authentication, additional claims are surfaced in the`request.auth.token`field.

When an unauthenticated user performs a request, the`request.auth`variable is`null`.

Using this data, there are several common ways to use authentication to secure files:

- Public: ignore`request.auth`
- Authenticated private: check that`request.auth`is not`null`
- User private: check that`request.auth.uid`equals a path`uid`
- Group private: check the custom token's claims to match a chosen claim, or read the file metadata to see if a metadata field exists

### Public

Any rule that doesn't consider the`request.auth`context can be considered a`public`rule, since it doesn't consider the authentication context of the user. These rules can be useful for surfacing public data such as game assets, sound files, or other static content.  

```gdscript
// Anyone to read a public image if the file is less than 100kB
// Anyone can upload a public file ending in '.txt'
match /public/{imageId} {
  allow read: if resource.size < 100 * 1024;
  allow write: if imageId.matches(".*\\.txt");
}
```

### Authenticated private

In certain cases, you may want data to be viewable by all authenticated users of your application, but not by unauthenticated users. Since the`request.auth`variable is`null`for all unauthenticated users, all you have to do is check the`request.auth`variable exists in order to require authentication:  

```scilab
// Require authentication on all internal image reads
match /internal/{imageId} {
  allow read: if request.auth != null;
}
```

### User private

By far the most common use case for`request.auth`will be to provide individual users with granular permissions on their files: from uploading profile pictures to reading private documents.

Since files inCloud Storagehave a full "path" to the file, all it takes to make a file controlled by a user is a piece of unique, user identifying information in the filename prefix (such as the user's`uid`) that can be checked when the rule is evaluated:  

```gdscript
// Only a user can upload their profile picture, but anyone can view it
match /users/{userId}/profilePicture.png {
  allow read;
  allow write: if request.auth.uid == userId;
}
```

### Group private

Another equally common use case will be to allow group permissions on an object, such as allowing several team members to collaborate on a shared document. There are several approaches to doing this:

- Mint aFirebase Authentication[custom token](https://firebase.google.com/docs/auth/admin/create-custom-tokens)that contains additional information about a group member (such as a group ID)
- Include group information (such as a group ID or list of authorized`uid`s) in the[file metadata](https://firebase.google.com/docs/storage/web/file-metadata)

Once this data is stored in the token or file metadata, it can be referenced from within a rule:  

```mysql
// Allow reads if the group ID in your token matches the file metadata's `owner` property
// Allow writes if the group ID is in the user's custom token
match /files/{groupId}/{fileName} {
  allow read: if resource.metadata.owner == request.auth.token.groupId;
  allow write: if request.auth.token.groupId == groupId;
}
```

## Request Evaluation

Uploads, downloads, metadata changes, and deletes are evaluated using the`request`sent toCloud Storage. In addition to the user's unique ID and theFirebase Authenticationpayload in the`request.auth`object as described above, the`request`variable contains the file path where the request is being performed, the time when the request is received, and the new`resource`value if the request is a write.

The`request`object also contains the user's unique ID and theFirebase Authenticationpayload in the`request.auth`object, which will be explained further in the[User-Based Security](https://firebase.google.com/docs/storage/security/rules-conditions#authentication)section of the docs.

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

|       Property       |         Type          |                                                      Description                                                       |
|----------------------|-----------------------|------------------------------------------------------------------------------------------------------------------------|
| `name`               | string                | The full name of the object                                                                                            |
| `bucket`             | string                | The name of the bucket this object resides in.                                                                         |
| `generation`         | int                   | The[Google Cloud Storageobject generation](https://cloud.google.com/storage/docs/object-versioning)of this object.     |
| `metageneration`     | int                   | The[Google Cloud Storageobject metageneration](https://cloud.google.com/storage/docs/object-versioning)of this object. |
| `size`               | int                   | The size of the object in bytes.                                                                                       |
| `timeCreated`        | timestamp             | A timestamp representing the time an object was created.                                                               |
| `updated`            | timestamp             | A timestamp representing the time an object was last updated.                                                          |
| `md5Hash`            | string                | An MD5 hash of the object.                                                                                             |
| `crc32c`             | string                | A crc32c hash of the object.                                                                                           |
| `etag`               | string                | The etag associated with this object.                                                                                  |
| `contentDisposition` | string                | The content disposition associated with this object.                                                                   |
| `contentEncoding`    | string                | The content encoding associated with this object.                                                                      |
| `contentLanguage`    | string                | The content language associated with this object.                                                                      |
| `contentType`        | string                | The content type associated with this object.                                                                          |
| `metadata`           | map\<string, string\> | Key/value pairs of additional, developer specified custom metadata.                                                    |

`request.resource`contains all of these with the exception of`generation`,`metageneration`,`etag`,`timeCreated`, and`updated`.
| **Note:** Detailed documentation for these properties is available in the[Firebase Security RulesforCloud StorageAPI reference](https://firebase.google.com/docs/reference/security/storage#resource).

## Enhance withCloud Firestore

You can access documents inCloud Firestoreto evaluate other authorization criteria.

Using the`firestore.get()`and`firestore.exists()`functions, your security rules can evaluate incoming requests against documents inCloud Firestore. The`firestore.get()`and`firestore.exists()`functions both expect fully specified document paths. When using variables to construct paths for`firestore.get()`and`firestore.exists()`, you need to explicitly escape variables using the`$(variable)`syntax.
| **Note:** Like any other access toCloud Firestoredocuments, reads of documents from StorageRulescount towards your project's Firestore quota and billing.
| **Warning:** StorageRulescan only access documents from the defaultCloud Firestoredatabase when[multiple databases](https://firebase.google.com/docs/firestore/manage-databases)are active.

In the example below, we see a rule that restricts read access to files to those users who are members of particular clubs.  

```text
service firebase.storage {
  match /b/{bucket}/o {
    match /users/{club}/files/{fileId} {
      allow read: if club in
        firestore.get(/databases/(default)/documents/users/$(request.auth.id)).data.memberships
    }
  }
}
```
In the next example, only a user's friends can see their photos.  

```text
service firebase.storage {
  match /b/{bucket}/o {
    match /users/{userId}/photos/{fileId} {
      allow read: if
        firestore.exists(/databases/(default)/documents/users/$(userId)/friends/$(request.auth.id))
    }
  }
}
```

Once you create and save your firstCloud StorageSecurity Rulesthat use theseCloud Firestorefunctions, you'll be prompted in theFirebaseconsole orFirebaseCLI to enable permissions to connect the two products.

You can disable the feature by removing an IAM role, as described in[Manage and deployFirebase Security Rules](https://firebase.google.com/docs/rules/manage-deploy#manage_permissions_for_cross-service).

## Validate data

Firebase Security RulesforCloud Storagecan also be used for data validation, including validating file name and path as well as file metadata properties such as`contentType`and`size`.  

```gdscript
service firebase.storage {
  match /b/{bucket}/o {
    match /images/{imageId} {
      // Only allow uploads of any image file that's less than 5MB
      allow write: if request.resource.size < 5 * 1024 * 1024
                   && request.resource.contentType.matches('image/.*');
    }
  }
}
```

## Custom functions

As yourFirebase Security Rulesbecome more complex, you may want to wrap sets of conditions in functions that you can reuse across your ruleset. Security rules support custom functions. The syntax for custom functions is a bit like JavaScript, butFirebase Security Rulesfunctions are written in a domain-specific language that has some important limitations:

- Functions can contain only a single`return`statement. They cannot contain any additional logic. For example, they cannot execute loops or call external services.
- Functions can automatically access functions and variables from the scope in which they are defined. For example, a function defined within the`service firebase.storage`scope has access to the`resource`variable, and forCloud Firestoreonly, built-in functions such as`get()`and`exists()`.
- Functions may call other functions but may not recurse. The total call stack depth is limited to 10.
- In version`rules2`, functions can define variables using the`let`keyword. Functions can have any number of let bindings, but must end with a return statement.

A function is defined with the`function`keyword and takes zero or more arguments. For example, you may want to combine the two types of conditions used in the examples above into a single function:  

    service firebase.storage {
      match /b/{bucket}/o {
        // True if the user is signed in or the requested data is 'public'
        function signedInOrPublic() {
          return request.auth.uid != null || resource.data.visibility == 'public';
        }
        match /images/{imageId} {
          allow read, write: if signedInOrPublic();
        }
        match /mp3s/{mp3Ids} {
          allow read: if signedInOrPublic();
        }
      }
    }

Using functions in yourFirebase Security Rulesmakes them more maintainable as the complexity of your rules grows.

## Next steps

After this discussion of conditions, you've got a more sophisticated understanding of Rules and are ready to:

**Learn how to handle core use cases, and learn the workflow for developing, testing and deploying Rules:**

- Write rules that address[common scenarios](https://firebase.google.com/docs/rules/basics).
- Build on your knowledge by reviewing situations where you must[spot and avoid insecure Rules](https://firebase.google.com/docs/rules/insecure-rules).
- Test rules using the[Cloud Storageemulator and dedicated Security Rules test library](https://firebase.google.com/docs/rules/emulator-setup).
- Review the methods available for[deployingRules](https://firebase.google.com/docs/rules/manage-deploy).