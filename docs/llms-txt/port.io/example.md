# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/argocd/example.md

# Examples

To view and test the integration's mapping against examples of the third-party API responses, use the jq playground in your [data sources page](https://app.getport.io/settings/data-sources). Find the integration in the list of data sources and click on it to open the playground.

## Cluster[â](#cluster "Direct link to Cluster")

**Cluster blueprint (click to expand)**

Create in Port

```
  {
    "identifier": "argocdCluster",
    "description": "This blueprint represents an ArgoCD cluster",
    "title": "ArgoCD Cluster",
    "icon": "Argo",
    "schema": {
      "properties": {
        "applicationsCount": {
          "title": "Applications Count",
          "type": "number",
          "description": "The number of applications managed by Argo CD on the cluster",
          "icon": "DefaultProperty"
        },
        "serverVersion": {
          "title": "Server Version",
          "type": "string",
          "description": "Contains information about the Kubernetes version of the cluster",
          "icon": "DefaultProperty"
        },
        "labels": {
          "title": "Labels",
          "type": "object",
          "description": "Contains information about cluster metadata",
          "icon": "DefaultProperty"
        },
        "updatedAt": {
          "icon": "DefaultProperty",
          "title": "Updated At",
          "type": "string",
          "format": "date-time"
        },
        "server": {
          "title": "Server",
          "description": "The API server URL of the Kubernetes cluster",
          "type": "string",
          "icon": "DefaultProperty"
        }
      },
      "required": []
    },
    "mirrorProperties": {},
    "calculationProperties": {},
    "relations": {}
  }
```

**Integration configuration (click to expand)**

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: cluster
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .name
          title: .name
          blueprint: '"argocdCluster"'
          properties:
            applicationsCount: .info.applicationsCount
            serverVersion: .serverVersion
            labels: .labels
            updatedAt: .connectionState.attemptedAt
            server: .server
```

## Namespace[â](#namespace "Direct link to Namespace")

**Namespace blueprint (click to expand)**

Create in Port

```
  {
    "identifier": "argocdNamespace",
    "description": "This blueprint represents an ArgoCD namespace",
    "title": "ArgoCD Namespace",
    "icon": "Argo",
    "schema": {
      "properties": {},
      "required": []
    },
    "aggregationProperties": {},
    "mirrorProperties": {},
    "calculationProperties": {},
    "relations": {
      "cluster": {
        "title": "ArgoCD Cluster",
        "target": "argocdCluster",
        "required": false,
        "many": false
      }
    }
  }
```

**Integration configuration (click to expand)**

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: cluster
    selector:
      query: "true"
    port:
      itemsToParse: .namespaces
      entity:
        mappings:
          identifier: .name + "-" + .item | tostring
          title: .name + "-" + .item
          blueprint: '"argocdNamespace"'
          properties: {}
          relations:
            cluster: .name
```

## Project[â](#project "Direct link to Project")

**Project blueprint (click to expand)**

Create in Port

```
  {
    "identifier": "argocdProject",
    "description": "This blueprint represents an ArgoCD Project",
    "title": "ArgoCD Project",
    "icon": "Argo",
    "schema": {
      "properties": {
        "createdAt": {
          "title": "Created At",
          "type": "string",
          "format": "date-time",
          "icon": "DefaultProperty"
        },
        "description": {
          "title": "Description",
          "description": "Project description",
          "type": "string",
          "icon": "DefaultProperty"
        }
      },
      "required": []
    },
    "mirrorProperties": {},
    "calculationProperties": {},
    "relations": {}
  }
```

**Integration configuration (click to expand)**

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: project
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .metadata.name
          title: .metadata.name
          blueprint: '"argocdProject"'
          properties:
            createdAt: .metadata.creationTimestamp
            description: .spec.description
