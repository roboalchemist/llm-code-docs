# Source: https://docs.datadoghq.com/cloudcraft/components-aws/ses.md

---
title: SES Component
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloudcraft (Standalone) > AWS Components > SES Component
source_url: https://docs.datadoghq.com/components-aws/ses/index.html
---

# SES Component

## Overview{% #overview %}

Use the SES component to represent transactional and marketing email services from your Amazon Web Services architecture.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/components-aws/ses/component-ses-diagram.3557c02312ac53ce387f8cca623ec2cb.png?auto=format"
   alt="Screenshot of an isometric Cloudcraft diagram showing the 'SES' AWS component." /%}

## Toolbar{% #toolbar %}

Use the toolbar to configure and customize the component. The following options are available:

- **Color**: Select a predefined color or enter the hexadecimal value of the color for the component and its accent. The component can use the same color for both the 2D and 3D view, or different colors for each.
- **Emails/month (K)**: Enter the number of email messages sent per month, in the thousands.

## API{% #api %}

Use the [Cloudcraft API](https://developers.cloudcraft.co/) to programmatically access and render your architecture diagrams as JSON objects.

### Schema{% #schema %}

The following is an example JSON of a SES component:

```json
{
  "type": "ses",
  "id": "11f3e4bc-f827-48b6-9d9c-73e99ca3e289",
  "region": "us-west-2",
  "mapPos": [0,10],
  "emailsOut": 400,
  "color": {
    "isometric": "#0a1538",
    "2d": "#0a1538"
  },
  "accentColor": {
    "isometric": "#2457f2",
    "2d": "#2457f2"
  },
  "link": "https://aws.amazon.com/ses/",
  "locked": true
}
```

- **type: ses**: The type of component.
- **id: string**: A unique identifier for the component in the `uuid` format.
- **region: string**: The AWS region where the SES is deployed in. All global regions are supported except `cn-` regions.
- **mapPos: [number, number]**: The position of the component in the blueprint, expressed as an x- and y-coordinate pair.
- **emailsOut: number**: The number of email messages sent per month, in the thousands. Defaults to `10`.
- **color: object**: The fill color for the component body.
  - **isometric: string**: The fill color for the component in the 3D view. Must be a hexadecimal color.
  - **2d: string**: The fill color for the component in the 2D view. Must be a hexadecimal color.
- **accentColor: object**: The accent color used to display the component logo on the block.
  - **isometric: string**: The accent color for the component in the 3D view. Must be a hexadecimal color.
  - **2d: string**: The accent color for the component in the 2D view. Must be a hexadecimal color.
- **link: uri**: Link the component to another diagram using the `blueprint://ID` format or to an external website using the `https://LINK` format.
- **locked: boolean**. If `true`, changes made to the component using the application are disabled until unlocked.
