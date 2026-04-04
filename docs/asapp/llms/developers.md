# Source: https://docs.asapp.com/getting-started/developers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Developer Quickstart

> Learn how to get started using ASAPPs APIs

Most of ASAPP's products require a combination of configuration and implementation, and making API calls is part of a successful integration.

<Warning> If you are **only** integrating ASAPP Messaging and **no other ASAPP product**, then you can skip this quickstart and go straight to [ASAPP Messaging](/agent-desk) guide.</Warning>

To get started making API calls, you need to:

* [Log in to the developer portal](#log-in-to-the-developer-portal)
* [Understand Sandbox vs Production](#understanding-sandbox-and-production)
* [Access your application's API Credentials](#access-api-credentials)
* [Make your first API call](#make-first-api-call)

## Log in to the developer portal

The developer portal is where you will:

* Grant access to developers and manage your team.
* Manage your API keys.

As part of [onboarding](/getting-started/intro), you would have appointed someone as the Developer Portal Admin. This user is in control of adding users and adjusting user access within the Dev Portal.

### Managing the developer portal

The developer portal uses **teams** and **apps** to manage access.

The members of your team can have one of the following roles:

* **Owner**: This user controls the team; this user is also called the Developer Portal Admin.
* **App Admin**: These users are able to change the information on applications owned by the team.
* **Viewers**: These users can view API credentials, but cannot change any settings.

Apps represent access to all of ASAPP's products. Your team will already have an app created for you. One app can access all of ASAPP's products. There can be one or more keys for the app; by default, the system already generates an initial API key.

The ASAPP email login or SSO only grants access to the dev portal, all permission and team management must be done from within the developer portal tooling.

## Understand Sandbox and Production

Initially, you only have access to the sandbox environment and we will create a Sandbox team and app for you. The sandbox is where you can initially build your integration but also try out new features before launching in production.

The different environments appear in ASAPP's API Domains:

| Environment | API Domain                      |
| :---------- | :------------------------------ |
| Sandbox     | `https://api.sandbox.asapp.com` |
| Production  | `https://api.asapp.com`         |

ASAPP's sandbox environment uses the same machine learning models and services as the production environment in order to replicate expected behaviors when interacting with a given endpoint.

<Warning>All requests to ASAPP sandbox and production APIs **must** use HTTPS protocol. The system will not redirect traffic using HTTP to HTTPS.</Warning>

### Moving to Production

Once you are ready to move to launch with real traffic and move to production, request production access. Tell your ASAPP account team which user will be the Production Developer Portal Admin. ASAPP will create a dedicated production team and app that you can manage as you did for the sandbox team and app.

## Access API Credentials

To access your API credentials, once you've logged in:

* Click your username and click Apps
  <Frame>
    <img src="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/dev-portal-access.png?fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=cffb996b431c494b9e9ccdd88aef03a9" data-og-width="1065" width="1065" data-og-height="525" height="525" data-path="images/getting-started/dev-portal-access.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/dev-portal-access.png?w=280&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=2c6744c06e52f104846decdd62e2c34f 280w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/dev-portal-access.png?w=560&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=3eda6fd6a6c2562559128cd94ea4c8ca 560w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/dev-portal-access.png?w=840&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=9f43e3f14676f831c6a1168b4ac1dfb6 840w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/dev-portal-access.png?w=1100&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=308c4365a21435de4f6bf042f82ba113 1100w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/dev-portal-access.png?w=1650&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=3c00d429c3b49237f87c3694bc2c1114 1650w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/dev-portal-access.png?w=2500&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=a03b40caeb5eceb53712ec59c492b981 2500w" />
  </Frame>
* Click your Sandbox App.
* Navigate down to API Keys and copy your API Id and API Secret
  <Frame>
    <img src="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/dev-portal-app.png?fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=d8d1e81828c1c06180edca26c9962ec5" data-og-width="1065" width="1065" data-og-height="966" height="966" data-path="images/getting-started/dev-portal-app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/dev-portal-app.png?w=280&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=c46389552b49f0a55b865cc0a1d11d9a 280w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/dev-portal-app.png?w=560&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=8fa34f0a1de6e6a9e486314ddec02856 560w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/dev-portal-app.png?w=840&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=c8e2f44d48d39d8d7ea0067157b8b447 840w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/dev-portal-app.png?w=1100&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=daefd5f47c41dad933cd15aa59b783ea 1100w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/dev-portal-app.png?w=1650&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=86f0c5df5f8cb0c20980eb3bd459f143 1650w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/dev-portal-app.png?w=2500&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=c905f8967c8d6dc696ae885e2b1d31e0 2500w" />
  </Frame>

Save the API Id and Secret. All API requests use these for authentication.

## Make First API Call

With credentials in hand, we can make our first API call. Let's start with creating a `conversation`, the root entity for any interaction within a call center.

This example creates an empty conversation with required id from your system. You need to include the API Id and Secret as `asapp-api-id` and `asapp-api-secret` headers respectively.

```bash  theme={null}
curl -X POST 'https://api.sandbox.asapp.com/conversation/v1/conversations' \
--header 'asapp-api-id: <API KEY ID>' \
--header 'asapp-api-secret: <API TOKEN>' \
--header 'Content-Type: application/json' \
--data '{ 
  "externalId": "con_1",
  "customer": {   
    "externalId": "cust_1234"
  },
  "timestamp": "2024-12-12T11:42:42Z"
}'
```
