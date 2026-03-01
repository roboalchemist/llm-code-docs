# Source: https://pkg.go.dev/go.uber.org/zap

Title: zap package - go.uber.org/zap - Go Packages

URL Source: https://pkg.go.dev/go.uber.org/zap

Markdown Content:
Package zap provides fast, structured, leveled logging.

For applications that log in the hot path, reflection-based serialization and string formatting are prohibitively expensive - they're CPU-intensive and make many small allocations. Put differently, using json.Marshal and fmt.Fprintf to log tons of interface{} makes your application slow.

Zap takes a different approach. It includes a reflection-free, zero-allocation JSON encoder, and the base Logger strives to avoid serialization overhead and allocations wherever possible. By building the high-level SugaredLogger on that foundation, zap lets users choose when they need to count every allocation and when they'd prefer a more familiar, loosely typed API.

#### Choosing a Logger [¶](https://pkg.go.dev/go.uber.org/zap#hdr-Choosing_a_Logger "Go to Choosing a Logger")

In contexts where performance is nice, but not critical, use the SugaredLogger. It's 4-10x faster than other structured logging packages and supports both structured and printf-style logging. Like log15 and go-kit, the SugaredLogger's structured logging APIs are loosely typed and accept a variadic number of key-value pairs. (For more advanced use cases, they also accept strongly typed fields - see the SugaredLogger.With documentation for details.)

sugar := zap.NewExample().Sugar()
defer sugar.Sync()
sugar.Infow("failed to fetch URL",
  "url", "http://example.com",
  "attempt", 3,
  "backoff", time.Second,
)
sugar.Infof("failed to fetch URL: %s", "http://example.com")

By default, loggers are unbuffered. However, since zap's low-level APIs allow buffering, calling Sync before letting your process exit is a good habit.

In the rare contexts where every microsecond and every allocation matter, use the Logger. It's even faster than the SugaredLogger and allocates far less, but it only supports strongly-typed, structured logging.

logger := zap.NewExample()
defer logger.Sync()
logger.Info("failed to fetch URL",
  zap.String("url", "http://example.com"),
  zap.Int("attempt", 3),
  zap.Duration("backoff", time.Second),
)

Choosing between the Logger and SugaredLogger doesn't need to be an application-wide decision: converting between the two is simple and inexpensive.

logger := zap.NewExample()
defer logger.Sync()
sugar := logger.Sugar()
plain := sugar.Desugar()

#### Configuring Zap [¶](https://pkg.go.dev/go.uber.org/zap#hdr-Configuring_Zap "Go to Configuring Zap")

The simplest way to build a Logger is to use zap's opinionated presets: NewExample, NewProduction, and NewDevelopment. These presets build a logger with a single function call:

logger, err := zap.NewProduction()
if err != nil {
  log.Fatalf("can't initialize zap logger: %v", err)
}
defer logger.Sync()

Presets are fine for small projects, but larger projects and organizations naturally require a bit more customization. For most users, zap's Config struct strikes the right balance between flexibility and convenience. See the package-level BasicConfiguration example for sample code.

More unusual configurations (splitting output between files, sending logs to a message queue, etc.) are possible, but require direct use of go.uber.org/zap/zapcore. See the package-level AdvancedConfiguration example for sample code.

#### Extending Zap [¶](https://pkg.go.dev/go.uber.org/zap#hdr-Extending_Zap "Go to Extending Zap")

The zap package itself is a relatively thin wrapper around the interfaces in go.uber.org/zap/zapcore. Extending zap to support a new encoding (e.g., BSON), a new log sink (e.g., Kafka), or something more exotic (perhaps an exception aggregation service, like Sentry or Rollbar) typically requires implementing the zapcore.Encoder, zapcore.WriteSyncer, or zapcore.Core interfaces. See the zapcore documentation for details.

Similarly, package authors can use the high-performance Encoder and Core implementations in the zapcore package to build their own loggers.

#### Frequently Asked Questions [¶](https://pkg.go.dev/go.uber.org/zap#hdr-Frequently_Asked_Questions "Go to Frequently Asked Questions")

