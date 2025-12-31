# Source: https://smartcar.com/docs/connect/what-is-connect.md

# What is Connect?

Smartcar Connect is the fastest and most transparent way to collect user consent. Before you can make API requests to a car, your customer needs to link the vehicle to your app. It’s a simple process for your users to enroll their vehicles:

1. Select the car brand
2. Sign in
3. Give consent

<Frame caption="Default Smartcar Connect Flow">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c2cd906b5876221be223249b7ba0c8ef" data-og-width="3782" width="3782" data-og-height="1942" height="1942" data-path="images/default-connect-flow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=57674aaf78d5e84ec7acf3a3e987101d 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=3009ebe305a4b1cbe0559c525f3b8bde 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=2d05dffc04980fbac98e83da00a09218 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4c7f94b577ddffff375afe841fe094b5 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=dc9a2de37a38d85955d176e3eea6a968 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=bfc194d9d2adabe6d5b0d2478dbe5954 2500w" />
</Frame>

From your app, you'll [redirect your users to Connect](/connect/redirect-to-connect), and [handle the response](/connect/handle-the-response) once the user completes or exits the Connect flow. You'll receive a `code` that you'll use to [exchange](/api-reference/authorization/auth-code-exchange) for an access token to start making requests to their vehicle(s).

We have designed Connect in compliance with the OAuth2 authorization protocol, safely handling all user information.

Connect comes with robust configurations to fit your needs and frontend [SDKs](/connect/connect-sdks) for faster integration.
