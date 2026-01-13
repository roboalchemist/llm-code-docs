# Source: https://docs.datadoghq.com/cloudcraft/components-aws/internet-gateway.md

---
title: Internet Gateway Component
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloudcraft (Standalone) > AWS Components > Internet Gateway Component
source_url: https://docs.datadoghq.com/components-aws/internet-gateway/index.html
---

# Internet Gateway Component

## Overview{% #overview %}

Use the Internet Gateway component to represent gateways to the internet from your Amazon Web Services architecture.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/components-aws/internet-gateway/component-internet-gateway-diagram.5f5d0ca5df6b732e87c6c373adead476.png?auto=format"
   alt="Screenshot of an isometric Cloudcraft diagram showing the 'Internet gateway' AWS component." /%}

## Toolbar{% #toolbar %}

Use the toolbar to configure and customize the component. The following options are available:

- **Color**: Select a predefined color or enter the hexadecimal value of the color for the component and its accent. The component can use the same color for both the 2D and 3D view, or different colors for each.
- **Rotate**: Rotate the component and change its direction.

## API{% #api %}

Use the [Cloudcraft API](https://developers.cloudcraft.co/) to programmatically access and render your architecture diagrams as JSON objects.

### Schema{% #schema %}

The following is an example JSON of an Internet Gateway component:

```json
{
  "type": "internetgateway",
  "id": "aacf299e-1336-46a3-98d7-3ef75eef8116",
  "region": "us-east-1",
  "mapPos": [-4.25,9],
  "color": {
    "isometric": "#4286c5",
    "2d": "#4286c5"
  },
  "accentColor": {
    "isometric": "#ffffff",
    "2d": "#ffffff"
  },
  "direction": "down",
  "link": "blueprint://b07827f7-2ead-4911-bb78-ddc02dc07b24",
  "locked": true
}
```

- **type: internetgateway**: The type of component.
- **id: string**: A unique identifier for the component in the `uuid` format.
- **region: string**: The AWS region the gateway is deployed in. All global regions are supported except `cn-` regions.
- **mapPos: [number, number]**: The position of the component in the blueprint, expressed as an x- and y-coordinate pair.
- **color: object**: The fill color for the component body.
  - **isometric: string**: The fill color for the component in the 3D view. Must be a hexadecimal color.
  - **2d: string**: The fill color for the component in the 2D view. Must be a hexadecimal color.
- **accentColor: obect**: The accent color used to display the component logo on the block.
  - **isometric: string**: The accent color for the component in the 3D view. Must be a hexadecimal color.
  - **2d: string**: The accent color for the component in the 2D view. Must be a hexadecimal color.
- **direction: string**: The rotation or direction of the component. Accepts `down` or `right`. Default is `down`.
- **link: uri**: Link the component to another diagram using the `blueprint://ID` format or to external website using the `https://LINK` format.
- **locked: boolean**: If `true`, changes made to the component using the application are disabled until unlocked.

The internet gateway component can only be added to [VPCs](https://docs.datadoghq.com/cloudcraft/components-aws/vpc/).
