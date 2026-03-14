# Source: https://docs.acceldata.io/documentation/understanding-mcp-server.md

# Understanding MCP Server

The **Model Context Protocol (MCP)** is an open standard that enables ADM to connect seamlessly with external tools, services, and data sources.
 Think of MCP as a _universal translator_ — it standardizes how ADM communicates with diverse systems across your data ecosystem, from cloud storage to catalogs, documentation platforms, and orchestration tools.

### How MCP Works

MCP acts as a **bridge** between ADM and external services. When you request information from an external system, the query travels through the MCP framework as follows:

```html
User Query → ADM Agent → MCP Server → External Service
                   ↓                        ↓
               Response ← MCP Protocol ← Service Data
```



ADM sends standardized requests via the MCP protocol. Each configured MCP server translates these into the API language of the target system, retrieves the response, and formats it into a structure ADM can interpret and present.

### Key Benefits of MCP Integration

| **Benefit** | **Description** | 
| ---- | ---- | 
| Unified Intelligence Layer | MCP allows ADM to merge context from multiple systems. For example, ADM can correlate data quality metrics from observability tools with JIRA tickets and catalog metadata — all within a single conversation. | 
| Seamless Integration | Instead of developing custom connectors, MCP provides a standard interface for all tools, reducing maintenance and speeding up onboarding. | 
| Extended AI Awareness | ADM can use MCP to access documentation, metadata, or logs, expanding its understanding beyond ADM’s internal scope. | 
| Real-Time Data Access | MCP fetches live data from connected systems, ensuring responses reflect the most current state of your environment. | 
| Enterprise-Grade Security | Supports secure authentication, including API keys and token-based access, with fine-grained authorization per service. | 


### MCP vs. Traditional Integrations

| **Aspect** | **Traditional Integration** | **MCP Integration** | 
| ---- | ---- | ---- | 
| Setup | Custom code per service | Standard protocol configuration | 
| Maintenance | Individual updates | Centralized management | 
| Security | Varying mechanisms | Consistent auth model | 
| Flexibility | Limited, vendor-specific | Universal, protocol-based | 
| Monitoring | Ad-hoc per system | Built-in health checks | 


With MCP, ADM becomes a **single pane of glass** across your data stack — combining operational insights from ADOC with business and governance context from external tools.

## Configuring MCP Servers

### Accessing MCP Configuration

Go to **Settings &gt; Integrations &gt; MCP Servers** to view and manage all MCP connections.
 The page displays each server’s name, URL, connection status, and available tools.

### Health Status Indicators

| **Status** | **Color** | **Meaning** | 
| ---- | ---- | ---- | 
| Connected | Green | Server is authenticated and responding. | 
| Disconnected | Red | Server unreachable — check network or endpoint. | 
| Needs Authentication | Orange | Server reachable but requires credentials refresh. | 
| Error | Red (with details) | Configuration or authentication issue detected. | 


### Server URL Requirements

All MCP endpoints must follow standardized suffixes:

| Connection Type | URL Format | Example | 
| ---- | ---- | ---- | 
| HTTP Endpoint | Must end with `/mcp` | `https://api.company.com/mcp` | 
| Server-Sent Events (SSE) | Must end with `/sse` | `https://api.company.com/sse` | 


This ensures ADM can establish proper communication channels with each MCP server.

### Connecting Through MCP Hubs

You can connect directly to individual servers or use **MCP hubs** like **Composio**, which aggregate multiple integrations into a single access point.

**Benefits of MCP Hubs:**

- Single authentication point for all tools
- Centralized credential management and monitoring
- Consistent API patterns
- Pre-built connectors to popular platforms (Google Drive, Slack, Atlassian, etc.)

#### Example: Using Composio as an MCP Hub

