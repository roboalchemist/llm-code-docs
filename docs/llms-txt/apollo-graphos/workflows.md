# Source: https://www.apollographql.com/docs/apollo-operator/workflows.md

# Workflows

The Apollo GraphOS Operator manages the lifecycle of GraphQL subgraphs and supergraphs in Kubernetes. Understanding how it works under the hood helps you choose the right deployment pattern for your existing architecture.

## Workflow Patterns

### 1. [Single Cluster Setup](https://www.apollographql.com/docs/apollo-operator/single-cluster)

**How it works:** All Subgraphs, SupergraphSchema, and Supergraph resources exist in the same cluster. This means the cluster becomes authoritative when composition occurs, so any subgraphs added via Studio UI or Rover will be deleted when composition is requested. This also means the Operator waits for all selected subgraph schemas to be available before composing the supergraph.

**When to use:**

* All your services run in Kubernetes
* You want the simplest possible setup
* Single team owns the entire stack

**Architectural benefits:**

* Complete operator-managed lifecycle
* Automatic subgraph discovery and composition
* Real-time schema synchronization
* Simplified monitoring and debugging

### 2. [Multi-Cluster and Hybrid Setup](https://www.apollographql.com/docs/apollo-operator/multi-cluster)

**How it works:** Subgraphs are distributed across multiple clusters or external systems, but SupergraphSchema and Supergraph are in a central cluster. Subgraphs running in other clusters or external systems are included by publishing them to Studio. The Operator uses `partial: true` so that any composition will include all subgraphs in the cluster and any defined in Studio.

**When to use:**

* Subgraph implementations are deployed in different clusters
* Some services run in Kubernetes, others don't
* You need service isolation for compliance
* You have multiple Kubernetes clusters
* You want centralized supergraph management

**Architectural benefits:**

* Team autonomy for subgraph deployment
* Service isolation across clusters
* Centralized supergraph management
* Requires cross-cluster networking
* Partial composition means some subgraphs may be missing

### 3. [Deploy Only Setup](https://www.apollographql.com/docs/apollo-operator/deploy-only)

**How it works:** All subgraphs are published externally via `rover subgraph publish`. The Supergraph resource directly references a graph variant in Apollo GraphOS.

**When to use:**

* You prefer external subgraph management
* You have complex CI/CD workflows
* You want Kubernetes supergraph benefits
* You're not ready for operator-managed subgraphs

**Architectural benefits:**

* Full control over subgraph publishing
* Kubernetes-native supergraph management
* CI/CD-driven subgraph workflows
* No operator-managed subgraphs
* Requires external subgraph management

## Architectural Decision Framework

### Consider Your Infrastructure

| Infrastructure Type              | Recommended Pattern      | Reasoning                                        |
| -------------------------------- | ------------------------ | ------------------------------------------------ |
| **Single Kubernetes cluster**    | Single Cluster           | Simplest setup, full operator benefits           |
| **Multiple Kubernetes clusters** | Multi-Cluster and Hybrid | Service isolation, centralized supergraphs       |
| **Mixed infrastructure**         | Multi-Cluster and Hybrid | Gradual migration, external service support      |
| **External-only subgraphs**      | Deploy Only              | Keep existing workflows, add Kubernetes benefits |

### Consider Your Team Structure

| Team Structure                        | Recommended Pattern      | Reasoning                        |
| ------------------------------------- | ------------------------ | -------------------------------- |
| **Single team**                       | Single Cluster           | Simplified coordination          |
| **Multiple teams, shared cluster**    | Single Cluster           | Use namespaces for isolation     |
| **Multiple teams, separate clusters** | Multi-Cluster and Hybrid | Team autonomy, service isolation |
| **Mixed ownership**                   | Multi-Cluster and Hybrid | Flexible ownership model         |

### Consider Your Operational Model

| Operational Model     | Recommended Pattern      | Reasoning                            |
| --------------------- | ------------------------ | ------------------------------------ |
| **Kubernetes-native** | Single Cluster           | Full operator lifecycle management   |
| **CI/CD-driven**      | Deploy Only              | Existing workflows, gradual adoption |
| **Mixed approach**    | Multi-Cluster and Hybrid | Flexibility during transition        |

## Key Architectural Considerations

### Composition Strategy

**Cluster Authoritative**

* All subgraphs are in the same Kubernetes cluster
* Operator waits for complete set before deploying
* Guarantees complete supergraph functionality

**Hybrid Authoritative (Multi-Cluster and Hybrid)**

* Subgraphs may be in multiple clusters, or exist outside of Kubernetes
* GraphOS composes subgraphs from multiple sources
* Requires `partial: true` in SupergraphSchema

**Studio Authoritative (Deploy Only)**

* Composition happens entirely in Apollo GraphOS
* No local subgraph management
* Fastest deployment (no local composition)
* Requires external subgraph management
