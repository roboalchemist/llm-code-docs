# Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats

Title: stats package - google.golang.org/grpc/experimental/stats - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats

Markdown Content:
Package stats contains experimental metrics/stats API's.

*   [Variables](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#pkg-variables)
*   [type AsyncMetric](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#AsyncMetric)
*   [type AsyncMetricReporter](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#AsyncMetricReporter)
*   [type AsyncMetricReporterFunc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#AsyncMetricReporterFunc)
*       *   [func (f AsyncMetricReporterFunc) Report(r AsyncMetricsRecorder) error](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#AsyncMetricReporterFunc.Report)

*   [type AsyncMetricsRecorder](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#AsyncMetricsRecorder)
*   [type Float64CountHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Float64CountHandle)
*       *   [func RegisterFloat64Count(descriptor MetricDescriptor) *Float64CountHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#RegisterFloat64Count)

*       *   [func (h *Float64CountHandle) Descriptor() *MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Float64CountHandle.Descriptor)
    *   [func (h *Float64CountHandle) Record(recorder MetricsRecorder, incr float64, labels ...string)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Float64CountHandle.Record)

*   [type Float64HistoHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Float64HistoHandle)
*       *   [func RegisterFloat64Histo(descriptor MetricDescriptor) *Float64HistoHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#RegisterFloat64Histo)

*       *   [func (h *Float64HistoHandle) Descriptor() *MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Float64HistoHandle.Descriptor)
    *   [func (h *Float64HistoHandle) Record(recorder MetricsRecorder, incr float64, labels ...string)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Float64HistoHandle.Record)

*   [type Int64AsyncGaugeHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64AsyncGaugeHandle)
*       *   [func RegisterInt64AsyncGauge(descriptor MetricDescriptor) *Int64AsyncGaugeHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#RegisterInt64AsyncGauge)

*       *   [func (h *Int64AsyncGaugeHandle) Descriptor() *MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64AsyncGaugeHandle.Descriptor)
    *   [func (h *Int64AsyncGaugeHandle) Record(recorder AsyncMetricsRecorder, value int64, labels ...string)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64AsyncGaugeHandle.Record)

*   [type Int64CountHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64CountHandle)
*       *   [func RegisterInt64Count(descriptor MetricDescriptor) *Int64CountHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#RegisterInt64Count)

*       *   [func (h *Int64CountHandle) Descriptor() *MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64CountHandle.Descriptor)
    *   [func (h *Int64CountHandle) Record(recorder MetricsRecorder, incr int64, labels ...string)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64CountHandle.Record)

*   [type Int64GaugeHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64GaugeHandle)
*       *   [func RegisterInt64Gauge(descriptor MetricDescriptor) *Int64GaugeHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#RegisterInt64Gauge)

*       *   [func (h *Int64GaugeHandle) Descriptor() *MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64GaugeHandle.Descriptor)
    *   [func (h *Int64GaugeHandle) Record(recorder MetricsRecorder, incr int64, labels ...string)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64GaugeHandle.Record)

*   [type Int64HistoHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64HistoHandle)
*       *   [func RegisterInt64Histo(descriptor MetricDescriptor) *Int64HistoHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#RegisterInt64Histo)

*       *   [func (h *Int64HistoHandle) Descriptor() *MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64HistoHandle.Descriptor)
    *   [func (h *Int64HistoHandle) Record(recorder MetricsRecorder, incr int64, labels ...string)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64HistoHandle.Record)

*   [type Int64UpDownCountHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64UpDownCountHandle)
*       *   [func RegisterInt64UpDownCount(descriptor MetricDescriptor) *Int64UpDownCountHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#RegisterInt64UpDownCount)

*       *   [func (h *Int64UpDownCountHandle) Descriptor() *MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64UpDownCountHandle.Descriptor)
    *   [func (h *Int64UpDownCountHandle) Record(recorder MetricsRecorder, v int64, labels ...string)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64UpDownCountHandle.Record)

*   [type Metric](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Metric)
*   [type MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)
*       *   [func DescriptorForMetric(metricName string) *MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#DescriptorForMetric)

*   [type MetricType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricType)
*   [type Metrics](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Metrics)
*       *   [func NewMetrics(metrics ...Metric) *Metrics](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#NewMetrics)

*   [type MetricsRecorder](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricsRecorder)
*   [type UnimplementedMetricsRecorder](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#UnimplementedMetricsRecorder)
*       *   [func (UnimplementedMetricsRecorder) RecordFloat64Count(*Float64CountHandle, float64, ...string)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#UnimplementedMetricsRecorder.RecordFloat64Count)
    *   [func (UnimplementedMetricsRecorder) RecordFloat64Histo(*Float64HistoHandle, float64, ...string)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#UnimplementedMetricsRecorder.RecordFloat64Histo)
    *   [func (UnimplementedMetricsRecorder) RecordInt64Count(*Int64CountHandle, int64, ...string)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#UnimplementedMetricsRecorder.RecordInt64Count)
    *   [func (UnimplementedMetricsRecorder) RecordInt64Gauge(*Int64GaugeHandle, int64, ...string)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#UnimplementedMetricsRecorder.RecordInt64Gauge)
    *   [func (UnimplementedMetricsRecorder) RecordInt64Histo(*Int64HistoHandle, int64, ...string)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#UnimplementedMetricsRecorder.RecordInt64Histo)
    *   [func (UnimplementedMetricsRecorder) RecordInt64UpDownCount(*Int64UpDownCountHandle, int64, ...string)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#UnimplementedMetricsRecorder.RecordInt64UpDownCount)
    *   [func (UnimplementedMetricsRecorder) RegisterAsyncReporter(AsyncMetricReporter, ...AsyncMetric) func()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#UnimplementedMetricsRecorder.RegisterAsyncReporter)

This section is empty.

DefaultMetrics are the default metrics registered through global metrics registry. This is written to at initialization time only, and is read only after initialization.

This section is empty.

type AsyncMetric interface {
 Descriptor() *[MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)	
}

AsyncMetric is a marker interface for asynchronous metric types.

type AsyncMetricReporter interface {
	Report([AsyncMetricsRecorder](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#AsyncMetricsRecorder)) [error](https://pkg.go.dev/builtin#error)
}

AsyncMetricReporter is an interface for types that record metrics asynchronously for the set of descriptors they are registered with. The AsyncMetricsRecorder parameter is used to record values for these metrics.

Implementations must make unique recordings across all registered AsyncMetricReporters. Meaning, they should not report values for a metric with the same attributes as another AsyncMetricReporter will report.

Implementations must be concurrent-safe.

type AsyncMetricReporterFunc func([AsyncMetricsRecorder](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#AsyncMetricsRecorder)) [error](https://pkg.go.dev/builtin#error)

AsyncMetricReporterFunc is an adapter to allow the use of ordinary functions as AsyncMetricReporters.

Report calls f(r).

type AsyncMetricsRecorder interface {
	
	RecordInt64AsyncGauge(handle *[Int64AsyncGaugeHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64AsyncGaugeHandle), incr [int64](https://pkg.go.dev/builtin#int64), labels ...[string](https://pkg.go.dev/builtin#string))
}

AsyncMetricsRecorder records on asynchronous metrics derived from metric registry.

#### type [Float64CountHandle](https://github.com/grpc/grpc-go/blob/v1.79.1/experimental/stats/metricregistry.go#L117)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Float64CountHandle "Go to Float64CountHandle")

type Float64CountHandle [MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)

Float64CountHandle is a typed handle for a float count metric. This handle is passed at the recording point in order to know which metric to record on.

func RegisterFloat64Count(descriptor [MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)) *[Float64CountHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Float64CountHandle)

RegisterFloat64Count registers the metric description onto the global registry. It returns a typed handle to use to recording data.

NOTE: this function must only be called during initialization time (i.e. in an init() function), and is not thread-safe. If multiple metrics are registered with the same name, this function will panic.

#### func (*Float64CountHandle) [Descriptor](https://github.com/grpc/grpc-go/blob/v1.79.1/experimental/stats/metricregistry.go#L121)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Float64CountHandle.Descriptor "Go to Float64CountHandle.Descriptor")

func (h *[Float64CountHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Float64CountHandle)) Descriptor() *[MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)

Descriptor returns the float64 count handle typecast to a pointer to a MetricDescriptor.

#### func (*Float64CountHandle) [Record](https://github.com/grpc/grpc-go/blob/v1.79.1/experimental/stats/metricregistry.go#L126)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Float64CountHandle.Record "Go to Float64CountHandle.Record")

Record records the float64 count value on the metrics recorder provided.

#### type [Float64HistoHandle](https://github.com/grpc/grpc-go/blob/v1.79.1/experimental/stats/metricregistry.go#L148)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Float64HistoHandle "Go to Float64HistoHandle")

type Float64HistoHandle [MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)

Float64HistoHandle is a typed handle for a float histogram metric. This handle is passed at the recording point in order to know which metric to record on.

func RegisterFloat64Histo(descriptor [MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)) *[Float64HistoHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Float64HistoHandle)

RegisterFloat64Histo registers the metric description onto the global registry. It returns a typed handle to use to recording data.

NOTE: this function must only be called during initialization time (i.e. in an init() function), and is not thread-safe. If multiple metrics are registered with the same name, this function will panic.

#### func (*Float64HistoHandle) [Descriptor](https://github.com/grpc/grpc-go/blob/v1.79.1/experimental/stats/metricregistry.go#L152)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Float64HistoHandle.Descriptor "Go to Float64HistoHandle.Descriptor")

func (h *[Float64HistoHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Float64HistoHandle)) Descriptor() *[MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)

Descriptor returns the float64 histo handle typecast to a pointer to a MetricDescriptor.

#### func (*Float64HistoHandle) [Record](https://github.com/grpc/grpc-go/blob/v1.79.1/experimental/stats/metricregistry.go#L157)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Float64HistoHandle.Record "Go to Float64HistoHandle.Record")

Record records the float64 histo value on the metrics recorder provided.

#### type [Int64AsyncGaugeHandle](https://github.com/grpc/grpc-go/blob/v1.79.1/experimental/stats/metricregistry.go#L184)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64AsyncGaugeHandle "Go to Int64AsyncGaugeHandle")added in v1.78.0

type Int64AsyncGaugeHandle [MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)

Int64AsyncGaugeHandle is a typed handle for an int gauge metric. This handle is passed at the recording point in order to know which metric to record on.

func RegisterInt64AsyncGauge(descriptor [MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)) *[Int64AsyncGaugeHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64AsyncGaugeHandle)

RegisterInt64AsyncGauge registers the metric description onto the global registry. It returns a typed handle to use for recording data.

NOTE: this function must only be called during initialization time (i.e. in an init() function), and is not thread-safe. If multiple metrics are registered with the same name, this function will panic.

#### func (*Int64AsyncGaugeHandle) [Descriptor](https://github.com/grpc/grpc-go/blob/v1.79.1/experimental/stats/metricregistry.go#L191)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64AsyncGaugeHandle.Descriptor "Go to Int64AsyncGaugeHandle.Descriptor")added in v1.78.0

func (h *[Int64AsyncGaugeHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64AsyncGaugeHandle)) Descriptor() *[MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)

Descriptor returns the int64 gauge handle typecast to a pointer to a MetricDescriptor.

#### func (*Int64AsyncGaugeHandle) [Record](https://github.com/grpc/grpc-go/blob/v1.79.1/experimental/stats/metricregistry.go#L196)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64AsyncGaugeHandle.Record "Go to Int64AsyncGaugeHandle.Record")added in v1.78.0

Record records the int64 gauge value on the metrics recorder provided.

#### type [Int64CountHandle](https://github.com/grpc/grpc-go/blob/v1.79.1/experimental/stats/metricregistry.go#L85)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64CountHandle "Go to Int64CountHandle")

type Int64CountHandle [MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)

Int64CountHandle is a typed handle for a int count metric. This handle is passed at the recording point in order to know which metric to record on.

func RegisterInt64Count(descriptor [MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)) *[Int64CountHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64CountHandle)

RegisterInt64Count registers the metric description onto the global registry. It returns a typed handle to use to recording data.

NOTE: this function must only be called during initialization time (i.e. in an init() function), and is not thread-safe. If multiple metrics are registered with the same name, this function will panic.

#### func (*Int64CountHandle) [Descriptor](https://github.com/grpc/grpc-go/blob/v1.79.1/experimental/stats/metricregistry.go#L89)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64CountHandle.Descriptor "Go to Int64CountHandle.Descriptor")

func (h *[Int64CountHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64CountHandle)) Descriptor() *[MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)

Descriptor returns the int64 count handle typecast to a pointer to a MetricDescriptor.

#### func (*Int64CountHandle) [Record](https://github.com/grpc/grpc-go/blob/v1.79.1/experimental/stats/metricregistry.go#L94)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64CountHandle.Record "Go to Int64CountHandle.Record")

Record records the int64 count value on the metrics recorder provided.

#### type [Int64GaugeHandle](https://github.com/grpc/grpc-go/blob/v1.79.1/experimental/stats/metricregistry.go#L163)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64GaugeHandle "Go to Int64GaugeHandle")

type Int64GaugeHandle [MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)

Int64GaugeHandle is a typed handle for an int gauge metric. This handle is passed at the recording point in order to know which metric to record on.

func RegisterInt64Gauge(descriptor [MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)) *[Int64GaugeHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64GaugeHandle)

RegisterInt64Gauge registers the metric description onto the global registry. It returns a typed handle to use to recording data.

NOTE: this function must only be called during initialization time (i.e. in an init() function), and is not thread-safe. If multiple metrics are registered with the same name, this function will panic.

#### func (*Int64GaugeHandle) [Descriptor](https://github.com/grpc/grpc-go/blob/v1.79.1/experimental/stats/metricregistry.go#L167)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64GaugeHandle.Descriptor "Go to Int64GaugeHandle.Descriptor")

func (h *[Int64GaugeHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64GaugeHandle)) Descriptor() *[MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)

Descriptor returns the int64 gauge handle typecast to a pointer to a MetricDescriptor.

#### func (*Int64GaugeHandle) [Record](https://github.com/grpc/grpc-go/blob/v1.79.1/experimental/stats/metricregistry.go#L172)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64GaugeHandle.Record "Go to Int64GaugeHandle.Record")

Record records the int64 histo value on the metrics recorder provided.

#### type [Int64HistoHandle](https://github.com/grpc/grpc-go/blob/v1.79.1/experimental/stats/metricregistry.go#L132)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64HistoHandle "Go to Int64HistoHandle")

type Int64HistoHandle [MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)

Int64HistoHandle is a typed handle for an int histogram metric. This handle is passed at the recording point in order to know which metric to record on.

func RegisterInt64Histo(descriptor [MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)) *[Int64HistoHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64HistoHandle)

RegisterInt64Histo registers the metric description onto the global registry. It returns a typed handle to use to recording data.

NOTE: this function must only be called during initialization time (i.e. in an init() function), and is not thread-safe. If multiple metrics are registered with the same name, this function will panic.

#### func (*Int64HistoHandle) [Descriptor](https://github.com/grpc/grpc-go/blob/v1.79.1/experimental/stats/metricregistry.go#L136)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64HistoHandle.Descriptor "Go to Int64HistoHandle.Descriptor")

func (h *[Int64HistoHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64HistoHandle)) Descriptor() *[MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)

Descriptor returns the int64 histo handle typecast to a pointer to a MetricDescriptor.

#### func (*Int64HistoHandle) [Record](https://github.com/grpc/grpc-go/blob/v1.79.1/experimental/stats/metricregistry.go#L141)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64HistoHandle.Record "Go to Int64HistoHandle.Record")

Record records the int64 histo value on the metrics recorder provided.

#### type [Int64UpDownCountHandle](https://github.com/grpc/grpc-go/blob/v1.79.1/experimental/stats/metricregistry.go#L101)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64UpDownCountHandle "Go to Int64UpDownCountHandle")added in v1.77.0

type Int64UpDownCountHandle [MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)

Int64UpDownCountHandle is a typed handle for an int up-down counter metric. This handle is passed at the recording point in order to know which metric to record on.

func RegisterInt64UpDownCount(descriptor [MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)) *[Int64UpDownCountHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64UpDownCountHandle)

RegisterInt64UpDownCount registers the metric description onto the global registry. It returns a typed handle to use for recording data.

NOTE: this function must only be called during initialization time (i.e. in an init() function), and is not thread-safe. If multiple metrics are registered with the same name, this function will panic.

#### func (*Int64UpDownCountHandle) [Descriptor](https://github.com/grpc/grpc-go/blob/v1.79.1/experimental/stats/metricregistry.go#L105)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64UpDownCountHandle.Descriptor "Go to Int64UpDownCountHandle.Descriptor")added in v1.77.0

func (h *[Int64UpDownCountHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64UpDownCountHandle)) Descriptor() *[MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)

Descriptor returns the int64 up-down counter handle typecast to a pointer to a MetricDescriptor.

#### func (*Int64UpDownCountHandle) [Record](https://github.com/grpc/grpc-go/blob/v1.79.1/experimental/stats/metricregistry.go#L111)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64UpDownCountHandle.Record "Go to Int64UpDownCountHandle.Record")added in v1.77.0

Record records the int64 up-down counter value on the metrics recorder provided. The value 'v' can be positive to increment or negative to decrement.

Metric was replaced by direct usage of strings.

MetricDescriptor is the data for a registered metric.

func DescriptorForMetric(metricName [string](https://pkg.go.dev/builtin#string)) *[MetricDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricDescriptor)

DescriptorForMetric returns the MetricDescriptor from the global registry.

Returns nil if MetricDescriptor not present.

MetricType is the type of metric.

const (
 MetricTypeIntCount [MetricType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#MetricType) = [iota](https://pkg.go.dev/builtin#iota) MetricTypeFloatCount  MetricTypeIntHisto  MetricTypeFloatHisto  MetricTypeIntGauge  MetricTypeIntUpDownCount  MetricTypeIntAsyncGauge )

Type of metric supported by this instrument registry.

Metrics is an experimental legacy alias of the now-stable stats.MetricSet. Metrics will be deleted in a future release.

func NewMetrics(metrics ...[Metric](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Metric)) *[Metrics](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Metrics)

NewMetrics is an experimental legacy alias of the now-stable stats.NewMetricSet. NewMetrics will be deleted in a future release.

type MetricsRecorder interface {
	
	RecordInt64Count(handle *[Int64CountHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64CountHandle), incr [int64](https://pkg.go.dev/builtin#int64), labels ...[string](https://pkg.go.dev/builtin#string))
	
	RecordFloat64Count(handle *[Float64CountHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Float64CountHandle), incr [float64](https://pkg.go.dev/builtin#float64), labels ...[string](https://pkg.go.dev/builtin#string))
	
	RecordInt64Histo(handle *[Int64HistoHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64HistoHandle), incr [int64](https://pkg.go.dev/builtin#int64), labels ...[string](https://pkg.go.dev/builtin#string))
	
	RecordFloat64Histo(handle *[Float64HistoHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Float64HistoHandle), incr [float64](https://pkg.go.dev/builtin#float64), labels ...[string](https://pkg.go.dev/builtin#string))
	
	RecordInt64Gauge(handle *[Int64GaugeHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64GaugeHandle), incr [int64](https://pkg.go.dev/builtin#int64), labels ...[string](https://pkg.go.dev/builtin#string))
	
	RecordInt64UpDownCount(handle *[Int64UpDownCountHandle](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#Int64UpDownCountHandle), incr [int64](https://pkg.go.dev/builtin#int64), labels ...[string](https://pkg.go.dev/builtin#string))
	
	
	
	RegisterAsyncReporter(reporter [AsyncMetricReporter](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#AsyncMetricReporter), descriptors ...[AsyncMetric](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#AsyncMetric)) func()

	
	
	
	[internal](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal).[EnforceMetricsRecorderEmbedding](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/internal#EnforceMetricsRecorderEmbedding)
}

MetricsRecorder records on metrics derived from metric registry. Implementors must embed UnimplementedMetricsRecorder.

UnimplementedMetricsRecorder must be embedded to have forward compatible implementations.

RecordFloat64Count provides a no-op implementation.

RecordFloat64Histo provides a no-op implementation.

RecordInt64Count provides a no-op implementation.

RecordInt64Gauge provides a no-op implementation.

RecordInt64Histo provides a no-op implementation.

RecordInt64UpDownCount provides a no-op implementation.

func ([UnimplementedMetricsRecorder](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#UnimplementedMetricsRecorder)) RegisterAsyncReporter([AsyncMetricReporter](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#AsyncMetricReporter), ...[AsyncMetric](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/experimental/stats#AsyncMetric)) func()

RegisterAsyncReporter provides a no-op implementation.
