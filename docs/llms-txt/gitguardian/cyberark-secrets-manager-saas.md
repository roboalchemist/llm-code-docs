# Source: https://docs.gitguardian.com/ggscout-docs/integrations/secret-managers/cyberark-secrets-manager-saas.md

# CyberArk Secrets Manager SaaS

> Guide to configuring ggscout to collect and monitor secrets from CyberArk Secrets Manager SaaS, with multiple authentication modes.

# CyberArk Secrets Manager SaaS Integration

ggscout supports integration with CyberArk Secrets Manager SaaS to collect and monitor your secrets. This guide will help you set up and configure the integration.

## Supported Features

- Multiple secret versions collection
- CyberArk authentication
- Tenant-specific configuration
- Subdomain support

## Configuration

The following table lists the available configuration options for ggscout when integrating with CyberArk Secrets Manager SaaS:

| Parameter            | Description                                                                               | Required | Default Value |
|----------------------|-------------------------------------------------------------------------------------------|----------|-------------|
| `type`               | Must be set to `"cyberarksaas"`                                                            | Yes |             |
| `auth.auth_mode`     | Authentication mode (one of: "cyber_ark", "workload", "k8s")                              | Yes |             |
| `subdomain`          | Your company's subdomain                                                                  | Yes |             |
| `fetch_all_versions` | Whether to collect all versions of secrets                                                | Yes |             |
| `mode`               | Integration mode (one of:  "read", "write", "read/write")                                 | No | "read" |
| `env`                | Environment label for categorizing secrets (e.g., "production", "staging", "development") | No |             |
| `owner`              | Owner of this source (an email, usually of an employee or a team)                         | No |             |
| `include`            | List of path patterns to include in secret collection                                     | No |             |
| `exclude`            | List of path patterns to exclude from secret collection                                   | No |             |

With additional parameters depending on the chosen authentication mode:

For CyberArk Authentication:

| Parameter            | Description | Required | Default Value |
|----------------------|-------------|----------|-------------|
| `auth.client_id`     | The client ID for authentication | Yes |             |
| `auth.client_secret` | The client secret for authentication | Yes |             |
| `auth.tenant_id`     | The tenant ID | Yes |             |

For Workload Authentication:

| Parameter      | Description | Required | Default Value |
|----------------|-------------|----------|-------------|
| `auth.api_key` | Your Conjur API key | Yes |             |
| `auth.login`   | Your Conjur login | Yes |             |

For Kubernetes Authentication:

| Parameter         | Description | Required | Default Value |
|-------------------|-------------|----------|-------------|
| `auth.service_id` | The ID of your JWT authenticator in CyberArk Secrets Manager SaaS | Yes | |

## Authentication

ggscout supports multiple authentication methods for CyberArk Secrets Manager SaaS:

### CyberArk Authentication

```toml
[sources.cyberarksaas]
type = "cyberarksaas"
auth.auth_mode = "cyber_ark"
auth.client_id = "${CYBERARK_CLIENT_ID}"
auth.client_secret = "${CYBERARK_CLIENT_SECRET}"
auth.tenant_id = "${CYBERARK_TENANT_ID}"
cyberarksaas_url = "${CYBERARK_SAAS_URL}"
subdomain = "my-company"
fetch_all_versions = true
mode = "read"
env = "production"
owner = "devops-team@example.com"

[[sources.cyberarksaas.include]]
resource_ids = ["app/*", "database/*", "api-key"]

[[sources.cyberarksaas.exclude]]
resource_ids = ["test/*", "temp/*", "old-secret"]
```

### Workload Authentication

```toml
[sources.cyberarksaas]
type = "cyberarksaas"
auth.auth_mode = "workload"
api_key = "${CONJUR_API_KEY}"
login = "${CONJUR_LOGIN}"
subdomain = "my-company"
fetch_all_versions = true
mode = "read"
env = "production"
owner = "devops-team@example.com"

[[sources.cyberarksaas.include]]
resource_ids = ["app/*", "database/*", "api-key"]

[[sources.cyberarksaas.exclude]]
resource_ids = ["test/*", "temp/*", "old-secret"]
```

### Kubernetes Authentication

```toml
[sources.cyberarksaas]
type = "cyberarksaas"
auth.auth_mode = "k8s"
auth.service_id = "k8s-cluster-name"
subdomain = "my-company"
fetch_all_versions = true
mode = "read"
env = "production"
owner = "devops-team@example.com"

[[sources.cyberarksaas.include]]
resource_ids = ["app/*", "database/*", "api-key"]

[[sources.cyberarksaas.exclude]]
resource_ids = ["test/*", "temp/*", "old-secret"]
```

