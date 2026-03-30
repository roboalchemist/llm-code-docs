# Source: https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr

Title: otellogr package - go.opentelemetry.io/contrib/bridges/otellogr - Go Packages

URL Source: https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr

Markdown Content:
Package otellogr provides a [LogSink](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#LogSink), a [logr.LogSink](https://pkg.go.dev/github.com/go-logr/logr#LogSink) implementation that can be used to bridge between the [logr](https://pkg.go.dev/github.com/go-logr/logr) API and [OpenTelemetry](https://opentelemetry.io/docs/concepts/signals/logs/).

#### Record Conversion [¶](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#hdr-Record_Conversion "Go to Record Conversion")

The logr records are converted to OpenTelemetry [log.Record](https://pkg.go.dev/go.opentelemetry.io/otel/log#Record) in the following way:

*   Message is set as the Body using a [log.StringValue](https://pkg.go.dev/go.opentelemetry.io/otel/log#StringValue).
*   Level is transformed and set as the Severity. The SeverityText is not set.
*   KeyAndValues are transformed and set as Attributes.
*   Error is always logged as an additional attribute with the key "exception.message" and with the severity [log.SeverityError](https://pkg.go.dev/go.opentelemetry.io/otel/log#SeverityError).
*   The [context.Context](https://pkg.go.dev/context#Context) value in KeyAndValues is propagated to OpenTelemetry log record. All non-nested [context.Context](https://pkg.go.dev/context#Context) values are ignored and not added as attributes. If there are multiple [context.Context](https://pkg.go.dev/context#Context) the last one is used.

The V-level is transformed by using the [WithLevelSeverity](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#WithLevelSeverity) option. If option is not provided then V-level is transformed in the following way:

*   logr.Info and logr.V(0) are transformed to [log.SeverityInfo](https://pkg.go.dev/go.opentelemetry.io/otel/log#SeverityInfo).
*   logr.V(1) is transformed to [log.SeverityDebug](https://pkg.go.dev/go.opentelemetry.io/otel/log#SeverityDebug).
*   logr.V(2) and higher are transformed to [log.SeverityTrace](https://pkg.go.dev/go.opentelemetry.io/otel/log#SeverityTrace).

KeysAndValues values are transformed based on their type. The following types are supported:

*   [bool] are transformed to [log.BoolValue](https://pkg.go.dev/go.opentelemetry.io/otel/log#BoolValue).
*   [string] are transformed to [log.StringValue](https://pkg.go.dev/go.opentelemetry.io/otel/log#StringValue).
*   [int], [int8], [int16], [int32], [int64] are transformed to [log.Int64Value](https://pkg.go.dev/go.opentelemetry.io/otel/log#Int64Value).
*   [uint], [uint8], [uint16], [uint32], [uint64], [uintptr] are transformed to [log.Int64Value](https://pkg.go.dev/go.opentelemetry.io/otel/log#Int64Value) or [log.StringValue](https://pkg.go.dev/go.opentelemetry.io/otel/log#StringValue) if the value is too large.
*   [float32], [float64] are transformed to [log.Float64Value](https://pkg.go.dev/go.opentelemetry.io/otel/log#Float64Value).
*   [time.Duration](https://pkg.go.dev/time#Duration) are transformed to [log.Int64Value](https://pkg.go.dev/go.opentelemetry.io/otel/log#Int64Value) with the nanoseconds.
*   [complex64], [complex128] are transformed to [log.MapValue](https://pkg.go.dev/go.opentelemetry.io/otel/log#MapValue) with the keys "r" and "i" for the real and imaginary parts. The values are [log.Float64Value](https://pkg.go.dev/go.opentelemetry.io/otel/log#Float64Value).
*   [time.Time](https://pkg.go.dev/time#Time) are transformed to [log.Int64Value](https://pkg.go.dev/go.opentelemetry.io/otel/log#Int64Value) with the nanoseconds.
*   [[]byte] are transformed to [log.BytesValue](https://pkg.go.dev/go.opentelemetry.io/otel/log#BytesValue).
*   [error] are transformed to [log.StringValue](https://pkg.go.dev/go.opentelemetry.io/otel/log#StringValue) with the error message.
*   [nil] are transformed to an empty [log.Value](https://pkg.go.dev/go.opentelemetry.io/otel/log#Value).
*   [struct] are transformed to [log.StringValue](https://pkg.go.dev/go.opentelemetry.io/otel/log#StringValue) with the struct fields.
*   [slice], [array] are transformed to [log.SliceValue](https://pkg.go.dev/go.opentelemetry.io/otel/log#SliceValue) with the elements.
*   [map] are transformed to [log.MapValue](https://pkg.go.dev/go.opentelemetry.io/otel/log#MapValue) with the key-value pairs.
*   [pointer], [interface] are transformed to the dereferenced value.

package main

import (
	"github.com/go-logr/logr"
	"go.opentelemetry.io/otel/log"
	"go.opentelemetry.io/otel/log/noop"

	"go.opentelemetry.io/contrib/bridges/otellogr"
)

func main() {
	// Use a working LoggerProvider implementation instead e.g. using go.opentelemetry.io/otel/sdk/log.
	provider := noop.NewLoggerProvider()

	// Create an logr.Logger with *otellogr.LogSink and use it in your application.
	logr.New(otellogr.NewLogSink(
		"my/pkg/name",
		otellogr.WithLoggerProvider(provider),
		// Optionally, set the log level severity mapping.
		otellogr.WithLevelSeverity(func(level int) log.Severity {
			switch level {
			case 0:
				return log.SeverityInfo
			case 1:
				return log.SeverityDebug
			default:
				return log.SeverityTrace
			}
		}),
	))
}

*   [Constants](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#pkg-constants)
*   [type LogSink](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#LogSink)
*       *   [func NewLogSink(name string, options ...Option) *LogSink](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#NewLogSink)

*       *   [func (l *LogSink) Enabled(level int) bool](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#LogSink.Enabled)
    *   [func (l *LogSink) Error(err error, msg string, keysAndValues ...any)](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#LogSink.Error)
    *   [func (l *LogSink) Info(level int, msg string, keysAndValues ...any)](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#LogSink.Info)
    *   [func (*LogSink) Init(logr.RuntimeInfo)](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#LogSink.Init)
    *   [func (l LogSink) WithName(name string) logr.LogSink](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#LogSink.WithName)
    *   [func (l LogSink) WithValues(keysAndValues ...any) logr.LogSink](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#LogSink.WithValues)

*   [type Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#Option)
*       *   [func WithAttributes(attributes ...attribute.KeyValue) Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#WithAttributes)
    *   [func WithLevelSeverity(f func(int) log.Severity) Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#WithLevelSeverity)
    *   [func WithLoggerProvider(provider log.LoggerProvider) Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#WithLoggerProvider)
    *   [func WithSchemaURL(schemaURL string) Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#WithSchemaURL)
    *   [func WithVersion(version string) Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#WithVersion)

*   [Package](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#example-package)

Version is the current release version of the otellogr bridge.

This section is empty.

This section is empty.

type LogSink struct {
	
}

LogSink is a [logr.LogSink](https://pkg.go.dev/github.com/go-logr/logr#LogSink) that sends all logging records it receives to OpenTelemetry. See package documentation for how conversions are made.

func NewLogSink(name [string](https://pkg.go.dev/builtin#string), options ...[Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#Option)) *[LogSink](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#LogSink)

NewLogSink returns a new [LogSink](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#LogSink) to be used as a [logr.LogSink](https://pkg.go.dev/github.com/go-logr/logr#LogSink).

If [WithLoggerProvider](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#WithLoggerProvider) is not provided, the returned [LogSink](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#LogSink) will use the global LoggerProvider.

Enabled tests whether this LogSink is enabled at the specified V-level. For example, commandline flags might be used to set the logging verbosity and disable some info logs.

Error logs an error, with the given message and key/value pairs.

Info logs a non-error message with the given key/value pairs.

Init receives optional information about the logr library this implementation does not use it.

WithName returns a new LogSink with the specified name appended.

WithValues returns a new LogSink with additional key/value pairs.

type Option interface {
	
}

Option configures a [LogSink](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#LogSink).

WithAttributes returns an [Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#Option) that configures the instrumentation scope attributes of the [log.Logger](https://pkg.go.dev/go.opentelemetry.io/otel/log#Logger) used by a [LogSink](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#LogSink).

WithLevelSeverity returns an [Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#Option) that configures the function used to convert logr levels to OpenTelemetry log severities.

By default if this Option is not provided, the LogSink will use a default conversion function that transforms in the following way:

*   logr.Info and logr.V(0) are transformed to [log.SeverityInfo](https://pkg.go.dev/go.opentelemetry.io/otel/log#SeverityInfo).
*   logr.V(1) is transformed to [log.SeverityDebug](https://pkg.go.dev/go.opentelemetry.io/otel/log#SeverityDebug).
*   logr.V(2) and higher are transformed to [log.SeverityTrace](https://pkg.go.dev/go.opentelemetry.io/otel/log#SeverityTrace).

WithLoggerProvider returns an [Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#Option) that configures [log.LoggerProvider](https://pkg.go.dev/go.opentelemetry.io/otel/log#LoggerProvider) used by a [LogSink](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#LogSink) to create its [log.Logger](https://pkg.go.dev/go.opentelemetry.io/otel/log#Logger).

By default if this Option is not provided, the LogSink will use the global LoggerProvider.

func WithSchemaURL(schemaURL [string](https://pkg.go.dev/builtin#string)) [Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#Option)

WithSchemaURL returns an [Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#Option) that configures the semantic convention schema URL of the [log.Logger](https://pkg.go.dev/go.opentelemetry.io/otel/log#Logger) used by a [LogSink](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#LogSink). The schemaURL should be the schema URL for the semantic conventions used in log records.

func WithVersion(version [string](https://pkg.go.dev/builtin#string)) [Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#Option)

WithVersion returns an [Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#Option) that configures the version of the [log.Logger](https://pkg.go.dev/go.opentelemetry.io/otel/log#Logger) used by a [LogSink](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otellogr#LogSink). The version should be the version of the package that is being logged.
