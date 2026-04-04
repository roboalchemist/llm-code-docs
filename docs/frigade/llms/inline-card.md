# Source: https://docs.frigade.com/component/inline-card.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Card

> Communicate information or drive action via in-line content cards

<Frame className="h-96 items-center">
  <img src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/inline-card.svg?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=abfab3323d2170b86b6ee639e15944dd" style={{ maxWidth: "300px" }} data-og-width="360" width="360" data-og-height="165" height="165" data-path="images/components/inline-card.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/inline-card.svg?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=6abc6d7c71151f904a656b78283f5616 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/inline-card.svg?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=92d84811248e1db170f274ede35174d4 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/inline-card.svg?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=f69788ea49c6d800fa5777dab22bb7ea 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/inline-card.svg?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=9b4f485d6b364775deea9388f28772ca 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/inline-card.svg?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=a7ccd2699537edf8410ee3df11409dd0 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/inline-card.svg?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=4db6b8e14ca67696eefbbf9faa2e9d0b 2500w" />
</Frame>

## About this component

The `Card` component is a handy little UI element that’s great for showing off promotional materials and important info in a visually appealing way. While they share some similarities with banners, cards have their own unique vibe and offer flexibility in placement.

**When to Use Cards:**

* **Promotional Materials:** Think of cards as your go-to swiss-army knife for inline promotions. For instance, showcasing new features, nudging users with onboarding tips, or encouraging user referrals.

**Advantages of Cards:**

* **Inline Placement:** You’ll usually find cards sitting neatly within in the main UI, like in a sidebar or alongside other product elements. This makes them easy to spot without getting in the way of the user experience.
* **Visual Appeal:** Cards can be designed with eye-catching images, icons, and text, making them interesting and engaging for users.
* **Versatile Use:** Whether you’re promoting a feature or sharing a helpful resource, cards can handle a variety of content types, making them super flexible.

**Best Practices for Cards:**

* **Strategic Placement:** Think about where you put your cards. Positioning them where users can easily see them can boost engagement.
* **Keep It Consistent:** Stick to a consistent design and placement across all your cards. These patterns helps create a cohesive look and feel throughout your app, which increases engagement.
* **Clear Calls to Action:** Make sure each card has a clear call to action, like “Learn More” or “Request Demo.” This encourages users to take that next step.

## Resources

* Launch cards with no-code using custom [Collections](/platform/collections#inline-ui-components)
* Target your card to specific users with [Targeting](/platform/targeting)
* See [industry examples](https://www.productonboarding.com/?type=card) of cards

## Demo

* See cards in action in our [live demo](https://demo.frigade.com/cards)

## Installation

<Tabs>
  <Tab title="Code">
    ```tsx  theme={"system"}
    import * as Frigade from '@frigade/react';

    const App = () => {
      return (
        <Frigade.Card flowId="my-flow-id" />
      );
    };
    ```
  </Tab>

  <Tab title="No-code">
    Cards can be be deployed with no-code using [Collections](/platform/collections).
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

    <ParamField body="children" type="any" />

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
