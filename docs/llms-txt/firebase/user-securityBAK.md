# Source: https://firebase.google.com/docs/storage/security/user-securityBAK.md.txt

Firebase Security RulesforCloud Storageintegrates withFirebase Authenticationto provide powerful user based authentication toCloud Storage. This allows for granular access control based on claims of aFirebase Authenticationtoken.

## User authentication

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

Since files inCloud Storagehave a full path to the file, all it takes to make a file controlled by a user is a piece of unique, user identifying information in the file path (such as the user's`uid`) that can be checked when the rule is evaluated:  

```gdscript
// Only a user can upload their profile picture, but anyone can view it
match /users/{userId}/profilePicture.png {
  allow read;
  allow write: if request.auth != null && request.auth.uid == userId;
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

## Full example

Simple cases of the four common types of authentication restrictions are shown in the example below:  

```css+lasso
service firebase.storage {
  match /b/{bucket}/o {
    match /images {
      // Anyone can view any image (no auth, publicly readable)
      match /{allImages=**} {
        allow read;
      }

      // Only authenticated users can write to "public" images
      match /public/{imageId} {
        allow write: if request.auth != null;
      }

      // Only an individual user can write to "their" images
      match /{userId}/{imageId} {
        allow write: if request.auth.uid == userId;
      }

      // Allow a "group" of users to read/write to shared images
      // An owner metadata property on the object contains the groupId for reads
      // A custom token has been minted with a groupId property for writes
      match /{groupId}/{imageId} {
        allow read: if resource.metadata.owner == request.auth.token.groupId;
        allow write: if request.auth.token.groupId == groupId;
      }
    }
  }
}
```