# Source: https://firebase.google.com/docs/storage/security.md.txt

# Source: https://firebase.google.com/docs/database/security.md.txt

<br />

Firebase Realtime Database Security Rules determine who has read and write access to your database, how your data is structured, and what indexes exist. These rules live on the Firebase servers and are enforced automatically at all times. Every read and write request will only be completed if your rules allow it. By default, your rules do not allow anyone access to your database. This is to protect your database from abuse until you have time to customize your rules or set up authentication.

Realtime Database Security Rules have a JavaScript-like syntax and come in four types:

|                                                         Rule Types                                                          ||
|---------------|--------------------------------------------------------------------------------------------------------------|
| **.read**     | Describes if and when data is allowed to be read by users.                                                   |
| **.write**    | Describes if and when data is allowed to be written.                                                         |
| **.validate** | Defines what a correctly formatted value will look like, whether it has child attributes, and the data type. |
| **.indexOn**  | Specifies a child to index to support ordering and querying.                                                 |

## Realtime Databasesecurity overview

TheFirebase Realtime Databaseprovides a full set of tools for managing the security of your app. These tools make it easy to authenticate your users, enforce user permissions, and validate inputs.

Firebase-powered apps run more client-side code than those with many other technology stacks. Therefore, the way we approach security may be a bit different than you're used to.
| TheFirebase Realtime Databasehandles many other security details for you. For example, we use SSL with strong 2048 bit keys for our certificates and we follow best practices for authentication tokens.

### Authentication

A common first step in securing your app is identifying your users. This process is called*authentication* . You can use[Firebase Authentication](https://firebase.google.com/docs/auth)to have users to sign in to your app. Firebase Authentication includes drop-in support for common authentication methods like Google and Facebook, as well as email and password login, anonymous login, and more.

User identity is an important security concept. Different users have different data, and sometimes they have different capabilities. For example, in a chat application, each message is associated with the user that created it. Users may also be able to delete their own messages, but not messages posted by other users.

### Authorization

Identifying your user is only part of security. Once you know who they are, you need a way to control their access to data in your database. Realtime Database Security Rules allow you to control access for each user. For example, here's a set of security rules that allows anyone to read the path`/foo/`, but no one to write to it:  

```text
{
  "rules": {
    "foo": {
      ".read": true,
      ".write": false
    }
  }
}
```

`.read`and`.write`rules cascade, so this ruleset grants read access to any data at path`/foo/`as well as any deeper paths such as`/foo/bar/baz`. Note that`.read`and`.write`rules shallower in the database override deeper rules, so read access to`/foo/bar/baz`would still be granted in this example even if a rule at the path`/foo/bar/baz`evaluated to false.

The Realtime Database Security Rules include[built-in variables](https://firebase.google.com/docs/database/security/rules-conditions)and functions that allow you to refer to other paths, server-side timestamps, authentication information, and more. Here's an example of a rule that grants write access for authenticated users to`/users/<uid>/`, where \<uid\> is the ID of the user obtained throughFirebase Authentication.  

```text
{
  "rules": {
    "users": {
      "$uid": {
        ".write": "$uid === auth.uid"
      }
    }
  }
}
```

### Data validation

TheFirebase Realtime Databaseis schemaless. This makes it easy to change things as you develop, but once your app is ready to distribute, it's important for data to stay consistent. The rules language includes a`.validate`rule which allows you to apply validation logic using the same expressions used for`.read`and`.write`rules. The only difference is that**validation rules do not cascade**, so all relevant validation rules must evaluate to true in order for the write to be allowed.

These rule enforce that data written to`/foo/`must be a string less than 100 characters:  

```text
{
  "rules": {
    "foo": {
      ".validate": "newData.isString() && newData.val().length < 100"
    }
  }
}
```

Validation rules have access to all of the same built-in functions and variables as`.read`and`.write`rules. You can use these to create validation rules that are aware of data elsewhere in your database, your user's identity, server time, and much more.
| **Note:** The`.validate`rules are only evaluated for non-null values and do not cascade.

## Defining database indexes

TheFirebase Realtime Databaseallows ordering and querying data. For small data sizes, the database supports ad hoc querying, so indexes are generally not required during development. Before launching your app though, it is important to specify indexes for any queries you have to ensure they continue to work as your app grows.

Indexes are specified using the`.indexOn`rule. Here is an example index declaration that would index the height and length fields for a list of dinosaurs:  

```text
{
  "rules": {
    "dinosaurs": {
      ".indexOn": ["height", "length"]
    }
  }
}
```

<br />

<br />

## Next steps

- [Get started](https://firebase.google.com/docs/database/security/get-started)planning rules development for your database.
- Learn more about[securing your data](https://firebase.google.com/docs/database/security/core-syntax)using security rules.
- Learn more about[specifying indexes](https://firebase.google.com/docs/database/security/indexing-data)using rules.