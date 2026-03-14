# Source: https://docs.gitguardian.com/nhi-governance/discover-your-nhis.md

# Discover your NHIs

> Describes the NHI inventory for discovering and exploring Non-Human Identities, including ownership management and the visual exploration map.

## NHI Inventory

The inventory provides a centralized, searchable table listing all Non-Human Identities discovered across your perimeter. This dynamic view helps you monitor, audit, and triage NHIs efficiently across various environments and sources.

**Inventory table overview** 

Each row in the inventory represents a unique NHI and displays the following key attributes:

- **Secret name** â The identifier of the associated secret.
- **Source** â The integration where the NHI was discovered (e.g., the name of the secret manager or Kubernetes cluster).
- **Path** â The exact path or location of the secret within the source.
- **Environment** â The associated environment tag (e.g., `prod`, `staging`, `dev`). [Learn how to categorize environments](nhi-governance/integrate-your-sources.md#contextualize-your-nhis-sources)
- **Breached policies** â Any detected misconfigurations or violations of security best practices. [Learn more about breached policies](nhi-governance/improve-your-posture.md)
- **Owners** â The person(s) responsible for the NHI. See [NHI Ownership](#nhi-ownership) below.
    
![NHI Inventory](/img/nhi-governance/nhi-inventory.png)

The inventory supports filtering based on:
- Category
- Breached policy
- Environment
- Source
- Owner: by specific owner, **No owner**, or **Current user**

Clicking into an NHI opens a detailed view that includes policy breaches, secret version, and a visual map of the NHIâs relationships and context.

Note that if a version is deleted, metadata remains but the graph is empty and marked as deleted, while fully destroyed secrets disappear from the inventory.

### NHI Ownership

Ownership assigns accountability for each NHI to one or more people in your organization: you can see who is responsible for an identity, filter the inventory by owner, and add or change owners manually.

**Suggested vs manual owners**

- **Suggested owners** â GitGuardian can automatically suggest owners using data from your integrated sources and from secret incidents. Suggested owners are labeled as *Set automatically by GitGuardian* in the NHI detail view. You can keep them, remove them, or add other owners.
- **Manual owners** â Any owner you add or confirm yourself is labeled *Set manually*. Manual assignments are never overwritten by automatic suggestions.

**How owners are suggested**

Suggestions are based on several signals, in order of confidence (highest first):

1. **Direct owner field** â The NHI source exposes an explicit owner for the identity (e.g. IAM or IdP owner field).
2. **Metadata tags** â A tag on the resource contains an owner (e.g. an AWS IAM or Azure tag with an email).
3. **Source-level owner** â The integration has a declared owner (e.g. the user who configured the integration).
4. **Last editor or creator** â The person who last modified or created the resource, when provided by the source.
5. **Incident committer** â A developer who committed a secret that led to an incident tied to this NHI (private or public).
6. **Public secrets scan** â The user whose scan detected the secret associated with this NHI.

When several candidates exist, the system keeps only those with the highest confidence. You can have up to **5 owners** per NHI.

**Who can be an owner**

- A **workspace member** (linked to their GitGuardian user).
- An **external user** identified by email (e.g. a contractor or someone in another team). No GitGuardian account is required.

**Managing owners**

- In the **inventory**, the Owner column shows up to two owners per NHI; use the **Owner** filter to narrow the list (e.g. *No owner*, *Current user*, or a specific person).
- In an **NHIâs detail view**, use the **Owners** section to add, remove, or replace owners. You can type a workspace member or any valid email to add an external owner. Removing a suggested owner discards that suggestion so it is not re-applied automatically.

**API**

Ownership can be managed via the public API using the `nhi:ownership:read` and `nhi:ownership:write` scopes. Endpoints allow you to list owners for an identity, add owners, remove an owner, or replace the full list of owners.

### Exploration map

The Exploration map gives you a visual, end-to-end view of an NHI, helping you understand its connections, usage, and potential impact across your environment.

The map is composed of:

- **Secrets managers** â Where the NHI's secrets are safely stored.
- **Consumers** â Entities (such as services, scripts, or jobs) that use the secret to authenticate and access other systems.
- **Accessed resources** â The targets accessed by the consumers, along with their permissions, based on [Secret Analyzers](/secrets-detection/secrets-detection-engine/secrets_analyzer).
- **Incidents** â Both **public** and **private** secret incidents associated with the NHI.

![Exploration Map](/img/nhi-governance/exploration-map.png)

You can access the map from an NHIâs detail view or directly from a secret incident, enabling fast, contextual navigation between detection and analysis.

**Use cases**

While the primary goal is to visualize and contextualize NHIs, the map also helps to:

- **Streamline remediation** â Quickly assess the impact of revoking a secret and identify all affected systems.
- **Investigate leaks** â Trace which consumers and resources may have been compromised.
- **Improve secret hygiene** â Spot stale or overprivileged secrets, unused consumers, and other hygiene issues across your perimeter.
