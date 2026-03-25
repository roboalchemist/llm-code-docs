# Source: https://docs.fiddler.ai/api/fiddler-langgraph-sdk/tracing/jsonl-span-exporter.md

# JSONLSpanExporter

SpanExporter that captures spans using JSONLSpanCapture.

## Parameters

| Parameter       | Type                                                                                               | Required | Default | Description                                              |
| --------------- | -------------------------------------------------------------------------------------------------- | -------- | ------- | -------------------------------------------------------- |
| `jsonl_capture` | [`JSONLSpanCapture`](https://docs.fiddler.ai/api/fiddler-langgraph-sdk/tracing/jsonl-span-capture) | ✗        | `None`  | The JSONLSpanCapture instance to use for capturing spans |

## export()

Export spans by capturing them with JSONLSpanCapture.

**Return type:** *SpanExportResult*