```

## Application[â](#application "Direct link to Application")

**Application blueprint (click to expand)**

Create in Port

```
  {
    "identifier": "argocdApplication",
    "description": "This blueprint represents an ArgoCD Application",
    "title": "Running Service",
    "icon": "Argo",
    "schema": {
      "properties": {
        "gitRepo": {
          "type": "string",
          "icon": "Git",
          "title": "Repository URL",
          "description": "The URL of the Git repository containing the application source code"
        },
        "gitPath": {
          "type": "string",
          "title": "Path",
          "description": "The path within the Git repository where the application manifests are located"
        },
        "destinationServer": {
          "type": "string",
          "title": "Destination Server",
          "description": "The URL of the target cluster's Kubernetes control plane API"
        },
        "revision": {
          "type": "string",
          "title": "Revision",
          "description": "Revision contains information about the revision the comparison has been performed to"
        },
        "targetRevision": {
          "type": "string",
          "title": "Target Revision",
          "description": "Target Revision defines the revision of the source to sync the application to. In case of Git, this can be commit, tag, or branch"
        },
        "syncStatus": {
          "type": "string",
          "title": "Sync Status",
          "enum": [
            "Synced",
            "OutOfSync",
            "Unknown"
          ],
          "enumColors": {
            "Synced": "green",
            "OutOfSync": "red",
            "Unknown": "lightGray"
          },
          "description": "Status is the sync state of the comparison"
        },
        "healthStatus": {
          "type": "string",
          "title": "Health Status",
          "enum": [
            "Healthy",
            "Missing",
            "Suspended",
            "Degraded",
            "Progressing",
            "Unknown"
          ],
          "enumColors": {
            "Healthy": "green",
            "Missing": "yellow",
            "Suspended": "purple",
            "Degraded": "red",
            "Progressing": "blue",
            "Unknown": "lightGray"
          },
          "description": "Status holds the status code of the application or resource"
        },
        "createdAt": {
          "title": "Created At",
          "type": "string",
          "format": "date-time",
          "description": "The created timestamp of the application"
        },
        "labels": {
          "type": "object",
          "title": "Labels",
          "description": "Map of string keys and values that can be used to organize and categorize object"
        },
        "annotations": {
          "type": "object",
          "title": "Annotations",
          "description": "Annotations are unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata"
        }
      },
      "required": []
    },
    "mirrorProperties": {},
    "calculationProperties": {},
    "relations": {
      "project": {
        "title": "ArgoCD Project",
        "target": "argocdProject",
        "required": false,
        "many": false
      },
      "cluster": {
        "title": "ArgoCD Cluster",
        "target": "argocdCluster",
        "required": false,
        "many": false
      },
      "namespace": {
        "title": "ArgoCD Namespace",
        "target": "argocdNamespace",
        "required": false,
        "many": false
      }
    }
  }
```

**Integration configuration (click to expand)**

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: application
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .metadata.uid
          title: .metadata.name
          blueprint: '"argocdApplication"'
          properties:
            gitRepo: .spec.source.repoURL
            gitPath: .spec.source.path
            destinationServer: .spec.destination.server
            revision: .status.sync.revision
            targetRevision: .spec.source.targetRevision
            syncStatus: .status.sync.status
            healthStatus: .status.health.status
            createdAt: .metadata.creationTimestamp
            labels: .metadata.labels
            annotations: .metadata.annotations
          relations:
            project: .spec.project
            namespace: .metadata.namespace
            cluster: .spec.destination.name
```

## Deployment history[â](#deployment-history "Direct link to Deployment history")

**Deployment history blueprint (click to expand)**

Create in Port

