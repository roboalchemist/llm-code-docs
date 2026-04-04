# Source: https://docs.zapier.com/platform/build/test-monitoring.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Test and monitor your integration in your Zapier account

> Testing inside the Platform UI is crucial during the building process. To ensure users can benefit from your integration's features, it is equally crucial to test your integration within the Zap editor. This is the best way to notice details that might have been overlooked while building your integration.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4f69910e7b7d5fb9325d0e36579bca5a.webp?fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=101500de5caeeacb04e6357280080ef7" data-og-width="1189" width="1189" data-og-height="880" height="880" data-path="images/4f69910e7b7d5fb9325d0e36579bca5a.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4f69910e7b7d5fb9325d0e36579bca5a.webp?w=280&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=267ed1b10ca39372c3c0d3f4031bf84b 280w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4f69910e7b7d5fb9325d0e36579bca5a.webp?w=560&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=501f7db68980f91ce21cf153235dc570 560w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4f69910e7b7d5fb9325d0e36579bca5a.webp?w=840&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=1b66c09cc2de6b761926adf2bc34db73 840w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4f69910e7b7d5fb9325d0e36579bca5a.webp?w=1100&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=902618734b2e309b310f8ee31822881a 1100w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4f69910e7b7d5fb9325d0e36579bca5a.webp?w=1650&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=d276bd4bef100eb3a52ca2c641e86b6b 1650w, https://mintcdn.com/zapier-82f0e938/88BoWUuO1MROWn5-/images/4f69910e7b7d5fb9325d0e36579bca5a.webp?w=2500&fit=max&auto=format&n=88BoWUuO1MROWn5-&q=85&s=b7697611956009de6b5634485435c333 2500w" />
</Frame>

## Prerequisites

* Completed build of your Zapier integration
* A [Zapier account](https://zapier.com/sign-up)
* If you haven't used Zapier before, you'll want to learn the basics in our [Zapier Getting Started Guide](https://zapier.com/learn/zapier-quick-start-guide/).
* Set of valid user credentials for your app - recommended to use a new account specifically for testing so you don't clutter your core app account with testing data.

## Steps

1. Create a Zap in the [Zap editor](https://zapier.com/app/editor/), selecting your app in the *Choose App* selector.

2. Your integration will show the name and logo set in *Integration Settings*, along with the integration's current version number and a *By Invite* tag. If your integration is a new version of an existing *Public* integration, look for the *Latest* tag, the latest version number and the *By Invite* tag to differentiate from existing, public integrations.

3. Check each of the following as you setup Zaps:
   * **Authentication**: Does your app account successfully connect? Zapier will show any testing accounts you already added, but try adding a new account here for a complete test. To remove connected accounts, you can delete connections from [Apps/Custom integrations](/images/c97ff65c5857c3ebfeb302ffa8454867.webp).
   * **Connection Label**: Does the Zap editor show the [expected connection label](/images/693c0b1c08dabf06ea515995eab636aa.webp) on the new account, with the info you set when building your integration?
   * **Trigger and Action List**: Do you see every trigger and action included in your integration? Is each trigger and action's name and description accurate and grammatically correct?
   * **Fields**: Do triggers and actions show the input fields you expect? Are their names and labels accurate and grammatically correct? Do any links or formatting in descriptions work correctly? Do drop-down fields or those with multiple selectors work correctly?
   * **Output**: When you run a Zap trigger or action's test, does the step return the fields and data you expect in the correct format? Do triggers show the most recently added item from your app, and do searches return appropriate results?
   * **Input**: Open your app, and check each item that Zapier actions added or updated for the correct format and expected appearance in your app.
   * **Automation**: Turn on Zaps with each of your integration's triggers and actions. Do they run correctly when the data they watch for is added or updated in your app? You can check your [Zap History](https://zapier.com/app/history) to make sure Zaps ran as expected for triggering events. Do your integration's actions successfully add and update items when those Zaps are triggered?

## Monitoring

Use the *Monitoring* page in the Platform UI to ensure that test Zaps and the expected requests are running without errors. Every request made to your API by your Zapier integration is shown.

Adjust the Chart Filter for the correct timeframe, then click on any data point in the chart to see the any error messages and logs which should help you troubleshoot further. You can also filter by log type and by user email.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8e7113b876e9dd37b71722fee763cf3e.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=812b72748738bea86528b4618d7c30f5" data-og-width="1487" width="1487" data-og-height="621" height="621" data-path="images/8e7113b876e9dd37b71722fee763cf3e.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8e7113b876e9dd37b71722fee763cf3e.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=2091c0df0e4ccc5e97dfed331f443999 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8e7113b876e9dd37b71722fee763cf3e.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=082a906757bd8d9cdff54fd54ae59fd3 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8e7113b876e9dd37b71722fee763cf3e.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=f71551a7e49f2df2d6b3f20ff7a9f88a 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8e7113b876e9dd37b71722fee763cf3e.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=9ea4c52be9060a71f80dc9f7ea516c1f 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8e7113b876e9dd37b71722fee763cf3e.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=3e34022990f4ce32288677c7c1c9898a 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/8e7113b876e9dd37b71722fee763cf3e.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=b1ed4008d4c2fd76dce03d0d083b6b23 2500w" />
</Frame>

To manually print a log statement you can see in Monitoring, use `z.console.log` in Code Mode:

`z.console.log('Here are the input fields', bundle.inputData);`

You can also refer to this video on using the Monitoring tool:

<video controls src="https://cdn.zappy.app/4f1d37c1ff6cb690c3ff9c9fa6afe701.mp4" />

## User testing

Have internal team members and/or beta users test your integration. If you are going to submit your app for *Publishing* in the Zapier App Directory, you'll need at least 3 users with live Zaps. Each additional tester helps ensure that your app doesn't ship with usability problems or bugs.

Internal team members can be invited from *[Manage Team](/platform/manage/add-team)* as admins or collaborators.

Beta users external to your organization can be invited from *[Sharing](/platform/manage/sharing)*

The *Insights* section in the Platform UI provides usage statistics by trigger and action.

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
