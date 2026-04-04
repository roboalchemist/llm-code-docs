# Source: https://docs.replit.com/extensions/api/data.md

# data API

> Access Replit's GraphQL API to retrieve user information, Replit App metadata, and other platform data through the Extensions API.

The data API allows you to get information and metadata exposed from Replit's GraphQL API.

## Usage

```ts  theme={null}
import { data } from '@replit/extensions';
```

## Methods

### `data.currentUser`

Fetches the current user via graphql

```ts  theme={null}
currentUser(args: CurrentUserDataInclusion): Promise<{ user: CurrentUser }>
```

### `data.userById`

Fetches a user by their id via graphql

```ts  theme={null}
userById(args: { id: number } & UserDataInclusion): Promise<{ user: User }>
```

### `data.userByUsername`

Fetches a user by their username via graphql

```ts  theme={null}
userByUsername(args: { username: string } & UserDataInclusion): Promise<{ userByUsername: User }>
```

### `data.currentRepl`

Fetches the current Replit App via graphql

```ts  theme={null}
currentRepl(args: ReplDataInclusion): Promise<{ repl: Repl }>
```

### `data.replById`

Fetches a Replit App by its ID via graphql

```ts  theme={null}
replById(args: { id: string } & ReplDataInclusion): Promise<{ repl: Repl }>
```

### `data.replByUrl`

Fetches a Replit App by its URL using GraphQL

```ts  theme={null}
replByUrl(args: { url: string } & ReplDataInclusion): Promise<{ repl: Repl }>
```

## Types

### CurrentUser

Extended values for the current user

| Property       | Type                          |
| -------------- | ----------------------------- |
| bio?           | `string`                      |
| displayName?   | `string`                      |
| firstName?     | `string`                      |
| followCount?   | `number`                      |
| followerCount? | `number`                      |
| fullName?      | `string`                      |
| id             | `number`                      |
| image          | `string`                      |
| isUserHacker?  | `boolean`                     |
| isUserPro?     | `boolean`                     |
| lastName?      | `string`                      |
| roles?         | [`UserRole[]`](#userrole)     |
| socials?       | [`UserSocial[]`](#usersocial) |
| url?           | `string`                      |
| username       | `string`                      |

### CurrentUserDataInclusion

Options for the currentUser query

| Property           | Type      |
| ------------------ | --------- |
| includePlan?       | `boolean` |
| includeRoles?      | `boolean` |
| includeSocialData? | `boolean` |

### EditorPreferences

Editor Preferences

| Property               | Type      |
| ---------------------- | --------- |
| \_\_typename           | `string`  |
| codeIntelligence       | `boolean` |
| codeSuggestion         | `boolean` |
| fontSize               | `number`  |
| indentIsSpaces         | `boolean` |
| indentSize             | `number`  |
| keyboardHandler        | `string`  |
| minimapDisplay         | `string`  |
| multiselectModifierKey | `string`  |
| wrapping               | `boolean` |

### Replit App

A Replit App

| Property         | Type                                              |
| ---------------- | ------------------------------------------------- |
| commentCount?    | `number`                                          |
| comments?        | [`ReplCommentConnection`](#replcommentconnection) |
| description      | `string`                                          |
| iconUrl?         | `string`                                          |
| id               | `string`                                          |
| imageUrl?        | `string`                                          |
| isPrivate        | `boolean`                                         |
| likeCount?       | `number`                                          |
| multiplayers?    | [`User[]`](#user)                                 |
| owner?           | [`ReplOwner`](#replowner)                         |
| publicForkCount? | `number`                                          |
| runCount?        | `number`                                          |
| slug             | `string`                                          |
| tags?            | [`Tag[]`](#tag)                                   |
| timeCreated      | `string`                                          |
| title            | `string`                                          |
| url              | `string`                                          |

### ReplComment

A Replit App Comment

| Property | Type            |
| -------- | --------------- |
| body     | `string`        |
| id       | `number`        |
| user     | [`User`](#user) |

### ReplCommentConnection

An array of ReplComments as items

| Property | Type                            |
| -------- | ------------------------------- |
| items    | [`ReplComment[]`](#replcomment) |

### ReplDataInclusion

Options for replit app queries

| Property             | Type      |
| -------------------- | --------- |
| includeComments?     | `boolean` |
| includeMultiplayers? | `boolean` |
| includeOwner?        | `boolean` |
| includeSocialData?   | `boolean` |

### ReplOwner

A Replit App Owner, can be either a User or a Team

| Property     | Type     |
| ------------ | -------- |
| \_\_typename | `string` |
| description? | `string` |
| id           | `number` |
| image        | `string` |
| username     | `string` |

### Tag

A Replit App tag

| Property   | Type      |
| ---------- | --------- |
| id         | `string`  |
| isOfficial | `boolean` |

### User

A Replit user

| Property       | Type                          |
| -------------- | ----------------------------- |
| bio?           | `string`                      |
| displayName?   | `string`                      |
| firstName?     | `string`                      |
| followCount?   | `number`                      |
| followerCount? | `number`                      |
| fullName?      | `string`                      |
| id             | `number`                      |
| image          | `string`                      |
| isUserHacker?  | `boolean`                     |
| isUserPro?     | `boolean`                     |
| lastName?      | `string`                      |
| roles?         | [`UserRole[]`](#userrole)     |
| socials?       | [`UserSocial[]`](#usersocial) |
| url?           | `string`                      |
| username       | `string`                      |

### UserDataInclusion

Options for user queries

| Property           | Type      |
| ------------------ | --------- |
| includePlan?       | `boolean` |
| includeRoles?      | `boolean` |
| includeSocialData? | `boolean` |

### UserRole

A user role

| Property | Type     |
| -------- | -------- |
| id       | `number` |
| key      | `string` |
| name     | `string` |
| tagline  | `string` |

### UserSocial

A user social media link

| Property | Type                                |
| -------- | ----------------------------------- |
| id       | `number`                            |
| type     | [`UserSocialType`](#usersocialtype) |
| url      | `string`                            |

### UserSocialType

An enumerated type of social media links

| Property | Type |
| -------- | ---- |

### UserSocialType

An enumerated type of social media links

```ts  theme={null}
discord = 'discord'
facebook = 'facebook'
github = 'github'
linkedin = 'linkedin'
twitch = 'twitch'
twitter = 'twitter'
website = 'website'
youtube = 'youtube'
```

### CurrentUserQueryOutput

A graphql response for the currentUser query

```ts  theme={null}
GraphResponse<{
  user: CurrentUser;
}>
```

### GraphResponse\<`T`>

A graphql response

```ts  theme={null}
Promise<T | never>
```

### ReplQueryOutput

A graphql response for the repl query

```ts  theme={null}
GraphResponse<{
  repl: Repl;
}>
```

### UserByUsernameQueryOutput

A graphql response for the userByUsername query

```ts  theme={null}
GraphResponse<{
  userByUsername: User;
}>
```

### UserQueryOutput

A graphql response for the user query

```ts  theme={null}
GraphResponse<{
  user: User;
}>
```
