# Source: https://firebase.google.com/docs/storage/security/startBAK.md.txt

# Get started with Cloud Storage Security Rules

In typical apps, developers must build and maintain many servers that perform
authentication, authorization, and data validation, as well as the developer's
business logic. Apps using Cloud Storage for Firebase make use of
Firebase Authentication and Firebase Security Rules for Cloud Storage to handle serverless
authentication, authorization, and data validation.

Using Cloud Storage and Cloud Storage Security Rules means that you can focus on
building a great user experience, without having to manage infrastructure or
write complex server-side authentication and authorization code!

## Overview

Cloud Storage Security Rules are used to determine who has read and write access to
files stored in Cloud Storage, as well as how files are structured and
what metadata they contain. The basic type of rule is the `allow` rule, which
allows `read` and `write` operations if an optionally specified condition is
met. Some examples of rules are:

```
// Rules can optionally specify a condition
allow write: if <condition>;
```

Rules `match` file paths representing
[Cloud Storage references](https://firebase.google.com/docs/storage/web/create-reference). Rules
may `match` one or more file paths, and more than one rule can `match` the file
path in a given `request`:

```
// Rules match specific paths
match /images/profilePhoto.png {
  allow write: if <condition>;
}

match /images/croppedProfilePhoto.png {
  allow write: if <other_condition>;
}
```

The context of the rule evaluation is also exposed through the `request` and
`resource` objects, which provide information such as the auth context
(`request.auth`) and the existing object's size (`resource.size`).

```
// Rules can specify conditions that consider the request context
match /images/profilePhoto.png {
  allow write: if request.auth != null && request.resource.size < 5 * 1024 * 1024;
}
```

> [!NOTE]
> **Note:** Cloud Storage for Firebase uses the same Google Cloud Storage bucket as your project's default App Engine app, so your [Cloud Storage Security Rules](https://firebase.google.com/docs/storage/security) may apply to any files that exist in that app.

Learn more about Cloud Storage Security Rules in the
[Secure Files](https://firebase.google.com/docs/storage/security/secure-files) section.

## Sample Rules

> [!NOTE]
> **Note:** Before launch, make sure that you evaluate your rules to ensure they provide the maximum level of security your application needs. Launching your app with `default` or `public` rules may allow unintended or unauthorized access to your stored data.

Cloud Storage Security Rules must first specify the `service` (in our case
`firebase.storage`), and the Cloud Storage bucket
(via `match /b/{bucket}/o`) which rules are
evaluated against. The default rules require Firebase Authentication, but here are
some examples of other common rules with different access control.

### Default

    // Only authenticated users can read or write to the folder
    service firebase.storage {
      match /b/{bucket}/o {
        match /someFolder/{fileName} {
          allow read, write: if request.auth != null;
        }
      }
    }

### Public

    // Anyone can read or write to the folder, even non-users of your app.
    // Because it is shared with App Engine, this will also make
    // files uploaded via App Engine public.
    service firebase.storage {
      match /b/{bucket}/o {
        match /someFolder/{fileName} {
          allow read, write;
        }
      }
    }

### User

    // Grants a user access to a node matching their user ID
    service firebase.storage {
      match /b/{bucket}/o {
        // Files look like: "user/<UID>/file.txt"
        match /user/{userId}/{fileName} {
          allow read, write: if request.auth != null && request.auth.uid == userId;
        }
      }
    }

### Private

    // Access to files through Cloud Storage for Firebase is completely disallowed.
    // Files may still be accessible through App Engine or Google Cloud Storage APIs.
    service firebase.storage {
      match /b/{bucket}/o {
        match /{allPaths=**} {
          allow read, write: if false;
        }
      }
    }

During development, you can use the public rules in place of the default
rules to set your files publicly readable and writable. This is very useful for
prototyping, as you can get started without setting up Firebase Authentication.
However, because Cloud Storage shares a bucket with your default
App Engine app, this rule also makes any data used by that app
public as well.

User rules allow you to give each of your authenticated users their own personal
file storage. You can also lock down your files entirely by using the private
rules, but be aware that your users won't be able to read or write anything
through Cloud Storage with these rules. Users accessing files from
your App Engine app or the
[Google Cloud Storage APIs](https://cloud.google.com/storage/docs/reference/libraries)
may still have access.

## Edit Rules

Cloud Storage provides an easy way to edit your Cloud Storage Security Rules
via the **Rules** tab in the [Firebase console](https://console.firebase.google.com/) Storage section.
In the **Rules** tab, you can quickly and easily view and edit your current
rules. These rules are deployed by clicking **Publish** , or by saving the file
(`ctrl/cmd + s`). Rules are immediately uploaded to Cloud Storage
servers, but may take up to five minutes to become live.

The Firebase CLI can be used to deploy rules as well. If you select
`Storage` when running `firebase init`, a `storage.rules` file with a copy of
the [default rules](https://firebase.google.com/docs/storage/security/start#sample-rules) will be created
in your project directory. You can deploy these rules using the
`firebase deploy` command. If you have multiple buckets in your project, you
can use [deploy targets](https://firebase.google.com/docs/cli/targets) to deploy rules to all of your
buckets at once from the same project folder.

> [!NOTE]
> **Note:** **When you
> [deploy security rules using the Firebase CLI](https://firebase.google.com/docs/cli/#deployment),
> the rules defined in your project directory overwrite any existing rules in the
> Firebase console.** So, if you choose to define or edit your security rules using the Firebase console, make sure that you also update the rules defined in your project directory.

Learn more about how file based security works in the
[Secure Files](https://firebase.google.com/docs/storage/security/secure-files) section, or understand user
based security in the [User Security](https://firebase.google.com/docs/storage/security/user-security)
section.

> [!NOTE]
> **Note:** Detailed reference documentation is available in the [Firebase Security Rules for Cloud Storage API reference](https://firebase.google.com/docs/reference/security/storage).