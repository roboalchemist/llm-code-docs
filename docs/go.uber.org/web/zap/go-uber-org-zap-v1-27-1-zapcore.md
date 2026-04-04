# Source: https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore

Title: zapcore package - go.uber.org/zap/zapcore - Go Packages

URL Source: https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore

Markdown Content:
Package zapcore defines and implements the low-level interfaces upon which zap is built. By providing alternate implementations of these interfaces, external packages can extend zap's capabilities.

*   [Constants](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#pkg-constants)
*   [Variables](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#pkg-variables)
*   [func CapitalColorLevelEncoder(l Level, enc PrimitiveArrayEncoder)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CapitalColorLevelEncoder)
*   [func CapitalLevelEncoder(l Level, enc PrimitiveArrayEncoder)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CapitalLevelEncoder)
*   [func EpochMillisTimeEncoder(t time.Time, enc PrimitiveArrayEncoder)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#EpochMillisTimeEncoder)
*   [func EpochNanosTimeEncoder(t time.Time, enc PrimitiveArrayEncoder)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#EpochNanosTimeEncoder)
*   [func EpochTimeEncoder(t time.Time, enc PrimitiveArrayEncoder)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#EpochTimeEncoder)
*   [func FullCallerEncoder(caller EntryCaller, enc PrimitiveArrayEncoder)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#FullCallerEncoder)
*   [func FullNameEncoder(loggerName string, enc PrimitiveArrayEncoder)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#FullNameEncoder)
*   [func ISO8601TimeEncoder(t time.Time, enc PrimitiveArrayEncoder)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#ISO8601TimeEncoder)
*   [func LowercaseColorLevelEncoder(l Level, enc PrimitiveArrayEncoder)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#LowercaseColorLevelEncoder)
*   [func LowercaseLevelEncoder(l Level, enc PrimitiveArrayEncoder)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#LowercaseLevelEncoder)
*   [func MillisDurationEncoder(d time.Duration, enc PrimitiveArrayEncoder)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MillisDurationEncoder)
*   [func NanosDurationEncoder(d time.Duration, enc PrimitiveArrayEncoder)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#NanosDurationEncoder)
*   [func RFC3339NanoTimeEncoder(t time.Time, enc PrimitiveArrayEncoder)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#RFC3339NanoTimeEncoder)
*   [func RFC3339TimeEncoder(t time.Time, enc PrimitiveArrayEncoder)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#RFC3339TimeEncoder)
*   [func SecondsDurationEncoder(d time.Duration, enc PrimitiveArrayEncoder)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#SecondsDurationEncoder)
*   [func ShortCallerEncoder(caller EntryCaller, enc PrimitiveArrayEncoder)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#ShortCallerEncoder)
*   [func StringDurationEncoder(d time.Duration, enc PrimitiveArrayEncoder)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#StringDurationEncoder)
*   [type ArrayEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#ArrayEncoder)
*   [type ArrayMarshaler](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#ArrayMarshaler)
*   [type ArrayMarshalerFunc](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#ArrayMarshalerFunc)
*       *   [func (f ArrayMarshalerFunc) MarshalLogArray(enc ArrayEncoder) error](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#ArrayMarshalerFunc.MarshalLogArray)

*   [type BufferedWriteSyncer](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#BufferedWriteSyncer)
*       *   [func (s *BufferedWriteSyncer) Stop() (err error)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#BufferedWriteSyncer.Stop)
    *   [func (s *BufferedWriteSyncer) Sync() error](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#BufferedWriteSyncer.Sync)
    *   [func (s *BufferedWriteSyncer) Write(bs []byte) (int, error)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#BufferedWriteSyncer.Write)

*   [type CallerEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CallerEncoder)
*       *   [func (e *CallerEncoder) UnmarshalText(text []byte) error](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CallerEncoder.UnmarshalText)

*   [type CheckWriteAction](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckWriteAction)
*       *   [func (a CheckWriteAction) OnWrite(ce *CheckedEntry, _ []Field)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckWriteAction.OnWrite)

*   [type CheckWriteHook](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckWriteHook)
*   [type CheckedEntry](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckedEntry)
*       *   [func (ce *CheckedEntry) AddCore(ent Entry, core Core) *CheckedEntry](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckedEntry.AddCore)
    *   [func (ce *CheckedEntry) After(ent Entry, hook CheckWriteHook) *CheckedEntry](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckedEntry.After)
    *   [func (ce *CheckedEntry) Should(ent Entry, should CheckWriteAction) *CheckedEntry](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckedEntry.Should)deprecated
    *   [func (ce *CheckedEntry) Write(fields ...Field)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckedEntry.Write)

*   [type Clock](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Clock)
*   [type Core](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Core)
*       *   [func NewCore(enc Encoder, ws WriteSyncer, enab LevelEnabler) Core](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#NewCore)
    *   [func NewIncreaseLevelCore(core Core, level LevelEnabler) (Core, error)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#NewIncreaseLevelCore)
    *   [func NewLazyWith(core Core, fields []Field) Core](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#NewLazyWith)
    *   [func NewNopCore() Core](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#NewNopCore)
    *   [func NewSampler(core Core, tick time.Duration, first, thereafter int) Core](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#NewSampler)deprecated
    *   [func NewSamplerWithOptions(core Core, tick time.Duration, first, thereafter int, opts ...SamplerOption) Core](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#NewSamplerWithOptions)
    *   [func NewTee(cores ...Core) Core](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#NewTee)
    *   [func RegisterHooks(core Core, hooks ...func(Entry) error) Core](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#RegisterHooks)

*   [type DurationEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#DurationEncoder)
*       *   [func (e *DurationEncoder) UnmarshalText(text []byte) error](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#DurationEncoder.UnmarshalText)

*   [type Encoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Encoder)
*       *   [func NewConsoleEncoder(cfg EncoderConfig) Encoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#NewConsoleEncoder)
    *   [func NewJSONEncoder(cfg EncoderConfig) Encoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#NewJSONEncoder)

*   [type EncoderConfig](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#EncoderConfig)
*   [type Entry](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Entry)
*   [type EntryCaller](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#EntryCaller)
*       *   [func NewEntryCaller(pc uintptr, file string, line int, ok bool) EntryCaller](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#NewEntryCaller)

*       *   [func (ec EntryCaller) FullPath() string](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#EntryCaller.FullPath)
    *   [func (ec EntryCaller) String() string](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#EntryCaller.String)
    *   [func (ec EntryCaller) TrimmedPath() string](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#EntryCaller.TrimmedPath)

*   [type Field](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Field)
*       *   [func (f Field) AddTo(enc ObjectEncoder)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Field.AddTo)
    *   [func (f Field) Equals(other Field) bool](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Field.Equals)

*   [type FieldType](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#FieldType)
*   [type Level](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Level)
*       *   [func LevelOf(enab LevelEnabler) Level](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#LevelOf)
    *   [func ParseLevel(text string) (Level, error)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#ParseLevel)

*       *   [func (l Level) CapitalString() string](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Level.CapitalString)
    *   [func (l Level) Enabled(lvl Level) bool](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Level.Enabled)
    *   [func (l *Level) Get() interface{}](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Level.Get)
    *   [func (l Level) MarshalText() ([]byte, error)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Level.MarshalText)
    *   [func (l *Level) Set(s string) error](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Level.Set)
    *   [func (l Level) String() string](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Level.String)
    *   [func (l *Level) UnmarshalText(text []byte) error](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Level.UnmarshalText)

*   [type LevelEnabler](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#LevelEnabler)
*   [type LevelEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#LevelEncoder)
*       *   [func (e *LevelEncoder) UnmarshalText(text []byte) error](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#LevelEncoder.UnmarshalText)

*   [type MapObjectEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder)
*       *   [func NewMapObjectEncoder() *MapObjectEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#NewMapObjectEncoder)

*       *   [func (m *MapObjectEncoder) AddArray(key string, v ArrayMarshaler) error](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddArray)
    *   [func (m *MapObjectEncoder) AddBinary(k string, v []byte)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddBinary)
    *   [func (m *MapObjectEncoder) AddBool(k string, v bool)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddBool)
    *   [func (m *MapObjectEncoder) AddByteString(k string, v []byte)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddByteString)
    *   [func (m *MapObjectEncoder) AddComplex64(k string, v complex64)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddComplex64)
    *   [func (m *MapObjectEncoder) AddComplex128(k string, v complex128)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddComplex128)
    *   [func (m MapObjectEncoder) AddDuration(k string, v time.Duration)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddDuration)
    *   [func (m *MapObjectEncoder) AddFloat32(k string, v float32)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddFloat32)
    *   [func (m *MapObjectEncoder) AddFloat64(k string, v float64)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddFloat64)
    *   [func (m *MapObjectEncoder) AddInt(k string, v int)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddInt)
    *   [func (m *MapObjectEncoder) AddInt8(k string, v int8)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddInt8)
    *   [func (m *MapObjectEncoder) AddInt16(k string, v int16)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddInt16)
    *   [func (m *MapObjectEncoder) AddInt32(k string, v int32)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddInt32)
    *   [func (m *MapObjectEncoder) AddInt64(k string, v int64)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddInt64)
    *   [func (m *MapObjectEncoder) AddObject(k string, v ObjectMarshaler) error](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddObject)
    *   [func (m *MapObjectEncoder) AddReflected(k string, v interface{}) error](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddReflected)
    *   [func (m *MapObjectEncoder) AddString(k string, v string)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddString)
    *   [func (m MapObjectEncoder) AddTime(k string, v time.Time)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddTime)
    *   [func (m *MapObjectEncoder) AddUint(k string, v uint)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddUint)
    *   [func (m *MapObjectEncoder) AddUint8(k string, v uint8)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddUint8)
    *   [func (m *MapObjectEncoder) AddUint16(k string, v uint16)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddUint16)
    *   [func (m *MapObjectEncoder) AddUint32(k string, v uint32)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddUint32)
    *   [func (m *MapObjectEncoder) AddUint64(k string, v uint64)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddUint64)
    *   [func (m *MapObjectEncoder) AddUintptr(k string, v uintptr)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.AddUintptr)
    *   [func (m *MapObjectEncoder) OpenNamespace(k string)](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder.OpenNamespace)

*   [type NameEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#NameEncoder)
*       *   [func (e *NameEncoder) UnmarshalText(text []byte) error](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#NameEncoder.UnmarshalText)

*   [type ObjectEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#ObjectEncoder)
*   [type ObjectMarshaler](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#ObjectMarshaler)
*   [type ObjectMarshalerFunc](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#ObjectMarshalerFunc)
*       *   [func (f ObjectMarshalerFunc) MarshalLogObject(enc ObjectEncoder) error](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#ObjectMarshalerFunc.MarshalLogObject)

*   [type PrimitiveArrayEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#PrimitiveArrayEncoder)
*   [type ReflectedEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#ReflectedEncoder)
*   [type SamplerOption](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#SamplerOption)
*       *   [func SamplerHook(hook func(entry Entry, dec SamplingDecision)) SamplerOption](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#SamplerHook)

*   [type SamplingDecision](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#SamplingDecision)
*   [type TimeEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#TimeEncoder)
*       *   [func TimeEncoderOfLayout(layout string) TimeEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#TimeEncoderOfLayout)

*       *   [func (e *TimeEncoder) UnmarshalJSON(data []byte) error](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#TimeEncoder.UnmarshalJSON)
    *   [func (e *TimeEncoder) UnmarshalText(text []byte) error](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#TimeEncoder.UnmarshalText)
    *   [func (e *TimeEncoder) UnmarshalYAML(unmarshal func(interface{}) error) error](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#TimeEncoder.UnmarshalYAML)

*   [type WriteSyncer](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#WriteSyncer)
*       *   [func AddSync(w io.Writer) WriteSyncer](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#AddSync)
    *   [func Lock(ws WriteSyncer) WriteSyncer](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Lock)
    *   [func NewMultiWriteSyncer(ws ...WriteSyncer) WriteSyncer](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#NewMultiWriteSyncer)

DefaultLineEnding defines the default line ending when writing logs. Alternate line endings specified in EncoderConfig can override this behavior.

OmitKey defines the key to use when callers want to remove a key from log output.

DefaultClock is the default clock used by Zap in operations that require time. This clock uses the system clock for all operations.

func CapitalColorLevelEncoder(l [Level](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Level), enc [PrimitiveArrayEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#PrimitiveArrayEncoder))

CapitalColorLevelEncoder serializes a Level to an all-caps string and adds color. For example, InfoLevel is serialized to "INFO" and colored blue.

func CapitalLevelEncoder(l [Level](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Level), enc [PrimitiveArrayEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#PrimitiveArrayEncoder))

CapitalLevelEncoder serializes a Level to an all-caps string. For example, InfoLevel is serialized to "INFO".

EpochMillisTimeEncoder serializes a time.Time to a floating-point number of milliseconds since the Unix epoch.

EpochNanosTimeEncoder serializes a time.Time to an integer number of nanoseconds since the Unix epoch.

EpochTimeEncoder serializes a time.Time to a floating-point number of seconds since the Unix epoch.

func FullCallerEncoder(caller [EntryCaller](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#EntryCaller), enc [PrimitiveArrayEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#PrimitiveArrayEncoder))

FullCallerEncoder serializes a caller in /full/path/to/package/file:line format.

func FullNameEncoder(loggerName [string](https://pkg.go.dev/builtin#string), enc [PrimitiveArrayEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#PrimitiveArrayEncoder))

FullNameEncoder serializes the logger name as-is.

ISO8601TimeEncoder serializes a time.Time to an ISO8601-formatted string with millisecond precision.

If enc supports AppendTimeLayout(t time.Time,layout string), it's used instead of appending a pre-formatted string value.

func LowercaseColorLevelEncoder(l [Level](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Level), enc [PrimitiveArrayEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#PrimitiveArrayEncoder))

LowercaseColorLevelEncoder serializes a Level to a lowercase string and adds coloring. For example, InfoLevel is serialized to "info" and colored blue.

func LowercaseLevelEncoder(l [Level](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Level), enc [PrimitiveArrayEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#PrimitiveArrayEncoder))

LowercaseLevelEncoder serializes a Level to a lowercase string. For example, InfoLevel is serialized to "info".

MillisDurationEncoder serializes a time.Duration to an integer number of milliseconds elapsed.

NanosDurationEncoder serializes a time.Duration to an integer number of nanoseconds elapsed.

RFC3339NanoTimeEncoder serializes a time.Time to an RFC3339-formatted string with nanosecond precision.

If enc supports AppendTimeLayout(t time.Time,layout string), it's used instead of appending a pre-formatted string value.

RFC3339TimeEncoder serializes a time.Time to an RFC3339-formatted string.

If enc supports AppendTimeLayout(t time.Time,layout string), it's used instead of appending a pre-formatted string value.

SecondsDurationEncoder serializes a time.Duration to a floating-point number of seconds elapsed.

func ShortCallerEncoder(caller [EntryCaller](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#EntryCaller), enc [PrimitiveArrayEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#PrimitiveArrayEncoder))

ShortCallerEncoder serializes a caller in package/file:line format, trimming all but the final directory from the full path.

StringDurationEncoder serializes a time.Duration using its built-in String method.

ArrayEncoder is a strongly-typed, encoding-agnostic interface for adding array-like objects to the logging context. Of note, it supports mixed-type arrays even though they aren't typical in Go. Like slices, ArrayEncoders aren't safe for concurrent use (though typical use shouldn't require locks).

type ArrayMarshaler interface {
 MarshalLogArray([ArrayEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#ArrayEncoder)) [error](https://pkg.go.dev/builtin#error)}

ArrayMarshaler allows user-defined types to efficiently add themselves to the logging context, and to selectively omit information which shouldn't be included in logs (e.g., passwords).

Note: ArrayMarshaler is only used when zap.Array is used or when passed directly to zap.Any. It is not used when reflection-based encoding is used.

type ArrayMarshalerFunc func([ArrayEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#ArrayEncoder)) [error](https://pkg.go.dev/builtin#error)

ArrayMarshalerFunc is a type adapter that turns a function into an ArrayMarshaler.

MarshalLogArray calls the underlying function.

type BufferedWriteSyncer struct {
	
	
	
	WS [WriteSyncer](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#WriteSyncer)

	
	
	
	Size [int](https://pkg.go.dev/builtin#int)

	
	
	
	FlushInterval [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)

	
	
	
	Clock [Clock](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Clock)
	
}

A BufferedWriteSyncer is a WriteSyncer that buffers writes in-memory before flushing them to a wrapped WriteSyncer after reaching some limit, or at some fixed interval--whichever comes first.

BufferedWriteSyncer is safe for concurrent use. You don't need to use zapcore.Lock for WriteSyncers with BufferedWriteSyncer.

To set up a BufferedWriteSyncer, construct a WriteSyncer for your log destination (*os.File is a valid WriteSyncer), wrap it with BufferedWriteSyncer, and defer a Stop() call for when you no longer need the object.

 func main() {
   ws := ... // your log destination
   bws := &zapcore.BufferedWriteSyncer{WS: ws}
   defer bws.Stop()

   // ...
   core := zapcore.NewCore(enc, bws, lvl)
   logger := zap.New(core)

   // ...
}

By default, a BufferedWriteSyncer will buffer up to 256 kilobytes of logs, waiting at most 30 seconds between flushes. You can customize these parameters by setting the Size or FlushInterval fields. For example, the following buffers up to 512 kB of logs before flushing them to Stderr, with a maximum of one minute between each flush.

ws := &BufferedWriteSyncer{
  WS:            os.Stderr,
  Size:          512 * 1024, // 512 kB
  FlushInterval: time.Minute,
}
defer ws.Stop()

Stop closes the buffer, cleans up background goroutines, and flushes remaining unwritten data.

Sync flushes buffered log data into disk directly.

Write writes log data into buffer syncer directly, multiple Write calls will be batched, and log data will be flushed to disk when the buffer is full or periodically.

type CallerEncoder func([EntryCaller](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#EntryCaller), [PrimitiveArrayEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#PrimitiveArrayEncoder))

A CallerEncoder serializes an EntryCaller to a primitive type.

This function must make exactly one call to a PrimitiveArrayEncoder's Append* method.

UnmarshalText unmarshals text to a CallerEncoder. "full" is unmarshaled to FullCallerEncoder and anything else is unmarshaled to ShortCallerEncoder.

type CheckWriteAction [uint8](https://pkg.go.dev/builtin#uint8)

CheckWriteAction indicates what action to take after a log entry is processed. Actions are ordered in increasing severity.

const (
	
	WriteThenNoop [CheckWriteAction](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckWriteAction) = [iota](https://pkg.go.dev/builtin#iota)
	WriteThenGoexit
	WriteThenPanic
	WriteThenFatal
)

func (a [CheckWriteAction](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckWriteAction)) OnWrite(ce *[CheckedEntry](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckedEntry), _ [][Field](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Field))

OnWrite implements the OnWrite method to keep CheckWriteAction compatible with the new CheckWriteHook interface which deprecates CheckWriteAction.

type CheckWriteHook interface {
	
	
	
	
	OnWrite(*[CheckedEntry](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckedEntry), [][Field](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Field))
}

CheckWriteHook is a custom action that may be executed after an entry is written.

Register one on a CheckedEntry with the After method.

if ce := logger.Check(...); ce != nil {
  ce = ce.After(hook)
  ce.Write(...)
}

You can configure the hook for Fatal log statements at the logger level with the zap.WithFatalHook option.

type CheckedEntry struct {
[Entry](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Entry) ErrorOutput [WriteSyncer](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#WriteSyncer)	
}

CheckedEntry is an Entry together with a collection of Cores that have already agreed to log it.

CheckedEntry references should be created by calling AddCore or After on a nil *CheckedEntry. References are returned to a pool after Write, and MUST NOT be retained after calling their Write method.

func (ce *[CheckedEntry](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckedEntry)) AddCore(ent [Entry](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Entry), core [Core](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Core)) *[CheckedEntry](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckedEntry)

AddCore adds a Core that has agreed to log this CheckedEntry. It's intended to be used by Core.Check implementations, and is safe to call on nil CheckedEntry references.

func (ce *[CheckedEntry](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckedEntry)) After(ent [Entry](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Entry), hook [CheckWriteHook](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckWriteHook)) *[CheckedEntry](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckedEntry)

After sets this CheckEntry's CheckWriteHook, which will be called after this log entry has been written. It's safe to call this on nil CheckedEntry references.

func (ce *[CheckedEntry](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckedEntry)) Should(ent [Entry](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Entry), should [CheckWriteAction](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckWriteAction)) *[CheckedEntry](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckedEntry)

Should sets this CheckedEntry's CheckWriteAction, which controls whether a Core will panic or fatal after writing this log entry. Like AddCore, it's safe to call on nil CheckedEntry references.

Deprecated: Use [CheckedEntry.After](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckedEntry.After) instead.

func (ce *[CheckedEntry](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CheckedEntry)) Write(fields ...[Field](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Field))

Write writes the entry to the stored Cores, returns any errors, and returns the CheckedEntry reference to a pool for immediate re-use. Finally, it executes any required CheckWriteAction.

Clock is a source of time for logged entries.

Core is a minimal, fast logger interface. It's designed for library authors to wrap in a more user-friendly API.

func NewCore(enc [Encoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Encoder), ws [WriteSyncer](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#WriteSyncer), enab [LevelEnabler](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#LevelEnabler)) [Core](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Core)

NewCore creates a Core that writes logs to a WriteSyncer.

func NewIncreaseLevelCore(core [Core](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Core), level [LevelEnabler](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#LevelEnabler)) ([Core](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Core), [error](https://pkg.go.dev/builtin#error))

NewIncreaseLevelCore creates a core that can be used to increase the level of an existing Core. It cannot be used to decrease the logging level, as it acts as a filter before calling the underlying core. If level decreases the log level, an error is returned.

func NewLazyWith(core [Core](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Core), fields [][Field](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Field)) [Core](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Core)

NewLazyWith wraps a Core with a "lazy" Core that will only encode fields if the logger is written to (or is further chained in a lon-lazy manner).

NewNopCore returns a no-op Core.

NewSampler creates a Core that samples incoming entries, which caps the CPU and I/O load of logging while attempting to preserve a representative subset of your logs.

Zap samples by logging the first N entries with a given level and message each tick. If more Entries with the same level and message are seen during the same interval, every Mth message is logged and the rest are dropped.

Keep in mind that zap's sampling implementation is optimized for speed over absolute precision; under load, each tick may be slightly over- or under-sampled.

Deprecated: use NewSamplerWithOptions.

func NewSamplerWithOptions(core [Core](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Core), tick [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration), first, thereafter [int](https://pkg.go.dev/builtin#int), opts ...[SamplerOption](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#SamplerOption)) [Core](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Core)

NewSamplerWithOptions creates a Core that samples incoming entries, which caps the CPU and I/O load of logging while attempting to preserve a representative subset of your logs.

Zap samples by logging the first N entries with a given level and message each tick. If more Entries with the same level and message are seen during the same interval, every Mth message is logged and the rest are dropped.

For example,

core = NewSamplerWithOptions(core, time.Second, 10, 5)

This will log the first 10 log entries with the same level and message in a one second interval as-is. Following that, it will allow through every 5th log entry with the same level and message in that interval.

If thereafter is zero, the Core will drop all log entries after the first N in that interval.

Sampler can be configured to report sampling decisions with the SamplerHook option.

Keep in mind that Zap's sampling implementation is optimized for speed over absolute precision; under load, each tick may be slightly over- or under-sampled.

func NewTee(cores ...[Core](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Core)) [Core](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Core)

NewTee creates a Core that duplicates log entries into two or more underlying Cores.

Calling it with a single Core returns the input unchanged, and calling it with no input returns a no-op Core.

func RegisterHooks(core [Core](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Core), hooks ...func([Entry](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Entry)) [error](https://pkg.go.dev/builtin#error)) [Core](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Core)

RegisterHooks wraps a Core and runs a collection of user-defined callback hooks each time a message is logged. Execution of the callbacks is blocking.

This offers users an easy way to register simple callbacks (e.g., metrics collection) without implementing the full Core interface.

A DurationEncoder serializes a time.Duration to a primitive type.

This function must make exactly one call to a PrimitiveArrayEncoder's Append* method.

UnmarshalText unmarshals text to a DurationEncoder. "string" is unmarshaled to StringDurationEncoder, and anything else is unmarshaled to NanosDurationEncoder.

Encoder is a format-agnostic interface for all log entry marshalers. Since log encoders don't need to support the same wide range of use cases as general-purpose marshalers, it's possible to make them faster and lower-allocation.

Implementations of the ObjectEncoder interface's methods can, of course, freely modify the receiver. However, the Clone and EncodeEntry methods will be called concurrently and shouldn't modify the receiver.

func NewConsoleEncoder(cfg [EncoderConfig](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#EncoderConfig)) [Encoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Encoder)

NewConsoleEncoder creates an encoder whose output is designed for human - rather than machine - consumption. It serializes the core log entry data (message, level, timestamp, etc.) in a plain-text format and leaves the structured context as JSON.

Note that although the console encoder doesn't use the keys specified in the encoder configuration, it will omit any element whose key is set to the empty string.

func NewJSONEncoder(cfg [EncoderConfig](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#EncoderConfig)) [Encoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Encoder)

NewJSONEncoder creates a fast, low-allocation JSON encoder. The encoder appropriately escapes all field keys and values.

Note that the encoder doesn't deduplicate keys, so it's possible to produce a message like

{"foo":"bar","foo":"baz"}

This is permitted by the JSON specification, but not encouraged. Many libraries will ignore duplicate key-value pairs (typically keeping the last pair) when unmarshaling, but users should attempt to avoid adding duplicate keys.

type EncoderConfig struct {
	
	
 MessageKey [string](https://pkg.go.dev/builtin#string) `json:"messageKey" yaml:"messageKey"`  LevelKey [string](https://pkg.go.dev/builtin#string) `json:"levelKey" yaml:"levelKey"`  TimeKey [string](https://pkg.go.dev/builtin#string) `json:"timeKey" yaml:"timeKey"`  NameKey [string](https://pkg.go.dev/builtin#string) `json:"nameKey" yaml:"nameKey"`  CallerKey [string](https://pkg.go.dev/builtin#string) `json:"callerKey" yaml:"callerKey"`  FunctionKey [string](https://pkg.go.dev/builtin#string) `json:"functionKey" yaml:"functionKey"`  StacktraceKey [string](https://pkg.go.dev/builtin#string) `json:"stacktraceKey" yaml:"stacktraceKey"`  SkipLineEnding [bool](https://pkg.go.dev/builtin#bool) `json:"skipLineEnding" yaml:"skipLineEnding"`  LineEnding [string](https://pkg.go.dev/builtin#string) `json:"lineEnding" yaml:"lineEnding"` 	
	
	
 EncodeLevel [LevelEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#LevelEncoder) `json:"levelEncoder" yaml:"levelEncoder"`  EncodeTime [TimeEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#TimeEncoder) `json:"timeEncoder" yaml:"timeEncoder"`  EncodeDuration [DurationEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#DurationEncoder) `json:"durationEncoder" yaml:"durationEncoder"`  EncodeCaller [CallerEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#CallerEncoder) `json:"callerEncoder" yaml:"callerEncoder"` 	
	EncodeName [NameEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#NameEncoder) `json:"nameEncoder" yaml:"nameEncoder"`
	
	NewReflectedEncoder func([io](https://pkg.go.dev/io).[Writer](https://pkg.go.dev/io#Writer)) [ReflectedEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#ReflectedEncoder) `json:"-" yaml:"-"`
	
	ConsoleSeparator [string](https://pkg.go.dev/builtin#string) `json:"consoleSeparator" yaml:"consoleSeparator"`
}

An EncoderConfig allows users to configure the concrete encoders supplied by zapcore.

An Entry represents a complete log message. The entry's structured context is already serialized, but the log level, time, message, and call site information are available for inspection and modification. Any fields left empty will be omitted when encoding.

Entries are pooled, so any functions that accept them MUST be careful not to retain references to them.

EntryCaller represents the caller of a logging function.

NewEntryCaller makes an EntryCaller from the return signature of runtime.Caller.

FullPath returns a /full/path/to/package/file:line description of the caller.

String returns the full path and line number of the caller.

TrimmedPath returns a package/file:line description of the caller, preserving only the leaf directory name and file name.

A Field is a marshaling operation used to add a key-value pair to a logger's context. Most fields are lazily marshaled, so it's inexpensive to add fields to disabled debug-level log statements.

func (f [Field](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Field)) AddTo(enc [ObjectEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#ObjectEncoder))

AddTo exports a field through the ObjectEncoder interface. It's primarily useful to library authors, and shouldn't be necessary in most applications.

func (f [Field](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Field)) Equals(other [Field](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Field)) [bool](https://pkg.go.dev/builtin#bool)

Equals returns whether two fields are equal. For non-primitive types such as errors, marshalers, or reflect types, it uses reflect.DeepEqual.

A FieldType indicates which member of the Field union struct should be used and how it should be serialized.

const (
	UnknownType [FieldType](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#FieldType) = [iota](https://pkg.go.dev/builtin#iota)
	ArrayMarshalerType
	ObjectMarshalerType
	BinaryType
	BoolType
	ByteStringType
	Complex128Type
	Complex64Type
	DurationType
	Float64Type
	Float32Type
	Int64Type
	Int32Type
	Int16Type
	Int8Type
	StringType
	
	TimeType
	TimeFullType
	Uint64Type
	Uint32Type
	Uint16Type
	Uint8Type
	UintptrType
	
	ReflectType
	
	NamespaceType
	StringerType
	ErrorType
	SkipType

	
	InlineMarshalerType
)

A Level is a logging priority. Higher levels are more important.

const (
	
	DebugLevel [Level](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Level) = [iota](https://pkg.go.dev/builtin#iota) - 1
	InfoLevel
	
	WarnLevel
	
	ErrorLevel
	
	DPanicLevel
	PanicLevel
	FatalLevel

	
	
	InvalidLevel = _maxLevel + 1
)

func LevelOf(enab [LevelEnabler](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#LevelEnabler)) [Level](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Level)

LevelOf reports the minimum enabled log level for the given LevelEnabler from Zap's supported log levels, or [InvalidLevel](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#InvalidLevel) if none of them are enabled.

A LevelEnabler may implement a 'Level() Level' method to override the behavior of this function.

func (c *core) Level() Level {
	return c.currentLevel
}

It is recommended that [Core](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Core) implementations that wrap other cores use LevelOf to retrieve the level of the wrapped core. For example,

func (c *coreWrapper) Level() Level {
	return zapcore.LevelOf(c.wrappedCore)
}

ParseLevel parses a level based on the lower-case or all-caps ASCII representation of the log level. If the provided ASCII representation is invalid an error is returned.

This is particularly useful when dealing with text input to configure log levels.

CapitalString returns an all-caps ASCII representation of the log level.

func (l [Level](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Level)) Enabled(lvl [Level](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Level)) [bool](https://pkg.go.dev/builtin#bool)

Enabled returns true if the given level is at or above this level.

func (l *[Level](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Level)) Get() interface{}

Get gets the level for the flag.Getter interface.

MarshalText marshals the Level to text. Note that the text representation drops the -Level suffix (see example).

Set sets the level for the flag.Value interface.

String returns a lower-case ASCII representation of the log level.

UnmarshalText unmarshals text to a level. Like MarshalText, UnmarshalText expects the text representation of a Level to drop the -Level suffix (see example).

In particular, this makes it easy to configure logging levels using YAML, TOML, or JSON files.

type LevelEnabler interface {
 Enabled([Level](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Level)) [bool](https://pkg.go.dev/builtin#bool)}

LevelEnabler decides whether a given logging level is enabled when logging a message.

Enablers are intended to be used to implement deterministic filters; concerns like sampling are better implemented as a Core.

Each concrete Level value implements a static LevelEnabler which returns true for itself and all higher logging levels. For example WarnLevel.Enabled() will return true for WarnLevel, ErrorLevel, DPanicLevel, PanicLevel, and FatalLevel, but return false for InfoLevel and DebugLevel.

type LevelEncoder func([Level](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Level), [PrimitiveArrayEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#PrimitiveArrayEncoder))

A LevelEncoder serializes a Level to a primitive type.

This function must make exactly one call to a PrimitiveArrayEncoder's Append* method.

UnmarshalText unmarshals text to a LevelEncoder. "capital" is unmarshaled to CapitalLevelEncoder, "coloredCapital" is unmarshaled to CapitalColorLevelEncoder, "colored" is unmarshaled to LowercaseColorLevelEncoder, and anything else is unmarshaled to LowercaseLevelEncoder.

type MapObjectEncoder struct {
	Fields map[[string](https://pkg.go.dev/builtin#string)]interface{}
	
}

MapObjectEncoder is an ObjectEncoder backed by a simple map[string]interface{}. It's not fast enough for production use, but it's helpful in tests.

func NewMapObjectEncoder() *[MapObjectEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#MapObjectEncoder)

NewMapObjectEncoder creates a new map-backed ObjectEncoder.

AddArray implements ObjectEncoder.

AddBinary implements ObjectEncoder.

AddBool implements ObjectEncoder.

AddByteString implements ObjectEncoder.

AddComplex64 implements ObjectEncoder.

AddComplex128 implements ObjectEncoder.

AddDuration implements ObjectEncoder.

AddFloat32 implements ObjectEncoder.

AddFloat64 implements ObjectEncoder.

AddInt implements ObjectEncoder.

AddInt8 implements ObjectEncoder.

AddInt16 implements ObjectEncoder.

AddInt32 implements ObjectEncoder.

AddInt64 implements ObjectEncoder.

AddObject implements ObjectEncoder.

AddReflected implements ObjectEncoder.

AddString implements ObjectEncoder.

AddTime implements ObjectEncoder.

AddUint implements ObjectEncoder.

AddUint8 implements ObjectEncoder.

AddUint16 implements ObjectEncoder.

AddUint32 implements ObjectEncoder.

AddUint64 implements ObjectEncoder.

AddUintptr implements ObjectEncoder.

OpenNamespace implements ObjectEncoder.

A NameEncoder serializes a period-separated logger name to a primitive type.

This function must make exactly one call to a PrimitiveArrayEncoder's Append* method.

UnmarshalText unmarshals text to a NameEncoder. Currently, everything is unmarshaled to FullNameEncoder.

type ObjectEncoder interface {
	
 AddArray(key [string](https://pkg.go.dev/builtin#string), marshaler [ArrayMarshaler](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#ArrayMarshaler)) [error](https://pkg.go.dev/builtin#error) AddObject(key [string](https://pkg.go.dev/builtin#string), marshaler [ObjectMarshaler](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#ObjectMarshaler)) [error](https://pkg.go.dev/builtin#error)
	
 AddBinary(key [string](https://pkg.go.dev/builtin#string), value [][byte](https://pkg.go.dev/builtin#byte))  AddByteString(key [string](https://pkg.go.dev/builtin#string), value [][byte](https://pkg.go.dev/builtin#byte))  AddBool(key [string](https://pkg.go.dev/builtin#string), value [bool](https://pkg.go.dev/builtin#bool))  AddComplex128(key [string](https://pkg.go.dev/builtin#string), value [complex128](https://pkg.go.dev/builtin#complex128))  AddComplex64(key [string](https://pkg.go.dev/builtin#string), value [complex64](https://pkg.go.dev/builtin#complex64))  AddDuration(key [string](https://pkg.go.dev/builtin#string), value [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration))  AddFloat64(key [string](https://pkg.go.dev/builtin#string), value [float64](https://pkg.go.dev/builtin#float64))  AddFloat32(key [string](https://pkg.go.dev/builtin#string), value [float32](https://pkg.go.dev/builtin#float32))  AddInt(key [string](https://pkg.go.dev/builtin#string), value [int](https://pkg.go.dev/builtin#int))  AddInt64(key [string](https://pkg.go.dev/builtin#string), value [int64](https://pkg.go.dev/builtin#int64))  AddInt32(key [string](https://pkg.go.dev/builtin#string), value [int32](https://pkg.go.dev/builtin#int32))  AddInt16(key [string](https://pkg.go.dev/builtin#string), value [int16](https://pkg.go.dev/builtin#int16))  AddInt8(key [string](https://pkg.go.dev/builtin#string), value [int8](https://pkg.go.dev/builtin#int8))  AddString(key, value [string](https://pkg.go.dev/builtin#string))  AddTime(key [string](https://pkg.go.dev/builtin#string), value [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time))  AddUint(key [string](https://pkg.go.dev/builtin#string), value [uint](https://pkg.go.dev/builtin#uint))  AddUint64(key [string](https://pkg.go.dev/builtin#string), value [uint64](https://pkg.go.dev/builtin#uint64))  AddUint32(key [string](https://pkg.go.dev/builtin#string), value [uint32](https://pkg.go.dev/builtin#uint32))  AddUint16(key [string](https://pkg.go.dev/builtin#string), value [uint16](https://pkg.go.dev/builtin#uint16))  AddUint8(key [string](https://pkg.go.dev/builtin#string), value [uint8](https://pkg.go.dev/builtin#uint8))  AddUintptr(key [string](https://pkg.go.dev/builtin#string), value [uintptr](https://pkg.go.dev/builtin#uintptr)) 
	
	AddReflected(key [string](https://pkg.go.dev/builtin#string), value interface{}) [error](https://pkg.go.dev/builtin#error)
	
	
	OpenNamespace(key [string](https://pkg.go.dev/builtin#string))
}

ObjectEncoder is a strongly-typed, encoding-agnostic interface for adding a map- or struct-like object to the logging context. Like maps, ObjectEncoders aren't safe for concurrent use (though typical use shouldn't require locks).

type ObjectMarshaler interface {
 MarshalLogObject([ObjectEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#ObjectEncoder)) [error](https://pkg.go.dev/builtin#error)}

ObjectMarshaler allows user-defined types to efficiently add themselves to the logging context, and to selectively omit information which shouldn't be included in logs (e.g., passwords).

Note: ObjectMarshaler is only used when zap.Object is used or when passed directly to zap.Any. It is not used when reflection-based encoding is used.

type ObjectMarshalerFunc func([ObjectEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#ObjectEncoder)) [error](https://pkg.go.dev/builtin#error)

ObjectMarshalerFunc is a type adapter that turns a function into an ObjectMarshaler.

MarshalLogObject calls the underlying function.

PrimitiveArrayEncoder is the subset of the ArrayEncoder interface that deals only in Go's built-in types. It's included only so that Duration- and TimeEncoders cannot trigger infinite recursion.

type ReflectedEncoder interface {
	Encode(interface{}) [error](https://pkg.go.dev/builtin#error)
}

ReflectedEncoder serializes log fields that can't be serialized with Zap's JSON encoder. These have the ReflectType field type. Use EncoderConfig.NewReflectedEncoder to set this.

type SamplerOption interface {
	
}

SamplerOption configures a Sampler.

func SamplerHook(hook func(entry [Entry](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#Entry), dec [SamplingDecision](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#SamplingDecision))) [SamplerOption](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#SamplerOption)

SamplerHook registers a function which will be called when Sampler makes a decision.

This hook may be used to get visibility into the performance of the sampler. For example, use it to track metrics of dropped versus sampled logs.

var dropped atomic.Int64
zapcore.SamplerHook(func(ent zapcore.Entry, dec zapcore.SamplingDecision) {
  if dec&zapcore.LogDropped > 0 {
    dropped.Inc()
  }
})

SamplingDecision is a decision represented as a bit field made by sampler. More decisions may be added in the future.

const (
	LogDropped [SamplingDecision](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#SamplingDecision) = 1 << [iota](https://pkg.go.dev/builtin#iota)
	LogSampled
)

A TimeEncoder serializes a time.Time to a primitive type.

This function must make exactly one call to a PrimitiveArrayEncoder's Append* method.

func TimeEncoderOfLayout(layout [string](https://pkg.go.dev/builtin#string)) [TimeEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#TimeEncoder)

TimeEncoderOfLayout returns TimeEncoder which serializes a time.Time using given layout.

UnmarshalJSON unmarshals JSON to a TimeEncoder as same way UnmarshalYAML does.

UnmarshalText unmarshals text to a TimeEncoder. "rfc3339nano" and "RFC3339Nano" are unmarshaled to RFC3339NanoTimeEncoder. "rfc3339" and "RFC3339" are unmarshaled to RFC3339TimeEncoder. "iso8601" and "ISO8601" are unmarshaled to ISO8601TimeEncoder. "millis" is unmarshaled to EpochMillisTimeEncoder. "nanos" is unmarshaled to EpochNanosEncoder. Anything else is unmarshaled to EpochTimeEncoder.

func (e *[TimeEncoder](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#TimeEncoder)) UnmarshalYAML(unmarshal func(interface{}) [error](https://pkg.go.dev/builtin#error)) [error](https://pkg.go.dev/builtin#error)

UnmarshalYAML unmarshals YAML to a TimeEncoder. If value is an object with a "layout" field, it will be unmarshaled to TimeEncoder with given layout.

timeEncoder:
  layout: 06/01/02 03:04pm

If value is string, it uses UnmarshalText.

timeEncoder: iso8601

A WriteSyncer is an io.Writer that can also flush any buffered data. Note that *os.File (and thus, os.Stderr and os.Stdout) implement WriteSyncer.

AddSync converts an io.Writer to a WriteSyncer. It attempts to be intelligent: if the concrete type of the io.Writer implements WriteSyncer, we'll use the existing Sync method. If it doesn't, we'll add a no-op Sync.

func Lock(ws [WriteSyncer](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#WriteSyncer)) [WriteSyncer](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#WriteSyncer)

Lock wraps a WriteSyncer in a mutex to make it safe for concurrent use. In particular, *os.Files must be locked before use.

func NewMultiWriteSyncer(ws ...[WriteSyncer](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#WriteSyncer)) [WriteSyncer](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#WriteSyncer)

NewMultiWriteSyncer creates a WriteSyncer that duplicates its writes and sync calls, much like io.MultiWriter.
