# Source: https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv

Title: dbconv package - go.opentelemetry.io/otel/semconv/v1.34.0/dbconv - Go Packages

URL Source: https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv

Markdown Content:
Package dbconv provides types and functionality for OpenTelemetry semantic conventions in the "db" namespace.

*   [type ClientConnectionCount](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionCount)
*       *   [func NewClientConnectionCount(m metric.Meter, opt ...metric.Int64UpDownCounterOption) (ClientConnectionCount, error)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#NewClientConnectionCount)

*       *   [func (m ClientConnectionCount) Add(ctx context.Context, incr int64, clientConnectionPoolName string, ...)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionCount.Add)
    *   [func (ClientConnectionCount) Description() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionCount.Description)
    *   [func (m ClientConnectionCount) Inst() metric.Int64UpDownCounter](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionCount.Inst)
    *   [func (ClientConnectionCount) Name() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionCount.Name)
    *   [func (ClientConnectionCount) Unit() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionCount.Unit)

*   [type ClientConnectionCreateTime](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionCreateTime)
*       *   [func NewClientConnectionCreateTime(m metric.Meter, opt ...metric.Float64HistogramOption) (ClientConnectionCreateTime, error)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#NewClientConnectionCreateTime)

*       *   [func (ClientConnectionCreateTime) Description() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionCreateTime.Description)
    *   [func (m ClientConnectionCreateTime) Inst() metric.Float64Histogram](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionCreateTime.Inst)
    *   [func (ClientConnectionCreateTime) Name() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionCreateTime.Name)
    *   [func (m ClientConnectionCreateTime) Record(ctx context.Context, val float64, clientConnectionPoolName string, ...)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionCreateTime.Record)
    *   [func (ClientConnectionCreateTime) Unit() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionCreateTime.Unit)

*   [type ClientConnectionIdleMax](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionIdleMax)
*       *   [func NewClientConnectionIdleMax(m metric.Meter, opt ...metric.Int64UpDownCounterOption) (ClientConnectionIdleMax, error)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#NewClientConnectionIdleMax)

*       *   [func (m ClientConnectionIdleMax) Add(ctx context.Context, incr int64, clientConnectionPoolName string, ...)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionIdleMax.Add)
    *   [func (ClientConnectionIdleMax) Description() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionIdleMax.Description)
    *   [func (m ClientConnectionIdleMax) Inst() metric.Int64UpDownCounter](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionIdleMax.Inst)
    *   [func (ClientConnectionIdleMax) Name() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionIdleMax.Name)
    *   [func (ClientConnectionIdleMax) Unit() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionIdleMax.Unit)

*   [type ClientConnectionIdleMin](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionIdleMin)
*       *   [func NewClientConnectionIdleMin(m metric.Meter, opt ...metric.Int64UpDownCounterOption) (ClientConnectionIdleMin, error)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#NewClientConnectionIdleMin)

*       *   [func (m ClientConnectionIdleMin) Add(ctx context.Context, incr int64, clientConnectionPoolName string, ...)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionIdleMin.Add)
    *   [func (ClientConnectionIdleMin) Description() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionIdleMin.Description)
    *   [func (m ClientConnectionIdleMin) Inst() metric.Int64UpDownCounter](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionIdleMin.Inst)
    *   [func (ClientConnectionIdleMin) Name() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionIdleMin.Name)
    *   [func (ClientConnectionIdleMin) Unit() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionIdleMin.Unit)

*   [type ClientConnectionMax](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionMax)
*       *   [func NewClientConnectionMax(m metric.Meter, opt ...metric.Int64UpDownCounterOption) (ClientConnectionMax, error)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#NewClientConnectionMax)

*       *   [func (m ClientConnectionMax) Add(ctx context.Context, incr int64, clientConnectionPoolName string, ...)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionMax.Add)
    *   [func (ClientConnectionMax) Description() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionMax.Description)
    *   [func (m ClientConnectionMax) Inst() metric.Int64UpDownCounter](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionMax.Inst)
    *   [func (ClientConnectionMax) Name() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionMax.Name)
    *   [func (ClientConnectionMax) Unit() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionMax.Unit)

*   [type ClientConnectionPendingRequests](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionPendingRequests)
*       *   [func NewClientConnectionPendingRequests(m metric.Meter, opt ...metric.Int64UpDownCounterOption) (ClientConnectionPendingRequests, error)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#NewClientConnectionPendingRequests)

*       *   [func (m ClientConnectionPendingRequests) Add(ctx context.Context, incr int64, clientConnectionPoolName string, ...)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionPendingRequests.Add)
    *   [func (ClientConnectionPendingRequests) Description() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionPendingRequests.Description)
    *   [func (m ClientConnectionPendingRequests) Inst() metric.Int64UpDownCounter](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionPendingRequests.Inst)
    *   [func (ClientConnectionPendingRequests) Name() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionPendingRequests.Name)
    *   [func (ClientConnectionPendingRequests) Unit() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionPendingRequests.Unit)

*   [type ClientConnectionStateAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionStateAttr)
*   [type ClientConnectionTimeouts](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionTimeouts)
*       *   [func NewClientConnectionTimeouts(m metric.Meter, opt ...metric.Int64CounterOption) (ClientConnectionTimeouts, error)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#NewClientConnectionTimeouts)

*       *   [func (m ClientConnectionTimeouts) Add(ctx context.Context, incr int64, clientConnectionPoolName string, ...)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionTimeouts.Add)
    *   [func (ClientConnectionTimeouts) Description() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionTimeouts.Description)
    *   [func (m ClientConnectionTimeouts) Inst() metric.Int64Counter](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionTimeouts.Inst)
    *   [func (ClientConnectionTimeouts) Name() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionTimeouts.Name)
    *   [func (ClientConnectionTimeouts) Unit() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionTimeouts.Unit)

*   [type ClientConnectionUseTime](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionUseTime)
*       *   [func NewClientConnectionUseTime(m metric.Meter, opt ...metric.Float64HistogramOption) (ClientConnectionUseTime, error)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#NewClientConnectionUseTime)

*       *   [func (ClientConnectionUseTime) Description() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionUseTime.Description)
    *   [func (m ClientConnectionUseTime) Inst() metric.Float64Histogram](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionUseTime.Inst)
    *   [func (ClientConnectionUseTime) Name() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionUseTime.Name)
    *   [func (m ClientConnectionUseTime) Record(ctx context.Context, val float64, clientConnectionPoolName string, ...)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionUseTime.Record)
    *   [func (ClientConnectionUseTime) Unit() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionUseTime.Unit)

*   [type ClientConnectionWaitTime](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionWaitTime)
*       *   [func NewClientConnectionWaitTime(m metric.Meter, opt ...metric.Float64HistogramOption) (ClientConnectionWaitTime, error)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#NewClientConnectionWaitTime)

*       *   [func (ClientConnectionWaitTime) Description() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionWaitTime.Description)
    *   [func (m ClientConnectionWaitTime) Inst() metric.Float64Histogram](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionWaitTime.Inst)
    *   [func (ClientConnectionWaitTime) Name() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionWaitTime.Name)
    *   [func (m ClientConnectionWaitTime) Record(ctx context.Context, val float64, clientConnectionPoolName string, ...)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionWaitTime.Record)
    *   [func (ClientConnectionWaitTime) Unit() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionWaitTime.Unit)

*   [type ClientConnectionsStateAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionsStateAttr)
*   [type ClientOperationDuration](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientOperationDuration)
*       *   [func NewClientOperationDuration(m metric.Meter, opt ...metric.Float64HistogramOption) (ClientOperationDuration, error)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#NewClientOperationDuration)

*       *   [func (ClientOperationDuration) AttrCollectionName(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientOperationDuration.AttrCollectionName)
    *   [func (ClientOperationDuration) AttrErrorType(val ErrorTypeAttr) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientOperationDuration.AttrErrorType)
    *   [func (ClientOperationDuration) AttrNamespace(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientOperationDuration.AttrNamespace)
    *   [func (ClientOperationDuration) AttrNetworkPeerAddress(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientOperationDuration.AttrNetworkPeerAddress)
    *   [func (ClientOperationDuration) AttrNetworkPeerPort(val int) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientOperationDuration.AttrNetworkPeerPort)
    *   [func (ClientOperationDuration) AttrOperationName(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientOperationDuration.AttrOperationName)
    *   [func (ClientOperationDuration) AttrQuerySummary(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientOperationDuration.AttrQuerySummary)
    *   [func (ClientOperationDuration) AttrQueryText(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientOperationDuration.AttrQueryText)
    *   [func (ClientOperationDuration) AttrResponseStatusCode(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientOperationDuration.AttrResponseStatusCode)
    *   [func (ClientOperationDuration) AttrServerAddress(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientOperationDuration.AttrServerAddress)
    *   [func (ClientOperationDuration) AttrServerPort(val int) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientOperationDuration.AttrServerPort)
    *   [func (ClientOperationDuration) AttrStoredProcedureName(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientOperationDuration.AttrStoredProcedureName)
    *   [func (ClientOperationDuration) Description() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientOperationDuration.Description)
    *   [func (m ClientOperationDuration) Inst() metric.Float64Histogram](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientOperationDuration.Inst)
    *   [func (ClientOperationDuration) Name() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientOperationDuration.Name)
    *   [func (m ClientOperationDuration) Record(ctx context.Context, val float64, systemName SystemNameAttr, ...)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientOperationDuration.Record)
    *   [func (ClientOperationDuration) Unit() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientOperationDuration.Unit)

*   [type ClientResponseReturnedRows](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientResponseReturnedRows)
*       *   [func NewClientResponseReturnedRows(m metric.Meter, opt ...metric.Int64HistogramOption) (ClientResponseReturnedRows, error)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#NewClientResponseReturnedRows)

*       *   [func (ClientResponseReturnedRows) AttrCollectionName(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientResponseReturnedRows.AttrCollectionName)
    *   [func (ClientResponseReturnedRows) AttrErrorType(val ErrorTypeAttr) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientResponseReturnedRows.AttrErrorType)
    *   [func (ClientResponseReturnedRows) AttrNamespace(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientResponseReturnedRows.AttrNamespace)
    *   [func (ClientResponseReturnedRows) AttrNetworkPeerAddress(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientResponseReturnedRows.AttrNetworkPeerAddress)
    *   [func (ClientResponseReturnedRows) AttrNetworkPeerPort(val int) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientResponseReturnedRows.AttrNetworkPeerPort)
    *   [func (ClientResponseReturnedRows) AttrOperationName(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientResponseReturnedRows.AttrOperationName)
    *   [func (ClientResponseReturnedRows) AttrQuerySummary(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientResponseReturnedRows.AttrQuerySummary)
    *   [func (ClientResponseReturnedRows) AttrQueryText(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientResponseReturnedRows.AttrQueryText)
    *   [func (ClientResponseReturnedRows) AttrResponseStatusCode(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientResponseReturnedRows.AttrResponseStatusCode)
    *   [func (ClientResponseReturnedRows) AttrServerAddress(val string) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientResponseReturnedRows.AttrServerAddress)
    *   [func (ClientResponseReturnedRows) AttrServerPort(val int) attribute.KeyValue](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientResponseReturnedRows.AttrServerPort)
    *   [func (ClientResponseReturnedRows) Description() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientResponseReturnedRows.Description)
    *   [func (m ClientResponseReturnedRows) Inst() metric.Int64Histogram](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientResponseReturnedRows.Inst)
    *   [func (ClientResponseReturnedRows) Name() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientResponseReturnedRows.Name)
    *   [func (m ClientResponseReturnedRows) Record(ctx context.Context, val int64, systemName SystemNameAttr, ...)](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientResponseReturnedRows.Record)
    *   [func (ClientResponseReturnedRows) Unit() string](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientResponseReturnedRows.Unit)

*   [type CosmosDBConsistencyLevelAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#CosmosDBConsistencyLevelAttr)
*   [type ErrorTypeAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ErrorTypeAttr)
*   [type SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr)

This section is empty.

This section is empty.

This section is empty.

ClientConnectionCount is an instrument used to record metric values conforming to the "db.client.connection.count" semantic conventions. It represents the number of connections that are currently in state described by the `state` attribute.

NewClientConnectionCount returns a new ClientConnectionCount instrument.

Add adds incr to the existing count.

The clientConnectionPoolName is the the name of the connection pool; unique within the instrumented application. In case the connection pool implementation doesn't provide a name, instrumentation SHOULD use a combination of parameters that would make the name unique, for example, combining attributes `server.address`, `server.port`, and `db.namespace`, formatted as `server.address:server.port/db.namespace`. Instrumentations that generate connection pool name following different patterns SHOULD document it.

The clientConnectionState is the the state of a connection in the pool

Description returns the semantic convention description of the instrument

Inst returns the underlying metric instrument.

Name returns the semantic convention name of the instrument.

Unit returns the semantic convention unit of the instrument

ClientConnectionCreateTime is an instrument used to record metric values conforming to the "db.client.connection.create_time" semantic conventions. It represents the time it took to create a new connection.

NewClientConnectionCreateTime returns a new ClientConnectionCreateTime instrument.

Description returns the semantic convention description of the instrument

Inst returns the underlying metric instrument.

Name returns the semantic convention name of the instrument.

Record records val to the current distribution.

The clientConnectionPoolName is the the name of the connection pool; unique within the instrumented application. In case the connection pool implementation doesn't provide a name, instrumentation SHOULD use a combination of parameters that would make the name unique, for example, combining attributes `server.address`, `server.port`, and `db.namespace`, formatted as `server.address:server.port/db.namespace`. Instrumentations that generate connection pool name following different patterns SHOULD document it.

Unit returns the semantic convention unit of the instrument

ClientConnectionIdleMax is an instrument used to record metric values conforming to the "db.client.connection.idle.max" semantic conventions. It represents the maximum number of idle open connections allowed.

NewClientConnectionIdleMax returns a new ClientConnectionIdleMax instrument.

Add adds incr to the existing count.

The clientConnectionPoolName is the the name of the connection pool; unique within the instrumented application. In case the connection pool implementation doesn't provide a name, instrumentation SHOULD use a combination of parameters that would make the name unique, for example, combining attributes `server.address`, `server.port`, and `db.namespace`, formatted as `server.address:server.port/db.namespace`. Instrumentations that generate connection pool name following different patterns SHOULD document it.

Description returns the semantic convention description of the instrument

Inst returns the underlying metric instrument.

Name returns the semantic convention name of the instrument.

Unit returns the semantic convention unit of the instrument

ClientConnectionIdleMin is an instrument used to record metric values conforming to the "db.client.connection.idle.min" semantic conventions. It represents the minimum number of idle open connections allowed.

NewClientConnectionIdleMin returns a new ClientConnectionIdleMin instrument.

Add adds incr to the existing count.

The clientConnectionPoolName is the the name of the connection pool; unique within the instrumented application. In case the connection pool implementation doesn't provide a name, instrumentation SHOULD use a combination of parameters that would make the name unique, for example, combining attributes `server.address`, `server.port`, and `db.namespace`, formatted as `server.address:server.port/db.namespace`. Instrumentations that generate connection pool name following different patterns SHOULD document it.

Description returns the semantic convention description of the instrument

Inst returns the underlying metric instrument.

Name returns the semantic convention name of the instrument.

Unit returns the semantic convention unit of the instrument

ClientConnectionMax is an instrument used to record metric values conforming to the "db.client.connection.max" semantic conventions. It represents the maximum number of open connections allowed.

NewClientConnectionMax returns a new ClientConnectionMax instrument.

Add adds incr to the existing count.

The clientConnectionPoolName is the the name of the connection pool; unique within the instrumented application. In case the connection pool implementation doesn't provide a name, instrumentation SHOULD use a combination of parameters that would make the name unique, for example, combining attributes `server.address`, `server.port`, and `db.namespace`, formatted as `server.address:server.port/db.namespace`. Instrumentations that generate connection pool name following different patterns SHOULD document it.

Description returns the semantic convention description of the instrument

Inst returns the underlying metric instrument.

Name returns the semantic convention name of the instrument.

Unit returns the semantic convention unit of the instrument

ClientConnectionPendingRequests is an instrument used to record metric values conforming to the "db.client.connection.pending_requests" semantic conventions. It represents the number of current pending requests for an open connection.

NewClientConnectionPendingRequests returns a new ClientConnectionPendingRequests instrument.

Add adds incr to the existing count.

The clientConnectionPoolName is the the name of the connection pool; unique within the instrumented application. In case the connection pool implementation doesn't provide a name, instrumentation SHOULD use a combination of parameters that would make the name unique, for example, combining attributes `server.address`, `server.port`, and `db.namespace`, formatted as `server.address:server.port/db.namespace`. Instrumentations that generate connection pool name following different patterns SHOULD document it.

Description returns the semantic convention description of the instrument

Inst returns the underlying metric instrument.

Name returns the semantic convention name of the instrument.

Unit returns the semantic convention unit of the instrument

type ClientConnectionStateAttr [string](https://pkg.go.dev/builtin#string)

ClientConnectionStateAttr is an attribute conforming to the db.client.connection.state semantic conventions. It represents the state of a connection in the pool.

var (
	ClientConnectionStateIdle [ClientConnectionStateAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionStateAttr) = "idle"
	ClientConnectionStateUsed [ClientConnectionStateAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionStateAttr) = "used"
)

ClientConnectionTimeouts is an instrument used to record metric values conforming to the "db.client.connection.timeouts" semantic conventions. It represents the number of connection timeouts that have occurred trying to obtain a connection from the pool.

NewClientConnectionTimeouts returns a new ClientConnectionTimeouts instrument.

Add adds incr to the existing count.

The clientConnectionPoolName is the the name of the connection pool; unique within the instrumented application. In case the connection pool implementation doesn't provide a name, instrumentation SHOULD use a combination of parameters that would make the name unique, for example, combining attributes `server.address`, `server.port`, and `db.namespace`, formatted as `server.address:server.port/db.namespace`. Instrumentations that generate connection pool name following different patterns SHOULD document it.

Description returns the semantic convention description of the instrument

Inst returns the underlying metric instrument.

Name returns the semantic convention name of the instrument.

Unit returns the semantic convention unit of the instrument

ClientConnectionUseTime is an instrument used to record metric values conforming to the "db.client.connection.use_time" semantic conventions. It represents the time between borrowing a connection and returning it to the pool.

NewClientConnectionUseTime returns a new ClientConnectionUseTime instrument.

Description returns the semantic convention description of the instrument

Inst returns the underlying metric instrument.

Name returns the semantic convention name of the instrument.

Record records val to the current distribution.

The clientConnectionPoolName is the the name of the connection pool; unique within the instrumented application. In case the connection pool implementation doesn't provide a name, instrumentation SHOULD use a combination of parameters that would make the name unique, for example, combining attributes `server.address`, `server.port`, and `db.namespace`, formatted as `server.address:server.port/db.namespace`. Instrumentations that generate connection pool name following different patterns SHOULD document it.

Unit returns the semantic convention unit of the instrument

ClientConnectionWaitTime is an instrument used to record metric values conforming to the "db.client.connection.wait_time" semantic conventions. It represents the time it took to obtain an open connection from the pool.

NewClientConnectionWaitTime returns a new ClientConnectionWaitTime instrument.

Description returns the semantic convention description of the instrument

Inst returns the underlying metric instrument.

Name returns the semantic convention name of the instrument.

Record records val to the current distribution.

The clientConnectionPoolName is the the name of the connection pool; unique within the instrumented application. In case the connection pool implementation doesn't provide a name, instrumentation SHOULD use a combination of parameters that would make the name unique, for example, combining attributes `server.address`, `server.port`, and `db.namespace`, formatted as `server.address:server.port/db.namespace`. Instrumentations that generate connection pool name following different patterns SHOULD document it.

Unit returns the semantic convention unit of the instrument

type ClientConnectionsStateAttr [string](https://pkg.go.dev/builtin#string)

ClientConnectionsStateAttr is an attribute conforming to the db.client.connections.state semantic conventions. It represents the deprecated, use `db.client.connection.state` instead.

var (
	ClientConnectionsStateIdle [ClientConnectionsStateAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionsStateAttr) = "idle"
	ClientConnectionsStateUsed [ClientConnectionsStateAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ClientConnectionsStateAttr) = "used"
)

ClientOperationDuration is an instrument used to record metric values conforming to the "db.client.operation.duration" semantic conventions. It represents the duration of database client operations.

NewClientOperationDuration returns a new ClientOperationDuration instrument.

AttrCollectionName returns an optional attribute for the "db.collection.name" semantic convention. It represents the name of a collection (table, container) within the database.

AttrErrorType returns an optional attribute for the "error.type" semantic convention. It represents the describes a class of error the operation ended with.

AttrNamespace returns an optional attribute for the "db.namespace" semantic convention. It represents the name of the database, fully qualified within the server address and port.

AttrNetworkPeerAddress returns an optional attribute for the "network.peer.address" semantic convention. It represents the peer address of the database node where the operation was performed.

AttrNetworkPeerPort returns an optional attribute for the "network.peer.port" semantic convention. It represents the peer port number of the network connection.

AttrOperationName returns an optional attribute for the "db.operation.name" semantic convention. It represents the name of the operation or command being executed.

AttrQuerySummary returns an optional attribute for the "db.query.summary" semantic convention. It represents the low cardinality summary of a database query.

AttrQueryText returns an optional attribute for the "db.query.text" semantic convention. It represents the database query being executed.

AttrResponseStatusCode returns an optional attribute for the "db.response.status_code" semantic convention. It represents the database response status code.

AttrServerAddress returns an optional attribute for the "server.address" semantic convention. It represents the name of the database host.

AttrServerPort returns an optional attribute for the "server.port" semantic convention. It represents the server port number.

AttrStoredProcedureName returns an optional attribute for the "db.stored_procedure.name" semantic convention. It represents the name of a stored procedure within the database.

Description returns the semantic convention description of the instrument

Inst returns the underlying metric instrument.

Name returns the semantic convention name of the instrument.

Record records val to the current distribution.

The systemName is the the database management system (DBMS) product as identified by the client instrumentation.

All additional attrs passed are included in the recorded value.

Batch operations SHOULD be recorded as a single operation.

Unit returns the semantic convention unit of the instrument

ClientResponseReturnedRows is an instrument used to record metric values conforming to the "db.client.response.returned_rows" semantic conventions. It represents the actual number of records returned by the database operation.

NewClientResponseReturnedRows returns a new ClientResponseReturnedRows instrument.

AttrCollectionName returns an optional attribute for the "db.collection.name" semantic convention. It represents the name of a collection (table, container) within the database.

AttrErrorType returns an optional attribute for the "error.type" semantic convention. It represents the describes a class of error the operation ended with.

AttrNamespace returns an optional attribute for the "db.namespace" semantic convention. It represents the name of the database, fully qualified within the server address and port.

AttrNetworkPeerAddress returns an optional attribute for the "network.peer.address" semantic convention. It represents the peer address of the database node where the operation was performed.

AttrNetworkPeerPort returns an optional attribute for the "network.peer.port" semantic convention. It represents the peer port number of the network connection.

AttrOperationName returns an optional attribute for the "db.operation.name" semantic convention. It represents the name of the operation or command being executed.

AttrQuerySummary returns an optional attribute for the "db.query.summary" semantic convention. It represents the low cardinality summary of a database query.

AttrQueryText returns an optional attribute for the "db.query.text" semantic convention. It represents the database query being executed.

AttrResponseStatusCode returns an optional attribute for the "db.response.status_code" semantic convention. It represents the database response status code.

AttrServerAddress returns an optional attribute for the "server.address" semantic convention. It represents the name of the database host.

AttrServerPort returns an optional attribute for the "server.port" semantic convention. It represents the server port number.

Description returns the semantic convention description of the instrument

Inst returns the underlying metric instrument.

Name returns the semantic convention name of the instrument.

Record records val to the current distribution.

The systemName is the the database management system (DBMS) product as identified by the client instrumentation.

All additional attrs passed are included in the recorded value.

Unit returns the semantic convention unit of the instrument

type CosmosDBConsistencyLevelAttr [string](https://pkg.go.dev/builtin#string)

CosmosDBConsistencyLevelAttr is an attribute conforming to the db.cosmosdb.consistency_level semantic conventions. It represents the deprecated, use `cosmosdb.consistency.level` instead.

var (
	CosmosDBConsistencyLevelStrong [CosmosDBConsistencyLevelAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#CosmosDBConsistencyLevelAttr) = "Strong"
	CosmosDBConsistencyLevelBoundedStaleness [CosmosDBConsistencyLevelAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#CosmosDBConsistencyLevelAttr) = "BoundedStaleness"
	CosmosDBConsistencyLevelSession [CosmosDBConsistencyLevelAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#CosmosDBConsistencyLevelAttr) = "Session"
	CosmosDBConsistencyLevelEventual [CosmosDBConsistencyLevelAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#CosmosDBConsistencyLevelAttr) = "Eventual"
	CosmosDBConsistencyLevelConsistentPrefix [CosmosDBConsistencyLevelAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#CosmosDBConsistencyLevelAttr) = "ConsistentPrefix"
)

ErrorTypeAttr is an attribute conforming to the error.type semantic conventions. It represents the describes a class of error the operation ended with.

var (
	
	ErrorTypeOther [ErrorTypeAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#ErrorTypeAttr) = "_OTHER"
)

SystemNameAttr is an attribute conforming to the db.system.name semantic conventions. It represents the database management system (DBMS) product as identified by the client instrumentation.

var (
	SystemNameOtherSQL [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "other_sql"
	
	
	SystemNameSoftwareagAdabas [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "softwareag.adabas"
	
	
	SystemNameActianIngres [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "actian.ingres"
	
	
	SystemNameAWSDynamoDB [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "aws.dynamodb"
	
	
	SystemNameAWSRedshift [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "aws.redshift"
	
	
	SystemNameAzureCosmosDB [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "azure.cosmosdb"
	
	
	SystemNameIntersystemsCache [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "intersystems.cache"
	
	
	SystemNameCassandra [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "cassandra"
	
	
	SystemNameClickHouse [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "clickhouse"
	
	
	SystemNameCockroachDB [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "cockroachdb"
	
	
	SystemNameCouchbase [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "couchbase"
	
	
	SystemNameCouchDB [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "couchdb"
	
	
	SystemNameDerby [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "derby"
	
	
	SystemNameElasticsearch [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "elasticsearch"
	
	
	SystemNameFirebirdSQL [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "firebirdsql"
	
	
	SystemNameGCPSpanner [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "gcp.spanner"
	
	
	SystemNameGeode [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "geode"
	
	
	SystemNameH2database [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "h2database"
	
	
	SystemNameHBase [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "hbase"
	
	
	SystemNameHive [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "hive"
	
	
	SystemNameHSQLDB [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "hsqldb"
	
	
	SystemNameIBMDB2 [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "ibm.db2"
	
	
	SystemNameIBMInformix [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "ibm.informix"
	
	
	SystemNameIBMNetezza [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "ibm.netezza"
	
	
	SystemNameInfluxDB [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "influxdb"
	
	
	SystemNameInstantDB [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "instantdb"
	
	
	SystemNameMariaDB [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "mariadb"
	
	
	SystemNameMemcached [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "memcached"
	
	
	SystemNameMongoDB [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "mongodb"
	
	
	SystemNameMicrosoftSQLServer [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "microsoft.sql_server"
	
	
	SystemNameMySQL [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "mysql"
	
	
	SystemNameNeo4j [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "neo4j"
	
	
	SystemNameOpenSearch [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "opensearch"
	
	
	SystemNameOracleDB [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "oracle.db"
	
	
	SystemNamePostgreSQL [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "postgresql"
	
	
	SystemNameRedis [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "redis"
	
	
	SystemNameSAPHANA [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "sap.hana"
	
	
	SystemNameSAPMaxDB [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "sap.maxdb"
	
	
	SystemNameSQLite [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "sqlite"
	
	
	SystemNameTeradata [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "teradata"
	
	
	SystemNameTrino [SystemNameAttr](https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.34.0/dbconv#SystemNameAttr) = "trino"
)
