# Source: https://docs.datadoghq.com/cloudcraft/components-aws/auto-scaling-group.md

---
title: Auto Scaling Group Component
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloudcraft (Standalone) > AWS Components > Auto Scaling Group Component
---

# Auto Scaling Group Component

## Overview{% #overview %}

Use the Auto Scaling Group component to represent Auto Scaling groups from your Amazon Web Services architecture.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/components-aws/auto-scaling-group/component-auto-scaling-group-diagram.81af6f3c3bea7dce462867cf4778585b.png?auto=format"
   alt="Screenshot of an isometric Cloudcraft diagram showing the 'Auto scaling group' AWS component." /%}

## Toolbar{% #toolbar %}

Use the toolbar to configure and customize your component. The following options are available:

- **Color**. Select a predefined color or enter the hexadecimal value of the color for the component. The component can use the same color for both 2D and 3D view, or different colors for each.
- **Layout**. Select the layout for the auto scaling group, "even," where members are evenly laid out in the available space, or "manual," where members are manually positioned.

## API{% #api %}

Use the [Cloudcraft API](https://developers.cloudcraft.co/) to programmatically access and render your architecture diagrams as JSON objects.

### Schema{% #schema %}

The following is an example JSON object of an Auto Scaling Group component:

```json
{
  "type": "asg",
  "id": "0998cf01-d22e-4324-83a9-b06ffbd93188",
  "region": "us-east-2",
  "mapPos": [-2.75, 9],
  "mapSize": [3.25, 1],
  "layout": "even",
  "nodes": [
    "056b4f94-fe18-43de-9e55-325d31813a80",
    "d037dd26-252e-4ba0-95f7-e6656cd00413"
  ],
  "color": {
    "2d": "#f5b720",
    "isometric": "#f5b720"
  },
  "link": "blueprint://bbb22829-4abb-4fba-8a25-1896545eb9d1",
  "locked": true
}
```

- **type: asg**: The type of component.
- **id: string**: A unique identifier for the component in the `uuid` format.
- **region: string**: The AWS region the auto scaling group is deployed in. All global regions are supported except `cn-` regions.
- **mapPos: [number, number]**: The position of the component in the blueprint, expressed as an x- and y-coordinate pair.
- **mapSize: [number, number]**: The size of the auto scaling group in the blueprint.
- **layout: string**: The layout of the auto scaling group. Accepted values are `even` or `manual`.
- **nodes: array**: The EC2 instances inside the auto scaling group. Must consist of an array of Cloudcraft issued unique identifiers for the EC2 instances.
- **color: object**: The fill color for the component body.
  - **isometric: string**: The fill color for the component in the 3D view. Must be a hexadecimal color.
  - **2d: string**: The fill color for the component in the 2D view. Must be a hexadecimal color.
- **link: uri**: Link the component to another diagram using the `blueprint://ID` format or to an external website using the `https://LINK` format.
- **locked: boolean**: If `true`, changes made to the component using the application are disabled until unlocked.
