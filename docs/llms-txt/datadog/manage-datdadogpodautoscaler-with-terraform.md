# Source: https://docs.datadoghq.com/containers/guide/manage-datdadogpodautoscaler-with-terraform.md

---
title: Managing DatadogPodAutoscaler with Terraform
description: >-
  Deploy and manage DatadogPodAutoscaler custom resources for Kubernetes
  autoscaling using Terraform
breadcrumbs: >-
  Docs > Container Monitoring > Containers Guides > Managing
  DatadogPodAutoscaler with Terraform
source_url: >-
  https://docs.datadoghq.com/guide/manage-datdadogpodautoscaler-with-terraform/index.html
---

# Managing DatadogPodAutoscaler with Terraform

## Overview{% #overview %}

The DatadogPodAutoscaler (DPA) is a Kubernetes custom resource definition (CRD) that enables autoscaling of Kubernetes workloads using [Datadog Kubernetes Autoscaling (DKA)](https://docs.datadoghq.com/containers/monitoring/autoscaling/). This guide demonstrates how to manage DatadogPodAutoscaler resources using Terraform and HashiCorp's Kubernetes provider to deploy an autoscaling configuration.

## Prerequisites{% #prerequisites %}

Before you begin, ensure you have the following:

- **Kubernetes cluster**: A working Kubernetes cluster with access using `kubectl`
- **Terraform**: Terraform installed (version 0.13 or later recommended)
- **Datadog API credentials**: Valid Datadog API key and application key

## Project structure{% #project-structure %}

This guide uses a multi-stage deployment approach to ensure proper dependency creation for Terraform.

```gdscript3
.
âââ providers.tf              # Provider configurations
âââ variables.tf              # Input variables
âââ main.tf                   # Stage 1: Datadog secret and operator (CRDs)
âââ terraform.tfvars          # Example variable values
âââ datadogagent/             # Stage 2: DatadogAgent CRD resource
â   âââ main.tf               # DatadogAgent manifest
âââ nginx-dpa/                # Stage 3: Nginx application with DPA
â   âââ main.tf               # Nginx namespace, deployment, and DPA
```

## Deployment stages{% #deployment-stages %}

A multi-stage deployment approach is essential when working with Kubernetes custom resource definitions (CRDs) and Terraform. This ordered approach is necessary to ensure that you create and install the dependencies required for each stage in the process.

Kubernetes CRDs must be installed in the cluster before you can create custom resources that use them. The DatadogPodAutoscaler CRD is created when you install the Datadog Operator in Stage 1. Terraform needs to know about these CRDs before it can manage resources that depend on them.

The Terraform Kubernetes provider discovers available resource types at initialization time. If you try to create a DatadogPodAutoscaler resource before the CRD is installed, Terraform will fail because it doesn't recognize the custom resource type.

1. **Stage 1 (Datadog Operator and CRDs)**: Creates Datadog secret, Operator, and CRD
   - Datadog Operator using Helm (creates CRDs)
1. **Stage 2 (Datadog Agent)**: Deploys the Datadog Agent configured for Datadog Kubernetes Autoscaling
   - Datadog API and application secrets
   - DatadogAgent custom resource with Cluster Agent enabled
1. **Stage 3 (Autoscaled workload)**: Deploys application with DatadogPodAutoscaler
   - Nginx namespace and deployment
   - DatadogPodAutoscaler resource for autoscaling the nginx deployment

## Set up configuration files{% #set-up-configuration-files %}

First, set up the following configuration files for each stage in the process.

### Stage 1: Datadog Operator and CRDs{% #stage-1-datadog-operator-and-crds %}

In the `providers.tf` file:

```hcl
provider "kubernetes" {
  config_path = "~/.kube/config"
}

provider "helm" {
  kubernetes = {
    config_path = "~/.kube/config"
  }
}
```

In the `main.tf` file:

```hcl
resource "helm_release" "datadog_operator" {
  name       = "datadog-operator"
  namespace  = "datadog"
  repository = "https://helm.datadoghq.com"
  chart      = "datadog-operator"
  version    = "2.11.1" # You can update to the latest stable version

  create_namespace = true
}
```

### Stage 2: Datadog Agent{% #stage-2-datadog-agent %}

In the `datadogagent/variables.tf` file:

```hcl
variable "datadog_api_key" {
  description = "Datadog API key"
  type        = string
  sensitive   = true
}

variable "datadog_app_key" {
  description = "Datadog application key"
  type        = string
  sensitive   = true
}
```

In the `datadogagent/main.tf` file:

```hcl
provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_secret" "datadog_secret" {
  metadata {
    name      = "datadog-secret"
    namespace = "datadog"
  }

  data = {
    api-key = var.datadog_api_key
    app-key = var.datadog_app_key
  }

  type = "Opaque"
}

resource "kubernetes_manifest" "datadog" {
  manifest = {
    apiVersion = "datadoghq.com/v2alpha1"
    kind       = "DatadogAgent"
    metadata = {
      name      = "datadog"
      namespace = "datadog"
    }
    spec = {
      features = {
        autoscaling = {
          workload = {
            enabled = true
          }
        }
        eventCollection = {
          unbundleEvents = true
        }
      }
      global = {
        site = "datadoghq.com"
        credentials = {
          apiSecret = {
            secretName = "datadog-secret"
            keyName = "api-key"
          }
          appSecret = {
            secretName = "datadog-secret"
            keyName = "app-key"
          }
        }
        clusterName = "minikube-dka-demo"
        kubelet = {
          tlsVerify = false
        }
      }
      override = {
        clusterAgent = {
          env = [
            {
              name  = "DD_AUTOSCALING_FAILOVER_ENABLED"
              value = "true"
            }
          ]
        }
        nodeAgent = {
          env = [
            {
              name  = "DD_AUTOSCALING_FAILOVER_ENABLED"
              value = "true"
            }
          ]
        }
      }
    }
  }
}
```

### Stage 3: Application with DatadogPodAutoscaler{% #stage-3-application-with-datadogpodautoscaler %}

In the `nginx-dpa/main.tf` file:

```hcl
terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

# Create namespace for the application
resource "kubernetes_namespace" "nginx_demo" {
  metadata {
    name = "nginx-dka-demo"
  }
}

# Nginx deployment
resource "kubernetes_deployment" "nginx" {
  metadata {
    name      = "nginx"
    namespace = kubernetes_namespace.nginx_demo.metadata[0].name
    labels = {
      app = "nginx"
    }
  }

  spec {
    replicas = 3

    selector {
      match_labels = {
        app = "nginx"
      }
    }

    template {
      metadata {
        labels = {
          app = "nginx"
        }
      }

      spec {
        container {
          image = "nginx:latest"
          name  = "nginx"

          port {
            container_port = 80
          }

          resources {
            limits = {
              cpu    = "500m"
              memory = "512Mi"
            }
            requests = {
              cpu    = "250m"
              memory = "256Mi"
            }
          }
        }
      }
    }
  }
}

# Service for the nginx deployment
resource "kubernetes_service" "nginx" {
  metadata {
    name      = "nginx-service"
    namespace = kubernetes_namespace.nginx_demo.metadata[0].name
  }

  spec {
    selector = {
      app = "nginx"
    }

    port {
      port        = 80
      target_port = 80
    }

    type = "ClusterIP"
  }
}

# DatadogPodAutoscaler for nginx
resource "kubernetes_manifest" "datadogpodautoscaler_nginx_dka_demo_nginx" {
  manifest = {
    "apiVersion" = "datadoghq.com/v1alpha2"
    "kind" = "DatadogPodAutoscaler"
    "metadata" = {
      "name" = "nginx"
      "namespace" = "nginx-dka-demo"
    }
    "spec" = {
      "applyPolicy" = {
        "mode" = "Apply"
        "scaleDown" = {
          "rules" = [
            {
              "periodSeconds" = 1200
              "type" = "Percent"
              "value" = 20
            },
          ]
          "stabilizationWindowSeconds" = 600
          "strategy" = "Max"
        }
        "scaleUp" = {
          "rules" = [
            {
              "periodSeconds" = 120
              "type" = "Percent"
              "value" = 50
            },
          ]
          "stabilizationWindowSeconds" = 600
          "strategy" = "Max"
        }
        "update" = {
          "strategy" = "Auto"
        }
      }
      "constraints" = {
        "containers" = [
          {
            "enabled" = true
            "name" = "nginx"
          },
        ]
        "maxReplicas" = 100
        "minReplicas" = 3
      }
      "objectives" = [
        {
          "podResource" = {
            "name" = "cpu"
            "value" = {
              "type" = "Utilization"
              "utilization" = 70
            }
          }
          "type" = "PodResource"
        },
      ]
      "owner" = "Local"
      "targetRef" = {
        "apiVersion" = "apps/v1"
        "kind" = "Deployment"
        "name" = "nginx"
      }
    }
  }
}
```

## Deployment instructions{% #deployment-instructions %}

After you have set up the configuration files for each stage, follow these steps to deploy the components in the correct order.

### Stage 1: Datadog Operator and CRDs{% #stage-1-datadog-operator-and-crds-1 %}

Deploy the Datadog Operator and CRDs:

```bash
terraform init
terraform apply
```

Verify that the Datadog Operator and CRDs are deployed:

```bash
kubectl get crd
kubectl get pods -n datadog
```

You should see that the Datadog CRDs are created and the datadog-operator pod is running.

### Stage 2: Datadog Agent{% #stage-2-datadog-agent-1 %}

Create a `terraform.tfvars` file with your Datadog credentials:



```bash
cat > datadogagent/terraform.tfvars << EOF
datadog_api_key = "your-api-key-here"
datadog_app_key = "your-app-key-here"
EOF
```
Alternatively, set the `TF_VAR_datadog_api_key` and `TF_VAR_datadog_app_key` environment variables in your shell.


```bash
cd datadogagent
terraform init
terraform apply
```

Verify that the Datadog Agent is deployed:

```bash
kubectl get datadogagent -n datadog
```

You should see the Datadog Agent custom resource created. It should be in the `Running` state before proceeding. Also verify that the Datadog Agent and datadog-cluster-agent pods are running:

```bash
kubectl get pods -n datadog
```

### Stage 3: Application with DatadogPodAutoscaler{% #stage-3-application-with-datadogpodautoscaler-1 %}

Deploy the nginx application with DatadogPodAutoscaler:

```bash
cd ../nginx-dpa
terraform init
terraform apply
```

After deployment, verify that all components are working correctly.

Check Datadog Agent status:

```bash
kubectl get datadogagent -n datadog
kubectl describe datadogagent datadog -n datadog
```

Check DatadogPodAutoscaler status:

```bash
kubectl get datadogpodautoscaler -n nginx-dka-demo
kubectl describe datadogpodautoscaler nginx-autoscaler -n nginx-dka-demo
```

Congratulations, you have a workload managed by the Datadog Kubernetes Autoscaler!

## Cleanup{% #cleanup %}

To remove all resources, follow the reverse order of the deployment stages:

1. Clean up the deployed application (Stage 3):

   ```bash
   cd nginx-dpa
   terraform destroy
   ```

1. Clean up the Datadog Agent (Stage 2):

   ```bash
   cd ../datadogagent
   terraform destroy
   ```

1. Clean up the Datadog Operator and CRDs (Stage 1):

   ```bash
   cd ..
   terraform destroy
   ```

## Troubleshooting{% #troubleshooting %}

### Debugging commands{% #debugging-commands %}

Check DatadogPodAutoscaler events:

```bash
kubectl get events -n nginx-dka-demo --sort-by='.lastTimestamp'
```



Check Cluster Agent logs:

```bash
kubectl logs -n datadog -l agent.datadoghq.com/component=cluster-agent
```



## Further reading{% #further-reading %}

- [Kubernetes autoscaling guide: determine which solution is right for your use case](https://www.datadoghq.com/blog/kubernetes-autoscaling-datadog/)
- [Datadog Kubernetes Autoscaling](https://docs.datadoghq.com/containers/monitoring/autoscaling/)
- [Datadog Cluster Agent](https://docs.datadoghq.com/agent/cluster_agent/)
- [Terraform Kubernetes Provider documentation](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs)
- [Kubernetes Horizontal Pod Autoscaling documentation](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