1. Log in to [Composio](https://composio.dev).
2. Create a project and configure integrations (e.g., Google Drive, Slack).
3. Generate an endpoint URL ending with `/mcp` or `/sse`.
4. Add this endpoint in ADM — one connection grants access to all integrated tools.

### Adding a New MCP Server

1. Go to **Settings &gt; Integrations &gt; MCP Servers**.
2. Click **+ Add Server**.
3. Fill in the required fields:

| **Field** | **Description** | 
| ---- | ---- | 
| Server Name | Friendly name for identification (e.g., “GoogleDocs” or “GitHub MCP”). | 
| Server URL | Full endpoint URL (must end with `/mcp` or `/sse`). | 
| Description | (Optional) Brief summary of what the server provides. | 


**Example URL**

```bash
https://apollo.composio.dev/v3/mcp/5add3917.../mcp?user_id=pg-test-6f1cd49f...
```



4. Click Add Server.
5. Once connected, you’ll see:
    1. **Connected** status badge
    2. **Available Tools** link showing capabilities (e.g., “Available Tools (30)”)
    3. **Last Checked** timestamp
    4. Action buttons: Test Connection, Edit, Delete

### Managing Servers

- **View Details:** Click a server card to see connection info and available tools.
- **Edit:** Update server name, URL, or description via the edit icon.
- **Test Connection:** Use the refresh icon to verify connectivity; ADM updates the status badge and timestamp.
- **Remove:** Click delete **&gt;** confirm. (Conversations using this server will lose access to its tools.)

### Important Notes on MCP Behavior

MCP responses may vary due to:

- The LLM model used
- Query phrasing
- Server capabilities and available data
- Conversation context

> **Tip:** Treat the examples in this documentation as guides — your actual ADM responses will adapt to your environment, connected systems, and ongoing conversation context.

## Google Drive Integration for Data Governance

Google Drive integration enables ADM to read documents, spreadsheets, and files from your organization’s Drive — empowering data teams to bridge **business documentation and operational policies**.

Common use cases include:

- Translating BRDs into data quality policies
- Validating existing policies against documented standards
- Enriching data quality investigations with business impact context

### Setup via Composio

#### Step 1: Configure in Composio

1. Log into **[composio.dev](https://composio.dev)**.
2. Create or open a project **&gt;** **MCP Config &gt; Create MCP Config**.
3. Click **Add Toolkit &gt; Google Drive**.
4. Set up authentication:
    - Choose **OAuth**.
    - Select required permissions (file read/search).
    - Complete Google authorization.

5. Click **Create MCP** **&gt;** **Create Instance**.
6. Copy the generated **MCP URL** (ends in `/mcp` or `/sse`).

#### Step 2: Add to ADM

1. In ADM: **Settings &gt; Integrations &gt; MCP Servers &gt; + Add Server**
2. Enter:
    - **Server Name:** “GoogleDocs”
    - **Server URL:** Paste the Composio endpoint
    - **Description:** “Access to Google Drive documents”

3. Click **Add Server** and verify **CONNECTED** status.

### Example Use Case 1: Creating Policies from Business Requirements

**You:** “Read the `Q4_2025_Data_Requirements.pdf` from my Drive and identify what data quality requirements we need.”

**ADM:**

> I found 12 data quality requirements across customer and financial data.
>  Recommending policies such as:
> 
> - Email format validation for `customers.email_address`
> - Conditional phone number checks for premium customers
> - Completeness validation on address fields
> - Transaction amount range and reconciliation checks

ADM extracts policy logic, severity, and affected tables directly from your documents, enabling pre-populated policy creation in Workflow Mode.

**Workflow Integration Benefits:**

- Auto-fills rule logic and thresholds
- Adds BRD references and requirement IDs
- Aligns severity with business impact
- Maintains traceability between policy and documentation

### Example Use Case 2: Validating Policies Against Documentation

**You:** “Compare our current data quality policies with the standards in `Data_Governance_Framework_2025.pdf`.”

**ADM:**

> 47 policies analyzed.
> 
> - 32 compliant with framework
> - 8 missing required rules (e.g., date range validation)
> - 2 conflicting configurations (e.g., uniqueness constraints)

**Recommendations:**

- Create missing policies for uncovered requirements
- Adjust thresholds to match governance standards
- Align documentation and operational rules

### Example Use Case 3: Enriching Business Context

**You:** “The `customer_ltv` column in `customer_360_view` is showing anomalies. What’s the business impact?”

**ADM:**

> According to _Customer_Analytics_Playbook.pdf_:
> 
> - LTV drives marketing budgets ($2.3M quarterly)
> - Influences CS resource allocation and recommendation models
> - Current anomalies could misdirect campaigns worth ~$180K

**Recommended Actions:**

1. Pause affected automations
2. Correct source data and reprocess
3. Implement policy for order amount anomalies

This integration allows ADM to connect **technical findings with business impact**, turning investigations into actionable intelligence.

### Capabilities & Privacy

**What ADM Can Do**

- Search and read files (Docs, Sheets, PDFs, text)
- Navigate folders and shared drives
- Retrieve metadata (owner, timestamps)

**What ADM Cannot Do**

- Create, delete, or edit files
- Modify permissions or upload content

**Privacy**

- ADM accesses files _only_ when queried
- No file content is stored
- Access is logged with timestamps and user identity
- Permissions can be revoked anytime via Google or ADM

## Atlassian Integration (Confluence & JIRA)

The Atlassian integration connects ADM to **Confluence** (knowledge/wiki) and **JIRA** (issue tracking) via MCP. This enables:

- Pulling governance standards, runbooks, and business definitions from Confluence into conversations and workflows.
- Correlating ADOC quality incidents with JIRA issues, and creating or updating tickets directly from context.

### Setup via Composio (Recommended)

**Step 1: Configure in Composio**

1. Sign in to **composio.dev** **&gt;** _MCP Config_ **&gt;** **Create MCP Config**.
2. **Add Toolkit** **&gt;** select **Atlassian** (Confluence + JIRA) or add them individually.
3. Choose **OAuth** **&gt;** complete Atlassian authorization.
4. Select scopes:
    - _Confluence:_ read pages, search content, access spaces
    - _JIRA:_ read issues, search projects, view issue details

5. **Create MCP** **&gt;** **Create Instance** **&gt;** authorize your Atlassian site.
6. Copy the generated **MCP URL** (ends with `/mcp` or `/sse`).

**Step 2: Add to ADM**

1. **ADM** **&gt;** **Settings &gt; MCP Servers &gt; + Add Server**
2. Name (e.g., “Atlassian”), paste **Server URL**, add a description.
3. Confirm status shows **CONNECTED** **&gt;** open **Available Tools** to verify.

### Use Cases

#### Enrich lineage with business context (Confluence)

**You:** “Show complete lineage for `customer_360_view`, including business context from Confluence.” 

**ADM:** Merges technical lineage (ADOC) with business lineage and consumers (Confluence), highlighting purpose, SLAs, owners, and downstream impact.

**Why it matters:** Aligns technical impact with business-critical dependencies (e.g., campaign spend, CS assignments, executive dashboards).

#### Validate standards vs. policies (Confluence → ADOC)

**You:** “Review our _Financial Data Quality Standards_ page and tell me what policies we should have.” 

**ADM:** Extracts standards (completeness, reconciliation, ranges, timestamp logic, referential integrity), proposes **policy types, rules, severities**, and target tables.

**Workflow boost:** Pre-populates policy forms with rule logic and links to Confluence for traceability.

#### Correlate incidents with tracked work (JIRA)

**You:** “Any open JIRA issues related to `orders` data quality problems?” 

**ADM:** Matches ADOC issues with JIRA tickets (status, assignee, comments), identifies **gaps** (no ticket yet), and offers to **create new issues** with context.

**Outcome:** Prevents duplicates, speeds remediation, and keeps audit trails aligned.

### Capabilities & Permissions

| **Capability** | **Confluence** | **JIRA** | 
| ---- | ---- | ---- | 
| Search & Read | Pages, spaces, content | Issues, projects, comments | 
| Write | (read-only) | (read-only) _(creation via MCP depends on server tools exposed)_ | 
| Linkage | Cite pages in responses | Link ADOC incidents to issues | 


> **Note:** Actions like ticket creation depend on the MCP server exposing those tools in a read/write mode. Many deployments start read-only.
> 
> ## Data Catalog Integration (Alation)
> 
> Alation provides business context (owners, glossary, classifications, rules, lineage). Through MCP, ADM+ADOC can combine operational quality metrics with catalog governance to drive prioritized action.
> 
> ### Setup
> 
> - **Via Composio:** Add the **Alation** toolkit if available, configure API token, create an instance, copy **/mcp** URL, add to ADM.
> - **Direct MCP:** If your Alation offers a native MCP endpoint, add it directly (must end with `/mcp` or `/sse`).
> 
> 
> Confirm **CONNECTED** and verify **Available Tools**.
> 
> ### Use Cases
> 
> #### Policy recommendations from catalog rules
> 
> **You:** “Review Alation’s business rules for `customer_orders` and propose ADOC policies.” 
> 
> **ADM:** Returns **policy list** (names, rules, severity, rationale), mapped to Alation rules and tables. 
> 
> **Value:** Bridges documentation and enforcement; keeps policies faithful to business intent.
> 
> #### Prioritize by criticality
> 
> **You:** “Show ADOC quality status for Alation ‘Tier 1 Critical’ assets.” 
> 
> **ADM:** Correlates **classification** with **quality scores**, flags **business impact** (owners, consumers, SLAs), and prioritizes fixes (e.g., SOX-tagged tables).
> 
> #### Close expectation gaps
> 
> **You:** “Find mismatches between Alation expectations and ADOC policies.” 
> 
> **ADM:** Highlights incomplete or missing policy coverage (e.g., freshness SLA not enforced, referential integrity partial), with **actionable remediation plan**.
> 
> ### Best Practices
> 
> - **Link policies** to Alation pages for audit traceability.
> - **Use Alation severity/classification** to set policy severity and alerting.
> - **Review quarterly:** ensure catalog rules are actually enforced in ADOC.
> 
> 
> ## Validating Documentation vs. Reality
> 
> Documentation drifts. ADM can compare documented facts (Confluence/Alation) with actual state (ADOC) and produce precise gaps.
> 
> **Checks include:**
> 
> - Documented-but-missing assets
> - Outdated descriptions, owners, schedules
> - Missing business context (purpose, consumers, SLAs)
> - Quality expectations documented but not enforced
> 
> 
> **Outputs:**
> 
> - Gap tables (undocumented assets; incomplete metadata)
> - Risk assessment (usage, downstream consumers, compliance tags)
> - One-click actions (create JIRA tickets, draft page updates, schedule recurring validations)
> 
> 
> ## Enterprise Custom MCP Servers
> 
> ### Why Custom MCP
> 
> Many enterprises have **internal** systems (homegrown catalogs, observability, compliance tools, legacy platforms). A **custom MCP server** exposes these systems to ADM via a standard, secure protocol — unlocking unified access without bespoke connectors.
> 
> ### Technical Requirements
> 
> **Protocol**
> 
> - Implement **Model Context Protocol** (v1.0+), JSON-RPC 2.0 over HTTP/SSE
> - Endpoints must end with **`/mcp`** or **`/sse`**
> - Return well-formed MCP messages and capability schemas
> 
> 
> **Network**
> 
> - HTTPS (TLS 1.2+, ideally 1.3)
> - Stable, reachable endpoint (support health checks)
> 
> 
> **Auth**
> 
> - API key or bearer token (stateless per request)
> - Clear error messages on auth failures
> - Minimum-privilege service accounts
> 
> 
> **Capabilities**
> 
> - Declare tools with input/output schemas, version them, and document rate limits and errors.
> 
> 
> ### Configuration in ADM
> 
> 1. **Prepare:** URL, credentials, capability list, SLOs, contacts.
> 2. **ADM** **&gt;** **Settings &gt; MCP Servers &gt; Add MCP Server**
> 3. Enter **Name**, **URL**, **Description**, **Auth** (API key header or bearer token).
> 4. **Test Connection** **&gt;** verify capabilities discovered.
> 5. **Enable** **&gt;** server available in conversations/workflows.
> 
> 
> ### Example Capability Set (Internal DataHub)
> 
> - `search_datasets(query, filters?)` → list datasets with metadata
> - `get_dataset_metadata(dataset_id)` → full metadata
> - `get_lineage(dataset_id, direction, depth)` → graph or adjacency
> - `get_business_rules(dataset_id)` → rules for policy mapping
> - `get_usage_stats(dataset_id, time_range)` → adoption signals
> 
> 
> **Usage:**
> 
> - Find assets by owner/domain, fetch rules, **generate ADOC policies**, and link documentation for audit.
> 
> 
> ### Security & Operations
> 
> **Authentication & Authorization**
> 
> - 32+ char API keys/tokens; rotate quarterly
> - Scope tokens minimally; never hardcode secrets
> - Enforce resource-level authorization server-side
> 
> 
> **Network & Abuse Protection**
> 
> - HTTPS only; optional VPN/IP allowlists
> - WAF + rate limiting (e.g., 100–500 req/min)
> - Monitor anomalies (geo/time anomalies, spikes)
> 
> 
> **Data Handling**
> 
> - Return minimal, masked data; avoid PII by default
> - Log access with user + timestamp; retain logs ~90 days
> - No sensitive caching in responses
> 
> 
> **Compliance**
> 
> - Document accessible data domains
> - Maintain audit trails and change logs
> - Review access monthly; patch regularly
> 
> 
> **Reliability**
> 
> - Health endpoints; connection pooling; timeouts (30s), retries (3, backoff)
> - Versioned APIs; backward-compatible changes
> - Non-prod test before prod rollout
> 
> 
> ### Monitoring & Maintenance

| **Area** | **What to Track** | **Thresholds / Actions** | 
| ---- | ---- | ---- | 
| Availability | Response time, error rate | Alert if &gt;500ms avg or &gt;1% errors | 
| Capacity | QPS, rate-limit hits | Scale or raise limits with caution | 
| Security | Auth failures, unusual patterns | Lockout + alert on bursts | 
| Accuracy | Payload shape, schema mismatches | Add contract tests; version bump | 
| Usage | Capability popularity | Guide optimization & deprecation | 


### Deployment Models

- **Hub-only (Composio):** Centralized auth/monitoring for many external tools.
- **Direct custom servers:** Fine-grained control for internal systems.
- **Hybrid (Recommended):** Hub for standard SaaS; direct MCP for proprietary systems.

### Practical Tips

- **Start read-only.** Add write actions after controls are proven.
- **Document capabilities** with examples and SLA expectations.
- **Instrument metrics** from day one; build a health dashboard.
- **Automate tests** for schema, auth, and rate-limit behavior.