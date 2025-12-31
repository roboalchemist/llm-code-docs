# Source: https://docs.tavily.com/examples/use-cases/meeting-prep.md

# Meeting Prep

> Build an intelligent meeting preparation agent with real-time web research capabilities using Tavily's API and Google Calendar integration

## Introduction

This repository demonstrates how to build a meeting preparation agent with real-time web access, leveraging Tavily's advanced search capabilities. This agent will connect to your Google Calendar via MCP, extract meeting information, and use Tavily search for profile research on the meeting attendees and general information on the companies you are meeting with.

<img src="https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/meeting-prep-agent.gif?s=58004f96bc27a202f3994033fb2c1308" alt="Meeting Prep Agent Demo" width="700" data-og-width="1784" data-og-height="1080" data-path="images/meeting-prep-agent.gif" data-optimize="true" data-opv="3" />

## Try Our Meeting Prep Agent

### Step 1: Get Your API Key

<Card title="Get your Tavily API key" icon="key" href="https://app.tavily.com" horizontal />

### Step 2: Read The Open Source Code and Clone the App

<Card title="View Github Repository" icon="github" href="https://github.com/tavily-ai/meeting-prep-agent" horizontal />

## System Diagram

<img src="https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/meeting-prep-diagram.svg?fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=f738bb1b34b76301223724cb1ab0539d" alt="Meeting Prep Agent Diagram" width="700" data-og-width="1803" data-og-height="595" data-path="images/meeting-prep-diagram.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/meeting-prep-diagram.svg?w=280&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=e31c5d16671561a11ed05b82e60a187d 280w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/meeting-prep-diagram.svg?w=560&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=5b8f2feaace3d9ac3613dd1d1d3ddd74 560w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/meeting-prep-diagram.svg?w=840&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=64181eaec8e00c8e7eb56eadf888c997 840w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/meeting-prep-diagram.svg?w=1100&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=2c1d9a087d4b9fff6e3b1e6cc13510f7 1100w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/meeting-prep-diagram.svg?w=1650&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=b576a7378989244d0e1ad4e6103bf516 1650w, https://mintcdn.com/tavilyai/tgJqPSjqNVSkMFTO/images/meeting-prep-diagram.svg?w=2500&fit=max&auto=format&n=tgJqPSjqNVSkMFTO&q=85&s=176101b0ac395026105aa604c5e8949c 2500w" />

## Features

1. **Real-time Web Search**: Instantly fetches up-to-date information using Tavily's search API.
2. **Agentic Reasoning**: Combines MCP and ReAct agent flows for smarter, context-aware responses.
3. **Streaming Substeps**: See agentic reasoning and substeps streamed live for transparency.
4. **Citations**: All web search results are cited for easy verification.
5. **Google Calendar Integration**: (via mcp-use) Access and analyze your meeting data.
6. **Async FastAPI Backend**: High-performance, async-ready backend for fast responses.
7. **Modern React Frontend**: Interactive UI for dynamic user interactions.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.tavily.com/llms.txt