# Source: https://firebase.google.com/docs/auth/admin.md.txt

<br />

The Firebase Admin SDK allows you to integrate your own servers with
Firebase Authentication. You can use the Firebase Admin SDK to manage your users or to
manage authentication tokens. There are a number of reasons you would want to
do this:

**User Management**

It is not always convenient to have to visit the
Firebase console

to manage your Firebase users. The admin user management API
provides programmatic access to those same users. It even allows you to do
things the Firebase console
cannot, such as
retrieving a user's full data and changing a user's password, email address, or
phone number.

**Custom Authentication**

You can integrate an external user system with Firebase. For
example, you may already have a pre-existing user database or you may want to
integrate with a third-party identity provider that Firebase Authentication doesn't natively
support.

To do this, you can create custom tokens with arbitrary claims identifying the
user. These custom tokens can then be used to sign into the Firebase Authentication service on
a client application and assume the identity described by the token's claims.
This identity will then be used when accessing other Firebase
services, such as Cloud Storage.

**Identity Verification**

Firebase Authentication is primarily used to identify users of your app in order to restrict
access to other services, like Cloud Storage.
You can also use the service to identify these users on your own server. This
lets you securely perform server-side logic on behalf of users that have signed
in with Firebase Authentication.

To do this, you can retrieve an ID token from a client
application signed in with Firebase Authentication and include the token in a request to your
server. Your server then verifies the ID token and extracts the claims that
identify the user (including their `uid`, the identity provider they logged in
with, etc.). This identity information can then be used by your server to carry
out actions on behalf of the user.

> [!NOTE]
> Note: This documentation explains how to manage your own authentication tokens. If you are instead looking for documentation on how to authenticate the Admin SDK to access the Firebase Realtime Database, check out [Introduction to the Admin Database API](https://firebase.google.com/docs/database/admin/start/).

The Firebase Admin SDK provides methods for accomplishing the
authentication tasks above by enabling you to manage your users, generate custom
tokens, and verify ID tokens.

**Custom User Claims**

In some cases, you may want to implement fine-grained access control
for users already signed in with one of the supported Firebase
auth providers such as Email/Password, Google, Facebook, phone, etc. A
combination of custom user claims and application security rules provides this
capability. For example, a user signed in with the Firebase Authentication Email and
Password provider can have access control defined using custom claims.

## User management

The Firebase Admin SDK provides an API for managing your
Firebase users with elevated privileges. The admin user management
API gives you the ability to programmatically retrieve, create, update, and
delete users without requiring a user's existing credentials and without
worrying about client-side rate limiting.
[Manage users](https://firebase.google.com/docs/auth/manage-users)

## Custom token creation

The primary use for creating custom tokens is to allow users to authenticate
against an external or legacy authentication mechanism. This could be one you
control, such as your LDAP server, or a third-party OAuth provider which
Firebase does not natively support, such as Instagram or LinkedIn.

The Firebase Admin SDK has a built-in method for creating
custom tokens. You can also programmatically create custom tokens in any
language using third-party JWT libraries.

Your server should create a custom token with a unique identifier (`uid`) and
pass that token to a client app, which will use it to sign in to
Firebase. See
[Create custom tokens](https://firebase.google.com/docs/auth/admin/create-custom-tokens)
for code samples and more details about the custom token creation process.

> [!NOTE]
> Note: If you just need to connect to the Firebase Realtime Database from your own server, don't use custom tokens. Instead, use a Firebase Admin SDK to [authenticate with limited privileges](https://firebase.google.com/docs/database/admin/start#authenticate-with-limited-privileges).

<br />

[Create custom tokens](https://firebase.google.com/docs/auth/admin/create-custom-tokens)

## ID token verification

If your Firebase client app communicates with your backend server,
you might need to identify the currently signed-in user on your server so you
can perform server-side logic on their behalf. You can do this securely by using
ID tokens, which are created by Firebase when a user signs into an
Firebase app. ID tokens conform to the
[OpenID Connect spec](http://openid.net/specs/openid-connect-core-1_0.html) and
contain data to identify a user, as well as some other profile and
authentication related information. You can send, verify,
and inspect these tokens from your own backends. This allows you to securely
identify the currently signed in user and authorize them into your own backend
resources.

The Firebase Admin SDK has a built-in method for verifying
ID tokens. You can also programmatically verify ID tokens in any
language using third-party JWT libraries. See
[Verify ID tokens](https://firebase.google.com/docs/auth/admin/verify-id-tokens)
for more details and code samples about the ID token verification process.

> [!NOTE]
> Note: If you want your server to emulate user actions like accessing the Firebase Realtime Database as that user, you should first verify and decode an ID token for that user. Then, use the `databaseAuthVariableOverride` option to limit the privileges of your server, as described in [Authenticate with limited privileges](https://firebase.google.com/docs/database/admin/start#authenticate-with-limited-privileges).

<br />

[Verify ID tokens](https://firebase.google.com/docs/auth/admin/verify-id-tokens)

## Custom user claims

The Firebase Admin SDK lets you set custom attributes on user accounts.
With custom user claims, you can give users different levels of access (roles),
which are then enforced in an application's security rules.

After custom claims are modified on a user via the Firebase Admin SDK, they are
propagated to the authenticated users on the client side via their ID tokens.
The ID token is a trusted mechanism for delivering
these custom claims, and all authenticated access must validate the ID token
before processing the associated request.

[Control Access with Custom Claims](https://firebase.google.com/docs/auth/admin/custom-claims)