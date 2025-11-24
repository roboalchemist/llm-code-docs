# Source: https://docs.zapier.com/platform/build/code-mode.md

# Use Code Mode to refine your API call

<Frame><img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1fa2f12c1c41a49f3d7aeff4d2706f7c.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=9b7cee390540952e249074b3491a152d" alt="" data-og-width="931" width="931" data-og-height="472" height="472" data-path="images/1fa2f12c1c41a49f3d7aeff4d2706f7c.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1fa2f12c1c41a49f3d7aeff4d2706f7c.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=b476565cc36bb5074b8858fc046237f1 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1fa2f12c1c41a49f3d7aeff4d2706f7c.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=636b7e79d0b016b41158f5a4f55fab6a 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1fa2f12c1c41a49f3d7aeff4d2706f7c.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=26396bd5d60775e2652bb8951b8739c3 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1fa2f12c1c41a49f3d7aeff4d2706f7c.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=28f14c577100092e0a6cefdbf3899150 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1fa2f12c1c41a49f3d7aeff4d2706f7c.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=8d9c3da67b794e1ebd3f361d1dd998c2 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/1fa2f12c1c41a49f3d7aeff4d2706f7c.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=b6cafa48352f9982eda88d5cc316b0c1 2500w" /></Frame>

In the Platform UI, when building your authentication, triggers and actions, you will create each component of your integration using Form Mode. However if you need to add further customization to your API calls, you can use Code Mode.

You can use Code Mode to:

* Transform your API response into JSON format
* Add user authentication details and input form data to the API call
* Use ‘z' object library to customize your API call
* Improve error response handling

## Getting started with Code Mode

