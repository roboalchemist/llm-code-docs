# Source: https://docs.datadoghq.com/cloudcraft/components-aws/dynamodb.md

---
title: DynamoDB Component
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloudcraft (Standalone) > AWS Components > DynamoDB Component
---

# DynamoDB Component

## Overview{% #overview %}

Use the DynamoDB component to represent and visualize NoSQL, serverless, managed databases in your Amazon Web Services architecture.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/components-aws/dynamodb/component-dynamodb-diagram.fd538e7e0db932a031acbc9eaf245e13.png?auto=format"
   alt="Screenshot of an isometric Cloudcraft diagram showing the 'DynamoDB' AWS component." /%}

## Toolbar{% #toolbar %}

Use the toolbar to configure the component. Available options include:

- **Color**: Select a fill color for the body of the component and an accent color for its symbol. You can use the same colors for both the 2D and 3D views, or choose different colors for each.
- **Table class**: Select the class of the DynamoDB table.
- **Capacity mode**: Select the capacity mode of the DynamoDB table.
- **Dataset (GiB)**: Enter the size of the dataset in GiB.
- **Read units**: Enter the number of read capacity units.
- **Write units**: Enter the number of write capacity units.
- **Read consistency**: Select the read consistency of the DynamoDB table.

## API{% #api %}

Use the [Cloudcraft API](https://developers.cloudcraft.co/) to programmatically access and render your architecture diagrams as JSON objects.

### Schema{% #schema %}

The following is an example JSON object of a DynamoDB component:

```json
{
    "type": "dynamodb",
    "id": "29c1f0fa-3f1c-4566-ad33-ae307feee4f0-0",
    "region": "us-east-1",
    "mapPos": [39,148],
    "tableClass": "standard",
    "capacityMode": "on-demand",
    "datasetGb": 0,
    "readUnits": 0,
    "writeUnits": 0,
    "readConsistency": "strong",
    "color": {
        "isometric": "#ececed",
        "2d": "#ececed"
    },
    "accentColor": {
        "isometric": "#4286c5",
        "2d": "#4286c5"
    },
    "link": "https://aws.amazon.com/dynamodb/",
    "locked": true
}
```

- **type: string**: The component type. Must be `dynamodb`.
- **id: string, uuid**: The unique identifier for the component. Typically a UUID v4.
- **arn: string**: The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) for the component.
- **region: string**: The AWS region for the component. All global regions are supported, [except for AWS China](https://docs.datadoghq.com/cloudcraft/faq/scan-error-aws-china-region/).
- **mapPos: array**: The component's position in the blueprint, defined as an `[x, y]` coordinate pair.
- **tableClass: string**: The class of the DynamoDB table. Accepts `standard` or `standardInfrequentAccess`. Defaults to `standard`.
- **capacityMode: string**: The capacity mode of the DynamoDB table. Accepts `provisioned` or `on-demand`. Defaults to `provisioned`.
- **datasetGb: number**: The size of the dataset in GiB. Defaults to `10`.
- **readUnits: number**: The number of read capacity units. Defaults to `5`.
- **writeUnits: number**: The number of write capacity units. Defaults to `5`.
- **readConsistency: string**: The read consistency of the DynamoDB table. Accepts `strong` or `eventual`. Defaults to `strong`.
- **color: object**: The fill color for the component body.
  - **isometric: string**: A hexadecimal color for the component body in the 3D view. Defaults to `#ECECED`.
  - **2d: string**: A hexadecimal color for the component body in the 2D view. Defaults to `#ECECED`.
- **accentColor: object**: The accent color for the component logo.
  - **isometric: string**: A hexadecimal color for the component logo in the 3D view. Defaults to `#4286C5`.
  - **2d: string**: A hexadecimal color for the component logo in the 2D view. Defaults to `#4286C5`.
- **link: string, uri**: A URI that links the component to another diagram or an external website. Accepts the following formats: `blueprint://` or `https://`.
- **locked: boolean**: Whether to allow changes to the position of the component through the web interface. Defaults to `false`.
