# Model Context Protocol - Talk to Meilisearch with Claude desktop

## Introduction

This guide will walk you through setting up and using Meilisearch through natural language interactions with Claude AI via Model Context Protocol (MCP).

## Requirements

To follow this guide, you'll need:

* [Claude Desktop](https://claude.ai/download) (free)
* [A Meilisearch Cloud project](https://www.meilisearch.com/cloud) (14 days free-trial)
* Python ≥ 3.9
* From the Meilisearch Cloud dashboard, your Meilisearch host & api key

## Setting up Claude Desktop with the Meilisearch MCP Server

### 1. Install Claude Desktop

Download and install [Claude Desktop](https://claude.ai/download).

### 2. Install the Meilisearch MCP Server

You can install the Meilisearch MCP server using `uv` or `pip`:

```bash theme={null}