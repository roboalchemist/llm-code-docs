# Source: https://docs.frigade.com/component/hint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Hint

> Hints are a great way to subtly call attention to specific parts of your UI

<Frame>
  <img
    src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/hint.svg?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=2da7d591eb61dcb9cec7eb90e6b6a9a4"
    style={{
    width: "350px",
  }}
    data-og-width="390"
    width="390"
    data-og-height="440"
    height="440"
    data-path="images/components/hint.svg"
    data-optimize="true"
    data-opv="3"
    srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/hint.svg?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=49177bd51b9a24bb32c8d707eac66332 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/hint.svg?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=9b5c06a32647218ad936be59da8b6305 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/hint.svg?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=74b6f27baa0bfe0471addc1145af6f22 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/hint.svg?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=8afbb6903463f6587367da28e3e200a1 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/hint.svg?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=719ae4f59f847c0ed1a6d29f35c7451f 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/hint.svg?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=86626bebb6613e9f1f49fc0b98ea4577 2500w"
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
    ```tsx App.tsx theme={"system"}
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
