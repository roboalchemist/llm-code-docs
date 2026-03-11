# Source: https://docs.startree.ai/corecapabilities/manage-data/indexes/overview.md

# Source: https://docs.startree.ai/corecapabilities/ingestdata/dataportal/data-modeling/overview.md

# Source: https://docs.startree.ai/corecapabilities/ingestdata/adv-concepts/realtime/overview.md

# Source: https://docs.startree.ai/corecapabilities/ingestdata/adv-concepts/realtime/decoders/overview.md

# Source: https://docs.startree.ai/corecapabilities/ingestdata/adv-concepts/batch/overview.md

# Source: https://docs.startree.ai/corecapabilities/ai/overview.md

# Source: https://docs.startree.ai/corecapabilities/ai/mcp/overview.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

# StarTree MCP Server for Apache Pinot

StarTree MCP Server represents a profound transformation in how businesses engage with their data. Move beyond traditional query consoles and complex SQL—MCP Server is the database client reinvented for the AI age.

Built on the Model Context Protocol (MCP) standard pioneered by Anthropic, this server creates a standardized bridge between large language models and real-time analytical data, serving everyone—AI agents, data analysts, and business users who've never written SQL.

### Your New Query Console

Traditional query consoles require complex SQL knowledge and manual data exploration. Whether you're a business user needing quick insights or an AI agent requiring contextual data access, StarTree MCP Server eliminates this friction by enabling natural language interactions with your analytical data at machine speed.

<img src="https://mintcdn.com/startree/xe5mTwlEdZc68KYh/images/05222025-mcp_server-blog_diagram_1-v3.png?fit=max&auto=format&n=xe5mTwlEdZc68KYh&q=85&s=69dac575066a22db2704e3c55a530d3b" alt="05222025 Mcp Server Blog Diagram 1 V3 Pn" width="1370" height="772" data-path="images/05222025-mcp_server-blog_diagram_1-v3.png" />

## Key Features

| **Feature**                       | **Description**                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Real-time Data Freshness**      | Access the most current data available with Pinot's real-time ingestion capabilities, ensuring AI agents and analysts work with up-to-the-second information. |
| **Millisecond Query Performance** | Leverage Pinot's industry-leading query speed for instantaneous responses, critical for maintaining AI agent context and fluid human interactions.            |
| **Natural Language Interface**    | Transform plain English questions directly into precise database results without writing SQL—perfect for business users and AI agents alike.                  |
| **Schema Discovery**              | Automatically identify table relationships, columns, and data types                                                                                           |
| **Multi-language Support**        | Query data in your preferred language with automatic translation                                                                                              |
| **Metadata Integration**          | Access table information, segment details, and performance metrics via API                                                                                    |
| **Universal Client Support**      | Compatible with most MCP clients including Claude Desktop, LibreChat, Cursor, Windsurf & Agents.                                                              |

## Supported Operations

| Tool                         | Purpose                    |
| :--------------------------- | :------------------------- |
| `list-tables`                | Enumerate available tables |
| `read-query`                 | Execute SELECT queries     |
| `table-details`              | Get table metadata         |
| `segment-list`               | List table segments        |
| `index-column-details`       | Examine segment indexes    |
| `segment-metadata-details`   | Get segment metadata       |
| `tableconfig-schema-details` | Get table configuration    |

Built with [Mintlify](https://mintlify.com).
