# Source: https://docs.frigade.com/component/checklist/collapsible.md

# Collapsible

> A condensed checklist component that can be used inline or in a modal

<Frame className="h-120 items-center px-4">
  <img
    src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/components/collapsible.svg"
    style={{
    width: "350px",
  }}
  />
</Frame>

## About this component

The `Checklist` component is one of Frigade’s most popular tools, especially for user onboarding and activation. They’re super handy for guiding users through their journey, whether it’s at the start of their experience or when they’re setting up a new product vertical or a complex feature.

**When to Use Checklists:**

* **Onboarding and Activation:** Checklists are perfect for helping users get started and ensuring they complete essential tasks. They provide a clear path forward and help users feel more confident as they navigate your product.

**Advantages of Announcements::**

* **Two Default Versions:** Frigade offers two out-of-the-box checklist formats—carousel and collapsible—so you can choose what fits best for your users. Plus, if you need something custom, you can easily build one using the Frigade SDK/API.
* **Deeply integrated:** The most effective checklists measure actual in-product results. Frigade makes it easy to connect checklist steps to automatically complete from actual in-product actions and milestones.

**Best Practices for Checklists:**

* **Limit the Number of Tasks:** Keep your checklists manageable. Too many tasks can overwhelm users, so aim for a concise list that’s easy to follow.
* **Pre-Complete Steps Where Applicable:** For example, marking “Set up account” complete after sign up can show users progress from the start and create a sense of momentum (like showing 20% done instead of 0%).
* **Avoid Basic “Mark Done” Steps:** Whenever possible, tie checklist steps to actual workflows and tasks. Deep linking users to complete actions is way more effective. It’s okay to have “Skip” or “Mark done” as secondary options for non-essential steps.
* **Include a CTA to Hide the Checklist:** Giving users the option to hide the checklist can help them feel more in control of their setup and UI.
* **Break Large Workflows into Smaller Segments:** If you have a hefty checklist (like 12 steps), consider phasing it and breaking it into smaller groups (like two groups of 6). This makes it feel less daunting.
* **Measure Completion Rates:** Keep track of how users are progressing through each step and the entire checklist. This data can help you identify areas for improvement for future iterations.

## Resources

* Target your checklist to specific users with [Targeting](/platform/targeting)
* [Dynamically mark a step complete](/sdk/advanced/completing-a-step#programmatically-marking-steps-complete)
* Create shared checklists using [Group Properties](/sdk/hooks/group) and [completion criteria](/sdk/advanced/completing-a-step#automatically-marking-steps-complete)
* See [industry examples](https://www.productonboarding.com/?type=checklist) of checklists

## Demo

* See checklists in action in our [live demo](https://demo.frigade.com/checklists)

## Code

<Tabs>
  <Tab title="Code">
    ```tsx
    import * as Frigade from '@frigade/react';

    const App = () => {
      return (
        <Frigade.Checklist.Collapsible flowId="my-flow-id" />
      );
    };

    ```
  </Tab>

  <Tab title="No-code">
    Checklists can be be deployed with no-code using [Collections](/platform/collections).
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

    <ParamField body="stepTypes" type="StepTypes">
      Map of step types to their respective components.
      Use this to build custom step components. The `type` defined on the step in the Flow YAML config should match the key in this object.
      For instance, if you have a step with `type: 'custom'`, you should provide a component for it like so:

      ```
      <Checklist.Collapsible stepTypes={{ custom: CustomStepComponent }} />
      ```

      The corresponding YAML config would look like:

      ```
      steps:
       - id: custom-step
         type: custom
      ```
    </ParamField>

    <ParamField body="variables" type="Record<string, unknown>">
      Variables to pass to the Flow. You can use variables in the Flow configuration to customize copy.
      For instance, you can use `title: Hello, ${name}!` in the Flow configuration and pass `variables={{name: 'John'}}` to customize the copy.
    </ParamField>
  </Tab>

  <Tab title="Flow Configuration (Advanced Editor)">
    <ParamField body="sequential" type="boolean">
      If true, all steps must be completed in order. This means that the next step will be disabled until the current step is completed. Default behavior is `false`.
    </ParamField>

    <ParamField body="steps" type="array">
      The steps to show in the checklist flow.
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
