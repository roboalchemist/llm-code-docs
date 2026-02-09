# Source: https://smartcar.com/docs/getting-started/using-vs-with-postman.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Testing with Postman

> In this tutorial we'll go over how to use Vehicle Simulator to test out Smartcar using Postman.

## What is Postman?

Postman is a collaboration platform for API development. Postman's features simplify each step of building an API and streamline collaboration so you can create better APIs - faster.
You’ll need a few things to start making API calls with Smartcar and Postman:

* [A Postman Account](https://identity.getpostman.com/signup?continue=https%3A%2F%2Fgo.postman.co%2Fbuild)
* [Smartcar’s Postman Collection](https://www.postman.com/smartcar/smartcar-api/collection/qk7g8v2/smartcar-api-v3?action=share\&creator=33621094)
* [A Smartcar Developer Account](https://dashboard.smartcar.com/signup)

## Configuring the Connect flow in Postman

1. Install the latest [Postman app](https://www.postman.com/downloads/) and log in
2. Import the [Smartcar collection](https://www.postman.com/smartcar/smartcar-api/collection/qk7g8v2/smartcar-api-v3?action=share\&creator=33621094) into your local Postman workspace. Hit Import.
3. Click Link, paste in [the link](https://www.postman.com/smartcar/smartcar-api/collection/qk7g8v2/smartcar-api-v3?action=share\&creator=33621094) to the collection and hit Continue.
4. On the next screen, hit Import.

<Tabs>
  <Tab title="Step 1">
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/postman.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=eff974c27c35429e996cc03ac0537ca3" data-og-width="1909" width="1909" data-og-height="735" height="735" data-path="images/help-center/guide-postman/postman.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/postman.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=016888b9f5f7351d6c23031258011ffd 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/postman.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=3fddd8da5d08c02b7b506e691dd0b9dd 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/postman.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=3c70e7485b08c3c9d26bd6c7e2c7dc8a 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/postman.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=44de4f15cf082a01142835380edfa632 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/postman.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c8fc1eb62d30bf5d77e41f43d6ec7785 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/postman.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=a8bf82c0dfe360db42977824304c19be 2500w" />
  </Tab>

  <Tab title="Step 2">
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import1.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=0d6ca63f2c0ec0531d6f43013d898d46" data-og-width="2000" width="2000" data-og-height="781" height="781" data-path="images/help-center/guide-postman/import1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import1.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=75cc5f5c6efea65b11aa05ad9bccaaec 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import1.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e408a3428f00acb334b0e8c828fd7b77 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import1.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=bfd2d6e8c679444d0f4b669971476c06 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import1.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=3f2f46f58bebc16f68bcadbab4c05e45 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import1.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=83754ca3236b6ea69edc473b9ebdbb73 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import1.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=218117c1cff0ac9877f08284d5fa861d 2500w" />
  </Tab>

  <Tab title="Step 3">
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import2.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ab103641bc93ed9d009e611042a87ddd" data-og-width="2000" width="2000" data-og-height="2034" height="2034" data-path="images/help-center/guide-postman/import2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import2.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=1bf38338e70dd967e6fa08b1a42d1be4 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import2.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=70c3f7ddec9d28f7d9a88a07e2441c64 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import2.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f151fa36c5b84d324f88e62ecc108bbe 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import2.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=6aec86aa154618901f62892be022faa7 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import2.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f64bfdc2333313b74a8f68fc104bd4d0 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import2.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=49a5bb764929570322d1d7d6b3b14b86 2500w" />
  </Tab>

  <Tab title="Step 4">
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import3.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ca91ea1a83ddcd32189f05e142917e3e" data-og-width="2000" width="2000" data-og-height="3103" height="3103" data-path="images/help-center/guide-postman/import3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import3.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=11a42a3cadbc26df42e96c5fee19f1b3 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import3.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=b9b8e8c1c6120d82fdc3586f9c66e5a5 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import3.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=d1f18a835ad80f2669bdcfb9f6480667 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import3.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ba8d70342d7d97385599b04d5c67bc77 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import3.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=6f96f78fcdcc2bece341c64ef878edae 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import3.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=b8dd3242dd2775d1a41b509344ae763c 2500w" />
  </Tab>
</Tabs>

## Smartcar Application Configuration

If you haven’t already signed up for a Smartcar Developer account, you can do so from this [**sign-up link**](https://dashboard.smartcar.com/signup).

* Grab your **Client ID** and **Client Secret** from the Configuration page after you sign in, and copy them to someplace secure. You’ll need those tokens a little later in this setup.
* Under the Credentials tab for your application, you’ll need to add the following Redirect URIs. This will ensure that Smartcar Connect exits successfully with both Postman’s Native and Web clients.

```
https://oauth.pstmn.io/v1/browser-callback 
http://localhost:8000/exchange
```

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/appConfig.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=227ee48bcdd4a1994049717c996deaa4" data-og-width="2000" width="2000" data-og-height="1306" height="1306" data-path="images/help-center/guide-postman/appConfig.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/appConfig.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=22525c94a1167dc50c0b7c29f521b75d 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/appConfig.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=35f84af32748222af74a57f5b8b56a1d 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/appConfig.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=7aef027c29db70ca3ba0a8ee7e878626 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/appConfig.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=0efa259095c171610dbabf66573d46e2 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/appConfig.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=d9bcc2b805c2374762e3e4340d0880e0 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/appConfig.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=0fb808d66c484339ccf916af71d3a1e3 2500w" />
</Frame>

Through the Connect flow, you’re able to get consent from vehicle owners to connect their vehicle to your application. Postman provides an easy way to manage OAuth 2.0 flows under the Authorization tab of a Collection. Set up the Configuration Options for either a live or simulated vehicle.

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/authorization.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=44585e961f665d2d259993a8ddd4319e" data-og-width="2000" width="2000" data-og-height="2428" height="2428" data-path="images/help-center/guide-postman/authorization.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/authorization.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=46aa2f12046829bd12721516223962fc 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/authorization.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e1564439120f97729c09dfdbb991f128 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/authorization.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c2a4277fff801a484e5119578b772632 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/authorization.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=64c4d2591f0c61bd44dc7652bed92312 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/authorization.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=817af5d94ee6ab342b4429d45d645300 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/authorization.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=8a9fc062932e0fc9d38577d3ecd1ec4f 2500w" />
</Frame>

**Live Vehicle**

| Parameter        | Description                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| Auth URL         | `https://connect.smartcar.com/oauth/authorize?approval_prompt=force`                                              |
| Access Token URL | `https://auth.smartcar.com/oauth/token`                                                                           |
| Client ID        | `client_id` from your Dashboard                                                                                   |
| Client Secret    | `client_secret` from your Dashboard                                                                               |
| Scope            | A space-separated list of [permissions](/api-reference/permissions) that your application is requesting access to |

**Simulated Vehicle**

| Parameter        | Description                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| Auth URL         | `https://connect.smartcar.com/oauth/authorize?approval_prompt=force&mode=simulated`                               |
| Access Token URL | `https://auth.smartcar.com/oauth/token`                                                                           |
| Client ID        | `client_id` from your Dashboard                                                                                   |
| Client Secret    | `client_secret` from your Dashboard                                                                               |
| Scope            | A space-separated list of [permissions](/api-reference/permissions) that your application is requesting access to |

## Setting up a Simulated Vehicle

Under the Simulator tab on Dashboard, hit Add Vehicle. Note that you may already have a pre-created simulated vehicle available, if so skip to **Connecting to a vehicle** below.

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim1.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=ac48f25d23f26724ac3c3a030a98db67" data-og-width="1601" width="1601" data-og-height="633" height="633" data-path="images/help-center/guide-postman/sim1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim1.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=81b228e533bb030731f804c8e5dc79f8 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim1.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=684fa9b64b213b5a14070d9805907e60 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim1.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=cf9129e663aabc81e830c5483165b9a5 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim1.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=1aa6264af9bbe9cc36d80b3cdb691d6f 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim1.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=1cbf429bcd1da5b1191df8a90aadec27 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim1.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=ad28310d044fb17262ac42b120855908 2500w" />
</Frame>

Select a region and MMY for your vehicle, then hit Search by MMY

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim2.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=d4185d0baab4608387e4bcb418395156" data-og-width="1691" width="1691" data-og-height="1120" height="1120" data-path="images/help-center/guide-postman/sim2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim2.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=3e8c4290600c6fac71158aed12b6311c 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim2.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=4b1c85eda9dffee5d77ba0f3e5df0f71 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim2.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=573ff038bcc73c80a01e07e46a07374e 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim2.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=1347a9538d405c40efc0b8ae939ba73e 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim2.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=a69b34c3beea29e4800ee2663adeaf20 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim2.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=e40af5e2b60a6d1bbd4a36d9bd7c0577 2500w" />
</Frame>

After selecting Use Vehicle, you’ll want to select a state for the vehicle. After that, you’ll get a set of credentials to use in the Connect flow.

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim3.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=a80ce27d74bf60db8c576a22a73dfe50" data-og-width="1691" width="1691" data-og-height="920" height="920" data-path="images/help-center/guide-postman/sim3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim3.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=5871a63b04a29e9813c2224b6decf078 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim3.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=0d6de51615abdd7657c0aee6bbf0df47 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim3.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=0689689c1f14cb2e861731807feafc16 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim3.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=5cbd492e16eb56d47a7c6015d2feb54b 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim3.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=efbc736170c9e3aa4272d65d019747de 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim3.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=bc5bccd272f3cc5b79e64abacf157dd8 2500w" />
</Frame>

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim4.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=234f54c381002a8dc4bbb988d9678d23" data-og-width="1929" width="1929" data-og-height="849" height="849" data-path="images/help-center/guide-postman/sim4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim4.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=ea1b8471e9682dd3b1a08502dd887fb5 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim4.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=e511753f8e9c7b299bc7424aeb654ce9 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim4.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=27e78a8cec0bdfb038b737a8e0842ad0 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim4.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=1812b6b804ee240ad2396dacc0c65bb4 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim4.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=0409c59399c2063de53898838018eaf8 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim4.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=da731b53ecdeeb4ef690b58e66cf17a7 2500w" />
</Frame>

Before proceeding to the next step, you’ll want to start the simulation in the Smartcar Dashboard.

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim5.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=62c9900a88d6027f0ef2c623aaf59729" data-og-width="1468" width="1468" data-og-height="646" height="646" data-path="images/help-center/guide-postman/sim5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim5.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=255690782e946ed2eb4b29788cca8f65 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim5.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=a28d37c35bc257f50c5da645efc968ae 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim5.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=e612df7a4fce464843c5cf89dcc4a51c 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim5.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=b8f37558d09cacbc68e9fab162f46bf4 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim5.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=2b83b12949a032b4fa074e0533c3518e 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim5.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=0a3a3318474af0d9f8a964f97f862e39 2500w" />
</Frame>

## Connecting to a vehicle

If configured correctly, when you click **Get New Access Token** in Postman, you should see the first screen of the Connect flow.

<Tip>
  Before hitting Continue, make sure to select a country from the dropdown appropriate to the region you selected for your simulated vehicle.
</Tip>

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect1.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4eac302ec3adec5e4bd844218b1e8c02" data-og-width="2000" width="2000" data-og-height="2490" height="2490" data-path="images/help-center/guide-postman/connect1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect1.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=b33c86b9a49200aca03b0b2268d56b30 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect1.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=851cfdcc84cca6418304adc05ba75bb6 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect1.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=818c4993a577ac3d44da91d638faaf00 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect1.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=1dcb7d05948fd0a2c6fcd28b65377804 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect1.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=89a567a8b88bcf023347fbad04fa4f65 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect1.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=54f5cb846fd240db594de5887e8b6c05 2500w" />
</Frame>

Continue through the Connect flow, select the brand of your simulated vehicle and enter in the credentials you were issued for your simulated vehicle.
After accepting the permissions you’ll be met with the following screen:

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect2.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=b3fda47b60fb4b1d049769362b24b9fa" data-og-width="2000" width="2000" data-og-height="1171" height="1171" data-path="images/help-center/guide-postman/connect2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect2.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=bf14c4a7fa472feed32bf1653a186d0a 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect2.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f629985aa1b2096126648869f6ef10ff 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect2.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=14afb459a27975f25c8b75f93d9fbaa4 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect2.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=12638020d51f7f48c974e9a1432486ef 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect2.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ba92c7b42557535ece0de00caf6cbb05 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect2.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f9af66b4ba70192c5b3317caa2cc4ad1 2500w" />
</Frame>

Hit Use Token. You should see Access Token under Current Token populate with the access\_token from the popup. Using this access\_token you can make API requests to Smartcar's API.

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect3.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=71eef9cb9f7fffbe7015cb6110b6daa7" data-og-width="2000" width="2000" data-og-height="774" height="774" data-path="images/help-center/guide-postman/connect3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect3.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=228f2abc0f83ae37967465df1e0c118f 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect3.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=14c08260ce21d05fe6c79ecdcde6c0b5 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect3.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=603e838cee16606a98763739e3d8671a 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect3.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ce42d6b65d2fd760ee1e5006536ce3d2 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect3.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=37d944156781e88428fd65712a838156 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect3.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=9db774eaa2fa873059031b38b629e69b 2500w" />
</Frame>

<br />

<Warning>
  Access tokens are only valid for two hours. If you want to make API requests after it has expired, you'll need to generate a
  new one by stepping through the Connect Flow again, or through a [token refresh](/api-reference/authorization/refreshing-access-token).
</Warning>

## Making an API request

<Tip>
  Thanks to Postman, requests in the collection will inherit the `access_token` from the OAuth 2.0 Authorization flow we went through in the steps above.
</Tip>

In order to make API requests, we’ll need to first get a Smartcar `vehicle Id`. A `vehicle Id` is a unique identifier for a vehicle on Smartcar’s platform.

This can be done with the `All Vehicles` request. Making this request will assign the `vehicle Id` to the `{{vehicle_id}}` variable for other requests in the Collection.

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req1.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=1182006af59ffca20f826b396d7876c5" data-og-width="2000" width="2000" data-og-height="1186" height="1186" data-path="images/help-center/guide-postman/req1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req1.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e95dac20eef0635b4e16ca565d4d5922 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req1.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=1b4ed61974c72f06e6b5be4789dba84a 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req1.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=9d5aeae2a0334cfcca8bfbd8d1f6e1d1 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req1.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=a1d5f5a2c76f7f52c52fc25d5af49f82 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req1.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ebb64246814d3f35781c3beb5dd08094 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req1.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=091082c4b9e2057866598684824a1b65 2500w" />
</Frame>

<br />

Now that you've got a vehicle Id, you can make a request to other endpoints. Hitting Vehicle Info, we can see the MMY of the vehicle.

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req2.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c9b1d9dd016d9ef9674a84a368648db6" data-og-width="2000" width="2000" data-og-height="1105" height="1105" data-path="images/help-center/guide-postman/req2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req2.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=80472e786a7f26a6d730ad761ed69d5d 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req2.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c96f5f6aad6b8db7f8955d7107c6fa61 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req2.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=efa987df738bf5c5219f16dd288181e8 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req2.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4cc1084b30ed7130b2c28594072f0038 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req2.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=876da9b854b51b8144042e2c007050f1 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req2.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=5fd20e450288ea503841316a82260332 2500w" />
</Frame>

<br />

Checking `EV Battery Level`, we can see the response matches the vehicle state on the simulator

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req3.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=7230503ce005f2bde54dddfd00c5b58c" data-og-width="2000" width="2000" data-og-height="1036" height="1036" data-path="images/help-center/guide-postman/req3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req3.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e4b83819e252f452039d0c963953d541 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req3.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=6add9acb8b6f8a19ef1a75629eac75c1 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req3.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=309bdf161ba4d9ae74452493a1dbcec9 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req3.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=8241ba78505dbb0ee4c81aa4514e6e86 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req3.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=9b65f4395bf55177a09c69c9637a1ac5 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req3.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e7af67311b0bb31397e6d4e7b369ed3d 2500w" />
</Frame>

<br />

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/req4.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=5798556122aea8b0f4e20aa60d816b7e" data-og-width="2000" width="2000" data-og-height="1580" height="1580" data-path="images/help-center/guide-postman/req4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/req4.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=9a501a8002cb2d23f52a9619349a6fec 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/req4.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=1b9fd83b56957a7d55c5a20f119a4023 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/req4.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=7e8e19baf5e09e99e58bf528e8c6f2a2 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/req4.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=91ef1aed95e552fdeffccea38c4c82c1 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/req4.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=f0b411f53e83c5c7977de54cc874ec42 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/req4.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=ce529293fd334a85251146348945de84 2500w" />
</Frame>

<br />

## Troubleshooting

<AccordionGroup>
  <Accordion title="I’m getting an Invalid Credentials error in the Connect flow">
    * Check that you’re launching Connect in simulated mode
    * If you’re still running into an error make sure you’ve selected a country that matches the region you selected for your simulated vehicle.
  </Accordion>

  <Accordion title="I’m getting a 403 - Permission error on API requests">
    * Check that the vehicle you’ve created supports the endpoint. Select View Estimated Latencies to see a list of endpoints supported for the vehicle.
    * If you’re still running into the error, check that you’ve requested the appropriate permission in the scope parameter of the Connect URL.

    <Tip>
      You can always check the `/permissions` endpoint to see what endpoints you have access to.
    </Tip>
  </Accordion>
</AccordionGroup>
