# Source: https://firebase.google.com/docs/reference/rules/rules.firestore.Request.md.txt

# Interface: Request

# [rules](https://firebase.google.com/docs/reference/rules/rules).[firestore](https://firebase.google.com/docs/reference/rules/rules.firestore).Request

interface static

The incoming request context.

## Properties

### auth

[rules.Map](https://firebase.google.com/docs/reference/rules/rules.Map)

Request authentication context.

- `uid` - the UID of the requesting user.
- `token` - a map of JWT token claims.

The `token` map contains the following values:

*** ** * ** ***

|             Field             |                                                                                                                                                                                                                                   Description                                                                                                                                                                                                                                   |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \`email\`                     | The email address associated with the account, if present.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| \`email_verified\`            | \`true\` if the user has verified they have access to the \`email\` address.                                                                                                                                                                                                                                                                                                                                                                                                    |
| \`phone_number\`              | The phone number associated with the account, if present.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| \`name\`                      | The user's display name, if set.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| \`sub\`                       | The user's Firebase UID. This is unique within a project.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| \`firebase.identities\`       | A map of all the identities that are associated with this user's account. The keys of the map can be any of the following: \`email\`, \`phone\`, \`google.com\`, \`facebook.com\`, \`github.com\`, \`twitter.com\`. The values of the map are lists of unique identifiers for each identitity provider associated with the account. For example, \`request.auth.token.firebase.identities\["google.com"\]\[0\]\` contains the first Google user ID associated with the account. |
| \`firebase.sign_in_provider\` | The sign-in provider used to obtain this token. Can be one of the following strings: \`custom\`, \`password\`, \`phone\`, \`anonymous\`, \`google.com\`, \`facebook.com\`, \`github.com\`, \`twitter.com\`.                                                                                                                                                                                                                                                                     |
| \`firebase.tenant\`           | The tenantId associated with the account, if present. e.g. \`tenant2-m6tyz\`                                                                                                                                                                                                                                                                                                                                                                                                    |

### method

non-null [rules.String](https://firebase.google.com/docs/reference/rules/rules.String)

The request method. One of:

- `get`
- `list`
- `create`
- `update`
- `delete`

### path

non-null [rules.Path](https://firebase.google.com/docs/reference/rules/rules.Path)

Path of the affected resource.

### query

non-null [rules.Map](https://firebase.google.com/docs/reference/rules/rules.Map)

Map of query properties, when present.

- `limit` - query limit clause.
- `offset` - query offset clause.
- `orderBy` - query orderBy clause.

#### Example

    // Limit documents per request to 50
    allow list: if request.query.limit <= 50

### resource

non-null [rules.firestore.Resource](https://firebase.google.com/docs/reference/rules/rules.firestore.Resource)

The new resource value, present on write requests only.

### time

non-null [rules.Timestamp](https://firebase.google.com/docs/reference/rules/rules.Timestamp)

When the request was received by the service.

For Firestore write operations that include server-side timestamps,
this time will be equal to the server timestamp.

#### Example

    // Make sure that 'myServerTimestampField' was set using a
    // server-side timestamp.
    request.time == request.resource.data.myServerTimestampField