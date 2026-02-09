# Source: https://docs.datadoghq.com/cloudprem/configure/ingress.md

---
title: CloudPrem Ingress Configuration
description: >-
  Learn how to configure and manage ingress controllers for your CloudPrem
  deployment
breadcrumbs: Docs > CloudPrem > Configure CloudPrem > CloudPrem Ingress Configuration
---

# CloudPrem Ingress Configuration

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### CloudPrem is in Preview

Join the CloudPrem Preview to access new self-hosted log management features.

[Request Access](https://www.datadoghq.com/product-preview/cloudprem/)
{% /callout %}

## Overview{% #overview %}

Ingress is a critical component of your CloudPrem deployment. The Helm chart automatically creates two ingress configurations called public ingress and internal ingress. If the AWS Load Balancer Controller is installed on the cluster, it provisions one ALB per ingress configuration. Each load balancer can be further configured using ingress annotations.

## Public ingress{% #public-ingress %}

{% alert level="danger" %}
Only the CloudPrem gRPC API endpoints (paths starting with `/cloudprem`) perform mutual TLS authentication. Exposing any other endpoints through the public ingress introduces a security risk, as those endpoints would be accessible over the internet without authentication. Always restrict non-gRPC endpoints to the internal ingress.
{% /alert %}

The public ingress is essential for enabling Datadog's control plane and query service to manage and query CloudPrem clusters over the public internet. It provides secure access to the CloudPrem gRPC API through the following mechanisms:

- Creates an internet-facing AWS Application Load Balancer (ALB) that accepts traffic from Datadog services
- Implements TLS encryption with termination at the load balancer level
- Uses HTTP/2 (gRPC) for communication between the ALB and CloudPrem cluster
- Requires mutual TLS (mTLS) authentication where Datadog services must present valid client certificates
- Configures the ALB in TLS passthrough mode to forward client certificates to CloudPrem pods with the `X-Amzn-Mtls-Clientcert` header
- Rejects requests that are missing valid client certificates or the certificate header

This setup ensures that only authenticated Datadog services can access the CloudPrem cluster while maintaining secure encrypted communication end-to-end.

{% image
   source="https://datadog-docs.imgix.net/images/cloudprem/ingress/cloudprem_public_ingress1.3958ce4146a5a6f5851bc3b08d114908.png?auto=format"
   alt="Diagram showing CloudPrem public ingress architecture with Datadog services connecting through an internet-facing AWS ALB using mTLS authentication to access the CloudPrem gRPC API" /%}

### IP Allowlisting{% #ip-allowlisting %}

The Datadog control plane and query services connect to CloudPrem clusters using a set of fixed IP ranges, which can be retrieved for each Datadog site from the Datadog [IP Ranges API](https://docs.datadoghq.com/api/latest/ip-ranges/), specifically under the "webhooks" section. For example, to fetch the IP ranges for the datadoghq.eu site, you can run:

```
curl -X GET "https://ip-ranges.datadoghq.eu/" \
      -H "Accept: application/json" |
      jq '.webhooks'
```

## Internal ingress{% #internal-ingress %}

The internal ingress enables log ingestion from Datadog Agents and other log collectors within your environment through HTTP.

{% image
   source="https://datadog-docs.imgix.net/images/cloudprem/ingress/internal_ingress.b39b7d43de4028e14a49a8114e69a078.png?auto=format"
   alt=" Internal ingress with ALB provisioned by Helm chart" /%}

By default, the chart creates an internal AWS Application Load Balancer (ALB) to route HTTP traffic to the appropriate CloudPrem services based on the requested API endpoint path. However, if you prefer to use your own ingress controller (such as HAProxy, NGINX, or Traefik), you can disable the default internal ALB and configure your controller with the following routing rules:

```
rules:
- http:
    paths:
      # Ingest (Quickwit, ES, Datadog) endpoints to indexers
      - path: /api/v1/*/ingest
        pathType: ImplementationSpecific
        backend:
          service:
            name: <RELEASE_NAME>-indexer
            port:
              name: rest
      - path: /api/v1/_elastic/bulk
        pathType: Prefix
        backend:
          service:
            name: <RELEASE_NAME>-indexer
            port:
              name: rest
      - path: /api/v1/_elastic/*/_bulk
        pathType: ImplementationSpecific
        backend:
          service:
            name: <RELEASE_NAME>-indexer
            port:
              name: rest
      - path: /api/v2/logs
        pathType: Prefix
        backend:
          service:
            name: <RELEASE_NAME>-indexer
            port:
              name: rest
      # Index management API endpoints to metastores
      - path: /api/v1/indexes
        pathType: Prefix
        backend:
          service:
            name: <RELEASE_NAME>-metastore
            port:
              name: rest
      # Everything else to searchers
      - path: /*
        pathType: ImplementationSpecific
        backend:
          service:
            name: <RELEASE_NAME>-searcher
            port:
              name: rest
```

{% image
   source="https://datadog-docs.imgix.net/images/cloudprem/ingress/internal_ingress_nginx_controller.502d1bbf279372ca4d48593652cc344a.png?auto=format"
   alt="CloudPrem internal ingress configuration using NGINX ingress controller showing path routing to indexer, metastore, and searcher services" /%}

## Further reading{% #further-reading %}

- [Set up Log Ingestion](https://docs.datadoghq.com/cloudprem/ingest/)
- [Monitor CloudPrem](https://docs.datadoghq.com/cloudprem/operate/monitoring/)