```
  {
    "identifier": "argocdDeploymentHistory",
    "description": "This blueprint represents an ArgoCD deployment history",
    "title": "ArgoCD Deployment History",
    "icon": "Argo",
    "schema": {
      "properties": {
        "deployedAt": {
          "title": "Deployed At",
          "type": "string",
          "format": "date-time"
        },
        "deployStartedAt": {
          "title": "Deploy Started At",
          "type": "string",
          "format": "date-time"
        },
        "revision": {
          "title": "Revision",
          "type": "string"
        },
        "initiatedBy": {
          "title": "Initiated By",
          "type": "string"
        },
        "repoURL": {
          "title": "Repository URL",
          "type": "string"
        },
        "sourcePath": {
          "title": "Source Path",
          "type": "string"
        }
      },
      "required": []
    },
    "mirrorProperties": {},
    "calculationProperties": {},
    "aggregationProperties": {},
    "relations": {
      "application": {
        "title": "Application",
        "target": "argocdApplication",
        "required": false,
        "many": false
      }
    }
  }
```

**Integration configuration (click to expand)**

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: application
    selector:
      query: "true"
    port:
      itemsToParse: .status.history
      entity:
        mappings:
          identifier: .metadata.uid + "-" + (.item.id | tostring)
          title: .metadata.name + "-" + (.item.id | tostring)
          blueprint: '"argocdDeploymentHistory"'
          properties:
            deployedAt: .item.deployedAt
            deployStartedAt: .item.deployStartedAt
            revision: .item.source.repoURL + "/commit/" + .item.revision
            initiatedBy: .item.initiatedBy.username
            repoURL: .item.source.repoURL
            sourcePath: .item.source.path
          relations:
            application: .metadata.uid
```

## Kubernetes Resource[â](#kubernetes-resource "Direct link to Kubernetes Resource")

**Images blueprint (click to expand)**

Create in Port

```
 {
    "identifier": "image",
    "description": "This blueprint represents an image",
    "title": "Image",
    "icon": "AWS",
    "schema": {
      "properties": {},
      "required": []
    },
    "mirrorProperties": {},
    "calculationProperties": {},
    "aggregationProperties": {},
    "relations": {}
  }
```

**Kubernetes resource blueprint (click to expand)**

Create in Port

```
  {
    "identifier": "argocdKubernetesResource",
    "description": "This blueprint represents an ArgoCD kubernetes resource",
    "title": "Kubernetes Resource",
    "icon": "Argo",
    "schema": {
      "properties": {
        "kind": {
          "title": "Kind",
          "type": "string"
        },
        "version": {
          "title": "Version",
          "type": "string"
        },
        "namespace": {
          "title": "Namespace",
          "type": "string"
        },
        "labels": {
          "type": "object",
          "title": "Labels"
        },
        "annotations": {
          "type": "object",
          "title": "Annotations"
        }
      },
      "required": []
    },
    "mirrorProperties": {
      "healthStatus": {
        "title": "Health Status",
        "path": "application.healthStatus"
      },
      "syncStatus": {
        "title": "Sync Status",
        "path": "application.syncStatus"
      }
    },
    "calculationProperties": {},
    "aggregationProperties": {},
    "relations": {
      "application": {
        "title": "Application",
        "target": "argocdApplication",
        "required": false,
        "many": false
      },
      "image": {
        "title": "Image",
        "target": "image",
        "required": false,
        "many": false
      }
    }
  }
```

**Integration configuration (click to expand)**

```
createMissingRelatedEntities: true
deleteDependentEntities: true
resources:
  - kind: managed-resource
    selector:
      query: "true"
    port:
      entity:
        mappings:
          identifier: .__application.metadata.uid + "-" + .kind + "-" + .name
          title: .__application.metadata.name + "-" + .kind + "-" + .name
          blueprint: '"argocdKubernetesResource"'
          properties:
            kind: .kind
            namespace: .namespace
            version: if .kind == "Deployment" then .resourceVersion else null end
            annotations: (.liveState // .targetState) | fromjson | .metadata.annotations
            labels: (.liveState // .targetState) | fromjson | .metadata.labels
          relations:
            application: .__application.metadata.uid
            image: >-
              if .kind == "Deployment" then (.liveState // .targetState) |
              fromjson | .spec.template.spec.containers[0].image else null end
```
