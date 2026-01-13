# Distributed Tracing Protocols - Detailed Specification Guide

Comprehensive technical reference for distributed tracing protocols and data formats.

---

## Table of Contents

1. [OTLP (OpenTelemetry Protocol)](#otlp-opentelemetry-protocol)
2. [W3C Trace Context](#w3c-trace-context)
3. [Jaeger Protocol](#jaeger-protocol)
4. [Zipkin Protocol](#zipkin-protocol)
5. [gRPC in Tracing](#grpc-in-tracing)
6. [Context Propagation](#context-propagation)
7. [Protocol Comparison](#protocol-comparison)

---

## OTLP (OpenTelemetry Protocol)

### Overview
OTLP is the native protocol for OpenTelemetry, designed for efficient collection and export of traces, metrics, and logs. It provides language-agnostic, vendor-neutral data format with multiple transport options.

### Key Characteristics
- **Format**: Protocol Buffers (protobuf3) for efficient binary serialization
- **Transports**: gRPC (primary), HTTP/protobuf, HTTP/JSON (experimental)
- **Bidirectional**: Supports streaming and request-response patterns
- **Stateless**: No session management required
- **Scalable**: Handles millions of spans per second

### OTLP/gRPC (Preferred)

**Transport Details**
- Uses HTTP/2 multiplexing
- Default ports: 4317 (unencrypted), 4318 (TLS)
- Connection: Long-lived, persistent
- Compression: Supports gzip compression
- Max message size: Configurable (default 4MB)

**Protocol Structure**
```protobuf
message ExportTraceServiceRequest {
  repeated ResourceSpans resource_spans = 1;
}

message ResourceSpans {
  Resource resource = 1;
  repeated InstrumentationLibrarySpans instrumentation_library_spans = 2;
  repeated Span spans = 3;
}

message Span {
  bytes trace_id = 1;           // 16-byte trace identifier
  bytes span_id = 2;            // 8-byte span identifier
  bytes parent_span_id = 3;     // Optional parent reference
  string name = 4;              // Operation name

  SpanKind kind = 5;            // INTERNAL, SERVER, CLIENT, PRODUCER, CONSUMER
  int64 start_time_unix_nano = 6;
  int64 end_time_unix_nano = 7;

  repeated KeyValue attributes = 8;
  repeated Event events = 9;
  repeated Link links = 10;

  Status status = 11;
  string trace_state = 12;
}

message Event {
  int64 time_unix_nano = 1;
  string name = 2;
  repeated KeyValue attributes = 3;
}

message Status {
  StatusCode code = 1;      // OK, ERROR, UNSET
  string message = 2;
}
```

**Example Request (JSON representation)**
```json
{
  "resourceSpans": [
    {
      "resource": {
        "attributes": [
          {
            "key": "service.name",
            "value": { "stringValue": "api-service" }
          },
          {
            "key": "service.version",
            "value": { "stringValue": "1.0.0" }
          }
        ]
      },
      "instrumentationLibrarySpans": [
        {
          "instrumentationLibrary": {
            "name": "io.opentelemetry.instrumentation",
            "version": "1.0.0"
          },
          "spans": [
            {
              "traceId": "4bf92f3577b34da6a3ce929d0e0e4736",
              "spanId": "00f067aa0ba902b7",
              "parentSpanId": "d3f067aa0ba902b7",
              "name": "GET /api/users",
              "kind": "SERVER",
              "startTimeUnixNano": "1669891200000000000",
              "endTimeUnixNano": "1669891201000000000",
              "attributes": [
                {
                  "key": "http.method",
                  "value": { "stringValue": "GET" }
                },
                {
                  "key": "http.url",
                  "value": { "stringValue": "http://localhost/api/users" }
                },
                {
                  "key": "http.status_code",
                  "value": { "intValue": "200" }
                }
              ],
              "events": [
                {
                  "timeUnixNano": "1669891200500000000",
                  "name": "db_query",
                  "attributes": [
                    {
                      "key": "db.operation",
                      "value": { "stringValue": "SELECT" }
                    }
                  ]
                }
              ],
              "status": {
                "code": "OK"
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### OTLP/HTTP

**Transport Details**
- Uses HTTP/1.1 or HTTP/2
- Endpoints: `http://host:4318/v1/traces` (traces), `/v1/metrics`, `/v1/logs`
- Default ports: 4318 (unencrypted), 4319 (TLS)
- Request method: POST
- Content-Type: `application/protobuf` (binary) or `application/json` (experimental)

**Request/Response**
```
POST /v1/traces HTTP/1.1
Content-Type: application/protobuf
Content-Encoding: gzip

[binary protobuf data]

HTTP/1.1 200 OK
Content-Type: application/protobuf
[empty body or optional response]
```

### Configuration Example

**OpenTelemetry Collector OTLP Receiver**
```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
        timeout: 10s
        max_recv_msg_size_mib: 50
      http:
        endpoint: 0.0.0.0:4318
        timeout: 10s
        max_content_length_logs: 2097152

processors:
  batch:
    send_batch_size: 256
    timeout: 5s
    send_batch_max_size: 512

exporters:
  jaeger:
    endpoint: jaeger-collector:14250

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [jaeger]
```

### Performance Characteristics

| Metric | gRPC | HTTP/Protobuf | HTTP/JSON |
|--------|------|---------------|-----------|
| Payload Size | Smallest | Small | Largest |
| Latency | <1ms | 1-2ms | 2-5ms |
| Throughput | Very High | High | Medium |
| CPU Usage | Low | Low | Medium |
| Compatibility | Modern systems | Universal | Browser-friendly |

---

## W3C Trace Context

### Overview
W3C Trace Context standardizes HTTP header format for propagating trace context across service boundaries. Enables interoperability between different tracing systems and vendors.

### Specification Versions

**Level 1 (W3C Recommendation)**
- Released November 2020
- HTTP header propagation for traces
- Minimal, stable specification

**Level 2 (W3C Candidate Recommendation)**
- Expected completion Q4 2025
- Enhanced response propagation
- Fingerprinting and privacy mitigations
- Improved identifier semantics
- Consent mechanisms

### HTTP Headers

#### traceparent Header

**Format**
```
traceparent: version-trace_id-parent_id-trace_flags
```

**Components**

| Component | Size | Format | Example |
|-----------|------|--------|---------|
| version | 2 hex | 00 (current) | 00 |
| trace_id | 32 hex | UUID-like (16 bytes) | 4bf92f3577b34da6a3ce929d0e0e4736 |
| parent_id | 16 hex | Span ID (8 bytes) | 00f067aa0ba902b7 |
| trace_flags | 2 hex | Sampled (1=yes, 0=no) | 01 |

**Full Example**
```
traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
```

**Field Details**
- `version` (00): Current version, reserves future extensions
- `trace_id`: Unique identifier for entire request path (128-bit)
- `parent_id`: Current span identifier in propagation chain (64-bit)
- `trace_flags`: Single byte with sampling bit (bit 0 = sampled yes/no)

#### tracestate Header

**Purpose**
- Vendor-specific trace context
- Comma-separated list of key-value pairs
- Each vendor has own namespace (e.g., "congo", "rojo", "datadog")

**Format**
```
tracestate: key1=value1, key2=value2, key3=value3
```

**Rules**
- Max 32 list members
- Key: `vendor_name` or `vendor_name@namespace`
- Value: up to 256 characters
- List order preserved
- Vendor-specific format

**Examples**
```
# Single vendor
tracestate: congo=t61rcWpm1t1

# Multiple vendors
tracestate: congo=t61rcWpm1t1,rojo=00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01

# Datadog example
tracestate: dd=s:1;o:rum;t.dm:-4
```

### Interaction with OpenTelemetry

OpenTelemetry implements W3C Trace Context propagator:

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.propagate import set_global_textmap
from opentelemetry.propagators.w3c_trace_context import W3CTraceContextPropagator

# Configure W3C Trace Context propagation
set_global_textmap(W3CTraceContextPropagator())

# HTTP request with automatic header injection
import requests
requests.get("http://downstream-service/api/data")
# Automatically includes: traceparent: 00-...-...-01
```

### Implementation Checklist

- Extract `traceparent` header on entry
- Validate format (version, trace_id, parent_id, flags)
- Create new span with extracted trace_id as parent
- Generate new span_id for current service
- Inject updated `traceparent` in outgoing requests
- Preserve `tracestate` and add vendor-specific entries if needed

---

## Jaeger Protocol

### Overview
Jaeger's native protocol for span submission and retrieval. Supports multiple serialization formats and transports.

### Historical: Thrift Protocol

**Format**
- Apache Thrift RPC format (binary)
- Efficient, compact serialization
- Widely used before OTLP

**Transports**
- UDP (port 6831, agent-based)
- HTTP (port 14268, collector-based)

**Thrift Definition (Historical)**
```thrift
service ThriftCollector {
  submitBatches(1: list<Batch> batches)
}

struct Batch {
  Process process,
  list<Span> spans
}

struct Span {
  i64 traceID,
  i64 spanID,
  i64 parentSpanID,
  string operationName,
  i32 references,
  i64 flags,
  i64 startTime,
  i64 duration,
  list<Tag> tags,
  list<Log> logs
}

struct Tag {
  string key,
  TagType vType,
  string vStr,
  i32 vInt,
  i64 vLong,
  double vDouble,
  bool vBool
}
```

### Modern: Jaeger v2 with OTLP

**Shift to OTLP**
- Jaeger v2 (2024+) adopts OTLP as primary protocol
- OTLP/gRPC on port 4317 (preferred)
- Backward compatibility with Thrift protocol
- Better ecosystem integration

**Configuration**
```yaml
# Jaeger v2 configuration
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318
  # Legacy Thrift support
  jaeger:
    protocols:
      grpc:
        endpoint: 0.0.0.0:14250
      thrift_http:
        endpoint: 0.0.0.0:14268
      thrift_compact:
        endpoint: 0.0.0.0:6831

exporters:
  jaeger:
    endpoint: localhost:14250
    tls:
      insecure: true

service:
  pipelines:
    traces:
      receivers: [otlp, jaeger]
      exporters: [jaeger]
```

### Jaeger-Specific Features

**Adaptive Sampling**
- Server-side sampling strategy determination
- Adjusts sampling rate based on traffic
- Minimizes data loss for critical services
- Configuration via sampling API

**Service Dependencies**
- Extracted from spans automatically
- Service call graphs generated
- Performance impact visualization

**Rich Query Capabilities**
- Search by span attributes
- Duration-based queries
- Tag-based filtering
- Complex boolean queries

---

## Zipkin Protocol

### Overview
Zipkin's native JSON-based protocol for trace submission and retrieval. Emphasizes simplicity and broad compatibility.

### JSON Format

**Span Model**
```json
{
  "traceId": "4bf92f3577b34da6a3ce929d0e0e4736",
  "id": "00f067aa0ba902b7",
  "parentId": "d3f067aa0ba902b7",
  "name": "GET /api/users",
  "timestamp": 1669891200000000,
  "duration": 1000000,
  "kind": "SERVER",
  "localEndpoint": {
    "serviceName": "api-service",
    "ipv4": "127.0.0.1",
    "port": 8080
  },
  "remoteEndpoint": {
    "serviceName": "client-service",
    "ipv4": "127.0.0.1",
    "port": 8081
  },
  "tags": {
    "http.method": "GET",
    "http.path": "/api/users",
    "http.status_code": "200",
    "error": "false"
  },
  "annotations": [
    {
      "timestamp": 1669891200500000,
      "value": "db_query"
    }
  ]
}
```

**Batch Format (Multiple Spans)**
```json
[
  { span object 1 },
  { span object 2 },
  { span object 3 }
]
```

### HTTP API

**Endpoint**
```
POST /api/v2/spans
Content-Type: application/json

[span1, span2, span3, ...]
```

**Response**
- 202 Accepted - Spans accepted for processing
- 400 Bad Request - Invalid format
- 413 Payload Too Large - Batch too large

### Configuration Example

```bash
# Send spans to Zipkin
curl -X POST http://zipkin:9411/api/v2/spans \
  -H "Content-Type: application/json" \
  -d '[
    {
      "traceId": "4bf92f3577b34da6a3ce929d0e0e4736",
      "id": "00f067aa0ba902b7",
      "name": "GET /api/users",
      "timestamp": 1669891200000000,
      "duration": 1000000,
      "kind": "SERVER",
      "localEndpoint": {
        "serviceName": "api-service"
      }
    }
  ]'
```

### Zipkin Compatibility

**Supported by Other Backends**
- Jaeger accepts Zipkin JSON spans
- Grafana Tempo accepts Zipkin format
- OpenTelemetry has Zipkin exporter

**Advantages**
- Human-readable JSON (no binary serialization)
- Simple HTTP API (easy debugging)
- No complex RPC frameworks needed
- Lightweight clients possible

---

## gRPC in Tracing

### Overview
gRPC provides high-performance RPC framework widely used in tracing protocols (primarily OTLP).

### HTTP/2 Multiplexing

**Efficiency**
- Single TCP connection for multiple streams
- Reduces connection overhead
- Better resource utilization
- Ideal for microservices

**Stream-Based Communication**
```
Client                          Server
  |                              |
  +------ Stream 1: Span A ----> |
  |                              |
  +------ Stream 2: Span B ----> |
  |                              |
  +------ Stream 3: Span C ----> |
  |                              |
  | <----- Stream 1: ACK --------+
  |                              |
```

### Protocol Buffers (protobuf)

**Advantages for Tracing**
- Compact binary encoding (30-50% smaller than JSON)
- Fast serialization/deserialization
- Schema evolution support
- Type safety

**Binary Size Comparison**
```
Span in JSON:      ~2 KB
Span in protobuf:  ~600 bytes
100K spans JSON:   ~200 MB
100K spans proto:  ~60 MB
```

### Configuration for High-Throughput

```go
// Go example with gRPC optimization
opts := []grpc.DialOption{
    grpc.WithDefaultCallOptions(
        grpc.MaxCallRecvMsgSize(50*1024*1024),
    ),
    grpc.WithKeepaliveParams(keepalive.ClientParameters{
        Time:                10 * time.Second,
        Timeout:             3 * time.Second,
        PermitWithoutStream: true,
    }),
}

conn, _ := grpc.Dial("jaeger-collector:4317", opts...)
```

---

## Context Propagation

### Propagation Mechanisms

**In-Process (Single Service)**
- Thread-local storage
- Context variable/async context
- No serialization needed

**Cross-Service (HTTP)**
- W3C Trace Context headers
- Custom headers (vendor-specific)
- Query parameters (fallback)

**Cross-Service (gRPC)**
- gRPC metadata headers
- Same format as HTTP (W3C Trace Context)
- Automatic injection/extraction

**Cross-Service (Message Queues)**
- Message headers/properties
- Payload wrapper (fallback)
- Message broker specific

### Propagator Implementations

**OpenTelemetry Propagators**
```python
from opentelemetry.propagate import inject, extract
from opentelemetry.propagators.w3c_trace_context import W3CTraceContextPropagator
from opentelemetry.propagators.jaeger import JaegerPropagator
from opentelemetry.propagators.b3 import B3SingleFormat, B3MultipleFormat

# W3C Trace Context (recommended)
set_global_textmap(W3CTraceContextPropagator())

# Inject headers in outgoing request
from opentelemetry import trace
headers = {}
trace.get_current_span().set_attribute("key", "value")

# Extract context from incoming request
ctx = extract(request.headers)
```

**Chain of Propagators**
```python
from opentelemetry.propagators.composite import CompositePropagator

set_global_textmap(
    CompositePropagator([
        W3CTraceContextPropagator(),
        JaegerPropagator(),
        B3SingleFormat()
    ])
)
```

---

## Protocol Comparison

### Feature Matrix

| Feature | OTLP/gRPC | OTLP/HTTP | Jaeger Thrift | Zipkin | gRPC-Generic |
|---------|-----------|-----------|---------------|--------|--------------|
| **Payload Size** | Smallest | Small | Small | Large | Smallest |
| **Latency** | <1ms | 1-2ms | 1-2ms | 2-5ms | <1ms |
| **Connection** | Persistent | Stateless | Persistent | Stateless | Persistent |
| **Compression** | gzip | gzip | None | None | gzip |
| **Streaming** | Yes | Yes | Yes | No | Yes |
| **Compatibility** | Universal | Universal | Jaeger-specific | Universal | Modern systems |
| **Debugging** | Hard (binary) | Easy (JSON) | Medium (Thrift) | Easy (JSON) | Hard (binary) |
| **Framework** | gRPC | HTTP/REST | Custom | HTTP/REST | gRPC |
| **Firewall-Friendly** | Medium | High | Low | High | Medium |

### Use Case Selection

**Choose OTLP/gRPC When**
- High throughput required (millions of spans/second)
- Latency sensitive (microservices)
- Modern, updated infrastructure
- Cost-conscious (small payloads)

**Choose OTLP/HTTP When**
- Corporate firewalls/proxies present
- Debugging important (human-readable)
- Legacy infrastructure
- Fallback required

**Choose Zipkin When**
- Simplicity paramount
- Existing Zipkin deployment
- HTTP-only requirements
- Human debugging critical

**Choose Jaeger When**
- Rich queries needed
- Adaptive sampling required
- Complex service graphs
- Enterprise features important

---

## Best Practices

### Protocol Selection Checklist

- [ ] Evaluate throughput requirements (spans/second)
- [ ] Assess latency sensitivity (SLA)
- [ ] Check firewall/proxy restrictions
- [ ] Consider backend capabilities
- [ ] Plan for multi-protocol support (backup)
- [ ] Monitor CPU/memory impact
- [ ] Test with realistic data volumes

### Configuration Recommendations

1. **Primary**: OTLP/gRPC for performance
2. **Fallback**: OTLP/HTTP for compatibility
3. **Propagation**: W3C Trace Context headers
4. **Batch Size**: 256 spans per batch
5. **Timeout**: 5-10 seconds
6. **Compression**: gzip enabled
7. **TLS**: Enabled in production

---

## Additional Resources

- OTLP Spec: https://opentelemetry.io/docs/specs/otel/protocol/
- W3C Trace Context: https://www.w3.org/TR/trace-context/
- Jaeger Documentation: https://www.jaegertracing.io/docs/
- Zipkin Architecture: https://zipkin.io/pages/architecture.html
- gRPC Performance: https://grpc.io/docs/guides/performance-best-practices/

