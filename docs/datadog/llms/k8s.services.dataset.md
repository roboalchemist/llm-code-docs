# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/k8s/k8s.services.dataset.md

---
title: Kubernetes Services
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Kubernetes Services
---

# Kubernetes Services

The Kubernetes Services table provides comprehensive information about Kubernetes services monitored by Datadog across your clusters. Each row represents a Kubernetes service and includes metadata about annotations, labels, service type (ClusterIP, NodePort, LoadBalancer, ExternalName), cluster IP, external IPs, external name for ExternalName services, external traffic policy (Cluster, Local), health check node ports, load balancer configuration (IP, source ranges), port configurations, pod selectors, session affinity settings (None, ClientIP), and whether not-ready endpoints should be published. This table enables you to monitor service discovery and networking, track load balancer configurations and external access points, analyze service-to-pod mappings via selectors, troubleshoot connectivity issues, monitor session affinity for stateful applications, and correlate service definitions with traffic patterns. You can filter and view resources by kube_service tag in Datadog. Services provide stable networking endpoints for accessing groups of pods, abstracting away pod IP changes and enabling load balancing.

```
k8s.services
```

## Fields

| Title                            | ID                               | Type | Data Type     | Description                                                                                                         |
| -------------------------------- | -------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------- |
| Annotations                      | annotations                      | core | hstore        | Key-value pairs containing annotations attached to the service, stored as hstore.                                   |
| Cluster Name                     | cluster_name                     | core | string        | The name of the Kubernetes cluster where the service is running.                                                    |
| Creation Timestamp               | creation_timestamp               | core | timestamp     | The timestamp when the service was created.                                                                         |
| Deletion Timestamp               | deletion_timestamp               | core | timestamp     | The timestamp when the service deletion was requested.                                                              |
| Labels                           | labels                           | core | hstore        | Key-value pairs containing labels attached to the service, stored as hstore.                                        |
| Service Name                     | name                             | core | string        | The name of the service.                                                                                            |
| Namespace                        | namespace                        | core | string        | The Kubernetes namespace where the service is running.                                                              |
| Spec Cluster IP                  | spec_cluster_ip                  | core | string        | The internal cluster IP address assigned to the service.                                                            |
| Spec External IPs                | spec_external_ips                | core | array<string> | List of external IP addresses for the service.                                                                      |
| Spec External Name               | spec_external_name               | core | string        | The external DNS name for ExternalName type services.                                                               |
| Spec External Traffic Policy     | spec_external_traffic_policy     | core | string        | The external traffic policy for the service (e.g., Cluster, Local).                                                 |
| Spec Health Check Node Port      | spec_health_check_node_port      | core | int64         | The health check node port for services with external traffic policy Local.                                         |
| Spec Load Balancer IP            | spec_load_balancer_ip            | core | string        | The requested load balancer IP address for LoadBalancer type services.                                              |
| Spec Load Balancer Source Ranges | spec_load_balancer_source_ranges | core | array<string> | List of source IP ranges allowed to access the load balancer.                                                       |
| Spec Ports                       | spec_ports                       | core | json          | The port configurations for the service, stored as JSON.                                                            |
| Spec Publish Not Ready Addresses | spec_publish_not_ready_addresses | core | bool          | Indicates whether endpoints that are not ready should be published.                                                 |
| Spec Selector                    | spec_selector                    | core | json          | The label selector used to select pods for the service, stored as JSON.                                             |
| Spec Session Affinity            | spec_session_affinity            | core | string        | The session affinity setting for the service (e.g., None, ClientIP).                                                |
| Spec Session Affinity Config     | spec_session_affinity_config     | core | json          | The session affinity configuration, stored as JSON.                                                                 |
| Spec Type                        | spec_type                        | core | string        | The type of service (e.g., ClusterIP, NodePort, LoadBalancer, ExternalName).                                        |
| Resource Tags                    | tags                             | core | hstore        | This field contains tags represented as key-value pairs, used to categorize and provide metadata about the service. |
| UID                              | uid                              | core | string        | The unique identifier of the service.                                                                               |
