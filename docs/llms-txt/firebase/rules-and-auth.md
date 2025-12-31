# Source: https://firebase.google.com/docs/rules/rules-and-auth.md.txt

<br />

Firebase Security Rulesprovide access control and data validation in a format that supports multiple levels of complexity. To build user-based and role-based access systems that keep your users' data safe, use[Firebase Authentication](https://firebase.google.com/docs/auth)withFirebase Security Rules.

## Identify users

Authenticationidentifies users requesting access to your data and provides that information as a variable you can leverage in your rules. The`auth`variable contains the following information:

- **`uid`:**A unique user ID, assigned to the requesting user.
- **`token`:** A map of values collected byAuthentication.

The`auth.token`variable contains the following values:

|            Field            |                                                                                                                                                                                                                           Description                                                                                                                                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `email`                     | The email address associated with the account, if present.                                                                                                                                                                                                                                                                                                                                                                                                      |
| `email_verified`            | `true`if the user has verified they have access to the`email`address. Some providers automatically verify email addresses they own.                                                                                                                                                                                                                                                                                                                             |
| `phone_number`              | The phone number associated with the account, if present.                                                                                                                                                                                                                                                                                                                                                                                                       |
| `name`                      | The user's display name, if set.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `sub`                       | The user's Firebase UID. This is unique within a project.                                                                                                                                                                                                                                                                                                                                                                                                       |
| `firebase.identities`       | Dictionary of all the identities that are associated with this user's account. The keys of the dictionary can be any of the following:`email`,`phone`,`google.com`,`facebook.com`,`github.com`,`twitter.com`. The values of the dictionary are arrays of unique identifiers for each identity provider associated with the account. For example,`auth.token.firebase.identities["google.com"][0]`contains the first Google user ID associated with the account. |
| `firebase.sign_in_provider` | The sign-in provider used to obtain this token. Can be one of the following strings:`custom`,`password`,`phone`,`anonymous`,`google.com`,`facebook.com`,`github.com`,`twitter.com`.                                                                                                                                                                                                                                                                             |
| `firebase.tenant`           | The tenantId associated with the account, if present. e.g.`tenant2-m6tyz`                                                                                                                                                                                                                                                                                                                                                                                       |

If you want to add customized authentication attributes, the`auth.token`variable also contains any[custom claims](https://firebase.google.com/docs/auth/admin/custom-claims)you specify.

When the user requesting access isn't signed in, the`auth`variable is`null`. You can leverage this in your rules if, for example, you want to limit read access to authenticated users ---`auth != null`. However, we generally recommend limiting write access further.

For more information about the`auth`variable, see the reference documentation for[Cloud Firestore](https://firebase.google.com/docs/reference/rules/rules.firestore.Request#auth),[Realtime Database](https://firebase.google.com/docs/reference/security/database/#variables), and[Cloud Storage](https://firebase.google.com/docs/reference/security/storage/#request).

## Leverage user information in rules

In practice, using authenticated information in your rules makes your rules more powerful and flexible. You can control access to data based on user identity.

In your rules, define how the information in the`auth`variable --- the requestor's user information --- matches the user information associated with the requested data.

For example, your app may want to make sure users can only read and write their own data. In this scenario, you would want a match between the`auth.uid`variable and the user ID on the requested data:  

### Cloud Firestore

    service cloud.firestore {
      match /databases/{database}/documents {
        // Make sure the uid of the requesting user matches name of the user
        // document. The wildcard expression {userId} makes the userId variable
        // available in rules.
        match /users/{userId} {
          allow read, write: if request.auth != null && request.auth.uid == userId;
        }
      }
    }

### Realtime Database

    {
      "rules": {
        "users": {
          "$userId": {
            // grants write access to the owner of this user account
            // whose uid must exactly match the key ($userId)
            ".write": "$userId === auth.uid"
          }
        }
      }
    }

### Cloud Storage

    service firebase.storage {
      // Only a user can upload their file, but anyone can view it
      match /users/{userId}/{fileName} {
        allow read;
        allow write: if request.auth != null && request.auth.uid == userId;
      }
    }

## Define custom user information

You can further leverage the`auth`variable to define custom fields assigned to your app's users.

For example, assume you want to create an "admin" role that enables write access on certain paths. You would assign that attribute to users, and then leverage it in the rules granting access on the paths.

InCloud Firestore, you can add a custom field to users' documents and retrieve that field's value with an embedded read in your rules. So, your admin-based rule would look like the following example:  

### Cloud Firestore

    service cloud.firestore {
      match /databases/{database}/documents/some_collection: {
        // Remember that, in Cloud Firestore, reads embedded in your rules are billed operations
        write: if request.auth != null && get(/databases/(database)/documents/users/$(request.auth.uid)).data.admin == true;
        read: if request.auth != null;
      }
    }

You can access custom claims inRulesafter[creating custom claims](https://firebase.google.com/docs/auth/admin/custom-claims)inAuthentication. You can then reference those custom claims using the`auth.token`variable.  

### Cloud Firestore

    service cloud.firestore {
      match /databases/{database}/documents {
        // For attribute-based access control, check for an admin claim
        allow write: if request.auth.token.admin == true;
        allow read: true;

        // Alterntatively, for role-based access, assign specific roles to users
        match /some_collection/{document} {
         allow read: if request.auth.token.reader == "true";
         allow write: if request.auth.token.writer == "true";
       }
      }
    }

### Realtime Database

    {
      "rules": {
        "some_path": {
          "$sub_path": {
          // Create a custom claim for the admin role
          ".write": "auth.uid !== null && auth.token.writer === true",
          ".read": "auth.uid !== null"
          }
        }
      }
    }

### Cloud Storage

    service firebase.storage {
      // Create a custom claim for the admin role
      match /files/{fileName} {
        allow read: if request.auth.uid != null;
        allow write: if request.auth.token.admin == true;
      }
    }

To see more examples of basicRulesleveragingAuthentication, see[Basic Security Rules](https://firebase.google.com/docs/rules/basics).