#### Detailed Setup Instructions

For applications running in Kubernetes clusters, you can configure CyberArk Secrets Manager SaaS to use JWT-based authentication. This allows your Kubernetes workloads to authenticate with CyberArk Secrets Manager SaaS using service account tokens.

#### Prerequisites

- A running CyberArk Secrets Manager SaaS instance
- A running Kubernetes cluster
- `kubectl` CLI installed and configured

#### Step 1: Retrieve Kubernetes OIDC Configuration

##### For AWS EKS

Get the OIDC issuer URL for your EKS cluster:

```bash
aws eks describe-cluster --name <YOUR_EKS_CLUSTER_NAME> --query "cluster.identity.oidc.issuer" --output text
```

The output will be a URL like `https://oidc.eks.us-east-1.amazonaws.com/id/EXAMPLED5A3C59576A0175F11F3414644`.

The JWKS URI is the issuer URL with `/keys` appended:
`https://oidc.eks.us-east-1.amazonaws.com/id/EXAMPLED5A3C59576A0175F11F3414644/keys`

##### For Other Kubernetes Clusters

For clusters that expose the OIDC discovery endpoint:

```bash
# Get the OIDC issuer URL
kubectl get --raw /.well-known/openid-configuration | jq -r '.issuer'

# Get the public keys (JWKS)
kubectl get --raw /openid/v1/jwks
```

#### Step 2: Configure JWT Authenticator in CyberArk Secrets Manager SaaS

You can create the JWT authenticator using the CyberArk Secrets Manager SaaS UI, API, or CLI.

##### Using CyberArk Secrets Manager SaaS UI

1. Navigate to the **Authenticators** page in CyberArk Secrets Manager SaaS
2. Click **Create authenticator**
3. Select **JWT** as the authenticator type
4. Enter a unique name for the authenticator (e.g., `k8s-cluster-name`)
5. Configure the following variables:

| Variable | Description | Required | Example Value |
|----------|-------------|------|---------------|
| `jwks-uri` | The JWKS URI of your Kubernetes cluster | Yes (or use `public-keys`) | `https://oidc.eks.us-east-1.amazonaws.com/id/EXAMPLE/keys` |
| `public-keys` | JWKS content as JSON string | Yes (or use `jwks-uri`) | Use for local/private clusters |
| `issuer` | The OIDC issuer URL | Yes | `https://oidc.eks.us-east-1.amazonaws.com/id/EXAMPLE` |
| `token-app-property` | JWT claim for application identity | Yes | `sub` |
| `audience` | Expected audience for the JWT | Recommended | `cyberark` |

##### Policy Example

When using policy files, your JWT authenticator policy should look like this:

```yaml
- !policy
  id: conjur/authn-jwt/k8s-cluster-name
  body:
  - !webservice
    annotations:
      description: JWT authenticator for Kubernetes cluster

  - !variable
    id: jwks-uri

  - !variable
    id: issuer

  - !variable
    id: token-app-property

  - !variable
    id: audience

  - !group users

  - !host-factory
    id: host-factory
    layers: [ !layer users ]
```

Then populate the variables:

```bash
# Set the JWKS URI
conjur variable set -i conjur/authn-jwt/k8s-cluster-name/jwks-uri -v "https://oidc.eks.us-east-1.amazonaws.com/id/EXAMPLE/keys"

# Set the issuer
conjur variable set -i conjur/authn-jwt/k8s-cluster-name/issuer -v "https://oidc.eks.us-east-1.amazonaws.com/id/EXAMPLE"

# Set the token app property (IMPORTANT: Use 'sub' for Kubernetes)
conjur variable set -i conjur/authn-jwt/k8s-cluster-name/token-app-property -v "sub"

# Set the audience
conjur variable set -i conjur/authn-jwt/k8s-cluster-name/audience -v "conjur"
```

#### Step 3: Create Workload Branch and Identity

Before creating workloads in CyberArk Secrets Manager SaaS, you need to set up the policy structure and workload identities.

##### Create Policy Branch (CLI Required)

If you're using the UI to create workloads, you must first create the policy branch using the CLI, as this cannot be done through the UI.

1. **Log in to Conjur CLI**:
   ```bash
   conjur login
   ```

