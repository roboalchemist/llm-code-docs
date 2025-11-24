# Source: https://docs.zapier.com/platform/build/hook-trigger.md

# Add a REST Hook trigger

> Set up your REST Hook trigger in the Platform UI with the Settings, Input Designer and API Configuration tabs.

## Prerequisites

* Your app supports REST Hooks - webhook subscriptions that can be manipulated through a REST API.
* An endpoint/s to set up and remove the hook subscription exists for Zapier to send Subscribe and Unsubscribe API requests to with a unique subscription URL, the`bundle.targetUrl`, for each active Zap.
* A separate endpoint exists that returns a list of sample items that would be expected to trigger the user's Zap. This is optional for apps remaining private and ***required*** for public apps.
* If your webhook subscriptions expire, make sure the subscribe endpoint returns an `expiration_date` property containing an ISO8601 date. The platform will automatically attempt to resubscribe after the expiration date.

## 1. Add the trigger settings

* Open the *Triggers* tab in Zapier's Platform UI and select **Add Trigger**.
* On the Settings page, specify the following:

– **Key**: A unique identifier for this trigger to be referenced inside Zapier. This is not shown to users. This cannot be edited once saved.

– **Name**: A human-friendly name for this trigger, typically with an adjective such as *New or Updated* followed by the name of the item that the trigger watches for inside your app. The title-case name is shown inside the Zap editor and on Zapier's app directory marketing pages.

– **Noun**: A single noun that describes what this trigger watches for, used by Zapier to auto-generate text in Zaps about your trigger.

– **Description**: A plain text sentence that describes what the trigger does and when it should be used. Shown inside the Zap editor and on Zapier's app directory marketing pages. Starts with the phrase “Triggers when”.

