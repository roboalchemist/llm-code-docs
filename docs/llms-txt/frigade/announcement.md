# Source: https://docs.frigade.com/component/announcement.md

# Announcement

> Communicate information or drive action via modal-based announcements

<Frame className="h-96 items-center px-4">
  <img
    src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/components/announcement.svg"
    style={{
    width: "350px",
  }}
  />
</Frame>

## About this component

The `Announcement` component is a flexible communication tool that’s perfect for sharing important information or driving user action. They’re especially effective for getting the word out about new feature launches, upcoming webinars, or welcoming users to new areas of your product.

**When to Use Announcements:**

* **Key Communications:** Use announcements to highlight significant updates or events that need immediate user attention.
* **Transactional Flows:** They’re also great for welcoming users or guiding them to explore new features, like kicking off a product tour.

**Advantages of Announcements:**

* **Grab Attention:** Announcements often interrupt workflows in a way that demands attention, making sure users don’t miss out on important info.
* **Visual Impact:** You have ample space for visual assets (videos, images, GIF), which can help draw users in and keep the message engaging.

**Best Practices for Effective Announcements:**

* **Limit Frequency:** To avoid overwhelming users, try to keep announcements to once a session per user, and ideally once a week. This helps maintain their impact and prevents the dreaded “wack-a-mole” effect.
* **Be Concise:** Keep your messages short and to the point. The easier they are to digest, the more likely users will engage with them.
* **Target Your Audience:** Make sure your announcements are relevant and reach the right people by targeting on user properties, events and other signals.
* **Clear Calls to Action:** Use actionable phrases like “Learn more” and direct links over passive language like "Got it" or "Okay".
* **Utilize Collections:** Use Frigade Collections to manage in-app UI channels effectively, ensuring that only one announcement is displayed at a time.
* **Less Critical Info:** For non-essential information, consider launching announcements in the corner of the screen without background blurs for a subtler touchpoint.

## Resources

* [Launch announcements](/platform/collections#launch-with-collections) in minutes with no-code via Collections
* Target your announcement to specific users with [Targeting](/platform/targeting)

## Demo

* See announcements in action in our [live demo](https://demo.frigade.com/modals)

## Installation

<Tabs>
  <Tab title="Code">
    ```tsx
    import * as Frigade from '@frigade/react';

    const App = () => {
      return (
        <Frigade.Announcement flowId="my-flow-id" />
      );
    };

    ```
  </Tab>

  <Tab title="No-code">
    Announcements can be be deployed with no-code using [Collections](/platform/collections).
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

    <ParamField body="onCloseAutoFocus" type="(event: Event) => void">
      Event handler called when auto-focusing on close.
      Can be prevented.
    </ParamField>

    <ParamField body="onComplete" type="FlowHandlerProp">
      Handler for when the Flow is completed. This is event is fired immediately after the user completes the Flow.
    </ParamField>

    <ParamField body="onDismiss" type="FlowHandlerProp">
      Handler for when the Flow is dismissed (skipped). This is event is fired immediately after the user dismisses the Flow.
    </ParamField>

    <ParamField body="onEscapeKeyDown" type="(event: KeyboardEvent) => void">
      Event handler called when the escape key is down.
      Can be prevented.
    </ParamField>

    <ParamField body="onInteractOutside" type="(event: PointerDownOutsideEvent , FocusOutsideEvent) => void">
      Event handler called when an interaction happens outside the `DismissableLayer`.
      Specifically, when a `pointerdown` event happens outside or focus moves outside of it.
      Can be prevented.
    </ParamField>

    <ParamField body="onOpenAutoFocus" type="(event: Event) => void">
      Event handler called when auto-focusing on open.
      Can be prevented.
    </ParamField>

    <ParamField body="onOpenChange" type="(open: boolean) => void" />

    <ParamField body="onPointerDownOutside" type="(event: PointerDownOutsideEvent) => void">
      Event handler called when the a `pointerdown` event happens outside of the `DismissableLayer`.
      Can be prevented.
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
      The individual steps/pages of the announcement
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
