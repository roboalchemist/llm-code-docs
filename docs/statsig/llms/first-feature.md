# Source: https://docs.statsig.com/guides/first-feature.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Build Your First Feature

> Walk through creating a feature gate, targeting audiences, and rolling out your first feature with the JavaScript SDK.

<Info title="Feature gates vs feature flags">
  Statsig refers to feature flags as <em>feature gates</em> across the console and SDKs. The terms are interchangeable throughout this guide.
</Info>

Once your Statsig account is ready, follow the steps below to create and test-drive a new feature gate.

<Steps>
  <Step title="Create a feature gate">
    Navigate to the [Feature Gates page](https://console.statsig.com/gates) and click <strong>Get Started</strong> (or <strong>Create</strong> if you already have gates).

    <Frame>
      <img src="https://mintcdn.com/statsig-4b2ff144/UTM4uy5tPUmUPfUG/images/guides/first-feature/feature-gates-page.png?fit=max&auto=format&n=UTM4uy5tPUmUPfUG&q=85&s=e414e05faabe9a075672b86368998f53" alt="Feature Gates page with Create button" width="797" height="481" data-path="images/guides/first-feature/feature-gates-page.png" />
    </Frame>

    Give the gate a clear name and description—for example, <code>Mobile Registration</code> with a note about the new mobile sign-up flow.
  </Step>

  <Step title="Target mobile platforms">
    New gates default to returning <code>false</code> until you add targeting. Click <strong>Add New Rule</strong>, choose <strong>Operating System → Any of</strong>, and select <strong>Android</strong> and <strong>iOS</strong>. Set the pass percentage to 100% and click <strong>Add Rule</strong>, then <strong>Save</strong>.

    <Frame>
      <img src="https://mintcdn.com/statsig-4b2ff144/UTM4uy5tPUmUPfUG/images/guides/first-feature/add-rule.png?fit=max&auto=format&n=UTM4uy5tPUmUPfUG&q=85&s=b50a6e886c061de3157be45215cf225e" alt="Adding a mobile targeting rule" width="536" height="582" data-path="images/guides/first-feature/add-rule.png" />
    </Frame>
  </Step>

  <Step title="Add an internal testing rule">
    Layer on a second rule for your team—for example <strong>Email → Contains any of</strong> with your company domain—so employees can exercise the feature regardless of device.

    <Frame>
      <img src="https://mintcdn.com/statsig-4b2ff144/UTM4uy5tPUmUPfUG/images/guides/first-feature/gate-rules.png?fit=max&auto=format&n=UTM4uy5tPUmUPfUG&q=85&s=2f2241e766ee02b5e277933793f389d4" alt="Gate with mobile and email rules" width="1550" height="691" data-path="images/guides/first-feature/gate-rules.png" />
    </Frame>
  </Step>

  <Step title="Generate a client API key">
    Head to [Project Settings → API Keys](https://console.statsig.com/api_keys) and copy the <strong>Client API key</strong>. Keep server secret keys on backends only, and use console API keys for programmatic configuration work.
  </Step>

  <Step title="Load the JavaScript SDK">
    <Tip title="Prefer a different SDK?">
      Statsig supports many platforms—see [Client SDK options](/sdks/getting-started) for alternatives. This walkthrough uses the browser SDK so you can experiment directly in DevTools.
    </Tip>

    Paste the snippet below into the browser console on any site to fetch the SDK from jsDelivr:

    ```js  theme={null}
    const script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/@statsig/js-client@3/build/statsig-js-client+session-replay+web-analytics.min.js';
    document.head.appendChild(script);
    ```

    <Frame>
      <img src="https://mintcdn.com/statsig-4b2ff144/UTM4uy5tPUmUPfUG/images/guides/first-feature/add-sdk-script.png?fit=max&auto=format&n=UTM4uy5tPUmUPfUG&q=85&s=cbcb94e2eee73c65f79ed0f9a61a5765" alt="Injecting the SDK via DevTools" width="888" height="264" data-path="images/guides/first-feature/add-sdk-script.png" />
    </Frame>
  </Step>

  <Step title="Initialize and check the gate">
    Replace <code>YOUR\_SDK\_KEY</code> with the client key from Step 4 and run:

    ```js  theme={null}
    const client = new window.Statsig.StatsigClient('YOUR_SDK_KEY', {});
    await client.initializeAsync();
    ```

    Then call:

    ```js  theme={null}
    client.checkGate('mobile_registration');
    ```

    You should see <code>false</code> because the current session is not mobile and doesn’t use the employee email domain.
  </Step>

  <Step title="Simulate a mobile environment">
    Enable the mobile device toolbar in Chrome DevTools.

    <Frame>
      <img src="https://mintcdn.com/statsig-4b2ff144/UTM4uy5tPUmUPfUG/images/guides/first-feature/devtools-mobile-toolbar.png?fit=max&auto=format&n=UTM4uy5tPUmUPfUG&q=85&s=3eeeabefdb0d3113c82ffe6bda508ad2" alt="Chrome DevTools mobile device toolbar icon" width="108" height="71" data-path="images/guides/first-feature/devtools-mobile-toolbar.png" />
    </Frame>

    Re-evaluate the user to pick up the new environment and re-check the gate:

    ```js  theme={null}
    await client.updateUserAsync({});
    client.checkGate('mobile_registration');
    ```

    The gate should now return <code>true</code> for the mobile profile.

    <Frame>
      <img src="https://mintcdn.com/statsig-4b2ff144/UTM4uy5tPUmUPfUG/images/guides/first-feature/mobile-rule-true.png?fit=max&auto=format&n=UTM4uy5tPUmUPfUG&q=85&s=b267363f47aa5204ec437fc7f9a353ae" alt="Gate returning true for mobile rule" width="893" height="137" data-path="images/guides/first-feature/mobile-rule-true.png" />
    </Frame>
  </Step>

  <Step title="Test the employee backdoor">
    Switch DevTools back to the desktop view and update the user with a company email:

    ```js  theme={null}
    await client.updateUserAsync({ email: 'teammate@statsig.com' });
    client.checkGate('mobile_registration');
    ```

    The gate passes again thanks to the email rule.

    <Frame>
      <img src="https://mintcdn.com/statsig-4b2ff144/UTM4uy5tPUmUPfUG/images/guides/first-feature/email-rule-true.png?fit=max&auto=format&n=UTM4uy5tPUmUPfUG&q=85&s=402cd4e96c44adc450f6ba08497062a7" alt="Gate returning true via email rule" width="879" height="153" data-path="images/guides/first-feature/email-rule-true.png" />
    </Frame>
  </Step>

  <Step title="Flush exposures and inspect diagnostics">
    ```js  theme={null}
    client.flush();
    ```

    Open the gate’s <strong>Diagnostics</strong> tab to confirm each exposure, including the failing desktop check, mobile pass, and employee pass.

    <Frame>
      <img src="https://mintcdn.com/statsig-4b2ff144/UTM4uy5tPUmUPfUG/images/guides/first-feature/diagnostics-stream.png?fit=max&auto=format&n=UTM4uy5tPUmUPfUG&q=85&s=1563c6c80fd50a4bf3f64f5111538586" alt="Diagnostics exposure stream showing recent checks" width="1578" height="732" data-path="images/guides/first-feature/diagnostics-stream.png" />
    </Frame>
  </Step>
</Steps>

## Use the gate in production

Wrap feature logic in a gate check so only targeted users see the experience:

```js  theme={null}
if (client.checkGate('mobile_registration')) {
  show(mobileRegistrationPage);
} else {
  show(oldRegistrationPage);
}
```

Happy feature gating!


Built with [Mintlify](https://mintlify.com).