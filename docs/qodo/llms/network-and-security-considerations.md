# Source: https://docs.qodo.ai/qodo-documentation/on-prem/qodo-on-premise/network-and-security-considerations.md

# Network and Security Considerations

#### Network Requirements

**Outbound Connectivity Required:**

* `artifacts-self-hosted.qodo.ai` - Helm chart and image registry
* `artif-reg-self-hosted.codium.ai` - Container images
* AI model provider endpoints (api.openai.com, api.anthropic.com, etc.)
* Git provider APIs (github.com, gitlab.com, or your self-hosted instances)

**Inbound Connectivity Required:**

* Git provider webhooks must reach your ingress endpoints
* Developer IDEs must reach Qodo API endpoints
* (For Context Engine) Context retriever MCP endpoint

**Firewall Considerations:**

* Allow outbound HTTPS (443) to all external dependencies
* Allow inbound HTTPS (443) for webhooks and API access
* Ensure K8s cluster can reach external PostgreSQL if not in-cluster

#### Security Best Practices

**Secrets Management:**

* Use Kubernetes secrets for all sensitive data
* Never commit `.secrets.toml` files to version control
* Consider External Secrets Operator for centralized secret management
* Rotate API keys and credentials regularly

**Network Policies:**

* Restrict pod-to-pod communication
* Limit egress to only required endpoints
* Implement namespace isolation

**Access Control:**

* Use RBAC for Kubernetes access
* Implement principle of least privilege
* Use service accounts with minimal permissions

**TLS/SSL:**

* Always use TLS for external endpoints
* Use cert-manager for certificate management
* Configure proper certificate validation

**Image Security:**

* Images come from trusted Replicated registry
* Regular updates through Helm for security patches
* Scan images for vulnerabilities if required by policy
