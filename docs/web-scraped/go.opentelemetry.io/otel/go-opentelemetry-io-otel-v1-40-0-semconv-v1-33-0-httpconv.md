# Source: https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv

Title: httpconv package - go.opentelemetry.io/otel/semconv/v1.33.0/httpconv - Go Packages

URL Source: https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv

Markdown Content:
Package httpconv provides types and functionality for OpenTelemetry semantic conventions in the "http" namespace.

*   [type ClientActiveRequests](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientActiveRequests)
*       *   [func NewClientActiveRequests(m metric.Meter, opt ...metric.Int64UpDownCounterOption) (ClientActiveRequests, error)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#NewClientActiveRequests)

*       *   [func (m ClientActiveRequests) Add(ctx context.Context, incr int64, serverAddress string, serverPort int, ...)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientActiveRequests.Add)
    *   [func (ClientActiveRequests) AttrRequestMethod(val RequestMethodAttr) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientActiveRequests.AttrRequestMethod)
    *   [func (ClientActiveRequests) AttrURLScheme(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientActiveRequests.AttrURLScheme)
    *   [func (ClientActiveRequests) AttrURLTemplate(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientActiveRequests.AttrURLTemplate)
    *   [func (ClientActiveRequests) Description() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientActiveRequests.Description)
    *   [func (m ClientActiveRequests) Inst() metric.Int64UpDownCounter](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientActiveRequests.Inst)
    *   [func (ClientActiveRequests) Name() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientActiveRequests.Name)
    *   [func (ClientActiveRequests) Unit() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientActiveRequests.Unit)

*   [type ClientConnectionDuration](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientConnectionDuration)
*       *   [func NewClientConnectionDuration(m metric.Meter, opt ...metric.Float64HistogramOption) (ClientConnectionDuration, error)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#NewClientConnectionDuration)

*       *   [func (ClientConnectionDuration) AttrNetworkPeerAddress(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientConnectionDuration.AttrNetworkPeerAddress)
    *   [func (ClientConnectionDuration) AttrNetworkProtocolVersion(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientConnectionDuration.AttrNetworkProtocolVersion)
    *   [func (ClientConnectionDuration) AttrURLScheme(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientConnectionDuration.AttrURLScheme)
    *   [func (ClientConnectionDuration) Description() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientConnectionDuration.Description)
    *   [func (m ClientConnectionDuration) Inst() metric.Float64Histogram](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientConnectionDuration.Inst)
    *   [func (ClientConnectionDuration) Name() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientConnectionDuration.Name)
    *   [func (m ClientConnectionDuration) Record(ctx context.Context, val float64, serverAddress string, serverPort int, ...)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientConnectionDuration.Record)
    *   [func (ClientConnectionDuration) Unit() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientConnectionDuration.Unit)

*   [type ClientOpenConnections](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientOpenConnections)
*       *   [func NewClientOpenConnections(m metric.Meter, opt ...metric.Int64UpDownCounterOption) (ClientOpenConnections, error)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#NewClientOpenConnections)

*       *   [func (m ClientOpenConnections) Add(ctx context.Context, incr int64, connectionState ConnectionStateAttr, ...)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientOpenConnections.Add)
    *   [func (ClientOpenConnections) AttrNetworkPeerAddress(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientOpenConnections.AttrNetworkPeerAddress)
    *   [func (ClientOpenConnections) AttrNetworkProtocolVersion(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientOpenConnections.AttrNetworkProtocolVersion)
    *   [func (ClientOpenConnections) AttrURLScheme(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientOpenConnections.AttrURLScheme)
    *   [func (ClientOpenConnections) Description() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientOpenConnections.Description)
    *   [func (m ClientOpenConnections) Inst() metric.Int64UpDownCounter](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientOpenConnections.Inst)
    *   [func (ClientOpenConnections) Name() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientOpenConnections.Name)
    *   [func (ClientOpenConnections) Unit() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientOpenConnections.Unit)

*   [type ClientRequestBodySize](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize)
*       *   [func NewClientRequestBodySize(m metric.Meter, opt ...metric.Int64HistogramOption) (ClientRequestBodySize, error)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#NewClientRequestBodySize)

*       *   [func (ClientRequestBodySize) AttrErrorType(val ErrorTypeAttr) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize.AttrErrorType)
    *   [func (ClientRequestBodySize) AttrNetworkProtocolName(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize.AttrNetworkProtocolName)
    *   [func (ClientRequestBodySize) AttrNetworkProtocolVersion(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize.AttrNetworkProtocolVersion)
    *   [func (ClientRequestBodySize) AttrResponseStatusCode(val int) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize.AttrResponseStatusCode)
    *   [func (ClientRequestBodySize) AttrURLScheme(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize.AttrURLScheme)
    *   [func (ClientRequestBodySize) AttrURLTemplate(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize.AttrURLTemplate)
    *   [func (ClientRequestBodySize) Description() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize.Description)
    *   [func (m ClientRequestBodySize) Inst() metric.Int64Histogram](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize.Inst)
    *   [func (ClientRequestBodySize) Name() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize.Name)
    *   [func (m ClientRequestBodySize) Record(ctx context.Context, val int64, requestMethod RequestMethodAttr, ...)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize.Record)
    *   [func (ClientRequestBodySize) Unit() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize.Unit)

*   [type ClientRequestDuration](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestDuration)
*       *   [func NewClientRequestDuration(m metric.Meter, opt ...metric.Float64HistogramOption) (ClientRequestDuration, error)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#NewClientRequestDuration)

*       *   [func (ClientRequestDuration) AttrErrorType(val ErrorTypeAttr) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestDuration.AttrErrorType)
    *   [func (ClientRequestDuration) AttrNetworkProtocolName(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestDuration.AttrNetworkProtocolName)
    *   [func (ClientRequestDuration) AttrNetworkProtocolVersion(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestDuration.AttrNetworkProtocolVersion)
    *   [func (ClientRequestDuration) AttrResponseStatusCode(val int) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestDuration.AttrResponseStatusCode)
    *   [func (ClientRequestDuration) AttrURLScheme(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestDuration.AttrURLScheme)
    *   [func (ClientRequestDuration) AttrURLTemplate(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestDuration.AttrURLTemplate)
    *   [func (ClientRequestDuration) Description() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestDuration.Description)
    *   [func (m ClientRequestDuration) Inst() metric.Float64Histogram](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestDuration.Inst)
    *   [func (ClientRequestDuration) Name() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestDuration.Name)
    *   [func (m ClientRequestDuration) Record(ctx context.Context, val float64, requestMethod RequestMethodAttr, ...)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestDuration.Record)
    *   [func (ClientRequestDuration) Unit() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestDuration.Unit)

*   [type ClientResponseBodySize](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize)
*       *   [func NewClientResponseBodySize(m metric.Meter, opt ...metric.Int64HistogramOption) (ClientResponseBodySize, error)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#NewClientResponseBodySize)

*       *   [func (ClientResponseBodySize) AttrErrorType(val ErrorTypeAttr) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize.AttrErrorType)
    *   [func (ClientResponseBodySize) AttrNetworkProtocolName(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize.AttrNetworkProtocolName)
    *   [func (ClientResponseBodySize) AttrNetworkProtocolVersion(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize.AttrNetworkProtocolVersion)
    *   [func (ClientResponseBodySize) AttrResponseStatusCode(val int) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize.AttrResponseStatusCode)
    *   [func (ClientResponseBodySize) AttrURLScheme(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize.AttrURLScheme)
    *   [func (ClientResponseBodySize) AttrURLTemplate(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize.AttrURLTemplate)
    *   [func (ClientResponseBodySize) Description() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize.Description)
    *   [func (m ClientResponseBodySize) Inst() metric.Int64Histogram](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize.Inst)
    *   [func (ClientResponseBodySize) Name() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize.Name)
    *   [func (m ClientResponseBodySize) Record(ctx context.Context, val int64, requestMethod RequestMethodAttr, ...)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize.Record)
    *   [func (ClientResponseBodySize) Unit() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize.Unit)

*   [type ConnectionStateAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ConnectionStateAttr)
*   [type ErrorTypeAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ErrorTypeAttr)
*   [type RequestMethodAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#RequestMethodAttr)
*   [type ServerActiveRequests](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerActiveRequests)
*       *   [func NewServerActiveRequests(m metric.Meter, opt ...metric.Int64UpDownCounterOption) (ServerActiveRequests, error)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#NewServerActiveRequests)

*       *   [func (m ServerActiveRequests) Add(ctx context.Context, incr int64, requestMethod RequestMethodAttr, ...)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerActiveRequests.Add)
    *   [func (ServerActiveRequests) AttrServerAddress(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerActiveRequests.AttrServerAddress)
    *   [func (ServerActiveRequests) AttrServerPort(val int) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerActiveRequests.AttrServerPort)
    *   [func (ServerActiveRequests) Description() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerActiveRequests.Description)
    *   [func (m ServerActiveRequests) Inst() metric.Int64UpDownCounter](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerActiveRequests.Inst)
    *   [func (ServerActiveRequests) Name() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerActiveRequests.Name)
    *   [func (ServerActiveRequests) Unit() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerActiveRequests.Unit)

*   [type ServerRequestBodySize](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize)
*       *   [func NewServerRequestBodySize(m metric.Meter, opt ...metric.Int64HistogramOption) (ServerRequestBodySize, error)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#NewServerRequestBodySize)

*       *   [func (ServerRequestBodySize) AttrErrorType(val ErrorTypeAttr) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.AttrErrorType)
    *   [func (ServerRequestBodySize) AttrNetworkProtocolName(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.AttrNetworkProtocolName)
    *   [func (ServerRequestBodySize) AttrNetworkProtocolVersion(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.AttrNetworkProtocolVersion)
    *   [func (ServerRequestBodySize) AttrResponseStatusCode(val int) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.AttrResponseStatusCode)
    *   [func (ServerRequestBodySize) AttrRoute(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.AttrRoute)
    *   [func (ServerRequestBodySize) AttrServerAddress(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.AttrServerAddress)
    *   [func (ServerRequestBodySize) AttrServerPort(val int) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.AttrServerPort)
    *   [func (ServerRequestBodySize) AttrUserAgentSyntheticType(val UserAgentSyntheticTypeAttr) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.AttrUserAgentSyntheticType)
    *   [func (ServerRequestBodySize) Description() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.Description)
    *   [func (m ServerRequestBodySize) Inst() metric.Int64Histogram](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.Inst)
    *   [func (ServerRequestBodySize) Name() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.Name)
    *   [func (m ServerRequestBodySize) Record(ctx context.Context, val int64, requestMethod RequestMethodAttr, ...)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.Record)
    *   [func (ServerRequestBodySize) Unit() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.Unit)

*   [type ServerRequestDuration](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestDuration)
*       *   [func NewServerRequestDuration(m metric.Meter, opt ...metric.Float64HistogramOption) (ServerRequestDuration, error)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#NewServerRequestDuration)

*       *   [func (ServerRequestDuration) AttrErrorType(val ErrorTypeAttr) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestDuration.AttrErrorType)
    *   [func (ServerRequestDuration) AttrNetworkProtocolName(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestDuration.AttrNetworkProtocolName)
    *   [func (ServerRequestDuration) AttrNetworkProtocolVersion(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestDuration.AttrNetworkProtocolVersion)
    *   [func (ServerRequestDuration) AttrResponseStatusCode(val int) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestDuration.AttrResponseStatusCode)
    *   [func (ServerRequestDuration) AttrRoute(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestDuration.AttrRoute)
    *   [func (ServerRequestDuration) AttrServerAddress(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestDuration.AttrServerAddress)
    *   [func (ServerRequestDuration) AttrServerPort(val int) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestDuration.AttrServerPort)
    *   [func (ServerRequestDuration) AttrUserAgentSyntheticType(val UserAgentSyntheticTypeAttr) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestDuration.AttrUserAgentSyntheticType)
    *   [func (ServerRequestDuration) Description() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestDuration.Description)
    *   [func (m ServerRequestDuration) Inst() metric.Float64Histogram](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestDuration.Inst)
    *   [func (ServerRequestDuration) Name() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestDuration.Name)
    *   [func (m ServerRequestDuration) Record(ctx context.Context, val float64, requestMethod RequestMethodAttr, ...)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestDuration.Record)
    *   [func (ServerRequestDuration) Unit() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestDuration.Unit)

*   [type ServerResponseBodySize](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize)
*       *   [func NewServerResponseBodySize(m metric.Meter, opt ...metric.Int64HistogramOption) (ServerResponseBodySize, error)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#NewServerResponseBodySize)

*       *   [func (ServerResponseBodySize) AttrErrorType(val ErrorTypeAttr) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.AttrErrorType)
    *   [func (ServerResponseBodySize) AttrNetworkProtocolName(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.AttrNetworkProtocolName)
    *   [func (ServerResponseBodySize) AttrNetworkProtocolVersion(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.AttrNetworkProtocolVersion)
    *   [func (ServerResponseBodySize) AttrResponseStatusCode(val int) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.AttrResponseStatusCode)
    *   [func (ServerResponseBodySize) AttrRoute(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.AttrRoute)
    *   [func (ServerResponseBodySize) AttrServerAddress(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.AttrServerAddress)
    *   [func (ServerResponseBodySize) AttrServerPort(val int) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.AttrServerPort)
    *   [func (ServerResponseBodySize) AttrUserAgentSyntheticType(val UserAgentSyntheticTypeAttr) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.AttrUserAgentSyntheticType)
    *   [func (ServerResponseBodySize) Description() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.Description)
    *   [func (m ServerResponseBodySize) Inst() metric.Int64Histogram](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.Inst)
    *   [func (ServerResponseBodySize) Name() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.Name)
    *   [func (m ServerResponseBodySize) Record(ctx context.Context, val int64, requestMethod RequestMethodAttr, ...)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.Record)
    *   [func (ServerResponseBodySize) Unit() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.Unit)

*   [type UserAgentSyntheticTypeAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#UserAgentSyntheticTypeAttr)

This section is empty.

This section is empty.

This section is empty.

ClientActiveRequests is an instrument used to record metric values conforming to the "http.client.active_requests" semantic conventions. It represents the number of active HTTP requests.

NewClientActiveRequests returns a new ClientActiveRequests instrument.

Add adds incr to the existing count.

The serverAddress is the server domain name if available without reverse DNS lookup; otherwise, IP address or Unix domain socket name.

The serverPort is the port identifier of the ["URI origin"](https://www.rfc-editor.org/rfc/rfc9110.html#name-uri-origin) HTTP request is sent to.

All additional attrs passed are included in the recorded value.

AttrRequestMethod returns an optional attribute for the "http.request.method" semantic convention. It represents the HTTP request method.

AttrURLScheme returns an optional attribute for the "url.scheme" semantic convention. It represents the [URI scheme](https://www.rfc-editor.org/rfc/rfc3986#section-3.1) component identifying the used protocol.

AttrURLTemplate returns an optional attribute for the "url.template" semantic convention. It represents the low-cardinality template of an [absolute path reference](https://www.rfc-editor.org/rfc/rfc3986#section-4.2).

Description returns the semantic convention description of the instrument

Inst returns the underlying metric instrument.

Name returns the semantic convention name of the instrument.

Unit returns the semantic convention unit of the instrument

ClientConnectionDuration is an instrument used to record metric values conforming to the "http.client.connection.duration" semantic conventions. It represents the duration of the successfully established outbound HTTP connections.

NewClientConnectionDuration returns a new ClientConnectionDuration instrument.

AttrNetworkPeerAddress returns an optional attribute for the "network.peer.address" semantic convention. It represents the peer address of the network connection - IP address or Unix domain socket name.

AttrNetworkProtocolVersion returns an optional attribute for the "network.protocol.version" semantic convention. It represents the actual version of the protocol used for network communication.

AttrURLScheme returns an optional attribute for the "url.scheme" semantic convention. It represents the [URI scheme](https://www.rfc-editor.org/rfc/rfc3986#section-3.1) component identifying the used protocol.

Description returns the semantic convention description of the instrument

Inst returns the underlying metric instrument.

Name returns the semantic convention name of the instrument.

Record records val to the current distribution.

The serverAddress is the server domain name if available without reverse DNS lookup; otherwise, IP address or Unix domain socket name.

The serverPort is the port identifier of the ["URI origin"](https://www.rfc-editor.org/rfc/rfc9110.html#name-uri-origin) HTTP request is sent to.

All additional attrs passed are included in the recorded value.

Unit returns the semantic convention unit of the instrument

ClientOpenConnections is an instrument used to record metric values conforming to the "http.client.open_connections" semantic conventions. It represents the number of outbound HTTP connections that are currently active or idle on the client.

NewClientOpenConnections returns a new ClientOpenConnections instrument.

Add adds incr to the existing count.

The connectionState is the state of the HTTP connection in the HTTP connection pool.

The serverAddress is the server domain name if available without reverse DNS lookup; otherwise, IP address or Unix domain socket name.

The serverPort is the port identifier of the ["URI origin"](https://www.rfc-editor.org/rfc/rfc9110.html#name-uri-origin) HTTP request is sent to.

All additional attrs passed are included in the recorded value.

AttrNetworkPeerAddress returns an optional attribute for the "network.peer.address" semantic convention. It represents the peer address of the network connection - IP address or Unix domain socket name.

AttrNetworkProtocolVersion returns an optional attribute for the "network.protocol.version" semantic convention. It represents the actual version of the protocol used for network communication.

AttrURLScheme returns an optional attribute for the "url.scheme" semantic convention. It represents the [URI scheme](https://www.rfc-editor.org/rfc/rfc3986#section-3.1) component identifying the used protocol.

Description returns the semantic convention description of the instrument

Inst returns the underlying metric instrument.

Name returns the semantic convention name of the instrument.

Unit returns the semantic convention unit of the instrument

#### type [ClientRequestBodySize](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L431)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize "Go to ClientRequestBodySize")

ClientRequestBodySize is an instrument used to record metric values conforming to the "http.client.request.body.size" semantic conventions. It represents the size of HTTP client request bodies.

#### func (ClientRequestBodySize) [AttrErrorType](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L531)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize.AttrErrorType "Go to ClientRequestBodySize.AttrErrorType")

AttrErrorType returns an optional attribute for the "error.type" semantic convention. It represents the describes a class of error the operation ended with.

#### func (ClientRequestBodySize) [AttrNetworkProtocolName](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L549)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize.AttrNetworkProtocolName "Go to ClientRequestBodySize.AttrNetworkProtocolName")

AttrNetworkProtocolName returns an optional attribute for the "network.protocol.name" semantic convention. It represents the [OSI application layer](https://wikipedia.org/wiki/Application_layer) or non-OSI equivalent.

#### func (ClientRequestBodySize) [AttrNetworkProtocolVersion](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L565)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize.AttrNetworkProtocolVersion "Go to ClientRequestBodySize.AttrNetworkProtocolVersion")

AttrNetworkProtocolVersion returns an optional attribute for the "network.protocol.version" semantic convention. It represents the actual version of the protocol used for network communication.

#### func (ClientRequestBodySize) [AttrURLScheme](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L574)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize.AttrURLScheme "Go to ClientRequestBodySize.AttrURLScheme")

AttrURLScheme returns an optional attribute for the "url.scheme" semantic convention. It represents the [URI scheme](https://www.rfc-editor.org/rfc/rfc3986#section-3.1) component identifying the used protocol.

#### func (ClientRequestBodySize) [AttrURLTemplate](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L558)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize.AttrURLTemplate "Go to ClientRequestBodySize.AttrURLTemplate")

AttrURLTemplate returns an optional attribute for the "url.template" semantic convention. It represents the low-cardinality template of an [absolute path reference](https://www.rfc-editor.org/rfc/rfc3986#section-4.2).

#### func (ClientRequestBodySize) [Description](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L474)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize.Description "Go to ClientRequestBodySize.Description")

Description returns the semantic convention description of the instrument

#### func (ClientRequestBodySize) [Inst](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L459)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize.Inst "Go to ClientRequestBodySize.Inst")

Inst returns the underlying metric instrument.

#### func (ClientRequestBodySize) [Name](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L464)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize.Name "Go to ClientRequestBodySize.Name")

Name returns the semantic convention name of the instrument.

#### func (ClientRequestBodySize) [Record](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L499)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize.Record "Go to ClientRequestBodySize.Record")

Record records val to the current distribution.

The requestMethod is the HTTP request method.

The serverAddress is the host identifier of the ["URI origin"](https://www.rfc-editor.org/rfc/rfc9110.html#name-uri-origin) HTTP request is sent to.

The serverPort is the port identifier of the ["URI origin"](https://www.rfc-editor.org/rfc/rfc9110.html#name-uri-origin) HTTP request is sent to.

All additional attrs passed are included in the recorded value.

The size of the request payload body in bytes. This is the number of bytes transferred excluding headers and is often, but not always, present as the [Content-Length](https://www.rfc-editor.org/rfc/rfc9110.html#field.content-length) header. For requests using transport encoding, this should be the compressed size.

#### func (ClientRequestBodySize) [Unit](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L469)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientRequestBodySize.Unit "Go to ClientRequestBodySize.Unit")

Unit returns the semantic convention unit of the instrument

ClientRequestDuration is an instrument used to record metric values conforming to the "http.client.request.duration" semantic conventions. It represents the duration of HTTP client requests.

NewClientRequestDuration returns a new ClientRequestDuration instrument.

AttrErrorType returns an optional attribute for the "error.type" semantic convention. It represents the describes a class of error the operation ended with.

AttrNetworkProtocolName returns an optional attribute for the "network.protocol.name" semantic convention. It represents the [OSI application layer](https://wikipedia.org/wiki/Application_layer) or non-OSI equivalent.

AttrNetworkProtocolVersion returns an optional attribute for the "network.protocol.version" semantic convention. It represents the actual version of the protocol used for network communication.

AttrResponseStatusCode returns an optional attribute for the "http.response.status_code" semantic convention. It represents the [HTTP response status code](https://tools.ietf.org/html/rfc7231#section-6).

AttrURLScheme returns an optional attribute for the "url.scheme" semantic convention. It represents the [URI scheme](https://www.rfc-editor.org/rfc/rfc3986#section-3.1) component identifying the used protocol.

AttrURLTemplate returns an optional attribute for the "url.template" semantic convention. It represents the low-cardinality template of an [absolute path reference](https://www.rfc-editor.org/rfc/rfc3986#section-4.2).

Description returns the semantic convention description of the instrument

Inst returns the underlying metric instrument.

Name returns the semantic convention name of the instrument.

Record records val to the current distribution.

The requestMethod is the HTTP request method.

The serverAddress is the host identifier of the ["URI origin"](https://www.rfc-editor.org/rfc/rfc9110.html#name-uri-origin) HTTP request is sent to.

The serverPort is the port identifier of the ["URI origin"](https://www.rfc-editor.org/rfc/rfc9110.html#name-uri-origin) HTTP request is sent to.

All additional attrs passed are included in the recorded value.

Unit returns the semantic convention unit of the instrument

#### type [ClientResponseBodySize](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L724)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize "Go to ClientResponseBodySize")

ClientResponseBodySize is an instrument used to record metric values conforming to the "http.client.response.body.size" semantic conventions. It represents the size of HTTP client response bodies.

#### func (ClientResponseBodySize) [AttrErrorType](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L824)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize.AttrErrorType "Go to ClientResponseBodySize.AttrErrorType")

AttrErrorType returns an optional attribute for the "error.type" semantic convention. It represents the describes a class of error the operation ended with.

#### func (ClientResponseBodySize) [AttrNetworkProtocolName](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L842)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize.AttrNetworkProtocolName "Go to ClientResponseBodySize.AttrNetworkProtocolName")

AttrNetworkProtocolName returns an optional attribute for the "network.protocol.name" semantic convention. It represents the [OSI application layer](https://wikipedia.org/wiki/Application_layer) or non-OSI equivalent.

#### func (ClientResponseBodySize) [AttrNetworkProtocolVersion](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L858)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize.AttrNetworkProtocolVersion "Go to ClientResponseBodySize.AttrNetworkProtocolVersion")

AttrNetworkProtocolVersion returns an optional attribute for the "network.protocol.version" semantic convention. It represents the actual version of the protocol used for network communication.

#### func (ClientResponseBodySize) [AttrURLScheme](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L867)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize.AttrURLScheme "Go to ClientResponseBodySize.AttrURLScheme")

AttrURLScheme returns an optional attribute for the "url.scheme" semantic convention. It represents the [URI scheme](https://www.rfc-editor.org/rfc/rfc3986#section-3.1) component identifying the used protocol.

#### func (ClientResponseBodySize) [AttrURLTemplate](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L851)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize.AttrURLTemplate "Go to ClientResponseBodySize.AttrURLTemplate")

AttrURLTemplate returns an optional attribute for the "url.template" semantic convention. It represents the low-cardinality template of an [absolute path reference](https://www.rfc-editor.org/rfc/rfc3986#section-4.2).

#### func (ClientResponseBodySize) [Description](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L767)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize.Description "Go to ClientResponseBodySize.Description")

Description returns the semantic convention description of the instrument

#### func (ClientResponseBodySize) [Inst](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L752)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize.Inst "Go to ClientResponseBodySize.Inst")

Inst returns the underlying metric instrument.

#### func (ClientResponseBodySize) [Name](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L757)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize.Name "Go to ClientResponseBodySize.Name")

Name returns the semantic convention name of the instrument.

#### func (ClientResponseBodySize) [Record](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L792)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize.Record "Go to ClientResponseBodySize.Record")

Record records val to the current distribution.

The requestMethod is the HTTP request method.

The serverAddress is the host identifier of the ["URI origin"](https://www.rfc-editor.org/rfc/rfc9110.html#name-uri-origin) HTTP request is sent to.

The serverPort is the port identifier of the ["URI origin"](https://www.rfc-editor.org/rfc/rfc9110.html#name-uri-origin) HTTP request is sent to.

All additional attrs passed are included in the recorded value.

The size of the response payload body in bytes. This is the number of bytes transferred excluding headers and is often, but not always, present as the [Content-Length](https://www.rfc-editor.org/rfc/rfc9110.html#field.content-length) header. For requests using transport encoding, this should be the compressed size.

#### func (ClientResponseBodySize) [Unit](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L762)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ClientResponseBodySize.Unit "Go to ClientResponseBodySize.Unit")

Unit returns the semantic convention unit of the instrument

type ConnectionStateAttr [string](https://pkg.go.dev/builtin#string)

ConnectionStateAttr is an attribute conforming to the http.connection.state semantic conventions. It represents the state of the HTTP connection in the HTTP connection pool.

var (
	ConnectionStateActive [ConnectionStateAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ConnectionStateAttr) = "active"
	ConnectionStateIdle [ConnectionStateAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ConnectionStateAttr) = "idle"
)

ErrorTypeAttr is an attribute conforming to the error.type semantic conventions. It represents the describes a class of error the operation ended with.

var (
	
	ErrorTypeOther [ErrorTypeAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ErrorTypeAttr) = "_OTHER"
)

RequestMethodAttr is an attribute conforming to the http.request.method semantic conventions. It represents the HTTP request method.

var (
	RequestMethodConnect [RequestMethodAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#RequestMethodAttr) = "CONNECT"
	RequestMethodDelete [RequestMethodAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#RequestMethodAttr) = "DELETE"
	RequestMethodGet [RequestMethodAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#RequestMethodAttr) = "GET"
	RequestMethodHead [RequestMethodAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#RequestMethodAttr) = "HEAD"
	RequestMethodOptions [RequestMethodAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#RequestMethodAttr) = "OPTIONS"
	RequestMethodPatch [RequestMethodAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#RequestMethodAttr) = "PATCH"
	RequestMethodPost [RequestMethodAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#RequestMethodAttr) = "POST"
	RequestMethodPut [RequestMethodAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#RequestMethodAttr) = "PUT"
	RequestMethodTrace [RequestMethodAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#RequestMethodAttr) = "TRACE"
	
	RequestMethodOther [RequestMethodAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#RequestMethodAttr) = "_OTHER"
)

ServerActiveRequests is an instrument used to record metric values conforming to the "http.server.active_requests" semantic conventions. It represents the number of active HTTP server requests.

NewServerActiveRequests returns a new ServerActiveRequests instrument.

Add adds incr to the existing count.

The requestMethod is the HTTP request method.

The urlScheme is the the [URI scheme](https://www.rfc-editor.org/rfc/rfc3986#section-3.1) component identifying the used protocol.

All additional attrs passed are included in the recorded value.

AttrServerAddress returns an optional attribute for the "server.address" semantic convention. It represents the name of the local HTTP server that received the request.

AttrServerPort returns an optional attribute for the "server.port" semantic convention. It represents the port of the local HTTP server that received the request.

Description returns the semantic convention description of the instrument

Inst returns the underlying metric instrument.

Name returns the semantic convention name of the instrument.

Unit returns the semantic convention unit of the instrument

#### type [ServerRequestBodySize](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L974)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize "Go to ServerRequestBodySize")

ServerRequestBodySize is an instrument used to record metric values conforming to the "http.server.request.body.size" semantic conventions. It represents the size of HTTP server request bodies.

#### func (ServerRequestBodySize) [AttrErrorType](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1067)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.AttrErrorType "Go to ServerRequestBodySize.AttrErrorType")

AttrErrorType returns an optional attribute for the "error.type" semantic convention. It represents the describes a class of error the operation ended with.

#### func (ServerRequestBodySize) [AttrNetworkProtocolName](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1092)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.AttrNetworkProtocolName "Go to ServerRequestBodySize.AttrNetworkProtocolName")

AttrNetworkProtocolName returns an optional attribute for the "network.protocol.name" semantic convention. It represents the [OSI application layer](https://wikipedia.org/wiki/Application_layer) or non-OSI equivalent.

#### func (ServerRequestBodySize) [AttrNetworkProtocolVersion](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1099)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.AttrNetworkProtocolVersion "Go to ServerRequestBodySize.AttrNetworkProtocolVersion")

AttrNetworkProtocolVersion returns an optional attribute for the "network.protocol.version" semantic convention. It represents the actual version of the protocol used for network communication.

#### func (ServerRequestBodySize) [AttrRoute](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1083)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.AttrRoute "Go to ServerRequestBodySize.AttrRoute")

AttrRoute returns an optional attribute for the "http.route" semantic convention. It represents the matched route, that is, the path template in the format used by the respective server framework.

#### func (ServerRequestBodySize) [AttrServerAddress](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1106)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.AttrServerAddress "Go to ServerRequestBodySize.AttrServerAddress")

AttrServerAddress returns an optional attribute for the "server.address" semantic convention. It represents the name of the local HTTP server that received the request.

#### func (ServerRequestBodySize) [AttrServerPort](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1113)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.AttrServerPort "Go to ServerRequestBodySize.AttrServerPort")

AttrServerPort returns an optional attribute for the "server.port" semantic convention. It represents the port of the local HTTP server that received the request.

#### func (ServerRequestBodySize) [AttrUserAgentSyntheticType](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1120)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.AttrUserAgentSyntheticType "Go to ServerRequestBodySize.AttrUserAgentSyntheticType")

AttrUserAgentSyntheticType returns an optional attribute for the "user_agent.synthetic.type" semantic convention. It represents the specifies the category of synthetic traffic, such as tests or bots.

#### func (ServerRequestBodySize) [Description](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1017)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.Description "Go to ServerRequestBodySize.Description")

Description returns the semantic convention description of the instrument

#### func (ServerRequestBodySize) [Inst](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1002)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.Inst "Go to ServerRequestBodySize.Inst")

Inst returns the underlying metric instrument.

#### func (ServerRequestBodySize) [Name](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1007)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.Name "Go to ServerRequestBodySize.Name")

Name returns the semantic convention name of the instrument.

#### func (ServerRequestBodySize) [Record](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1037)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.Record "Go to ServerRequestBodySize.Record")

Record records val to the current distribution.

The requestMethod is the HTTP request method.

The urlScheme is the the [URI scheme](https://www.rfc-editor.org/rfc/rfc3986#section-3.1) component identifying the used protocol.

All additional attrs passed are included in the recorded value.

The size of the request payload body in bytes. This is the number of bytes transferred excluding headers and is often, but not always, present as the [Content-Length](https://www.rfc-editor.org/rfc/rfc9110.html#field.content-length) header. For requests using transport encoding, this should be the compressed size.

#### func (ServerRequestBodySize) [Unit](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1012)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerRequestBodySize.Unit "Go to ServerRequestBodySize.Unit")

Unit returns the semantic convention unit of the instrument

ServerRequestDuration is an instrument used to record metric values conforming to the "http.server.request.duration" semantic conventions. It represents the duration of HTTP server requests.

NewServerRequestDuration returns a new ServerRequestDuration instrument.

AttrErrorType returns an optional attribute for the "error.type" semantic convention. It represents the describes a class of error the operation ended with.

AttrNetworkProtocolName returns an optional attribute for the "network.protocol.name" semantic convention. It represents the [OSI application layer](https://wikipedia.org/wiki/Application_layer) or non-OSI equivalent.

AttrNetworkProtocolVersion returns an optional attribute for the "network.protocol.version" semantic convention. It represents the actual version of the protocol used for network communication.

AttrResponseStatusCode returns an optional attribute for the "http.response.status_code" semantic convention. It represents the [HTTP response status code](https://tools.ietf.org/html/rfc7231#section-6).

AttrRoute returns an optional attribute for the "http.route" semantic convention. It represents the matched route, that is, the path template in the format used by the respective server framework.

AttrServerAddress returns an optional attribute for the "server.address" semantic convention. It represents the name of the local HTTP server that received the request.

AttrServerPort returns an optional attribute for the "server.port" semantic convention. It represents the port of the local HTTP server that received the request.

AttrUserAgentSyntheticType returns an optional attribute for the "user_agent.synthetic.type" semantic convention. It represents the specifies the category of synthetic traffic, such as tests or bots.

Description returns the semantic convention description of the instrument

Inst returns the underlying metric instrument.

Name returns the semantic convention name of the instrument.

Record records val to the current distribution.

The requestMethod is the HTTP request method.

The urlScheme is the the [URI scheme](https://www.rfc-editor.org/rfc/rfc3986#section-3.1) component identifying the used protocol.

All additional attrs passed are included in the recorded value.

Unit returns the semantic convention unit of the instrument

#### type [ServerResponseBodySize](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1273)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize "Go to ServerResponseBodySize")

ServerResponseBodySize is an instrument used to record metric values conforming to the "http.server.response.body.size" semantic conventions. It represents the size of HTTP server response bodies.

#### func (ServerResponseBodySize) [AttrErrorType](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1366)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.AttrErrorType "Go to ServerResponseBodySize.AttrErrorType")

AttrErrorType returns an optional attribute for the "error.type" semantic convention. It represents the describes a class of error the operation ended with.

#### func (ServerResponseBodySize) [AttrNetworkProtocolName](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1391)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.AttrNetworkProtocolName "Go to ServerResponseBodySize.AttrNetworkProtocolName")

AttrNetworkProtocolName returns an optional attribute for the "network.protocol.name" semantic convention. It represents the [OSI application layer](https://wikipedia.org/wiki/Application_layer) or non-OSI equivalent.

#### func (ServerResponseBodySize) [AttrNetworkProtocolVersion](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1398)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.AttrNetworkProtocolVersion "Go to ServerResponseBodySize.AttrNetworkProtocolVersion")

AttrNetworkProtocolVersion returns an optional attribute for the "network.protocol.version" semantic convention. It represents the actual version of the protocol used for network communication.

#### func (ServerResponseBodySize) [AttrRoute](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1382)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.AttrRoute "Go to ServerResponseBodySize.AttrRoute")

AttrRoute returns an optional attribute for the "http.route" semantic convention. It represents the matched route, that is, the path template in the format used by the respective server framework.

#### func (ServerResponseBodySize) [AttrServerAddress](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1405)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.AttrServerAddress "Go to ServerResponseBodySize.AttrServerAddress")

AttrServerAddress returns an optional attribute for the "server.address" semantic convention. It represents the name of the local HTTP server that received the request.

#### func (ServerResponseBodySize) [AttrServerPort](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1412)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.AttrServerPort "Go to ServerResponseBodySize.AttrServerPort")

AttrServerPort returns an optional attribute for the "server.port" semantic convention. It represents the port of the local HTTP server that received the request.

#### func (ServerResponseBodySize) [AttrUserAgentSyntheticType](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1419)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.AttrUserAgentSyntheticType "Go to ServerResponseBodySize.AttrUserAgentSyntheticType")

AttrUserAgentSyntheticType returns an optional attribute for the "user_agent.synthetic.type" semantic convention. It represents the specifies the category of synthetic traffic, such as tests or bots.

#### func (ServerResponseBodySize) [Description](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1316)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.Description "Go to ServerResponseBodySize.Description")

Description returns the semantic convention description of the instrument

#### func (ServerResponseBodySize) [Inst](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1301)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.Inst "Go to ServerResponseBodySize.Inst")

Inst returns the underlying metric instrument.

#### func (ServerResponseBodySize) [Name](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1306)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.Name "Go to ServerResponseBodySize.Name")

Name returns the semantic convention name of the instrument.

#### func (ServerResponseBodySize) [Record](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1336)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.Record "Go to ServerResponseBodySize.Record")

Record records val to the current distribution.

The requestMethod is the HTTP request method.

The urlScheme is the the [URI scheme](https://www.rfc-editor.org/rfc/rfc3986#section-3.1) component identifying the used protocol.

All additional attrs passed are included in the recorded value.

The size of the response payload body in bytes. This is the number of bytes transferred excluding headers and is often, but not always, present as the [Content-Length](https://www.rfc-editor.org/rfc/rfc9110.html#field.content-length) header. For requests using transport encoding, this should be the compressed size.

#### func (ServerResponseBodySize) [Unit](https://github.com/open-telemetry/opentelemetry-go/blob/v1.40.0/semconv/v1.33.0/httpconv/metric.go#L1311)[¶](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#ServerResponseBodySize.Unit "Go to ServerResponseBodySize.Unit")

Unit returns the semantic convention unit of the instrument

type UserAgentSyntheticTypeAttr [string](https://pkg.go.dev/builtin#string)

UserAgentSyntheticTypeAttr is an attribute conforming to the user_agent.synthetic.type semantic conventions. It represents the specifies the category of synthetic traffic, such as tests or bots.

var (
	UserAgentSyntheticTypeBot [UserAgentSyntheticTypeAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#UserAgentSyntheticTypeAttr) = "bot"
	UserAgentSyntheticTypeTest [UserAgentSyntheticTypeAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.33.0/httpconv#UserAgentSyntheticTypeAttr) = "test"
)
