# Source: https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog

Title: otelslog package - go.opentelemetry.io/contrib/bridges/otelslog - Go Packages

URL Source: https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog

Markdown Content:
Package otelslog provides [Handler](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Handler), an [slog.Handler](https://pkg.go.dev/log/slog#Handler) implementation, that can be used to bridge between the [log/slog](https://pkg.go.dev/log/slog) API and [OpenTelemetry](https://opentelemetry.io/docs/concepts/signals/logs/).

#### Record Conversion [¶](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#hdr-Record_Conversion "Go to Record Conversion")

The [slog.Record](https://pkg.go.dev/log/slog#Record) are converted to OpenTelemetry [log.Record](https://pkg.go.dev/go.opentelemetry.io/otel/log#Record) in the following way:

*   Time is set as the Timestamp.
*   Message is set as the Body using a [log.StringValue](https://pkg.go.dev/go.opentelemetry.io/otel/log#StringValue).
*   Level is transformed and set as the Severity. The SeverityText is also set.
*   PC is dropped.
*   Attr are transformed and set as the Attributes.

The Level is transformed by using the static offset to the OpenTelemetry Severity types. For example:

*   [slog.LevelDebug](https://pkg.go.dev/log/slog#LevelDebug) is transformed to [log.SeverityDebug](https://pkg.go.dev/go.opentelemetry.io/otel/log#SeverityDebug)
*   [slog.LevelInfo](https://pkg.go.dev/log/slog#LevelInfo) is transformed to [log.SeverityInfo](https://pkg.go.dev/go.opentelemetry.io/otel/log#SeverityInfo)
*   [slog.LevelWarn](https://pkg.go.dev/log/slog#LevelWarn) is transformed to [log.SeverityWarn](https://pkg.go.dev/go.opentelemetry.io/otel/log#SeverityWarn)
*   [slog.LevelError](https://pkg.go.dev/log/slog#LevelError) is transformed to [log.SeverityError](https://pkg.go.dev/go.opentelemetry.io/otel/log#SeverityError)

Attribute values are transformed based on their [slog.Kind](https://pkg.go.dev/log/slog#Kind):

*   [slog.KindAny](https://pkg.go.dev/log/slog#KindAny) values are transformed based on their type or into a string value encoded using [fmt.Sprintf](https://pkg.go.dev/fmt#Sprintf) if there is no matching type.
*   [slog.KindBool](https://pkg.go.dev/log/slog#KindBool) are transformed to [log.BoolValue](https://pkg.go.dev/go.opentelemetry.io/otel/log#BoolValue) directly.
*   [slog.KindDuration](https://pkg.go.dev/log/slog#KindDuration) are transformed to [log.Int64Value](https://pkg.go.dev/go.opentelemetry.io/otel/log#Int64Value) as nanoseconds.
*   [slog.KindFloat64](https://pkg.go.dev/log/slog#KindFloat64) are transformed to [log.Float64Value](https://pkg.go.dev/go.opentelemetry.io/otel/log#Float64Value) directly.
*   [slog.KindInt64](https://pkg.go.dev/log/slog#KindInt64) are transformed to [log.Int64Value](https://pkg.go.dev/go.opentelemetry.io/otel/log#Int64Value) directly.
*   [slog.KindString](https://pkg.go.dev/log/slog#KindString) are transformed to [log.StringValue](https://pkg.go.dev/go.opentelemetry.io/otel/log#StringValue) directly.
*   [slog.KindTime](https://pkg.go.dev/log/slog#KindTime) are transformed to [log.Int64Value](https://pkg.go.dev/go.opentelemetry.io/otel/log#Int64Value) as nanoseconds since the Unix epoch.
*   [slog.KindUint64](https://pkg.go.dev/log/slog#KindUint64) are transformed to [log.Int64Value](https://pkg.go.dev/go.opentelemetry.io/otel/log#Int64Value) using int64 conversion.
*   [slog.KindGroup](https://pkg.go.dev/log/slog#KindGroup) are transformed to [log.MapValue](https://pkg.go.dev/go.opentelemetry.io/otel/log#MapValue) using appropriate transforms for each group value.
*   [slog.KindLogValuer](https://pkg.go.dev/log/slog#KindLogValuer) the value is resolved and then transformed.

package main

import (
	"go.opentelemetry.io/otel/log/noop"

	"go.opentelemetry.io/contrib/bridges/otelslog"
)

func main() {
	// Use a working LoggerProvider implementation instead e.g. using go.opentelemetry.io/otel/sdk/log.
	provider := noop.NewLoggerProvider()

	// Create an *slog.Logger and use it in your application.
	otelslog.NewLogger("my/pkg/name", otelslog.WithLoggerProvider(provider))
}

*   [Constants](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#pkg-constants)
*   [func NewLogger(name string, options ...Option) *slog.Logger](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#NewLogger)
*   [type Handler](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Handler)
*       *   [func NewHandler(name string, options ...Option) *Handler](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#NewHandler)

*       *   [func (h *Handler) Enabled(ctx context.Context, l slog.Level) bool](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Handler.Enabled)
    *   [func (h *Handler) Handle(ctx context.Context, record slog.Record) error](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Handler.Handle)
    *   [func (h *Handler) WithAttrs(attrs []slog.Attr) slog.Handler](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Handler.WithAttrs)
    *   [func (h *Handler) WithGroup(name string) slog.Handler](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Handler.WithGroup)

*   [type Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Option)
*       *   [func WithAttributes(attributes ...attribute.KeyValue) Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#WithAttributes)
    *   [func WithLoggerProvider(provider log.LoggerProvider) Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#WithLoggerProvider)
    *   [func WithSchemaURL(schemaURL string) Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#WithSchemaURL)
    *   [func WithSource(source bool) Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#WithSource)
    *   [func WithVersion(version string) Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#WithVersion)

*   [Package](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#example-package)

Version is the current release version of the otelslog bridge.

This section is empty.

NewLogger returns a new [slog.Logger](https://pkg.go.dev/log/slog#Logger) backed by a new [Handler](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Handler). See [NewHandler](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#NewHandler) for details on how the backing Handler is created.

#### type [Handler](https://github.com/open-telemetry/opentelemetry-go-contrib/blob/bridges/otelslog/v0.15.0/bridges/otelslog/handler.go#L162)[¶](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Handler "Go to Handler")

type Handler struct {
	
}

Handler is an [slog.Handler](https://pkg.go.dev/log/slog#Handler) that sends all logging records it receives to OpenTelemetry. See package documentation for how conversions are made.

#### func [NewHandler](https://github.com/open-telemetry/opentelemetry-go-contrib/blob/bridges/otelslog/v0.15.0/bridges/otelslog/handler.go#L184)[¶](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#NewHandler "Go to NewHandler")

func NewHandler(name [string](https://pkg.go.dev/builtin#string), options ...[Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Option)) *[Handler](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Handler)

NewHandler returns a new [Handler](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Handler) to be used as an [slog.Handler](https://pkg.go.dev/log/slog#Handler).

If [WithLoggerProvider](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#WithLoggerProvider) is not provided, the returned Handler will use the global LoggerProvider.

The provided name needs to uniquely identify the code being logged. This is most commonly the package name of the code. If name is empty, the [log.Logger](https://pkg.go.dev/go.opentelemetry.io/otel/log#Logger) implementation may override this value with a default.

#### func (*Handler) [Enabled](https://github.com/open-telemetry/opentelemetry-go-contrib/blob/bridges/otelslog/v0.15.0/bridges/otelslog/handler.go#L245)[¶](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Handler.Enabled "Go to Handler.Enabled")

Enabled returns true if the Handler is enabled to log for the provided context and Level. Otherwise, false is returned if it is not enabled.

#### func (*Handler) [Handle](https://github.com/open-telemetry/opentelemetry-go-contrib/blob/bridges/otelslog/v0.15.0/bridges/otelslog/handler.go#L193)[¶](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Handler.Handle "Go to Handler.Handle")

Handle handles the passed record.

#### func (*Handler) [WithAttrs](https://github.com/open-telemetry/opentelemetry-go-contrib/blob/bridges/otelslog/v0.15.0/bridges/otelslog/handler.go#L253)[¶](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Handler.WithAttrs "Go to Handler.WithAttrs")

WithAttrs returns a new [slog.Handler](https://pkg.go.dev/log/slog#Handler) based on h that will log using the passed attrs.

#### func (*Handler) [WithGroup](https://github.com/open-telemetry/opentelemetry-go-contrib/blob/bridges/otelslog/v0.15.0/bridges/otelslog/handler.go#L271)[¶](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Handler.WithGroup "Go to Handler.WithGroup")

WithGroup returns a new [slog.Handler](https://pkg.go.dev/log/slog#Handler) based on h that will log all messages and attributes within a group of the provided name.

type Option interface {
	
}

Option configures a [Handler](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Handler).

WithAttributes returns an [Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Option) that configures the instrumentation scope attributes of the [log.Logger](https://pkg.go.dev/go.opentelemetry.io/otel/log#Logger) used by a [Handler](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Handler).

WithLoggerProvider returns an [Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Option) that configures [log.LoggerProvider](https://pkg.go.dev/go.opentelemetry.io/otel/log#LoggerProvider) used by a [Handler](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Handler) to create its [log.Logger](https://pkg.go.dev/go.opentelemetry.io/otel/log#Logger).

By default if this Option is not provided, the Handler will use the global LoggerProvider.

func WithSchemaURL(schemaURL [string](https://pkg.go.dev/builtin#string)) [Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Option)

WithSchemaURL returns an [Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Option) that configures the semantic convention schema URL of the [log.Logger](https://pkg.go.dev/go.opentelemetry.io/otel/log#Logger) used by a [Handler](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Handler). The schemaURL should be the schema URL for the semantic conventions used in log records.

func WithSource(source [bool](https://pkg.go.dev/builtin#bool)) [Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Option)

WithSource returns an [Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Option) that configures the [Handler](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Handler) to include the source location of the log record in log attributes.

func WithVersion(version [string](https://pkg.go.dev/builtin#string)) [Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Option)

WithVersion returns an [Option](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Option) that configures the version of the [log.Logger](https://pkg.go.dev/go.opentelemetry.io/otel/log#Logger) used by a [Handler](https://pkg.go.dev/go.opentelemetry.io/contrib/bridges/otelslog#Handler). The version should be the version of the package that is being logged.
