# Source: https://docs.frigade.com/component/banner.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Banner

> Communicate information or drive action via in-line banners

<Frame className="h-96 items-center px-4">
  <img
    src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/banner.svg?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=85007c7bf1c50af98cb76411ff1256e3"
    style={{
    height: "auto",
  }}
    data-og-width="1000"
    width="1000"
    data-og-height="100"
    height="100"
    data-path="images/components/banner.svg"
    data-optimize="true"
    data-opv="3"
    srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/banner.svg?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=28087310105f6277a14b4ef167423363 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/banner.svg?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=b02de011f0cd469ccf6a2eb7304f7f8f 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/banner.svg?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=b77009cb787e78dfdaad5f49c0f31b21 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/banner.svg?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=691706e4786fb88c6539c6f2b734ce62 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/banner.svg?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=4e5781f625009647b9da7edfab7f40bc 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/banner.svg?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=01e0b610a723d20c9b46e130fe01da0e 2500w"
  />
</Frame>

## About this component

The `Banner` component is a versatile, persistent UI component that typically span the full width of a page or container, often at the top or bottom of the page. They serve as an unobtrusive way to communicate important information and promote additional offerings without disrupting the user’s workflow.

**When to use Banners:**

* **Alerts:** Ideal for notifying users about critical updates, such as free trial expirations or scheduled maintenance.
* **Lightweight Up-sells:** Effective for promoting related products or features, banners can be strategically targted and placed next to relevant content.

**Advantages of Banners:**

* **Non-Disruptive Communication:** Since banners remain visible without interrupting the user experience, they allow users to continue their tasks while still being informed.
* **Flexible Design Options:** Banners can be customized with full-bleed graphics and images, making them visually appealing and engaging. Frigade supports custom components including on-brand, eye-catching banners.

**Best Practices for Banners:**

* **Use Collections:** Leverage Collections to define reusable in-app UI channels, enabling teams to efficiently manage and launch banners across different pages, such as your product dashboard or a specific product pages.
* **Regulate Frequency:** Control the frequency of banner displays to ensure they remain relevant and engaging without overwhelming users.
* **Make Dismissible:** Most often, banners are easily dismissible for the best user expeirence. In select cases, banners may be non-dismissible to communicate a critical message for some time (e.g. product downtime).

## Resources

