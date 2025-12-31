# Source: https://docs.frigade.com/component/hint.md

# Hint

> Hints are a great way to subtly call attention to specific parts of your UI

<Frame>
  <img
    src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/components/hint.svg"
    style={{
    width: "350px",
  }}
  />
</Frame>

## About this component

The `Hint` component provides users with contextual guidance without interrupting their workflow. Unlike tours, hints are not sequential and are closed by default, allowing users to engage with them at their own pace. This design choice minimizes disruption and enhances the user experience by offering assistance when needed.

**When to Use Hints:**

* **Contextual Assistance:** Provide users with relevant tips or information based on their current task or location within the app.
* **Feature Highlights:** Draw attention to new or underutilized features without overwhelming users with a full tour.
* **Error Prevention:** Offer guidance that helps users avoid common mistakes or pitfalls as they navigate the application.

**Best Practices for Hints:**

* **Visibility:** Ensure hints are easily noticeable but not obtrusive. Use subtle animations or colors to draw attention without being distracting.
* **Actionable Content:** Like tours, hints should provide actionable advice. For example, instead of stating “This is the settings page,” a hint could say, “Click here to adjust your notification preferences.”
* **Dismissible:** Hints should be easily dismissible. Users should feel in control and not forced to engage with hints if they choose not to.

## Demo

* See hints in action in our [live demo](https://demo.frigade.com/hints)

## Installation

<Tabs>
  <Tab title="Code">
    ```tsx App.tsx
    import * as Frigade from '@frigade/react';

    const App = () => {
      return (
        <Frigade.Tour
          flowId='flow_laJhda4sgJCdsCy6'
          sequential={false} // Show all Steps at once
          defaultOpen={false} // Only show Hint markers
        />
      );
    };
    ```
  </Tab>

  <Tab title="No-code">
    Hints can be be deployed with no-code using [Collections](/platform/collections).
  </Tab>
</Tabs>

## Customization

To learn about how to customize Frigade components, see the [customization documentation](/sdk/styling/) and [examples](https://demo.frigade.com) of custom themes in action.

## SDK Properties

Hints are a specific configuration of Tours. Please refer to the [Tour](/component/tour#sdk-properties) documentation to see properties for Hints.
