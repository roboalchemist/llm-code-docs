# Source: https://smartcar.com/docs/integrations/webhooks/overview.md

# Source: https://smartcar.com/docs/integrations/webhooks/best-practices/overview.md

# Source: https://smartcar.com/docs/getting-started/dashboard/overview.md

# Source: https://smartcar.com/docs/api-reference/webhooks/events/overview.md

# Source: https://smartcar.com/docs/api-reference/authorization/overview.md

# Source: https://smartcar.com/docs/integrations/webhooks/overview.md

# Source: https://smartcar.com/docs/integrations/webhooks/best-practices/overview.md

# Source: https://smartcar.com/docs/getting-started/dashboard/overview.md

# Source: https://smartcar.com/docs/api-reference/webhooks/events/overview.md

# Source: https://smartcar.com/docs/api-reference/authorization/overview.md

# Source: https://smartcar.com/docs/integrations/webhooks/overview.md

# Source: https://smartcar.com/docs/getting-started/dashboard/overview.md

# Source: https://smartcar.com/docs/api-reference/authorization/overview.md

# Overview

> Understand how to manage access and refresh tokens to maintain persistent access to vehicles.

Smartcar uses OAuth 2.0 access tokens to secure API requests. Managing these tokens correctly is critical for ensuring your application can reliably interact with vehicles.

* **Access Tokens**: Short-lived tokens (2 hours) used to authorize requests to the Smartcar API.
* **Refresh Tokens**: Long-lived tokens (60 days) used to obtain new access tokens without requiring the user to re-authenticate.

## Token Management

* **[Auth Code Exchange](/api-reference/authorization/auth-code-exchange)**: The initial exchange of an authorization code for your first access and refresh token pair.
* **[Access Tokens Refresh](/api-reference/authorization/refreshing-access-token)**: How to get a new token set when the current one expires.

<Warning>
  When you use a refresh token, you receive a **new refresh token** in the response. You must save this new refresh token for future use, as the old one is invalidated.
</Warning>

## Storing access tokens

### Default and Brand Select Connect Flow

By default tokens are scoped to the user's connected services account.

<Note>This means that if there are multiple vehicles
on the account - and they are selected at the time of authorization, the access token is valid for all those vehicle Ids.</Note>

To manage this, we recommend using the [Smartcar User Id](/api-reference/user) to link tokens to your corresponding user id. The diagram below
will also allow multiple users to connect to vehicles on the same account.

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/StandardFlowDBDiagram.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=6ed076cedb2755b7ae11daa09475f614" data-og-width="850" width="850" data-og-height="324" height="324" data-path="images/connect/StandardFlowDBDiagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/StandardFlowDBDiagram.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=215549f52afa07960e4e79170e2ef433 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/StandardFlowDBDiagram.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1ef28f61d60c6e497951fe1699b5cd92 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/StandardFlowDBDiagram.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=29d52ce9358bfd402e377322317b3f5d 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/StandardFlowDBDiagram.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=cfb0b8f36d52241651c4c36624f6926e 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/StandardFlowDBDiagram.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=d0910d5555b6a82c37b46e9e1b279ccb 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/StandardFlowDBDiagram.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=0dca721dfb26cc28dc307e25873fa8fe 2500w" />
</Frame>

### Single Select Connect Flow

When using the Single Select flow, tokens are strictly scoped to the vehicle that was authorized for that Connect session.
This means that if a user connects multiple vehicles under the same connected services account, each vehicle id will be tied
to its own set of tokens.

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/ConnectMatchDBDiagram.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=0543e3075f012e372b8a5328509d5161" data-og-width="850" width="850" data-og-height="551" height="551" data-path="images/connect/ConnectMatchDBDiagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/ConnectMatchDBDiagram.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=3c1d425f8b4449673fdda5e2761ce74d 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/ConnectMatchDBDiagram.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=17c9fb393808fb58c070ac138cd89a5e 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/ConnectMatchDBDiagram.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1529833e0983bf57768dd22917dbbea5 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/ConnectMatchDBDiagram.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=41a7223d2aef7827e14fdf1e77ca7da2 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/ConnectMatchDBDiagram.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=0d75de09cc972859a9b71913cff846fb 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/ConnectMatchDBDiagram.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=9519db1db5666638998cede5a393e47a 2500w" />
</Frame>

## Token expiry

Access tokens are valid for 2 hours, while refresh tokens are valid for 60 days. You can use the corresponding refresh token to fetch a new token pair
once an access token has expired.

In order to maintain access to a vehicle without having a user go through Connect again, you'll want to make sure the refresh token never expires.
Whenever you fetch a new token pair, we will return a **new access and refresh token**.

Prior to expiry, access tokens will remain valid until their expiry when fetching a new token pair. Refresh tokens on the other hand are invalidated
1 minute after they're used.

To avoid common 401 Authentication errors, please ensure you are **persisting both the access and refresh token** we return whenever you fetch a new pair.

<Tip>
  In addition to any logic that checks access token expiry when making an API request, we strongly recommend having another job that periodically
  checks for refresh tokens that are close to expiry and refreshes them.
</Tip>
