# Source: https://docs.datadoghq.com/containers/monitoring/container_images.md

---
title: Container Images Explorer
description: Using the Container Images Explorer page in Datadog.
breadcrumbs: Docs > Containers > Container Monitoring > Container Images Explorer
---

# Container Images Explorer

{% image
   source="https://datadog-docs.imgix.net/images/security/vulnerabilities/container_images.bdb2dc2d5068100e2cfa4df7fda58d78.png?auto=format"
   alt="The container images view highlighting vulnerabilities and container column sort feature" /%}

In Datadog, the [Container Images Explorer](https://app.datadoghq.com/container-images) provides insights into every image used in your environment. You can also view [Cloud Security](https://docs.datadoghq.com/security/cloud_security_management) vulnerabilities in your container images, and track these vulnerabilities to specific layers.

Select the [Trends tab](https://app.datadoghq.com/container-images/image-trends) for high-level insights across all of your images in your containerized infrastructure. Container image trends metrics can help you answer key questions about your security posture and deployment footprint over the span of weeks and months.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/containerimages/container_image_trends.f908623247040b803bc5d4e67ee57948.png?auto=format"
   alt="The container images trends view highlighting image size, image age, vulnerabilities and running container count metrics" /%}

## Configuration{% #configuration %}

### Setup{% #setup %}

Container Images Explorer uses data from the following sources:

- Container collection
- Image collection
- Software Bill of Materials (SBOM) collection
- Amazon ECR metadata

#### Enable container collection{% #enable-container-collection %}

Container collection is **enabled by default** for most Datadog Agent installations. See [Set up container collection](https://docs.datadoghq.com/containers/monitoring/containers/#set-up-container-collection) for details.

#### Enable image collection{% #enable-image-collection %}

{% tab title="Datadog Operator" %}
When you install the Datadog Agent by using the Datadog Operator, image collection is automatically enabled.
{% /tab %}

{% tab title="Helm" %}
When you install the Datadog Agent by using the [official Helm chart](https://github.com/DataDog/helm-charts), image collection is enabled by default.

To verify that image collection is enabled, ensure that `datadog.containerImageCollection.enabled` is set to `true` in `datadog-values.yaml`.

```yaml
datadog:
  containerImageCollection:
    enabled: true
```

{% /tab %}

{% tab title="Amazon ECS with EC2" %}
To enable container image collection on your [ECS EC2 instances](https://docs.datadoghq.com/containers/amazon_ecs/?tab=awscli#setup), add the following environment variables to your `datadog-agent` container definition:

```yaml
{
  "containerDefinitions": [
    {
      "name": "datadog-agent",
        ...
      "environment": [
        ...
        {
          "name": "DD_CONTAINER_IMAGE_ENABLED",
          "value": "true"
        }
      ]
    }
  ]
  ...
}
```

{% /tab %}

{% tab title="Hosts" %}
Add the following to your `datadog.yaml` configuration file:

```yaml
container_image:
  enabled: true
```

{% /tab %}

#### Enable SBOM collection{% #enable-sbom-collection %}

To automatically detect container image vulnerabilities, enable [Software Bill of Materials](https://www.cisa.gov/sbom) (SBOM) collection for [Cloud Security Vulnerabilities](https://docs.datadoghq.com/security/cloud_security_management/vulnerabilities). Vulnerabilities are evaluated and scanned against your containers every hour.

{% alert level="warning" %}
**Windows environments**: The Cloud Security Vulnerabilities feature is not available for containers running on Windows environments.**Amazon ECS with AWS Fargate**: The Cloud Security Vulnerabilities feature is available for ECS Fargate through [Agentless scanning](https://docs.datadoghq.com/security/cloud_security_management/setup/agentless_scanning/compatibility).**Google Kubernetes Engine (GKE)**: To enable SBOM collection in GKE, you must [disable GKE's image streaming feature](https://cloud.google.com/kubernetes-engine/docs/how-to/image-streaming#disable).
{% /alert %}

{% tab title="Datadog Operator" %}
Add the following to your `datadog-agent.yaml` file:

```yaml
apiVersion: datadoghq.com/v2alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  features:
    # ...
    sbom:
      enabled: true
      containerImage:
        enabled: true
      host:
        enabled: true
```

{% /tab %}

{% tab title="Helm" %}
Add the following to your `datadog-values.yaml` file:

```yaml
datadog:
  sbom:
    containerImage:
      enabled: true
    host:
      enabled: true
```

{% /tab %}

{% tab title="Amazon ECS with EC2" %}
To enable container image vulnerability scanning on your [ECS EC2 instances](https://docs.datadoghq.com/containers/amazon_ecs/?tab=awscli#setup), add the following environment variables to your `datadog-agent` container definition:

```yaml
{
  "containerDefinitions": [
    {
      "name": "datadog-agent",
        ...
      "environment": [
        ...
        {
          "name": "DD_SBOM_ENABLED",
          "value": "true"
        },
        {
          "name": "DD_SBOM_CONTAINER_IMAGE_ENABLED",
          "value": "true"
        },
        {
          "name": "DD_SBOM_HOST_ENABLED",
          "value": "true"
        }
      ]
    }
  ]
  ...
}
```

If the Agent fails to extract the SBOM from the container image, increase the Agent memory in the container definition:

```yaml
{
  "containerDefinitions": [
    {
      "name": "datadog-agent",
      "memory": 256,
      ...
    }
  ]
  ...
}
```

{% /tab %}

{% tab title="Hosts" %}
Add the following to your `datadog.yaml` configuration file:

```yaml
sbom:
  enabled: true
  container_image:
    enabled: true
  host:
    enabled: true
```

{% /tab %}

#### Enable ECR metadata collection{% #enable-ecr-metadata-collection %}

Set up [Datadog's AWS integration](https://app.datadoghq.com/integrations/amazon-web-services) and enable [resource collection](https://docs.datadoghq.com/integrations/amazon_web_services/#resource-collection) to collect container image metadata from Amazon ECR.

### Tagging container images{% #tagging-container-images %}

To tag your container images, see [Kubernetes Tag Extraction](https://docs.datadoghq.com/containers/kubernetes/tag/) or [Docker Tag Extraction](https://docs.datadoghq.com/containers/docker/tag/).

## Data collected{% #data-collected %}

| Metric Name                              | Description                                                                                                                                        |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **contimage.max\_image\_size**(gauge)    | The maximum size of the container image                                                                                                            |
| **contimage.max\_image\_age**(gauge)     | The age of the container image                                                                                                                     |
| **contimage.running\_containers**(gauge) | The number of containers in which the container image is running                                                                                   |
| **contimage.vuln\_count**(gauge)         | The total number of vulnerabilities found in the container image (for Datadog Cloud Security customers who have enabled Container Vulnerabilities) |

## Further reading{% #further-reading %}

- [Enhance your troubleshooting workflow with Container Images in Datadog Container Monitoring](https://www.datadoghq.com/blog/datadog-container-image-view/)
- [Cloud Security Vulnerabilities](https://docs.datadoghq.com/security/cloud_security_management/vulnerabilities)
- [Enable SBOM collection in Cloud Security Vulnerabilities](https://docs.datadoghq.com/infrastructure/containers/container_images/#enable-sbom-collection)
- [Troubleshooting Cloud Security Vulnerabilities](https://docs.datadoghq.com/security/cloud_security_management/troubleshooting/vulnerabilities/)
