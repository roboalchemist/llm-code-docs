# Source: https://docs.frigade.com/component/progress-badge.md

# Progress Badge

> Display a user's progress through a Flow

<Frame className="h-96 items-center">
  <img
    src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/components/progress-badge.svg"
    style={{
    width: "220px",
  }}
  />
</Frame>

## About this component

The Progress Badge component is unlike other components in that it doesn't have its own Flow. It exists to remind a user where they left off in an existing Flow (e.g. Checklist), and to help get them jump back in and complete it.

## Demo

* See progress badges in action in our [live demo](https://demo.frigade.com/checklists)

## Installation

<Tabs>
  <Tab title="Code">
    ```tsx
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
