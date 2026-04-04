# Source: https://modelcontextprotocol.io/specification/2025-11-25/server/index.md

# Source: https://modelcontextprotocol.io/specification/2025-11-25/index.md

# Source: https://modelcontextprotocol.io/specification/2025-11-25/basic/index.md

# Source: https://modelcontextprotocol.io/specification/2025-11-25/architecture/index.md

# Source: https://modelcontextprotocol.io/community/seps/index.md

> ## Documentation Index
> Fetch the complete documentation index at: https://modelcontextprotocol.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Specification Enhancement Proposals (SEPs)

> Index of all MCP Specification Enhancement Proposals

export const Badge = ({children, color = "gray"}) => {
  const styles = {
    green: {
      light: {
        bg: "#dcfce7",
        text: "#166534"
      },
      dark: {
        bg: "#14532d",
        text: "#86efac"
      }
    },
    blue: {
      light: {
        bg: "#dbeafe",
        text: "#1e40af"
      },
      dark: {
        bg: "#1e3a5f",
        text: "#93c5fd"
      }
    },
    yellow: {
      light: {
        bg: "#fef9c3",
        text: "#854d0e"
      },
      dark: {
        bg: "#713f12",
        text: "#fde047"
      }
    },
    red: {
      light: {
        bg: "#fee2e2",
        text: "#991b1b"
      },
      dark: {
        bg: "#7f1d1d",
        text: "#fca5a5"
      }
    },
    orange: {
      light: {
        bg: "#ffedd5",
        text: "#9a3412"
      },
      dark: {
        bg: "#7c2d12",
        text: "#fdba74"
      }
    },
    purple: {
      light: {
        bg: "#f3e8ff",
        text: "#6b21a8"
      },
      dark: {
        bg: "#581c87",
        text: "#d8b4fe"
      }
    },
    gray: {
      light: {
        bg: "#f3f4f6",
        text: "#1f2937"
      },
      dark: {
        bg: "#374151",
        text: "#d1d5db"
      }
    }
  };
  const s = styles[color] || styles.gray;
  return <>
      <style>{`
        .badge-${color} { background-color: ${s.light.bg}; color: ${s.light.text}; }
        .dark .badge-${color}, [data-theme="dark"] .badge-${color} { background-color: ${s.dark.bg}; color: ${s.dark.text}; }
        @media (prefers-color-scheme: dark) {
          .badge-${color}:not(.light *) { background-color: ${s.dark.bg}; color: ${s.dark.text}; }
        }
      `}</style>
      <span className={`badge-${color} inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium`}>
        {children}
      </span>
    </>;
};

Specification Enhancement Proposals (SEPs) are the primary mechanism for proposing major changes to the Model Context Protocol. Each SEP provides a concise technical specification and rationale for proposed features.

<Card title="Submit a SEP" icon="file-plus" href="/community/sep-guidelines">
  Learn how to submit your own Specification Enhancement Proposal
</Card>

## Summary

* **Final**: 24

## All SEPs