An FAQ covering everything from installation errors to design decisions is available at [https://github.com/uber-go/zap/blob/master/FAQ.md](https://github.com/uber-go/zap/blob/master/FAQ.md).

Output:

{"level":"info","message":"logger construction succeeded","foo":"bar"} 

Output:

{"level":"info","msg":"Failed to fetch URL.","url":"http://example.com","attempt":3,"backoff":"1s"} {"level":"info","msg":"Failed to fetch URL: http://example.com"} {"level":"info","msg":"Failed to fetch URL.","url":"http://example.com","attempt":3,"backoff":"1s"} 

*   [Constants](https://pkg.go.dev/go.uber.org/zap#pkg-constants)
*   [func CombineWriteSyncers(writers ...zapcore.WriteSyncer) zapcore.WriteSyncer](https://pkg.go.dev/go.uber.org/zap#CombineWriteSyncers)
*   [func DictObject(val ...Field) zapcore.ObjectMarshaler](https://pkg.go.dev/go.uber.org/zap#DictObject)
*   [func LevelFlag(name string, defaultLevel zapcore.Level, usage string) *zapcore.Level](https://pkg.go.dev/go.uber.org/zap#LevelFlag)
*   [func NewDevelopmentEncoderConfig() zapcore.EncoderConfig](https://pkg.go.dev/go.uber.org/zap#NewDevelopmentEncoderConfig)
*   [func NewProductionEncoderConfig() zapcore.EncoderConfig](https://pkg.go.dev/go.uber.org/zap#NewProductionEncoderConfig)
*   [func NewStdLog(l *Logger) *log.Logger](https://pkg.go.dev/go.uber.org/zap#NewStdLog)
*   [func NewStdLogAt(l *Logger, level zapcore.Level) (*log.Logger, error)](https://pkg.go.dev/go.uber.org/zap#NewStdLogAt)
*   [func Open(paths ...string) (zapcore.WriteSyncer, func(), error)](https://pkg.go.dev/go.uber.org/zap#Open)
*   [func RedirectStdLog(l *Logger) func()](https://pkg.go.dev/go.uber.org/zap#RedirectStdLog)
*   [func RedirectStdLogAt(l *Logger, level zapcore.Level) (func(), error)](https://pkg.go.dev/go.uber.org/zap#RedirectStdLogAt)
*   [func RegisterEncoder(name string, constructor func(zapcore.EncoderConfig) (zapcore.Encoder, error)) error](https://pkg.go.dev/go.uber.org/zap#RegisterEncoder)
*   [func RegisterSink(scheme string, factory func(*url.URL) (Sink, error)) error](https://pkg.go.dev/go.uber.org/zap#RegisterSink)
*   [func ReplaceGlobals(logger *Logger) func()](https://pkg.go.dev/go.uber.org/zap#ReplaceGlobals)
*   [type AtomicLevel](https://pkg.go.dev/go.uber.org/zap#AtomicLevel)
*       *   [func NewAtomicLevel() AtomicLevel](https://pkg.go.dev/go.uber.org/zap#NewAtomicLevel)
    *   [func NewAtomicLevelAt(l zapcore.Level) AtomicLevel](https://pkg.go.dev/go.uber.org/zap#NewAtomicLevelAt)
    *   [func ParseAtomicLevel(text string) (AtomicLevel, error)](https://pkg.go.dev/go.uber.org/zap#ParseAtomicLevel)

*       *   [func (lvl AtomicLevel) Enabled(l zapcore.Level) bool](https://pkg.go.dev/go.uber.org/zap#AtomicLevel.Enabled)
    *   [func (lvl AtomicLevel) Level() zapcore.Level](https://pkg.go.dev/go.uber.org/zap#AtomicLevel.Level)
    *   [func (lvl AtomicLevel) MarshalText() (text []byte, err error)](https://pkg.go.dev/go.uber.org/zap#AtomicLevel.MarshalText)
    *   [func (lvl AtomicLevel) ServeHTTP(w http.ResponseWriter, r *http.Request)](https://pkg.go.dev/go.uber.org/zap#AtomicLevel.ServeHTTP)
    *   [func (lvl AtomicLevel) SetLevel(l zapcore.Level)](https://pkg.go.dev/go.uber.org/zap#AtomicLevel.SetLevel)
    *   [func (lvl AtomicLevel) String() string](https://pkg.go.dev/go.uber.org/zap#AtomicLevel.String)
    *   [func (lvl *AtomicLevel) UnmarshalText(text []byte) error](https://pkg.go.dev/go.uber.org/zap#AtomicLevel.UnmarshalText)

*   [type Config](https://pkg.go.dev/go.uber.org/zap#Config)
*       *   [func NewDevelopmentConfig() Config](https://pkg.go.dev/go.uber.org/zap#NewDevelopmentConfig)
    *   [func NewProductionConfig() Config](https://pkg.go.dev/go.uber.org/zap#NewProductionConfig)

*       *   [func (cfg Config) Build(opts ...Option) (*Logger, error)](https://pkg.go.dev/go.uber.org/zap#Config.Build)

*   [type Field](https://pkg.go.dev/go.uber.org/zap#Field)
*       *   [func Any(key string, value interface{}) Field](https://pkg.go.dev/go.uber.org/zap#Any)
    *   [func Array(key string, val zapcore.ArrayMarshaler) Field](https://pkg.go.dev/go.uber.org/zap#Array)
    *   [func Binary(key string, val []byte) Field](https://pkg.go.dev/go.uber.org/zap#Binary)
    *   [func Bool(key string, val bool) Field](https://pkg.go.dev/go.uber.org/zap#Bool)
    *   [func Boolp(key string, val *bool) Field](https://pkg.go.dev/go.uber.org/zap#Boolp)
    *   [func Bools(key string, bs []bool) Field](https://pkg.go.dev/go.uber.org/zap#Bools)
    *   [func ByteString(key string, val []byte) Field](https://pkg.go.dev/go.uber.org/zap#ByteString)
    *   [func ByteStrings(key string, bss [][]byte) Field](https://pkg.go.dev/go.uber.org/zap#ByteStrings)
    *   [func Complex64(key string, val complex64) Field](https://pkg.go.dev/go.uber.org/zap#Complex64)
    *   [func Complex64p(key string, val *complex64) Field](https://pkg.go.dev/go.uber.org/zap#Complex64p)
    *   [func Complex64s(key string, nums []complex64) Field](https://pkg.go.dev/go.uber.org/zap#Complex64s)
    *   [func Complex128(key string, val complex128) Field](https://pkg.go.dev/go.uber.org/zap#Complex128)
    *   [func Complex128p(key string, val *complex128) Field](https://pkg.go.dev/go.uber.org/zap#Complex128p)
    *   [func Complex128s(key string, nums []complex128) Field](https://pkg.go.dev/go.uber.org/zap#Complex128s)
    *   [func Dict(key string, val ...Field) Field](https://pkg.go.dev/go.uber.org/zap#Dict)
    *   [func Duration(key string, val time.Duration) Field](https://pkg.go.dev/go.uber.org/zap#Duration)
    *   [func Durationp(key string, val *time.Duration) Field](https://pkg.go.dev/go.uber.org/zap#Durationp)
    *   [func Durations(key string, ds []time.Duration) Field](https://pkg.go.dev/go.uber.org/zap#Durations)
    *   [func Error(err error) Field](https://pkg.go.dev/go.uber.org/zap#Error)
    *   [func Errors(key string, errs []error) Field](https://pkg.go.dev/go.uber.org/zap#Errors)
    *   [func Float32(key string, val float32) Field](https://pkg.go.dev/go.uber.org/zap#Float32)
    *   [func Float32p(key string, val *float32) Field](https://pkg.go.dev/go.uber.org/zap#Float32p)
    *   [func Float32s(key string, nums []float32) Field](https://pkg.go.dev/go.uber.org/zap#Float32s)
    *   [func Float64(key string, val float64) Field](https://pkg.go.dev/go.uber.org/zap#Float64)
    *   [func Float64p(key string, val *float64) Field](https://pkg.go.dev/go.uber.org/zap#Float64p)
    *   [func Float64s(key string, nums []float64) Field](https://pkg.go.dev/go.uber.org/zap#Float64s)
    *   [func Inline(val zapcore.ObjectMarshaler) Field](https://pkg.go.dev/go.uber.org/zap#Inline)
    *   [func Int(key string, val int) Field](https://pkg.go.dev/go.uber.org/zap#Int)
    *   [func Int8(key string, val int8) Field](https://pkg.go.dev/go.uber.org/zap#Int8)
    *   [func Int8p(key string, val *int8) Field](https://pkg.go.dev/go.uber.org/zap#Int8p)
    *   [func Int8s(key string, nums []int8) Field](https://pkg.go.dev/go.uber.org/zap#Int8s)
    *   [func Int16(key string, val int16) Field](https://pkg.go.dev/go.uber.org/zap#Int16)
    *   [func Int16p(key string, val *int16) Field](https://pkg.go.dev/go.uber.org/zap#Int16p)
    *   [func Int16s(key string, nums []int16) Field](https://pkg.go.dev/go.uber.org/zap#Int16s)
    *   [func Int32(key string, val int32) Field](https://pkg.go.dev/go.uber.org/zap#Int32)
    *   [func Int32p(key string, val *int32) Field](https://pkg.go.dev/go.uber.org/zap#Int32p)
    *   [func Int32s(key string, nums []int32) Field](https://pkg.go.dev/go.uber.org/zap#Int32s)
    *   [func Int64(key string, val int64) Field](https://pkg.go.dev/go.uber.org/zap#Int64)
    *   [func Int64p(key string, val *int64) Field](https://pkg.go.dev/go.uber.org/zap#Int64p)
    *   [func Int64s(key string, nums []int64) Field](https://pkg.go.dev/go.uber.org/zap#Int64s)
    *   [func Intp(key string, val *int) Field](https://pkg.go.dev/go.uber.org/zap#Intp)
    *   [func Ints(key string, nums []int) Field](https://pkg.go.dev/go.uber.org/zap#Ints)
    *   [func NamedError(key string, err error) Field](https://pkg.go.dev/go.uber.org/zap#NamedError)
    *   [func Namespace(key string) Field](https://pkg.go.dev/go.uber.org/zap#Namespace)
    *   [func Object(key string, val zapcore.ObjectMarshaler) Field](https://pkg.go.dev/go.uber.org/zap#Object)
    *   [func ObjectValues[T any, P ObjectMarshalerPtr[T]](key string, values []T) Field](https://pkg.go.dev/go.uber.org/zap#ObjectValues)
    *   [func Objects[T zapcore.ObjectMarshaler](key string, values []T) Field](https://pkg.go.dev/go.uber.org/zap#Objects)
    *   [func Reflect(key string, val interface{}) Field](https://pkg.go.dev/go.uber.org/zap#Reflect)
    *   [func Skip() Field](https://pkg.go.dev/go.uber.org/zap#Skip)
    *   [func Stack(key string) Field](https://pkg.go.dev/go.uber.org/zap#Stack)
    *   [func StackSkip(key string, skip int) Field](https://pkg.go.dev/go.uber.org/zap#StackSkip)
    *   [func String(key string, val string) Field](https://pkg.go.dev/go.uber.org/zap#String)
    *   [func Stringer(key string, val fmt.Stringer) Field](https://pkg.go.dev/go.uber.org/zap#Stringer)
    *   [func Stringers[T fmt.Stringer](key string, values []T) Field](https://pkg.go.dev/go.uber.org/zap#Stringers)
    *   [func Stringp(key string, val *string) Field](https://pkg.go.dev/go.uber.org/zap#Stringp)
    *   [func Strings(key string, ss []string) Field](https://pkg.go.dev/go.uber.org/zap#Strings)
    *   [func Time(key string, val time.Time) Field](https://pkg.go.dev/go.uber.org/zap#Time)
    *   [func Timep(key string, val *time.Time) Field](https://pkg.go.dev/go.uber.org/zap#Timep)
    *   [func Times(key string, ts []time.Time) Field](https://pkg.go.dev/go.uber.org/zap#Times)
    *   [func Uint(key string, val uint) Field](https://pkg.go.dev/go.uber.org/zap#Uint)
    *   [func Uint8(key string, val uint8) Field](https://pkg.go.dev/go.uber.org/zap#Uint8)
    *   [func Uint8p(key string, val *uint8) Field](https://pkg.go.dev/go.uber.org/zap#Uint8p)
    *   [func Uint8s(key string, nums []uint8) Field](https://pkg.go.dev/go.uber.org/zap#Uint8s)
    *   [func Uint16(key string, val uint16) Field](https://pkg.go.dev/go.uber.org/zap#Uint16)
    *   [func Uint16p(key string, val *uint16) Field](https://pkg.go.dev/go.uber.org/zap#Uint16p)
    *   [func Uint16s(key string, nums []uint16) Field](https://pkg.go.dev/go.uber.org/zap#Uint16s)
    *   [func Uint32(key string, val uint32) Field](https://pkg.go.dev/go.uber.org/zap#Uint32)
    *   [func Uint32p(key string, val *uint32) Field](https://pkg.go.dev/go.uber.org/zap#Uint32p)
    *   [func Uint32s(key string, nums []uint32) Field](https://pkg.go.dev/go.uber.org/zap#Uint32s)
    *   [func Uint64(key string, val uint64) Field](https://pkg.go.dev/go.uber.org/zap#Uint64)
    *   [func Uint64p(key string, val *uint64) Field](https://pkg.go.dev/go.uber.org/zap#Uint64p)
    *   [func Uint64s(key string, nums []uint64) Field](https://pkg.go.dev/go.uber.org/zap#Uint64s)
    *   [func Uintp(key string, val *uint) Field](https://pkg.go.dev/go.uber.org/zap#Uintp)
    *   [func Uintptr(key string, val uintptr) Field](https://pkg.go.dev/go.uber.org/zap#Uintptr)
    *   [func Uintptrp(key string, val *uintptr) Field](https://pkg.go.dev/go.uber.org/zap#Uintptrp)
    *   [func Uintptrs(key string, us []uintptr) Field](https://pkg.go.dev/go.uber.org/zap#Uintptrs)
    *   [func Uints(key string, nums []uint) Field](https://pkg.go.dev/go.uber.org/zap#Uints)

*   [type LevelEnablerFunc](https://pkg.go.dev/go.uber.org/zap#LevelEnablerFunc)
*       *   [func (f LevelEnablerFunc) Enabled(lvl zapcore.Level) bool](https://pkg.go.dev/go.uber.org/zap#LevelEnablerFunc.Enabled)

*   [type Logger](https://pkg.go.dev/go.uber.org/zap#Logger)
*       *   [func L() *Logger](https://pkg.go.dev/go.uber.org/zap#L)
    *   [func Must(logger *Logger, err error) *Logger](https://pkg.go.dev/go.uber.org/zap#Must)
    *   [func New(core zapcore.Core, options ...Option) *Logger](https://pkg.go.dev/go.uber.org/zap#New)
    *   [func NewDevelopment(options ...Option) (*Logger, error)](https://pkg.go.dev/go.uber.org/zap#NewDevelopment)
    *   [func NewExample(options ...Option) *Logger](https://pkg.go.dev/go.uber.org/zap#NewExample)
    *   [func NewNop() *Logger](https://pkg.go.dev/go.uber.org/zap#NewNop)
    *   [func NewProduction(options ...Option) (*Logger, error)](https://pkg.go.dev/go.uber.org/zap#NewProduction)

*       *   [func (log *Logger) Check(lvl zapcore.Level, msg string) *zapcore.CheckedEntry](https://pkg.go.dev/go.uber.org/zap#Logger.Check)
    *   [func (log *Logger) Core() zapcore.Core](https://pkg.go.dev/go.uber.org/zap#Logger.Core)
    *   [func (log *Logger) DPanic(msg string, fields ...Field)](https://pkg.go.dev/go.uber.org/zap#Logger.DPanic)
    *   [func (log *Logger) Debug(msg string, fields ...Field)](https://pkg.go.dev/go.uber.org/zap#Logger.Debug)
    *   [func (log *Logger) Error(msg string, fields ...Field)](https://pkg.go.dev/go.uber.org/zap#Logger.Error)
    *   [func (log *Logger) Fatal(msg string, fields ...Field)](https://pkg.go.dev/go.uber.org/zap#Logger.Fatal)
    *   [func (log *Logger) Info(msg string, fields ...Field)](https://pkg.go.dev/go.uber.org/zap#Logger.Info)
    *   [func (log *Logger) Level() zapcore.Level](https://pkg.go.dev/go.uber.org/zap#Logger.Level)
    *   [func (log *Logger) Log(lvl zapcore.Level, msg string, fields ...Field)](https://pkg.go.dev/go.uber.org/zap#Logger.Log)
    *   [func (log *Logger) Name() string](https://pkg.go.dev/go.uber.org/zap#Logger.Name)
    *   [func (log *Logger) Named(s string) *Logger](https://pkg.go.dev/go.uber.org/zap#Logger.Named)
    *   [func (log *Logger) Panic(msg string, fields ...Field)](https://pkg.go.dev/go.uber.org/zap#Logger.Panic)
    *   [func (log *Logger) Sugar() *SugaredLogger](https://pkg.go.dev/go.uber.org/zap#Logger.Sugar)
    *   [func (log *Logger) Sync() error](https://pkg.go.dev/go.uber.org/zap#Logger.Sync)
    *   [func (log *Logger) Warn(msg string, fields ...Field)](https://pkg.go.dev/go.uber.org/zap#Logger.Warn)
    *   [func (log *Logger) With(fields ...Field) *Logger](https://pkg.go.dev/go.uber.org/zap#Logger.With)
    *   [func (log *Logger) WithLazy(fields ...Field) *Logger](https://pkg.go.dev/go.uber.org/zap#Logger.WithLazy)
    *   [func (log *Logger) WithOptions(opts ...Option) *Logger](https://pkg.go.dev/go.uber.org/zap#Logger.WithOptions)

*   [type ObjectMarshalerPtr](https://pkg.go.dev/go.uber.org/zap#ObjectMarshalerPtr)
*   [type Option](https://pkg.go.dev/go.uber.org/zap#Option)
*       *   [func AddCaller() Option](https://pkg.go.dev/go.uber.org/zap#AddCaller)
    *   [func AddCallerSkip(skip int) Option](https://pkg.go.dev/go.uber.org/zap#AddCallerSkip)
    *   [func AddStacktrace(lvl zapcore.LevelEnabler) Option](https://pkg.go.dev/go.uber.org/zap#AddStacktrace)
    *   [func Development() Option](https://pkg.go.dev/go.uber.org/zap#Development)
    *   [func ErrorOutput(w zapcore.WriteSyncer) Option](https://pkg.go.dev/go.uber.org/zap#ErrorOutput)
    *   [func Fields(fs ...Field) Option](https://pkg.go.dev/go.uber.org/zap#Fields)
    *   [func Hooks(hooks ...func(zapcore.Entry) error) Option](https://pkg.go.dev/go.uber.org/zap#Hooks)
    *   [func IncreaseLevel(lvl zapcore.LevelEnabler) Option](https://pkg.go.dev/go.uber.org/zap#IncreaseLevel)
    *   [func OnFatal(action zapcore.CheckWriteAction) Option](https://pkg.go.dev/go.uber.org/zap#OnFatal)deprecated
    *   [func WithCaller(enabled bool) Option](https://pkg.go.dev/go.uber.org/zap#WithCaller)
    *   [func WithClock(clock zapcore.Clock) Option](https://pkg.go.dev/go.uber.org/zap#WithClock)
    *   [func WithFatalHook(hook zapcore.CheckWriteHook) Option](https://pkg.go.dev/go.uber.org/zap#WithFatalHook)
    *   [func WithPanicHook(hook zapcore.CheckWriteHook) Option](https://pkg.go.dev/go.uber.org/zap#WithPanicHook)
    *   [func WrapCore(f func(zapcore.Core) zapcore.Core) Option](https://pkg.go.dev/go.uber.org/zap#WrapCore)

*   [type SamplingConfig](https://pkg.go.dev/go.uber.org/zap#SamplingConfig)
*   [type Sink](https://pkg.go.dev/go.uber.org/zap#Sink)
*   [type SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)
*       *   [func S() *SugaredLogger](https://pkg.go.dev/go.uber.org/zap#S)

*       *   [func (s *SugaredLogger) DPanic(args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.DPanic)
    *   [func (s *SugaredLogger) DPanicf(template string, args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.DPanicf)
    *   [func (s *SugaredLogger) DPanicln(args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.DPanicln)
    *   [func (s *SugaredLogger) DPanicw(msg string, keysAndValues ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.DPanicw)
    *   [func (s *SugaredLogger) Debug(args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Debug)
    *   [func (s *SugaredLogger) Debugf(template string, args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Debugf)
    *   [func (s *SugaredLogger) Debugln(args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Debugln)
    *   [func (s *SugaredLogger) Debugw(msg string, keysAndValues ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Debugw)
    *   [func (s *SugaredLogger) Desugar() *Logger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Desugar)
    *   [func (s *SugaredLogger) Error(args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Error)
    *   [func (s *SugaredLogger) Errorf(template string, args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Errorf)
    *   [func (s *SugaredLogger) Errorln(args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Errorln)
    *   [func (s *SugaredLogger) Errorw(msg string, keysAndValues ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Errorw)
    *   [func (s *SugaredLogger) Fatal(args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Fatal)
    *   [func (s *SugaredLogger) Fatalf(template string, args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Fatalf)
    *   [func (s *SugaredLogger) Fatalln(args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Fatalln)
    *   [func (s *SugaredLogger) Fatalw(msg string, keysAndValues ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Fatalw)
    *   [func (s *SugaredLogger) Info(args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Info)
    *   [func (s *SugaredLogger) Infof(template string, args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Infof)
    *   [func (s *SugaredLogger) Infoln(args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Infoln)
    *   [func (s *SugaredLogger) Infow(msg string, keysAndValues ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Infow)
    *   [func (s *SugaredLogger) Level() zapcore.Level](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Level)
    *   [func (s *SugaredLogger) Log(lvl zapcore.Level, args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Log)
    *   [func (s *SugaredLogger) Logf(lvl zapcore.Level, template string, args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Logf)
    *   [func (s *SugaredLogger) Logln(lvl zapcore.Level, args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Logln)
    *   [func (s *SugaredLogger) Logw(lvl zapcore.Level, msg string, keysAndValues ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Logw)
    *   [func (s *SugaredLogger) Named(name string) *SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Named)
    *   [func (s *SugaredLogger) Panic(args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Panic)
    *   [func (s *SugaredLogger) Panicf(template string, args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Panicf)
    *   [func (s *SugaredLogger) Panicln(args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Panicln)
    *   [func (s *SugaredLogger) Panicw(msg string, keysAndValues ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Panicw)
    *   [func (s *SugaredLogger) Sync() error](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Sync)
    *   [func (s *SugaredLogger) Warn(args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Warn)
    *   [func (s *SugaredLogger) Warnf(template string, args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Warnf)
    *   [func (s *SugaredLogger) Warnln(args ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Warnln)
    *   [func (s *SugaredLogger) Warnw(msg string, keysAndValues ...interface{})](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.Warnw)
    *   [func (s *SugaredLogger) With(args ...interface{}) *SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.With)
    *   [func (s *SugaredLogger) WithLazy(args ...interface{}) *SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.WithLazy)
    *   [func (s *SugaredLogger) WithOptions(opts ...Option) *SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger.WithOptions)

*   [Package (AdvancedConfiguration)](https://pkg.go.dev/go.uber.org/zap#example-package-AdvancedConfiguration)
*   [Package (BasicConfiguration)](https://pkg.go.dev/go.uber.org/zap#example-package-BasicConfiguration)
*   [Package (Presets)](https://pkg.go.dev/go.uber.org/zap#example-package-Presets)
*   [AtomicLevel](https://pkg.go.dev/go.uber.org/zap#example-AtomicLevel)
*   [AtomicLevel (Config)](https://pkg.go.dev/go.uber.org/zap#example-AtomicLevel-Config)
*   [Dict](https://pkg.go.dev/go.uber.org/zap#example-Dict)
*   [DictObject](https://pkg.go.dev/go.uber.org/zap#example-DictObject)
*   [Logger.Check](https://pkg.go.dev/go.uber.org/zap#example-Logger.Check)
*   [Logger.Named](https://pkg.go.dev/go.uber.org/zap#example-Logger.Named)
*   [Namespace](https://pkg.go.dev/go.uber.org/zap#example-Namespace)
*   [NewStdLog](https://pkg.go.dev/go.uber.org/zap#example-NewStdLog)
*   [Object](https://pkg.go.dev/go.uber.org/zap#example-Object)
*   [ObjectValues](https://pkg.go.dev/go.uber.org/zap#example-ObjectValues)
*   [Objects](https://pkg.go.dev/go.uber.org/zap#example-Objects)
*   [RedirectStdLog](https://pkg.go.dev/go.uber.org/zap#example-RedirectStdLog)
*   [ReplaceGlobals](https://pkg.go.dev/go.uber.org/zap#example-ReplaceGlobals)
*   [WrapCore (Replace)](https://pkg.go.dev/go.uber.org/zap#example-WrapCore-Replace)
*   [WrapCore (Wrap)](https://pkg.go.dev/go.uber.org/zap#example-WrapCore-Wrap)

This section is empty.

CombineWriteSyncers is a utility that combines multiple WriteSyncers into a single, locked WriteSyncer. If no inputs are supplied, it returns a no-op WriteSyncer.

It's provided purely as a convenience; the result is no different from using zapcore.NewMultiWriteSyncer and zapcore.Lock individually.

DictObject constructs a [zapcore.ObjectMarshaler](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#ObjectMarshaler) with the given list of fields. The resulting object marshaler can be used as input to [Object](https://pkg.go.dev/go.uber.org/zap#Object), [Objects](https://pkg.go.dev/go.uber.org/zap#Objects), or any other functions that expect an object marshaler.

Output:

{"level":"debug","msg":"worker received job","w1":{"id":402000,"description":"compress image data","priority":3}} {"level":"info","msg":"worker status checks","job batch enqueued":[{"worker":"w1","load":419,"latency":"68ms"},{"worker":"w2","load":520,"latency":"79ms"},{"worker":"w3","load":310,"latency":"57ms"}]} 

LevelFlag uses the standard library's flag.Var to declare a global flag with the specified name, default, and usage guidance. The returned value is a pointer to the value of the flag.

If you don't want to use the flag package's global state, you can use any non-nil *Level as a flag.Value with your own *flag.FlagSet.

NewDevelopmentEncoderConfig returns an opinionated EncoderConfig for development environments.

Messages encoded with this configuration will use Zap's console encoder intended to print human-readable output. It will print log messages with the following information:

*   The log level (e.g. "INFO", "ERROR").
*   The time in ISO8601 format (e.g. "2017-01-01T12:00:00Z").
*   The message passed to the log statement.
*   If available, a short path to the file and line number where the log statement was issued. The logger configuration determines whether this field is captured.
*   If available, a stacktrace from the line where the log statement was issued. The logger configuration determines whether this field is captured.

By default, the following formats are used for different types:

*   Time is formatted in ISO8601 format (e.g. "2017-01-01T12:00:00Z").
*   Duration is formatted as a string (e.g. "1.234s").

You may change these by setting the appropriate fields in the returned object. For example, use the following to change the time encoding format:

cfg := zap.NewDevelopmentEncoderConfig()
cfg.EncodeTime = zapcore.ISO8601TimeEncoder

NewProductionEncoderConfig returns an opinionated EncoderConfig for production environments.

Messages encoded with this configuration will be JSON-formatted and will have the following keys by default:

*   "level": The logging level (e.g. "info", "error").
*   "ts": The current time in number of seconds since the Unix epoch.
*   "msg": The message passed to the log statement.
*   "caller": If available, a short path to the file and line number where the log statement was issued. The logger configuration determines whether this field is captured.
*   "stacktrace": If available, a stack trace from the line where the log statement was issued. The logger configuration determines whether this field is captured.

By default, the following formats are used for different types:

*   Time is formatted as floating-point number of seconds since the Unix epoch.
*   Duration is formatted as floating-point number of seconds.

You may change these by setting the appropriate fields in the returned object. For example, use the following to change the time encoding format:

cfg := zap.NewProductionEncoderConfig()
cfg.EncodeTime = zapcore.ISO8601TimeEncoder

NewStdLog returns a *log.Logger which writes to the supplied zap Logger at InfoLevel. To redirect the standard library's package-global logging functions, use RedirectStdLog instead.

Output:

{"level":"info","msg":"standard logger wrapper"} 

NewStdLogAt returns *log.Logger which writes to supplied zap logger at required level.

Open is a high-level wrapper that takes a variadic number of URLs, opens or creates each of the specified resources, and combines them into a locked WriteSyncer. It also returns any error encountered and a function to close any opened files.

Passing no URLs returns a no-op WriteSyncer. Zap handles URLs without a scheme and URLs with the "file" scheme. Third-party code may register factories for other schemes using RegisterSink.

URLs with the "file" scheme must use absolute paths on the local filesystem. No user, password, port, fragments, or query parameters are allowed, and the hostname must be empty or "localhost".

Since it's common to write logs to the local filesystem, URLs without a scheme (e.g., "/var/log/foo.log") are treated as local file paths. Without a scheme, the special paths "stdout" and "stderr" are interpreted as os.Stdout and os.Stderr. When specified without a scheme, relative file paths also work.

func RedirectStdLog(l *[Logger](https://pkg.go.dev/go.uber.org/zap#Logger)) func()

RedirectStdLog redirects output from the standard library's package-global logger to the supplied logger at InfoLevel. Since zap already handles caller annotations, timestamps, etc., it automatically disables the standard library's annotations and prefixing.

It returns a function to restore the original prefix and flags and reset the standard library's output to os.Stderr.

Output:

{"level":"info","msg":"redirected standard library"} 

RedirectStdLogAt redirects output from the standard library's package-global logger to the supplied logger at the specified level. Since zap already handles caller annotations, timestamps, etc., it automatically disables the standard library's annotations and prefixing.

It returns a function to restore the original prefix and flags and reset the standard library's output to os.Stderr.

RegisterEncoder registers an encoder constructor, which the Config struct can then reference. By default, the "json" and "console" encoders are registered.

Attempting to register an encoder whose name is already taken returns an error.

RegisterSink registers a user-supplied factory for all sinks with a particular scheme.

All schemes must be ASCII, valid under section 0.1 of [RFC 3986](https://rfc-editor.org/rfc/rfc3986.html) ([https://tools.ietf.org/html/rfc3983#section-3.1](https://tools.ietf.org/html/rfc3983#section-3.1)), and must not already have a factory registered. Zap automatically registers a factory for the "file" scheme.

func ReplaceGlobals(logger *[Logger](https://pkg.go.dev/go.uber.org/zap#Logger)) func()

ReplaceGlobals replaces the global Logger and SugaredLogger, and returns a function to restore the original values. It's safe for concurrent use.

Output:

{"level":"info","msg":"replaced zap's global loggers"} 

type AtomicLevel struct {
	
}

An AtomicLevel is an atomically changeable, dynamic logging level. It lets you safely change the log level of a tree of loggers (the root logger and any children created by adding context) at runtime.

The AtomicLevel itself is an http.Handler that serves a JSON endpoint to alter its level.

AtomicLevels must be created with the NewAtomicLevel constructor to allocate their internal atomic pointer.

Output:

{"level":"info","msg":"info logging enabled"} 

Output:

{"level":"info","message":"info logging enabled"} 

func NewAtomicLevel() [AtomicLevel](https://pkg.go.dev/go.uber.org/zap#AtomicLevel)

NewAtomicLevel creates an AtomicLevel with InfoLevel and above logging enabled.

NewAtomicLevelAt is a convenience function that creates an AtomicLevel and then calls SetLevel with the given level.

ParseAtomicLevel parses an AtomicLevel based on a lowercase or all-caps ASCII representation of the log level. If the provided ASCII representation is invalid an error is returned.

This is particularly useful when dealing with text input to configure log levels.

Enabled implements the zapcore.LevelEnabler interface, which allows the AtomicLevel to be used in place of traditional static levels.

Level returns the minimum enabled log level.

MarshalText marshals the AtomicLevel to a byte slice. It uses the same text representation as the static zapcore.Levels ("debug", "info", "warn", "error", "dpanic", "panic", and "fatal").

ServeHTTP is a simple JSON endpoint that can report on or change the current logging level.

#### GET [¶](https://pkg.go.dev/go.uber.org/zap#hdr-GET-AtomicLevel_ServeHTTP "Go to GET")

The GET request returns a JSON description of the current logging level like:

{"level":"info"}

#### PUT [¶](https://pkg.go.dev/go.uber.org/zap#hdr-PUT-AtomicLevel_ServeHTTP "Go to PUT")

The PUT request changes the logging level. It is perfectly safe to change the logging level while a program is running. Two content types are supported:

Content-Type: application/x-www-form-urlencoded

With this content type, the level can be provided through the request body or a query parameter. The log level is URL encoded like:

level=debug

The request body takes precedence over the query parameter, if both are specified.

This content type is the default for a curl PUT request. Following are two example curl requests that both set the logging level to debug.

curl -X PUT localhost:8080/log/level?level=debug
curl -X PUT localhost:8080/log/level -d level=debug

For any other content type, the payload is expected to be JSON encoded and look like:

{"level":"info"}

An example curl request could look like this:

curl -X PUT localhost:8080/log/level -H "Content-Type: application/json" -d '{"level":"debug"}'

SetLevel alters the logging level.

String returns the string representation of the underlying Level.

UnmarshalText unmarshals the text to an AtomicLevel. It uses the same text representations as the static zapcore.Levels ("debug", "info", "warn", "error", "dpanic", "panic", and "fatal").

type Config struct {
	
	
	Level [AtomicLevel](https://pkg.go.dev/go.uber.org/zap#AtomicLevel) `json:"level" yaml:"level"`
	
	Development [bool](https://pkg.go.dev/builtin#bool) `json:"development" yaml:"development"`
	
	DisableCaller [bool](https://pkg.go.dev/builtin#bool) `json:"disableCaller" yaml:"disableCaller"`
	
	
	DisableStacktrace [bool](https://pkg.go.dev/builtin#bool) `json:"disableStacktrace" yaml:"disableStacktrace"`
	Sampling *[SamplingConfig](https://pkg.go.dev/go.uber.org/zap#SamplingConfig) `json:"sampling" yaml:"sampling"`
	
	
	Encoding [string](https://pkg.go.dev/builtin#string) `json:"encoding" yaml:"encoding"`
	
	EncoderConfig [zapcore](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore).[EncoderConfig](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#EncoderConfig) `json:"encoderConfig" yaml:"encoderConfig"`
	
	OutputPaths [][string](https://pkg.go.dev/builtin#string) `json:"outputPaths" yaml:"outputPaths"`
	
	
	
	
	
	ErrorOutputPaths [][string](https://pkg.go.dev/builtin#string) `json:"errorOutputPaths" yaml:"errorOutputPaths"`
	InitialFields map[[string](https://pkg.go.dev/builtin#string)]interface{} `json:"initialFields" yaml:"initialFields"`
}

Config offers a declarative way to construct a logger. It doesn't do anything that can't be done with New, Options, and the various zapcore.WriteSyncer and zapcore.Core wrappers, but it's a simpler way to toggle common options.

Note that Config intentionally supports only the most common options. More unusual logging setups (logging to network connections or message queues, splitting output between multiple files, etc.) are possible, but require direct use of the zapcore package. For sample code, see the package-level BasicConfiguration and AdvancedConfiguration examples.

For an example showing runtime log level changes, see the documentation for AtomicLevel.

func NewDevelopmentConfig() [Config](https://pkg.go.dev/go.uber.org/zap#Config)

NewDevelopmentConfig builds a reasonable default development logging configuration. Logging is enabled at DebugLevel and above, and uses a console encoder. Logs are written to standard error. Stacktraces are included on logs of WarnLevel and above. DPanicLevel logs will panic.

See [NewDevelopmentEncoderConfig](https://pkg.go.dev/go.uber.org/zap#NewDevelopmentEncoderConfig) for information on the default encoder configuration.

func NewProductionConfig() [Config](https://pkg.go.dev/go.uber.org/zap#Config)

NewProductionConfig builds a reasonable default production logging configuration. Logging is enabled at InfoLevel and above, and uses a JSON encoder. Logs are written to standard error. Stacktraces are included on logs of ErrorLevel and above. DPanicLevel logs will not panic, but will write a stacktrace.

Sampling is enabled at 100:100 by default, meaning that after the first 100 log entries with the same level and message in the same second, it will log every 100th entry with the same level and message in the same second. You may disable this behavior by setting Sampling to nil.

See [NewProductionEncoderConfig](https://pkg.go.dev/go.uber.org/zap#NewProductionEncoderConfig) for information on the default encoder configuration.

func (cfg [Config](https://pkg.go.dev/go.uber.org/zap#Config)) Build(opts ...[Option](https://pkg.go.dev/go.uber.org/zap#Option)) (*[Logger](https://pkg.go.dev/go.uber.org/zap#Logger), [error](https://pkg.go.dev/builtin#error))

Build constructs a logger from the Config and Options.

Field is an alias for Field. Aliasing this type dramatically improves the navigability of this package's API documentation.

func Any(key [string](https://pkg.go.dev/builtin#string), value interface{}) [Field](https://pkg.go.dev/go.uber.org/zap#Field)

Any takes a key and an arbitrary value and chooses the best way to represent them as a field, falling back to a reflection-based approach only if necessary.

Since byte/uint8 and rune/int32 are aliases, Any can't differentiate between them. To minimize surprises, []byte values are treated as binary blobs, byte values are treated as uint8, and runes are always treated as integers.

Array constructs a field with the given key and ArrayMarshaler. It provides a flexible, but still type-safe and efficient, way to add array-like types to the logging context. The struct's MarshalLogArray method is called lazily.

Binary constructs a field that carries an opaque binary blob.

Binary data is serialized in an encoding-appropriate format. For example, zap's JSON encoder base64-encodes binary blobs. To log UTF-8 encoded text, use ByteString.

Bool constructs a field that carries a bool.

Boolp constructs a field that carries a *bool. The returned Field will safely and explicitly represent `nil` when appropriate.

Bools constructs a field that carries a slice of bools.

ByteString constructs a field that carries UTF-8 encoded text as a []byte. To log opaque binary blobs (which aren't necessarily valid UTF-8), use Binary.

ByteStrings constructs a field that carries a slice of []byte, each of which must be UTF-8 encoded text.

Complex64 constructs a field that carries a complex number. Unlike most numeric fields, this costs an allocation (to convert the complex64 to interface{}).

Complex64p constructs a field that carries a *complex64. The returned Field will safely and explicitly represent `nil` when appropriate.

Complex64s constructs a field that carries a slice of complex numbers.

Complex128 constructs a field that carries a complex number. Unlike most numeric fields, this costs an allocation (to convert the complex128 to interface{}).

Complex128p constructs a field that carries a *complex128. The returned Field will safely and explicitly represent `nil` when appropriate.

Complex128s constructs a field that carries a slice of complex numbers.

Dict constructs a field containing the provided key-value pairs. It acts similar to [Object](https://pkg.go.dev/go.uber.org/zap#Object), but with the fields specified as arguments.

Output:

{"level":"info","msg":"login event","event":{"id":123,"name":"jane","status":"pending"}} 

Duration constructs a field with the given key and value. The encoder controls how the duration is serialized.

Durationp constructs a field that carries a *time.Duration. The returned Field will safely and explicitly represent `nil` when appropriate.

Durations constructs a field that carries a slice of time.Durations.

Error is shorthand for the common idiom NamedError("error", err).

Errors constructs a field that carries a slice of errors.

Float32 constructs a field that carries a float32. The way the floating-point value is represented is encoder-dependent, so marshaling is necessarily lazy.

Float32p constructs a field that carries a *float32. The returned Field will safely and explicitly represent `nil` when appropriate.

Float32s constructs a field that carries a slice of floats.

Float64 constructs a field that carries a float64. The way the floating-point value is represented is encoder-dependent, so marshaling is necessarily lazy.

Float64p constructs a field that carries a *float64. The returned Field will safely and explicitly represent `nil` when appropriate.

Float64s constructs a field that carries a slice of floats.

Inline constructs a Field that is similar to Object, but it will add the elements of the provided ObjectMarshaler to the current namespace.

Int constructs a field with the given key and value.

Int8 constructs a field with the given key and value.

Int8p constructs a field that carries a *int8. The returned Field will safely and explicitly represent `nil` when appropriate.

Int8s constructs a field that carries a slice of integers.

Int16 constructs a field with the given key and value.

Int16p constructs a field that carries a *int16. The returned Field will safely and explicitly represent `nil` when appropriate.

Int16s constructs a field that carries a slice of integers.

Int32 constructs a field with the given key and value.

Int32p constructs a field that carries a *int32. The returned Field will safely and explicitly represent `nil` when appropriate.

Int32s constructs a field that carries a slice of integers.

Int64 constructs a field with the given key and value.

Int64p constructs a field that carries a *int64. The returned Field will safely and explicitly represent `nil` when appropriate.

Int64s constructs a field that carries a slice of integers.

Intp constructs a field that carries a *int. The returned Field will safely and explicitly represent `nil` when appropriate.

Ints constructs a field that carries a slice of integers.

NamedError constructs a field that lazily stores err.Error() under the provided key. Errors which also implement fmt.Formatter (like those produced by github.com/pkg/errors) will also have their verbose representation stored under key+"Verbose". If passed a nil error, the field is a no-op.

For the common case in which the key is simply "error", the Error function is shorter and less repetitive.

Namespace creates a named, isolated scope within the logger's context. All subsequent fields will be added to the new namespace.

This helps prevent key collisions when injecting loggers into sub-components or third-party libraries.

Output:

{"level":"info","msg":"tracked some metrics","metrics":{"counter":1}} 

Object constructs a field with the given key and ObjectMarshaler. It provides a flexible, but still type-safe and efficient, way to add map- or struct-like user-defined types to the logging context. The struct's MarshalLogObject method is called lazily.

Output:

{"level":"info","msg":"new request, in nested object","req":{"url":"/test","ip":"127.0.0.1","port":8080,"remote":{"ip":"127.0.0.1","port":31200}}} {"level":"info","msg":"new request, inline","url":"/test","ip":"127.0.0.1","port":8080,"remote":{"ip":"127.0.0.1","port":31200}} 

ObjectValues constructs a field with the given key, holding a list of the provided objects, where pointers to these objects can be marshaled by Zap.

Note that pointers to these objects must implement zapcore.ObjectMarshaler. That is, if you're trying to marshal a []Request, the MarshalLogObject method must be declared on the *Request type, not the value (Request). If it's on the value, use Objects.

Given an object that implements MarshalLogObject on the pointer receiver, you can log a slice of those objects with ObjectValues like so:

type Request struct{ ... }
func (r *Request) MarshalLogObject(enc zapcore.ObjectEncoder) error

var requests []Request = ...
logger.Info("sending requests", zap.ObjectValues("requests", requests))

If instead, you have a slice of pointers of such an object, use the Objects field constructor.

var requests []*Request = ...
logger.Info("sending requests", zap.Objects("requests", requests))

Output:

{"level":"debug","msg":"starting tunnels","addrs":[{"url":"/foo","ip":"127.0.0.1","port":8080,"remote":{"ip":"123.45.67.89","port":4040}},{"url":"/bar","ip":"127.0.0.1","port":8080,"remote":{"ip":"127.0.0.1","port":31200}}]} 

Objects constructs a field with the given key, holding a list of the provided objects that can be marshaled by Zap.

Note that these objects must implement zapcore.ObjectMarshaler directly. That is, if you're trying to marshal a []Request, the MarshalLogObject method must be declared on the Request type, not its pointer (*Request). If it's on the pointer, use ObjectValues.

Given an object that implements MarshalLogObject on the value receiver, you can log a slice of those objects with Objects like so:

type Author struct{ ... }
func (a Author) MarshalLogObject(enc zapcore.ObjectEncoder) error

var authors []Author = ...
logger.Info("loading article", zap.Objects("authors", authors))

Similarly, given a type that implements MarshalLogObject on its pointer receiver, you can log a slice of pointers to that object with Objects like so:

type Request struct{ ... }
func (r *Request) MarshalLogObject(enc zapcore.ObjectEncoder) error

var requests []*Request = ...
logger.Info("sending requests", zap.Objects("requests", requests))

If instead, you have a slice of values of such an object, use the ObjectValues constructor.

var requests []Request = ...
logger.Info("sending requests", zap.ObjectValues("requests", requests))

Output:

{"level":"debug","msg":"opening connections","addrs":[{"ip":"123.45.67.89","port":4040},{"ip":"127.0.0.1","port":4041},{"ip":"192.168.0.1","port":4042}]} 

func Reflect(key [string](https://pkg.go.dev/builtin#string), val interface{}) [Field](https://pkg.go.dev/go.uber.org/zap#Field)

Reflect constructs a field with the given key and an arbitrary object. It uses an encoding-appropriate, reflection-based function to lazily serialize nearly any object into the logging context, but it's relatively slow and allocation-heavy. Outside tests, Any is always a better choice.

If encoding fails (e.g., trying to serialize a map[int]string to JSON), Reflect includes the error message in the final log output.

Skip constructs a no-op field, which is often useful when handling invalid inputs in other Field constructors.

Stack constructs a field that stores a stacktrace of the current goroutine under provided key. Keep in mind that taking a stacktrace is eager and expensive (relatively speaking); this function both makes an allocation and takes about two microseconds.

StackSkip constructs a field similarly to Stack, but also skips the given number of frames from the top of the stacktrace.

String constructs a field with the given key and value.

Stringer constructs a field with the given key and the output of the value's String method. The Stringer's String method is called lazily.

Stringers constructs a field with the given key, holding a list of the output provided by the value's String method

Given an object that implements String on the value receiver, you can log a slice of those objects with Objects like so:

type Request struct{ ... }
func (a Request) String() string

var requests []Request = ...
logger.Info("sending requests", zap.Stringers("requests", requests))

Note that these objects must implement fmt.Stringer directly. That is, if you're trying to marshal a []Request, the String method must be declared on the Request type, not its pointer (*Request).

Stringp constructs a field that carries a *string. The returned Field will safely and explicitly represent `nil` when appropriate.

Strings constructs a field that carries a slice of strings.

Time constructs a Field with the given key and value. The encoder controls how the time is serialized.

Timep constructs a field that carries a *time.Time. The returned Field will safely and explicitly represent `nil` when appropriate.

Times constructs a field that carries a slice of time.Times.

Uint constructs a field with the given key and value.

Uint8 constructs a field with the given key and value.

Uint8p constructs a field that carries a *uint8. The returned Field will safely and explicitly represent `nil` when appropriate.

Uint8s constructs a field that carries a slice of unsigned integers.

Uint16 constructs a field with the given key and value.

Uint16p constructs a field that carries a *uint16. The returned Field will safely and explicitly represent `nil` when appropriate.

Uint16s constructs a field that carries a slice of unsigned integers.

Uint32 constructs a field with the given key and value.

Uint32p constructs a field that carries a *uint32. The returned Field will safely and explicitly represent `nil` when appropriate.

Uint32s constructs a field that carries a slice of unsigned integers.

Uint64 constructs a field with the given key and value.

Uint64p constructs a field that carries a *uint64. The returned Field will safely and explicitly represent `nil` when appropriate.

Uint64s constructs a field that carries a slice of unsigned integers.

Uintp constructs a field that carries a *uint. The returned Field will safely and explicitly represent `nil` when appropriate.

Uintptr constructs a field with the given key and value.

Uintptrp constructs a field that carries a *uintptr. The returned Field will safely and explicitly represent `nil` when appropriate.

Uintptrs constructs a field that carries a slice of pointer addresses.

Uints constructs a field that carries a slice of unsigned integers.

LevelEnablerFunc is a convenient way to implement zapcore.LevelEnabler with an anonymous function.

It's particularly useful when splitting log output between different outputs (e.g., standard error and standard out). For sample code, see the package-level AdvancedConfiguration example.

Enabled calls the wrapped function.

type Logger struct {
	
}

A Logger provides fast, leveled, structured logging. All methods are safe for concurrent use.

The Logger is designed for contexts in which every microsecond and every allocation matters, so its API intentionally favors performance and type safety over brevity. For most applications, the SugaredLogger strikes a better balance between performance and ergonomics.

L returns the global Logger, which can be reconfigured with ReplaceGlobals. It's safe for concurrent use.

func Must(logger *[Logger](https://pkg.go.dev/go.uber.org/zap#Logger), err [error](https://pkg.go.dev/builtin#error)) *[Logger](https://pkg.go.dev/go.uber.org/zap#Logger)

Must is a helper that wraps a call to a function returning (*Logger, error) and panics if the error is non-nil. It is intended for use in variable initialization such as:

var logger = zap.Must(zap.NewProduction())

New constructs a new Logger from the provided zapcore.Core and Options. If the passed zapcore.Core is nil, it falls back to using a no-op implementation.

This is the most flexible way to construct a Logger, but also the most verbose. For typical use cases, the highly-opinionated presets (NewProduction, NewDevelopment, and NewExample) or the Config struct are more convenient.

For sample code, see the package-level AdvancedConfiguration example.

func NewDevelopment(options ...[Option](https://pkg.go.dev/go.uber.org/zap#Option)) (*[Logger](https://pkg.go.dev/go.uber.org/zap#Logger), [error](https://pkg.go.dev/builtin#error))

NewDevelopment builds a development Logger that writes DebugLevel and above logs to standard error in a human-friendly format.

It's a shortcut for NewDevelopmentConfig().Build(...Option).

func NewExample(options ...[Option](https://pkg.go.dev/go.uber.org/zap#Option)) *[Logger](https://pkg.go.dev/go.uber.org/zap#Logger)

NewExample builds a Logger that's designed for use in zap's testable examples. It writes DebugLevel and above logs to standard out as JSON, but omits the timestamp and calling function to keep example output short and deterministic.

NewNop returns a no-op Logger. It never writes out logs or internal errors, and it never runs user-defined hooks.

Using WithOptions to replace the Core or error output of a no-op Logger can re-enable logging.

func NewProduction(options ...[Option](https://pkg.go.dev/go.uber.org/zap#Option)) (*[Logger](https://pkg.go.dev/go.uber.org/zap#Logger), [error](https://pkg.go.dev/builtin#error))

NewProduction builds a sensible production Logger that writes InfoLevel and above logs to standard error as JSON.

It's a shortcut for NewProductionConfig().Build(...Option).

Check returns a CheckedEntry if logging a message at the specified level is enabled. It's a completely optional optimization; in high-performance applications, Check can help avoid allocating a slice to hold fields.

Output:

{"level":"debug","msg":"debugging","foo":"bar","baz":"quux"} 

Core returns the Logger's underlying zapcore.Core.

func (log *[Logger](https://pkg.go.dev/go.uber.org/zap#Logger)) DPanic(msg [string](https://pkg.go.dev/builtin#string), fields ...[Field](https://pkg.go.dev/go.uber.org/zap#Field))

DPanic logs a message at DPanicLevel. The message includes any fields passed at the log site, as well as any fields accumulated on the logger.

If the logger is in development mode, it then panics (DPanic means "development panic"). This is useful for catching errors that are recoverable, but shouldn't ever happen.

func (log *[Logger](https://pkg.go.dev/go.uber.org/zap#Logger)) Debug(msg [string](https://pkg.go.dev/builtin#string), fields ...[Field](https://pkg.go.dev/go.uber.org/zap#Field))

Debug logs a message at DebugLevel. The message includes any fields passed at the log site, as well as any fields accumulated on the logger.

func (log *[Logger](https://pkg.go.dev/go.uber.org/zap#Logger)) Error(msg [string](https://pkg.go.dev/builtin#string), fields ...[Field](https://pkg.go.dev/go.uber.org/zap#Field))

Error logs a message at ErrorLevel. The message includes any fields passed at the log site, as well as any fields accumulated on the logger.

func (log *[Logger](https://pkg.go.dev/go.uber.org/zap#Logger)) Fatal(msg [string](https://pkg.go.dev/builtin#string), fields ...[Field](https://pkg.go.dev/go.uber.org/zap#Field))

Fatal logs a message at FatalLevel. The message includes any fields passed at the log site, as well as any fields accumulated on the logger.

The logger then calls os.Exit(1), even if logging at FatalLevel is disabled.

func (log *[Logger](https://pkg.go.dev/go.uber.org/zap#Logger)) Info(msg [string](https://pkg.go.dev/builtin#string), fields ...[Field](https://pkg.go.dev/go.uber.org/zap#Field))

Info logs a message at InfoLevel. The message includes any fields passed at the log site, as well as any fields accumulated on the logger.

Level reports the minimum enabled level for this logger.

For NopLoggers, this is [zapcore.InvalidLevel](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#InvalidLevel).

Log logs a message at the specified level. The message includes any fields passed at the log site, as well as any fields accumulated on the logger. Any Fields that require evaluation (such as Objects) are evaluated upon invocation of Log.

Name returns the Logger's underlying name, or an empty string if the logger is unnamed.

Named adds a new path segment to the logger's name. Segments are joined by periods. By default, Loggers are unnamed.

Output:

{"level":"info","msg":"no name"} {"level":"info","logger":"main","msg":"main logger"} {"level":"info","logger":"main.subpackage","msg":"sub-logger"} 

func (log *[Logger](https://pkg.go.dev/go.uber.org/zap#Logger)) Panic(msg [string](https://pkg.go.dev/builtin#string), fields ...[Field](https://pkg.go.dev/go.uber.org/zap#Field))

Panic logs a message at PanicLevel. The message includes any fields passed at the log site, as well as any fields accumulated on the logger.

The logger then panics, even if logging at PanicLevel is disabled.

func (log *[Logger](https://pkg.go.dev/go.uber.org/zap#Logger)) Sugar() *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)

Sugar wraps the Logger to provide a more ergonomic, but slightly slower, API. Sugaring a Logger is quite inexpensive, so it's reasonable for a single application to use both Loggers and SugaredLoggers, converting between them on the boundaries of performance-sensitive code.

Sync calls the underlying Core's Sync method, flushing any buffered log entries. Applications should take care to call Sync before exiting.

func (log *[Logger](https://pkg.go.dev/go.uber.org/zap#Logger)) Warn(msg [string](https://pkg.go.dev/builtin#string), fields ...[Field](https://pkg.go.dev/go.uber.org/zap#Field))

Warn logs a message at WarnLevel. The message includes any fields passed at the log site, as well as any fields accumulated on the logger.

func (log *[Logger](https://pkg.go.dev/go.uber.org/zap#Logger)) With(fields ...[Field](https://pkg.go.dev/go.uber.org/zap#Field)) *[Logger](https://pkg.go.dev/go.uber.org/zap#Logger)

With creates a child logger and adds structured context to it. Fields added to the child don't affect the parent, and vice versa. Any fields that require evaluation (such as Objects) are evaluated upon invocation of With.

func (log *[Logger](https://pkg.go.dev/go.uber.org/zap#Logger)) WithLazy(fields ...[Field](https://pkg.go.dev/go.uber.org/zap#Field)) *[Logger](https://pkg.go.dev/go.uber.org/zap#Logger)

WithLazy creates a child logger and adds structured context to it lazily.

The fields are evaluated only if the logger is further chained with [With] or is written to with any of the log level methods. Until that occurs, the logger may retain references to objects inside the fields, and logging will reflect the state of an object at the time of logging, not the time of WithLazy().

WithLazy provides a worthwhile performance optimization for contextual loggers when the likelihood of using the child logger is low, such as error paths and rarely taken branches.

Similar to [With], fields added to the child don't affect the parent, and vice versa.

func (log *[Logger](https://pkg.go.dev/go.uber.org/zap#Logger)) WithOptions(opts ...[Option](https://pkg.go.dev/go.uber.org/zap#Option)) *[Logger](https://pkg.go.dev/go.uber.org/zap#Logger)

WithOptions clones the current Logger, applies the supplied Options, and returns the resulting Logger. It's safe to use concurrently.

ObjectMarshalerPtr is a constraint that specifies that the given type implements zapcore.ObjectMarshaler on a pointer receiver.

type Option interface {
	
}

An Option configures a Logger.

AddCaller configures the Logger to annotate each message with the filename, line number, and function name of zap's caller. See also WithCaller.

func AddCallerSkip(skip [int](https://pkg.go.dev/builtin#int)) [Option](https://pkg.go.dev/go.uber.org/zap#Option)

AddCallerSkip increases the number of callers skipped by caller annotation (as enabled by the AddCaller option). When building wrappers around the Logger and SugaredLogger, supplying this Option prevents zap from always reporting the wrapper code as the caller.

AddStacktrace configures the Logger to record a stack trace for all messages at or above a given level.

func Development() [Option](https://pkg.go.dev/go.uber.org/zap#Option)

Development puts the logger in development mode, which makes DPanic-level logs panic instead of simply logging an error.

ErrorOutput sets the destination for errors generated by the Logger. Note that this option only affects internal errors; for sample code that sends error-level logs to a different location from info- and debug-level logs, see the package-level AdvancedConfiguration example.

The supplied WriteSyncer must be safe for concurrent use. The Open and zapcore.Lock functions are the simplest ways to protect files with a mutex.

func Fields(fs ...[Field](https://pkg.go.dev/go.uber.org/zap#Field)) [Option](https://pkg.go.dev/go.uber.org/zap#Option)

Fields adds fields to the Logger.

Hooks registers functions which will be called each time the Logger writes out an Entry. Repeated use of Hooks is additive.

Hooks are useful for simple side effects, like capturing metrics for the number of emitted logs. More complex side effects, including anything that requires access to the Entry's structured fields, should be implemented as a zapcore.Core instead. See zapcore.RegisterHooks for details.

IncreaseLevel increase the level of the logger. It has no effect if the passed in level tries to decrease the level of the logger.

OnFatal sets the action to take on fatal logs.

Deprecated: Use [WithFatalHook](https://pkg.go.dev/go.uber.org/zap#WithFatalHook) instead.

func WithCaller(enabled [bool](https://pkg.go.dev/builtin#bool)) [Option](https://pkg.go.dev/go.uber.org/zap#Option)

WithCaller configures the Logger to annotate each message with the filename, line number, and function name of zap's caller, or not, depending on the value of enabled. This is a generalized form of AddCaller.

WithClock specifies the clock used by the logger to determine the current time for logged entries. Defaults to the system clock with time.Now.

WithFatalHook sets a CheckWriteHook to run on fatal logs. Zap will call this hook after writing a log statement with a Fatal level.

For example, the following builds a logger that will exit the current goroutine after writing a fatal log message, but it will not exit the program.

zap.New(core, zap.WithFatalHook(zapcore.WriteThenGoexit))

It is important that the provided CheckWriteHook stops the control flow at the current statement to meet expectations of callers of the logger. We recommend calling os.Exit or runtime.Goexit inside custom hooks at minimum.

WithPanicHook sets a CheckWriteHook to run on Panic/DPanic logs. Zap will call this hook after writing a log statement with a Panic/DPanic level.

For example, the following builds a logger that will exit the current goroutine after writing a Panic/DPanic log message, but it will not start a panic.

zap.New(core, zap.WithPanicHook(zapcore.WriteThenGoexit))

This is useful for testing Panic/DPanic log output.

WrapCore wraps or replaces the Logger's underlying zapcore.Core.

Output:

{"level":"info","msg":"working"} {"level":"info","msg":"original logger still works"} 

Output:

{"level":"info","msg":"single"} {"level":"info","msg":"doubled"} {"level":"info","msg":"doubled"} 

SamplingConfig sets a sampling strategy for the logger. Sampling caps the global CPU and I/O load that logging puts on your process while attempting to preserve a representative subset of your logs.

If specified, the Sampler will invoke the Hook after each decision.

Values configured here are per-second. See zapcore.NewSamplerWithOptions for details.

Sink defines the interface to write to and close logger destinations.

type SugaredLogger struct {
	
}

A SugaredLogger wraps the base Logger functionality in a slower, but less verbose, API. Any Logger can be converted to a SugaredLogger with its Sugar method.

Unlike the Logger, the SugaredLogger doesn't insist on structured logging. For each log level, it exposes four methods:

*   methods named after the log level for log.Print-style logging
*   methods ending in "w" for loosely-typed structured logging
*   methods ending in "f" for log.Printf-style logging
*   methods ending in "ln" for log.Println-style logging

For example, the methods for InfoLevel are:

Info(...any)           Print-style logging
Infow(...any)          Structured logging (read as "info with")
Infof(string, ...any)  Printf-style logging
Infoln(...any)         Println-style logging

S returns the global SugaredLogger, which can be reconfigured with ReplaceGlobals. It's safe for concurrent use.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) DPanic(args ...interface{})

DPanic logs the provided arguments at [DPanicLevel](https://pkg.go.dev/go.uber.org/zap#DPanicLevel). In development, the logger then panics. (See [DPanicLevel](https://pkg.go.dev/go.uber.org/zap#DPanicLevel) for details.) Spaces are added between arguments when neither is a string.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) DPanicf(template [string](https://pkg.go.dev/builtin#string), args ...interface{})

DPanicf formats the message according to the format specifier and logs it at [DPanicLevel](https://pkg.go.dev/go.uber.org/zap#DPanicLevel). In development, the logger then panics. (See [DPanicLevel](https://pkg.go.dev/go.uber.org/zap#DPanicLevel) for details.)

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) DPanicln(args ...interface{})

DPanicln logs a message at [DPanicLevel](https://pkg.go.dev/go.uber.org/zap#DPanicLevel). In development, the logger then panics. (See [DPanicLevel](https://pkg.go.dev/go.uber.org/zap#DPanicLevel) for details.) Spaces are always added between arguments.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) DPanicw(msg [string](https://pkg.go.dev/builtin#string), keysAndValues ...interface{})

DPanicw logs a message with some additional context. In development, the logger then panics. (See DPanicLevel for details.) The variadic key-value pairs are treated as they are in With.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Debug(args ...interface{})

Debug logs the provided arguments at [DebugLevel](https://pkg.go.dev/go.uber.org/zap#DebugLevel). Spaces are added between arguments when neither is a string.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Debugf(template [string](https://pkg.go.dev/builtin#string), args ...interface{})

Debugf formats the message according to the format specifier and logs it at [DebugLevel](https://pkg.go.dev/go.uber.org/zap#DebugLevel).

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Debugln(args ...interface{})

Debugln logs a message at [DebugLevel](https://pkg.go.dev/go.uber.org/zap#DebugLevel). Spaces are always added between arguments.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Debugw(msg [string](https://pkg.go.dev/builtin#string), keysAndValues ...interface{})

Debugw logs a message with some additional context. The variadic key-value pairs are treated as they are in With.

When debug-level logging is disabled, this is much faster than

s.With(keysAndValues).Debug(msg)

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Desugar() *[Logger](https://pkg.go.dev/go.uber.org/zap#Logger)

Desugar unwraps a SugaredLogger, exposing the original Logger. Desugaring is quite inexpensive, so it's reasonable for a single application to use both Loggers and SugaredLoggers, converting between them on the boundaries of performance-sensitive code.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Error(args ...interface{})

Error logs the provided arguments at [ErrorLevel](https://pkg.go.dev/go.uber.org/zap#ErrorLevel). Spaces are added between arguments when neither is a string.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Errorf(template [string](https://pkg.go.dev/builtin#string), args ...interface{})

Errorf formats the message according to the format specifier and logs it at [ErrorLevel](https://pkg.go.dev/go.uber.org/zap#ErrorLevel).

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Errorln(args ...interface{})

Errorln logs a message at [ErrorLevel](https://pkg.go.dev/go.uber.org/zap#ErrorLevel). Spaces are always added between arguments.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Errorw(msg [string](https://pkg.go.dev/builtin#string), keysAndValues ...interface{})

Errorw logs a message with some additional context. The variadic key-value pairs are treated as they are in With.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Fatal(args ...interface{})

Fatal constructs a message with the provided arguments and calls os.Exit. Spaces are added between arguments when neither is a string.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Fatalf(template [string](https://pkg.go.dev/builtin#string), args ...interface{})

Fatalf formats the message according to the format specifier and calls os.Exit.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Fatalln(args ...interface{})

Fatalln logs a message at [FatalLevel](https://pkg.go.dev/go.uber.org/zap#FatalLevel) and calls os.Exit. Spaces are always added between arguments.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Fatalw(msg [string](https://pkg.go.dev/builtin#string), keysAndValues ...interface{})

Fatalw logs a message with some additional context, then calls os.Exit. The variadic key-value pairs are treated as they are in With.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Info(args ...interface{})

Info logs the provided arguments at [InfoLevel](https://pkg.go.dev/go.uber.org/zap#InfoLevel). Spaces are added between arguments when neither is a string.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Infof(template [string](https://pkg.go.dev/builtin#string), args ...interface{})

Infof formats the message according to the format specifier and logs it at [InfoLevel](https://pkg.go.dev/go.uber.org/zap#InfoLevel).

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Infoln(args ...interface{})

Infoln logs a message at [InfoLevel](https://pkg.go.dev/go.uber.org/zap#InfoLevel). Spaces are always added between arguments.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Infow(msg [string](https://pkg.go.dev/builtin#string), keysAndValues ...interface{})

Infow logs a message with some additional context. The variadic key-value pairs are treated as they are in With.

Level reports the minimum enabled level for this logger.

For NopLoggers, this is [zapcore.InvalidLevel](https://pkg.go.dev/go.uber.org/zap@v1.27.1/zapcore#InvalidLevel).

Log logs the provided arguments at provided level. Spaces are added between arguments when neither is a string.

Logf formats the message according to the format specifier and logs it at provided level.

Logln logs a message at provided level. Spaces are always added between arguments.

Logw logs a message with some additional context. The variadic key-value pairs are treated as they are in With.

Named adds a sub-scope to the logger's name. See Logger.Named for details.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Panic(args ...interface{})

Panic constructs a message with the provided arguments and panics. Spaces are added between arguments when neither is a string.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Panicf(template [string](https://pkg.go.dev/builtin#string), args ...interface{})

Panicf formats the message according to the format specifier and panics.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Panicln(args ...interface{})

Panicln logs a message at [PanicLevel](https://pkg.go.dev/go.uber.org/zap#PanicLevel) and panics. Spaces are always added between arguments.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Panicw(msg [string](https://pkg.go.dev/builtin#string), keysAndValues ...interface{})

Panicw logs a message with some additional context, then panics. The variadic key-value pairs are treated as they are in With.

Sync flushes any buffered log entries.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Warn(args ...interface{})

Warn logs the provided arguments at [WarnLevel](https://pkg.go.dev/go.uber.org/zap#WarnLevel). Spaces are added between arguments when neither is a string.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Warnf(template [string](https://pkg.go.dev/builtin#string), args ...interface{})

Warnf formats the message according to the format specifier and logs it at [WarnLevel](https://pkg.go.dev/go.uber.org/zap#WarnLevel).

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Warnln(args ...interface{})

Warnln logs a message at [WarnLevel](https://pkg.go.dev/go.uber.org/zap#WarnLevel). Spaces are always added between arguments.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) Warnw(msg [string](https://pkg.go.dev/builtin#string), keysAndValues ...interface{})

Warnw logs a message with some additional context. The variadic key-value pairs are treated as they are in With.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) With(args ...interface{}) *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)

With adds a variadic number of fields to the logging context. It accepts a mix of strongly-typed Field objects and loosely-typed key-value pairs. When processing pairs, the first element of the pair is used as the field key and the second as the field value.

For example,

 sugaredLogger.With(
   "hello", "world",
   "failure", errors.New("oh no"),
   Stack(),
   "count", 42,
   "user", User{Name: "alice"},
)

is the equivalent of

unsugared.With(
  String("hello", "world"),
  String("failure", "oh no"),
  Stack(),
  Int("count", 42),
  Object("user", User{Name: "alice"}),
)

Note that the keys in key-value pairs should be strings. In development, passing a non-string key panics. In production, the logger is more forgiving: a separate error is logged, but the key-value pair is skipped and execution continues. Passing an orphaned key triggers similar behavior: panics in development and errors in production.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) WithLazy(args ...interface{}) *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)

WithLazy adds a variadic number of fields to the logging context lazily. The fields are evaluated only if the logger is further chained with [With] or is written to with any of the log level methods. Until that occurs, the logger may retain references to objects inside the fields, and logging will reflect the state of an object at the time of logging, not the time of WithLazy().

Similar to [With], fields added to the child don't affect the parent, and vice versa. Also, the keys in key-value pairs should be strings. In development, passing a non-string key panics, while in production it logs an error and skips the pair. Passing an orphaned key has the same behavior.

func (s *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)) WithOptions(opts ...[Option](https://pkg.go.dev/go.uber.org/zap#Option)) *[SugaredLogger](https://pkg.go.dev/go.uber.org/zap#SugaredLogger)

WithOptions clones the current SugaredLogger, applies the supplied Options, and returns the result. It's safe to use concurrently.
