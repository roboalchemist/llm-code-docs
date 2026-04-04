# Source: https://grafbase.com/docs/platform/self-hosting/charts/dashboard.md

# Grafbase Dashboard

This reference documents the Kubernetes configuration options for the Grafbase Dashboard, which provides a web-based interface to manage your federated graphs.

## replicaCount

[Kubernetes ReplicationController Docs](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/)

**Defaults**:

```yaml
replicaCount: 1
```

## serviceAccount

[Kubernetes Service Account Docs](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)

**Defaults**:

```yaml
serviceAccount:
  # Controls service account creation
  create: true
  # Annotations to add to the service account
  annotations: {}
  # Service account name. Uses default if not set
  name: ''
```

## service

[Kubernetes Service Types](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types)

**Defaults**:

```yaml
service:
  # Either ClusterIP, NodePort, ExternalName, or LoadBalancer
  type: ClusterIP
  # Port to expose
  port: 8080
  # Target port
  targetPort: 8080
  # Name of the service
  name: http
  # The node port to use
  nodePort: 30081
```

## ingress

```yaml
ingress:
  # Enables ingress
  enabled: false
  # Ingress class
  className: 'nginx'
  hosts:
    # Hostnames and paths for the ingress
    - host: dashboard.local
      paths:
        - path: /*
          pathType: ImplementationSpecific
          backend:
            serviceName: dashboard
            servicePort: 8080
```

## autoscaling

[Kubernetes Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)

**Defaults**:

```yaml
autoscaling:
  # Enables autoscaling
  enabled: true
  # Minimum number of replicas
  minReplicas: 1
  # Maximum number of replicas
  maxReplicas: 2
  # Target CPU utilization percentage
  targetCPUUtilizationPercentage: 50
```

## configmap

Configuration values for the configmap used by the dashboard server.

```yaml
configmap:
  # Enable or disable the ConfigMap. Enabling will create a configmap with the given values and then mounted as env vars in the deployment.
  enabled: true
  # Cluster configmap to reference and mount its contents as environment variables.
  name: ''
  # Key-value pairs for configuration.
  values:
    # The port the service will expose.
    PORT: 8080
    # The host of the Grafbase API for web clients.
    GRAFBASE_API_HOST: http://localhost:30080
    # The host of the Grafbase API for the dashboard server (cluster internal host).
    GRAFBASE_API_HOST_INTERNAL: http://localhost:30080

    # The following environment variables are used to configure the OpenID Connect Authorization Code Grant flow with your IdP.
    OIDC_PROVIDER_TYPE: 'zitadel' # either 'zitadel' or 'generic' to use your own IdP directly.
    OIDC_ISSUER: null # The public issuer URL of your IdP. The other endpoints will be discovered through the standard OIDC mechanisms.
    OIDC_CLIENT_ID: null # The client ID of the Grafbase dashboard application inside your IdP.
    OIDC_SCOPES: null # OAuth scopes to request from the IdP. Space separated. Example: "openid profile email groups offline_access"
    OIDC_SIGNUP_HINT: false # Whether to show sign-up hint on authorization. Some IdPs require it.
    OIDC_ACCESS_TYPE: null # Optional access_type parameter for OAuth authorization (e.g., 'offline' for Google OAuth)
```

## secrets

Configuration values for the cluster secret.

```yaml
secrets:
  # Enable or disable the Secret. Enabling will create a secret with the given values and then mounted as env vars in the deployment.
  enabled: true
  name: ''
  values:
    # The secret key for cookie encryption.
    SESSION_ENCRYPTION_KEY: ASecretEncryptionKeyAtLeast32chars
    # If you configured OIDC based authentication, the client secret associated to the client identified by OIDC_CLIENT_ID.
    OIDC_CLIENT_SECRET: null
```