2. **Create the workload branch policy**:

   Save the following as `workload-branch.yaml`:
   ```yaml
   - !policy
     id: <policy-id>
   ```

   Where `<policy-id>` is the name of your branch (for example, `myspace/jwt-apps` or `k8s-apps`).

3. **Load the policy branch**:
   ```bash
   conjur policy load -f workload-branch.yaml -b data
   ```

##### Create Workload Identity

After creating the policy branch, you can create the workload identity using either the UI or CLI.

###### Option A: Using CyberArk Secrets Manager SaaS UI

1. Navigate to **Workloads** in the CyberArk Secrets Manager SaaS UI
2. Click **Create workload**
3. Select **JWT** as the authentication method
4. Choose your JWT authenticator (e.g., `k8s-cluster-name`)
5. Configure the workload:
   - **Workload ID**: `system:serviceaccount:my-namespace:my-service-account`
   - **Policy Branch**: The branch you created (e.g., `myspace/jwt-apps`)
   - **Annotations**: Add relevant metadata
     - `kubernetes/namespace`: `my-namespace`
     - `kubernetes/service-account`: `my-service-account`

###### Option B: Using CLI Policy (Detailed Steps)

**Step 1: Create the workload host policy**

Save the following policy in a file named `authn-jwt-hosts.yaml`:

```yaml
- !policy
  id: <policy-id>
  body:
    - !group
    - !host
      id: <host-id>
      annotations:
        authn-jwt/<service-id>/<jwt-claim-name>: <jwt-claim-value>

    - !grant
      role: !group
      member: !host
```

Where:
- `<policy-id>` is the name of the branch (e.g., `myspace/jwt-apps` or `k8s-apps`)
- `<host-id>` is the name of the workload. **For Kubernetes JWT authentication using `token-app-property`, this must be the value of the JWT claim** (e.g., `system:serviceaccount:my-namespace:my-service-account`)
- `<service-id>` is the name of your JWT authenticator (e.g., `k8s-cluster-name`)
- `<jwt-claim-name>` is the name of a JWT claim (e.g., `sub`, `namespace`, etc.)
- `<jwt-claim-value>` is the value of the specified JWT claim

**For Kubernetes workloads**, here's a concrete example using the `sub` claim:

```yaml
- !policy
  id: k8s-apps
  body:
    - !group
    - !host
      id: system:serviceaccount:ggscout-namespace:ggscout-service-account
      annotations:
        kubernetes/namespace: ggscout-namespace
        kubernetes/service-account: ggscout-service-account
        workload/type: ggscout

    - !grant
      role: !group
      member: !host
```

**Step 2: Load the workload policy**

```bash
conjur policy load -f authn-jwt-hosts.yaml -b data
```

**Step 3: Grant workload permissions to JWT authenticator**

Create a policy file `authn-jwt-grant.yaml`:

```yaml
- !grant
  role: !group conjur/authn-jwt/k8s-cluster-name/users
  member: !group /data/k8s-apps
```

Load the policy in the JWT authenticator branch:

```bash
conjur policy load -f authn-jwt-grant.yaml -b conjur/authn-jwt/k8s-cluster-name
```

**Step 4: Create comprehensive workload policy with secrets**

For a complete setup including secrets and permissions, create `k8s-workload-complete.yaml`:

```yaml
- !policy
  id: k8s-apps
  body:
  # Create the workload host with proper annotations
  - !host
    id: system:serviceaccount:ggscout-namespace:ggscout-service-account
    annotations:
      authn-jwt/k8s-cluster-name/sub: system:serviceaccount:ggscout-namespace:ggscout-service-account
      kubernetes/namespace: ggscout-namespace
      kubernetes/service-account: ggscout-service-account
      description: "ggscout service account for Kubernetes cluster authentication"

  # Create secrets that this workload can access
  - !variable
    id: database/password

  - !variable
    id: api/token

  # Create a group for this workload's permissions
  - !group
    id: ggscout-consumers

  # Grant the workload access to the consumer group
  - !grant
    role: !group ggscout-consumers
    member: !host system:serviceaccount:ggscout-namespace:ggscout-service-account

  # Grant read permissions to secrets
  - !permit
    role: !group ggscout-consumers
    privilege: [ read, execute ]
    resource: !variable database/password

  - !permit
    role: !group ggscout-consumers
    privilege: [ read, execute ]
    resource: !variable api/token
```

Load the complete policy:
```bash
conjur policy load -f k8s-workload-complete.yaml -b data
```

##### Multiple Workloads Example

For multiple Kubernetes workloads, you can create them in batch:

