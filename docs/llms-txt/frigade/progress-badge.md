# Source: https://docs.frigade.com/component/progress-badge.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Progress Badge

> Display a user's progress through a Flow

<Frame className="h-96 items-center">
  <img
    src="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/progress-badge.svg?fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=268f826aae66c1096fecfe00d390a6b7"
    style={{
    width: "220px",
  }}
    data-og-width="220"
    width="220"
    data-og-height="67"
    height="67"
    data-path="images/components/progress-badge.svg"
    data-optimize="true"
    data-opv="3"
    srcset="https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/progress-badge.svg?w=280&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=acb64175dce30c206a90c60f5e01b08c 280w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/progress-badge.svg?w=560&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=9a2c2e23719d8b3c8a62bf37ede988e0 560w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/progress-badge.svg?w=840&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=43dc825fb2c9d094734dfd26cd638e9c 840w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/progress-badge.svg?w=1100&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=16642606f3d70aa01c10705d125de11c 1100w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/progress-badge.svg?w=1650&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=684d3caa16a43f910ab4be5fc7464b39 1650w, https://mintcdn.com/frigade-docs/7j7O5wbAiLBomVEP/images/components/progress-badge.svg?w=2500&fit=max&auto=format&n=7j7O5wbAiLBomVEP&q=85&s=d573a6396b82c5c7e50f2c7e6b91e30c 2500w"
  />
</Frame>

## About this component

The Progress Badge component is unlike other components in that it doesn't have its own Flow. It exists to remind a user where they left off in an existing Flow (e.g. Checklist), and to help get them jump back in and complete it.

## Demo

* See progress badges in action in our [live demo](https://demo.frigade.com/checklists)

## Installation

<Tabs>
  <Tab title="Code">
    ```tsx  theme={"system"}
    import * as Frigade from '@frigade/react';

    const App = () => {
      return (
        <Frigade.ProgressBadge flowId="my-flow-id" />
      );
    };
    ```
  </Tab>
</Tabs>

## Customization

To learn about how to customize Frigade components, see the [customization documentation](/sdk/styling/) and [examples](https://demo.frigade.com) of custom themes in action.

## SDK Properties
