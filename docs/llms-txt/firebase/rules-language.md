# Source: https://firebase.google.com/docs/rules/rules-language.md.txt

<br />

Firebase Security Rulesleverage flexible, powerful, custom languages that support a wide range of complexity and granularity. You can make yourRulesas specific or as general as makes sense for your app.Realtime Databaserules use a syntax that looks like JavaScript in a JSON structure.Cloud FirestoreandCloud Storagerules use a language based on the[Common Expression Language (CEL)](https://github.com/google/cel-spec), that builds on CEL with`match`and`allow`statements that support conditionally granted access.

Because these are custom languages, however, there is a learning curve. Use this guide to better understand theRuleslanguage as you dive deeper into more complex rules.

Select a product to learn more about its rules.

## Basic structure

<br />

### Cloud Firestore

<br />

Firebase Security RulesinCloud FirestoreandCloud Storageuse the following structure and syntax:  

    service <<name>> {
      // Match the resource path.
      match <<path>> {
        // Allow the request if the following conditions are true.
        allow <<methods>> : if <<condition>>
      }
    }

The following key concepts are important to understand as you build the rules:

- **Request:** The method or methods invoked in the`allow`statement. These are methods you're allowing to run. The standard methods are:`get`,`list`,`create`,`update`, and`delete`. The`read`and`write`convenience methods enable broad read and write access on the specified database or storage path.
- **Path:**The database or storage location, represented as a URI path.
- **Rule:** The`allow`statement, which includes a condition that permits a request if it evaluates to true.

Each of these concepts is described in further detail below.

<br />

### Cloud Storage

<br />

Firebase Security RulesinCloud FirestoreandCloud Storageuse the following structure and syntax:  

    service <<name>> {
      // Match the resource path.
      match <<path>> {
        // Allow the request if the following conditions are true.
        allow <<methods>> : if <<condition>>
      }
    }

The following key concepts are important to understand as you build the rules:

- **Request:** The method or methods invoked in the`allow`statement. These are methods you're allowing to run. The standard methods are:`get`,`list`,`create`,`update`, and`delete`. The`read`and`write`convenience methods enable broad read and write access on the specified database or storage path.
- **Path:**The database or storage location, represented as a URI path.
- **Rule:** The`allow`statement, which includes a condition that permits a request if it evaluates to true.

Each of these concepts is described in further detail below.

<br />

### Realtime Database

<br />

InRealtime Database,Firebase Security Rulesconsist of JavaScript-like expressions contained in a JSON document.

They use the following syntax:  

    {
      "rules": {
        "<<path>>": {
        // Allow the request if the condition for each method is true.
          ".read": <<condition>>,
          ".write": <<condition>>,
          ".validate": <<condition>>
        }
      }
    }

There are three basic elements in the rule:

- **Path:**The database location. This mirrors your database's JSON structure.
- **Request:** These are the methods the rule uses to grant access. The`read`and`write`rules grant broad read and write access, while`validate`rules act as a secondary verification to grant access based on incoming or existing data.
- **Condition:**The condition that permits a request if it evaluates to true.

<br />

<br />

## Rule constructs

<br />

### Cloud Firestore

<br />

The basic elements of a rule inCloud FirestoreandCloud Storageare as follows:

- The`service`declaration: Declares the Firebase product the rules apply to.
- The`match`block: Defines a path in the database or storage bucket the rules apply to.
- The`allow`statement: Provides conditions for granting access, differentiated by methods. The supported methods include:`get`,`list`,`create`,`update`,`delete`, and the convenience methods`read`and`write`.
- Optional`function`declarations: Provide the ability to combine and wrap conditions for use across multiple rules.

The`service`contains one or more`match`blocks with`allow`statements that provide conditions granting access to requests. The`request`and`resource`variables are available for use in rule conditions. TheFirebase Security Ruleslanguage also supports`function`declarations.

### Syntax version

The`syntax`statement indicates the version of the Firebase Rules language used to write the source. The latest version of the language is`v2`.  

    rules_version = '2';
    service cloud.firestore {
    ...
    }

If no`rules_version`statement is supplied, your rules will be evaluated using the`v1`engine.

### Service

The`service`declaration defines which Firebase product, or service, your rules apply to. You can only include one`service`declaration per source file.  

### Cloud Firestore

    service cloud.firestore {
     // Your 'match' blocks with their corresponding 'allow' statements and
     // optional 'function' declarations are contained here
    }

### Cloud Storage

    service firebase.storage {
      // Your 'match' blocks with their corresponding 'allow' statements and
      // optional 'function' declarations are contained here
    }

If you're defining rules for bothCloud FirestoreandCloud Storageusing theFirebaseCLI, you'll have to maintain them in separate files.

### Match

A`match`block declares a`path`pattern that is matched against the path for the requested operation (the incoming`request.path`). The body of the`match`must have one or more nested`match`blocks,`allow`statements, or`function`declarations. The path in nested`match`blocks is relative to the path in the parent`match`block.

The`path`pattern is a directory-like name that may include variables or wildcards. The`path`pattern allows for single-path segment and multi-path segment matches. Any variables bound in a`path`are visible within the`match`scope or any nested scope where the`path`is declared.

Matches against a`path`pattern may be partial or complete:

- **Partial matches:** The`path`pattern is a prefix-match of the`request.path`.
- **Complete matches:** The`path`pattern matches the entire`request.path`.

When a**complete** match is made the rules within the block are evaluated. When a**partial** match is made the nested`match`rules are tested to see whether any nested`path`will**complete**the match.

The rules in each**complete** `match`are evaluated to determine whether to permit the request. If any matching rule grants access, the request is permitted. If no matching rule grants access, the request is denied.  

    // Given request.path == /example/hello/nested/path the following
    // declarations indicate whether they are a partial or complete match and
    // the value of any variables visible within the scope.
    service firebase.storage {
      // Partial match.
      match /example/{singleSegment} {   // `singleSegment` == 'hello'
        allow write;                     // Write rule not evaluated.
        // Complete match.
        match /nested/path {             // `singleSegment` visible in scope.
          allow read;                    // Read rule is evaluated.
        }
      }
      // Complete match.
      match /example/{multiSegment=**} { // `multiSegment` == /hello/nested/path
        allow read;                      // Read rule is evaluated.
      }
    }

As the example above shows, the`path`declarations supports the following variables:

- **Single-segment wildcard:** A wildcard variable is declared in a path by wrapping a variable in curly braces:`{variable}`. This variable is accessible within the`match`statement as a`string`.
- **Recursive wildcard:** The recursive, or multi-segment, wildcard matches multiple path segments at or below a path. This wildcard matches all paths below the location you set it to. You can declare it by adding the`=**`string at the end of your segment variable:`{variable=**}`. This variable is accessible within the`match`statement as a`path`object.

| Avoid using recursive wildcards unless you intend for permissive security rules to propagate to all nested paths.

### Allow

The`match`block contains one or more`allow`statements. These are your actual rules. You can apply`allow`rules to one or more methods. The conditions on an`allow`statement must evaluate to true forCloud FirestoreorCloud Storageto grant any incoming request. You can also write`allow`statements without conditions, for example,`allow read`. If the`allow`statement doesn't include a condition, however, it always allows the request for that method.

If any of the`allow`rules for the method are satisfied, the request is allowed. Additionally, if a broader rule grants access,Rulesgrant access and ignore any more granular rules that might limit access.

Consider the following example, where any user can read or delete any of their own files. A more granular rule only allows writes if the user requesting the write owns the file and the file is a PNG. A user can delete any files at the subpath --- even if they're not PNGs --- because the earlier rule allows it.  

    service firebase.storage {
      // Allow the requestor to read or delete any resource on a path under the
      // user directory.
      match /users/{userId}/{anyUserFile=**} {
        allow read, delete: if request.auth != null && request.auth.uid == userId;
      }

      // Allow the requestor to create or update their own images.
      // When 'request.method' == 'delete' this rule and the one matching
      // any path under the user directory would both match and the `delete`
      // would be permitted.

      match /users/{userId}/images/{imageId} {
        // Whether to permit the request depends on the logical OR of all
        // matched rules. This means that even if this rule did not explicitly
        // allow the 'delete' the earlier rule would have.
        allow write: if request.auth != null && request.auth.uid == userId && imageId.matches('*.png');
      }
    }

#### Method

Each`allow`statement includes a method that grants access for incoming requests of the same method.

|  Method  |                       Type of request                        |
|----------|--------------------------------------------------------------|
| Convenience methods                                                    ||
| `read`   | Any type of read request                                     |
| `write`  | Any type of write request                                    |
| Standard methods                                                       ||
| `get`    | Read requests for single documents or files                  |
| `list`   | Read requests for queries and collections                    |
| `create` | Write new documents or files                                 |
| `update` | Write to existing database documents or update file metadata |
| `delete` | Delete data                                                  |

You can't overlap read methods in the same`match`block or conflicting write methods in the same`path`declaration.

For example, the following rules would fail:  

    service bad.example {
      match /rules/with/overlapping/methods {
        // This rule allows reads to all authenticated users
        allow read: if request.auth != null;

        match another/subpath {
          // This secondary, more specific read rule causes an error
          allow get: if request.auth != null && request.auth.uid == "me";
          // Overlapping write methods in the same path cause an error as well
          allow write: if request.auth != null;
          allow create: if request.auth != null && request.auth.uid == "me";
        }
      }
    }

### Function

As your security rules become more complex, you may want to wrap sets of conditions in functions that you can reuse across your ruleset. Security rules support custom functions. The syntax for custom functions is a bit like JavaScript, but security rules functions are written in a domain-specific language that has some important limitations:

- Functions can contain only a single`return`statement. They cannot contain any additional logic. For example, they cannot execute loops or call external services.
- Functions can automatically access functions and variables from the scope in which they are defined. For example, a function defined within the`service cloud.firestore`scope has access to the`resource`variable and built-in functions such as`get()`and`exists()`.
- Functions may call other functions but may not recurse. The total call stack depth is limited to 20.
- In rules version`v2`, functions can define variables using the`let`keyword. Functions can have up to 10 let bindings, but must end with a return statement.

A function is defined with the`function`keyword and takes zero or more arguments. For example, you may want to combine the two types of conditions used in the examples above into a single function:  

    service cloud.firestore {
      match /databases/{database}/documents {
        // True if the user is signed in or the requested data is 'public'
        function signedInOrPublic() {
          return request.auth.uid != null || resource.data.visibility == 'public';
        }

        match /cities/{city} {
          allow read, write: if signedInOrPublic();
        }

        match /users/{user} {
          allow read, write: if signedInOrPublic();
        }
      }
    }

Here is an example showing function arguments and let assignments. Let assignment statements must be separated by semicolons.  

    function isAuthorOrAdmin(userId, article) {
      let isAuthor = article.author == userId;
      let isAdmin = exists(/databases/$(database)/documents/admins/$(userId));
      return isAuthor || isAdmin;
    }

Note how the`isAdmin`assignment enforces a lookup of the admins collection. For lazy evaluation without requiring unneeded lookups, take advantage of the short-circuiting nature of`&&`(AND) and`||`(OR) comparisons to call a second function only if`isAuthor`is shown to be true (for`&&`comparisons) or false (for`||`comparisons).  

    function isAdmin(userId) {
      return exists(/databases/$(database)/documents/admins/$(userId));
    }
    function isAuthorOrAdmin(userId, article) {
      let isAuthor = article.author == userId;
      // `||` is short-circuiting; isAdmin called only if isAuthor == false.
      return isAuthor || isAdmin(userId);
    }

Using functions in your security rules makes them more maintainable as the complexity of your rules grows.

<br />

### Cloud Storage

<br />

The basic elements of a rule inCloud FirestoreandCloud Storageare as follows:

- The`service`declaration: Declares the Firebase product the rules apply to.
- The`match`block: Defines a path in the database or storage bucket the rules apply to.
- The`allow`statement: Provides conditions for granting access, differentiated by methods. The supported methods include:`get`,`list`,`create`,`update`,`delete`, and the convenience methods`read`and`write`.
- Optional`function`declarations: Provide the ability to combine and wrap conditions for use across multiple rules.

The`service`contains one or more`match`blocks with`allow`statements that provide conditions granting access to requests. The`request`and`resource`variables are available for use in rule conditions. TheFirebase Security Ruleslanguage also supports`function`declarations.

### Syntax version

The`syntax`statement indicates the version of the Firebase Rules language used to write the source. The latest version of the language is`v2`.  

    rules_version = '2';
    service cloud.firestore {
    ...
    }

If no`rules_version`statement is supplied, your rules will be evaluated using the`v1`engine.

### Service

The`service`declaration defines which Firebase product, or service, your rules apply to. You can only include one`service`declaration per source file.  

### Cloud Firestore

    service cloud.firestore {
     // Your 'match' blocks with their corresponding 'allow' statements and
     // optional 'function' declarations are contained here
    }

### Cloud Storage

    service firebase.storage {
      // Your 'match' blocks with their corresponding 'allow' statements and
      // optional 'function' declarations are contained here
    }

If you're defining rules for bothCloud FirestoreandCloud Storageusing theFirebaseCLI, you'll have to maintain them in separate files.

### Match

A`match`block declares a`path`pattern that is matched against the path for the requested operation (the incoming`request.path`). The body of the`match`must have one or more nested`match`blocks,`allow`statements, or`function`declarations. The path in nested`match`blocks is relative to the path in the parent`match`block.

The`path`pattern is a directory-like name that may include variables or wildcards. The`path`pattern allows for single-path segment and multi-path segment matches. Any variables bound in a`path`are visible within the`match`scope or any nested scope where the`path`is declared.

Matches against a`path`pattern may be partial or complete:

- **Partial matches:** The`path`pattern is a prefix-match of the`request.path`.
- **Complete matches:** The`path`pattern matches the entire`request.path`.

When a**complete** match is made the rules within the block are evaluated. When a**partial** match is made the nested`match`rules are tested to see whether any nested`path`will**complete**the match.

The rules in each**complete** `match`are evaluated to determine whether to permit the request. If any matching rule grants access, the request is permitted. If no matching rule grants access, the request is denied.  

    // Given request.path == /example/hello/nested/path the following
    // declarations indicate whether they are a partial or complete match and
    // the value of any variables visible within the scope.
    service firebase.storage {
      // Partial match.
      match /example/{singleSegment} {   // `singleSegment` == 'hello'
        allow write;                     // Write rule not evaluated.
        // Complete match.
        match /nested/path {             // `singleSegment` visible in scope.
          allow read;                    // Read rule is evaluated.
        }
      }
      // Complete match.
      match /example/{multiSegment=**} { // `multiSegment` == /hello/nested/path
        allow read;                      // Read rule is evaluated.
      }
    }

As the example above shows, the`path`declarations supports the following variables:

- **Single-segment wildcard:** A wildcard variable is declared in a path by wrapping a variable in curly braces:`{variable}`. This variable is accessible within the`match`statement as a`string`.
- **Recursive wildcard:** The recursive, or multi-segment, wildcard matches multiple path segments at or below a path. This wildcard matches all paths below the location you set it to. You can declare it by adding the`=**`string at the end of your segment variable:`{variable=**}`. This variable is accessible within the`match`statement as a`path`object.

| Avoid using recursive wildcards unless you intend for permissive security rules to propagate to all nested paths.

### Allow

The`match`block contains one or more`allow`statements. These are your actual rules. You can apply`allow`rules to one or more methods. The conditions on an`allow`statement must evaluate to true forCloud FirestoreorCloud Storageto grant any incoming request. You can also write`allow`statements without conditions, for example,`allow read`. If the`allow`statement doesn't include a condition, however, it always allows the request for that method.

If any of the`allow`rules for the method are satisfied, the request is allowed. Additionally, if a broader rule grants access,Rulesgrant access and ignore any more granular rules that might limit access.

Consider the following example, where any user can read or delete any of their own files. A more granular rule only allows writes if the user requesting the write owns the file and the file is a PNG. A user can delete any files at the subpath --- even if they're not PNGs --- because the earlier rule allows it.  

    service firebase.storage {
      // Allow the requestor to read or delete any resource on a path under the
      // user directory.
      match /users/{userId}/{anyUserFile=**} {
        allow read, delete: if request.auth != null && request.auth.uid == userId;
      }

      // Allow the requestor to create or update their own images.
      // When 'request.method' == 'delete' this rule and the one matching
      // any path under the user directory would both match and the `delete`
      // would be permitted.

      match /users/{userId}/images/{imageId} {
        // Whether to permit the request depends on the logical OR of all
        // matched rules. This means that even if this rule did not explicitly
        // allow the 'delete' the earlier rule would have.
        allow write: if request.auth != null && request.auth.uid == userId && imageId.matches('*.png');
      }
    }

#### Method

Each`allow`statement includes a method that grants access for incoming requests of the same method.

|  Method  |                       Type of request                        |
|----------|--------------------------------------------------------------|
| Convenience methods                                                    ||
| `read`   | Any type of read request                                     |
| `write`  | Any type of write request                                    |
| Standard methods                                                       ||
| `get`    | Read requests for single documents or files                  |
| `list`   | Read requests for queries and collections                    |
| `create` | Write new documents or files                                 |
| `update` | Write to existing database documents or update file metadata |
| `delete` | Delete data                                                  |

You can't overlap read methods in the same`match`block or conflicting write methods in the same`path`declaration.

For example, the following rules would fail:  

    service bad.example {
      match /rules/with/overlapping/methods {
        // This rule allows reads to all authenticated users
        allow read: if request.auth != null;

        match another/subpath {
          // This secondary, more specific read rule causes an error
          allow get: if request.auth != null && request.auth.uid == "me";
          // Overlapping write methods in the same path cause an error as well
          allow write: if request.auth != null;
          allow create: if request.auth != null && request.auth.uid == "me";
        }
      }
    }

### Function

As your security rules become more complex, you may want to wrap sets of conditions in functions that you can reuse across your ruleset. Security rules support custom functions. The syntax for custom functions is a bit like JavaScript, but security rules functions are written in a domain-specific language that has some important limitations:

- Functions can contain only a single`return`statement. They cannot contain any additional logic. For example, they cannot execute loops or call external services.
- Functions can automatically access functions and variables from the scope in which they are defined. For example, a function defined within the`service cloud.firestore`scope has access to the`resource`variable and built-in functions such as`get()`and`exists()`.
- Functions may call other functions but may not recurse. The total call stack depth is limited to 20.
- In rules version`v2`, functions can define variables using the`let`keyword. Functions can have up to 10 let bindings, but must end with a return statement.

A function is defined with the`function`keyword and takes zero or more arguments. For example, you may want to combine the two types of conditions used in the examples above into a single function:  

    service cloud.firestore {
      match /databases/{database}/documents {
        // True if the user is signed in or the requested data is 'public'
        function signedInOrPublic() {
          return request.auth.uid != null || resource.data.visibility == 'public';
        }

        match /cities/{city} {
          allow read, write: if signedInOrPublic();
        }

        match /users/{user} {
          allow read, write: if signedInOrPublic();
        }
      }
    }

Here is an example showing function arguments and let assignments. Let assignment statements must be separated by semicolons.  

    function isAuthorOrAdmin(userId, article) {
      let isAuthor = article.author == userId;
      let isAdmin = exists(/databases/$(database)/documents/admins/$(userId));
      return isAuthor || isAdmin;
    }

Note how the`isAdmin`assignment enforces a lookup of the admins collection. For lazy evaluation without requiring unneeded lookups, take advantage of the short-circuiting nature of`&&`(AND) and`||`(OR) comparisons to call a second function only if`isAuthor`is shown to be true (for`&&`comparisons) or false (for`||`comparisons).  

    function isAdmin(userId) {
      return exists(/databases/$(database)/documents/admins/$(userId));
    }
    function isAuthorOrAdmin(userId, article) {
      let isAuthor = article.author == userId;
      // `||` is short-circuiting; isAdmin called only if isAuthor == false.
      return isAuthor || isAdmin(userId);
    }

Using functions in your security rules makes them more maintainable as the complexity of your rules grows.

<br />

### Realtime Database

<br />

As outlined above,Realtime DatabaseRulesinclude three basic elements: the database location as a mirror of the database's JSON structure, the request type, and the condition granting access.

### Database location

The structure of your rules should follow the structure of the data you have stored in your database. For example, in a chat app with a list of messages, you might have data that looks like this:  

      {
        "messages": {
          "message0": {
            "content": "Hello",
            "timestamp": 1405704370369
          },
          "message1": {
            "content": "Goodbye",
            "timestamp": 1405704395231
          },
          ...
        }
      }

Your rules should mirror that structure. For example:  

      {
        "rules": {
          "messages": {
            "$message": {
              // only messages from the last ten minutes can be read
              ".read": "data.child('timestamp').val() > (now - 600000)",

              // new messages must have a string content and a number timestamp
              ".validate": "newData.hasChildren(['content', 'timestamp']) &&
                            newData.child('content').isString() &&
                            newData.child('timestamp').isNumber()"
            }
          }
        }
      }

As the example above shows,Realtime DatabaseRulessupport a`$location`variable to match path segments. Use the`$`prefix in front of your path segment to match your rule to any child nodes along the path.  

      {
        "rules": {
          "rooms": {
            // This rule applies to any child of /rooms/, the key for each room id
            // is stored inside $room_id variable for reference
            "$room_id": {
              "topic": {
                // The room's topic can be changed if the room id has "public" in it
                ".write": "$room_id.contains('public')"
              }
            }
          }
        }
      }

You can also use the`$variable`in parallel with constant path names.  

      {
        "rules": {
          "widget": {
            // a widget can have a title or color attribute
            "title": { ".validate": true },
            "color": { ".validate": true },

            // but no other child paths are allowed
            // in this case, $other means any key excluding "title" and "color"
            "$other": { ".validate": false }
          }
        }
      }

### Method

InRealtime Database, there are three types of rules. Two of these rule types ---`read`and`write`--- apply to the method of an incoming request. The`validate`rule type enforces data structures and validates the format and content of data.Rulesrun`.validate`rules after verifying that a`.write`rule grants access.

|                                                         Rule Types                                                          ||
|---------------|--------------------------------------------------------------------------------------------------------------|
| **.read**     | Describes if and when data is allowed to be read by users.                                                   |
| **.write**    | Describes if and when data is allowed to be written.                                                         |
| **.validate** | Defines what a correctly formatted value will look like, whether it has child attributes, and the data type. |

By default, if there isn't a rule allowing it, access at a path is denied.

<br />

<br />

## Building conditions

<br />

### Cloud Firestore

<br />

A condition is a boolean expression that determines whether a particular operation should be allowed or denied. The`request`and`resource`variables provide context for those conditions.

### The`request`variable

The`request`variable includes the following fields and corresponding information:

#### `request.auth`

A JSON Web Token (JWT) that contains authentication credentials fromFirebase Authentication.`auth`token contains a set of standard claims and any custom claims you create throughFirebase Authentication. Learn more about[Firebase Security RulesandAuthentication](https://firebase.google.com/docs/rules/rules-and-auth).

#### `request.method`

The`request.method`may be any of the standard methods or a custom method. The convenience methods`read`and`write`also exist to simplify writing rules that apply to all read-only or all write-only standard methods respectively.

#### `request.params`

The`request.params`include any data not specifically related to the`request.resource`that might be useful for evaluation. In practice, this map should be empty for all standard methods, and should contain non-resource data for custom methods. Services must be careful not to rename or modify the type of any of the keys and values presented as params.

#### `request.path`

The`request.path`is the path for the target`resource`. The path is relative to the service. Path segments containing non-url safe characters such as`/`are url-encoded.

### The`resource`variable

The`resource`is the current value within the service represented as a map of key-value pairs. Referencing`resource`within a condition will result in at most one read of the value from the service. This lookup will count against any service-related quota for the resource. For`get`requests, the`resource`will only count toward quota on deny.

### Operators and operator precedence

Use the table below as a reference for operators and their corresponding precedence inRulesforCloud FirestoreandCloud Storage.

Given arbitrary expressions`a`and`b`, a field`f`, and an index`i`.

|            Operator            |                                                     Description                                                     | Associativity |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------|---------------|
| `a[i] a() a.f`                 | Index, call, field access                                                                                           | left to right |
| `!a -a`                        | Unary negation                                                                                                      | right to left |
| `a/b a%b a*b`                  | Multiplicative operators                                                                                            | left to right |
| `a+b a-b`                      | Additive operators                                                                                                  | left to right |
| `a>b a>=b a`                   | Relational operators                                                                                                | left to right |
| `a in b`                       | Existence in list or map                                                                                            | left to right |
| `a is type`                    | Type comparison, where`type`can be bool, int, float, number, string, list, map, timestamp, duration, path or latlng | left to right |
| `a==b a!=b`                    | Comparison operators                                                                                                | left to right |
| `a && b`                       | Conditional AND                                                                                                     | left to right |
| `a || b`                       | Conditional OR                                                                                                      | left to right |
| `a ? true_value : false_value` | Ternary expression                                                                                                  | left to right |

<br />

### Cloud Storage

<br />

A condition is a boolean expression that determines whether a particular operation should be allowed or denied. The`request`and`resource`variables provide context for those conditions.

### The`request`variable

The`request`variable includes the following fields and corresponding information:

#### `request.auth`

A JSON Web Token (JWT) that contains authentication credentials fromFirebase Authentication.`auth`token contains a set of standard claims and any custom claims you create throughFirebase Authentication. Learn more about[Firebase Security RulesandAuthentication](https://firebase.google.com/docs/rules/rules-and-auth).

#### `request.method`

The`request.method`may be any of the standard methods or a custom method. The convenience methods`read`and`write`also exist to simplify writing rules that apply to all read-only or all write-only standard methods respectively.

#### `request.params`

The`request.params`include any data not specifically related to the`request.resource`that might be useful for evaluation. In practice, this map should be empty for all standard methods, and should contain non-resource data for custom methods. Services must be careful not to rename or modify the type of any of the keys and values presented as params.

#### `request.path`

The`request.path`is the path for the target`resource`. The path is relative to the service. Path segments containing non-url safe characters such as`/`are url-encoded.

### The`resource`variable

The`resource`is the current value within the service represented as a map of key-value pairs. Referencing`resource`within a condition will result in at most one read of the value from the service. This lookup will count against any service-related quota for the resource. For`get`requests, the`resource`will only count toward quota on deny.

### Operators and operator precedence

Use the table below as a reference for operators and their corresponding precedence inRulesforCloud FirestoreandCloud Storage.

Given arbitrary expressions`a`and`b`, a field`f`, and an index`i`.

|            Operator            |                                                     Description                                                     | Associativity |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------|---------------|
| `a[i] a() a.f`                 | Index, call, field access                                                                                           | left to right |
| `!a -a`                        | Unary negation                                                                                                      | right to left |
| `a/b a%b a*b`                  | Multiplicative operators                                                                                            | left to right |
| `a+b a-b`                      | Additive operators                                                                                                  | left to right |
| `a>b a>=b a`                   | Relational operators                                                                                                | left to right |
| `a in b`                       | Existence in list or map                                                                                            | left to right |
| `a is type`                    | Type comparison, where`type`can be bool, int, float, number, string, list, map, timestamp, duration, path or latlng | left to right |
| `a==b a!=b`                    | Comparison operators                                                                                                | left to right |
| `a && b`                       | Conditional AND                                                                                                     | left to right |
| `a || b`                       | Conditional OR                                                                                                      | left to right |
| `a ? true_value : false_value` | Ternary expression                                                                                                  | left to right |

<br />

### Realtime Database

<br />

A condition is a boolean expression that determines whether a particular operation should be allowed or denied. You can define those conditions inRealtime DatabaseRulesin the following ways.

### Pre-defined variables

There are a number of helpful, pre-defined variables that can be accessed inside a rule definition. Here is a brief summary of each:

|                                                                                                                                                         Predefined Variables                                                                                                                                                          ||
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **[now](https://firebase.google.com/docs/reference/security/database#variables)**         | The current time in milliseconds since Linux epoch. This works particularly well for validating timestamps created with the SDK's firebase.database.ServerValue.TIMESTAMP.                                                                 |
| **[root](https://firebase.google.com/docs/reference/security/database#variables)**        | A[RuleDataSnapshot](https://firebase.google.com/docs/reference/security/database#ruledatasnapshot_methods)representing the root path in the Firebase database as it exists before the attempted operation.                                 |
| **[newData](https://firebase.google.com/docs/reference/security/database#variables)**     | A[RuleDataSnapshot](https://firebase.google.com/docs/reference/security/database#ruledatasnapshot_methods)representing the data as it would exist after the attempted operation. It includes the new data being written and existing data. |
| **[data](https://firebase.google.com/docs/reference/security/database#variables)**        | A[RuleDataSnapshot](https://firebase.google.com/docs/reference/security/database#ruledatasnapshot_methods)representing the data as it existed before the attempted operation.                                                              |
| **[$ variables](https://firebase.google.com/docs/reference/security/database#variables)** | A wildcard path used to represent ids and dynamic child keys.                                                                                                                                                                              |
| **[auth](https://firebase.google.com/docs/reference/security/database#variables)**        | Represents an authenticated user's token payload.                                                                                                                                                                                          |

These variables can be used anywhere in your rules. For example, the security rules below ensure that data written to the`/foo/`node must be a string less than 100 characters:  

```text
{
  "rules": {
    "foo": {
      // /foo is readable by the world
      ".read": true,

      // /foo is writable by the world
      ".write": true,

      // data written to /foo must be a string less than 100 characters
      ".validate": "newData.isString() && newData.val().length < 100"
    }
  }
}
```

### Data-based rules

Any data in your database can be used in your rules. Using the predefined variables`root`,`data`, and`newData`, you can access any path as it would exist before or after a write event.

Consider this example, which allows write operations as long as the value of the`/allow_writes/`node is`true`, the parent node does not have a`readOnly`flag set, and there is a child named`foo`in the newly written data:  

```scdoc
".write": "root.child('allow_writes').val() === true &&
          !data.parent().child('readOnly').exists() &&
          newData.child('foo').exists()"
```

### Query-based rules

Although you can't use rules as filters, you can limit access to subsets of data by using query parameters in your rules. Use`query.`expressions in your rules to grant read or write access based on query parameters.

For example, the following query-based rule uses[user-based security rules](https://firebase.google.com/docs/rules/rules-and-auth)and query-based rules to restrict access to data in the`baskets`collection to only the shopping baskets the active user owns:  

    "baskets": {
      ".read": "auth.uid !== null &&
                query.orderByChild === 'owner' &&
                query.equalTo === auth.uid" // restrict basket access to owner of basket
    }

The following query, which includes the query parameters in the rule, would succeed:  

    db.ref("baskets").orderByChild("owner")
                     .equalTo(auth.currentUser.uid)
                     .on("value", cb)                 // Would succeed

However, queries that do not include the parameters in the rule would fail with a`PermissionDenied`error:  

    db.ref("baskets").on("value", cb)                 // Would fail with PermissionDenied

You can also use query-based rules to limit how much data a client downloads through read operations.

For example, the following rule limits read access to only the first 1000 results of a query, as ordered by priority:  

    messages: {
      ".read": "query.orderByKey &&
                query.limitToFirst <= 1000"
    }

    // Example queries:

    db.ref("messages").on("value", cb)                // Would fail with PermissionDenied

    db.ref("messages").limitToFirst(1000)
                      .on("value", cb)                // Would succeed (default order by key)

The following`query.`expressions are available inRealtime DatabaseSecurity Rules.

|                                                                                                                        Query-based rule expressions                                                                                                                         |||
|---------------------------------------------------------------|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Expression**                                                | **Type**                   | **Description**                                                                                                                                                                  |
| **query.orderByKey query.orderByPriority query.orderByValue** | boolean                    | True for queries ordered by key, priority, or value. False otherwise.                                                                                                            |
| **query.orderByChild**                                        | string null                | Use a string to represent the relative path to a child node. For example,`query.orderByChild === "address/zip"`. If the query isn't ordered by a child node, this value is null. |
| **query.startAt query.endAt query.equalTo**                   | string number boolean null | Retrieves the bounds of the executing query, or returns null if there is no bound set.                                                                                           |
| **query.limitToFirst query.limitToLast**                      | number null                | Retrieves the limit on the executing query, or returns null if there is no limit set.                                                                                            |

### Operators

Realtime DatabaseRulessupport a number of[operators](https://firebase.google.com/docs/reference/security/database#operators)you can use to combine variables in the condition statement. See the full list of[operators in the reference documentation](https://firebase.google.com/docs/reference/security/database#operators).

<br />

<br />

### Creating conditions

Your actual conditions will vary based on the access you want to grant.Rulesintentionally offer an enormous degree of flexibility, so your app's rules can ultimately be as simple or as complex as you need them to be.

For some guidance creating simple, production-readyRules, see[Basic Security Rules](https://firebase.google.com/docs/rules/basics).