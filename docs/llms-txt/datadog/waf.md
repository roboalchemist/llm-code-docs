# Source: https://docs.datadoghq.com/cloudcraft/components-aws/waf.md

---
title: WAF Component
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloudcraft (Standalone) > AWS Components > WAF Component
source_url: https://docs.datadoghq.com/components-aws/waf/index.html
---

# WAF Component

## Overview{% #overview %}

Use the WAF component to represent visualize web application firewalls from your Amazon Web Services architecture.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/components-aws/waf/component-waf-diagram.897b0b8ab6dec23c538f693f6b3cd35c.png?auto=format"
   alt="Screenshot of an isometric Cloudcraft diagram showing interconnected AWS components." /%}

## Toolbar{% #toolbar %}

Use the toolbar to configure and customize the component. The following options are available:

- **Color**: Select a fill color for the body of the component and an accent color for its symbol. You can use the same colors for the 2D and 3D views or different colors for each.
- **Rules & Groups**: Enter the number of rules and groups you want per web ACL.
- **Requests (millions/mo)**: Enter the number of web requests your WAF receives per month, in millions.

## API{% #api %}

Use the [Cloudcraft API](https://developers.cloudcraft.co/) to programmatically access and render your architecture diagrams as JSON objects.

### Schema{% #schema %}

The following is an example JSON object of a WAF component:

```json
{
    "type": "waf",
    "id": "7334ebd8-e980-45c6-9211-e8f090089c6e",
    "arn": "arn:aws:wafv2:us-east-1:746399320916:global/webacl/webacl-test-cdn/793709d6-e353-4cce-aeb7-b1fa5d8845d4",
    "region": "us-east-1",
    "mapPos": [-1,9],
    "aclCount": 5,
    "ruleCount": 5,
    "requestMillions": 5,
    "color": {
        "isometric": "#000000",
        "2d": "#000000"
    },
    "accentColor": {
        "isometric": "#f44336",
        "2d": "#f44336"
    },
    "link": "https://aws.amazon.com/waf/",
    "locked": true
}
```

- **type: string**: The type of component. Must be a string of value `waf` for this component.
- **id: string, uuid**: The unique identifier for the component. The API uses a UUID v4 internally but accepts any unique string.
- **arn: string**: The globally unique identifier for the component within AWS, known as the [Amazon Resource Names](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
- **region: string**: The AWS region for the component. All global regions are supported, [except for AWS China](https://docs.datadoghq.com/cloudcraft/faq/scan-error-aws-china-region/).
- **mapPos: array**: The position of the component in the blueprint, expressed as an x- and y-coordinate pair.
- **aclCount: number**: The number of web access control lists used. Defaults to `1`.
- **ruleCount: number**: The number of rules added per web access control list. Defaults to `0`.
- **requestMillions: number**: The number of web requests received per month, in millions. Defaults to `0`.
- **color: object**: The fill color for the component body.
  - **isometric: string**: A hexadecimal color for the component body in the 3D view. Defaults to `#607D8B`.
  - **2d: string**: A hexadecimal color for the component body in the 2D view. Defaults to `#D6242D`.
- **accentColor: object**: The accent color for the component logo.
  - **isometric: string**: A hexadecimal color for the component logo in the 3D view. Defaults to `#FF5722`.
  - **2d: string**: A hexadecimal color for the component logo in the 2D view. Defaults to `#FFFFFF`.
- **link: string, uri**: A URI that links the component to another diagram or an external website. Accepts one of the following formats: `blueprint://` or `https://`.
- **locked: boolean**: Whether to allow changes to the position of the component through the web interface. Defaults to `false`.
