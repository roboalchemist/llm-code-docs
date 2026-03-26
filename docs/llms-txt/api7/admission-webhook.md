# Source: https://docs.api7.ai/ingress-controller/troubleshoot/admission-webhook.md

# Understand Admission Webhook

When you apply resources managed by the Ingress Controller, an admission webhook validates your configuration before Kubernetes accepts the request. This helps catch configuration errors early, before they cause runtime issues or service disruptions.

The admission webhook is **enabled by default** when you install APISIX or API7 Ingress Controller using Helm, which sets `webhook.enabled=true`. It intercepts resource creation and update requests before Kubernetes accepts them, validates them against the rules, and either approves the request or returns a detailed error message. This ensures:

* **Schema Validation**: Resource specifications comply with requirements
* **Configuration Safety**: Invalid resource references, such as non-existent secrets or services, are detected immediately
* **Conflict Prevention**: Duplicate or conflicting configurations are identified before deployment
* **TLS/SSL Verification**: Certificate configurations are validated for correctness

The webhook operates silently in the background during regular operations. You will only see webhook messages when there are potential configuration issues that need attention.

This document explains common webhook messages and helps you understand how to resolve them.

## SSL Certificate Conflicts[â](#ssl-certificate-conflicts "Direct link to SSL Certificate Conflicts")

When you see certificate conflict errors, it means you are trying to use different TLS certificates for the same hostname across multiple resources within the same GatewayProxy scope. The admission webhook prevents this to avoid ambiguous routing and security issues.

```
SSL configuration conflicts detected:
- Host '<hostname>' is already configured with a different certificate in <resource-type>/<namespace>/<resource-name>
```

SSL certificate conflicts typically occur when duplicate TLS resources are created for the same hostname or when certificate rotation mistakes result in a new TLS resource being created instead of updating the existing one. In all cases, the webhook prevents the conflict by rejecting the new resource and providing details about which existing resource is already using that hostname with a different certificate.

## GatewayProxy Conflicts[â](#gatewayproxy-conflicts "Direct link to GatewayProxy Conflicts")

When you create or update a GatewayProxy resource, the admission webhook validates that it does not conflict with existing GatewayProxy resources. These errors would block resource creation to prevent multiple controllers from interfering with the same control plane instance.

```
gateway proxy configuration conflict: GatewayProxy <namespace>/<new-gatewayproxy-name> and <namespace>/<existing-gatewayproxy-name> both target Service <namespace>/<service-name> port <port> while sharing <admin-key>

gateway proxy configuration conflict: GatewayProxy <namespace>/<new-gatewayproxy-name> and <namespace>/<existing-gatewayproxy-name> both target control plane endpoints [<endpoint-url>] while sharing <admin-key>
```

GatewayProxy conflicts typically occur when two GatewayProxy resources are configured to manage the same control plane instance using the same admin key (either the same inline value or the same secret reference).

To resolve this conflict, identify all GatewayProxy resources and determine which one should remain. If you genuinely need multiple GatewayProxy resources, ensure they target different control plane instances.

## Missing Service References[â](#missing-service-references "Direct link to Missing Service References")

When you create or update resources that route traffic to backend services, the admission webhook validates that the referenced Kubernetes services exist. If the service referenced by your resource does not exist, you will see a warning message such as:

```
Warning: Referenced Service '<namespace>/<service-name>' not found
```

Unlike errors, warnings allow the resource to be created, but traffic routing will fail until the backend services exist.

Missing service references typically occur when there are typos in service names or namespaces, or when the referenced service has not been created. To resolve this issue, verify that the service exists in the correct namespace, check for any spelling errors in the service reference, and create the service before applying the resource that depends on it.

## Missing Secret References[â](#missing-secret-references "Direct link to Missing Secret References")

When you create or update resources that reference Kubernetes secrets for TLS certificates, authentication credentials, or plugin configurations, the admission webhook validates that these secrets exist and contain the required keys.

If the secret referenced by your resource does not exist, you will see a warning message such as:

```
Warning: Referenced Secret '<namespace>/<secret-name>' not found
```

If the secret referenced by your resource does not contain the required key (such as missing `password` key for basic authentication), you will see a warning message such as:

```
Warning: Secret key '<key-name>' not found in Secret '<namespace>/<secret-name>'
```

Unlike errors, warnings allow the resource to be created, but the affected functionality will not work correctly until the referenced secrets are properly configured.

To resolve this issue, ensure that the required secret is created before applying the resource that references it, verify that it contains all required keys, and double-check the secretâs name and namespace.

## Missing Gateway References[â](#missing-gateway-references "Direct link to Missing Gateway References")

When you create or update a Gateway or IngressClass that references a GatewayProxy, the admission webhook validates that the GatewayProxy exists. If the GatewayProxy referenced by your resource does not exist, you will see a warning message such as:

```
Warning: Referenced GatewayProxy '<namespace>/<gatewayproxy-name>' not found
```

Unlike errors, warnings allow the resource to be created, but the affected functionality will not work correctly until the referenced GatewayProxy is properly configured.

To resolve this issue, ensure that the GatewayProxy exists in the correct namespace and check for any spelling errors in the GatewayProxy reference.
