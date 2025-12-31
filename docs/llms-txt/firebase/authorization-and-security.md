# Source: https://firebase.google.com/docs/data-connect/authorization-and-security.md.txt

<br />

Firebase Data Connectprovides robust client-side security with:

- Mobile and web client authorization
- Individual query- and mutation-level authorization controls
- App attestation withFirebase App Check.

Data Connectextends this security with:

- Server-side authorization
- Firebase project and Cloud SQL user security with IAM.

## Authorize client queries and mutations

Data Connectis fully integrated withFirebase Authentication, so you can use rich data about users who are accessing your data (authentication) in your design for what data those users can access (authorization).

Data Connectprovides an`@auth`directive for queries and mutations that lets you set the level of authentication required to authorize the operation. This guide[introduces the`@auth`directive, with examples](https://firebase.google.com/docs/data-connect/authorization-and-security#auth-directive).

In addition,Data Connectsupports execution of queries embedded in mutations, so you can retrieve additional authorization criteria you've stored in your database, and use those criteria in`@check`directives to decide if enclosing mutations are authorized. For this authorization case, the`@redact`directive allows you control whether query results are returned to clients in the wire protocol and the embedded query omitted in generated SDKs. Find the[introduction to these directives, with examples](https://firebase.google.com/docs/data-connect/authorization-and-security#check-redact-directives).

### Understand the`@auth`directive

You can parameterize the`@auth`directive to follow one of several preset access levels that cover many common access scenarios. These levels range from`PUBLIC`(which allows queries and mutations from all clients without authentication of any kind) to`NO_ACCESS`(which disallows queries and mutations outside of[privileged server environments using the Firebase Admin SDK](https://firebase.google.com/docs/data-connect/admin-sdk)). Each of these levels is correlated with authentication flows provided byFirebase Authentication.

|         Level         |                                                                    Definition                                                                    |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `PUBLIC`              | The operation can be executed by anyone with or without authentication.                                                                          |
| `PUBLIC`              | The operation can be executed by anyone with or without authentication.                                                                          |
| `USER_ANON`           | Any identified user, including those who have logged in anonymously withFirebase Authentication, is authorized to perform the query or mutation. |
| `USER`                | Any user who has logged in withFirebase Authenticationis authorized to perform the query or mutation except anonymous sign-in users.             |
| `USER_EMAIL_VERIFIED` | Any user who has logged in withFirebase Authenticationwith a verified email address is authorized to perform the query or mutation.              |
| `NO_ACCESS`           | This operation cannot be executed outside an Admin SDK context.                                                                                  |

Using these preset access levels as a starting point, you can define complex and robust authorization checks in the`@auth`directive using`where`filters and Common Expression Language (CEL) expressions evaluated on the server.
| **Note:** All queries and mutations in your connector must have an`@auth`directive to be accessible by client applications. Queries and mutations default to`NO_ACCESS`if the`@auth`directive is not specified.
| **Tip:** See the[directives reference for the`@auth`directive](https://firebase.google.com/docs/reference/data-connect/gql/directive#auth)and the[complete reference for access levels](https://firebase.google.com/docs/data-connect/authorization-and-security#preset-authz-levels).

### Use the`@auth`directive to implement common authorization scenarios

The preset access levels are the*starting point*for authorization.

The`USER`access level is the most widely useful basic level to start with.

Fully secure access will build on the`USER`level plus filters and expressions that check user attributes, resource attributes, roles and other checks. The`USER_ANON`and`USER_EMAIL_VERIFIED`levels are variations on the`USER`case.

Expression syntax lets you evaluate data using an`auth`object representing authentication data passed with operations, both standard data in auth tokens and custom data in tokens. For the list of fields available in the`auth`object, see the[reference section](https://firebase.google.com/docs/data-connect/authorization-and-security#auth-cel-reference).
| **Note:** You can augment authorization with`@auth`by looking up authorization roles and other data stored in your database, as described in the[section on adding`@check`and`@redact`for lookups](https://firebase.google.com/docs/data-connect/authorization-and-security#check-redact-directives).

There are of course use cases where`PUBLIC`is the correct access level to start with. Again, an access level is always a starting point, and additional filters and expressions are needed for robust security.

This guide now gives examples of how to build on`USER`and`PUBLIC`.

#### A motivating example

The following best practice examples refer to the following schema for a blogging platform with certain content locked behind a payment plan.

Such a platform would likely model`Users`and`Posts`.  

    type User @table(key: "uid") {
      uid: String!
      name: String
      birthday: Date
      createdAt: Timestamp! @default(expr: "request.time")
    }

    type Post @table {
      author: User!
      text: String!
      # "one of 'draft', 'public', or 'pro'"
      visibility: String! @default(value: "draft")
      # "the time at which the post should be considered published. defaults to
      # immediately"
      publishedAt: Timestamp! @default(expr: "request.time")
      createdAt: Timestamp! @default(expr: "request.time")
      updatedAt: Timestamp! @default(expr: "request.time")
    }

#### User-owned resources

Firebase recommends that you write filters and expressions that test user ownership of a resource, in the following cases, ownership of`Posts`.

In the following examples, data from auth tokens is read and compared using expressions. The typical pattern is to use expressions like`where: {authorUid:
{eq_expr: "auth.uid"}}`to compare a stored`authorUid`to the`auth.uid`(user ID) passed in the authentication token.

##### Create

This authorization practice starts by adding the`auth.uid`from the auth token to each new`Post`as an`authorUid`field to allow comparison in subsequence authorization tests.  

    # Create a new post as the current user
    mutation CreatePost($text: String!, $visibility: String) @auth(level: USER) {
      post_insert(data: {
        # set the author's uid to the current user uid
        authorUid_expr: "auth.uid"
        text: $text
        visibility: $visibility
      })
    }

##### Update

When a client attempts to update a`Post`, you can test the passed`auth.uid`against the stored`authorUid`.  

    # Update one of the current user's posts
    mutation UpdatePost($id: UUID!, $text: String, $visibility: String) @auth(level:USER) {
      post_update(
        # only update posts whose author is the current user
        first: { where: {
          id: {eq: $id}
          authorUid: {eq_expr: "auth.uid"}
        }}
        data: {
          text: $text
          visibility: $visibility
          # insert the current server time for updatedAt
          updatedAt_expr: "request.time"
        }
      )
    }

##### Delete

The same technique is used to authorize delete operations.  

    # Delete one of the current user's posts
    mutation DeletePost($id: UUID!) @auth(level: USER) {
      post_delete(
        # only delete posts whose author is the current user
        first: { where: {
          id: {eq: $id}
          authorUid: {eq_expr: "auth.uid"}
        }}
      )
    }

**Note:** For these query examples, the following fragment is used to select common fields on`Post`.  

    # Common display information for a post
    fragment DisplayPost on Post {
      id, text, createdAt, updatedAt
      author { uid, name }
    }

##### List

    # List all posts belonging to the current user
    query ListMyPosts @auth(level: USER) {
      posts(where: {
        userUid: {eq_expr: "auth.uid"}
      }) {
        # See the fragment above
        ...DisplayPost
        # also show visibility since it is user-controlled
        visibility
      }
    }

##### Get

    # Get a post only if it belongs to the current user
    query GetMyPost($id: UUID!) @auth(level: USER) {
      post(key: {id: $id},
        first: {where: {
          id: {eq: $id}
          authorUid: {eq_expr: "auth.uid"}}
          }}, {
          # See the fragment above
          ...DisplayPost
          # also show visibility since it is user-controlled
          visibility
      }
    }

#### Filter Data

Data Connect's authorization system lets you write sophisticated filters combined with preset access levels like`PUBLIC`as well as by using data from auth tokens.

The authorization system also lets you use expressions only, without a base access level, as shown in some of the following examples.

##### Filter by resource attributes

Here, authorization is not based on auth tokens since the base security level is set to`PUBLIC`. But, we can explicitly set records in our database as suitable for public access; assume we have`Post`records in our database with`visibility`set to "public".  

    # List all posts marked as 'public' visibility
    query ListPublicPosts @auth(level: PUBLIC) {
      posts(where: {
        # Test that visibility is "public"
        visibility: {eq: "public"}
        # Only display articles that are already published
        publishedAt: {lt_expr: "request.time"}
      }) {
        # see the fragment above
        ...DisplayPost
      }
    }

##### Filter by user claims

Here, assume you've set up custom user claims that pass in auth tokens to identify users in a "pro" plan for your app, flagged with an`auth.token.plan`field in the auth token. Your expressions can test against this field.  

    # List all public or pro posts, only permitted if user has "pro" plan claim
    query ProListPosts @auth(expr: "auth.token.plan == 'pro'") {
      posts(where: {
        # display both public posts and "pro" posts
        visibility: {in: ['public', 'pro']},
        # only display articles that are already published
        publishedAt: {lt_expr: "request.time"},
      }) {
        # see the fragment above
        ...DisplayPost
        # show visibility so pro users can see which posts are pro\
        visibility
      }
    }

##### Filter by order + limit

Or again, you may have set`visibility`in`Post`records to identify they are content available for "pro" users, but for a preview or teaser listing of data, further limit the number of records returned.  

    # Show 2 oldest Pro post as a preview
    query ProTeaser @auth(level: USER) {
      posts(
        where: {
          # show only pro posts
          visibility: {eq: "pro"}
          # that have already been published more than 30 days ago
          publishedAt: {lt_time: {now: true, sub: {days: 30}}}
        },
        # order by publish time
        orderBy: [{publishedAt: DESC}],
        # only return two posts
        limit: 2
      ) {
        # See the fragment above
        ...DisplayPost
      }
    }

##### Filter by role

If your custom claim defines an`admin`role, you can test and authorize operations accordingly.  

    # List all posts unconditionally iff the current user has an admin claim
    query AdminListPosts @auth(expr: "auth.token.admin == true") {
      posts { ...DisplayPost }
    }

### Add the`@check`and`@redact`directives to look up authorization data

A common authorization use case involves storing custom authorization roles in your database, for example in a special permissions table, and using those roles to authorize mutations to create, update, or delete data.

Using authorization data lookups, you can query for roles based on a userID and use CEL expressions to decide if the mutation is authorized. For example, you might want to write an`UpdateMovieTitle`mutation that lets an authorized client update movie titles.

For the rest of this discussion, assume the movie review app database stores an authorization role in a`MoviePermission`table.  

    # MoviePermission
    # Suppose a user has an authorization role with respect to records in the Movie table
    type MoviePermission @table(key: ["movie", "user"]) {
      movie: Movie! # implies another field: movieId: UUID!
      user: User!
      role: String!
    }

#### Use in mutations

In the following example implementation, the`UpdateMovieTitle`mutation includes a`query`field to retrieve data from`MoviePermission`, and the following directives to ensure the operation is secure and robust:

- A`@transaction`directive to ensure all authorization queries and checks are completed or fail atomically.
- The`@redact`directive to omit query results from the response, meaning our authorization check is performed on theData Connectserver but sensitive data is not exposed to the client.
- A pair of`@check`directives to evaluate authorization logic on query results, such as testing that a given userID has an appropriate role to make modifications.

  | **Note:** The`message`argument for`@check`is optional, but it's useful in combination with the`@redact`directive, so you can define messages to return to client code even though specific fields are redacted from the response.

    mutation UpdateMovieTitle($movieId: UUID!, $newTitle: String!) @auth(level: USER) @transaction {
      # Step 1: Query and check
      query @redact {
        moviePermission( # Look up a join table called MoviePermission with a compound key.
          key: {movieId: $movieId, userId_expr: "auth.uid"}
        # Step 1a: Use @check to test if the user has any role associated with the movie
        # Here the `this` binding refers the lookup result, i.e. a MoviePermission object or null
        # The `this != null` expression could be omitted since rejecting on null is default behavior
        ) @check(expr: "this != null", message: "You do not have access to this movie") {
          # Step 1b: Check if the user has the editor role for the movie
          # Next we execute another @check; now `this` refers to the contents of the `role` field
          role @check(expr: "this == 'editor'", message: "You must be an editor of this movie to update title")
        }
      }
      # Step 2: Act
      movie_update(id: $movieId, data: {
        title: $newTitle
      })
    }

| **Tip:** Refer to the[directives reference guide](https://firebase.google.com/docs/reference/data-connect/gql/directive)and[CEL reference for the`this`binding](https://firebase.google.com/docs/data-connect/authorization-and-security#cel-this-binding).

#### Use in queries

Authorization data lookups are also useful to restrict queries based on roles or other restrictions.

In the following example, which also uses the`MoviePermission`schema, the query checks whether a requestor has an appropriate "admin" role to view users who can edit a movie.  

    query GetMovieEditors($movieId: UUID!) @auth(level: PUBLIC) {
      moviePermission(key: { movieId: $movieId, userId_expr: "auth.uid" }) @redact {
        role @check(expr: "this == 'admin'", message: "You must be an admin to view all editors of a movie.")
      }
      moviePermissions(where: { movieId: { eq: $movieId }, role: { eq: "editor" } }) {
        user {
          id
          username
        }
      }
    }

| **Tip:** Refer to the[directives reference guide](https://firebase.google.com/docs/reference/data-connect/gql/directive)and[CEL reference for the`this`binding](https://firebase.google.com/docs/data-connect/authorization-and-security#cel-this-binding).

### Antipatterns to avoid in authorization

The previous section covers patterns to follow when using the`@auth`directive.

You should also be aware of important antipatterns to avoid.

Avoid passing user attributes IDs and auth token parameters in query and mutation arguments

Firebase Authenticationis a powerful tool for presenting authentication flows and securely capturing authentication data such as registered user IDs and numerous fields stored in auth tokens.

It's not a recommended practice to pass user IDs and auth token data in query and mutation arguments.
**Tip:** Instead, in the filters and expressions you use to augment basic access levels, test against`auth.uid`and the fields in`auth.token`to enhance security. For more information about`auth`data, see the[expression reference](https://firebase.google.com/docs/data-connect/authorization-and-security#auth-cel-reference).  

    # Antipattern!
    # This incorrectly allows any user to view any other user's posts
    query AllMyPosts($userId: String!) @auth(level: USER) {
      posts(where: {authorUid: {eq: $userId}}) {
        id, text, createdAt
      }
    }

Avoid using the`USER`access level without any filters

As discussed several times in the guide, the core access levels like`USER`,`USER_ANON`,`USER_EMAIL_VERIFIED`are baselines and starting points for authorization checks, to be enhanced with filters and expressions. Using these levels without a corresponding filter or expression that checks*which* user is performing the request is essentially equivalent to using the`PUBLIC`level.
**Tip:** Firebase recommends that you*always*augment basic access levels with expressions.  

    # Antipattern!
    # This incorrectly allows any user to view all documents
    query ListDocuments @auth(level: USER) {
      documents {
        id
        title
        text
      }
    }

Avoid using`PUBLIC`or`USER`access level for prototyping

To speed up development, it can be tempting to set all operations to the`PUBLIC`access level or to`USER`access level without further enhancements to authorize all operations and let you quickly test your code.
| **Tip:** Before you deploy your operations to production, when you prototype in the console and with the tooling in theData ConnectVS Code extension, set your queries and mutations to the`NO_ACCESS`access level. You'll be able to execute these operations in the safe console and VS Code prototyping environments before they are deployed. Following this practice means that even if you deploy such operations to production, they cannot be executed.

When you've done very initial prototyping this way, begin to switch from`NO_ACCESS`to production-ready authorization with`PUBLIC`and`USER`levels. However, don't deploy them as`PUBLIC`or`USER`without adding additional logic as shown in this guide.  

    # Antipattern!
    # This incorrectly allows anyone to delete any post
    mutation DeletePost($id: UUID!) @auth(level: PUBLIC) {
      post: post_delete(
        id: $id,
      )
    }

Avoid basing authorization on unverified email addresses

Granting access to users on a particular domain is a great way to limit access. However, anyone can claim to own an email during sign-in. Ensure you only grant access to email addresses that have been verified through Firebase Authentication.  

    # Antipattern!
    # Anyone can claim an email address during sign-in
    mutation CreatePost($text: String!, $visibility: String) @auth(expr: "auth.token.email.endsWith('@example.com')") {
      post_insert(data: {
        # set the author's uid to the current user uid
        authorUid_expr: "auth.uid"
        text: $text
        visibility: $visibility
      })
    }

Also check`auth.token.email_verified`  

    mutation CreatePost($text: String!, $visibility: String) @auth(expr: "auth.token.email_verified && auth.token.email.endsWith('@example.com')") {
      post_insert(data: {
        # set the author's uid to the current user uid
        authorUid_expr: "auth.uid"
        text: $text
        visibility: $visibility
      })
    }

### Audit authorization with the Firebase CLI

As indicated earlier, preset access levels such as`PUBLIC`and`USER`are the starting point for robust authorization, and should be used with additional filter and expression-based authorization checks. They shouldn't be used on their own without careful consideration of the use case.

Data Connecthelps you audit your authorization strategy by analyzing your connector code when you deploy to the server using`firebase deploy`from theFirebaseCLI. You can use this audit to help you review your codebase.

When you deploy your connectors, the CLI will output assessments for existing, modified and new operation code in your connector.

For modified and new operations, the CLI issues warnings and prompts you for confirmation when you use certain access levels in your new operations, or when you modify existing operations to use those access levels.
| **Note:** Insecure operation warnings are suppressed if you annotate the`@auth`directive in the operation with the[`insecureReason`argument](https://firebase.google.com/docs/data-connect/authorization-and-security#insecureReasons).

Warnings and prompts always occur for:

- `PUBLIC`

And, warnings and prompts occur on the following access levels when you*don't augment them* with filters using`auth.uid`:

- `USER`
- `USER_ANON`
- `USER_EMAIL_VERIFIED`

#### Suppress insecure operation warnings with the`@auth(insecureReason:)`argument

In many cases, you will conclude that using the`PUBLIC`and`USER*`access levels is perfectly appropriate.

When your connector contains many operations, you may want clearer, more relevant security audit output that omits operations that would normally trigger a warning, but you know have the correct access level.

You can suppress warnings for such operations with`@auth(insecureReason:)`. For example:  

    query listItem @auth(level: PUBLIC, insecureReason: "This operation is safe to expose to the public.")
      {
        items {
          id name
        }
      }

## UseFirebase App Checkfor app attestation

Authentication and authorization are critical components ofData Connectsecurity. Authentication and authorization combined with app attestation makes for a very robust security solution.

With attestation throughFirebase App Check, devices running your app will use an app or device attestation provider that attests thatData Connectoperations originate from your authentic app and requests originate from an authentic, untampered device. This attestation is attached to every request your app makes toData Connect.

To learn how to enableApp CheckforData Connectand include its client SDK in your app, have a[look at theApp Checkoverview](https://firebase.google.com/docs/app-check).

## Authentication levels for the`@auth(level)`directive

The following table lists all standard access levels and their CEL equivalents. Authentication levels are listed from broad to narrow -- each level encompasses all users who match following levels.
| **Warning:** These access levels are only the starting point for security, upon which you implement additional filter and expression-based authorization checks like those[discussed above](https://firebase.google.com/docs/data-connect/authorization-and-security#auth-best-practices).

|         Level         |                                                                                                                                                                                                                                                                                                                                                                                                     Definition                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PUBLIC`              | The operation can be executed by anyone with or without authentication. **Considerations:** Data can be read or modified by any user. Firebase recommends this level of authorization for publicly-browsable data like product or media listings. See the[best practice examples and alternatives](https://firebase.google.com/docs/data-connect/authorization-and-security#auth-best-practices). Equivalent to`@auth(expr: "true")` `@auth`filters and expressions cannot be used in combination with this access level. Any such expressions will fail with a 400 bad request error.                                                                                                                                                                                                                             |
| `USER_ANON`           | Any identified user, including those who have logged in anonymously withFirebase Authentication, is authorized to perform the query or mutation. Note:`USER_ANON`is a superset of`USER`. **Considerations:** Note that you must carefully design your queries and mutations for this level of authorization. This level allows user to be logged in**anonymously** (automatic sign-in tied only to a user device) withAuthentication, and does not on its own perform other checks on, for example, whether data belongs to the user. See the[best practice examples and alternatives](https://firebase.google.com/docs/data-connect/authorization-and-security#auth-best-practices). SinceAuthenticationanonymous login flows issue a`uid`, the`USER_ANON`level is equivalent to `@auth(expr: "auth.uid != nil")` |
| `USER`                | Any user who has logged in withFirebase Authenticationis authorized to perform the query or mutation except anonymous sign-in users. **Considerations:** Note that you must carefully design your queries and mutations for this level of authorization. This level only checks that the user is logged in withAuthentication, and does not on its own perform other checks on, for example, whether data belongs to the user. See the[best practice examples and alternatives](https://firebase.google.com/docs/data-connect/authorization-and-security#auth-best-practices). Equivalent to`@auth(expr: "auth.uid != nil && auth.token.firebase.sign_in_provider != 'anonymous'")"`                                                                                                                               |
| `USER_EMAIL_VERIFIED` | Any user who has logged in withFirebase Authenticationwith a verified email address is authorized to perform the query or mutation. **Considerations:** Since email verification is performed usingAuthentication, it's based on a more robustAuthenticationmethod, thus this level provides additional security compared to`USER`or`USER_ANON`. This level only checks that the user is logged in withAuthenticationwith a verified email, and does not on its own perform other checks on, for example, whether data belongs to the user. See the[best practice examples and alternatives](https://firebase.google.com/docs/data-connect/authorization-and-security#auth-best-practices). Equivalent to`@auth(expr: "auth.uid != nil && auth.token.email_verified")"`                                            |
| `NO_ACCESS`           | This operation cannot be executed outside an Admin SDK context. Equivalent to`@auth(expr: "false")`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## CEL Reference for`@auth(expr)`

As shown in examples elsewhere in this guide, you can and should use expressions defined in Common Expression Language (CEL) to control authorization forData Connectusing`@auth(expr:)`and`@check`directives.

This section covers CEL syntax relevant to creating expressions for these directives.

Complete reference information for CEL is provided in the[CEL specification](https://github.com/google/cel-spec).

### Test variables passed in queries and mutations

`@auth(expr)`syntax allows you access and test variables from queries and mutations.

For example, you can include an operation variable, such as`$status`, using`vars.status`.  

    mutation Update($id: UUID!, $status: Any) @auth(expr: "has(vars.status)")

### Data available to expressions: request, response, this

You use data for:

- Evaluation with CEL expressions in`@auth(expr:)`and`@check(expr:)`directives
- Assignment using server expressions,`<field>_expr`.

Both`@auth(expr:)`and`@check(expr:)`CEL expressions can evaluate the following:

- `request.operationName`
- `vars`(alias for`request.variables`)
- `auth`(alias for`request.auth`)

In mutations, you can access and assign the contents of:

- `response`(to check partial results in multi-step logic)

Additionally,`@check(expr:)`expressions can evaluate:

- `this`(the value of the current field)
- `response`(to check partial results in multi-step logic)

#### The request.operationName binding

The`request.operarationName`binding stores the type of operation, either query or mutation.

#### The`vars`binding (request.vars)

The`vars`binding allows your expressions to access all variables passed in your query or mutation.

You can use`vars.<variablename>`in an expression as an alias for the fully-qualified`request.variables.<variablename>`:  

    # The following are equivalent
    mutation StringType($v: String!) @auth(expr: "vars.v == 'hello'")
    mutation StringType($v: String!) @auth(expr: "request.variables.v == 'hello'")

#### The`auth`binding (request.auth)

Authenticationidentifies users requesting access to your data and provides that information as a binding you can build on in your expressions.

In your filters and expressions, you can use`auth`as an alias for`request.auth`.

The auth binding contains the following information:

- `uid`: A unique user ID, assigned to the requesting user.
- `token`: A map of values collected byAuthentication.

For more details on the contents of`auth.token`see[Data in auth tokens](https://firebase.google.com/docs/data-connect/authorization-and-security#auth-token-contents)

#### The`response`binding

The`response`binding contains the data being assembled by the server in response to a query or mutation*as that data is being assembled*.

As the operation proceeds, as each step is completed successfully,`response`contains response data from successfully-completed steps.

The`response`binding is structured according the shape of its associated operation, including (multiple) nested fields and (if applicable) embedded queries.

Note that when you access**embedded query response data** , fields can contain any data type, depending on the data requested in the embedded query; when you access data returned by mutation fields like`_insert`s and`_delete`s, they may contain UUID keys, number of deletes, nulls (see the[mutations reference](https://firebase.google.com/docs/reference/data-connect/gql/mutation)).

For example:

- In a mutation that contains an embedded query, the`response`binding contains lookup data at`response.query.<fieldName>.<fieldName>....`, in this case,`response.query.todoList`and`response.query.todoList.priority`.

    mutation CheckTodoPriority(
      $uniqueListName: String!
    ) {
      # This query is identified as `response.query`
      query @check(expr: "response.query.todoList.priority == 'high'", message: "This list is not for high priority items!") {
        # This field is identified as `response.query.todoList`
        todoList(where: { name: $uniqueListName }) {
          # This field is identified as `response.query.todoList.priority`
          priority
        }
      }
    }

- In a multi-step mutation, for example with multiple`_insert`fields, the`response`binding contains partial data at`response.<fieldName>.<fieldName>....`, in this case,`response.todoList_insert.id`.

    mutation CreateTodoListWithFirstItem(
      $listName: String!,
      $itemContent: String!
    ) @transaction {
      # Step 1
      todoList_insert(data: {
        id_expr: "uuidV4()",
        name: $listName,
      })
      # Step 2:
      todo_insert(data: {
        listId_expr: "response.todoList_insert.id" # <-- Grab the newly generated ID from the partial response so far.
        content: $itemContent,
      })
    }

#### The`this`binding

| **Note:** The`this`binding is valid for`@check`expressions, not`@auth`expressions.

The binding`this`evaluates to the field that the`@check`directive is attached to. In a basic case, you might evaluate single-valued query results.  

    mutation UpdateMovieTitle (
      $movieId: UUID!,
      $newTitle: String!)
      @auth(level: USER)
      @transaction {
      # Step 1: Query and check
      query @redact {
        moviePermission( # Look up a join table called MoviePermission with a compound key.
          key: {movieId: $movieId, userId_expr: "auth.uid"}
        ) {
          # Check if the user has the editor role for the movie. `this` is the string value of `role`.
          # If the parent moviePermission is null, the @check will also fail automatically.
          role @check(expr: "this == 'editor'", message: "You must be an editor of this movie to update title")
        }
      }
      # Step 2: Act
      movie_update(id: $movieId, data: {
        title: $newTitle
      })
    }

If the returned field occurs multiple times because any ancestor is a list, each occurrence is tested with`this`bound to each value.

For any given path, if an ancestor is`null`or`[]`, the field won't be reached and the CEL evaluation will be skipped for that path. In other words, evaluation only takes place when`this`is`null`or non-`null`, but never`undefined`.

When the field itself is a list or object,`this`follows the same structure (including all descendants selected in case of objects), as illustrated in the following example.  

    mutation UpdateMovieTitle2($movieId: UUID!, $newTitle: String!) @auth(level: USER) @transaction {
      # Step 1: Query and check
      query {
        moviePermissions( # Now we query for a list of all matching MoviePermissions.
          where: {movieId: {eq: $movieId}, userId: {eq_expr: "auth.uid"}}
        # This time we execute the @check on the list, so `this` is the list of objects.
        # We can use the `.exists` macro to check if there is at least one matching entry.
        ) @check(expr: "this.exists(p, p.role == 'editor')", message: "You must be an editor of this movie to update title") {
          role
        }
      }
      # Step 2: Act
      movie_update(id: $movieId, data: {
        title: $newTitle
      })
    }

### Complex expression syntax

You can write more complex expressions by combining with the`&&`and`||`operators.  

    mutation UpsertUser($username: String!) @auth(expr: "(auth != null) && (vars.username == 'joe')")

The following section describes all available operators.

### Operators and operator precedence

Use the following table as a reference for operators and their corresponding precedence.

Given arbitrary expressions`a`and`b`, a field`f`, and an index`i`.

|            Operator            |                                             Description                                             | Associativity |
|--------------------------------|-----------------------------------------------------------------------------------------------------|---------------|
| `a[i] a() a.f`                 | Index, call, field access                                                                           | left to right |
| `!a -a`                        | Unary negation                                                                                      | right to left |
| `a/b a%b a*b`                  | Multiplicative operators                                                                            | left to right |
| `a+b a-b`                      | Additive operators                                                                                  | left to right |
| `a>b a>=b a<b a<=b`            | Relational operators                                                                                | left to right |
| `a in b`                       | Existence in list or map                                                                            | left to right |
| `type(a) == t`                 | Type comparison, where`t`can be bool, int, float, number, string, list, map, timestamp, or duration | left to right |
| `a==b a!=b`                    | Comparison operators                                                                                | left to right |
| `a && b`                       | Conditional AND                                                                                     | left to right |
| `a || b`                       | Conditional OR                                                                                      | left to right |
| `a ? true_value : false_value` | Ternary expression                                                                                  | left to right |

### Data in auth tokens

The`auth.token`object may contain the following values:

|            Field            |                                                                                                                                                                                                                           Description                                                                                                                                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `email`                     | The email address associated with the account, if present.                                                                                                                                                                                                                                                                                                                                                                                                      |
| `email_verified`            | `true`if the user has verified they have access to the`email`address. Some providers automatically verify email addresses they own.                                                                                                                                                                                                                                                                                                                             |
| `phone_number`              | The phone number associated with the account, if present.                                                                                                                                                                                                                                                                                                                                                                                                       |
| `name`                      | The user's display name, if set.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `sub`                       | The user's Firebase UID. This is unique within a project.                                                                                                                                                                                                                                                                                                                                                                                                       |
| `firebase.identities`       | Dictionary of all the identities that are associated with this user's account. The keys of the dictionary can be any of the following:`email`,`phone`,`google.com`,`facebook.com`,`github.com`,`twitter.com`. The values of the dictionary are arrays of unique identifiers for each identity provider associated with the account. For example,`auth.token.firebase.identities["google.com"][0]`contains the first Google user ID associated with the account. |
| `firebase.sign_in_provider` | The sign-in provider used to obtain this token. Can be one of the following strings:`custom`,`password`,`phone`,`anonymous`,`google.com`,`facebook.com`,`github.com`,`twitter.com`.                                                                                                                                                                                                                                                                             |
| `firebase.tenant`           | The tenantId associated with the account, if present. For example,`tenant2-m6tyz`                                                                                                                                                                                                                                                                                                                                                                               |

#### Additional fields in JWT ID tokens

You can also access the following`auth.token`fields:

|                                                                                                                                                                                                 Custom Token Claims                                                                                                                                                                                                 |||
|----------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `alg`                | Algorithm       | `"RS256"`                                                                                                                                                                                                                                                                                                                                                                    |
| `iss`                | Issuer          | Your project's service account email address                                                                                                                                                                                                                                                                                                                                 |
| `sub`                | Subject         | Your project's service account email address                                                                                                                                                                                                                                                                                                                                 |
| `aud`                | Audience        | `"https://identitytoolkit.googleapis.com/google.identity.identitytoolkit.v1.IdentityToolkit"`                                                                                                                                                                                                                                                                                |
| `iat`                | Issued-at time  | The current time, in seconds since the UNIX epoch                                                                                                                                                                                                                                                                                                                            |
| `exp`                | Expiration time | The time, in seconds since the UNIX epoch, at which the token expires. It can be a**maximum of 3600 seconds later** than the`iat`. Note: this only controls the time when the*custom token* itself expires. But once you sign a user in using`signInWithCustomToken()`, they will remain signed in into the device until their session is invalidated or the user signs out. |
| `<claims>`(optional) |                 | Optional custom claims to include in token, which can be accessed through`auth.token`(or`request.auth.token`) in expressions. For example, if you create a custom claim`adminClaim`, you can access it with`auth.token.adminClaim`.                                                                                                                                          |

## What's next?

- Firebase Data Connectprovides an Admin SDK to let you perform[queries and mutations from privileged environments](https://firebase.google.com/docs/data-connect/admin-sdk).
- Learn about IAM security in the[guide for managing services and databases](https://firebase.google.com/docs/data-connect/manage-services-and-databases).