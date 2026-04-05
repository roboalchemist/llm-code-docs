# Viper Package Documentation

## Overview

**Viper** is a complete configuration solution for Go applications. It is designed to work within an application and can handle all types of configuration needs and formats.

**Package:** `github.com/spf13/viper`  
**Version:** v1.21.0  
**License:** MIT  
**Repository:** https://github.com/spf13/viper

## Supported Features

Viper supports:
- Setting defaults
- Reading from JSON, TOML, YAML, HCL, envfile and Java properties config files
- Live watching and re-reading of config files (optional)
- Reading from environment variables
- Reading from remote config systems (etcd or Consul), and watching changes
- Reading from command line flags
- Reading from buffer
- Setting explicit values

## Configuration Precedence Order

Each item takes precedence over the item below it:
1. Explicit call to `Set`
2. Flag
3. Environment variable
4. Config file
5. Key/value store
6. Default

## Core Functions

### Configuration File Management

```go
func SetConfigName(in string)
func SetConfigType(in string)
func SetConfigFile(in string)
func AddConfigPath(in string)
func SetConfigPermissions(perm os.FileMode)
func ConfigFileUsed() string
```

### Reading Configuration

```go
func ReadInConfig() error
func ReadConfig(in io.Reader) error
func ReadRemoteConfig() error
func MergeInConfig() error
func MergeConfig(in io.Reader) error
func MergeConfigMap(cfg map[string]any) error
```

### Writing Configuration

```go
func WriteConfig() error
func WriteConfigAs(filename string) error
func SafeWriteConfig() error
func SafeWriteConfigAs(filename string) error
func WriteConfigTo(w io.Writer) error
```

### Watching Configuration

```go
func WatchConfig()
func WatchRemoteConfig() error
func OnConfigChange(run func(in fsnotify.Event))
```

### Getting Values

```go
func Get(key string) any
func GetBool(key string) bool
func GetFloat64(key string) float64
func GetInt(key string) int
func GetInt32(key string) int32
func GetInt64(key string) int64
func GetIntSlice(key string) []int
func GetString(key string) string
func GetStringMap(key string) map[string]any
func GetStringMapString(key string) map[string]string
func GetStringMapStringSlice(key string) map[string][]string
func GetStringSlice(key string) []string
func GetTime(key string) time.Time
func GetDuration(key string) time.Duration
func GetUint(key string) uint
func GetUint8(key string) uint8
func GetUint16(key string) uint16
func GetUint32(key string) uint32
func GetUint64(key string) uint64
func GetSizeInBytes(key string) uint
func IsSet(key string) bool
func InConfig(key string) bool
func AllKeys() []string
func AllSettings() map[string]any
```

### Setting Values

```go
func Set(key string, value any)
func SetDefault(key string, value any)
func RegisterAlias(alias, key string)
```

### Environment Variables

```go
func BindEnv(input ...string) error
func MustBindEnv(input ...string)
func AutomaticEnv()
func SetEnvPrefix(in string)
func GetEnvPrefix() string
func SetEnvKeyReplacer(r *strings.Replacer)
func AllowEmptyEnv(allowEmptyEnv bool)
```

### Flags

```go
func BindPFlag(key string, flag *pflag.Flag) error
func BindPFlags(flags *pflag.FlagSet) error
func BindFlagValue(key string, flag FlagValue) error
func BindFlagValues(flags FlagValueSet) error
```

### Remote Configuration

```go
func AddRemoteProvider(provider, endpoint, path string) error
func AddSecureRemoteProvider(provider, endpoint, path, secretkeyring string) error
```

Supported remote providers:
- etcd
- etcd3
- Consul
- Firestore
- NATS

### Unmarshaling

```go
func Unmarshal(rawVal any, opts ...DecoderConfigOption) error
func UnmarshalExact(rawVal any, opts ...DecoderConfigOption) error
func UnmarshalKey(key string, rawVal any, opts ...DecoderConfigOption) error
```

### Debugging

```go
func Debug()
func DebugTo(w io.Writer)
func Reset()
```

## Viper Instance Methods

Create a new Viper instance instead of using the global singleton:

```go
func New() *Viper
func NewWithOptions(opts ...Option) *Viper
func GetViper() *Viper
```

### Sub-configurations

```go
func Sub(key string) *Viper
```

Extract a subset of configuration:

