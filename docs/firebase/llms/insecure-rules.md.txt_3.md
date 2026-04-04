# Source: https://firebase.google.com/docs/rules/insecure-rules.md.txt

# Avoid insecure rules

Use this guide to understand common vulnerabilities in Firebase Security Rules
configurations, review and better secure your own rules,
and test your changes before deploying them.

If you receive an alert that your data isn't properly secured,
review these commonly made errors and update any vulnerable rules.

## Access your Firebase Security Rules

To view your existing Security Rules, use either the Firebase CLI or the
Firebase console. Make sure you edit your rules using the same method,
consistently, to avoid mistakenly overwriting updates. If you're not sure
whether your locally defined rules reflect the most recent updates, the Firebase
console always shows the most recently deployed version of your Firebase Security Rules.

To access your rules from the [Firebase console](https://console.firebase.google.com/), select your
project, then navigate to **Realtime Database** , **Cloud Firestore** or
**Storage** . Click **Rules** once you're in the correct database or storage
bucket.

To access your rules from the Firebase CLI, go to the
rules file noted in your [firebase.json file](https://firebase.google.com/docs/cli#the_firebasejson_file).

## Understand Firebase Security Rules

Firebase Security Rules protect your data from malicious users. When you create a database
instance or Cloud Storage bucket in the Firebase console, you can
choose to either deny access to all users (**Locked mode** ) or grant access to
all users (**Test mode**). While you might want a more open configuration during
development, make sure you take the time to properly configure your rules and
secure your data before deploying your app.

As you're developing your app and testing different configurations for your
rules, use one of the [local Firebase emulators](https://firebase.google.com/docs/rules/emulator-setup) to run your app
in a local development environment.

## Common scenarios with insecure rules

The Security Rules you might have set up by default or as you initially
worked on developing your app should be reviewed and updated
before you deploy your app. Make sure you properly secure your users' data
by avoiding the following common pitfalls.

### Open access

As you set up your Firebase project, you might have set your rules to allow open
access during development. You might think you're the only person using your
app, but if you've deployed it, it's available on the internet. If you're not
authenticating users and configuring security rules, then anyone who guesses
your project ID can steal, modify, or delete the data.

|---|
| Not recommended: Read and write access for all users. ### Cloud Firestore ``` // Allow read/write access to all users under any conditions // Warning: \*\*NEVER\*\* use this ruleset in production; it allows // anyone to overwrite your entire database. service cloud.firestore { match /databases/{database}/documents { match /{document=**} { allow read, write: if true; } } } ``` ### Realtime Database ``` { // Allow read/write access to all users under any conditions // Warning: **NEVER** use this ruleset in production; it allows // anyone to overwrite your entire database. "rules": { ".read": true, ".write": true } } ``` ### Cloud Storage ``` // Anyone can read or write to the bucket, even non-users of your app. // Because it is shared with App Engine, this will also make // files uploaded using App Engine public. // Warning: This rule makes every file in your Cloud Storage bucket accessible to any user. // Apply caution before using it in production, since it means anyone // can overwrite all your files. service firebase.storage { match /b/{bucket}/o { match /{allPaths=**} { allow read, write; } } } ``` |

|---|
| Solution: Rules that restrict read and write access. Build rules that make sense for your data hierarchy. One of the common solutions to this insecurity is user-based security with Firebase Authentication. Learn more about [authenticating users with rules](https://firebase.google.com/docs/rules/rules-and-auth). ### Cloud Firestore #### Content owner only ``` service cloud.firestore { match /databases/{database}/documents { // Allow only authenticated content owners access match /some_collection/{document} { // Allow reads and deletion if the current user owns the existing document allow read, delete: if request.auth.uid == resource.data.author_uid; // Allow creation if the current user owns the new document allow create: if request.auth.uid == request.resource.data.author_uid; // Allow updates by the owner, and prevent change of ownership allow update: if request.auth.uid == request.resource.data.author_uid && request.auth.uid == resource.data.author_uid; } } } ``` #### Mixed public and private access ``` service cloud.firestore { match /databases/{database}/documents { // Allow public read access, but only content owners can write match /some_collection/{document} { // Allow public reads allow read: if true // Allow creation if the current user owns the new document allow create: if request.auth.uid == request.resource.data.author_uid; // Allow updates by the owner, and prevent change of ownership allow update: if request.auth.uid == request.resource.data.author_uid && request.auth.uid == resource.data.author_uid; // Allow deletion if the current user owns the existing document allow delete: if request.auth.uid == resource.data.author_uid; } } } ``` ### Realtime Database #### Content owner only ``` { "rules": { "some_path": { "$uid": { // Allow only authenticated content owners access to their data ".read": "auth !== null && auth.uid === $uid", ".write": "auth !== null && auth.uid === $uid" } } } } ``` #### Mixed public and private access ``` { // Allow anyone to read data, but only authenticated content owners can // make changes to their data "rules": { "some_path/$uid": { ".read": true, // or ".read": "auth.uid !== null" for only authenticated users ".write": "auth.uid === $uid" } } } ``` ### Cloud Storage #### Content owner only ``` // Grants a user access to a node matching their user ID service firebase.storage { match /b/{bucket}/o { // Files look like: "user/<UID>/file.txt" match /user/{userId}/{fileName} { allow read, write: if request.auth.uid == userId; } } } ``` #### Mixed public and private access ``` service firebase.storage { match /b/{bucket}/o { // Files look like: "user/<UID>/file.txt" match /user/{userId}/{fileName} { allow read; allow write: if request.auth.uid == userId; } } } ``` |

### Access for any authenticated user

Sometimes, Security Rules check that a user is logged in, but don't further
restrict access based on that authentication. If one of your rules includes
`auth != null`, confirm that you want any logged-in user to have access to the
data.

|---|
| Not recommended: Any logged-in user has read and write access to your entire database. ### Cloud Firestore ``` service cloud.firestore { match /databases/{database}/documents { match /some_collection/{document} { allow read, write: if request.auth.uid != null; } } } ``` ### Realtime Database ``` { "rules": { ".read": "auth.uid !== null", ".write": "auth.uid !== null" } } ``` ### Cloud Storage ``` // Only authenticated users can read or write to the bucket service firebase.storage { match /b/{bucket}/o { match /{allPaths=**} { allow read, write: if request.auth != null; } } } ``` |

|---|
| Solution: Narrow access using security conditions. When you're checking for authentication, you might also want to use one of the authentication properties to further restrict access to specific users for specific data sets. Learn more about the different [authentication properties](https://firebase.google.com/docs/rules/rules-and-auth). ### Cloud Firestore #### Role-based access ``` service cloud.firestore { match /databases/{database}/documents { // Assign roles to all users and refine access based on user roles match /some_collection/{document} { allow read: if get(/databases/$(database)/documents/users/$(request.auth.uid)).data.role == "Reader" allow write: if get(/databases/$(database)/documents/users/$(request.auth.uid)).data.role == "Writer" // Note: Checking for roles in your database using `get` (as in the code // above) or `exists` carry standard charges for read operations. } } } ``` #### Attribute-based access ``` // Give each user in your database a particular attribute // and set it to true/false // Then, use that attribute to grant access to subsets of data // For example, an "administrator" attribute set // to "true" grants write access to data service cloud.firestore { match /databases/{database}/documents { match /some_collection/{document} { allow write: if get(/databases/$(database)/documents/users/$(request.auth.uid)).data.admin == true; allow read: true; } } } ``` #### Mixed public and private access ``` service cloud.firestore { match /databases/{database}/documents { // Allow public read access, but only content owners can write match /some_collection/{document} { allow read: if true allow write: if request.auth.uid == request.resource.data.author_uid } } } ``` ### Realtime Database #### Content owner only ``` { "rules": { "some_path": { "$uid": { // Allow only authenticated content owners access to their data ".read": "auth.uid === $uid", ".write": "auth.uid === $uid" } } } } ``` #### Path-delineated access ``` { "rules": { "some_path/$uid": { ".write": "auth.uid === $uid", // Create a "public" subpath in your dataset "public": { ".read": true // or ".read": "auth.uid !== null" }, // Create a "private" subpath in your dataset "private": { ".read": "auth.uid === $uid" } } } } ``` #### Mixed public and private access ``` { // Allow anyone to read data, but only authenticated content owners can // make changes to their data "rules": { "some_path/$uid": { ".read": true, // or ".read": "auth.uid !== null" for only authenticated users ".write": "auth.uid === $uid" } } } ``` ### Cloud Storage #### Group-based access ``` // Allow reads if the group ID in your token matches the file metadata `owner` property // Allow writes if the group ID is in the user's custom token match /files/{groupId}/{fileName} { allow read: if resource.metadata.owner == request.auth.token.groupId; allow write: if request.auth.token.groupId == groupId; } ``` #### Content owner only ``` // Grants a user access to a node matching their user ID service firebase.storage { match /b/{bucket}/o { // Files look like: "user/<UID>/file.txt" match /user/{userId}/{fileName} { allow read, write: if request.auth.uid == userId; } } } ``` #### Mixed public and private access ``` service firebase.storage { match /b/{bucket}/o { // Files look like: "user/<UID>/file.txt" match /user/{userId}/{fileName} { allow read; allow write: if request.auth.uid == userId; } } } ``` |

### (Realtime Database) Improperly inherited rules

Realtime Database Security Rules cascade, with rules at more shallow, parent paths overriding
rules at deeper, child nodes. When you write a rule at a child node, remember
that it can only grant additional privileges. You can't refine or revoke
access to data at a deeper path in your database.

|---|
| Not recommended: Refining rules at child paths ``` { "rules": { "foo": { // allows read to /foo/* ".read": "data.child('baz').val() === true", "bar": { /* ignored, since read was allowed already */ ".read": false } } } } ``` |

|---|
| Solution: Write rules at parent paths that are broad, and grant more specific privileges at child paths If your data access needs require more granularity, keep your rules granular. Learn more about cascading Realtime Database Security Rules in [Core syntax of Realtime Database Security Rules](https://firebase.google.com/docs/database/security/core-syntax#read_and_write_rules_cascade). |

### Closed access

While you're developing your app, another common approach is to keep your
data locked down. Typically, this means you've closed off read and write
access to all users, as follows:

### Cloud Firestore

```
// Deny read/write access to all users under any conditions
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if false;
    }
  }
}
```

### Realtime Database

```
{
  "rules": {
    ".read": false,
    ".write": false
  }
}
    
```

### Cloud Storage

```
// Access to files through Cloud Storage is completely disallowed.
// Files may still be accessible through App Engine or Google Cloud Storage APIs.

service firebase.storage {
  match /b/{bucket}/o {
    match /{allPaths=**} {
      allow read, write: if false;
    }
  }
}
```

The Firebase Admin SDKs and Cloud Functions can still access your
database. Use these rules when you intend to use Cloud Firestore or
Realtime Database as a server-only
backend in conjunction with the Firebase
Admin SDK. While it is secure, you should test that your app's clients can
properly retrieve data.

Learn more about Cloud Firestore Security Rules and how they work in
[Get Started with Cloud Firestore Security Rules](https://firebase.google.com/docs/rules/get-started).

## Test your Cloud Firestore Security Rules

To check your app's behavior and verify your Cloud Firestore Security Rules configurations,
use the [Firebase Emulator](https://firebase.google.com/docs/rules/emulator-setup). Use the Cloud Firestore
emulator to run and automate unit tests in a local environment before you deploy
any changes.

To quickly validate Firebase Security Rules in the Firebase console, use
the [Firebase Rules Simulator](https://firebase.google.com/docs/rules/simulator).