# Source: https://firebase.google.com/docs/database/security/core-syntax.md.txt

# Source: https://firebase.google.com/docs/storage/security/core-syntax.md.txt

<br />

Firebase Security RulesforCloud Storageallow you to control access to objects stored inCloud Storagebuckets. The flexible rules syntax allows you to create rules to control any operation, from all writes to yourCloud Storagebucket to operations on a specific file.
| **Note:** Buckets inCloud Storageonly contain files, they don't contain directories. On this page you'll see slashes`/`in filenames, like`/images/profilePhoto.png`, which suggest there is a hierarchy of directories and sub-directories in a bucket. However, filenames can include prefixes with slashes to allow you to define unique filenames that look like the full directory paths we're used to seeing in file systems.

This guide describes the basic syntax and structure ofCloud StorageSecurity Rulesto create complete rulesets.

## Service and database declaration

Firebase Security RulesforCloud Storagealways begin with the following declaration:  

    service firebase.storage {
        // ...
    }

The`service firebase.storage`declaration scopes the rules toCloud Storage, preventing conflicts betweenCloud StorageSecurity Rulesand rules for other products such asCloud Firestore.

## Basic read/write rules

Basic rules consist of a`match`statement identifyingCloud Storagebuckets, a match statement specifying a filename, and an`allow`expression detailing when reading the specified data is allowed.`allow`expressions specify the*access methods* (e.g., read, write) involved, and*conditions*under which access is either allowed or denied.

In your default ruleset, the first`match`statement uses a`{bucket}`wildcard expression to indicate the rules apply to all buckets in your project. We'll discuss the idea of wildcard matches more in the next section.  

    service firebase.storage {
      // The {bucket} wildcard indicates we match files in all Cloud Storage buckets
      match /b/{bucket}/o {
        // Match filename
        match /filename {
          allow read: if <condition>;
          allow write: if <condition>;
        }
      }
    }

All match statements point to files. A match statement can point to a specific file, as in`match /images/profilePhoto.png`.

### Match wildcards

In additiont to pointing to a single file,Rulescan use**wildcards** to point to any file with a given string prefix in its name, including slashes, as in`match /images/{imageId}`.

In the example above, the match statement uses the`{imageId}`wildcard syntax. This means the rule applies to any file with`/images/`at the start of its name, such as`/images/profilePhoto.png`or`/images/croppedProfilePhoto.png`. When the`allow`expressions in the match statement are evaluated, the`imageId`variable will resolve to the image filename, such as`profilePhoto.png`or`croppedProfilePhoto.png`.

A wildcard variable can be referenced from within the`match`to provide file name or path authorization:  

    // Another way to restrict the name of a file
    match /images/{imageId} {
      allow read: if imageId == "profilePhoto.png";
    }

| **Note:** Users can only access files that yourFirebase Security Rulesspecifically allow you to access. For example, the rules shown above allow access only to files with`/images/`at the beginning of their names; as a result, they also deny access to files with different filename prefixes.

## Hierarchical data

As we said before, there is no hierarchical structure inside aCloud Storagebucket. But by using a file naming convention, often one that includes slashes in filenames, we can mimic a structure that looks like a nested series of directories and sub-directories. It is important to understand howFirebase Security Rulesinteract with these filenames.

Consider the situation of a set of files with names that all begin with the`/images/`stem.Firebase Security Rulesapply only at the matched filename, so the access controls defined on the`/images/`stem do not apply to the`/mp3s/`stem. Instead, write explicit rules that match different filename patterns:  

    service firebase.storage {
      match /b/{bucket}/o {
        match /images/{imageId} {
          allow read, write: if <condition>;
        }

        // Explicitly define rules for the 'mp3s' pattern
        match /mp3s/{mp3Id} {
          allow read, write: if <condition>;
        }
      }
    }

When nesting`match`statements, the path of the inner`match`statement is always appended to the path of the outer`match`statement. The following two rulesets are therefore equivalent:  

    service firebase.storage {
      match /b/{bucket}/o {
        match /images {
          // Exact match for "images/profilePhoto.png"
          match /profilePhoto.png {
            allow write: if <condition>;
          }
        }
      }
    }

    service firebase.storage {
      match /b/{bucket}/o {
        // Exact match for "images/profilePhoto.png"
        match /images/profilePhoto.png {
          allow write: if <condition>;
          }
      }
    }

### Recursive match wildcards

In addition to wildcards that match and return strings at the end of a filename, a**multiple segment wildcard** can be declared for more complex matching by adding`=**`to the wildcard name, like`{path=**}`:  

    // Partial match for files that start with "images"
    match /images {

      // Exact match for "images/**"
      // e.g. images/users/user:12345/profilePhoto.png is matched
      // images/profilePhoto.png is also matched!
      match /{allImages=**} {
        // This rule matches one or more path segments (**)
        // allImages is a path that contains all segments matched
        allow read: if <other_condition>;
      }
    }

