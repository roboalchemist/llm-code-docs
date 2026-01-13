# Source: https://docs.datadoghq.com/cloudcraft/components-aws/eks-workload.md

---
title: EKS Workload Component
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Cloudcraft (Standalone) > AWS Components > EKS Workload Component
source_url: https://docs.datadoghq.com/components-aws/eks-workload/index.html
---

# EKS Workload Component

## Overview{% #overview %}

{% alert level="info" %}
Scanning Amazon EKS components requires [authorizing Cloudcraft's IAM role for view-only access](https://docs.datadoghq.com/cloudcraft/getting-started/connect-amazon-eks-cluster-with-cloudcraft/).
{% /alert %}

Use the EKS Workload component to visualize Amazon EKS workloads from your Amazon Web Services architecture.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/components-aws/eks-workload/component-eks-workload-diagram.f4f70be3afa8f2e1b0eb4ca70f05ebde.png?auto=format"
   alt="Screenshot of an isometric Cloudcraft diagram showing interconnected AWS components." /%}

## Toolbar{% #toolbar %}

Use the toolbar to configure and customize the component. The following options are available:

- **Color**: Select a fill color for the top of the component and an accent color for the bottom. You can use the same colors for the 2D and 3D views or different colors for each.
- **Name**: Enter a name for the workload.
- **Type**: Select the type of workload to use.

## API{% #api %}

Use the [Cloudcraft API](https://developers.cloudcraft.co/) to programmatically access and render your architecture diagrams as JSON objects.

### Schema{% #schema %}

The following is an example JSON object of a EKS Workload component:

```json
{
    "type": "eksworkload",
    "id": "a5cad956-3366-4582-a73a-2709d53e975f",
    "region": "us-east-1",
    "mapPos": [3.5,-0.75],
    "name": "EKS Workload",
    "workloadType": "deployment",
    "nodes": [
        "cadf6a3f-67d2-4df9-ad40-f892030af58b",
        "a9437fdf-56f9-4c3b-8acf-6f0f37f70980",
        "b15e51da-b99b-4072-b4c4-e9e85df7e285",
        "b5878fa9-bf1a-44d0-bc8d-336f99763fce"
    ],
    "color": {
        "isometric": "#f44336",
        "2d": "#f44336"
    },
    "accentColor": {
        "isometric": "#f44336",
        "2d": "#f44336"
    },
    "link": "https://aws.amazon.com/eks/",
    "locked": true
}
```

- **type: string**: The type of component. Must be a string of value `eksworkload` for this component.
- **id: string, uuid**: The unique identifier for the component. The API uses a UUID v4 internally but accepts any unique string.
- **arn: string**: The globally unique identifier for the component within AWS, known as the [Amazon Resource Names](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
- **region: string**: The AWS region for the component. All global regions are supported, [except for AWS China](https://docs.datadoghq.com/cloudcraft/faq/scan-error-aws-china-region/).
- **mapPos: array**: The position of the component in the blueprint, expressed as an x- and y-coordinate pair.
- **name: string**: The name of the workload. Defaults to `EKS Workload`.
- **workloadType: string**. The type of the workload on the cluster. See Accepted values for `workloadType` for more information. Defaults to `deployment`.
- **nodes: array**: The pods running on this workload. Accepts an array of unique identifiers of EKS Pods.
- **color: object**: The fill color for the top of the component body.
  - **isometric: string**: A hexadecimal color for the component body in the 3D view. Defaults to `#FFFFFF`.
  - **2d: string**: A hexadecimal color for the component body in the 2D view. Defaults to `#FFFFFF`.
- **accentColor: object**: The accent color for the bottom of the component body.
  - **isometric: string**: A hexadecimal color for the component logo in the 3D view. Defaults to `#4286C5`.
  - **2d: string**: A hexadecimal color for the component logo in the 2D view. Defaults to `#693CC5`.
- **link: string, uri**: A URI that links the component to another diagram or an external website. Accepts one of the following formats, `blueprint://` or `https://`.
- **locked: boolean**: Whether to allow changes to the position of the component through the web interface. Defaults to `false`.

## Accepted values for `workloadType`{% #accepted-values-for-workloadtype %}

The `workloadType` key accepts one of the following string values:

```
deployment, statefulSet, daemonSet, job, cronJob
```
