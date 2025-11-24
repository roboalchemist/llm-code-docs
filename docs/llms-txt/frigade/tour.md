# Source: https://docs.frigade.com/component/tour.md

# Tour

> Guide users through a specific product flow or feature

<Frame>
  <img
    src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/components/tour.svg"
    style={{
    width: "350px",
  }}
  />
</Frame>

## About this component

The `Tour` component is a sequential walkthrough designed to guide users through in-app steps. While tours can be one of the most effective ways to onboard users, they can also be a bit controversial. A poorly designed tour can be frustrating, especially if it interrupts users when they have a task in mind. We’ve all been there—logging into an app only to be confronted by an intrusive tour that disrupts our focus. This often leads to users rushing to close or ignore the tour, resulting in a net negative experience.

**When to Use Tours:**

* **Product Onboarding:** Show new users around critical workflows to get started
* **Feature Launches:** Increase adoption of a new feature by showing users how it workflows
* **Ongoing Education:** Automatically trigger tours for users once they reach a certain usage threshold, or give users the ability to request a tour themselves if they get stuck

**Best Practices for Announcements:**

* **Opt-In Design:** Tours should ideally be opt-in. Asking users if they want guidance results in much higher engagement compared to forcing a tour upon them. Users can opt in from a checklist, announcement, inline card, or help hub.
* **Actionable Steps:** Avoid generic and obvious statements like “This is the X page.” Instead, make tours actionable by connecting them to actual user actions. For example, a step that completes only when a user enters specific input or successfully finishes a task.
* **Keep It Short:** Tours should be concise—avoid lengthy, 16-step tours that can overwhelm users.
* **Dismissible:** Generally, tours should be dismissible. Be cautious about creating a tour that cannot be closed.
* **Relaunch Hub:** If relevant, consider providing a hub where users can relaunch specific tours. This is helpful if they are not ready or don’t have time when prompted.

## Resources

* [Create your first product tour](/guides/tours) in just a few minutes
* See [industry examples](https://www.productonboarding.com/?type=tour) of tours

## Demo

* See tours in action in our [live demo](https://demo.frigade.com/tours)

## Installation

<Tabs>
  <Tab title="Code">
    ```tsx
    import * as Frigade from "@frigade/react";

    const App = () => {
      return <Frigade.Tour flowId="my-flow-id" />;
    };
    ```
  </Tab>

  <Tab title="No-code">
    Tours can be be deployed with no-code using [Collections](/platform/collections).
  </Tab>
</Tabs>

## Customization

To learn about how to customize Frigade components, see the [customization documentation](/sdk/styling/) and [examples](https://demo.frigade.com) of custom themes in action.

## SDK Properties

<Tabs>
  <Tab title="React Props">
    <ParamField body="align" type="AlignValue">
      The alignment of the tooltip relative to the anchor.
      Possible values: `after`, `before`, `center`, `end`, `start`.
    </ParamField>

    <ParamField body="alignOffset" type="number">
      The offset of the tooltip relative to the anchor along the alignment axis.
    </ParamField>

    <ParamField body="as" type="ElementType<any, keyof IntrinsicElements>">
      Optional component to wrap the child components in, e.g. `as={Dialog}` will render the Flow in a modal Dialog. Defaults to `Box`.
    </ParamField>

    <ParamField body="autoScroll" type="boolean">
      Automatically scroll to the anchor element of the current Step
    </ParamField>

    <ParamField body="autoStart" type="boolean">
      Whether to automatically mark the Flow started (i.e. in progress) when the Flow is eligible to be shown.
      You will need to call `flow.start()` or `step.start()` from the parent component if you set this to `false`. Most components should not need to override this behavior.

      Defaults to `true`.
    </ParamField>

    <ParamField body="container" type="string , Element , DocumentFragment">
      Specify a container in the DOM render the Tour into.
      Use this to render the Tour into a different container/scrollable ancestor.
    </ParamField>

    <ParamField body="css" type="Interpolation<Theme>">
      Emotion CSS prop to apply to the component. See [Theming documentation](https://docs.frigade.com/v2/sdk/styling/css-overrides) for more information.

      Example usage:

      ```
      <Frigade.Checklist css={{ backgroundColor: "pink", ".fr-button-primary": { backgroundColor: "fuchsia" } }} />
      ```
    </ParamField>

    <ParamField body="defaultOpen" type="boolean">
      Whether the tooltip should be open by default.
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

    <ParamField body="lockScroll" type="boolean">
      Whether to lock the scroll of the container when the Spotlight is enabled.
      Defaults to `true`.
    </ParamField>

    <ParamField body="modal" type="boolean">
      Whether to render a modal overlay behind the tooltip.
    </ParamField>

    <ParamField body="onComplete" type="FlowHandlerProp">
      Handler for when the Flow is completed. This is event is fired immediately after the user completes the Flow.
    </ParamField>

    <ParamField body="onDismiss" type="FlowHandlerProp">
      Handler for when the Flow is dismissed (skipped). This is event is fired immediately after the user dismisses the Flow.
    </ParamField>

    <ParamField body="onOpenChange" type="(open: boolean) => void">
      Callback function triggered when the open state of the tooltip changes.
    </ParamField>

    <ParamField body="onPrimary" type="StepHandlerProp">
      Handler for when primary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="onSecondary" type="StepHandlerProp">
      Handler for when secondary button is clicked.
      If this function returns false or a promise that resolves to `false`, the step will not be automatically completed when clicked.
    </ParamField>

    <ParamField body="open" type="boolean">
      Controls the open state of the tooltip. Use this for controlled components.
    </ParamField>

    <ParamField body="sequential" type="boolean">
      Whether the Tour should be completed by the end-user in sequential order.
      If `false`, all steps will be rendered at once.
      Defaults to `true`, which means only one step will be rendered at a time in sequential order.
    </ParamField>

    <ParamField body="side" type="SideValue">
      The preferred side of the anchor to render the tooltip.
      Possible values: `top`, `right`, `bottom`, `left`.
    </ParamField>

    <ParamField body="sideOffset" type="number">
      The distance in pixels from the tooltip to the anchor element.
    </ParamField>

    <ParamField body="spotlight" type="boolean">
      Whether to highlight the anchor element with a spotlight/scrim effect.
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

    <ParamField body="steps[].selector" type="string">
      CSS class or ID of the element to highlight in the step (e.g. .my-element or #my-element)
    </ParamField>
  </Tab>
</Tabs>
