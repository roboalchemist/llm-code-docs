# Source: https://docs.datadoghq.com/cloudcraft/components-aws/ecr-repository.md

---
title: ECR Repository Component
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloudcraft (Standalone) > AWS Components > ECR Repository Component
source_url: https://docs.datadoghq.com/components-aws/ecr-repository/index.html
---

# ECR Repository Component

## Overview{% #overview %}

Use the ECR Repository component to visualize container repositories from your Amazon Web Services architecture.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/components-aws/ecr-repository/component-ecr-repository-diagram.d5905f772310883ca68bc59737065972.png?auto=format"
   alt="Screenshot of an isometric Cloudcraft diagram showing interconnected AWS components." /%}

## Toolbar{% #toolbar %}

Use the toolbar to configure and customize the component. The following options are available:

- **Color**: Select a fill color for the body of the component and an accent color for its symbol. You can use the same colors for the 2D and 3D views or different colors for each.
- **Data stored (GB)**: Enter the amount of data you store in your repositories.
- **Private**: Select if your repository is public or private.

## API{% #api %}

Use the [Cloudcraft API](https://developers.cloudcraft.co/) to programmatically access and render your architecture diagrams as JSON objects.

### Schema{% #schema %}

The following is an example JSON of a ECR Repository component:

```json
{
    "type": "ecr",
    "id": "15e88546-33f3-40d5-b88c-e7cdae335da8",
    "arn": "arn:aws:ecr:us-east-1:728720640411:repository/cloudcraft",
    "region": "us-east-1",
    "mapPos": [7.5,6],
    "storageGB": 1,
    "private": true,
    "color": {
        "isometric": "#ff9800",
        "2d": "#ff9800"
    },
    "accentColor": {
        "isometric": "#ffffff",
        "2d": "#ffffff"
    },
    "link": "https://aws.amazon.com/ecr/",
    "locked": true
}
```

- **type: string**: The type of component. Must be a string of value `ecr` for this component.
- **id: string, uuid**: The unique identifier for the component. The API uses a UUID v4 internally but accepts any unique string.
- **arn: string**: The globally unique identifier for the component within AWS, known as the [Amazon Resource Names](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
- **region: string**: The AWS region for the component. The API supports all global regions, [except for AWS China](https://docs.datadoghq.com/cloudcraft/faq/scan-error-aws-china-region/).
- **mapPos: array**: The position of the component in the blueprint, expressed as an x- and y-coordinate pair.
- **storageGB: number**: The amount of data stored in the repositories inside the registry, in gigabytes. Defaults to `1`.
- **private: boolean**: Whether the repository is private. Defaults to `true`.
- **color: object**: The fill color for the component body.
  - **isometric: string**: A hexadecimal color for the component body in the 3D view. Defaults to `#3F7DDE`.
  - **2d: string**: A hexadecimal color for the component body in the 2D view. Defaults to `#D86613`.
- **accentColor: object**: The accent color for the component logo.
  - **isometric: string**: A hexadecimal color for the component logo in the 3D view. Defaults to `#052048`.
  - **2d: string**: A hexadecimal color for the component logo in the 2D view. Defaults to `#FFFFFF`.
- **link: string, uri**: A URI that links the component to another diagram or an external website. Accepts one of the following formats: `blueprint://` or `https://`.
- **locked: boolean**: Whether to allow changes to the position of the component through the web interface. Defaults to `false`.