```yaml
- !policy
  id: myspace/jwt-apps
  body:
  # ggscout workload
  - !host
    id: system:serviceaccount:ggscout-namespace:ggscout-service-account
    annotations:
      kubernetes/namespace: ggscout-namespace
      kubernetes/service-account: ggscout-service-account
      workload/type: ggscout

  # Application workload
  - !host
    id: system:serviceaccount:app-namespace:app-service-account
    annotations:
      kubernetes/namespace: app-namespace
      kubernetes/service-account: app-service-account
      workload/type: application

  # Grant authentication permissions to both
  - !grant
    role: !group conjur/authn-jwt/k8s-cluster-name/users
    members:
      - !host system:serviceaccount:ggscout-namespace:ggscout-service-account
      - !host system:serviceaccount:app-namespace:app-service-account
```

##### Workload Naming Conventions

For Kubernetes workloads using JWT authentication, follow these naming conventions:

- **Host ID Format**: `system:serviceaccount:<namespace>:<service-account-name>`
- **Policy Branch**: Use logical groupings like `k8s-apps`, `<environment>/k8s`, or `<team>/jwt-workloads`
- **Annotations**: Include metadata for better organization:
  - `kubernetes/namespace`
  - `kubernetes/service-account`
  - `environment` (dev, staging, prod)
  - `team` or `application`

#### Step 4: Configure ggscout for JWT Authentication

Add the JWT authentication configuration to your `ggscout.toml`:

```toml
[sources.cyberarksaas-k8s]
type = "cyberarksaas"
auth.auth_mode = "k8s"
auth.service_id = "k8s-cluster-name"
subdomain = "my-company"
fetch_all_versions = true
mode = "read"
owner = "devops-team@example.com"
```

#### Important Notes

1. **Always use `sub` as `token-app-property`**: For Kubernetes workloads, the `sub` (subject) claim contains the service account identity in the format `system:serviceaccount:<namespace>:<serviceaccount-name>`.

2. **Follow least privilege**: Create specific host identities for each workload and grant only the minimum required permissions.

3. **Workload ID matching**: Ensure the workload ID in CyberArk Secrets Manager SaaS exactly matches the Kubernetes service account format: `system:serviceaccount:<namespace>:<service-account-name>`.

#### Step 6: Grant Access to Variables/Secrets

After creating your workload identity, you need to grant it access to the specific secrets it requires. This is done through the policy system using groups, layers, and permit statements.

##### Method 1: Direct Variable Assignment

Create variables and assign privileges directly to a group or layer:

```yaml
- !policy
  id: ggscout-secrets
  body:
    # Define the variables/secrets
    - &variables
      - !variable
        id: db-password
        kind: password

      - !variable
        id: api-token
        kind: API token

      - !variable
        id: ssl/private_key
        kind: SSL private key
        mime_type: application/x-pem-file

    # Create a layer for workloads that need these secrets
    - !layer app

    # Grant access to the variables
    - !permit
      role: !layer app
      privileges: [read, execute]
      resources: *variables

    # Add your workload to the layer
    - !grant
      role: !layer app
      member: !host /data/k8s-apps/system:serviceaccount:ggscout-namespace:ggscout-service-account
```

##### Method 2: Policy-Based Secret Organization

For better organization, create a dedicated policy for your application's secrets:

```yaml
- !policy
  id: ggscout-app-secrets
  owner: !group devops
  annotations:
    description: This policy contains secrets for ggscout application

  body:
    # Define secret variables using YAML anchor
    - &app-secrets
      - !variable
        id: database/password
      - !variable
        id: database/url
      - !variable
        id: database/username
      - !variable
        id: external-api/token
      - !variable
        id: encryption/key

    # Create a group for consumers of these secrets
    - !group consumers

    # Grant read and execute permissions to the consumer group
    - !permit
      role: !group consumers
      privileges: [ read, execute ]
      resources: *app-secrets

    # Add your ggscout workload to the consumers group
    - !grant
      role: !group consumers
      member: !host /data/k8s-apps/system:serviceaccount:ggscout-namespace:ggscout-service-account
```

##### Load the Secret Policies

After creating your secret policies, load them into CyberArk Secrets Manager SaaS:

```bash
# Load the policy
conjur policy load -f ggscout-secrets.yaml -b data

# Set the secret values (example)
conjur variable set -i ggscout-secrets/db-password -v "your-secure-password"
conjur variable set -i ggscout-secrets/api-token -v "your-api-token"
```
