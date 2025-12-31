# Source: https://firebase.google.com/docs/storage/security/startBAK.md.txt

In typical apps, developers must build and maintain many servers that perform authentication, authorization, and data validation, as well as the developer's business logic. Apps usingCloud Storage for Firebasemake use ofFirebase AuthenticationandFirebase Security RulesforCloud Storageto handle serverless authentication, authorization, and data validation.

UsingCloud StorageandCloud StorageSecurity Rulesmeans that you can focus on building a great user experience, without having to manage infrastructure or write complex server-side authentication and authorization code!

## Overview

Cloud StorageSecurity Rulesare used to determine who has read and write access to files stored inCloud Storage, as well as how files are structured and what metadata they contain. The basic type of rule is the`allow`rule, which allows`read`and`write`operations if an optionally specified condition is met. Some examples of rules are:  

```scilab
// Rules can optionally specify a condition
allow write: if <condition>;
```

Rules`match`file paths representing[Cloud Storagereferences](https://firebase.google.com/docs/storage/web/create-reference). Rules may`match`one or more file paths, and more than one rule can`match`the file path in a given`request`:  

```scilab
// Rules match specific paths
match /images/profilePhoto.png {
  allow write: if <condition>;
}

match /images/croppedProfilePhoto.png {
  allow write: if <other_condition>;
}
```

The context of the rule evaluation is also exposed through the`request`and`resource`objects, which provide information such as the auth context (`request.auth`) and the existing object's size (`resource.size`).  

```scilab
// Rules can specify conditions that consider the request context
match /images/profilePhoto.png {
  allow write: if request.auth != null && request.resource.size < 5 * 1024 * 1024;
}
```
| **Note:** Cloud Storage for Firebaseuses the sameGoogle Cloud Storagebucket as your project's defaultApp Engineapp, so your[Cloud StorageSecurity Rules](https://firebase.google.com/docs/storage/security)may apply to any files that exist in that app.

Learn more aboutCloud StorageSecurity Rulesin the[Secure Files](https://firebase.google.com/docs/storage/security/secure-files)section.

## Sample Rules

| **Note:** Before launch, make sure that you evaluate your rules to ensure they provide the maximum level of security your application needs. Launching your app with`default`or`public`rules may allow unintended or unauthorized access to your stored data.

Cloud StorageSecurity Rulesmust first specify the`service`(in our case`firebase.storage`), and theCloud Storagebucket (via`match /b/{bucket}/o`) which rules are evaluated against. The default rules requireFirebase Authentication, but here are some examples of other common rules with different access control.  

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

During development, you can use the public rules in place of the default rules to set your files publicly readable and writable. This is very useful for prototyping, as you can get started without setting upFirebase Authentication. However, becauseCloud Storageshares a bucket with your defaultApp Engineapp, this rule also makes any data used by that app public as well.

User rules allow you to give each of your authenticated users their own personal file storage. You can also lock down your files entirely by using the private rules, but be aware that your users won't be able to read or write anything throughCloud Storagewith these rules. Users accessing files from yourApp Engineapp or the[Google Cloud StorageAPIs](https://cloud.google.com/storage/docs/reference/libraries)may still have access.

## Edit Rules

Cloud Storageprovides an easy way to edit yourCloud StorageSecurity Rulesvia the**Rules** tab in the[Firebaseconsole](https://console.firebase.google.com/)Storage section. In the**Rules** tab, you can quickly and easily view and edit your current rules. These rules are deployed by clicking**Publish** , or by saving the file (`ctrl/cmd + s`). Rules are immediately uploaded toCloud Storageservers, but may take up to five minutes to become live.

TheFirebaseCLI can be used to deploy rules as well. If you select`Storage`when running`firebase init`, a`storage.rules`file with a copy of the[default rules](https://firebase.google.com/docs/storage/security/start#sample-rules)will be created in your project directory. You can deploy these rules using the`firebase deploy`command. If you have multiple buckets in your project, you can use[deploy targets](https://firebase.google.com/docs/cli/targets)to deploy rules to all of your buckets at once from the same project folder.
| **Note:** **When you[deploy security rules using theFirebaseCLI](https://firebase.google.com/docs/cli/#deployment), the rules defined in your project directory overwrite any existing rules in theFirebaseconsole.** So, if you choose to define or edit your security rules using theFirebaseconsole, make sure that you also update the rules defined in your project directory.

Learn more about how file based security works in the[Secure Files](https://firebase.google.com/docs/storage/security/secure-files)section, or understand user based security in the[User Security](https://firebase.google.com/docs/storage/security/user-security)section.
| **Note:** Detailed reference documentation is available in the[Firebase Security RulesforCloud StorageAPI reference](https://firebase.google.com/docs/reference/security/storage).