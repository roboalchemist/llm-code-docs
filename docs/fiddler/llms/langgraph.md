# Source: https://docs.fiddler.ai/api/fiddler-langgraph-sdk/langgraph.md

# Introduction

**Version:** 1.4.0

## Overview

Complete API reference documentation for the fiddler-langgraph package.

## Components

### Core

Core functionality and utilities

* [FiddlerResourceAttributes](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/core/fiddler-resource-attributes)
* [FiddlerSpanAttributes](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/core/fiddler-span-attributes)
* [SpanType](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/core/span-type)
* [FiddlerClient](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/core/fiddler-client)
* [get\_client](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/core/get-client)
* [get\_current\_span](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/core/get-current-span)
* [trace](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/core/trace)
* [FiddlerSpanProcessor](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/core/fiddler-span-processor)
* [FiddlerChain](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/core/fiddler-chain)
* [FiddlerGeneration](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/core/fiddler-generation)
* [FiddlerSpan](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/core/fiddler-span)
* [FiddlerTool](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/core/fiddler-tool)
* [is\_fiddler\_span](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/core/is-fiddler-span)

### Tracing

Tracing module documentation

* [LangGraphInstrumentor](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/tracing/lang-graph-instrumentor)
* [add\_session\_attributes](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/tracing/add-session-attributes)
* [add\_span\_attributes](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/tracing/add-span-attributes)
* [set\_conversation\_id](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/tracing/set-conversation-id)
* [set\_llm\_context](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/tracing/set-llm-context)
* [JSONLSpanCapture](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/tracing/jsonl-span-capture)
* [JSONLSpanExporter](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/tracing/jsonl-span-exporter)
* [initialize\_jsonl\_capture](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/tracing/initialize-jsonl-capture)