If multiple rules match a file, the result is the`OR`of the result of all rules evaluations. That is, if any rule the file matches evaluates to`true`, the result is`true`.

In the rules above, the file "images/profilePhoto.png" can be read if either`condition`or`other_condition`evaluate to true, while the file "images/users/user:12345/profilePhoto.png" is only subject to the result of`other_condition`.

Cloud StorageSecurity Rulesdo not cascade, and rules are only evaluated when the request path matches a path with rules specified.  

### Version 1

Firebase Security Rulesuse version 1 by default. In version 1, recursive wildcards match one or more filename elements, not zero or more elements. Thus,`match /images/{filenamePrefixWildcard}/{imageFilename=**}`matches a filename like /images/profilePics/profile.png, but not /images/badge.png. Use`/images/{imagePrefixorFilename=**}`instead.

Recursive wildcards must come at the end of a match statement.

We recommend you use version 2 for its more powerful features.

### Version 2

In version 2 ofFirebase Security Rules, recursive wildcards match zero or more path items. Thus,`/images/{filenamePrefixWildcard}/{imageFilename=**}`matches filenames /images/profilePics/profile.png and /images/badge.png.

You must opt-in to version 2 by adding`rules_version = '2';`at the top of your security rules:  

    rules_version = '2';
    service cloud.storage {
      match /b/{bucket}/o {
       ...
     }
    }

You can have at most one recursive wildcard per match statement, but in version 2, you can place this wildcard anywhere in the match statement. For example:  

    rules_version = '2';
    service firebase.storage {
     match /b/{bucket}/o {
       // Matches any file in a songs "subdirectory" under the
       // top level of your Cloud Storage bucket.
       match /{prefixSegment=**}/songs/{mp3filenames} {
         allow read, write: if <condition>;
       }
      }
    }

## Granular operations

In some situations, it's useful to break down`read`and`write`into more granular operations. For example, your app may want to enforce different conditions on file creation than on file deletion.

A`read`operation can be broken into`get`and`list`.
| **Note:** `list`Rulesoperations and hence theCloud StorageList API are only available in projects that useRulesVersion 2.

A`write`rule can be broken into`create`,`update`, and`delete`:  

```css+lasso
service firebase.storage {
  match /b/{bucket}/o {
    // A read rule can be divided into read and list rules
    match /images/{imageId} {
      // Applies to single file read requests
      allow get: if <condition>;
      // Applies to list and listAll requests (Rules Version 2)
      allow list: if <condition>;

    // A write rule can be divided into create, update, and delete rules
    match /images/{imageId} {
      // Applies to writes to file contents
      allow create: if <condition>;

      // Applies to updates to (pre-existing) file metadata
      allow update: if <condition>;

      // Applies to delete operations
      allow delete: if <condition>;
    }
  }
 }
}
```

## Overlapping match statements

It's possible for a filename to match more than one`match`statement. In the case where multiple`allow`expressions match a request, the access is allowed if**any** of the conditions is`true`:  

    service firebase.storage {
      match b/{bucket}/o {
        // Matches file names directly inside of '/images/'.
        match /images/{imageId} {
          allow read, write: if false;
        }

        // Matches file names anywhere under `/images/`
        match /images/{imageId=**} {
          allow read, write: if true;
        }
      }
    }

In the example above, all reads and writes to files whose name starts with`/images/`are allowed because the second rule is always`true`, even when the first rule is`false`.

## Rules are not filters

Once you secure your data and begin to perform file operations, keep in mind that security rules are not filters. You cannot perform operations on a set of files matching a filename pattern and expectCloud Storageto access only the files that the current client has permission to access.

For example, take the following security rule:  

    service firebase.storage {
      match /b/{bucket}/o {
        // Allow the client to read files with contentType 'image/png'
        match /aFileNamePrefix/{aFileName} {
          allow read: if resource.contentType == 'image/png';
        }
      }
    }

Denied: This rule rejects the following request because the result set can include files where`contentType`is not`image/png`:  

##### Web

```css+lasso
filesRef = storage.ref().child("aFilenamePrefix");

filesRef.listAll()
    .then(function(result) {
      console.log("Success: ", result.items);
    })
});
```

Rules inCloud StorageSecurity Rulesevaluate each query against its potential result and fails the request if it could return a file that the client does not have permission to read. Access requests must follow the constraints set by your rules.

## Next steps

You can deepen your understanding ofFirebase Security RulesforCloud Storage:

- Learn the next major concept of the Rules language, dynamic[conditions](https://firebase.google.com/docs/storage/security/rules-conditions), which let your Rules check user authorization, compare existing and incoming data, validate incoming data, and more.

- Review typical security use cases and the[Firebase Security Rulesdefinitions that address them](https://firebase.google.com/docs/rules/basics).

You can exploreFirebase Security Rulesuse cases specific toCloud Storage: