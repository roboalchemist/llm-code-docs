# Source: https://docs.zapier.com/platform/news/2025/4xx-errors-refreshAccessToken.md

# No more manual handling of 4xx errors in refreshAccessToken

> We now automatically handle 4xx error responses when refreshing OAuth2 access tokens.

*Effective: 2025-09-08*

We made a change to how we handle error responses when refreshing OAuth2 access tokens.

## Old behavior

When an app gives an error response (status code 4xx or 5xx) while refreshing the OAuth2 access token, Zapier keeps retrying the Zap step indefinitely or until it hits a certain limit, depending on the user's settings.

## New behavior

When an app encounter a 4xx error response (except for the ones listed below) while refreshing the access token, Zapier will mark the connect as stale, and send an email telling the user to reconnect.

Exceptions: The following 4xx errors often indicate a temporary issue so they still have the same behavior as before:

* 408 (Request Timeout)
* 409 (Conflict)
* 423 (Locked)
* 425 (Too Early)
* 429 (Too Many Requests)

This is how Zapier handles a stale connection:

* If the stale connection is used by a trigger step, the trigger polling system will skip polling when the scheduled time comes.
* If the stale connection is used by an action step, the Zap run will be put on hold until the user reconnects and replays the run.

## What does it mean to you?

You don't need to handle 4xx error responses in `refreshAccessToken` anymore. For example, you might have been catching 4xx errors in `refreshAccessToken` by enabling `skipThrowForStatus` and throwing `ExpiredAuthError`:

```js  theme={null}
const refreshAccessToken = async (z, bundle) => {
  const response = await z.request({
    url: "https://example.com/token/refresh",
    method: "POST",
    body: {
      refresh_token: bundle.authData.refresh_token,
      client_id: process.env.CLIENT_ID,
      client_secret: process.env.CLIENT_SECRET,
      grant_type: "refresh_token",
    },
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    skipThrowForStatus: true,
  });

  if (response.status >= 400 && response.status < 500) {
    throw new z.errors.ExpiredAuthError(
      "Authentication issue. Please reconnect.",
    );
  }

  return response.data;
};
```

This is no longer necessary. Now you can simplify your code as follows and let the platform handle it:

```js  theme={null}
const refreshAccessToken = async (z, bundle) => {
  const response = await z.request({
    url: "https://example.com/token/refresh",
    method: "POST",
    body: {
      refresh_token: bundle.authData.refresh_token,
      client_id: process.env.CLIENT_ID,
      client_secret: process.env.CLIENT_SECRET,
      grant_type: "refresh_token",
    },
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  });
  return response.data;
};
```

No need to upgrade zapier-platform-core; this change is implemented in the Zapier backend.
