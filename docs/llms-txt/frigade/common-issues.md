# Source: https://docs.frigade.com/sdk/common-issues.md

# Common Issues and Solutions

> Find solutions to common issues with the Frigade SDK.

---

## Flows not showing up
If your Frigade components are not rendering in your product as expected, below are some of thhe most common issues and solutions to help you troubleshoot.

<AccordionGroup>
    <Accordion title="Developer console">
        Open the developer console in your browser and look for any error messages.
    </Accordion>
    <Accordion title="API key">
        Make sure you have the correct API key in your `<Frigade.Provider />` component. You can find your API key in the [Frigade dashboard](https://app.frigade.com/developer).
    </Accordion>
    <Accordion title="Flow status">
        Make sure your Flows are properly installed in your app and that they are active in the Frigade dashboard. If you have not published your Flows, or if you have turned them off, they will not be available in your app.
    </Accordion>
    <Accordion title="Flow targeting">
        Make sure any targeting you've set in the **Targeting** tab of your Flow is correct. If the targeting is too restrictive, your Flows may not show up for the intended users.
    </Accordion>
    <Accordion title="Environment">
        Make sure you are using the correct environment in your `<Frigade.Provider />` component. Each environment has its own API key and Flows. If you are using the wrong environment, your Flows will not show up in your app.
    </Accordion>
    <Accordion title="Debug mode">
        If you are still having issues, you can enable debug mode in Chrome Devtools ([see guide](/guides/tours#debugging-tooltips)).
    </Accordion>
    <Accordion title="Ensure zIndex is set correctly">
        If your Flows are not showing up, it may be because they are being rendered behind other elements on the page. You can fix this by setting the `zIndex` on components such as `Frigade.Tour` or `Frigade.Announcement` to a higher value.
    </Accordion>
    <Accordion title="Rules">
        If you've created a rule in the **Rules** tab of Frigade that includes the Flow then that could affect its visibility. Make sure you've configured the rule correctly and that your Flow is actually expected to show.
    </Accordion>
</AccordionGroup>

---

## Guest users in my dashboard

If a `userId` is not available when Frigade is initialized via the `<Frigade.Provider />` and/or the JS SDK, Frigade will automatically assign a guest user id to the user. This is to ensure that the user can still be tracked and that their data is not lost.

To prevent Frigade from automatically generating guest user IDs, you can pass a flag to the `<Frigade.Provider />` as shown below:

```jsx
<Frigade.Provider generateGuestId={false} />
```

## Import error

If you into an error such as `Can't import the named export 'Anchor' from non EcmaScript module (only default export is available)`, it is likely that you are using an older version of create-react-app.

There are two ways to fix this issue:

1. Upgrade to the latest version of create-react-app (you need to be on version 5.0.0 or higher of `react-scripts`).
2. Eject your app from create-react-app (if not already done) and manually configure your webpack to support ESM. Do this by adding the following to your webpack config:

```javascript
module.exports = {
  //...
  resolve: {
    extensions: ['.mjs', '.js', '.json'],
    mainFields: ['module', 'main'],
  },
  rules: [
    ///...
    { test: /\.mjs$/, include: /node_modules/, type: 'javascript/auto' }
  ],
  //...
};
```

***

## Something else?

If you are still having trouble with Frigade, [get in touch](mailto:support@frigade.com) and we'll be happy to help.