| SEP                                                                                 | Title                                                                         | Status                             | Type             | Created    |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ---------------------------------- | ---------------- | ---------- |
| [SEP-2133](/community/seps/2133-extensions)                                         | Extensions                                                                    | <Badge color="green">Final</Badge> | Standards Track  | 2025-01-21 |
| [SEP-2085](/community/seps/2085-governance-succession-and-amendment)                | Governance Succession and Amendment Procedures                                | <Badge color="green">Final</Badge> | Process          | 2025-12-05 |
| [SEP-1865](/community/seps/1865-mcp-apps-interactive-user-interfaces-for-mcp)       | MCP Apps - Interactive User Interfaces for MCP                                | <Badge color="green">Final</Badge> | Extensions Track | 2025-11-21 |
| [SEP-1850](/community/seps/1850-pr-based-sep-workflow)                              | PR-Based SEP Workflow                                                         | <Badge color="green">Final</Badge> | Process          | 2025-11-20 |
| [SEP-1730](/community/seps/1730-sdks-tiering-system)                                | SDKs Tiering System                                                           | <Badge color="green">Final</Badge> | Standards Track  | 2025-10-29 |
| [SEP-1699](/community/seps/1699-support-sse-polling-via-server-side-disconnect)     | Support SSE polling via server-side disconnect                                | <Badge color="green">Final</Badge> | Standards Track  | 2025-10-22 |
| [SEP-1686](/community/seps/1686-tasks)                                              | Tasks                                                                         | <Badge color="green">Final</Badge> | Standards Track  | 2025-10-20 |
| [SEP-1613](/community/seps/1613-establish-json-schema-2020-12-as-default-dialect-f) | Establish JSON Schema 2020-12 as Default Dialect for MCP                      | <Badge color="green">Final</Badge> | Standards Track  | 2025-10-06 |
| [SEP-1577](/community/seps/1577--sampling-with-tools)                               | Sampling With Tools                                                           | <Badge color="green">Final</Badge> | Standards Track  | 2025-09-30 |
| [SEP-1330](/community/seps/1330-elicitation-enum-schema-improvements-and-standards) | Elicitation Enum Schema Improvements and Standards Compliance                 | <Badge color="green">Final</Badge> | Standards Track  | 2025-08-11 |
| [SEP-1319](/community/seps/1319-decouple-request-payload-from-rpc-methods-definiti) | Decouple Request Payload from RPC Methods Definition                          | <Badge color="green">Final</Badge> | Standards Track  | 2025-08-08 |
| [SEP-1303](/community/seps/1303-input-validation-errors-as-tool-execution-errors)   | Input Validation Errors as Tool Execution Errors                              | <Badge color="green">Final</Badge> | Standards Track  | 2025-08-05 |
| [SEP-1302](/community/seps/1302-formalize-working-groups-and-interest-groups-in-mc) | Formalize Working Groups and Interest Groups in MCP Governance                | <Badge color="green">Final</Badge> | Standards Track  | 2025-08-05 |
| [SEP-1046](/community/seps/1046-support-oauth-client-credentials-flow-in-authoriza) | Support OAuth client credentials flow in authorization                        | <Badge color="green">Final</Badge> | Standards Track  | 2025-07-23 |
| [SEP-1036](/community/seps/1036-url-mode-elicitation-for-secure-out-of-band-intera) | URL Mode Elicitation for secure out-of-band interactions                      | <Badge color="green">Final</Badge> | Standards Track  | 2025-07-22 |
| [SEP-1034](/community/seps/1034--support-default-values-for-all-primitive-types-in) | Support default values for all primitive types in elicitation schemas         | <Badge color="green">Final</Badge> | Standards Track  | 2025-07-22 |
| [SEP-1024](/community/seps/1024-mcp-client-security-requirements-for-local-server-) | MCP Client Security Requirements for Local Server Installation                | <Badge color="green">Final</Badge> | Standards Track  | 2025-07-22 |
| [SEP-994](/community/seps/994-shared-communication-practicesguidelines)             | Shared Communication Practices/Guidelines                                     | <Badge color="green">Final</Badge> | Process          | 2025-07-17 |
| [SEP-991](/community/seps/991-enable-url-based-client-registration-using-oauth-c)   | Enable URL-based Client Registration using OAuth Client ID Metadata Documents | <Badge color="green">Final</Badge> | Standards Track  | 2025-07-07 |
| [SEP-990](/community/seps/990-enable-enterprise-idp-policy-controls-during-mcp-o)   | Enable enterprise IdP policy controls during MCP OAuth flows                  | <Badge color="green">Final</Badge> | Standards Track  | 2025-06-04 |
| [SEP-986](/community/seps/986-specify-format-for-tool-names)                        | Specify Format for Tool Names                                                 | <Badge color="green">Final</Badge> | Standards Track  | 2025-07-16 |
| [SEP-985](/community/seps/985-align-oauth-20-protected-resource-metadata-with-rf)   | Align OAuth 2.0 Protected Resource Metadata with RFC 9728                     | <Badge color="green">Final</Badge> | Standards Track  | 2025-07-16 |
| [SEP-973](/community/seps/973-expose-additional-metadata-for-implementations-res)   | Expose additional metadata for Implementations, Resources, Tools and Prompts  | <Badge color="green">Final</Badge> | Standards Track  | 2025-07-15 |
| [SEP-932](/community/seps/932-model-context-protocol-governance)                    | Model Context Protocol Governance                                             | <Badge color="green">Final</Badge> | Process          | 2025-07-08 |

## SEP Status Definitions

* <Badge color="gray">Draft</Badge> - SEP proposal with a sponsor, undergoing
  informal review
* <Badge color="yellow">In-Review</Badge> - SEP proposal ready for formal review
  by Core Maintainers
* <Badge color="blue">Accepted</Badge> - SEP accepted, awaiting reference
  implementation
* <Badge color="green">Final</Badge> - SEP finalized with reference
  implementation complete
* <Badge color="red">Rejected</Badge> - SEP rejected by Core Maintainers
* <Badge color="red">Withdrawn</Badge> - SEP withdrawn by the author
* <Badge color="purple">Superseded</Badge> - SEP replaced by a newer SEP
* <Badge color="orange">Dormant</Badge> - SEP without a sponsor, closed after 6
  months
