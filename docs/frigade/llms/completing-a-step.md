# Source: https://docs.frigade.com/sdk/advanced/completing-a-step.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dynamically Completing a Step

> Learn how to dynamically complete steps in Flows when your users take certain actions in your application.

For most components, steps in Flows are marked as completed when a user clicks the primary button. However, for components such as [Checklists](/component/checklist), you may want to complete or skip steps when your users take certain actions in your application rather than clicking the primary button. This can be achieved either marking a step completed via the SDK or API, or by defining a targeting query in the `completionCriteria` property on a step.

### Marking Steps completed via the SDK

Call the `complete` method from the [useFlow hook](/sdk/hooks/flow) in the [React SDK](/sdk/quickstart) or via the [JS SDK](/sdk/js/flow). In the example below, we're calling the `complete` method from the React SDK:

```javascript  theme={"system"}
import { useFlow } from '@frigade/react';

const { flow } = useFlow("my-flow-id");

await flow.steps.get('my-step-id').complete();
```

### Marking Steps complete via Targeting

Use the `completionCriteria` property on a step to automatically mark the step as completed when a user meets the criteria. See [Targeting](/platform/targeting) for more examples of how to write targeting queries.

```yaml  theme={"system"}
steps:
  - id: my-step-id
    ...
    completionCriteria: user.property('connectedBank') == true
```

### Preventing Steps from completing on primary button click

In built-in Flow components, a step is marked as complete when the primary button is clicked. To prevent this, select **No action** in the editor under the **Primary button** property:

<Frame>
  <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/no-action.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=37f4d1e7ccf0a41ffac913d6c8a01130" data-og-width="1842" width="1842" data-og-height="1027" height="1027" data-path="images/sdk/no-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/no-action.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=7e941d97545749a9a679bf68e4e49848 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/no-action.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=8e493b96aa2399a875646562bdcf85a7 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/no-action.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=9173016be52c5144d283dae29d948243 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/no-action.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=96e27308262ae1777c0a22c7e62bd044 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/no-action.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=ef86e0b2b1d391ba67477c39d522de11 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/sdk/no-action.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=e4d598be5d5b582fd2f62e78b3b97a73 2500w" />
</Frame>

## API Methods

You can also mark steps completed via the [flowStates](/api-reference/flows/flow-states-post) API endpoint.