– **Visibility in Editor**: An option to select when this trigger will be shown. *Shown* is chosen by default. Choose `Hidden` if this trigger should not be shown to users.`Hidden` is usually selected when the trigger is not ready to be used in the integration, or for polling triggers that power [dynamic dropdown](/platform/build/add-fields#dynamic-dropdown) fields.

– **Directions** is used for static webhooks only to describe how and where to copy-paste the static webhook URL for the trigger within your app. **Directions** will not show to users in other cases. Static webhooks are not permitted in public integrations.

* Click on the **Save and continue** button.

## 2. Complete the Input Designer

On the Input Designer page, add user [input fields](/platform/build/add-fields) needed by your API to watch for the triggering item.

Trigger input fields allow users to enter filters, tags, and other details to filter through new or updated data at the endpoint.

If no input data is needed for this trigger's endpoint, continue.

## 3. Set up the API Configuration

On the API Configuration page, select **REST Hook** as the trigger type, and complete each section.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0368aeae12e11ec59688d10a7ef69d8c.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=940424284f026fcc0e37d7aedf2f9187" data-og-width="1500" width="1500" data-og-height="1505" height="1505" data-path="images/0368aeae12e11ec59688d10a7ef69d8c.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0368aeae12e11ec59688d10a7ef69d8c.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=b891d9a2e983f1f619f7ee093e1dd836 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0368aeae12e11ec59688d10a7ef69d8c.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=1d7098b77ba72fa374c9f54ed63102bb 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0368aeae12e11ec59688d10a7ef69d8c.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=a6f4b47f4e58eb8ff1ede8bafa306fcb 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0368aeae12e11ec59688d10a7ef69d8c.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=8008a79d349dfdc67f4bf508d3921b31 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0368aeae12e11ec59688d10a7ef69d8c.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=f2f8492a12171fae81f03644ddd6a82e 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0368aeae12e11ec59688d10a7ef69d8c.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=849d4297f27ad7920ea91922173afc68 2500w" />
</Frame>

REST Hook triggers are marked as *Instant* [in the Zap editor](/images/f510859bf90c0e341bc94997a75f9626.webp).

### Subscribe

This request, usually a POST, is performed when a user activates a Zap that starts with this REST Hook trigger. This is how a Zap makes a subscription request to your API to be notified (via webhook) of all trigger events with the given parameters going forward.

The subscribe request is **only** made when a Zap is turned on for the first time, or if an active Zap is paused and then unpaused. Note that [publishing a new Draft](https://help.zapier.com/hc/en-us/articles/8496260938125-Create-drafts-of-your-Zaps) would not always mean pausing/unpausing a Zap. Only if a new trigger subscription is required, would a new subscribe request be made. In cases of remapping action step fields (from existing trigger data), this doesn't require any change to the trigger itself as a datasource, so a new subscribe request would **not** be made when that Draft was published.

Click on the *Show Options* dropdown to add data to the Request Body or HTTP Headers that are needed by your API for a successful subscription. Note that you'll need to make sure the keys here match what your API expects.

Zapier includes a `targetUrl` when making this request. You need to store the targetUrl, usually in a database, and you'd typically associate it with an id. Return that id in the response back to Zapier to be used later in the Unsubscribe.

Your app's event system would determine which stored subscriptions should be invoked when an event occurs in your app, posting to the corresponding stored `targetUrl`.

The webhook URL can be accessed via `{{bundle.targetUrl}}`.

For example, for Gitlab's API `url` is used as the key for the `{{bundle.targetUrl}}` value that contains the webhook URL to send data to.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8b7941e3092850bd7edf331cb78b5659.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=873391e85be79eeb5d2725bf4db864b1" data-og-width="958" width="958" data-og-height="592" height="592" data-path="images/8b7941e3092850bd7edf331cb78b5659.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8b7941e3092850bd7edf331cb78b5659.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=2d2f1a04d864504af5ecd9eca965d1b5 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8b7941e3092850bd7edf331cb78b5659.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=eeada93d272d2bf8696c9c910093f65c 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8b7941e3092850bd7edf331cb78b5659.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=af7e5b3cdcfb314c43c028a12205ec31 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8b7941e3092850bd7edf331cb78b5659.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=978f2db4a0799f104e5fc7948d387f09 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8b7941e3092850bd7edf331cb78b5659.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=85f517782c506deec47b27100a798767 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8b7941e3092850bd7edf331cb78b5659.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=b24567ec3c0ff565f290c58fd618a65d 2500w" />
</Frame>

If you need to customize the subscription request, select *Switch to Code Mode* and [write custom JavaScript code](/platform/build/code-mode) to handle the API call and the response parsing as needed.

It is recommended that a successful Subscribe response return a 201 status code. The data returned with the response should include any data needed to later the Unsubscribe request. This data will be stored in `bundle.subscribeData`.

### Unsubscribe

This request, usually a DELETE, is how Zapier notifies your API when it is no longer listening for trigger events, when the Zap is deactivated or deleted. If your API continues posting notification payloads to the Zap after it has unsubscribed, you can expect to see a 410 response from Zapier.

Click on the *Show Options* dropdown to add data to the Request Body or HTTP Headers that is needed by your API for a successful unsubscription. Note that you'll need to make sure the keys here match what your API expects. When Zapier sends the request to your API to unsubscribe the webhook, it can reference any data that was returned from your API during the Subscribe request and was stored in `bundle.subscribeData`.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/44615176b56966a90101067d719b09ad.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=749c4aed694f4a7e0ad171a2060659e6" data-og-width="960" width="960" data-og-height="277" height="277" data-path="images/44615176b56966a90101067d719b09ad.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/44615176b56966a90101067d719b09ad.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=db501884843f1099faf828e9f7e7973f 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/44615176b56966a90101067d719b09ad.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=c6872ec56b8d1af0bbb1b005fe514ac0 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/44615176b56966a90101067d719b09ad.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=2d85c1c774b66b3986198f52184d3e8b 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/44615176b56966a90101067d719b09ad.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=c38fad78f22b2139aa8661fd40dcc9e0 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/44615176b56966a90101067d719b09ad.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=feebb38f96f652c6cdf16c960199de82 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/44615176b56966a90101067d719b09ad.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=56a89e0b0222f38aa19c1fd83837f58e 2500w" />
</Frame>

A REST Hook trigger missing a Subscribe or Unsubscribe endpoint, is presented to users as a [Static Webhook](/images/3b35908a6a0c232087b5da807cf9d6fb.webp). Static hooks are [not supported in public integrations](/platform/publish/integration-checks-reference#d017---static-hook-is-discouraged), but they could be used if the integration intends to remain private.

### Perform List

This request, usually a GET, is used to collect sample data in the Zap editor, typically prior to a Zap's activation. This will be used to fetch sample data when users are testing the trigger and mapping fields to their Zap's subsequent steps. Though optional, not defining a Perform List is a sub-optimal experience for users and is [required for public apps](/platform/quickstart/private-vs-public-integrations).

Most commonly this is a GET request to an endpoint of your API which will provide a response with the exact same schema as the data delivered via webhook when a trigger event happens.

Response data returned must be an array, even if the array contains only one object. It must have the exact same schema as the data delivered via webhook when a trigger event happens otherwise fields mapped from this sample in subsequent steps of a Zap will break when it runs live.

### Perform

The Perform function is called each time your app delivers a notification payload to Zapier. Use custom code to parse the webhook payload and modify it as required before returning it to the Zap as trigger data.

The data returned by the perform must be an array. By default, Zapier includes `return [bundle.cleanedRequest]` to return the data from the webhook as an array. If the data needs to be transformed, or includes multiple objects, you can add custom code to parse the response data in `bundle.cleanedRequest` within the Perform into an array of objects.

If your webhook already provides an array, you can remove the wrapping array and simply `return bundle.cleanedRequest`.

If, for architectural reasons, your webhook will receive some data that shouldn't trigger the Zap, include code for the Perform function to return an empty array in those cases, so the Zap won't run.

For data sent to Zapier via REST Hook, most requests will be successful and return a 200 status code with some request-tracking data. This indicates that Zapier has accepted the data, but it is still possible for errors to occur within the Zap if the structure of the provided data is unexpected.

### Best practices when sending data to a REST Hook trigger

* Be mindful of Zapier's [rate limits](https://zapier.com/help/troubleshoot/behavior/rate-limits-and-throttling-in-zapier#step-4).
* If your app receives a 410 response, that webhook subscription is no longer active, and you should stop sending data to it.
* If your app receives repeated 4xx or 5xx failures from Zapier outside those error types, this can be handled at your discretion. You may choose to try again later, or to stop sending data and deactivate the hook.
* To signal that your app has deactivated the hook for any reason, you can optionally send a *reverse unsubscribe* call to Zapier. This can allow users to manage their subscriptions from inside your app, or permit you to clean up after a user deletes their account or revokes credentials. The request should be of the form `DELETE <target_url>`, where `target_url` is the unique target URL that was provided when the subscription was created. This will pause the Zap within Zapier.

Once you've configured all the endpoints, click *Save API Request & Continue*

## 4. Test your API request

To test the REST Hook trigger, [build a Zap in the editor](/platform/build/test-triggers-actions).

## 5. Define your output

Define sample data and output fields following [the guide](/platform/build/sample-data).

## Video Tutorial

You can refer to this video on REST Hook triggers:

<video controls src="https://cdn.zappy.app/b8511ab881f3ad50a9465a1732501cf8.mp4" />

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
