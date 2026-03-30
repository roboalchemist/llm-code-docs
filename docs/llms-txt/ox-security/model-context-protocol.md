# Source: https://docs.ox.security/vibesec/model-context-protocol.md

# Model Context Protocol

> **Note:** This capability is currently in Early Access (EA) and is not generally available. To request access, please contact OX technical support.

OX Security supports integration with AI agents through the Model Context Protocol (MCP), allowing structured, secure interaction between agents and OX Security data.

With this setup, organizations can build or connect smart assistants that interact with their security data conversationally, without logging into the OX UI or navigating dashboards.

Any AI system or tool that supports MCP integration can work with OX.

By exposing selected data and actions through an MCP server, OX Security enables AI-powered tools, such as Cursor, Claude, VS Code extensions, and internal company agents to query and act on live security information from OX.

For the actual integration instructions, refer to [MCP Integration Guide](https://docs.ox.security/vibesec/model-context-protocol/mcp-integration-guide).

## How It Works

When an AI agent connects to the OX MCP server using valid credentials, such as an organization token. It gains access to a set of registered tools, each representing a secure function call that retrieves or manipulates data in OX.

For example:

* The agent can call `Get Issues` to retrieve a list of open security issues.
* The agent can access `Get Applications`, `Get Pipelines`, and other endpoints to pull context from different parts of the OX platform.

This enables natural language agents to:

* Access and interpret OX Security data.
* Intelligently select and orchestrate the required tools to meet user goals.
* Execute actions and deliver the results directly within the conversational interface.

#### Read Data

The following table presents APIs that support use cases such as generating reports, answering questions like, what are my top vulnerabilities, or retrieving application-level insights directly within an agent interface.

The following data can be retrieved by authorized AI agents using MCP:

| Area                                                                      | Description                                                                               |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| <p><strong>Active Issues</strong><br><code>GetIssues</code></p>           | Access currently open and unresolved security issues.                                     |
| <p><strong>Removed Issues</strong><br><code>GetRemovedIssues</code></p>   | Retrieves issues that were automatically resolved due to code or environment changes.     |
| <p><strong>Resolved Issues</strong><br><code>GetResolvedIssues</code></p> | Views issues that were manually or automatically marked as resolved.                      |
| <p><strong>Pipeline Issues</strong><br><code>GetPipelineIssues</code></p> | Pulls data from pipeline scans, including scan results and related issues.                |
| <p><strong>Applications</strong><br><code>GetApplications</code></p>      | Accesses metadata on registered applications, including name, environment, and ownership. |
| <p>SBOM<br><code>GetSbom</code></p>                                       | Retrieves Software Bill of Materials (SBOM) data for specific components or applications. |

#### Perform Actions

There are capabilities that allow AI agents to not only retrieve data but also interact with it, empowering workflows such as issue resolution, feedback tagging, or prioritization suggestions.

> **Note:** All MCP operations are permission-controlled and scoped by organization-level access tokens. Agents can only access data and perform actions that have been explicitly exposed using the OX MCP server configuration.

The following actions can be performed by AI agents through MCP:

| Action                                                                                                                                                | Description                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| <p><strong>Add Comment</strong><br><code>AddCommentToIssue</code></p>                                                                                 | Posts a contextual comment on a specific issue.                             |
| <p><strong>Mark as False Positive</strong><br><code>ReportAsFalsePositive</code><br><code>ReportFalsePositiveForPipelineIssues</code><br><br><br></p> | Updates issue status to "false positive" for improved filtering and triage. |
| <p><strong>Change Severity</strong><br><code>UpdateIssueSeverity</code></p>                                                                           | Modifies the severity level of an issue (e.g., from High to Medium).        |
| <p><strong>Exclude Issues</strong><br><code>ExcludeIssues</code></p>                                                                                  | Mark an issue as excluded so it no longer affects risk metrics or reports.  |

### Using MCP on-prem

You can use MCP SaaS and on-prem.

**To use MCP on-prem:**

1. Verify the [GTP connector](https://docs.ox.security/fix-with-ox/gpt) is connected.
2. Use the following URL:

```
// https://${onpremHostName}/api/mcp
```

## Example Use Cases

When MCP is connected to OX, AI agents can assist with a wide range of queries and operations:

### Show all my critical issues

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-4a136305200288876f394e6d3a52368f7b4f54ab%2Fexample_show_critical_issues.png?alt=media" alt="" width="548"><figcaption></figcaption></figure>

### Generate a leadership report

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0ac0d1f9241dda10f2431668067be42b54c0c859%2Fexample_security_leadership_report.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3f77af31eedffb00d7c1cc077fd9a53fa4970ebf%2Fexample_security_leadership_report1.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

### More examples

| Use Case                              | Example Prompt                                               | Agent Action (via MCP)                                                                |
| ------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| **Query Top Issues**                  | "What are the top 10 critical issues in my OX organization?" | Runs `GetIssues` and returns a severity-sorted list of the top issues.                |
| **Summarize Vulnerabilities by Team** | "How many issues are assigned to each team lead?"            | Queries ownership metadata and returns a breakdown by team lead.                      |
| **Contextual Recommendations**        | "Should I fix this issue or mark it as excluded?"            | Retrieves issue details (e.g., via `GetIssueDetails`) and recommends the next action. |
