# Source: https://docs.datadoghq.com/cloudcraft/components-aws/vpc-endpoint.md

---
title: VPC Endpoint Component
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloudcraft (Standalone) > AWS Components > VPC Endpoint Component
source_url: https://docs.datadoghq.com/components-aws/vpc-endpoint/index.html
---

# VPC Endpoint Component

## Overview{% #overview %}

Use the VPC Endpoint component to visualize VPC endpoints from your Amazon Web Services architecture.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/components-aws/vpc-endpoint/component-vpc-endpoint-diagram.a4d6acf12190332d014eabee27f0b809.png?auto=format"
   alt="Screenshot of an isometric Cloudcraft diagram showing interconnected AWS components." /%}

## Toolbar{% #toolbar %}

Use the toolbar to configure and customize the component. The following options are available:

- **Color**: Select a fill color for the body of the component and an accent color for its symbol. You can use the same colors for the 2D and 3D views or different colors for each.
- **Type**: Select the type for your VPC endpoint.
- **Data processed (GB)**: Enter the total volume of data processed by the endpoint, in gigabytes. Not available for the gateway type.

## API{% #api %}

Use the [Cloudcraft API](https://developers.cloudcraft.co/) to programmatically access and render your architecture diagrams as JSON objects.

### Schema{% #schema %}

The following is an example JSON object of a VPC Endpoint component:

```json
{
    "type": "vpcendpoint",
    "id": "b1c1f99c-4b2b-437c-bcf4-36597da7e369",
    "region": "us-east-1",
    "mapPos": [17,4],
    "endpointType": "interface",
    "dataGb": 10,
    "color": {
        "isometric": "#ECECED",
        "2d": "#693CC5"
    },
    "accentColor": {
        "isometric": null,
        "2d": null
    },
    "locked": true
}
```

- **type: string**: The type of component. Must be a string of value `vpcendpoint` for this component.
- **id: string, uuid**: The unique identifier for the component. The API uses a UUID v4 internally but accepts any unique string.
- **arn: string**: The globally unique identifier for the component within AWS, known as the [Amazon Resource Names](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
- **region: string**: The AWS region for the component. All global regions are supported, [except for AWS China](https://docs.datadoghq.com/cloudcraft/faq/scan-error-aws-china-region/).
- **mapPos: array**": The position of the component in the blueprint, expressed as an x- and y-coordinate pair.
- **endpointType: string**: The type of endpoint. Accepts one of the following options, `interface`, `gateway`, or `gatewayloadbalancer`. Defaults to `interface`.
- **dataGb: number**: The total volume of data processed by the endpoint, in gigabytes. Defaults to `10`.
- **color: object**: The fill color for the component body.
  - **isometric: string**: A hexadecimal color for the component body in the 3D view. Defaults to `#ECECED`.
  - **2d: string**: A hexadecimal color for the component body in the 2D view. Defaults to `#CC2264`.
- **accentColor: object**: The accent color for the component logo.
  - **isometric: string**: A hexadecimal color for the component logo in the 3D view. Defaults to `#4286C5`.
  - **2d: string**: A hexadecimal color for the component logo in the 2D view. Defaults to `#FFFFFF`.
- **link: string, uri**: A URI that links the component to another diagram or an external website. Accepts one of the following formats: `blueprint://` or `https://`.
- **locked: boolean**: Whether to allow changes to the position of the component through the web interface. Defaults to `false`.
