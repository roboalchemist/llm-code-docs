# Source: https://docs.zapier.com/platform/build/troubleshoot-trigger-timeouts.md

# Troubleshoot trigger timeouts

## Testing trigger in Zap editor

### Constraint

When a user clicks **Test Trigger** in the Zap editor, the output of your `perform` (polling) or `performList` (REST Hook) must be returned within 30 seconds.

### Errors user will see if constraint is hit

* *“The app did not respond in-time. It may or may not have completed successfully.”*
* *“Problem creating Sample: Our computers ran into a problem”*
* *“We couldn't find any more x. Create a new x in your account and try again.”*

### Best practice

The Zap editor will only process three new records at a time for sample data, so one way of speeding up the response is by limiting returned results to three records when a trigger is tested.

To determine when the request is for sample data, use the bundle meta parameter `bundle.meta.isLoadingSample`. When that is set to `true`, the user is testing in the Zap editor, and your integration can respond with a limited payload. More on `bundle.meta` properties [here](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#bundlemeta).

## Trigger runs in a Zap

### Constraint

Each time a Zap executes, the trigger's `perform` method must finish processing in 30 seconds. Polling triggers run on an interval based on a [user's Zapier plan](https://zapier.com/pricing) (between 1 and 15 minutes). REST Hook triggers run on an inbound POST to their subscription URL.

### Errors user will see if constraint is hit

* User will receive an email with an error message, usually with *“Trigger partner failure”* in the message text. An example of the email sent when the trigger errors due to a timeout:
  <Frame>
    {" "}

    <img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0247e40bb198cd439e63cdfb6cc58bdb.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=58d5d7032cf2ec925770bcfaef679bde" data-og-width="761" width="761" data-og-height="377" height="377" data-path="images/0247e40bb198cd439e63cdfb6cc58bdb.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0247e40bb198cd439e63cdfb6cc58bdb.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=3e4ee08abc5a99b0820b180242d594e7 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0247e40bb198cd439e63cdfb6cc58bdb.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=fe3a124ad70a082e47dc12047a66d7b5 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0247e40bb198cd439e63cdfb6cc58bdb.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=c1f14fae0f8d8297ae0df2352fcee932 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0247e40bb198cd439e63cdfb6cc58bdb.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=1ed0e9b41d373d13a76ca081c11b48f2 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0247e40bb198cd439e63cdfb6cc58bdb.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=63d85afef2da78304181cd6455ec00e3 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0247e40bb198cd439e63cdfb6cc58bdb.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=4bac5be56102ce633757de704c463f83 2500w" />

    {" "}
  </Frame>

### Best practices

* For polling triggers, if your API endpoint supports request filtering around number of records or datetime, use these to reduce the number of records returned
* For both types of triggers, optimize the `perform` scripting for manipulating the payload
* Use [console logging](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#console-logging) efficiently. It can help you determine where issues might lie, but too much console logging can cause timeouts due to logging overhead.
* If you have multiple requests per record that are causing timeouts, use the Zapier platform [dehydration functions](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#dehydration). Instead of making the request immediately, a dehydration pointer is created, and the request will only be made if the Zap needs a hydrated property in a later step.

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
