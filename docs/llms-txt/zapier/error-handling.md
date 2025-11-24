# Source: https://docs.zapier.com/platform/manage/error-handling.md

# Improve error response handling

> Errors from your API cause pain for users at two vital points:

* During the Zap setup process, stopping them from enabling and activating their Zaps
* During the Zap's runtime, once it has been turned on, preventing the Zap from completing all actions successfully

Zap runs that encounter an error response status code when making a request to your API throw an exception and receive the “Stopped / Errored” status. This will [display an error message to the user](https://help.zapier.com/hc/en-us/articles/20505304170637-Review-Zap-run-statuses) in their Zap History and they will be notified via email based on their [notification settings](https://help.zapier.com/hc/en-us/articles/8496289225229-Manage-notifications-when-errors-occur-in-Zaps).

Even if the `message` included in the response details an error, users should **never receive** a success/200 response if there was an error in the request as this will not show up as an error in the Zap history.

If [95% of a Zap's runs in the last 7 days are assigned the “Stopped / Errored” status](https://help.zapier.com/hc/en-us/articles/8496037690637-Troubleshoot-errors-in-Zapier#500-series-error-codes-0-3), the Zap will be automatically turned off. The Zap will not run again until the user manually enables it, so only return an error if the scenario is truly an error that needs to be fixed.

Monitor spikes in errors from the the *Monitoring* page in the Platform UI as leading indicators of problems users are facing within your integration.

The more descriptive and thorough [error handling](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#error-handling) your API and integration have in place, the easier it will be for users to resolve their own issues and for Zapier's support team to assist with debugging.

If you don't have control to make changes to the API itself, utilize custom error handling to improve your error messages:

* Elaborate on briefly worded errors with user-friendly messaging.
* When writing user-facing error messages however, keep the message below 250 characters total as Zapier truncates errors from integrations at 250 characters when displaying them to users.
* Update “not\_authenticated” to “Your API Key is invalid. Please reconnect your account.”
* Surface specific information to users regarding the field and why it's producing an error. This empowers users to fix Zap issues independently.
* Instead of “Provided data is invalid”, return “Contact name is invalid”.
* Improve “Contact name is invalid” with “Contact name exceeds character limit.”
* Format the error to include a second, optional argument code machines can use to identify the type of error, and last, optional argument of a HTTP status code. `throw new z.errors.Error('Contact name exceeds character limit.', 'InvalidData', 400);`

Your app integration can use custom code to improve the user experience in Zapier by returning a user-friendly message and optional error and status code. Typically, this will be prettifying 4xx responses or APIs that return errors as 200s with a payload that describes the error. The code and status is used by Zapier to provide relevant troubleshooting to the user when communicating the error.

## Prerequisites

* Documentation for the API you're working with that includes the response status codes per endpoint
* Familiarity with [general error handling in Zapier](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#general-errors).

## 1. Custom errors in Platform CLI

Switching to the [Platform CLI](/platform/manage/export-cli), allows you to [make use of HTTP middleware](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#using-http-middleware) to implement any [custom error response handling](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#error-response-handling).

This will allow you to write a single script that applies across the entire integration to detect a specific error from the API, and show the relevant message to the user within Zapier.

## 2. Custom errors in Platform UI

When you build and maintain your app in the UI, custom error handling can still be implemented. The main difference is that you'll need to add it to each individual element of the integration (triggers, actions, searches, authentication) that could encounter the error.

In the UI, `skipThrowForStatus` is set from the [Advanced tab](/platform/build/errors). This allows for custom error handling for status codes above 400. Note that 401 status codes will throw a `RefreshAuthError` [regardless](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#user-content-error-response-handling).

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8cafa443c6e5844d6881f2690e4f34c5.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=acd34d15af28dc49d78a67346dfcdb01" data-og-width="1936" width="1936" data-og-height="560" height="560" data-path="images/8cafa443c6e5844d6881f2690e4f34c5.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8cafa443c6e5844d6881f2690e4f34c5.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=c3bfa8c5a934b900e67ad36b6c735830 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8cafa443c6e5844d6881f2690e4f34c5.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=0da66fc6b18bf35ba30fc626585b9633 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8cafa443c6e5844d6881f2690e4f34c5.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=d69fed3862dd26668922a904eb2f3422 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8cafa443c6e5844d6881f2690e4f34c5.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=2009bdc547e42035dd710080c94c2282 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8cafa443c6e5844d6881f2690e4f34c5.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=fd834639612ab443971cce9afb074e7d 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8cafa443c6e5844d6881f2690e4f34c5.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=8b98f7475d21a33f97a1704e98291269 2500w" />
</Frame>

Once set, you can add [error handling](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#general-errors) when in Code Mode within the API Configuration for each trigger/action/search.

```js  theme={null}
return z.request(options).then((response) => {
  if (response.status === 404) {
    throw new z.errors.Error(
      "An error was returned. Help!",
      "InvalidData",
      404,
    );
  }
  return response.json;
});
```

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/9553266cb5a5ab7804d3f9ac1a9eed60.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=b285f7641f30a2f81d132c906407fcd2" data-og-width="1028" width="1028" data-og-height="169" height="169" data-path="images/9553266cb5a5ab7804d3f9ac1a9eed60.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/9553266cb5a5ab7804d3f9ac1a9eed60.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=ab42d5913795cfa392418016121225eb 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/9553266cb5a5ab7804d3f9ac1a9eed60.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=8ba9c4f4f1f960550960258a3a7aa5b9 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/9553266cb5a5ab7804d3f9ac1a9eed60.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=b2721e95ec64372b32be8b6352353a06 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/9553266cb5a5ab7804d3f9ac1a9eed60.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=17ab4af6f3cac8ea0121753f248dc3b4 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/9553266cb5a5ab7804d3f9ac1a9eed60.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=784b41a2901df8e27e91c2ab21763825 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/9553266cb5a5ab7804d3f9ac1a9eed60.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=963e0c05bd4e8aed027069e050be5964 2500w" />
</Frame>

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
