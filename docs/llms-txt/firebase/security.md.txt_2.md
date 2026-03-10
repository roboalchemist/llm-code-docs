# Source: https://firebase.google.com/docs/storage/security.md.txt

# Understand Firebase Security Rules for Cloud Storage

<br />

[Video](https://www.youtube.com/watch?v=PUBnlbjZFAI)

Traditionally, security has been one of the most complex parts of app
development. In most applications, developers must build and run a server that
handles authentication (who a user is) and authorization (what a user can do).
Authentication and authorization are hard to set up, harder to get right, and
critical to the success of your product.

Similar to how Firebase Authentication makes it easy for you to authenticate your
users, Firebase Security Rules for Cloud Storage makes it easy for you to authorize users
and validate requests. Cloud Storage Security Rules manage the complexity for you by
allowing you to specify path based permissions. In just a few lines of code, you
can write authorization rules that restrict Cloud Storage requests to a
certain user or limit the size of an upload.

> [!NOTE]
> **Note:** If you use Google App Engine and have a default Cloud Storage bucket with a name format of `*.appspot.com`, you may need to consider [how your security rules impact access to App Engine files](https://firebase.google.com/docs/storage/gcp-integration#security-rules-and-app-engine-files).

The Firebase Realtime Database has a similar feature, called
[Firebase Realtime Database Security Rules](https://firebase.google.com/docs/database/security)

## Authentication

Knowing who your users are is an important part of building an application, and
Firebase Authentication provides an easy to use, secure, client side only solution
to authentication. Firebase Security Rules for Cloud Storage ties in to Firebase Authentication
for user based security. When a user is authenticated with Firebase Authentication,
the `request.auth` variable in Cloud Storage Security Rules becomes an object that
contains the user's unique ID (`request.auth.uid`) and all other user
information in the token (`request.auth.token`). When the user is not
authenticated, `request.auth` is `null`. This allows you to securely control
data access on a per-user basis. You can learn more in the
[Authentication](https://firebase.google.com/docs/storage/security/rules-conditions#authentication) section.

## Authorization

Identifying your user is only part of security. Once you know who they are, you
need a way to control their access to files in Cloud Storage.

Cloud Storage lets you specify per file and per path authorization
rules that live on our servers and determine access to the files in your app.
For example, the default Cloud Storage Security Rules require Firebase Authentication in
order to perform any `read` or `write` operations on all files:

```
service firebase.storage {
  match /b/{bucket}/o {
    match /someFolder/{fileName} {
      allow read, write: if request.auth != null;
    }
  }
}
```

You can edit these rules by selecting a Firebase app in the [Firebase console](https://console.firebase.google.com/)
and viewing the `Rules` tab of the Storage section.

## Data Validation

Firebase Security Rules for Cloud Storage can also be used for data validation, including
validating file name and path as well as file metadata properties such as
`contentType` and `size`.

```
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

## Next steps

- [Get started](https://firebase.google.com/docs/storage/security/get-started) planning rules development
  for your Cloud Storage buckets.

- Learn more about [securing your data](https://firebase.google.com/docs/storage/security/core-syntax)
  using security rules.