```go
cache1Config := viper.Sub("cache.cache1")
if cache1Config == nil {
    panic("cache configuration not found")
}
```

## Configuration Options

```go
type Option interface{}

func KeyDelimiter(d string) Option
func WithCodecRegistry(r CodecRegistry) Option
func WithDecoderRegistry(r DecoderRegistry) Option
func WithEncoderRegistry(r EncoderRegistry) Option
func WithDecodeHook(h mapstructure.DecodeHookFunc) Option
func WithFinder(f Finder) Option
func WithLogger(l *slog.Logger) Option
func EnvKeyReplacer(r StringReplacer) Option
func ExperimentalFinder() Option
func ExperimentalBindStruct() Option
```

## Error Types

```go
type ConfigFileNotFoundError struct {
    name, locations string
}

type ConfigFileAlreadyExistsError string

type ConfigMarshalError struct {
    err error
}

type ConfigParseError struct {
    err error
}

type RemoteConfigError struct {
    err string
}

type UnsupportedConfigError string

type UnsupportedRemoteProviderError string
```

## Interfaces

```go
type FlagValue interface {
    HasChanged() bool
    Name() string
    ValueString() string
    ValueType() string
}

type FlagValueSet interface {
    VisitAll(fn func(FlagValue))
}

type Codec interface {
    Encoder
    Decoder
}

type Encoder interface {
    Encode(v map[string]any) ([]byte, error)
}

type Decoder interface {
    Decode(b []byte, v map[string]any) error
}

type CodecRegistry interface {
    Encoder(format string) (Encoder, error)
    Decoder(format string) (Decoder, error)
}

type EncoderRegistry interface {
    Encoder(format string) (Encoder, error)
}

type DecoderRegistry interface {
    Decoder(format string) (Decoder, error)
}

type Finder interface {
    Find(fsys afero.Fs) ([]string, error)
}

type StringReplacer interface {
    Replace(s string) string
}

type DecoderConfigOption func(*mapstructure.DecoderConfig)
```

## Common Examples

### Basic Setup

```go
viper.SetConfigName("config")
viper.SetConfigType("yaml")
viper.AddConfigPath("/etc/appname/")
viper.AddConfigPath("$HOME/.appname")
viper.AddConfigPath(".")
err := viper.ReadInConfig()
if err != nil {
    panic(fmt.Errorf("fatal error config file: %w", err))
}
```

### Environment Variables

```go
viper.SetEnvPrefix("spf")
viper.BindEnv("id")
os.Setenv("SPF_ID", "13")
id := viper.Get("id") // 13
```

### Unmarshaling to Struct

```go
type Config struct {
    Port    int
    Name    string
    PathMap string `mapstructure:"path_map"`
}

var C Config
err := viper.Unmarshal(&C)
if err != nil {
    t.Fatalf("unable to decode into struct, %v", err)
}
```

### Accessing Nested Keys

```go
viper.GetString("datastore.metric.host") // "127.0.0.1"
viper.GetInt("host.ports.1")              // 6029
```

### Multiple Viper Instances

```go
x := viper.New()
y := viper.New()

x.SetDefault("ContentDir", "content")
y.SetDefault("ContentDir", "foobar")
```

### Watching Config Changes

```go
viper.OnConfigChange(func(e fsnotify.Event) {
    fmt.Println("Config file changed:", e.Name)
})
viper.WatchConfig()
```

### Custom Codec Registry

```go
codecRegistry := viper.NewCodecRegistry()
codecRegistry.RegisterCodec("myformat", &MyCodec{})

v := viper.NewWithOptions(
    viper.WithCodecRegistry(codecRegistry),
)
```

### Custom Finder

```go
v := viper.NewWithOptions(
    viper.WithFinder(&MyFinder{}),
)
```

## Important Notes

- **Case Insensitivity:** Viper keys are case insensitive by default
- **Concurrent Access:** Not thread-safe; use `sync` package for concurrent access
- **Type Inference:** `SetTypeByDefaultValue()` enables type inference based on default values
- **Key Delimiter:** Default delimiter is `.`; customize with `KeyDelimiter()` option
- **Empty Environment Variables:** By default, empty env vars are considered unset; use `AllowEmptyEnv()` to change this

## Supported Configuration Formats

JSON, TOML, YAML, HCL, INI, envfile, Java Properties, and custom formats via codec registry.
