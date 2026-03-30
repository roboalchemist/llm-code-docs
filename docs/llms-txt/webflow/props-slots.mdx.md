# Source: https://developers.webflow.com/devlink/docs/component-export/design-guidelines/props-slots.mdx

***

title: Props and Slots in Exported Components
description: >-
How to create and expose custom properties in Webflow Designer for use in
React.
subtitle: Create and expose custom properties in Webflow Designer for use in React.
max-toc-depth: 3
----------------

DevLink converts Webflow’s component properties into fully typed React props, giving you programmatic control over your components.

These props come with full TypeScript support and preserve all the defaults and rules set up in Webflow. You can use them to update content, handle user interactions, and control how your components behave in your React app.

## Basic props

Webflow’s native component properties for content and visibility. The visual editor defines these properties, and DevLink automatically types them in React. Component export supports the following properties:

A prop’s **Type** setting determines the values it can accept and how it appears in the Designer.

<div>
  <div>
    * Text
    * Video
    * Link
  </div>

  <div>
    * Rich text
    * Number
    * Visibility
  </div>
</div>

#### Example: Notification button

This **Button** component has text and visibility props to show the number of new notifications for a user. The `text` prop sets the number of notifications, while the `showThis` visibility prop shows/hides the button based on the number of notifications.

```jsx title="Dashboard.tsx"
import { Button } from "../../devlink/Button";


export default function Dashboard({numNotifications}: {numNotifications: number}) {
  return (
    <div>
      <Button
        text={`${numNotifications} new notifications`}
        showIcon={numNotifications > 0}
      />
    </div>
  );
}
```

## DevLink props

DevLink-specific props customize the behavior of the exported component in your React app. They're not natively supported on Webflow sites, but can be configured in the Designer before exporting.

### Runtime props

Runtime props let you add React-specific behavior to an exported component where Webflow doesn’t have a native setting. When you add a runtime-props property to an element in the Designer, DevLink generates a matching React prop and spreads it onto that element’s underlying HTML node.

#### Creating runtime props in Webflow

Add runtime props to your components by selecting a supported element, then navigating to the element’s settings panel.

In the DevLink section, you can add runtime props to the element. Only certain elements have support for Runtime Props.

<div>
  <Frame caption="Runtime props component property">
    <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/05870ec2a862afde6d526dabe621e65d78f5d05e8b4289e7be2f17325d9cd3cc/products/devlink/pages/exported-components/assets/runtime-props.png" />
  </Frame>
</div>

Use runtime props to:

* Handle events (e.g., `onClick`, `onSubmit`)
* Apply specific inline styles via the React style prop
* Override the element’s class (not recommended—replaces Webflow classes)
* Attach a React `ref`

#### Example: Notification button

This **Button** component has a `buttonProps` runtime prop to handle the click event of the button. The `buttonProps` prop is an object that contains the properties of the button.

```jsx title="Dashboard.tsx"
import { Button } from "../../devlink/Button";


export default function Dashboard({numNotifications}: {numNotifications: number}) {
  return (
    <div>
      <Button
        text={`${numNotifications} new notifications`}
        showIcon={numNotifications > 0}
        buttonProps={{ onClick: () => handleClick() }}
      />
    </div>
  );
}
```

### DevLink slots

A **slot** is a DevLink-specific property that accepts a React component as its value.

Slots let you nest components inside other components in your React app. This is especially useful when you need to combine Webflow-authored structure with custom React logic or third-party components that can’t be built in Webflow directly.

To set a slot property on an element, create a wrapper div block in the component, then go to the Element settings panel > DevLink > Slot, then connect it to a property.

#### Example: Card component with a slot

This **Card** component has a `cardContent` slot that accepts a React component as its value.

```jsx title="Card.tsx"
import { Card } from "@/devlink/Card";
import { UserProfile } from "@/components/UserProfile";

export function Example() {
  return (
    <Card
      cardContent={
        <UserProfile id="42" />
      }
    />
  );
}
```

**When to use slots**

* Embed custom React components (e.g., charts, modals, media players).
* Integrate third-party libraries inside a Webflow-made layout.
* Pass dynamic content into a reusable Webflow component without hard-coding it in the Designer.

<Warning title="DevLink slots are different than Webflow Component Slots">
  DevLink slots enable you to inject custom React components or content into specific areas of an exported React component. In contrast, Webflow Component Slots are used within Webflow’s visual editor to insert Webflow Components into designated areas of a component.

  **Webflow Component Slots aren’t supported in DevLink.**
</Warning>
