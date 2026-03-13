# Source: https://blitzjs.com/docs/session-management

Title: Sessions - Blitz.js

URL Source: https://blitzjs.com/docs/session-management

Markdown Content:
Blitz has built in session management that can be used with any type of authentication or identity providers.

Session management performs the following functions:

1. Tracking whether a user is logged in or not
2. Attribute multiple requests to the same user, even when they are logged out
3. Protection against CSRF attacks

[](https://blitzjs.com/docs/session-management#session-basics)Basics
--------------------------------------------------------------------

### [](https://blitzjs.com/docs/session-management#login)Login

For login you will have form component in your UI that will submit a login mutation like the one shown below.

### [](https://blitzjs.com/docs/session-management#logout)Logout

For logout you will have a button in your UI that will submit a logout mutation like the one shown below.

Revoking a session will immediately delete all client-side query cache causing all queries on the page to be refetched. This ensures any sensitive data in the cache is deleted.

### [](https://blitzjs.com/docs/session-management#change-session-public-data-of-current-user)Change Session PublicData of Current User

Each session has [`PublicData`](https://blitzjs.com/docs/session-management#publicdata), data which is available on the client and has the potential to be read by third-parties because it's stored in a cookie readable by any Javascript code. This is usually used to store the current user id, user role, and perhaps current organization id.

You can change the session public data in any query or mutation like this:

### [](https://blitzjs.com/docs/session-management#session-expiration-and-auto-refresh)Session Expiration / Auto-refresh

A session is automatically refreshed after 1/4th of the expiry time has passed. The default expiry time is 30 days. If you change the session’s [`PublicData`](https://blitzjs.com/docs/session-management#publicdata) the session is also automatically refreshed. You will need to update tokens (access and anti-CSRF) after a session refresh, if you use them (e.g. in a mobile app).

[](https://blitzjs.com/docs/session-management#anonymous-sessions)Anonymous Sessions
------------------------------------------------------------------------------------

If a user is not logged in, an anonymous session will automatically be created for them. You can use `ctx.session.$setPublicData()` and `ctx.session.$setPrivateData()` for anonymous sessions the same as for logged in users. Any data you set for an anonymous session will automatically be transferred to an authentication session when a user logs in.

Anonymous sessions are JWT tokens that are stored on the client as an httpOnly cookie that never expires.

`PublicData` for anonymous sessions is kept in the session JWT and not stored in the database. Anonymous sessions will only be saved in your database if you call `session.$setPrivateData()`.

The anonymous session will be created on the first network request, whether SSR or via an API. This will happen as long as `sessionMiddleware` is in your middleware chain for that request.

One use case for this is saving shopping cart items for anonymous users. If an anonymous user later signs up or logs in, the anonymous session data can be merged into their new authenticated session.

Anonymous session `PublicData` looks like this:

[](https://blitzjs.com/docs/session-management#customize-session-public-data-in-typescript)Customize Session Public Data in TypeScript
--------------------------------------------------------------------------------------------------------------------------------------

If using TypeScript, first update the `Session.PublicData` type in `types.ts` like this:

Then change all uses of `ctx.session.$create()` to pass in the new fields.

You can also use `ctx.session.$setPublicData()` to update session data for an already logged in user. This will _merge_ values with the existing public data.

To access public data on the client:

To access public data on the server:

[](https://blitzjs.com/docs/session-management#manual-api-requests)Manual API Requests
--------------------------------------------------------------------------------------

When making a request from the client to an API route, you need to include the anti-CSRF token in the `anti-csrf` header like this:

And then you can get the sessionContext in the API route like this:

[](https://blitzjs.com/docs/session-management#technical-details-of-how-it-works)Technical Details of How it Works
------------------------------------------------------------------------------------------------------------------

Authenticated sessions use opaque tokens that are stored in the database.

### [](https://blitzjs.com/docs/session-management#implementation-details)Implementation Details

#### Session Creation

* At login, the server creates two opaque tokens:
  * An access token.
  * An anti-csrf token.

* Both are a 32 character long `string`.
* The access token is sent to the frontend via an `httpOnly`, `secure` cookie.
* The anti-csrf token is sent to the frontend via a normal, `secure` cookie that can be read from Javascript.
* The SHA256 hash of the access token will be stored in the database. This token has the following properties mapped to it:
  * userId
  * expiry time
  * session data

* The anti-csrf token is stored alongside the access token.
* Creating a new session while another one exists results in the headers / cookies changing. However, the older session will still be alive.
* For serious production apps, a cronjob is needed to remove all expired tokens on a regular basis.

#### Session Verification

* For each request that requires CSRF protection, the frontend sends the anti-csrf token in the request header.
* An incoming access token is verified by checking that it's in the db and that it has not expired. After each verification, the expiry time of the access token is updated.
* CSRF attacks are prevented by checking that the incoming anti-csrf token (from the header) is the one associated with the session.

#### Session Revocation/Logout

* This is done by deleting the session from the database.
* Logout additionally clears the cookies, and a header is sent signaling the frontend to remove the anti-csrf token from the localstorage

[](https://blitzjs.com/docs/session-management#types)Types
----------------------------------------------------------

#### `SessionContext`
