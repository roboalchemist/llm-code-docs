# Source: https://docs.replit.com/extensions/api/auth.md

# auth API

> Learn how to authenticate users securely in your Replit extensions using the auth API module. Get and verify JWT tokens for user authentication.

# auth API <span className="deprecated-pill">experimental</span>

The `auth` api module allows you to securely authenticate a Replit user if they use your extension.

## Usage

```ts  theme={null}
import { experimental } from '@replit/extensions';
const { auth } = experimental;
```

## Methods

### `auth.getAuthToken`

Returns a unique JWT token that can be used to verify that an extension has been loaded on Replit by a particular user

```ts  theme={null}
getAuthToken(): Promise<string>
```

### `auth.verifyAuthToken`

Verifies a provided JWT token and returns the decoded token.

```ts  theme={null}
verifyAuthToken(token: string): Promise<{ payload: any, protectedHeader: any }>
```

### `auth.authenticate`

Performs authentication and returns the user and installation information

```ts  theme={null}
authenticate(): Promise<AuthenticateResult>
```

## Types

### AuthenticatedUser

| Property | Type     |
| -------- | -------- |
| id       | `number` |

### AuthenticateResult

| Property     | Type                                      |
| ------------ | ----------------------------------------- |
| installation | `AuthenticatedInstallation`               |
| user         | [`AuthenticatedUser`](#authenticateduser) |