* Launch banners with no-code using custom [Collections](/platform/collections#inline-ui-components)
* Target your banner to specific users with [Targeting](/platform/targeting)
* See [industry examples](https://www.productonboarding.com/?type=banner) of banners

## Demo

* See banners in action in our [live demo](https://demo.frigade.com/cards)

## Installation

<Tabs>
  <Tab title="Code">
    ```tsx  theme={"system"}
    import * as Frigade from '@frigade/react';

    const App = () => {
      return (
        <Frigade.Banner flowId="my-flow-id" />
      );
    };
    ```
  </Tab>

  <Tab title="No-code">
    Banners can be be deployed with no-code using [Collections](/platform/collections).
  </Tab>
</Tabs>

## Customization

To learn about how to customize Frigade components, see the [customization documentation](/sdk/styling/) and [examples](https://demo.frigade.com) of custom themes in action.

## SDK Properties

<Tabs>
  <Tab title="React Props">
    <ParamField body="as" type="ElementType<any, keyof IntrinsicElements>">
      Optional component to wrap the child components in, e.g. `as={Dialog}` will render the Flow in a modal Dialog. Defaults to `Box`.
    </ParamField>

    <ParamField body="autoStart" type="boolean">
      Whether to automatically mark the Flow started (i.e. in progress) when the Flow is eligible to be shown.
      You will need to call `flow.start()` or `step.start()` from the parent component if you set this to `false`. Most components should not need to override this behavior.

      Defaults to `true`.
    </ParamField>

    <ParamField body="css" type="Interpolation<Theme>">
      Emotion CSS prop to apply to the component. See [Theming documentation](https://docs.frigade.com/v2/sdk/styling/css-overrides) for more information.

      Example usage:

      ```
      <Frigade.Checklist css={{ backgroundColor: "pink", ".fr-button-primary": { backgroundColor: "fuchsia" } }} />
      ```
    </ParamField>

    <ParamField body="dismissible" type="boolean">
      Whether the Flow is dismissible or not
    </ParamField>

    <ParamField body="flowId" type="string">
      The Flow ID to render. You can find the Flow ID in the Frigade dashboard.
    </ParamField>

    <ParamField body="forceMount" type="boolean">
      If true, the Flow will be mounted even if it has already been completed or dismissed.
      However, if the user does not match the Flow's targeting, the Flow will not be mounted.
    </ParamField>

    <ParamField body="modal" type="boolean">
      Register the Flow as a modal to prevent popup collisions (only one modal Flow will render at a time).
    </ParamField>

    <ParamField body="onComplete" type="FlowHandlerProp">
      Handler for when the Flow is completed. This is event is fired immediately after the user completes the Flow.
    </ParamField>

    <ParamField body="onDismiss" type="FlowHandlerProp">
      Handler for when the Flow is dismissed (skipped). This is event is fired immediately after the user dismisses the Flow.
    </ParamField>

    <ParamField body="onPrimary" type="StepHandlerProp">
      Handler for when primary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="onSecondary" type="StepHandlerProp">
      Handler for when secondary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="variables" type="Record<string, unknown>">
      Variables to pass to the Flow. You can use variables in the Flow configuration to customize copy.
      For instance, you can use `title: Hello, ${name}!` in the Flow configuration and pass `variables={{name: 'John'}}` to customize the copy.
    </ParamField>
  </Tab>

  <Tab title="Flow Configuration (Advanced Editor)">
    <ParamField body="steps" type="array">
      The steps to show in the tooltip tour.
    </ParamField>

    <ParamField body="steps[].id" type="string">
      Unique identifier for the step. Do not change this once the step has been created.
    </ParamField>

    <ParamField body="steps[].title" type="string">
      The title of the step
    </ParamField>

    <ParamField body="steps[].subtitle" type="string">
      The description of the step
    </ParamField>

    <ParamField body="steps[].imageUri" type="string">
      Url to an image to display in the step
    </ParamField>

    <ParamField body="steps[].iconUri" type="string">
      Url to an icon to display in the step. This is only supported by the carousel checklist component.
    </ParamField>

    <ParamField body="steps[].videoUri" type="string">
      Url to a video to display in the step such as YouTube, Vimeo, or a direct link to an mp4 file
    </ParamField>

    <ParamField body="steps[].primaryButton" type="object">
      Config for the primary button in this step.
    </ParamField>

    <ParamField body="steps[].primaryButton.action" type="boolean,string">
      Primary button action. (defaults to step.complete).<br />**Possible values:** `false`, `flow.back`, `flow.complete`, `flow.forward`, `flow.restart`, `flow.skip`, `flow.start`, `step.complete`, `step.skip`, `step.reset`, `step.start`
    </ParamField>

    <ParamField body="steps[].primaryButton.target" type="string">
      Primary button URI target (defaults to \_self).
    </ParamField>

    <ParamField body="steps[].primaryButton.title" type="string">
      Primary button title. If omitted, the primary button will not be shown.
    </ParamField>

    <ParamField body="steps[].primaryButton.uri" type="string">
      Primary button URI.
    </ParamField>

    <ParamField body="steps[].primaryButtonTitle" type="string">
      **Deprecated**: use `primaryButton.title` instead. The title of the primary button
    </ParamField>

    <ParamField body="steps[].primaryButtonUri" type="string">
      **Deprecated**: use `primaryButton.uri` instead. The url to open when the primary button is clicked
    </ParamField>

    <ParamField body="steps[].primaryButtonUriTarget" type="string">
      **Deprecated**: use `primaryButton.target` instead. The target of the primary button url (default: \_blank; use \_self to open in the same window). Setting it to # will open the existing page and dismiss any Frigade modals.
    </ParamField>

    <ParamField body="steps[].secondaryButton" type="object">
      Config for the secondary button in this step.
    </ParamField>

    <ParamField body="steps[].secondaryButton.action" type="boolean,string">
      Secondary button action. (defaults to step.complete).<br />**Possible values:** `false`, `flow.back`, `flow.complete`, `flow.forward`, `flow.restart`, `flow.skip`, `flow.start`, `step.complete`, `step.skip`, `step.reset`, `step.start`
    </ParamField>

    <ParamField body="steps[].secondaryButton.target" type="string">
      Secondary button URI target (defaults to \_self).
    </ParamField>

    <ParamField body="steps[].secondaryButton.title" type="string">
      Secondary button title. If omitted, the secondary button will not be shown.
    </ParamField>

    <ParamField body="steps[].secondaryButton.uri" type="string">
      Secondary button URI.
    </ParamField>

    <ParamField body="steps[].secondaryButtonTitle" type="string">
      **Deprecated**: use `secondaryButton.title` instead. The title of the secondary button
    </ParamField>

    <ParamField body="steps[].secondaryButtonUri" type="string">
      **Deprecated**: use `secondaryButton.uri` instead. The url to open when the secondary button is clicked
    </ParamField>

    <ParamField body="steps[].secondaryButtonUriTarget" type="string">
      **Deprecated**: use `secondaryButton.target` instead. The target of the secondary button url (default: \_blank; use \_self to open in the same window). Setting it to # will open the existing page and dismiss any Frigade modals.
    </ParamField>

    <ParamField body="steps[].completionCriteria" type="string">
      Targeting that automatically completes the step. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].startCriteria" type="string">
      Targeting that automatically blocks the step from starting until it becomes true. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].visibilityCriteria" type="string">
      Targeting that automatically shows the step when it becomes true. E.g.: user.property('connectedBank') == true
    </ParamField>

    <ParamField body="steps[].props" type="object">
      Override the default UI props for the corresponding component
    </ParamField>
  </Tab>
</Tabs>
