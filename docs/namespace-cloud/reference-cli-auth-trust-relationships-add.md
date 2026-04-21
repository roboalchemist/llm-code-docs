<!-- Source: https://namespace.so/docs/reference/cli/auth-trust-relationships-add -->

# nsc auth trust-relationships add

Add a new trust relationship by specifying issuer and subject match patterns.

`nsc auth trust-relationships add` creates a new trust relationship that allows external systems to authenticate to your workspace using OIDC tokens that match the specified issuer and subject patterns.

## Usage

```
nsc auth trust-relationships add --issuer string --subject-match string [--grant string]
```

### Examples

**Google Cloud Platform trust relationship:**

```
$ nsc auth trust-relationships add \
  --issuer "https://accounts.google.com" \
  --subject-match "projects/123456789/serviceAccounts/my-service@my-project.iam.gserviceaccount.com"
```

**fly.io trust relationship:**

```
$ nsc auth trust-relationships add \
  --issuer "https://fly.io/example-org" \
  --subject-match "example-org:example-app:example-machine"
```

**rwx trust relationship:**

```
$ nsc auth trust-relationships add \
  --issuer "https://cloud.rwx.com/mint" \
  --subject-match "org:my-org:vault:deploy-vault"
```

**Buildkite trust relationship:**

```
$ nsc auth trust-relationships add \
  --issuer "https://agent.buildkite.com" \
  --subject-match "organization:my-org:pipeline:my-pipeline:ref:refs/heads/main"
```

**Using wildcards:**

```
# All service accounts in GCP project
$ nsc auth trust-relationships add \
  --issuer "https://accounts.google.com" \
  --subject-match "projects/123456789/serviceAccounts/*"
 
# All fly.io apps in organization
$ nsc auth trust-relationships add \
  --issuer "https://fly.io/example-org" \
  --subject-match "example-org:app:*"
 
# All vaults in rwx organization
$ nsc auth trust-relationships add \
  --issuer "https://cloud.rwx.com/mint" \
  --subject-match "org:my-org:vault:*"
 
# All pipelines in Buildkite organization
$ nsc auth trust-relationships add \
  --issuer "https://agent.buildkite.com" \
  --subject-match "organization:my-org:pipeline:*"
```

**Scoping permissions with `--grant`:**

```
# Grant only instance management permissions
$ nsc auth trust-relationships add \
  --issuer "https://accounts.google.com" \
  --subject-match "projects/123456789/serviceAccounts/my-service@my-project.iam.gserviceaccount.com" \
  --grant '{"resource_type":"instance","resource_id":"*","actions":["create","list","get","destroy"]}'
 
# Grant builder and artifact access for CI/CD
$ nsc auth trust-relationships add \
  --issuer "https://agent.buildkite.com" \
  --subject-match "organization:my-org:pipeline:*" \
  --grant '{"resource_type":"builder","resource_id":"*","actions":["ensure","access"]}' \
  --grant '{"resource_type":"artifact","resource_id":"*","actions":["create","resolve","list"]}'
 
# Grant container registry push/pull access
$ nsc auth trust-relationships add \
  --issuer "https://fly.io/example-org" \
  --subject-match "example-org:deploy-app:*" \
  --grant '{"resource_type":"containerregistry","resource_id":"*","actions":["configure"]}' \
  --grant '{"resource_type":"containerregistry/repository","resource_id":"*","actions":["list"]}'
```

## Required Flags

### --issuer string

The token issuer URL that identifies the external identity provider. This must be the exact issuer claim (`iss`) that appears in the OIDC tokens you want to trust.

**Supported issuers:**

- **Google Cloud Platform**: `https://accounts.google.com`
- **fly.io**: `https://fly.io/{org-name}` (replace `{org-name}` with your organization)
- **rwx**: `https://cloud.rwx.com/mint`
- **Buildkite**: `https://agent.buildkite.com`

### --subject-match string

Subject match pattern that defines which subjects from the issuer are trusted. This pattern is matched against the subject claim (`sub`) in the OIDC token.

The pattern supports wildcards (`*`) for flexible matching:

**Google Cloud Platform patterns:**

- **Service account**: `projects/123456789/serviceAccounts/my-service@my-project.iam.gserviceaccount.com` (exact match)
- **Multiple service accounts**: `projects/123456789/serviceAccounts/*` (all service accounts in project)

**fly.io patterns:**

- **Specific machine**: `example-org:example-app:example-machine` (matches specific machine)
- **All apps in organization**: `example-org:app:*` (matches all apps in organization)
- **Specific app**: `example-org:example-app:*` (matches all machines in specific app)

**rwx patterns:**

- **Specific vault**: `org:my-org:vault:deploy-vault` (matches specific vault)
- **All vaults in organization**: `org:my-org:vault:*` (matches all vaults in organization)

**Buildkite patterns:**

- **Specific pipeline and branch**: `organization:my-org:pipeline:my-pipeline:ref:refs/heads/main` (matches specific pipeline on main branch)
- **All pipelines in organization**: `organization:my-org:pipeline:*` (matches all pipelines in organization)
- **Specific pipeline all branches**: `organization:my-org:pipeline:my-pipeline:ref:*` (matches specific pipeline on any branch)

## Optional Flags

### --grant stringArray (optional, can be repeated)

Grant specific permissions to the trust relationship as a JSON object. When omitted, the federated identity receives full access to the workspace. Use this flag to restrict access to only the resources and actions needed.

This flag can be specified multiple times to grant multiple permissions.

**Format:**

```
{"resource_type":"...","resource_id":"...","actions":["..."]}
```

- `resource_type` — The type of resource to grant access to (e.g. `instance`, `builder`, `artifact`).
- `resource_id` — The ID of the specific resource, or `*` to match all resources of that type.
- `actions` — An array of permitted actions on the resource.

See [Permissions](/docs/security/permissions) for the full list of available resource types and actions.

**Common grant examples:**

| Use Case | Grant |
|---|---|
| Manage instances | `{"resource_type":"instance","resource_id":"*","actions":["create","list","get","destroy"]}` |
| Remote builds | `{"resource_type":"builder","resource_id":"*","actions":["ensure","access"]}` |
| Artifact storage | `{"resource_type":"artifact","resource_id":"*","actions":["create","resolve","list"]}` |
| Container registry | `{"resource_type":"containerregistry/repository","resource_id":"*","actions":["list","share"]}` |
| Ingress access | `{"resource_type":"ingress","resource_id":"*","actions":["access"]}` |

## Related Topics

- [nsc auth trust-relationships](/docs/reference/cli/auth-trust-relationships) - Main command overview
- [nsc auth trust-relationships list](/docs/reference/cli/auth-trust-relationships-list) - List existing relationships
- [nsc auth trust-relationships remove](/docs/reference/cli/auth-trust-relationships-remove) - Remove relationships
- [Workload Federation](/docs/federation) - Integration guides for cloud providers
- [Permissions](/docs/security/permissions) - Full list of resource types and actions

Last updated February 22, 2026