To use Code Mode, Zapier recommends for users to have an understanding of Javascript and making [HTTP requests](/platform/reference/cli-docs#making-http-requests).

Code Mode is available to use in the API request settings:

* For authentications, Code Mode is in the *Configure a Test Request & Connection Label* setting. Note, for OAuth v2, Code Mode is in the *OAuth v2 Endpoint Configuration* setting.
* For triggers and actions, Code Mode is in the *API Configuration* setting.

<Frame><img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/554f0c395459b37fd34312566feac891.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=b770c78ccbc78049e03cfb20ad9eb434" alt="" data-og-width="932" width="932" data-og-height="566" height="566" data-path="images/554f0c395459b37fd34312566feac891.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/554f0c395459b37fd34312566feac891.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=802b5fcd220ab652ba3c69e280377733 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/554f0c395459b37fd34312566feac891.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=a2d19cd86d9e2075963db7c87b19708c 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/554f0c395459b37fd34312566feac891.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=7323a11e3baf083fd61c44f564f742d8 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/554f0c395459b37fd34312566feac891.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=d05145c65dbbf8a3a7f27ee84ea68d76 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/554f0c395459b37fd34312566feac891.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=345d1b142cf3a0365132982d9f7947f7 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/554f0c395459b37fd34312566feac891.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=2752da071fb1803b29299727df9d8da4 2500w" /></Frame>

Changes made in Code Mode are not saved automatically. Once you have added the code you want, click **Save & Continue**.

## Capabilities of Code Mode

### Use `z` object to customize your API call

You can write JavaScript code, using Zapier's default code as a base or writing custom code. Use the `z` object for Zapier specific features, including `z.console` to write to the console log, `z.JSON` to parse JSON and `z.errors` to handle errors. Learn more in [Zapier's CLI Z Object docs](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md#z-object).

### Add user authentication details and input form data

You can use Zapier bundles to access authentication data, data from user input forms and request data. Learn more in [Zapier data bundles](https://platform.zapier.com/docs/advanced#bundle).

### Importing libraries

You can import from Node's standard library with `z.require`, for example, `z.require('querystring')` or `z.require('crypto')`. Zapier strongly recommend you keep it simple when coding in Platform UI. Building and testing complex code is better suited with the Platform CLI.

NPM modules are not supported within the Platform UI. You'd need to export your project to [Platform CLI](https://github.com/zapier/zapier-platform/blob/main/packages/cli/README.md) and use `npm` to add additional libraries.

### Performance considerations

Each trigger and action has a 30 second time limit. To ensure that Zaps run smoothly, keep your custom code as lightweight and efficient as possible. If your code takes longer than 30 seconds to run, it will time out and user's Zaps will error. We also can't guarantee that all imported libraries will be supported within our runtime environment.

Here are some specific things you can do to improve the performance of your custom code:

* Use efficient algorithms and data structures.
* Avoid unnecessary loops and recursions.
* Optimize your code for the specific task it is performing.
* Avoid using imported libraries that are not essential to triggers or actions.

### Error handling in Code Mode

When working in Code Mode, it's important to handle errors correctly so that Zapier can respond appropriately and ensure Zaps run as expected. While it might feel natural to throw a standard JavaScript `Error`, this will not work as expected in Zapier integrations. Instead, you should use the `z.error` error classes provided by the platform.

**Don't**

```javascript  theme={null}
if (response.status === 401) {
  throw new Error("Authentication failed. Please reconnect your account.");
}
```

**Do**

```javascript  theme={null}
if (response.status === 401) {
  throw new z.errors.RefreshAuthError();
}
```

Learn more in the [CLI Error Handling docs](https://docs.zapier.com/platform/build-cli/overview#error-handling).

## Switching between Form Mode to Code Mode

When you switch to Code Mode, Zapier uses your code when making API calls. Any previous settings from Form Mode will not be discarded. This is because Form Mode and Code Mode cannot be used together.

If you switch back to Form Mode, click **Switch to Form Mode**. Your previous Form Mode settings will be restored. Zapier will save the code you entered in Code Mode so you can use it again if you switch back to Code Mode.

## Code Mode resources

Here are some resources that will be helpful when using the code mode:

<CardGroup cols={3}>
  <Card title="HTTP Request Options" icon="gear" horizontal={false} href="https://docs.zapier.com/platform/build-cli/overview#http-request-options" />

  <Card title="HTTP Response Object" icon="file-code" horizontal={false} href="https://docs.zapier.com/platform/build-cli/overview#http-response-object" />

  <Card title="HTTP Requests" icon="server" horizontal={false} href="https://docs.zapier.com/platform/build-cli/overview#making-http-requests" />

  <Card title="Dynamic Dropdowns" icon="list" horizontal={false} href="https://docs.zapier.com/platform/build-cli/dynamic-dropdowns" />

  <Card title="Return Types" icon="code" horizontal={false} href="https://docs.zapier.com/platform/build-cli/overview#return-types" />

  <Card title="Bundle Object" icon="box" horizontal={false} href="https://docs.zapier.com/platform/build-cli/core#bundle-object" />

  <Card title="Environment Variables" icon="leaf" horizontal={false} href="https://docs.zapier.com/platform/build-cli/overview#defining-environment-variables" />

  <Card title="Placeholders vs Template Literals" icon="code" horizontal={false} href="https://docs.zapier.com/platform/build-cli/faqs#when-to-use-placeholders-or-curlies%3F" />

  <Card title="Error Handling" icon="triangle-exclamation" horizontal={false} href="https://docs.zapier.com/platform/build-cli/overview#error-handling" />

  <Card title="Error Response Handling" icon="bug" horizontal={false} href="https://docs.zapier.com/platform/build-cli/overview#error-response-handling" />

  <Card title="Schema Docs" icon="book" horizontal>
    [14.x](https://github.com/zapier/zapier-platform/blob/zapier-platform-schema@14.1.2/packages/schema/docs/build/schema.md)

    [13.x](https://github.com/zapier/zapier-platform/blob/zapier-platform-schema@13.0.0/packages/schema/docs/build/schema.md)
    [12.x](https://github.com/zapier/zapier-platform/blob/zapier-platform-schema%4012.2.1/packages/schema/docs/build/schema.md)
  </Card>
</CardGroup>

***

[*Need help? Tell us about your problem and we'll connect you with the right resource or contact support.*](https://developer.zapier.com/contact)
