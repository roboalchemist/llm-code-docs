# Source: https://firebase.google.com/docs/data-connect/cel-reference.md.txt

<br />

This reference guides covers Common Expression Language (CEL) syntax relevant to creating expressions for the`@auth(expr:)`and`@check(expr:)`directives.

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

For more details on the contents of`auth.token`see[Data in auth tokens](https://firebase.google.com/docs/data-connect/cel-reference#auth-token-contents)

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