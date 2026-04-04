# Source: https://docs.ox.security/generate-reports/built-in-reports/vibesec-usage-reports.md

# VibeSec Usage Reports

The VibeSec Usage Report provides visibility into how developers use the VibeSec AI assistant across your organization. It aggregates key usage metrics, backlog fix adoption, and security impact indicators to help AppSec and R\&D managers track the effectiveness of AI-driven secure coding assistance.

The dashboard presents visual insights and tables that summarize developer engagement, backlog fix trends, and risk prevention statistics.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-97e513869fee640c24a606f3d7bbc1bb5eacdd02%2FVibeSec%20usage%202.png?alt=media" alt=""><figcaption></figcaption></figure>

## Daily Active VibeSec Users

This graph shows the number of individual developers who used an AI agent with VibeSec installed on each day.\
A developer is counted as active when their IDE agent communicates with the OX backend while VibeSec is enabled.

## Backlog Fixes Suggested vs Accepted

This graph compares the number of security fixes suggested by VibeSec with the number of fixes that developers accepted.

* **Suggested** – Fixes automatically proposed by VibeSec through the AI agent.
* **Accepted** – Fixes that developers approved, prompting the agent (for example, Cursor) to apply the change in code.

This metric helps evaluate how often developers act on VibeSec’s automated recommendations.

## Risks Prevented (Daily)

This graph shows the number of security risks prevented each day by proactive VibeSec guidance.\
The data corresponds to the entries listed in the **Risks Prevented** and **Risks Prevented by Application** tables.

## Developers by Tool

This table lists all developers who used VibeSec, grouped by their IDE or development tool.\
It includes connection and activity data, as well as metrics that summarize each developer’s engagement and security impact.

| Column                 | Description                                                         |
| ---------------------- | ------------------------------------------------------------------- |
| **User**               | Developer’s email or ID using VibeSec                               |
| **Tool**               | IDE or development environment (for example, Cursor)                |
| **First request date** | Date when the developer first used VibeSec                          |
| **Last used date**     | Most recent date of activity                                        |
| **Installation date**  | Date when VibeSec was first installed                               |
| **Number of requests** | Total number of VibeSec requests made by the developer              |
| **Risks prevented**    | Number of security issues proactively prevented during code writing |
| **Fixes suggested**    | Number of security fixes suggested by VibeSec                       |
| **Fixes accepted**     | Number of fixes accepted by the developer                           |

## Recent Backlog Fixes

This table lists recent security fixes suggested by VibeSec and accepted by developers.\
It helps track how developers respond to VibeSec’s backlog remediation guidance.

| Column        | Description                                        |
| ------------- | -------------------------------------------------- |
| **Issue**     | The issue description, including type and severity |
| **Owner**     | Developer who accepted the fix                     |
| **App**       | The affected application or repository             |
| **Timestamp** | When the fix was accepted                          |

## Risks Prevented

This table lists all instances where VibeSec proactively secured code before vulnerabilities were introduced.\
As developers work, VibeSec continuously provides guidance through the AI agent, ensuring that risky code patterns are corrected early.

| Column            | Description                                                                               |
| ----------------- | ----------------------------------------------------------------------------------------- |
| **User**          | Developer who triggered the prevention event                                              |
| **Vulnerability** | The vulnerability type that was prevented (for example, Input Validation, Path Traversal) |
| **Timestamp**     | When the prevention occurred                                                              |
| **App**           | Application or repository where the risk was prevented                                    |
| **Language**      | Programming language of the secured code                                                  |
| **File name**     | The file in which the prevented vulnerability was detected                                |
| **Line of code**  | The line number in which the prevention occurred                                          |

## Risks Prevented by Application

This table aggregates all prevented risks by application.\
It shows how many vulnerabilities were avoided per app and provides visibility into which environments benefit most from VibeSec’s proactive security assistance.

| Column              | Description                                          |
| ------------------- | ---------------------------------------------------- |
| **App**             | Application or repository name                       |
| **Language**        | Programming language used in the application         |
| **Timestamp**       | When the latest prevention occurred                  |
| **Risks prevented** | Total number of vulnerabilities prevented in the app |
