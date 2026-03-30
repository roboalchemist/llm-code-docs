# Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/dynamicconfig

Title: dynamicconfig package - go.temporal.io/server/common/dynamicconfig - Go Packages

URL Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/dynamicconfig

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
go.temporal.io/server
 
common
 
dynamicconfig
dynamicconfig
package
Version: v1.30.0 Latest 
Published: Feb 4, 2026 
License: MIT 
Imports: 38 
Imported by: 12
Details
 Valid go.mod file 
 Redistributable license 
 Tagged version 
 Stable version 
Learn more about best practices
Repository
github.com/temporalio/temporal
Links
 Open Source Insights
Jump to ...
Documentation
Source Files
 Documentation ¶
Overview ¶

Package dynamicconfig is a generated GoMock package.

Index ¶
Constants
Variables
func ConvertGradualChange[T any](def T) func(v any) (GradualChange[T], error)
func ConvertStructure[T any](def T) func(v any) (T, error)
func ConvertWildcardStringListToRegexp(in any) (*regexp.Regexp, error)
func NewFileBasedClient(config *FileBasedClientConfig, logger log.Logger, doneCh <-chan interface{}) (*fileBasedClient, error)
func NewFileBasedClientWithReader(reader FileReader, config *FileBasedClientConfig, logger log.Logger, ...) (*fileBasedClient, error)
func ResetRegistryForTest()
func SubscribeGradualChange[T any](subscribable TypedSubscribable[GradualChange[T]], changeKey []byte, ...) (T, func())
type BoolPropertyFn
func GetBoolPropertyFn(value bool) BoolPropertyFn
type BoolPropertyFnWithDestinationFilter
func GetBoolPropertyFnFilteredByDestination(value bool) BoolPropertyFnWithDestinationFilter
type BoolPropertyFnWithNamespaceFilter
func GetBoolPropertyFnFilteredByNamespace(value bool) BoolPropertyFnWithNamespaceFilter
type BoolPropertyFnWithNamespaceIDFilter
func GetBoolPropertyFnFilteredByNamespaceID(value bool) BoolPropertyFnWithNamespaceIDFilter
type BoolPropertyFnWithShardIDFilter
func GetBoolPropertyFnFilteredByShardID(value bool) BoolPropertyFnWithShardIDFilter
type BoolPropertyFnWithTaskQueueFilter
func GetBoolPropertyFnFilteredByTaskQueue(value bool) BoolPropertyFnWithTaskQueueFilter
type BoolPropertyFnWithTaskTypeFilter
func GetBoolPropertyFnFilteredByTaskType(value bool) BoolPropertyFnWithTaskTypeFilter
type CacheBackgroundEvictSettings
type CircuitBreakerSettings
type Client
func NewNoopClient() Client
type ClientUpdateFunc
type Collection
func NewCollection(client Client, logger log.Logger) *Collection
func NewNoopCollection() *Collection
func (c *Collection) GetPingChecks() []pingable.Check
func (c *Collection) Start()
func (c *Collection) Stop()
type ConfigValueMap
func DiffAndLogConfigs(logger log.Logger, oldValues ConfigValueMap, newValues ConfigValueMap) ConfigValueMap
type ConstrainedValue
type Constraints
type DestinationBoolConstrainedDefaultSetting
func NewDestinationBoolSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[bool], description string) DestinationBoolConstrainedDefaultSetting
type DestinationBoolSetting
func NewDestinationBoolSetting(key string, def bool, description string) DestinationBoolSetting
type DestinationDurationConstrainedDefaultSetting
func NewDestinationDurationSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[time.Duration], description string) DestinationDurationConstrainedDefaultSetting
type DestinationDurationSetting
func NewDestinationDurationSetting(key string, def time.Duration, description string) DestinationDurationSetting
type DestinationFloatConstrainedDefaultSetting
func NewDestinationFloatSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[float64], description string) DestinationFloatConstrainedDefaultSetting
type DestinationFloatSetting
func NewDestinationFloatSetting(key string, def float64, description string) DestinationFloatSetting
type DestinationIntConstrainedDefaultSetting
func NewDestinationIntSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[int], description string) DestinationIntConstrainedDefaultSetting
type DestinationIntSetting
func NewDestinationIntSetting(key string, def int, description string) DestinationIntSetting
type DestinationMapConstrainedDefaultSetting
func NewDestinationMapSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[map[string]any], description string) DestinationMapConstrainedDefaultSetting
type DestinationMapSetting
func NewDestinationMapSetting(key string, def map[string]any, description string) DestinationMapSetting
type DestinationStringConstrainedDefaultSetting
func NewDestinationStringSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[string], description string) DestinationStringConstrainedDefaultSetting
type DestinationStringSetting
func NewDestinationStringSetting(key string, def string, description string) DestinationStringSetting
type DestinationTypedConstrainedDefaultSetting
func NewDestinationTypedSettingWithConstrainedDefault[T any](key string, convert func(any) (T, error), cdef []TypedConstrainedValue[T], ...) DestinationTypedConstrainedDefaultSetting[T]
func (s DestinationTypedConstrainedDefaultSetting[T]) Get(c *Collection) TypedPropertyFnWithDestinationFilter[T]
func (s DestinationTypedConstrainedDefaultSetting[T]) Key() Key
func (s DestinationTypedConstrainedDefaultSetting[T]) Precedence() Precedence
func (s DestinationTypedConstrainedDefaultSetting[T]) Subscribe(c *Collection) TypedSubscribableWithDestinationFilter[T]
func (s DestinationTypedConstrainedDefaultSetting[T]) Validate(v any) error
type DestinationTypedSetting
func NewDestinationTypedSetting[T any](key string, def T, description string) DestinationTypedSetting[T]
func NewDestinationTypedSettingWithConverter[T any](key string, convert func(any) (T, error), def T, description string) DestinationTypedSetting[T]
func (s DestinationTypedSetting[T]) Get(c *Collection) TypedPropertyFnWithDestinationFilter[T]
func (s DestinationTypedSetting[T]) Key() Key
func (s DestinationTypedSetting[T]) Precedence() Precedence
func (s DestinationTypedSetting[T]) Subscribe(c *Collection) TypedSubscribableWithDestinationFilter[T]
func (s DestinationTypedSetting[T]) Validate(v any) error
func (s DestinationTypedSetting[T]) WithDefault(v T) DestinationTypedSetting[T]
type DurationPropertyFn
func GetDurationPropertyFn(value time.Duration) DurationPropertyFn
type DurationPropertyFnWithDestinationFilter
func GetDurationPropertyFnFilteredByDestination(value time.Duration) DurationPropertyFnWithDestinationFilter
type DurationPropertyFnWithNamespaceFilter
func GetDurationPropertyFnFilteredByNamespace(value time.Duration) DurationPropertyFnWithNamespaceFilter
type DurationPropertyFnWithNamespaceIDFilter
func GetDurationPropertyFnFilteredByNamespaceID(value time.Duration) DurationPropertyFnWithNamespaceIDFilter
type DurationPropertyFnWithShardIDFilter
func GetDurationPropertyFnFilteredByShardID(value time.Duration) DurationPropertyFnWithShardIDFilter
type DurationPropertyFnWithTaskQueueFilter
func GetDurationPropertyFnFilteredByTaskQueue(value time.Duration) DurationPropertyFnWithTaskQueueFilter
type DurationPropertyFnWithTaskTypeFilter
func GetDurationPropertyFnFilteredByTaskType(value time.Duration) DurationPropertyFnWithTaskTypeFilter
type DynamicRateLimitingParams
type FileBasedClientConfig
type FileReader
type FloatPropertyFn
func GetFloatPropertyFn(value float64) FloatPropertyFn
type FloatPropertyFnWithDestinationFilter
func GetFloatPropertyFnFilteredByDestination(value float64) FloatPropertyFnWithDestinationFilter
type FloatPropertyFnWithNamespaceFilter
func GetFloatPropertyFnFilteredByNamespace(value float64) FloatPropertyFnWithNamespaceFilter
type FloatPropertyFnWithNamespaceIDFilter
func GetFloatPropertyFnFilteredByNamespaceID(value float64) FloatPropertyFnWithNamespaceIDFilter
type FloatPropertyFnWithShardIDFilter
func GetFloatPropertyFnFilteredByShardID(value float64) FloatPropertyFnWithShardIDFilter
type FloatPropertyFnWithTaskQueueFilter
func GetFloatPropertyFnFilteredByTaskQueue(value float64) FloatPropertyFnWithTaskQueueFilter
type FloatPropertyFnWithTaskTypeFilter
func GetFloatPropertyFnFilteredByTaskType(value float64) FloatPropertyFnWithTaskTypeFilter
type GenericParseHook
type GenericSetting
type GlobalBoolConstrainedDefaultSetting
func NewGlobalBoolSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[bool], description string) GlobalBoolConstrainedDefaultSetting
type GlobalBoolSetting
func NewGlobalBoolSetting(key string, def bool, description string) GlobalBoolSetting
type GlobalDurationConstrainedDefaultSetting
func NewGlobalDurationSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[time.Duration], description string) GlobalDurationConstrainedDefaultSetting
type GlobalDurationSetting
func NewGlobalDurationSetting(key string, def time.Duration, description string) GlobalDurationSetting
type GlobalFloatConstrainedDefaultSetting
func NewGlobalFloatSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[float64], description string) GlobalFloatConstrainedDefaultSetting
type GlobalFloatSetting
func NewGlobalFloatSetting(key string, def float64, description string) GlobalFloatSetting
type GlobalIntConstrainedDefaultSetting
func NewGlobalIntSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[int], description string) GlobalIntConstrainedDefaultSetting
type GlobalIntSetting
func NewGlobalIntSetting(key string, def int, description string) GlobalIntSetting
type GlobalMapConstrainedDefaultSetting
func NewGlobalMapSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[map[string]any], description string) GlobalMapConstrainedDefaultSetting
type GlobalMapSetting
func NewGlobalMapSetting(key string, def map[string]any, description string) GlobalMapSetting
type GlobalStringConstrainedDefaultSetting
func NewGlobalStringSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[string], description string) GlobalStringConstrainedDefaultSetting
type GlobalStringSetting
func NewGlobalStringSetting(key string, def string, description string) GlobalStringSetting
type GlobalTypedConstrainedDefaultSetting
func NewGlobalTypedSettingWithConstrainedDefault[T any](key string, convert func(any) (T, error), cdef []TypedConstrainedValue[T], ...) GlobalTypedConstrainedDefaultSetting[T]
func (s GlobalTypedConstrainedDefaultSetting[T]) Get(c *Collection) TypedPropertyFn[T]
func (s GlobalTypedConstrainedDefaultSetting[T]) Key() Key
func (s GlobalTypedConstrainedDefaultSetting[T]) Precedence() Precedence
func (s GlobalTypedConstrainedDefaultSetting[T]) Subscribe(c *Collection) TypedSubscribable[T]
func (s GlobalTypedConstrainedDefaultSetting[T]) Validate(v any) error
type GlobalTypedSetting
func NewGlobalTypedSetting[T any](key string, def T, description string) GlobalTypedSetting[T]
func NewGlobalTypedSettingWithConverter[T any](key string, convert func(any) (T, error), def T, description string) GlobalTypedSetting[T]
func (s GlobalTypedSetting[T]) Get(c *Collection) TypedPropertyFn[T]
func (s GlobalTypedSetting[T]) Key() Key
func (s GlobalTypedSetting[T]) Precedence() Precedence
func (s GlobalTypedSetting[T]) Subscribe(c *Collection) TypedSubscribable[T]
func (s GlobalTypedSetting[T]) Validate(v any) error
func (s GlobalTypedSetting[T]) WithDefault(v T) GlobalTypedSetting[T]
type GradualChange
func StaticGradualChange[T any](def T) GradualChange[T]
func (c *GradualChange[T]) Value(key []byte, now time.Time) T
func (c *GradualChange[T]) When(key []byte) time.Time
type IntPropertyFn
func GetIntPropertyFn(value int) IntPropertyFn
type IntPropertyFnWithDestinationFilter
func GetIntPropertyFnFilteredByDestination(value int) IntPropertyFnWithDestinationFilter
type IntPropertyFnWithNamespaceFilter
func GetIntPropertyFnFilteredByNamespace(value int) IntPropertyFnWithNamespaceFilter
type IntPropertyFnWithNamespaceIDFilter
func GetIntPropertyFnFilteredByNamespaceID(value int) IntPropertyFnWithNamespaceIDFilter
type IntPropertyFnWithShardIDFilter
func GetIntPropertyFnFilteredByShardID(value int) IntPropertyFnWithShardIDFilter
type IntPropertyFnWithTaskQueueFilter
func GetIntPropertyFnFilteredByTaskQueue(value int) IntPropertyFnWithTaskQueueFilter
type IntPropertyFnWithTaskTypeFilter
func GetIntPropertyFnFilteredByTaskType(value int) IntPropertyFnWithTaskTypeFilter
type Key
func MakeKey(s string) Key
func (k Key) String() string
type MapPropertyFn
func GetMapPropertyFn(value map[string]any) MapPropertyFn
type MapPropertyFnWithDestinationFilter
func GetMapPropertyFnFilteredByDestination(value map[string]any) MapPropertyFnWithDestinationFilter
type MapPropertyFnWithNamespaceFilter
func GetMapPropertyFnFilteredByNamespace(value map[string]any) MapPropertyFnWithNamespaceFilter
type MapPropertyFnWithNamespaceIDFilter
func GetMapPropertyFnFilteredByNamespaceID(value map[string]any) MapPropertyFnWithNamespaceIDFilter
type MapPropertyFnWithShardIDFilter
func GetMapPropertyFnFilteredByShardID(value map[string]any) MapPropertyFnWithShardIDFilter
type MapPropertyFnWithTaskQueueFilter
func GetMapPropertyFnFilteredByTaskQueue(value map[string]any) MapPropertyFnWithTaskQueueFilter
type MapPropertyFnWithTaskTypeFilter
func GetMapPropertyFnFilteredByTaskType(value map[string]any) MapPropertyFnWithTaskTypeFilter
type MemoryClient
func NewMemoryClient() *MemoryClient
func (d *MemoryClient) GetValue(key Key) []ConstrainedValue
func (d *MemoryClient) OverrideSetting(setting GenericSetting, value any) (cleanup func())
func (d *MemoryClient) OverrideValue(key Key, value any) (cleanup func())
type MockFileReader
func NewMockFileReader(ctrl *gomock.Controller) *MockFileReader
func (m *MockFileReader) EXPECT() *MockFileReaderMockRecorder
func (m *MockFileReader) GetModTime() (time.Time, error)
func (m *MockFileReader) ReadFile() ([]byte, error)
type MockFileReaderMockRecorder
func (mr *MockFileReaderMockRecorder) GetModTime() *gomock.Call
func (mr *MockFileReaderMockRecorder) ReadFile() *gomock.Call
type NamespaceBoolConstrainedDefaultSetting
func NewNamespaceBoolSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[bool], description string) NamespaceBoolConstrainedDefaultSetting
type NamespaceBoolSetting
func NewNamespaceBoolSetting(key string, def bool, description string) NamespaceBoolSetting
type NamespaceDurationConstrainedDefaultSetting
func NewNamespaceDurationSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[time.Duration], description string) NamespaceDurationConstrainedDefaultSetting
type NamespaceDurationSetting
func NewNamespaceDurationSetting(key string, def time.Duration, description string) NamespaceDurationSetting
type NamespaceFloatConstrainedDefaultSetting
func NewNamespaceFloatSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[float64], description string) NamespaceFloatConstrainedDefaultSetting
type NamespaceFloatSetting
func NewNamespaceFloatSetting(key string, def float64, description string) NamespaceFloatSetting
type NamespaceIDBoolConstrainedDefaultSetting
func NewNamespaceIDBoolSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[bool], description string) NamespaceIDBoolConstrainedDefaultSetting
type NamespaceIDBoolSetting
func NewNamespaceIDBoolSetting(key string, def bool, description string) NamespaceIDBoolSetting
type NamespaceIDDurationConstrainedDefaultSetting
func NewNamespaceIDDurationSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[time.Duration], description string) NamespaceIDDurationConstrainedDefaultSetting
type NamespaceIDDurationSetting
func NewNamespaceIDDurationSetting(key string, def time.Duration, description string) NamespaceIDDurationSetting
type NamespaceIDFloatConstrainedDefaultSetting
func NewNamespaceIDFloatSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[float64], description string) NamespaceIDFloatConstrainedDefaultSetting
type NamespaceIDFloatSetting
func NewNamespaceIDFloatSetting(key string, def float64, description string) NamespaceIDFloatSetting
type NamespaceIDIntConstrainedDefaultSetting
func NewNamespaceIDIntSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[int], description string) NamespaceIDIntConstrainedDefaultSetting
type NamespaceIDIntSetting
func NewNamespaceIDIntSetting(key string, def int, description string) NamespaceIDIntSetting
type NamespaceIDMapConstrainedDefaultSetting
func NewNamespaceIDMapSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[map[string]any], description string) NamespaceIDMapConstrainedDefaultSetting
type NamespaceIDMapSetting
func NewNamespaceIDMapSetting(key string, def map[string]any, description string) NamespaceIDMapSetting
type NamespaceIDStringConstrainedDefaultSetting
func NewNamespaceIDStringSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[string], description string) NamespaceIDStringConstrainedDefaultSetting
type NamespaceIDStringSetting
func NewNamespaceIDStringSetting(key string, def string, description string) NamespaceIDStringSetting
type NamespaceIDTypedConstrainedDefaultSetting
func NewNamespaceIDTypedSettingWithConstrainedDefault[T any](key string, convert func(any) (T, error), cdef []TypedConstrainedValue[T], ...) NamespaceIDTypedConstrainedDefaultSetting[T]
func (s NamespaceIDTypedConstrainedDefaultSetting[T]) Get(c *Collection) TypedPropertyFnWithNamespaceIDFilter[T]
func (s NamespaceIDTypedConstrainedDefaultSetting[T]) Key() Key
func (s NamespaceIDTypedConstrainedDefaultSetting[T]) Precedence() Precedence
func (s NamespaceIDTypedConstrainedDefaultSetting[T]) Subscribe(c *Collection) TypedSubscribableWithNamespaceIDFilter[T]
func (s NamespaceIDTypedConstrainedDefaultSetting[T]) Validate(v any) error
type NamespaceIDTypedSetting
func NewNamespaceIDTypedSetting[T any](key string, def T, description string) NamespaceIDTypedSetting[T]
func NewNamespaceIDTypedSettingWithConverter[T any](key string, convert func(any) (T, error), def T, description string) NamespaceIDTypedSetting[T]
func (s NamespaceIDTypedSetting[T]) Get(c *Collection) TypedPropertyFnWithNamespaceIDFilter[T]
func (s NamespaceIDTypedSetting[T]) Key() Key
func (s NamespaceIDTypedSetting[T]) Precedence() Precedence
func (s NamespaceIDTypedSetting[T]) Subscribe(c *Collection) TypedSubscribableWithNamespaceIDFilter[T]
func (s NamespaceIDTypedSetting[T]) Validate(v any) error
func (s NamespaceIDTypedSetting[T]) WithDefault(v T) NamespaceIDTypedSetting[T]
type NamespaceIntConstrainedDefaultSetting
func NewNamespaceIntSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[int], description string) NamespaceIntConstrainedDefaultSetting
type NamespaceIntSetting
func NewNamespaceIntSetting(key string, def int, description string) NamespaceIntSetting
type NamespaceMapConstrainedDefaultSetting
func NewNamespaceMapSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[map[string]any], description string) NamespaceMapConstrainedDefaultSetting
type NamespaceMapSetting
func NewNamespaceMapSetting(key string, def map[string]any, description string) NamespaceMapSetting
type NamespaceStringConstrainedDefaultSetting
func NewNamespaceStringSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[string], description string) NamespaceStringConstrainedDefaultSetting
type NamespaceStringSetting
func NewNamespaceStringSetting(key string, def string, description string) NamespaceStringSetting
type NamespaceTypedConstrainedDefaultSetting
func NewNamespaceTypedSettingWithConstrainedDefault[T any](key string, convert func(any) (T, error), cdef []TypedConstrainedValue[T], ...) NamespaceTypedConstrainedDefaultSetting[T]
func (s NamespaceTypedConstrainedDefaultSetting[T]) Get(c *Collection) TypedPropertyFnWithNamespaceFilter[T]
func (s NamespaceTypedConstrainedDefaultSetting[T]) Key() Key
func (s NamespaceTypedConstrainedDefaultSetting[T]) Precedence() Precedence
func (s NamespaceTypedConstrainedDefaultSetting[T]) Subscribe(c *Collection) TypedSubscribableWithNamespaceFilter[T]
func (s NamespaceTypedConstrainedDefaultSetting[T]) Validate(v any) error
type NamespaceTypedSetting
func NewNamespaceTypedSetting[T any](key string, def T, description string) NamespaceTypedSetting[T]
func NewNamespaceTypedSettingWithConverter[T any](key string, convert func(any) (T, error), def T, description string) NamespaceTypedSetting[T]
func (s NamespaceTypedSetting[T]) Get(c *Collection) TypedPropertyFnWithNamespaceFilter[T]
func (s NamespaceTypedSetting[T]) Key() Key
func (s NamespaceTypedSetting[T]) Precedence() Precedence
func (s NamespaceTypedSetting[T]) Subscribe(c *Collection) TypedSubscribableWithNamespaceFilter[T]
func (s NamespaceTypedSetting[T]) Validate(v any) error
func (s NamespaceTypedSetting[T]) WithDefault(v T) NamespaceTypedSetting[T]
type NotifyingClient
type NotifyingClientImpl
func NewNotifyingClientImpl() NotifyingClientImpl
func (n *NotifyingClientImpl) PublishUpdates(changed map[Key][]ConstrainedValue)
func (n *NotifyingClientImpl) Subscribe(f ClientUpdateFunc) (cancel func())
type Precedence
type ShardIDBoolConstrainedDefaultSetting
func NewShardIDBoolSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[bool], description string) ShardIDBoolConstrainedDefaultSetting
type ShardIDBoolSetting
func NewShardIDBoolSetting(key string, def bool, description string) ShardIDBoolSetting
type ShardIDDurationConstrainedDefaultSetting
func NewShardIDDurationSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[time.Duration], description string) ShardIDDurationConstrainedDefaultSetting
type ShardIDDurationSetting
func NewShardIDDurationSetting(key string, def time.Duration, description string) ShardIDDurationSetting
type ShardIDFloatConstrainedDefaultSetting
func NewShardIDFloatSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[float64], description string) ShardIDFloatConstrainedDefaultSetting
type ShardIDFloatSetting
func NewShardIDFloatSetting(key string, def float64, description string) ShardIDFloatSetting
type ShardIDIntConstrainedDefaultSetting
func NewShardIDIntSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[int], description string) ShardIDIntConstrainedDefaultSetting
type ShardIDIntSetting
func NewShardIDIntSetting(key string, def int, description string) ShardIDIntSetting
type ShardIDMapConstrainedDefaultSetting
func NewShardIDMapSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[map[string]any], description string) ShardIDMapConstrainedDefaultSetting
type ShardIDMapSetting
func NewShardIDMapSetting(key string, def map[string]any, description string) ShardIDMapSetting
type ShardIDStringConstrainedDefaultSetting
func NewShardIDStringSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[string], description string) ShardIDStringConstrainedDefaultSetting
type ShardIDStringSetting
func NewShardIDStringSetting(key string, def string, description string) ShardIDStringSetting
type ShardIDTypedConstrainedDefaultSetting
func NewShardIDTypedSettingWithConstrainedDefault[T any](key string, convert func(any) (T, error), cdef []TypedConstrainedValue[T], ...) ShardIDTypedConstrainedDefaultSetting[T]
func (s ShardIDTypedConstrainedDefaultSetting[T]) Get(c *Collection) TypedPropertyFnWithShardIDFilter[T]
func (s ShardIDTypedConstrainedDefaultSetting[T]) Key() Key
func (s ShardIDTypedConstrainedDefaultSetting[T]) Precedence() Precedence
func (s ShardIDTypedConstrainedDefaultSetting[T]) Subscribe(c *Collection) TypedSubscribableWithShardIDFilter[T]
func (s ShardIDTypedConstrainedDefaultSetting[T]) Validate(v any) error
type ShardIDTypedSetting
func NewShardIDTypedSetting[T any](key string, def T, description string) ShardIDTypedSetting[T]
func NewShardIDTypedSettingWithConverter[T any](key string, convert func(any) (T, error), def T, description string) ShardIDTypedSetting[T]
func (s ShardIDTypedSetting[T]) Get(c *Collection) TypedPropertyFnWithShardIDFilter[T]
func (s ShardIDTypedSetting[T]) Key() Key
func (s ShardIDTypedSetting[T]) Precedence() Precedence
func (s ShardIDTypedSetting[T]) Subscribe(c *Collection) TypedSubscribableWithShardIDFilter[T]
func (s ShardIDTypedSetting[T]) Validate(v any) error
func (s ShardIDTypedSetting[T]) WithDefault(v T) ShardIDTypedSetting[T]
type StaticClient
func (s StaticClient) GetValue(key Key) []ConstrainedValue
type StringPropertyFn
func GetStringPropertyFn(value string) StringPropertyFn
type StringPropertyFnWithDestinationFilter
func GetStringPropertyFnFilteredByDestination(value string) StringPropertyFnWithDestinationFilter
type StringPropertyFnWithNamespaceFilter
func GetStringPropertyFnFilteredByNamespace(value string) StringPropertyFnWithNamespaceFilter
type StringPropertyFnWithNamespaceIDFilter
func GetStringPropertyFnFilteredByNamespaceID(value string) StringPropertyFnWithNamespaceIDFilter
type StringPropertyFnWithShardIDFilter
func GetStringPropertyFnFilteredByShardID(value string) StringPropertyFnWithShardIDFilter
type StringPropertyFnWithTaskQueueFilter
func GetStringPropertyFnFilteredByTaskQueue(value string) StringPropertyFnWithTaskQueueFilter
type StringPropertyFnWithTaskTypeFilter
func GetStringPropertyFnFilteredByTaskType(value string) StringPropertyFnWithTaskTypeFilter
type TaskQueueBoolConstrainedDefaultSetting
func NewTaskQueueBoolSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[bool], description string) TaskQueueBoolConstrainedDefaultSetting
type TaskQueueBoolSetting
func NewTaskQueueBoolSetting(key string, def bool, description string) TaskQueueBoolSetting
type TaskQueueDurationConstrainedDefaultSetting
func NewTaskQueueDurationSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[time.Duration], description string) TaskQueueDurationConstrainedDefaultSetting
type TaskQueueDurationSetting
func NewTaskQueueDurationSetting(key string, def time.Duration, description string) TaskQueueDurationSetting
type TaskQueueFloatConstrainedDefaultSetting
func NewTaskQueueFloatSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[float64], description string) TaskQueueFloatConstrainedDefaultSetting
type TaskQueueFloatSetting
func NewTaskQueueFloatSetting(key string, def float64, description string) TaskQueueFloatSetting
type TaskQueueIntConstrainedDefaultSetting
func NewTaskQueueIntSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[int], description string) TaskQueueIntConstrainedDefaultSetting
type TaskQueueIntSetting
func NewTaskQueueIntSetting(key string, def int, description string) TaskQueueIntSetting
type TaskQueueMapConstrainedDefaultSetting
func NewTaskQueueMapSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[map[string]any], description string) TaskQueueMapConstrainedDefaultSetting
type TaskQueueMapSetting
func NewTaskQueueMapSetting(key string, def map[string]any, description string) TaskQueueMapSetting
type TaskQueueStringConstrainedDefaultSetting
func NewTaskQueueStringSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[string], description string) TaskQueueStringConstrainedDefaultSetting
type TaskQueueStringSetting
func NewTaskQueueStringSetting(key string, def string, description string) TaskQueueStringSetting
type TaskQueueTypedConstrainedDefaultSetting
func NewTaskQueueTypedSettingWithConstrainedDefault[T any](key string, convert func(any) (T, error), cdef []TypedConstrainedValue[T], ...) TaskQueueTypedConstrainedDefaultSetting[T]
func (s TaskQueueTypedConstrainedDefaultSetting[T]) Get(c *Collection) TypedPropertyFnWithTaskQueueFilter[T]
func (s TaskQueueTypedConstrainedDefaultSetting[T]) Key() Key
func (s TaskQueueTypedConstrainedDefaultSetting[T]) Precedence() Precedence
func (s TaskQueueTypedConstrainedDefaultSetting[T]) Subscribe(c *Collection) TypedSubscribableWithTaskQueueFilter[T]
func (s TaskQueueTypedConstrainedDefaultSetting[T]) Validate(v any) error
type TaskQueueTypedSetting
func NewTaskQueueTypedSetting[T any](key string, def T, description string) TaskQueueTypedSetting[T]
func NewTaskQueueTypedSettingWithConverter[T any](key string, convert func(any) (T, error), def T, description string) TaskQueueTypedSetting[T]
func (s TaskQueueTypedSetting[T]) Get(c *Collection) TypedPropertyFnWithTaskQueueFilter[T]
func (s TaskQueueTypedSetting[T]) Key() Key
func (s TaskQueueTypedSetting[T]) Precedence() Precedence
func (s TaskQueueTypedSetting[T]) Subscribe(c *Collection) TypedSubscribableWithTaskQueueFilter[T]
func (s TaskQueueTypedSetting[T]) Validate(v any) error
func (s TaskQueueTypedSetting[T]) WithDefault(v T) TaskQueueTypedSetting[T]
type TaskTypeBoolConstrainedDefaultSetting
func NewTaskTypeBoolSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[bool], description string) TaskTypeBoolConstrainedDefaultSetting
type TaskTypeBoolSetting
func NewTaskTypeBoolSetting(key string, def bool, description string) TaskTypeBoolSetting
type TaskTypeDurationConstrainedDefaultSetting
func NewTaskTypeDurationSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[time.Duration], description string) TaskTypeDurationConstrainedDefaultSetting
type TaskTypeDurationSetting
func NewTaskTypeDurationSetting(key string, def time.Duration, description string) TaskTypeDurationSetting
type TaskTypeFloatConstrainedDefaultSetting
func NewTaskTypeFloatSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[float64], description string) TaskTypeFloatConstrainedDefaultSetting
type TaskTypeFloatSetting
func NewTaskTypeFloatSetting(key string, def float64, description string) TaskTypeFloatSetting
type TaskTypeIntConstrainedDefaultSetting
func NewTaskTypeIntSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[int], description string) TaskTypeIntConstrainedDefaultSetting
type TaskTypeIntSetting
func NewTaskTypeIntSetting(key string, def int, description string) TaskTypeIntSetting
type TaskTypeMapConstrainedDefaultSetting
func NewTaskTypeMapSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[map[string]any], description string) TaskTypeMapConstrainedDefaultSetting
type TaskTypeMapSetting
func NewTaskTypeMapSetting(key string, def map[string]any, description string) TaskTypeMapSetting
type TaskTypeStringConstrainedDefaultSetting
func NewTaskTypeStringSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[string], description string) TaskTypeStringConstrainedDefaultSetting
type TaskTypeStringSetting
func NewTaskTypeStringSetting(key string, def string, description string) TaskTypeStringSetting
type TaskTypeTypedConstrainedDefaultSetting
func NewTaskTypeTypedSettingWithConstrainedDefault[T any](key string, convert func(any) (T, error), cdef []TypedConstrainedValue[T], ...) TaskTypeTypedConstrainedDefaultSetting[T]
func (s TaskTypeTypedConstrainedDefaultSetting[T]) Get(c *Collection) TypedPropertyFnWithTaskTypeFilter[T]
func (s TaskTypeTypedConstrainedDefaultSetting[T]) Key() Key
func (s TaskTypeTypedConstrainedDefaultSetting[T]) Precedence() Precedence
func (s TaskTypeTypedConstrainedDefaultSetting[T]) Subscribe(c *Collection) TypedSubscribableWithTaskTypeFilter[T]
func (s TaskTypeTypedConstrainedDefaultSetting[T]) Validate(v any) error
type TaskTypeTypedSetting
func NewTaskTypeTypedSetting[T any](key string, def T, description string) TaskTypeTypedSetting[T]
func NewTaskTypeTypedSettingWithConverter[T any](key string, convert func(any) (T, error), def T, description string) TaskTypeTypedSetting[T]
func (s TaskTypeTypedSetting[T]) Get(c *Collection) TypedPropertyFnWithTaskTypeFilter[T]
func (s TaskTypeTypedSetting[T]) Key() Key
func (s TaskTypeTypedSetting[T]) Precedence() Precedence
func (s TaskTypeTypedSetting[T]) Subscribe(c *Collection) TypedSubscribableWithTaskTypeFilter[T]
func (s TaskTypeTypedSetting[T]) Validate(v any) error
func (s TaskTypeTypedSetting[T]) WithDefault(v T) TaskTypeTypedSetting[T]
type TypedConstrainedValue
type TypedPropertyFn
func GetTypedPropertyFn[T any](value T) TypedPropertyFn[T]
type TypedPropertyFnWithDestinationFilter
func GetTypedPropertyFnFilteredByDestination[T any](value T) TypedPropertyFnWithDestinationFilter[T]
type TypedPropertyFnWithNamespaceFilter
func GetTypedPropertyFnFilteredByNamespace[T any](value T) TypedPropertyFnWithNamespaceFilter[T]
type TypedPropertyFnWithNamespaceIDFilter
func GetTypedPropertyFnFilteredByNamespaceID[T any](value T) TypedPropertyFnWithNamespaceIDFilter[T]
type TypedPropertyFnWithShardIDFilter
func GetTypedPropertyFnFilteredByShardID[T any](value T) TypedPropertyFnWithShardIDFilter[T]
type TypedPropertyFnWithTaskQueueFilter
func GetTypedPropertyFnFilteredByTaskQueue[T any](value T) TypedPropertyFnWithTaskQueueFilter[T]
type TypedPropertyFnWithTaskTypeFilter
func GetTypedPropertyFnFilteredByTaskType[T any](value T) TypedPropertyFnWithTaskTypeFilter[T]
type TypedSubscribable
type TypedSubscribableWithDestinationFilter
type TypedSubscribableWithNamespaceFilter
type TypedSubscribableWithNamespaceIDFilter
type TypedSubscribableWithShardIDFilter
type TypedSubscribableWithTaskQueueFilter
type TypedSubscribableWithTaskTypeFilter
type YamlLoader
func LoadYamlFile(contents []byte) *YamlLoader
func (lr *YamlLoader) Err() error
func (lr *YamlLoader) LoadFile(contents []byte)
func (lr *YamlLoader) LoadValue(key Key, contents []byte)
Constants ¶
View Source
const GlobalDefaultNumTaskQueuePartitions = 4
Variables ¶
View Source
var (
	// keys for dynamic config itself
	DynamicConfigSubscriptionPollInterval = NewGlobalDurationSetting(
		"dynamicconfig.subscriptionPollInterval",
		time.Minute,
		`Poll interval for emulating subscriptions on non-subscribable Client.`,
	)

	AdminEnableListHistoryTasks = NewGlobalBoolSetting(
		"admin.enableListHistoryTasks",
		true,
		`AdminEnableListHistoryTasks is the key for enabling listing history tasks`,
	)
	AdminMatchingNamespaceToPartitionDispatchRate = NewNamespaceFloatSetting(
		"admin.matchingNamespaceToPartitionDispatchRate",
		10000,
		`AdminMatchingNamespaceToPartitionDispatchRate is the max qps of any task queue partition for a given namespace`,
	)
	AdminMatchingNamespaceTaskqueueToPartitionDispatchRate = NewTaskQueueFloatSetting(
		"admin.matchingNamespaceTaskqueueToPartitionDispatchRate",
		1000,
		`AdminMatchingNamespaceTaskqueueToPartitionDispatchRate is the max qps of a task queue partition for a given namespace & task queue`,
	)

	VisibilityPersistenceMaxReadQPS = NewGlobalIntSetting(
		"system.visibilityPersistenceMaxReadQPS",
		9000,
		`VisibilityPersistenceMaxReadQPS is the max QPC system host can query visibility DB for read.`,
	)
	VisibilityPersistenceMaxWriteQPS = NewGlobalIntSetting(
		"system.visibilityPersistenceMaxWriteQPS",
		9000,
		`VisibilityPersistenceMaxWriteQPS is the max QPC system host can query visibility DB for write.`,
	)
	VisibilityPersistenceSlowQueryThreshold = NewGlobalDurationSetting(
		"system.visibilityPersistenceSlowQueryThreshold",
		time.Second,
		`VisibilityPersistenceSlowQueryThreshold is the threshold above which a query is considered slow and logged.`,
	)
	EnableReadFromSecondaryVisibility = NewNamespaceBoolSetting(
		"system.enableReadFromSecondaryVisibility",
		false,
		`EnableReadFromSecondaryVisibility is the config to enable read from secondary visibility`,
	)
	VisibilityEnableShadowReadMode = NewGlobalBoolSetting(
		"system.visibilityEnableShadowReadMode",
		false,
		`VisibilityEnableShadowReadMode is the config to enable shadow read from secondary visibility`,
	)
	SecondaryVisibilityWritingMode = NewGlobalStringSetting(
		"system.secondaryVisibilityWritingMode",
		"off",
		`SecondaryVisibilityWritingMode is key for how to write to secondary visibility`,
	)
	VisibilityDisableOrderByClause = NewNamespaceBoolSetting(
		"system.visibilityDisableOrderByClause",
		true,
		`VisibilityDisableOrderByClause is the config to disable ORDERY BY clause for Elasticsearch`,
	)
	VisibilityEnableManualPagination = NewNamespaceBoolSetting(
		"system.visibilityEnableManualPagination",
		true,
		`VisibilityEnableManualPagination is the config to enable manual pagination for Elasticsearch`,
	)
	VisibilityAllowList = NewNamespaceBoolSetting(
		"system.visibilityAllowList",
		true,
		`VisibilityAllowList is the config to allow list of values for regular types`,
	)
	SuppressErrorSetSystemSearchAttribute = NewNamespaceBoolSetting(
		"system.suppressErrorSetSystemSearchAttribute",
		false,
		`SuppressErrorSetSystemSearchAttribute suppresses errors when trying to set
values in system search attributes.`,
	)
	VisibilityEnableUnifiedQueryConverter = NewGlobalBoolSetting(
		"system.visibilityEnableUnifiedQueryConverter",
		false,
		`VisibilityEnableUnifiedQueryConverter enables the unified query converter for parsing the
query.`,
	)

	HistoryArchivalState = NewGlobalStringSetting(
		"system.historyArchivalState",
		"",
		`HistoryArchivalState is key for the state of history archival`,
	)
	EnableReadFromHistoryArchival = NewGlobalBoolSetting(
		"system.enableReadFromHistoryArchival",
		false,
		`EnableReadFromHistoryArchival is key for enabling reading history from archival store`,
	)
	VisibilityArchivalState = NewGlobalStringSetting(
		"system.visibilityArchivalState",
		"",
		`VisibilityArchivalState is key for the state of visibility archival`,
	)
	EnableReadFromVisibilityArchival = NewGlobalBoolSetting(
		"system.enableReadFromVisibilityArchival",
		false,
		`EnableReadFromVisibilityArchival is key for enabling reading visibility from archival store`,
	)
	EnableNamespaceNotActiveAutoForwarding = NewNamespaceBoolSetting(
		"system.enableNamespaceNotActiveAutoForwarding",
		true,
		`EnableNamespaceNotActiveAutoForwarding whether enabling DC auto forwarding to active cluster
for signal / start / signal with start API if namespace is not active`,
	)
	EnableNamespaceHandoverWait = NewNamespaceBoolSetting(
		"system.enableNamespaceHandoverWait",
		false,
		`EnableNamespaceHandoverWait whether waiting for namespace replication state update before serve the request`,
	)
	TransactionSizeLimit = NewGlobalIntSetting(
		"system.transactionSizeLimit",
		primitives.DefaultTransactionSizeLimit,
		`TransactionSizeLimit is the largest allowed transaction size to persistence`,
	)
	DisallowQuery = NewNamespaceBoolSetting(
		"system.disallowQuery",
		false,
		`DisallowQuery is the key to disallow query for a namespace`,
	)
	EnableCrossNamespaceCommands = NewGlobalBoolSetting(
		"system.enableCrossNamespaceCommands",
		false,
		`EnableCrossNamespaceCommands is the key to enable commands for external namespaces`,
	)
	ClusterMetadataRefreshInterval = NewGlobalDurationSetting(
		"system.clusterMetadataRefreshInterval",
		time.Minute,
		`ClusterMetadataRefreshInterval is config to manage cluster metadata table refresh interval`,
	)
	ForceSearchAttributesCacheRefreshOnRead = NewGlobalBoolSetting(
		"system.forceSearchAttributesCacheRefreshOnRead",
		false,
		`ForceSearchAttributesCacheRefreshOnRead forces refreshing search attributes cache on a read operation, so we always
get the latest data from DB. This effectively bypasses cache value and is used to facilitate testing of changes in
search attributes. This should not be turned on in production.`,
	)
	EnableRingpopTLS = NewGlobalBoolSetting(
		"system.enableRingpopTLS",
		false,
		`EnableRingpopTLS controls whether to use TLS for ringpop, using the same "internode" TLS
config as the other services.`,
	)
	RingpopApproximateMaxPropagationTime = NewGlobalDurationSetting(
		"system.ringpopApproximateMaxPropagationTime",
		3*time.Second,
		`RingpopApproximateMaxPropagationTime is used for timing certain startup and shutdown processes.
(It is not and doesn't have to be a guarantee.)`,
	)
	EnableParentClosePolicyWorker = NewGlobalBoolSetting(
		"system.enableParentClosePolicyWorker",
		true,
		`EnableParentClosePolicyWorker decides whether or not enable system workers for processing parent close policy task`,
	)
	EnableStickyQuery = NewNamespaceBoolSetting(
		"system.enableStickyQuery",
		true,
		`EnableStickyQuery indicates if sticky query should be enabled per namespace`,
	)
	EnableActivityEagerExecution = NewNamespaceBoolSetting(
		"system.enableActivityEagerExecution",
		false,
		`EnableActivityEagerExecution indicates if activity eager execution is enabled per namespace`,
	)
	EnableActivityRetryStampIncrement = NewGlobalBoolSetting(
		"system.enableActivityRetryStampIncrement",
		false,
		`EnableActivityRetryStampIncrement indicates if activity retry stamp increment is enabled`,
	)
	EnableEagerWorkflowStart = NewNamespaceBoolSetting(
		"system.enableEagerWorkflowStart",
		true,
		`Toggles "eager workflow start" - returning the first workflow task inline in the
response to a StartWorkflowExecution request and skipping the trip through matching.`,
	)
	NamespaceCacheRefreshInterval = NewGlobalDurationSetting(
		"system.namespaceCacheRefreshInterval",
		2*time.Second,
		`NamespaceCacheRefreshInterval is the key for namespace cache refresh interval dynamic config`,
	)
	PersistenceHealthSignalMetricsEnabled = NewGlobalBoolSetting(
		"system.persistenceHealthSignalMetricsEnabled",
		true,
		`PersistenceHealthSignalMetricsEnabled determines whether persistence shard RPS metrics are emitted`,
	)
	HistoryHealthSignalMetricsEnabled = NewGlobalBoolSetting(
		"system.historyHealthSignalMetricsEnabled",
		true,
		`HistoryHealthSignalMetricsEnabled determines whether history service RPC metrics are emitted`,
	)
	PersistenceHealthSignalAggregationEnabled = NewGlobalBoolSetting(
		"system.persistenceHealthSignalAggregationEnabled",
		true,
		`PersistenceHealthSignalAggregationEnabled determines whether persistence latency and error averages are tracked`,
	)
	PersistenceHealthSignalWindowSize = NewGlobalDurationSetting(
		"system.persistenceHealthSignalWindowSize",
		10*time.Second,
		`PersistenceHealthSignalWindowSize is the time window size in seconds for aggregating persistence signals`,
	)
	PersistenceHealthSignalBufferSize = NewGlobalIntSetting(
		"system.persistenceHealthSignalBufferSize",
		5000,
		`PersistenceHealthSignalBufferSize is the maximum number of persistence signals to buffer in memory per signal key`,
	)
	OperatorRPSRatio = NewGlobalFloatSetting(
		"system.operatorRPSRatio",
		0.2,
		`OperatorRPSRatio is the percentage of the rate limit provided to priority rate limiters that should be used for
operator API calls (highest priority). Should be >0.0 and <= 1.0 (defaults to 20% if not specified)`,
	)
	// TODO: The following 2 configs should be removed once server keepalive and client keepalive are enabled by default
	EnableInternodeServerKeepAlive = NewGlobalBoolSetting(
		"system.enableInternodeServerKeepAlive",
		false,
		`enableInternodeServerKeepAlive is the config to enable keep alive for inter-node connections on server side.`,
	)
	EnableInternodeClientKeepAlive = NewGlobalBoolSetting(
		"system.enableInternodeClientKeepAlive",
		false,
		`enableInternodeClientKeepAlive is the config to enable keep alive for inter-node connections on client side.`,
	)

	PersistenceQPSBurstRatio = NewGlobalFloatSetting(
		"system.persistenceQPSBurstRatio",
		1.0,
		`PersistenceQPSBurstRatio is the burst ratio for persistence QPS. This flag controls the burst ratio for all services.`,
	)

	EnableDataLossMetrics = NewGlobalBoolSetting(
		"system.enableDataLossMetrics",
		false,
		`EnableDataLossMetrics determines whether dataloss metrics are emitted when dataloss errors are encountered`,
	)

	DeadlockDumpGoroutines = NewGlobalBoolSetting(
		"system.deadlock.DumpGoroutines",
		true,
		`Whether the deadlock detector should dump goroutines`,
	)
	DeadlockFailHealthCheck = NewGlobalBoolSetting(
		"system.deadlock.FailHealthCheck",
		false,
		`Whether the deadlock detector should cause the grpc server to fail health checks`,
	)
	DeadlockAbortProcess = NewGlobalBoolSetting(
		"system.deadlock.AbortProcess",
		false,
		`Whether the deadlock detector should abort the process`,
	)
	DeadlockInterval = NewGlobalDurationSetting(
		"system.deadlock.Interval",
		60*time.Second,
		`How often the detector checks each root.`,
	)
	DeadlockMaxWorkersPerRoot = NewGlobalIntSetting(
		"system.deadlock.MaxWorkersPerRoot",
		10,
		`How many extra goroutines can be created per root.`,
	)

	NumConsecutiveWorkflowTaskProblemsToTriggerSearchAttribute = NewNamespaceIntSetting(
		"system.numConsecutiveWorkflowTaskProblemsToTriggerSearchAttribute",
		5,
		`NumConsecutiveWorkflowTaskProblemsToTriggerSearchAttribute is the number of consecutive workflow task problems to trigger the TemporalReportedProblems search attribute.
Setting this to 0 prevents the search attribute from being set when a problem is detected, and unset when the problem is resolved.`,
	)

	BlobSizeLimitError = NewNamespaceIntSetting(
		"limit.blobSize.error",
		2*1024*1024,
		`BlobSizeLimitError is the per event blob size limit`,
	)
	BlobSizeLimitWarn = NewNamespaceIntSetting(
		"limit.blobSize.warn",
		512*1024,
		`BlobSizeLimitWarn is the per event blob size limit for warning`,
	)
	MemoSizeLimitError = NewNamespaceIntSetting(
		"limit.memoSize.error",
		2*1024*1024,
		`MemoSizeLimitError is the per event memo size limit`,
	)
	MemoSizeLimitWarn = NewNamespaceIntSetting(
		"limit.memoSize.warn",
		2*1024,
		`MemoSizeLimitWarn is the per event memo size limit for warning`,
	)
	NumPendingChildExecutionsLimitError = NewNamespaceIntSetting(
		"limit.numPendingChildExecutions.error",
		2000,
		`NumPendingChildExecutionsLimitError is the maximum number of pending child workflows a workflow can have before
StartChildWorkflowExecution commands will fail.`,
	)
	NumPendingActivitiesLimitError = NewNamespaceIntSetting(
		"limit.numPendingActivities.error",
		2000,
		`NumPendingActivitiesLimitError is the maximum number of pending activities a workflow can have before
ScheduleActivityTask will fail.`,
	)
	NumPendingSignalsLimitError = NewNamespaceIntSetting(
		"limit.numPendingSignals.error",
		2000,
		`NumPendingSignalsLimitError is the maximum number of pending signals a workflow can have before
SignalExternalWorkflowExecution commands from this workflow will fail.`,
	)
	NumPendingCancelRequestsLimitError = NewNamespaceIntSetting(
		"limit.numPendingCancelRequests.error",
		2000,
		`NumPendingCancelRequestsLimitError is the maximum number of pending requests to cancel other workflows a workflow can have before
RequestCancelExternalWorkflowExecution commands will fail.`,
	)
	HistorySizeLimitError = NewNamespaceIntSetting(
		"limit.historySize.error",
		50*1024*1024,
		`HistorySizeLimitError is the per workflow execution history size limit`,
	)
	HistorySizeLimitWarn = NewNamespaceIntSetting(
		"limit.historySize.warn",
		10*1024*1024,
		`HistorySizeLimitWarn is the per workflow execution history size limit for warning`,
	)
	HistorySizeSuggestContinueAsNew = NewNamespaceIntSetting(
		"limit.historySize.suggestContinueAsNew",
		4*1024*1024,
		`HistorySizeSuggestContinueAsNew is the workflow execution history size limit to suggest
continue-as-new (in workflow task started event)`,
	)
	HistoryCountLimitError = NewNamespaceIntSetting(
		"limit.historyCount.error",
		50*1024,
		`HistoryCountLimitError is the per workflow execution history event count limit`,
	)
	HistoryCountLimitWarn = NewNamespaceIntSetting(
		"limit.historyCount.warn",
		10*1024,
		`HistoryCountLimitWarn is the per workflow execution history event count limit for warning`,
	)
	MutableStateActivityFailureSizeLimitError = NewNamespaceIntSetting(
		"limit.mutableStateActivityFailureSize.error",
		4*1024,
		`MutableStateActivityFailureSizeLimitError is the per activity failure size limit for workflow mutable state.
If exceeded, failure will be truncated before being stored in mutable state.`,
	)
	MutableStateActivityFailureSizeLimitWarn = NewNamespaceIntSetting(
		"limit.mutableStateActivityFailureSize.warn",
		2*1024,
		`MutableStateActivityFailureSizeLimitWarn is the per activity failure size warning limit for workflow mutable state`,
	)
	MutableStateSizeLimitError = NewGlobalIntSetting(
		"limit.mutableStateSize.error",
		8*1024*1024,
		`MutableStateSizeLimitError is the per workflow execution mutable state size limit in bytes`,
	)
	MutableStateSizeLimitWarn = NewGlobalIntSetting(
		"limit.mutableStateSize.warn",
		1*1024*1024,
		`MutableStateSizeLimitWarn is the per workflow execution mutable state size limit in bytes for warning`,
	)
	MutableStateTombstoneCountLimit = NewGlobalIntSetting(
		"limit.mutableStateTombstoneCountLimit",
		16,
		`MutableStateTombstoneCountLimit is the maximum number of deleted sub state machines tracked in mutable state.`,
	)
	HistoryCountSuggestContinueAsNew = NewNamespaceIntSetting(
		"limit.historyCount.suggestContinueAsNew",
		4*1024,
		`HistoryCountSuggestContinueAsNew is the workflow execution history event count limit to
suggest continue-as-new (in workflow task started event)`,
	)
	HistoryMaxPageSize = NewNamespaceIntSetting(
		"limit.historyMaxPageSize",
		primitives.GetHistoryMaxPageSize,
		`HistoryMaxPageSize is default max size for GetWorkflowExecutionHistory in one page`,
	)
	MaxIDLengthLimit = NewGlobalIntSetting(
		"limit.maxIDLength",
		1000,
		`MaxIDLengthLimit is the length limit for various IDs, including: Namespace, TaskQueue, WorkflowID, ActivityID, TimerID,
WorkflowType, ActivityType, SignalName, MarkerName, ErrorReason/FailureReason/CancelCause, Identity, RequestID`,
	)
	WorkerBuildIdSizeLimit = NewGlobalIntSetting(
		"limit.workerBuildIdSize",
		255,
		`WorkerBuildIdSizeLimit is the byte length limit for a worker build id as used in the rpc methods for updating
the version sets for a task queue.
Do not set this to a value higher than 255 for clusters using SQL based persistence due to predefined VARCHAR
column width.`,
	)
	VersionCompatibleSetLimitPerQueue = NewNamespaceIntSetting(
		"limit.versionCompatibleSetLimitPerQueue",
		10,
		`VersionCompatibleSetLimitPerQueue is the max number of compatible sets allowed in the versioning data for a task
queue. Update requests which would cause the versioning data to exceed this number will fail with a
FailedPrecondition error.`,
	)
	VersionBuildIdLimitPerQueue = NewNamespaceIntSetting(
		"limit.versionBuildIdLimitPerQueue",
		100,
		`VersionBuildIdLimitPerQueue is the max number of build IDs allowed to be defined in the versioning data for a
task queue. Update requests which would cause the versioning data to exceed this number will fail with a
FailedPrecondition error.`,
	)
	AssignmentRuleLimitPerQueue = NewNamespaceIntSetting(
		"limit.wv.AssignmentRuleLimitPerQueue",
		100,
		`AssignmentRuleLimitPerQueue is the max number of Build ID assignment rules allowed to be defined in the
versioning data for a task queue. Update requests which would cause the versioning data to exceed this number
will fail with a FailedPrecondition error.`,
	)
	RedirectRuleLimitPerQueue = NewNamespaceIntSetting(
		"limit.wv.RedirectRuleLimitPerQueue",
		500,
		`RedirectRuleLimitPerQueue is the max number of compatible redirect rules allowed to be defined
in the versioning data for a task queue. Update requests which would cause the versioning data to exceed this
number will fail with a FailedPrecondition error.`,
	)
	RedirectRuleMaxUpstreamBuildIDsPerQueue = NewNamespaceIntSetting(
		"limit.wv.RedirectRuleMaxUpstreamBuildIDsPerQueue",
		50,
		`RedirectRuleMaxUpstreamBuildIDsPerQueue is the max number of compatible redirect rules allowed to be connected
in one chain in the versioning data for a task queue. Update requests which would cause the versioning data
to exceed this number will fail with a FailedPrecondition error.`,
	)
	MatchingDeletedRuleRetentionTime = NewNamespaceDurationSetting(
		"matching.wv.DeletedRuleRetentionTime",
		14*24*time.Hour,
		`MatchingDeletedRuleRetentionTime is the length of time that deleted Version Assignment Rules and
Deleted Redirect Rules will be kept in the DB (with DeleteTimestamp). After this time, the tombstones are deleted at the next time update of versioning data for the task queue.`,
	)
	PollerHistoryTTL = NewNamespaceDurationSetting(
		"matching.PollerHistoryTTL",
		5*time.Minute,
		`PollerHistoryTTL is the time to live for poller histories in the pollerHistory cache of a physical task queue. Poller histories are fetched when
		requiring a list of pollers that polled a given task queue.`,
	)
	ReachabilityBuildIdVisibilityGracePeriod = NewNamespaceDurationSetting(
		"matching.wv.ReachabilityBuildIdVisibilityGracePeriod",
		3*time.Minute,
		`ReachabilityBuildIdVisibilityGracePeriod is the time period for which deleted versioning rules are still considered active
to account for the delay in updating the build id field in visibility. Not yet supported for GetDeploymentReachability. We recommend waiting
at least 2 minutes between changing the current deployment and calling GetDeployment, so that newly started workflow executions using the
recently-current deployment can arrive in visibility.`,
	)
	VersionDrainageStatusVisibilityGracePeriod = NewNamespaceDurationSetting(
		"matching.wv.VersionDrainageStatusVisibilityGracePeriod",
		3*time.Minute,
		`VersionDrainageStatusVisibilityGracePeriod is the time period for which non-current / non-ramping worker deployment versions
are still considered active to account for the delay in updating the build id field in visibility.`,
	)
	VersionDrainageStatusRefreshInterval = NewNamespaceDurationSetting(
		"matching.wv.VersionDrainageStatusRefreshInterval",
		3*time.Minute,
		`VersionDrainageStatusRefreshInterval is the interval at which each draining deployment version refreshes its
Drainage Status by querying visibility for open pinned workflows using that version.`,
	)
	ReachabilityTaskQueueScanLimit = NewGlobalIntSetting(
		"limit.reachabilityTaskQueueScan",
		20,
		`ReachabilityTaskQueueScanLimit limits the number of task queues to scan when responding to a
GetWorkerTaskReachability query.`,
	)
	ReachabilityQueryBuildIdLimit = NewGlobalIntSetting(
		"limit.reachabilityQueryBuildIds",
		5,
		`ReachabilityQueryBuildIdLimit limits the number of build ids that can be requested in a single call to the
DescribeTaskQueue API with ReportTaskQueueReachability==true, or to the GetWorkerTaskReachability API.`,
	)
	ReachabilityCacheOpenWFsTTL = NewGlobalDurationSetting(
		"matching.wv.reachabilityCacheOpenWFsTTL",
		time.Minute,
		`ReachabilityCacheOpenWFsTTL is the TTL for the reachability open workflows cache.`,
	)
	ReachabilityCacheClosedWFsTTL = NewGlobalDurationSetting(
		"matching.wv.reachabilityCacheClosedWFsTTL",
		10*time.Minute,
		`ReachabilityCacheClosedWFsTTL is the TTL for the reachability closed workflows cache.`,
	)
	ReachabilityQuerySetDurationSinceDefault = NewGlobalDurationSetting(
		"frontend.reachabilityQuerySetDurationSinceDefault",
		5*time.Minute,
		`ReachabilityQuerySetDurationSinceDefault is the minimum period since a version set was demoted from being the
queue default before it is considered unreachable by new workflows.
This setting allows some propagation delay of versioning data for the reachability queries, which may happen for
the following reasons:
1. There are no workflows currently marked as open in the visibility store but a worker for the demoted version
is currently processing a task.
2. There are delays in the visibility task processor (which is asynchronous).
3. There's propagation delay of the versioning data between matching nodes.`,
	)
	TaskQueuesPerBuildIdLimit = NewNamespaceIntSetting(
		"limit.taskQueuesPerBuildId",
		20,
		`TaskQueuesPerBuildIdLimit limits the number of task queue names that can be mapped to a single build id.`,
	)

	NexusEndpointNameMaxLength = NewGlobalIntSetting(
		"limit.endpointNameMaxLength",
		200,
		`NexusEndpointNameMaxLength is the maximum length of a Nexus endpoint name.`,
	)
	NexusEndpointExternalURLMaxLength = NewGlobalIntSetting(
		"limit.endpointExternalURLMaxLength",
		4*1024,
		`NexusEndpointExternalURLMaxLength is the maximum length of a Nexus endpoint external target URL.`,
	)
	NexusEndpointDescriptionMaxSize = NewNamespaceIntSetting(
		"limit.endpointDescriptionMaxSize",
		20000,
		`Maximum size of Nexus Endpoint description payload in bytes including data and metadata.`,
	)
	NexusEndpointListDefaultPageSize = NewGlobalIntSetting(
		"limit.endpointListDefaultPageSize",
		100,
		`NexusEndpointListDefaultPageSize is the default page size for listing Nexus endpoints.`,
	)
	NexusEndpointListMaxPageSize = NewGlobalIntSetting(
		"limit.endpointListMaxPageSize",
		1000,
		`NexusEndpointListMaxPageSize is the maximum page size for listing Nexus endpoints.`,
	)

	RemovableBuildIdDurationSinceDefault = NewGlobalDurationSetting(
		"worker.removableBuildIdDurationSinceDefault",
		time.Hour,
		`RemovableBuildIdDurationSinceDefault is the minimum duration since a build id was last default in its containing
set for it to be considered for removal, used by the build id scavenger.
This setting allows some propagation delay of versioning data, which may happen for the following reasons:
1. There are no workflows currently marked as open in the visibility store but a worker for the demoted version
is currently processing a task.
2. There are delays in the visibility task processor (which is asynchronous).
3. There's propagation delay of the versioning data between matching nodes.`,
	)
	BuildIdScavengerVisibilityRPS = NewGlobalFloatSetting(
		"worker.buildIdScavengerVisibilityRPS",
		1.0,
		`BuildIdScavengerVisibilityRPS is the rate limit for visibility calls from the build id scavenger`,
	)

	// keys for frontend
	FrontendAllowedExperiments = NewNamespaceTypedSetting(
		"frontend.allowedExperiments",
		[]string(nil),
		`FrontendAllowedExperiments is a list of experiment names that can be enabled via the temporal-experiment header for a specific namespace.`,
	)
	FrontendHTTPAllowedHosts = NewGlobalTypedSettingWithConverter(
		"frontend.httpAllowedHosts",
		ConvertWildcardStringListToRegexp,
		MatchAnythingRE,
		`HTTP API Requests with a "Host" header matching the allowed hosts will be processed, otherwise rejected.
Wildcards (*) are expanded to allow any substring. By default any Host header is allowed.
Concrete type should be list of strings.`,
	)
	FrontendPersistenceMaxQPS = NewGlobalIntSetting(
		"frontend.persistenceMaxQPS",
		2000,
		`FrontendPersistenceMaxQPS is the max qps frontend host can query DB`,
	)
	FrontendPersistenceGlobalMaxQPS = NewGlobalIntSetting(
		"frontend.persistenceGlobalMaxQPS",
		0,
		`FrontendPersistenceGlobalMaxQPS is the max qps frontend cluster can query DB`,
	)
	FrontendPersistenceNamespaceMaxQPS = NewNamespaceIntSetting(
		"frontend.persistenceNamespaceMaxQPS",
		0,
		`FrontendPersistenceNamespaceMaxQPS is the max qps each namespace on frontend host can query DB`,
	)
	FrontendPersistenceGlobalNamespaceMaxQPS = NewNamespaceIntSetting(
		"frontend.persistenceGlobalNamespaceMaxQPS",
		0,
		`FrontendPersistenceGlobalNamespaceMaxQPS is the max qps each namespace in frontend cluster can query DB`,
	)
	FrontendPersistenceDynamicRateLimitingParams = NewGlobalTypedSetting(
		"frontend.persistenceDynamicRateLimitingParams",
		DefaultDynamicRateLimitingParams,
		`FrontendPersistenceDynamicRateLimitingParams is a struct that contains all adjustable dynamic rate limiting params.
Fields: Enabled, RefreshInterval, LatencyThreshold, ErrorThreshold, RateBackoffStepSize, RateIncreaseStepSize, RateMultiMin, RateMultiMax.
See DynamicRateLimitingParams comments for more details.`,
	)
	FrontendVisibilityMaxPageSize = NewNamespaceIntSetting(
		"frontend.visibilityMaxPageSize",
		1000,
		`FrontendVisibilityMaxPageSize is default max size for ListWorkflowExecutions in one page`,
	)
	FrontendHistoryMaxPageSize = NewNamespaceIntSetting(
		"frontend.historyMaxPageSize",
		primitives.GetHistoryMaxPageSize,
		`FrontendHistoryMaxPageSize is default max size for GetWorkflowExecutionHistory in one page`,
	)
	FrontendRPS = NewGlobalIntSetting(
		"frontend.rps",
		2400,
		`FrontendRPS is workflow rate limit per second per-instance`,
	)
	FrontendGlobalRPS = NewGlobalIntSetting(
		"frontend.globalRPS",
		0,
		`FrontendGlobalRPS is workflow rate limit per second for the whole cluster`,
	)
	FrontendNamespaceReplicationInducingAPIsRPS = NewGlobalIntSetting(
		"frontend.rps.namespaceReplicationInducingAPIs",
		20,
		`FrontendNamespaceReplicationInducingAPIsRPS limits the per second request rate for namespace replication inducing
APIs (e.g. RegisterNamespace, UpdateNamespace, UpdateWorkerBuildIdCompatibility).
This config is EXPERIMENTAL and may be changed or removed in a later release.`,
	)
	FrontendMaxNamespaceRPSPerInstance = NewNamespaceIntSetting(
		"frontend.namespaceRPS",
		2400,
		`FrontendMaxNamespaceRPSPerInstance is workflow namespace rate limit per second`,
	)
	FrontendMaxNamespaceBurstRatioPerInstance = NewNamespaceFloatSetting(
		"frontend.namespaceBurstRatio",
		2,
		`FrontendMaxNamespaceBurstRatioPerInstance is workflow namespace burst limit as a ratio of namespace RPS. The RPS
used here will be the effective RPS from global and per-instance limits. The value must be 1 or higher.`,
	)
	FrontendMaxConcurrentLongRunningRequestsPerInstance = NewNamespaceIntSetting(
		"frontend.namespaceCount",
		1200,
		`FrontendMaxConcurrentLongRunningRequestsPerInstance limits concurrent long-running requests per-instance,
per-API. Example requests include long-poll requests, and 'Query' requests (which need to wait for WFTs). The
limit is applied individually to each API method. This value is ignored if
FrontendGlobalMaxConcurrentLongRunningRequests is greater than zero. Warning: setting this to zero will cause all
long-running requests to fail. The name 'frontend.namespaceCount' is kept for backwards compatibility with
existing deployments even though it is a bit of a misnomer. This does not limit the number of namespaces; it is a
per-_namespace_ limit on the _count_ of long-running requests. Requests are only throttled when the limit is
exceeded, not when it is only reached.`,
	)
	FrontendGlobalMaxConcurrentLongRunningRequests = NewNamespaceIntSetting(
		"frontend.globalNamespaceCount",
		0,
		`FrontendGlobalMaxConcurrentLongRunningRequests limits concurrent long-running requests across all frontend
instances in the cluster, for a given namespace, per-API method. If this is set to 0 (the default), then it is
ignored. The name 'frontend.globalNamespaceCount' is kept for consistency with the per-instance limit name,
'frontend.namespaceCount'.`,
	)
	FrontendMaxNamespaceVisibilityRPSPerInstance = NewNamespaceIntSetting(
		"frontend.namespaceRPS.visibility",
		10,
		`FrontendMaxNamespaceVisibilityRPSPerInstance is namespace rate limit per second for visibility APIs.
This config is EXPERIMENTAL and may be changed or removed in a later release.`,
	)
	FrontendMaxNamespaceNamespaceReplicationInducingAPIsRPSPerInstance = NewNamespaceIntSetting(
		"frontend.namespaceRPS.namespaceReplicationInducingAPIs",
		1,
		`FrontendMaxNamespaceNamespaceReplicationInducingAPIsRPSPerInstance is a per host/per namespace RPS limit for
namespace replication inducing APIs (e.g. RegisterNamespace, UpdateNamespace, UpdateWorkerBuildIdCompatibility).
This config is EXPERIMENTAL and may be changed or removed in a later release.`,
	)
	FrontendMaxNamespaceVisibilityBurstRatioPerInstance = NewNamespaceFloatSetting(
		"frontend.namespaceBurstRatio.visibility",
		1,
		`FrontendMaxNamespaceVisibilityBurstRatioPerInstance is namespace burst limit for visibility APIs as a ratio of
namespace visibility RPS. The RPS used here will be the effective RPS from global and per-instance limits. This
config is EXPERIMENTAL and may be changed or removed in a later release. The value must be 1 or higher.`,
	)
	FrontendMaxNamespaceNamespaceReplicationInducingAPIsBurstRatioPerInstance = NewNamespaceFloatSetting(
		"frontend.namespaceBurstRatio.namespaceReplicationInducingAPIs",
		10,
		`FrontendMaxNamespaceNamespaceReplicationInducingAPIsBurstRatioPerInstance is a per host/per namespace burst limit for
namespace replication inducing APIs (e.g. RegisterNamespace, UpdateNamespace, UpdateWorkerBuildIdCompatibility)
as a ratio of namespace ReplicationInducingAPIs RPS. The RPS used here will be the effective RPS from global and
per-instance limits. This config is EXPERIMENTAL and may be changed or removed in a later release. The value must
be 1 or higher.`,
	)
	FrontendGlobalNamespaceRPS = NewNamespaceIntSetting(
		"frontend.globalNamespaceRPS",
		0,
		`FrontendGlobalNamespaceRPS is workflow namespace rate limit per second for the whole cluster.
The limit is evenly distributed among available frontend service instances.
If this is set, it overwrites per instance limit "frontend.namespaceRPS".`,
	)
	InternalFrontendGlobalNamespaceRPS = NewNamespaceIntSetting(
		"internal-frontend.globalNamespaceRPS",
		0,
		`InternalFrontendGlobalNamespaceRPS is workflow namespace rate limit per second across
all internal-frontends.`,
	)
	FrontendGlobalNamespaceVisibilityRPS = NewNamespaceIntSetting(
		"frontend.globalNamespaceRPS.visibility",
		0,
		`FrontendGlobalNamespaceVisibilityRPS is workflow namespace rate limit per second for the whole cluster for visibility API.
The limit is evenly distributed among available frontend service instances.
If this is set, it overwrites per instance limit "frontend.namespaceRPS.visibility".
This config is EXPERIMENTAL and may be changed or removed in a later release.`,
	)
	FrontendGlobalNamespaceNamespaceReplicationInducingAPIsRPS = NewNamespaceIntSetting(
		"frontend.globalNamespaceRPS.namespaceReplicationInducingAPIs",
		10,
		`FrontendGlobalNamespaceNamespaceReplicationInducingAPIsRPS is a cluster global, per namespace RPS limit for
namespace replication inducing APIs (e.g. RegisterNamespace, UpdateNamespace, UpdateWorkerBuildIdCompatibility).
The limit is evenly distributed among available frontend service instances.
If this is set, it overwrites the per instance limit configured with
"frontend.namespaceRPS.namespaceReplicationInducingAPIs".
This config is EXPERIMENTAL and may be changed or removed in a later release.`,
	)
	InternalFrontendGlobalNamespaceVisibilityRPS = NewNamespaceIntSetting(
		"internal-frontend.globalNamespaceRPS.visibility",
		0,
		`InternalFrontendGlobalNamespaceVisibilityRPS is workflow namespace rate limit per second
across all internal-frontends.
This config is EXPERIMENTAL and may be changed or removed in a later release.`,
	)
	FrontendThrottledLogRPS = NewGlobalIntSetting(
		"frontend.throttledLogRPS",
		20,
		`FrontendThrottledLogRPS is the rate limit on number of log messages emitted per second for throttled logger`,
	)
	FrontendShutdownDrainDuration = NewGlobalDurationSetting(
		"frontend.shutdownDrainDuration",
		0*time.Second,
		`FrontendShutdownDrainDuration is the duration of traffic drain during shutdown`,
	)
	FrontendShutdownFailHealthCheckDuration = NewGlobalDurationSetting(
		"frontend.shutdownFailHealthCheckDuration",
		0*time.Second,
		`FrontendShutdownFailHealthCheckDuration is the duration of shutdown failure detection`,
	)
	FrontendMaxBadBinaries = NewNamespaceIntSetting(
		"frontend.maxBadBinaries",
		10,
		`FrontendMaxBadBinaries is the max number of bad binaries in namespace config`,
	)
	FrontendMaskInternalErrorDetails = NewNamespaceBoolSetting(
		"frontend.maskInternalErrorDetails",
		true,
		`MaskInternalOrUnknownErrors is whether to replace internal/unknown errors with default error`,
	)
	HistoryHostErrorPercentage = NewGlobalFloatSetting(
		"frontend.historyHostErrorPercentage",
		0.5,
		`HistoryHostErrorPercentage is the proportion of hosts that are unhealthy through observation external to the host and internal host health checks`,
	)
	HistoryHostSelfErrorProportion = NewGlobalFloatSetting(
		"frontend.historyHostSelfErrorProportion",
		0.05,
		`HistoryHostStartingProportion is the proportion of hosts that have marked themselves as not ready -- this could due to waiting to acquire all shards on startup, or an internal health check failure`,
	)
	SendRawWorkflowHistory = NewNamespaceBoolSetting(
		"frontend.sendRawWorkflowHistory",
		false,
		`SendRawWorkflowHistory is whether to enable raw history retrieving`,
	)
	SearchAttributesNumberOfKeysLimit = NewNamespaceIntSetting(
		"frontend.searchAttributesNumberOfKeysLimit",
		100,
		`SearchAttributesNumberOfKeysLimit is the limit of number of keys`,
	)
	SearchAttributesSizeOfValueLimit = NewNamespaceIntSetting(
		"frontend.searchAttributesSizeOfValueLimit",
		2*1024,
		`SearchAttributesSizeOfValueLimit is the size limit of each value`,
	)
	SearchAttributesTotalSizeLimit = NewNamespaceIntSetting(
		"frontend.searchAttributesTotalSizeLimit",
		40*1024,
		`SearchAttributesTotalSizeLimit is the size limit of the whole map`,
	)
	VisibilityArchivalQueryMaxPageSize = NewGlobalIntSetting(
		"frontend.visibilityArchivalQueryMaxPageSize",
		10000,
		`VisibilityArchivalQueryMaxPageSize is the maximum page size for a visibility archival query`,
	)
	EnableServerVersionCheck = NewGlobalBoolSetting(
		"frontend.enableServerVersionCheck",
		os.Getenv("TEMPORAL_VERSION_CHECK_DISABLED") == "",
		`EnableServerVersionCheck is a flag that controls whether or not periodic version checking is enabled`,
	)
	EnableTokenNamespaceEnforcement = NewGlobalBoolSetting(
		"frontend.enableTokenNamespaceEnforcement",
		true,
		`EnableTokenNamespaceEnforcement enables enforcement that namespace in completion token matches namespace of the request`,
	)
	DisableListVisibilityByFilter = NewNamespaceBoolSetting(
		"frontend.disableListVisibilityByFilter",
		false,
		`DisableListVisibilityByFilter is config to disable list open/close workflow using filter`,
	)
	ExposeAuthorizerErrors = NewGlobalBoolSetting(
		"frontend.exposeAuthorizerErrors",
		false,
		`ExposeAuthorizerErrors controls whether the frontend authorization interceptor will pass through errors returned by
the Authorizer component. If false, a generic PermissionDenied error without details will be returned. Default false.`,
	)
	KeepAliveMinTime = NewGlobalDurationSetting(
		"frontend.keepAliveMinTime",
		10*time.Second,
		`KeepAliveMinTime is the minimum amount of time a client should wait before sending a keepalive ping.`,
	)
	KeepAlivePermitWithoutStream = NewGlobalBoolSetting(
		"frontend.keepAlivePermitWithoutStream",
		true,
		`KeepAlivePermitWithoutStream If true, server allows keepalive pings even when there are no active
streams(RPCs). If false, and client sends ping when there are no active
streams, server will send GOAWAY and close the connection.`,
	)
	KeepAliveMaxConnectionIdle = NewGlobalDurationSetting(
		"frontend.keepAliveMaxConnectionIdle",
		2*time.Minute,
		`KeepAliveMaxConnectionIdle is a duration for the amount of time after which an
idle connection would be closed by sending a GoAway. Idleness duration is
defined since the most recent time the number of outstanding RPCs became
zero or the connection establishment.`,
	)
	KeepAliveMaxConnectionAge = NewGlobalDurationSetting(
		"frontend.keepAliveMaxConnectionAge",
		5*time.Minute,
		`KeepAliveMaxConnectionAge is a duration for the maximum amount of time a
connection may exist before it will be closed by sending a GoAway. A
random jitter of +/-10% will be added to MaxConnectionAge to spread out
connection storms.`,
	)
	KeepAliveMaxConnectionAgeGrace = NewGlobalDurationSetting(
		"frontend.keepAliveMaxConnectionAgeGrace",
		70*time.Second,
		`KeepAliveMaxConnectionAgeGrace is an additive period after MaxConnectionAge after
which the connection will be forcibly closed.`,
	)
	KeepAliveTime = NewGlobalDurationSetting(
		"frontend.keepAliveTime",
		1*time.Minute,
		`KeepAliveTime After a duration of this time if the server doesn't see any activity it
pings the client to see if the transport is still alive.
If set below 1s, a minimum value of 1s will be used instead.`,
	)
	KeepAliveTimeout = NewGlobalDurationSetting(
		"frontend.keepAliveTimeout",
		10*time.Second,
		`KeepAliveTimeout After having pinged for keepalive check, the server waits for a duration
of Timeout and if no activity is seen even after that the connection is closed.`,
	)
	FrontendEnableSchedules = NewNamespaceBoolSetting(
		"frontend.enableSchedules",
		true,
		`FrontendEnableSchedules enables schedule-related RPCs in the frontend`,
	)
	// [cleanup-wv-pre-release]
	EnableDeployments = NewNamespaceBoolSetting(
		"system.enableDeployments",
		false,
		`EnableDeployments enables deployments (deprecated versioning v3 pre-release) in all services,
including deployment-related RPCs in the frontend, deployment entity workflows in the worker,
and deployment interaction in matching and history.`,
	)
	EnableDeploymentVersions = NewNamespaceBoolSetting(
		"system.enableDeploymentVersions",
		true,
		`EnableDeploymentVersions enables deployment versions (versioning v3) in all services,
including deployment-related RPCs in the frontend, deployment version entity workflows in the worker,
and deployment interaction in matching and history.`,
	)
	UseRevisionNumberForWorkerVersioning = NewNamespaceBoolSetting(
		"system.useRevisionNumberForWorkerVersioning",
		false,
		`UseRevisionNumberForWorkerVersioning enables the use of revision number to resolve consistency problems that may arise during task dispatch time.`,
	)
	EnableNexus = NewGlobalBoolSetting(
		"system.enableNexus",
		true,
		`Toggles all Nexus functionality on the server. Note that toggling this requires restarting server hosts for it
		to take effect.`,
	)

	AllowDeleteNamespaceIfNexusEndpointTarget = NewGlobalBoolSetting(
		"frontend.allowDeleteNamespaceIfNexusEndpointTarget",
		false,
		`If set to true (default is false), namespaces that are Nexus endpoint targets will be prevented from being deleted.`,
	)

	RefreshNexusEndpointsLongPollTimeout = NewGlobalDurationSetting(
		"system.refreshNexusEndpointsLongPollTimeout",
		5*time.Minute,
		`RefreshNexusEndpointsLongPollTimeout is the maximum duration of background long poll requests to update Nexus endpoints.`,
	)
	RefreshNexusEndpointsMinWait = NewGlobalDurationSetting(
		"system.refreshNexusEndpointsMinWait",
		1*time.Second,
		`RefreshNexusEndpointsMinWait is the minimum wait time between background long poll requests to update Nexus endpoints.`,
	)
	NexusReadThroughCacheSize = NewGlobalIntSetting(
		"system.nexusReadThroughCacheSize",
		100,
		`The size of the Nexus endpoint registry's readthrough LRU cache - the cache is a secondary cache and is only
used when the first cache layer has a miss. Requires server restart for change to be applied.`,
	)
	NexusReadThroughCacheTTL = NewGlobalDurationSetting(
		"system.nexusReadThroughCacheTTL",
		30*time.Second,
		`The TTL of the Nexus endpoint registry's readthrough LRU cache - the cache is a secondary cache and is only
used when the first cache layer has a miss. Requires server restart for change to be applied.`,
	)
	FrontendNexusRequestHeadersBlacklist = NewGlobalTypedSettingWithConverter(
		"frontend.nexusRequestHeadersBlacklist",
		ConvertWildcardStringListToRegexp,
		MatchNothingRE,
		`Nexus request headers to be removed before being sent to a user handler.
Wildcards (*) are expanded to allow any substring. By default blacklist is empty.
Concrete type should be list of strings.`,
	)
	FrontendNexusForwardRequestUseEndpointDispatch = NewGlobalBoolSetting(
		"frontend.nexusForwardRequestUseEndpointDispatch",
		false,
		`!EXPERIMENTAL! NB: This config will be removed in a future release. Controls whether to use Nexus
task dispatch by endpoint URLs for forwarded Nexus requests. If set to true, forwarded requests will use the same
dispatch type (by endpoint or by namespace + task queue) as the original request. If false, dispatch by namespace + task
queue will always be used for forwarded requests. Defaults to false because Nexus endpoints do not support replication,
so forwarding by endpoint ID will not work out of the box.`,
	)
	FrontendCallbackURLMaxLength = NewNamespaceIntSetting(
		"frontend.callbackURLMaxLength",
		1000,
		`FrontendCallbackURLMaxLength is the maximum length of callback URL`,
	)
	FrontendCallbackHeaderMaxSize = NewNamespaceIntSetting(
		"frontend.callbackHeaderMaxLength",
		8*1024,
		`FrontendCallbackHeaderMaxSize is the maximum accumulated size of callback header keys and values`,
	)
	MaxCallbacksPerWorkflow = NewNamespaceIntSetting(
		"system.maxCallbacksPerWorkflow",
		32,
		`MaxCallbacksPerWorkflow is the maximum number of callbacks that can be attached to a workflow.`,
	)
	// NOTE (seankane): MaxCHASMCallbacksPerWorkflow is temporary, this will be removed and replaced with MaxCallbacksPerWorkflow
	// once CHASM is fully enabled
	MaxCHASMCallbacksPerWorkflow = NewNamespaceIntSetting(
		"system.maxCHASMCallbacksPerWorkflow",
		2000,
		`MaxCHASMCallbacksPerWorkflow is the maximum number of callbacks that can be attached to a workflow when using the CHASM implementation.`,
	)
	FrontendLinkMaxSize = NewNamespaceIntSetting(
		"frontend.linkMaxSize",
		4000,
		`Maximum size in bytes of temporal.api.common.v1.Link object in an API request.`,
	)
	FrontendMaxLinksPerRequest = NewNamespaceIntSetting(
		"frontend.maxlinksPerRequest",
		10,
		`Maximum number of links allowed to be attached via a single API request.`,
	)
	FrontendMaxConcurrentBatchOperationPerNamespace = NewNamespaceIntSetting(
		"frontend.MaxConcurrentBatchOperationPerNamespace",
		1,
		`FrontendMaxConcurrentBatchOperationPerNamespace is the max concurrent batch operation job count per namespace`,
	)
	FrontendMaxExecutionCountBatchOperationPerNamespace = NewNamespaceIntSetting(
		"frontend.MaxExecutionCountBatchOperationPerNamespace",
		1000,
		`FrontendMaxExecutionCountBatchOperationPerNamespace is the max execution count batch operation supports per namespace`,
	)
	FrontendEnableBatcher = NewNamespaceBoolSetting(
		"frontend.enableBatcher",
		true,
		`FrontendEnableBatcher enables batcher-related RPCs in the frontend`,
	)
	FrontendMaxConcurrentAdminBatchOperationPerNamespace = NewNamespaceIntSetting(
		"frontend.MaxConcurrentAdminBatchOperationPerNamespace",
		1,
		`FrontendMaxConcurrentAdminBatchOperationPerNamespace is the max concurrent admin batch operation job count per namespace`,
	)

	FrontendEnableUpdateWorkflowExecution = NewNamespaceBoolSetting(
		"frontend.enableUpdateWorkflowExecution",
		true,
		`FrontendEnableUpdateWorkflowExecution enables UpdateWorkflowExecution API in the frontend.`,
	)

	FrontendEnableUpdateWorkflowExecutionAsyncAccepted = NewNamespaceBoolSetting(
		"frontend.enableUpdateWorkflowExecutionAsyncAccepted",
		true,
		`FrontendEnableUpdateWorkflowExecutionAsyncAccepted enables the UpdateWorkflowExecution API
to allow waiting on the "Accepted" lifecycle stage.`,
	)

	FrontendEnableWorkerVersioningDataAPIs = NewNamespaceBoolSetting(
		"frontend.workerVersioningDataAPIs",
		false,
		`FrontendEnableWorkerVersioningDataAPIs enables worker versioning data read / write APIs.`,
	)
	FrontendEnableWorkerVersioningWorkflowAPIs = NewNamespaceBoolSetting(
		"frontend.workerVersioningWorkflowAPIs",
		true,
		`FrontendEnableWorkerVersioningWorkflowAPIs enables worker versioning in workflow progress APIs.`,
	)
	FrontendEnableWorkerVersioningRuleAPIs = NewNamespaceBoolSetting(
		"frontend.workerVersioningRuleAPIs",
		false,
		`FrontendEnableWorkerVersioningRuleAPIs enables worker versioning in workflow progress APIs.`,
	)

	DeleteNamespaceDeleteActivityRPS = NewGlobalIntSetting(
		"frontend.deleteNamespaceDeleteActivityRPS",
		100,
		`DeleteNamespaceDeleteActivityRPS is an RPS per every parallel delete executions activity.
Total RPS is equal to DeleteNamespaceDeleteActivityRPS * DeleteNamespaceConcurrentDeleteExecutionsActivities.
Default value is 100. Despite starting with 'frontend.' this setting is used by a worker and can be changed while namespace is deleted.`,
	)
	DeleteNamespacePageSize = NewGlobalIntSetting(
		"frontend.deleteNamespaceDeletePageSize",
		1000,
		`DeleteNamespacePageSize is a page size to read executions from visibility for delete executions activity.
Default value is 1000. Read once before delete of specified namespace is started.`,
	)
	DeleteNamespacePagesPerExecution = NewGlobalIntSetting(
		"frontend.deleteNamespacePagesPerExecution",
		256,
		`DeleteNamespacePagesPerExecution is a number of pages before returning ContinueAsNew from delete executions activity.
Default value is 256. Read once before delete of specified namespace is started.`,
	)
	DeleteNamespaceConcurrentDeleteExecutionsActivities = NewGlobalIntSetting(
		"frontend.deleteNamespaceConcurrentDeleteExecutionsActivities",
		4,
		`DeleteNamespaceConcurrentDeleteExecutionsActivities is a number of concurrent delete executions activities.
Must be not greater than 256 and number of worker cores in the cluster.
Default is 4. Read once before delete of specified namespace is started.`,
	)
	DeleteNamespaceNamespaceDeleteDelay = NewGlobalDurationSetting(
		"frontend.deleteNamespaceNamespaceDeleteDelay",
		0*time.Hour,
		`DeleteNamespaceNamespaceDeleteDelay is a duration for how long namespace stays in database
after all namespace resources (i.e. workflow executions) are deleted.
Default is 0, means, namespace will be deleted immediately.`,
	)
	ProtectedNamespaces = NewGlobalTypedSetting(
		"worker.protectedNamespaces",
		([]string)(nil),
		`List of namespace names that can't be deleted.`,
	)

	MatchingRPS = NewGlobalIntSetting(
		"matching.rps",
		1200,
		`MatchingRPS is request rate per second for each matching host`,
	)
	MatchingPersistenceMaxQPS = NewGlobalIntSetting(
		"matching.persistenceMaxQPS",
		3000,
		`MatchingPersistenceMaxQPS is the max qps matching host can query DB`,
	)
	MatchingPersistenceGlobalMaxQPS = NewGlobalIntSetting(
		"matching.persistenceGlobalMaxQPS",
		0,
		`MatchingPersistenceGlobalMaxQPS is the max qps matching cluster can query DB`,
	)
	MatchingPersistenceNamespaceMaxQPS = NewNamespaceIntSetting(
		"matching.persistenceNamespaceMaxQPS",
		0,
		`MatchingPersistenceNamespaceMaxQPS is the max qps each namespace on matching host can query DB`,
	)
	MatchingPersistenceGlobalNamespaceMaxQPS = NewNamespaceIntSetting(
		"matching.persistenceGlobalNamespaceMaxQPS",
		0,
		`MatchingPersistenceNamespaceMaxQPS is the max qps each namespace in matching cluster can query DB`,
	)
	MatchingPersistenceDynamicRateLimitingParams = NewGlobalTypedSetting(
		"matching.persistenceDynamicRateLimitingParams",
		DefaultDynamicRateLimitingParams,
		`MatchingPersistenceDynamicRateLimitingParams is a struct that contains all adjustable dynamic rate limiting params.
Fields: Enabled, RefreshInterval, LatencyThreshold, ErrorThreshold, RateBackoffStepSize, RateIncreaseStepSize, RateMultiMin, RateMultiMax.
See DynamicRateLimitingParams comments for more details.`,
	)
	MatchingMinTaskThrottlingBurstSize = NewTaskQueueIntSetting(
		"matching.minTaskThrottlingBurstSize",
		1,
		`MatchingMinTaskThrottlingBurstSize is the minimum burst size for task queue throttling`,
	)
	MatchingGetTasksBatchSize = NewTaskQueueIntSetting(
		"matching.getTasksBatchSize",
		1000,
		`How many backlog tasks to read from persistence at once`,
	)
	MatchingGetTasksReloadAt = NewTaskQueueIntSetting(
		"matching.getTasksReloadAt",
		100,
		`Reload a batch of tasks when there are this many remaining. Must be less than MatchingGetTasksBatchSize. (Requires new matcher.)`,
	)
	MatchingLongPollExpirationInterval = NewTaskQueueDurationSetting(
		"matching.longPollExpirationInterval",
		time.Minute,
		`MatchingLongPollExpirationInterval is the long poll expiration interval in the matching service`,
	)
	// TODO(pri): old matcher cleanup
	MatchingSyncMatchWaitDuration = NewTaskQueueDurationSetting(
		"matching.syncMatchWaitDuration",
		200*time.Millisecond,
		`MatchingSyncMatchWaitDuration is to wait time for sync match`,
	)
	MatchingHistoryMaxPageSize = NewNamespaceIntSetting(
		"matching.historyMaxPageSize",
		primitives.GetHistoryMaxPageSize,
		`MatchingHistoryMaxPageSize is the maximum page size of history events returned on PollWorkflowTaskQueue requests`,
	)
	MatchingUpdateAckInterval = NewTaskQueueDurationSettingWithConstrainedDefault(
		"matching.updateAckInterval",
		[]TypedConstrainedValue[time.Duration]{

			{
				Constraints: Constraints{
					TaskQueueName: primitives.PerNSWorkerTaskQueue,
				},
				Value: 5 * time.Minute,
			},

			{
				Value: 1 * time.Minute,
			},
		},
		`MatchingUpdateAckInterval is the interval for update ack`,
	)
	MatchingMaxTaskQueueIdleTime = NewTaskQueueDurationSetting(
		"matching.maxTaskQueueIdleTime",
		5*time.Minute,
		`MatchingMaxTaskQueueIdleTime is the time after which an idle task queue will be unloaded.
Note: this should be greater than matching.longPollExpirationInterval and matching.getUserDataLongPollTimeout.`,
	)
	MatchingOutstandingTaskAppendsThreshold = NewTaskQueueIntSetting(
		"matching.outstandingTaskAppendsThreshold",
		250,
		`MatchingOutstandingTaskAppendsThreshold is the threshold for outstanding task appends`,
	)
	MatchingMaxTaskBatchSize = NewTaskQueueIntSetting(
		"matching.maxTaskBatchSize",
		100,
		`MatchingMaxTaskBatchSize is max batch size for task writer`,
	)
	MatchingMaxTaskDeleteBatchSize = NewTaskQueueIntSetting(
		"matching.maxTaskDeleteBatchSize",
		100,
		`MatchingMaxTaskDeleteBatchSize is the max batch size for range deletion of tasks`,
	)
	MatchingTaskDeleteInterval = NewTaskQueueDurationSetting(
		"matching.taskDeleteInterval",
		15*time.Second,
		`MatchingTaskDeleteInterval is the minimum interval between task range deletions`,
	)
	MatchingThrottledLogRPS = NewGlobalIntSetting(
		"matching.throttledLogRPS",
		20,
		`MatchingThrottledLogRPS is the rate limit on number of log messages emitted per second for throttled logger`,
	)
	MatchingNumTaskqueueWritePartitions = NewTaskQueueIntSettingWithConstrainedDefault(
		"matching.numTaskqueueWritePartitions",
		defaultNumTaskQueuePartitions,
		`MatchingNumTaskqueueWritePartitions is the number of write partitions for a task queue`,
	)
	MatchingNumTaskqueueReadPartitions = NewTaskQueueIntSettingWithConstrainedDefault(
		"matching.numTaskqueueReadPartitions",
		defaultNumTaskQueuePartitions,
		`MatchingNumTaskqueueReadPartitions is the number of read partitions for a task queue`,
	)
	MetricsBreakdownByTaskQueue = NewTaskQueueBoolSetting(
		"metrics.breakdownByTaskQueue",
		true,
		`MetricsBreakdownByTaskQueue determines if the 'taskqueue' tag in Matching and History metrics should
contain the actual TQ name or a generic __omitted__ value. Disable this option if the cardinality is too high for your
observability stack. Disabling this option will disable all the per-Task Queue gauges such as backlog lag, count, and age.`,
	)
	MetricsBreakdownByPartition = NewTaskQueueBoolSetting(
		"metrics.breakdownByPartition",
		true,
		`MetricsBreakdownByPartition determines if the 'partition' tag in Matching metrics should
contain the actual normal partition ID or a generic __normal__ value. Regardless of this config, the tag value for sticky
queues will be "__sticky__". Disable this option if the partition cardinality is too high for your
observability stack. Disabling this option will disable all the per-Task Queue gauges such as backlog lag, count, and age.`,
	)
	MetricsBreakdownByBuildID = NewTaskQueueBoolSetting(
		"metrics.breakdownByBuildID",
		true,
		`MetricsBreakdownByBuildID determines if the 'worker_version' tag in Matching metrics should
contain the actual Worker Deployment Version or a generic "__versioned__" value. Regardless of this config, the tag value for unversioned
queues will be "__unversioned__". Disable this option if the version cardinality is too high for your
observability stack. Disabling this option will disable all the per-Task Queue gauges such as backlog lag, count, and age
for VERSIONED queues.`,
	)
	MatchingForwarderMaxOutstandingPolls = NewTaskQueueIntSetting(
		"matching.forwarderMaxOutstandingPolls",
		1,
		`MatchingForwarderMaxOutstandingPolls is the max number of inflight polls from the forwarder`,
	)
	MatchingForwarderMaxOutstandingTasks = NewTaskQueueIntSetting(
		"matching.forwarderMaxOutstandingTasks",
		1,
		`MatchingForwarderMaxOutstandingTasks is the max number of inflight addTask/queryTask from the forwarder`,
	)
	MatchingForwarderMaxRatePerSecond = NewTaskQueueFloatSetting(
		"matching.forwarderMaxRatePerSecond",
		10,
		`MatchingForwarderMaxRatePerSecond is the max rate at which add/query can be forwarded`,
	)
	MatchingForwarderMaxChildrenPerNode = NewTaskQueueIntSetting(
		"matching.forwarderMaxChildrenPerNode",
		20,
		`MatchingForwarderMaxChildrenPerNode is the max number of children per node in the task queue partition tree`,
	)
	MatchingAlignMembershipChange = NewGlobalDurationSetting(
		"matching.alignMembershipChange",
		0*time.Second,
		`MatchingAlignMembershipChange is a duration to align matching's membership changes to.
This can help reduce effects of task queue movement.`,
	)
	MatchingShutdownDrainDuration = NewGlobalDurationSetting(
		"matching.shutdownDrainDuration",
		0*time.Second,
		`MatchingShutdownDrainDuration is the duration of traffic drain during shutdown`,
	)
	MatchingGetUserDataLongPollTimeout = NewGlobalDurationSetting(
		"matching.getUserDataLongPollTimeout",
		5*time.Minute-10*time.Second,
		`MatchingGetUserDataLongPollTimeout is the max length of long polls for GetUserData calls between partitions.`,
	)
	MatchingGetUserDataRefresh = NewGlobalDurationSetting(
		"matching.getUserDataRefresh",
		5*time.Minute,
		`MatchingGetUserDataRefresh is how often the user data owner refreshes data from persistence.`,
	)
	MatchingBacklogNegligibleAge = NewTaskQueueDurationSetting(
		"matching.backlogNegligibleAge",
		5*time.Second,
		`MatchingBacklogNegligibleAge if the head of backlog gets older than this we stop sync match and
forwarding to ensure more equal dispatch order among partitions.`,
	)
	MatchingMaxWaitForPollerBeforeFwd = NewTaskQueueDurationSetting(
		"matching.maxWaitForPollerBeforeFwd",
		200*time.Millisecond,
		`MatchingMaxWaitForPollerBeforeFwd in presence of a non-negligible backlog, we resume forwarding tasks if the
duration since last poll exceeds this threshold.`,
	)
	QueryPollerUnavailableWindow = NewGlobalDurationSetting(
		"matching.queryPollerUnavailableWindow",
		20*time.Second,
		`QueryPollerUnavailableWindow WF Queries are rejected after a while if no poller has been seen within the window`,
	)
	MatchingListNexusEndpointsLongPollTimeout = NewGlobalDurationSetting(
		"matching.listNexusEndpointsLongPollTimeout",
		5*time.Minute-10*time.Second,
		`MatchingListNexusEndpointsLongPollTimeout is the max length of long polls for ListNexusEndpoints calls.`,
	)
	MatchingNexusEndpointsRefreshInterval = NewGlobalDurationSetting(
		"matching.nexusEndpointsRefreshInterval",
		10*time.Second,
		`Time to wait between calls to check that the in-memory view of Nexus endpoints matches the persisted state.`,
	)
	MatchingMembershipUnloadDelay = NewGlobalDurationSetting(
		"matching.membershipUnloadDelay",
		500*time.Millisecond,
		`MatchingMembershipUnloadDelay is how long to wait to re-confirm loss of ownership before unloading a task queue.
Set to zero to disable proactive unload.`,
	)
	MatchingQueryWorkflowTaskTimeoutLogRate = NewTaskQueueFloatSetting(
		"matching.queryWorkflowTaskTimeoutLogRate",
		0.0,
		`MatchingQueryWorkflowTaskTimeoutLogRate defines the sampling rate for logs when a query workflow task times out. Since
these log lines can be noisy, we want to be able to turn on and sample selectively for each affected namespace.`,
	)
	TaskQueueInfoByBuildIdTTL = NewTaskQueueDurationSetting(
		"matching.TaskQueueInfoByBuildIdTTL",
		5*time.Second,
		`TaskQueueInfoByBuildIdTTL serves as a TTL for the cache holding DescribeTaskQueue partition results`,
	)
	MatchingDeploymentWorkflowVersion = NewNamespaceIntSetting(
		"matching.deploymentWorkflowVersion",
		0,
		`MatchingDeploymentWorkflowVersion controls what version of the logic should the manager workflows use.`,
	)
	MatchingMaxTaskQueuesInDeployment = NewNamespaceIntSetting(
		"matching.maxTaskQueuesInDeployment",
		1000,
		`MatchingMaxTaskQueuesInDeployment represents the maximum number of task-queues that can be registed in a single deployment`,
	)
	MatchingMaxDeployments = NewNamespaceIntSetting(
		"matching.maxDeployments",
		100,
		`MatchingMaxDeployments represents the maximum number of worker deployments that can be registered in a single namespace`,
	)
	MatchingMaxVersionsInDeployment = NewNamespaceIntSetting(
		"matching.maxVersionsInDeployment",
		100,
		`MatchingMaxVersionsInDeployment represents the maximum number of versions that can be registered in a single worker deployment`,
	)
	MatchingMaxVersionsInTaskQueue = NewNamespaceIntSetting(
		"matching.maxVersionsInTaskQueue",
		200,
		`MatchingMaxVersionsInTaskQueue represents the maximum number of versions that can be registered in a single task queue.
 Should be larger than MatchingMaxVersionsInDeployment because a task queue can be in versions spanning across more than one deployments.`,
	)
	MatchingMaxTaskQueuesInDeploymentVersion = NewNamespaceIntSetting(
		"matching.maxTaskQueuesInDeploymentVersion",
		100,
		`MatchingMaxTaskQueuesInDeployment represents the maximum number of task-queues that can be registered in a single worker deployment version`,
	)
	MatchingPollerScalingBacklogAgeScaleUp = NewTaskQueueDurationSetting(
		"matching.pollerScalingMinimumBacklog",
		200*time.Millisecond,
		`MatchingPollerScalingBacklogAgeScaleUp is the minimum backlog age that must be accumulated before
a decision to scale up the number of pollers will be issued`,
	)
	MatchingPollerScalingWaitTime = NewTaskQueueDurationSetting(
		"matching.pollerScalingWaitTime",
		1*time.Second,
		`MatchingPollerScalingWaitTime is the duration a sync-matched poller must exceed before
a decision to scale down the number of pollers will be issued`,
	)
	MatchingPollerScalingDecisionsPerSecond = NewTaskQueueFloatSetting(
		"matching.pollerScalingDecisionsPerSecond",
		10,
		`MatchingPollerScalingDecisionsPerSecond is the maximum number of scaling decisions that will be issued per
second per poller by one physical queue manager`,
	)
	MatchingUseNewMatcher = NewTaskQueueTypedSettingWithConverter(
		"matching.useNewMatcher",
		ConvertGradualChange(false),
		StaticGradualChange(false),
		`Use priority-enabled TaskMatcher`,
	)
	MatchingEnableFairness = NewTaskQueueTypedSettingWithConverter(
		"matching.enableFairness",
		ConvertGradualChange(false),
		StaticGradualChange(false),
		`Enable fairness for task dispatching. Implies matching.useNewMatcher.`,
	)
	MatchingEnableMigration = NewTaskQueueBoolSetting(
		"matching.enableMigration",
		false,
		`Allows migration between v1 and v2 (fairness) task backlogs.`,
	)
	MatchingPriorityLevels = NewTaskQueueIntSetting(
		"matching.priorityLevels",
		5,
		`Number of simple priority levels (requires new matcher)`,
	)
	MatchingBacklogTaskForwardTimeout = NewTaskQueueDurationSetting(
		"matching.backlogTaskForwardTimeout",
		60*time.Second,
		`Timeout for forwarded backlog task (requires new matcher)`,
	)
	MatchingFairnessCounter = NewTaskQueueTypedSetting(
		"matching.fairnessCounter",
		counter.DefaultCounterParams,
		`Configuration for counter used in matching fairness.`,
	)
	MatchingFairnessKeyRateLimitCacheSize = NewTaskQueueIntSetting(
		"matching.fairnessKeyRateLimitCacheSize",
		2000,
		"Cache size for fairness key rate limits.",
	)
	MatchingMaxFairnessKeyWeightOverrides = NewTaskQueueIntSetting(
		"matching.maxFairnessKeyWeightOverrides",
		1000,
		"Maximum number of fairness key weight overrides that can be configured for a task queue at a time.",
	)
	MatchingEnableWorkerPluginMetrics = NewGlobalBoolSetting(
		"matching.enableWorkerPluginMetrics",
		false,
		`MatchingEnableWorkerPluginMetrics controls whether to export worker plugin metrics.
The metric has 2 dimensions: namespace_id and plugin_name. Disabled by default as this is
an optional feature and also requires a metrics collection system that can handle higher cardinalities.`,
	)
	MatchingAutoEnableV2 = NewTaskQueueBoolSetting(
		"matching.autoEnableV2",
		false,
		`MatchingAutoEnableV2 automatically enables fairness when a fairness or priority key is seen`,
	)

	// Worker registry settings
	MatchingWorkerRegistryNumBuckets = NewGlobalIntSetting(
		"matching.workerRegistryNumBuckets",
		10,
		`MatchingWorkerRegistryNumBuckets is the number of buckets used to partition the worker registry
keyspace for reduced lock contention. Changes require a restart to take effect.`,
	)
	MatchingWorkerRegistryEntryTTL = NewGlobalDurationSetting(
		"matching.workerRegistryEntryTTL",
		5*time.Minute,
		`MatchingWorkerRegistryEntryTTL is the time after which worker heartbeat entries are considered expired
and eligible for eviction. Workers typically heartbeat every 30-60 seconds, so 5 minutes without a
heartbeat indicates the worker is likely dead.`,
	)
	MatchingWorkerRegistryMinEvictAge = NewGlobalDurationSetting(
		"matching.workerRegistryMinEvictAge",
		1*time.Minute,
		`MatchingWorkerRegistryMinEvictAge is the minimum age of worker heartbeat entries before they can be
evicted due to capacity pressure. This prevents evicting recently-heartbeated workers even when
the registry is at capacity. Lower values help handle crash-looping workers more aggressively.`,
	)
	MatchingWorkerRegistryMaxEntries = NewGlobalIntSetting(
		"matching.workerRegistryMaxEntries",
		1_000_000,
		`MatchingWorkerRegistryMaxEntries is the maximum number of worker heartbeat entries allowed across
all namespaces. When exceeded, the oldest entries (older than MinEvictAge) are evicted.`,
	)
	MatchingWorkerRegistryEvictionInterval = NewGlobalDurationSetting(
		"matching.workerRegistryEvictionInterval",
		1*time.Minute,
		`MatchingWorkerRegistryEvictionInterval is how often the worker registry runs background eviction
to remove expired entries. Should be shorter than EntryTTL for timely cleanup. Lower values mean faster cleanup but more CPU overhead.`,
	)

	EnableReplicationStream = NewGlobalBoolSetting(
		"history.enableReplicationStream",
		true,
		`EnableReplicationStream turn on replication stream`,
	)
	EnableSeparateReplicationEnableFlag = NewGlobalBoolSetting(
		"history.enableSeparateReplicationEnableFlag",
		false,
		`EnableSeparateReplicationEnableFlag controls whether to use the new ReplicationEnabled flag to control replication streams separately from cluster connectivity. When false, falls back to using only the Enabled flag for both connectivity and replication.`,
	)
	EnableHistoryReplicationDLQV2 = NewGlobalBoolSetting(
		"history.enableHistoryReplicationDLQV2",
		true,
		`EnableHistoryReplicationDLQV2 switches to the DLQ v2 implementation for history replication. See details in
[go.temporal.io/server/common/persistence.QueueV2]`,
	)

	HistoryRPS = NewGlobalIntSetting(
		"history.rps",
		3000,
		`HistoryRPS is request rate per second for each history host`,
	)
	HistoryPersistenceMaxQPS = NewGlobalIntSetting(
		"history.persistenceMaxQPS",
		9000,
		`HistoryPersistenceMaxQPS is the max qps history host can query DB`,
	)
	HistoryPersistenceGlobalMaxQPS = NewGlobalIntSetting(
		"history.persistenceGlobalMaxQPS",
		0,
		`HistoryPersistenceGlobalMaxQPS is the max qps history cluster can query DB`,
	)
	HistoryPersistenceNamespaceMaxQPS = NewNamespaceIntSetting(
		"history.persistenceNamespaceMaxQPS",
		0,
		`HistoryPersistenceNamespaceMaxQPS is the max qps each namespace on history host can query DB
If value less or equal to 0, will fall back to HistoryPersistenceMaxQPS`,
	)
	HistoryPersistenceGlobalNamespaceMaxQPS = NewNamespaceIntSetting(
		"history.persistenceGlobalNamespaceMaxQPS",
		0,
		`HistoryPersistenceNamespaceMaxQPS is the max qps each namespace in history cluster can query DB`,
	)
	HistoryPersistencePerShardNamespaceMaxQPS = NewNamespaceIntSetting(
		"history.persistencePerShardNamespaceMaxQPS",
		0,
		`HistoryPersistencePerShardNamespaceMaxQPS is the max qps each namespace on a shard can query DB`,
	)
	HistoryPersistenceDynamicRateLimitingParams = NewGlobalTypedSetting(
		"history.persistenceDynamicRateLimitingParams",
		DefaultDynamicRateLimitingParams,
		`HistoryPersistenceDynamicRateLimitingParams is a struct that contains all adjustable dynamic rate limiting params.
Fields: Enabled, RefreshInterval, LatencyThreshold, ErrorThreshold, RateBackoffStepSize, RateIncreaseStepSize, RateMultiMin, RateMultiMax.
See DynamicRateLimitingParams comments for more details.`,
	)
	EnableBestEffortDeleteTasksOnWorkflowUpdate = NewGlobalBoolSetting(
		"history.enableBestEffortDeleteTasksOnWorkflowUpdate",
		false,
		`Enable deletion of requested history tasks (e.g., WFT timeout tasks) right after a successful UpdateWorkflowExecution.
		WARNING: Turning on this config can create a large number of tombstones in cassandra and degrade performance, use with caution.`,
	)
	HistoryLongPollExpirationInterval = NewNamespaceDurationSetting(
		"history.longPollExpirationInterval",
		time.Second*20,
		`HistoryLongPollExpirationInterval is the long poll expiration interval in the history service`,
	)
	HistoryCacheSizeBasedLimit = NewGlobalBoolSetting(
		"history.cacheSizeBasedLimit",
		false,
		`HistoryCacheSizeBasedLimit if true, size of the history cache will be limited by HistoryCacheMaxSizeBytes
and HistoryCacheHostLevelMaxSizeBytes. Otherwise, entry count in the history cache will be limited by
HistoryCacheMaxSize and HistoryCacheHostLevelMaxSize.`,
	)
	HistoryCacheTTL = NewGlobalDurationSetting(
		"history.cacheTTL",
		time.Hour,
		`HistoryCacheTTL is TTL of history cache`,
	)
	HistoryCacheNonUserContextLockTimeout = NewGlobalDurationSetting(
		"history.cacheNonUserContextLockTimeout",
		500*time.Millisecond,
		`HistoryCacheNonUserContextLockTimeout controls how long non-user call (callerType != API or Operator)
will wait on workflow lock acquisition. Requires service restart to take effect.`,
	)
	HistoryCacheHostLevelMaxSize = NewGlobalIntSetting(
		"history.hostLevelCacheMaxSize",
		128000,
		`HistoryCacheHostLevelMaxSize is the maximum number of entries in the host level history cache`,
	)
	HistoryCacheHostLevelMaxSizeBytes = NewGlobalIntSetting(
		"history.hostLevelCacheMaxSizeBytes",
		256000*4*1024,
		`HistoryCacheHostLevelMaxSizeBytes is the maximum size of the host level history cache. This is only used if
HistoryCacheSizeBasedLimit is set to true.`,
	)
	HistoryCacheBackgroundEvict = NewGlobalTypedSetting(
		"history.cacheBackgroundEvict",
		DefaultHistoryCacheBackgroundEvictSettings,
		`HistoryCacheBackgroundEvict configures background processing to purge expired entries from the history cache.`,
	)
	EnableWorkflowExecutionTimeoutTimer = NewGlobalBoolSetting(
		"history.enableWorkflowExecutionTimeoutTimer",
		true,
		`EnableWorkflowExecutionTimeoutTimer controls whether to enable the new logic for generating a workflow execution
timeout timer when execution timeout is specified when starting a workflow.`,
	)
	EnableUpdateWorkflowModeIgnoreCurrent = NewGlobalBoolSetting(
		"history.enableUpdateWorkflowModeIgnoreCurrent",
		true,
		`EnableUpdateWorkflowModeIgnoreCurrent controls whether to enable the new logic for updating closed workflow execution
by mutation using UpdateWorkflowModeIgnoreCurrent`,
	)
	EnableTransitionHistory = NewNamespaceBoolSetting(
		"history.enableTransitionHistory",
		true,
		`EnableTransitionHistory controls whether to enable the new logic for recording the history for each state transition.`,
	)
	HistoryStartupMembershipJoinDelay = NewGlobalDurationSetting(
		"history.startupMembershipJoinDelay",
		0*time.Second,
		`HistoryStartupMembershipJoinDelay is the duration a history instance waits
before joining membership after starting.`,
	)
	HistoryAlignMembershipChange = NewGlobalDurationSetting(
		"history.alignMembershipChange",
		0*time.Second,
		`HistoryAlignMembershipChange is a duration to align history's membership changes to.
This can help reduce effects of shard movement.`,
	)
	HistoryShutdownDrainDuration = NewGlobalDurationSetting(
		"history.shutdownDrainDuration",
		0*time.Second,
		`HistoryShutdownDrainDuration is the duration of traffic drain during shutdown`,
	)
	XDCCacheMaxSizeBytes = NewGlobalIntSetting(
		"history.xdcCacheMaxSizeBytes",
		8*1024*1024,
		`XDCCacheMaxSizeBytes is max size of events cache in bytes`,
	)
	EventsCacheMaxSizeBytes = NewGlobalIntSetting(
		"history.eventsCacheMaxSizeBytes",
		512*1024,
		`EventsCacheMaxSizeBytes is max size of the shard level events cache in bytes`,
	)
	EventsHostLevelCacheMaxSizeBytes = NewGlobalIntSetting(
		"history.eventsHostLevelCacheMaxSizeBytes",
		512*512*1024,
		`EventsHostLevelCacheMaxSizeBytes is max size of the host level events cache in bytes`,
	)
	EventsCacheTTL = NewGlobalDurationSetting(
		"history.eventsCacheTTL",
		time.Hour,
		`EventsCacheTTL is TTL of events cache`,
	)
	EnableHostLevelEventsCache = NewGlobalBoolSetting(
		"history.enableHostLevelEventsCache",
		false,
		`EnableHostLevelEventsCache controls if the events cache is host level`,
	)
	AcquireShardInterval = NewGlobalDurationSetting(
		"history.acquireShardInterval",
		time.Minute,
		`AcquireShardInterval is interval that timer used to acquire shard`,
	)
	AcquireShardConcurrency = NewGlobalIntSetting(
		"history.acquireShardConcurrency",
		10,
		`AcquireShardConcurrency is number of goroutines that can be used to acquire shards in the shard controller.`,
	)
	ShardLingerOwnershipCheckQPS = NewGlobalIntSetting(
		"history.shardLingerOwnershipCheckQPS",
		4,
		`ShardLingerOwnershipCheckQPS is the frequency to perform shard ownership
checks while a shard is lingering.`,
	)
	ShardLingerTimeLimit = NewGlobalDurationSetting(
		"history.shardLingerTimeLimit",
		0,
		`ShardLingerTimeLimit configures if and for how long the shard controller
will temporarily delay closing shards after a membership update, awaiting a
shard ownership lost error from persistence. If set to zero, shards will not delay closing.
Do NOT use non-zero value with persistence layers that are missing AssertShardOwnership support.`,
	)
	ShardFinalizerTimeout = NewGlobalDurationSetting(
		"history.shardFinalizerTimeout",
		2*time.Second,
		`ShardFinalizerTimeout configures if and for how long the shard will attempt
to cleanup any of its associated data, such as workflow contexts. If set to zero, the finalizer is disabled.`,
	)
	HistoryClientOwnershipCachingEnabled = NewGlobalBoolSetting(
		"history.clientOwnershipCachingEnabled",
		false,
		`HistoryClientOwnershipCachingEnabled configures if history clients try to cache
shard ownership information, instead of checking membership for each request.
Only inspected when an instance first creates a history client, so changes
to this require a restart to take effect.`,
	)
	HistoryClientOwnershipCachingStaleTTL = NewGlobalDurationSetting(
		"history.clientOwnershipCachingUnusedTTL",
		30*time.Second,
		`HistoryClientOwnershipCachingStaleTTL, if non-zero, configures the TTL
for cached shard ownership entries after a membership update.`,
	)
	ShardIOConcurrency = NewGlobalIntSetting(
		"history.shardIOConcurrency",
		1,
		`ShardIOConcurrency controls the concurrency of persistence operations in shard context`,
	)
	ShardIOTimeout = NewGlobalDurationSetting(
		"history.shardIOTimeout",
		5*time.Second*debug.TimeoutMultiplier,
		`ShardIOTimeout sets the timeout for persistence operations in the shard context`,
	)
	StandbyClusterDelay = NewGlobalDurationSetting(
		"history.standbyClusterDelay",
		5*time.Minute,
		`StandbyClusterDelay is the artificial delay added to standby cluster's view of active cluster's time`,
	)
	StandbyTaskMissingEventsResendDelay = NewTaskTypeDurationSetting(
		"history.standbyTaskMissingEventsResendDelay",
		10*time.Minute,
		`StandbyTaskMissingEventsResendDelay is the amount of time standby cluster's will wait (if events are missing)
before calling remote for missing events`,
	)
	StandbyTaskMissingEventsDiscardDelay = NewTaskTypeDurationSetting(
		"history.standbyTaskMissingEventsDiscardDelay",
		15*time.Minute,
		`StandbyTaskMissingEventsDiscardDelay is the amount of time standby cluster's will wait (if events are missing)
before discarding the task`,
	)
	QueuePendingTaskCriticalCount = NewGlobalIntSetting(
		"history.queuePendingTaskCriticalCount",
		9000,
		`Max number of pending tasks in a history queue before triggering slice splitting and unloading.
NOTE: The outbound queue has a separate configuration: outboundQueuePendingTaskCriticalCount.`,
	)
	QueueReaderStuckCriticalAttempts = NewGlobalIntSetting(
		"history.queueReaderStuckCriticalAttempts",
		3,
		`QueueReaderStuckCriticalAttempts is the max number of task loading attempts for a certain task range
before that task range is split into a separate slice to unblock loading for later range.
currently only work for scheduled queues and the task range is 1s.`,
	)
	QueueCriticalSlicesCount = NewGlobalIntSetting(
		"history.queueCriticalSlicesCount",
		50,
		`QueueCriticalSlicesCount is the max number of slices in one queue
before force compacting slices`,
	)
	QueuePendingTaskMaxCount = NewGlobalIntSetting(
		"history.queuePendingTasksMaxCount",
		10000,
		`The max number of task pending tasks in a history queue before stopping loading new tasks into memory. This
limit is in addition to queuePendingTaskCriticalCount which controls when to unload already loaded tasks but doesn't
prevent loading new tasks. Ideally this max count limit should not be hit and task unloading should happen once critical
count is exceeded. But since queue action is async, we need this hard limit.
NOTE: The outbound queue has a separate configuration: outboundQueuePendingTaskMaxCount.
`,
	)
	QueueMaxPredicateSize = NewGlobalIntSetting(
		"history.queueMaxPredicateSize",
		10*1024,
		`The max size of the multi-cursor predicate structure stored in the shard info record. 0 is considered
unlimited. When the predicate size is surpassed for a given scope, the predicate is converted to a universal predicate,
which causes all tasks in the scope's range to eventually be reprocessed without applying any filtering logic.
NOTE: The outbound queue has a separate configuration: outboundQueueMaxPredicateSize.
`,
	)
	QueueMoveGroupTaskCountBase = NewGlobalIntSetting(
		"history.queueMoveGroupTaskCountBase",
		500,
		`The base number of pending tasks count for a task group to be moved to the next level reader.
The actual count is calculated as base * (multiplier ^ level)`,
	)
	QueueMoveGroupTaskCountMultiplier = NewGlobalFloatSetting(
		"history.queueMoveGroupTaskCountMultiplier",
		3.0,
		`The multiplier used to calculate the number of pending tasks for a task group to be moved to the next level reader.
The actual count is calculated as base * (multiplier ^ level)`,
	)

	TaskSchedulerEnableRateLimiter = NewGlobalBoolSetting(
		"history.taskSchedulerEnableRateLimiter",
		false,
		`TaskSchedulerEnableRateLimiter indicates if task scheduler rate limiter should be enabled`,
	)
	TaskSchedulerEnableRateLimiterShadowMode = NewGlobalBoolSetting(
		"history.taskSchedulerEnableRateLimiterShadowMode",
		true,
		`TaskSchedulerEnableRateLimiterShadowMode indicates if task scheduler rate limiter should run in shadow mode
i.e. through rate limiter and emit metrics but do not actually block/throttle task scheduling`,
	)
	TaskSchedulerRateLimiterStartupDelay = NewGlobalDurationSetting(
		"history.taskSchedulerRateLimiterStartupDelay",
		5*time.Second,
		`TaskSchedulerRateLimiterStartupDelay is the duration to wait after startup before enforcing task scheduler rate limiting`,
	)
	TaskSchedulerGlobalMaxQPS = NewGlobalIntSetting(
		"history.taskSchedulerGlobalMaxQPS",
		0,
		`TaskSchedulerGlobalMaxQPS is the max qps all task schedulers in the cluster can schedule tasks
If value less or equal to 0, will fall back to TaskSchedulerMaxQPS`,
	)
	TaskSchedulerMaxQPS = NewGlobalIntSetting(
		"history.taskSchedulerMaxQPS",
		0,
		`TaskSchedulerMaxQPS is the max qps task schedulers on a host can schedule tasks
If value less or equal to 0, will fall back to HistoryPersistenceMaxQPS`,
	)
	TaskSchedulerGlobalNamespaceMaxQPS = NewNamespaceIntSetting(
		"history.taskSchedulerGlobalNamespaceMaxQPS",
		0,
		`TaskSchedulerGlobalNamespaceMaxQPS is the max qps all task schedulers in the cluster can schedule tasks for a certain namespace
If value less or equal to 0, will fall back to TaskSchedulerNamespaceMaxQPS`,
	)
	TaskSchedulerNamespaceMaxQPS = NewNamespaceIntSetting(
		"history.taskSchedulerNamespaceMaxQPS",
		0,
		`TaskSchedulerNamespaceMaxQPS is the max qps task schedulers on a host can schedule tasks for a certain namespace
If value less or equal to 0, will fall back to HistoryPersistenceNamespaceMaxQPS`,
	)
	TaskSchedulerInactiveChannelDeletionDelay = NewGlobalDurationSetting(
		"history.taskSchedulerInactiveChannelDeletionDelay",
		time.Hour,
		`TaskSchedulerInactiveChannelDeletionDelay the time delay before a namespace's' channel is removed from the scheduler`,
	)

	TimerTaskBatchSize = NewGlobalIntSetting(
		"history.timerTaskBatchSize",
		100,
		`TimerTaskBatchSize is batch size for timer processor to process tasks`,
	)
	TimerProcessorSchedulerWorkerCount = NewGlobalIntSetting(
		"history.timerProcessorSchedulerWorkerCount",
		512,
		`TimerProcessorSchedulerWorkerCount is the number of workers in the host level task scheduler for timer processor`,
	)
	TimerProcessorSchedulerActiveRoundRobinWeights = NewNamespaceMapSetting(
		"history.timerProcessorSchedulerActiveRoundRobinWeights",
		nil,
		`TimerProcessorSchedulerActiveRoundRobinWeights is the priority round robin weights used by timer task scheduler for active namespaces`,
	)
	TimerProcessorSchedulerStandbyRoundRobinWeights = NewNamespaceMapSetting(
		"history.timerProcessorSchedulerStandbyRoundRobinWeights",
		nil,
		`TimerProcessorSchedulerStandbyRoundRobinWeights is the priority round robin weights used by timer task scheduler for standby namespaces`,
	)
	TimerProcessorUpdateAckInterval = NewGlobalDurationSetting(
		"history.timerProcessorUpdateAckInterval",
		30*time.Second,
		`TimerProcessorUpdateAckInterval is update interval for timer processor`,
	)
	TimerProcessorUpdateAckIntervalJitterCoefficient = NewGlobalFloatSetting(
		"history.timerProcessorUpdateAckIntervalJitterCoefficient",
		0.15,
		`TimerProcessorUpdateAckIntervalJitterCoefficient is the update interval jitter coefficient`,
	)
	TimerProcessorMaxPollRPS = NewGlobalIntSetting(
		"history.timerProcessorMaxPollRPS",
		20,
		`TimerProcessorMaxPollRPS is max poll rate per second for timer processor`,
	)
	TimerProcessorMaxPollHostRPS = NewGlobalIntSetting(
		"history.timerProcessorMaxPollHostRPS",
		0,
		`TimerProcessorMaxPollHostRPS is max poll rate per second for all timer processor on a host`,
	)
	TimerProcessorMaxPollInterval = NewGlobalDurationSetting(
		"history.timerProcessorMaxPollInterval",
		5*time.Minute,
		`TimerProcessorMaxPollInterval is max poll interval for timer processor`,
	)
	TimerProcessorMaxPollIntervalJitterCoefficient = NewGlobalFloatSetting(
		"history.timerProcessorMaxPollIntervalJitterCoefficient",
		0.15,
		`TimerProcessorMaxPollIntervalJitterCoefficient is the max poll interval jitter coefficient`,
	)
	TimerProcessorPollBackoffInterval = NewGlobalDurationSetting(
		"history.timerProcessorPollBackoffInterval",
		5*time.Second,
		`TimerProcessorPollBackoffInterval is the poll backoff interval if task redispatcher's size exceeds limit for timer processor`,
	)
	TimerProcessorMaxTimeShift = NewGlobalDurationSetting(
		"history.timerProcessorMaxTimeShift",
		1*time.Second,
		`TimerProcessorMaxTimeShift is the max shift timer processor can have`,
	)
	TimerQueueMaxReaderCount = NewGlobalIntSetting(
		"history.timerQueueMaxReaderCount",
		2,
		`TimerQueueMaxReaderCount is the max number of readers in one multi-cursor timer queue`,
	)
	RetentionTimerJitterDuration = NewGlobalDurationSetting(
		"history.retentionTimerJitterDuration",
		30*time.Minute,
		`RetentionTimerJitterDuration is a time duration jitter to distribute timer from T0 to T0 + jitter duration`,
	)

	MemoryTimerProcessorSchedulerWorkerCount = NewGlobalIntSetting(
		"history.memoryTimerProcessorSchedulerWorkerCount",
		64,
		`MemoryTimerProcessorSchedulerWorkerCount is the number of workers in the task scheduler for in memory timer processor.`,
	)

	TransferTaskBatchSize = NewGlobalIntSetting(
		"history.transferTaskBatchSize",
		100,
		`TransferTaskBatchSize is batch size for transferQueueProcessor`,
	)
	TransferProcessorMaxPollRPS = NewGlobalIntSetting(
		"history.transferProcessorMaxPollRPS",
		20,
		`TransferProcessorMaxPollRPS is max poll rate per second for transferQueueProcessor`,
	)
	TransferProcessorMaxPollHostRPS = NewGlobalIntSetting(
		"history.transferProcessorMaxPollHostRPS",
		0,
		`TransferProcessorMaxPollHostRPS is max poll rate per second for all transferQueueProcessor on a host`,
	)
	TransferProcessorSchedulerWorkerCount = NewGlobalIntSetting(
		"history.transferProcessorSchedulerWorkerCount",
		512,
		`TransferProcessorSchedulerWorkerCount is the number of workers in the host level task scheduler for transferQueueProcessor`,
	)
	TransferProcessorSchedulerActiveRoundRobinWeights = NewNamespaceMapSetting(
		"history.transferProcessorSchedulerActiveRoundRobinWeights",
		nil,
		`TransferProcessorSchedulerActiveRoundRobinWeights is the priority round robin weights used by transfer task scheduler for active namespaces`,
	)
	TransferProcessorSchedulerStandbyRoundRobinWeights = NewNamespaceMapSetting(
		"history.transferProcessorSchedulerStandbyRoundRobinWeights",
		nil,
		`TransferProcessorSchedulerStandbyRoundRobinWeights is the priority round robin weights used by transfer task scheduler for standby namespaces`,
	)
	TransferProcessorMaxPollInterval = NewGlobalDurationSetting(
		"history.transferProcessorMaxPollInterval",
		1*time.Minute,
		`TransferProcessorMaxPollInterval max poll interval for transferQueueProcessor`,
	)
	TransferProcessorMaxPollIntervalJitterCoefficient = NewGlobalFloatSetting(
		"history.transferProcessorMaxPollIntervalJitterCoefficient",
		0.15,
		`TransferProcessorMaxPollIntervalJitterCoefficient is the max poll interval jitter coefficient`,
	)
	TransferProcessorUpdateAckInterval = NewGlobalDurationSetting(
		"history.transferProcessorUpdateAckInterval",
		30*time.Second,
		`TransferProcessorUpdateAckInterval is update interval for transferQueueProcessor`,
	)
	TransferProcessorUpdateAckIntervalJitterCoefficient = NewGlobalFloatSetting(
		"history.transferProcessorUpdateAckIntervalJitterCoefficient",
		0.15,
		`TransferProcessorUpdateAckIntervalJitterCoefficient is the update interval jitter coefficient`,
	)
	TransferProcessorPollBackoffInterval = NewGlobalDurationSetting(
		"history.transferProcessorPollBackoffInterval",
		5*time.Second,
		`TransferProcessorPollBackoffInterval is the poll backoff interval if task redispatcher's size exceeds limit for transferQueueProcessor`,
	)
	TransferProcessorEnsureCloseBeforeDelete = NewGlobalBoolSetting(
		"history.transferProcessorEnsureCloseBeforeDelete",
		true,
		`TransferProcessorEnsureCloseBeforeDelete means we ensure the execution is closed before we delete it`,
	)
	TransferQueueMaxReaderCount = NewGlobalIntSetting(
		"history.transferQueueMaxReaderCount",
		2,
		`TransferQueueMaxReaderCount is the max number of readers in one multi-cursor transfer queue`,
	)

	OutboundTaskBatchSize = NewGlobalIntSetting(
		"history.outboundTaskBatchSize",
		100,
		`OutboundTaskBatchSize is batch size for outboundQueueFactory`,
	)
	OutboundQueuePendingTaskMaxCount = NewGlobalIntSetting(
		"history.outboundQueuePendingTasksMaxCount",
		10000,
		`The max number of task pending tasks in the outbound queue before stopping loading new tasks into memory. This
limit is in addition to outboundQueuePendingTaskCriticalCount which controls when to unload already loaded tasks but
doesn't prevent loading new tasks. Ideally this max count limit should not be hit and task unloading should happen once
critical count is exceeded. But since queue action is async, we need this hard limit.
`,
	)
	OutboundQueuePendingTaskCriticalCount = NewGlobalIntSetting(
		"history.outboundQueuePendingTaskCriticalCount",
		9000,
		`Max number of pending tasks in the outbound queue before triggering slice splitting and unloading.`,
	)
	OutboundQueueMaxPredicateSize = NewGlobalIntSetting(
		"history.outboundQueueMaxPredicateSize",
		10*1024,
		`The max size of the multi-cursor predicate structure stored in the shard info record for the outbound queue. 0
is considered unlimited. When the predicate size is surpassed for a given scope, the predicate is converted to a
universal predicate, which causes all tasks in the scope's range to eventually be reprocessed without applying any
filtering logic.
`,
	)

	OutboundProcessorMaxPollRPS = NewGlobalIntSetting(
		"history.outboundProcessorMaxPollRPS",
		20,
		`OutboundProcessorMaxPollRPS is max poll rate per second for outboundQueueFactory`,
	)
	OutboundProcessorMaxPollHostRPS = NewGlobalIntSetting(
		"history.outboundProcessorMaxPollHostRPS",
		0,
		`OutboundProcessorMaxPollHostRPS is max poll rate per second for all outboundQueueFactory on a host`,
	)
	OutboundProcessorMaxPollInterval = NewGlobalDurationSetting(
		"history.outboundProcessorMaxPollInterval",
		1*time.Minute,
		`OutboundProcessorMaxPollInterval max poll interval for outboundQueueFactory`,
	)
	OutboundProcessorMaxPollIntervalJitterCoefficient = NewGlobalFloatSetting(
		"history.outboundProcessorMaxPollIntervalJitterCoefficient",
		0.15,
		`OutboundProcessorMaxPollIntervalJitterCoefficient is the max poll interval jitter coefficient`,
	)
	OutboundProcessorUpdateAckInterval = NewGlobalDurationSetting(
		"history.outboundProcessorUpdateAckInterval",
		30*time.Second,
		`OutboundProcessorUpdateAckInterval is update interval for outboundQueueFactory`,
	)
	OutboundProcessorUpdateAckIntervalJitterCoefficient = NewGlobalFloatSetting(
		"history.outboundProcessorUpdateAckIntervalJitterCoefficient",
		0.15,
		`OutboundProcessorUpdateAckIntervalJitterCoefficient is the update interval jitter coefficient`,
	)
	OutboundProcessorPollBackoffInterval = NewGlobalDurationSetting(
		"history.outboundProcessorPollBackoffInterval",
		5*time.Second,
		`OutboundProcessorPollBackoffInterval is the poll backoff interval if task redispatcher's size exceeds limit for outboundQueueFactory`,
	)
	OutboundQueueMaxReaderCount = NewGlobalIntSetting(
		"history.outboundQueueMaxReaderCount",
		4,
		`OutboundQueueMaxReaderCount is the max number of readers in one multi-cursor outbound queue`,
	)
	OutboundQueueGroupLimiterBufferSize = NewDestinationIntSetting(
		"history.outboundQueue.groupLimiter.bufferSize",
		100,
		`OutboundQueueGroupLimiterBufferSize is the max buffer size of the group limiter`,
	)
	OutboundQueueGroupLimiterConcurrency = NewDestinationIntSetting(
		"history.outboundQueue.groupLimiter.concurrency",
		100,
		`OutboundQueueGroupLimiterConcurrency is the concurrency of the group limiter`,
	)
	OutboundQueueHostSchedulerMaxTaskRPS = NewDestinationFloatSetting(
		"history.outboundQueue.hostScheduler.maxTaskRPS",
		100.0,
		`OutboundQueueHostSchedulerMaxTaskRPS is the host scheduler max task RPS`,
	)
	OutboundQueueCircuitBreakerSettings = NewDestinationTypedSetting(
		"history.outboundQueue.circuitBreakerSettings",
		CircuitBreakerSettings{},
		`OutboundQueueCircuitBreakerSettings are circuit breaker settings.
Fields (see gobreaker reference for more details):
- MaxRequests: Maximum number of requests allowed to pass through when it is half-open (default 1).
- Interval (duration): Cyclic period in closed state to clear the internal counts;
  if interval is 0, then it never clears the internal counts (default 0).
- Timeout (duration): Period of open state before changing to half-open state (default 60s).`,
	)
	OutboundStandbyTaskMissingEventsDiscardDelay = NewDestinationDurationSetting(
		"history.outboundQueue.standbyTaskMissingEventsDiscardDelay",

		time.Duration(math.MaxInt64),
		`OutboundStandbyTaskMissingEventsDiscardDelay is the equivalent of
StandbyTaskMissingEventsDiscardDelay for outbound standby task processor.`,
	)
	OutboundStandbyTaskMissingEventsDestinationDownErr = NewDestinationBoolSetting(
		"history.outboundQueue.standbyTaskMissingEventsDestinationDownErr",
		true,
		`OutboundStandbyTaskMissingEventsDestinationDownErr enables returning DestinationDownError when
the outbound standby task failed to be processed due to missing events.`,
	)

	VisibilityTaskBatchSize = NewGlobalIntSetting(
		"history.visibilityTaskBatchSize",
		100,
		`VisibilityTaskBatchSize is batch size for visibilityQueueProcessor`,
	)
	VisibilityProcessorMaxPollRPS = NewGlobalIntSetting(
		"history.visibilityProcessorMaxPollRPS",
		20,
		`VisibilityProcessorMaxPollRPS is max poll rate per second for visibilityQueueProcessor`,
	)
	VisibilityProcessorMaxPollHostRPS = NewGlobalIntSetting(
		"history.visibilityProcessorMaxPollHostRPS",
		0,
		`VisibilityProcessorMaxPollHostRPS is max poll rate per second for all visibilityQueueProcessor on a host`,
	)
	VisibilityProcessorSchedulerWorkerCount = NewGlobalIntSetting(
		"history.visibilityProcessorSchedulerWorkerCount",
		512,
		`VisibilityProcessorSchedulerWorkerCount is the number of workers in the host level task scheduler for visibilityQueueProcessor`,
	)
	VisibilityProcessorSchedulerActiveRoundRobinWeights = NewNamespaceMapSetting(
		"history.visibilityProcessorSchedulerActiveRoundRobinWeights",
		nil,
		`VisibilityProcessorSchedulerActiveRoundRobinWeights is the priority round robin weights by visibility task scheduler for active namespaces`,
	)
	VisibilityProcessorSchedulerStandbyRoundRobinWeights = NewNamespaceMapSetting(
		"history.visibilityProcessorSchedulerStandbyRoundRobinWeights",
		nil,
		`VisibilityProcessorSchedulerStandbyRoundRobinWeights is the priority round robin weights by visibility task scheduler for standby namespaces`,
	)
	VisibilityProcessorMaxPollInterval = NewGlobalDurationSetting(
		"history.visibilityProcessorMaxPollInterval",
		1*time.Minute,
		`VisibilityProcessorMaxPollInterval max poll interval for visibilityQueueProcessor`,
	)
	VisibilityProcessorMaxPollIntervalJitterCoefficient = NewGlobalFloatSetting(
		"history.visibilityProcessorMaxPollIntervalJitterCoefficient",
		0.15,
		`VisibilityProcessorMaxPollIntervalJitterCoefficient is the max poll interval jitter coefficient`,
	)
	VisibilityProcessorUpdateAckInterval = NewGlobalDurationSetting(
		"history.visibilityProcessorUpdateAckInterval",
		30*time.Second,
		`VisibilityProcessorUpdateAckInterval is update interval for visibilityQueueProcessor`,
	)
	VisibilityProcessorUpdateAckIntervalJitterCoefficient = NewGlobalFloatSetting(
		"history.visibilityProcessorUpdateAckIntervalJitterCoefficient",
		0.15,
		`VisibilityProcessorUpdateAckIntervalJitterCoefficient is the update interval jitter coefficient`,
	)
	VisibilityProcessorPollBackoffInterval = NewGlobalDurationSetting(
		"history.visibilityProcessorPollBackoffInterval",
		5*time.Second,
		`VisibilityProcessorPollBackoffInterval is the poll backoff interval if task redispatcher's size exceeds limit for visibilityQueueProcessor`,
	)
	VisibilityProcessorEnsureCloseBeforeDelete = NewGlobalBoolSetting(
		"history.visibilityProcessorEnsureCloseBeforeDelete",
		false,
		`VisibilityProcessorEnsureCloseBeforeDelete means we ensure the visibility of an execution is closed before we delete its visibility records`,
	)
	VisibilityProcessorEnableCloseWorkflowCleanup = NewNamespaceBoolSetting(
		"history.visibilityProcessorEnableCloseWorkflowCleanup",
		false,
		`VisibilityProcessorEnableCloseWorkflowCleanup to clean up the mutable state after visibility
close task has been processed. Must use Elasticsearch as visibility store, otherwise workflow
data (eg: search attributes) will be lost after workflow is closed.`,
	)
	VisibilityProcessorRelocateAttributesMinBlobSize = NewNamespaceIntSetting(
		"history.visibilityProcessorRelocateAttributesMinBlobSize",
		0,
		`VisibilityProcessorRelocateAttributesMinBlobSize is the minimum size in bytes of memo or search
attributes.`,
	)
	VisibilityQueueMaxReaderCount = NewGlobalIntSetting(
		"history.visibilityQueueMaxReaderCount",
		2,
		`VisibilityQueueMaxReaderCount is the max number of readers in one multi-cursor visibility queue`,
	)

	DisableFetchRelocatableAttributesFromVisibility = NewNamespaceBoolSetting(
		"history.disableFetchRelocatableAttributesFromVisibility",
		false,
		`DisableFetchRelocatableAttributesFromVisibility disables fetching memo and search attributes from
visibility if they were removed from the mutable state`,
	)

	ArchivalTaskBatchSize = NewGlobalIntSetting(
		"history.archivalTaskBatchSize",
		100,
		`ArchivalTaskBatchSize is batch size for archivalQueueProcessor`,
	)
	ArchivalProcessorMaxPollRPS = NewGlobalIntSetting(
		"history.archivalProcessorMaxPollRPS",
		20,
		`ArchivalProcessorMaxPollRPS is max poll rate per second for archivalQueueProcessor`,
	)
	ArchivalProcessorMaxPollHostRPS = NewGlobalIntSetting(
		"history.archivalProcessorMaxPollHostRPS",
		0,
		`ArchivalProcessorMaxPollHostRPS is max poll rate per second for all archivalQueueProcessor on a host`,
	)
	ArchivalProcessorSchedulerWorkerCount = NewGlobalIntSetting(
		"history.archivalProcessorSchedulerWorkerCount",
		512,
		`ArchivalProcessorSchedulerWorkerCount is the number of workers in the host level task scheduler for
archivalQueueProcessor`,
	)
	ArchivalProcessorMaxPollInterval = NewGlobalDurationSetting(
		"history.archivalProcessorMaxPollInterval",
		5*time.Minute,
		`ArchivalProcessorMaxPollInterval max poll interval for archivalQueueProcessor`,
	)
	ArchivalProcessorMaxPollIntervalJitterCoefficient = NewGlobalFloatSetting(
		"history.archivalProcessorMaxPollIntervalJitterCoefficient",
		0.15,
		`ArchivalProcessorMaxPollIntervalJitterCoefficient is the max poll interval jitter coefficient`,
	)
	ArchivalProcessorUpdateAckInterval = NewGlobalDurationSetting(
		"history.archivalProcessorUpdateAckInterval",
		30*time.Second,
		`ArchivalProcessorUpdateAckInterval is update interval for archivalQueueProcessor`,
	)
	ArchivalProcessorUpdateAckIntervalJitterCoefficient = NewGlobalFloatSetting(
		"history.archivalProcessorUpdateAckIntervalJitterCoefficient",
		0.15,
		`ArchivalProcessorUpdateAckIntervalJitterCoefficient is the update interval jitter coefficient`,
	)
	ArchivalProcessorPollBackoffInterval = NewGlobalDurationSetting(
		"history.archivalProcessorPollBackoffInterval",
		5*time.Second,
		`ArchivalProcessorPollBackoffInterval is the poll backoff interval if task redispatcher's size exceeds limit for
archivalQueueProcessor`,
	)
	ArchivalProcessorArchiveDelay = NewGlobalDurationSetting(
		"history.archivalProcessorArchiveDelay",
		5*time.Minute,
		`ArchivalProcessorArchiveDelay is the delay before archivalQueueProcessor starts to process archival tasks`,
	)
	ArchivalBackendMaxRPS = NewGlobalFloatSetting(
		"history.archivalBackendMaxRPS",
		10000.0,
		`ArchivalBackendMaxRPS is the maximum rate of requests per second to the archival backend`,
	)
	ArchivalQueueMaxReaderCount = NewGlobalIntSetting(
		"history.archivalQueueMaxReaderCount",
		2,
		`ArchivalQueueMaxReaderCount is the max number of readers in one multi-cursor archival queue`,
	)

	WorkflowExecutionMaxInFlightUpdates = NewNamespaceIntSetting(
		"history.maxInFlightUpdates",
		10,
		`WorkflowExecutionMaxInFlightUpdates is the max number of updates that can be in-flight (admitted but not yet completed) for any given workflow execution. Set to zero to disable limit.`,
	)
	WorkflowExecutionMaxInFlightUpdatePayloads = NewNamespaceIntSetting(
		"history.maxInFlightUpdatePayloads",
		20*1024*1024,
		`WorkflowExecutionMaxInFlightUpdatePayloads is the max total payload size (in bytes) of in-flight updates (admitted but not yet completed) for any given workflow execution. Set to zero to disable.`,
	)
	WorkflowExecutionMaxTotalUpdates = NewNamespaceIntSetting(
		"history.maxTotalUpdates",
		2000,
		`WorkflowExecutionMaxTotalUpdates is the max number of updates that any given workflow execution can receive. Set to zero to disable.`,
	)
	WorkflowExecutionMaxTotalUpdatesSuggestContinueAsNewThreshold = NewNamespaceFloatSetting(
		"history.maxTotalUpdates.suggestContinueAsNewThreshold",
		0.9,
		`WorkflowExecutionMaxTotalUpdatesSuggestContinueAsNewThreshold is the percentage threshold of total updates that any given workflow execution can receive before suggesting to continue-as-new.`,
	)
	EnableUpdateWithStartRetryOnClosedWorkflowAbort = NewNamespaceBoolSetting(
		"history.enableUpdateWithStartRetryOnClosedWorkflowAbort",
		true,
		`EnableUpdateWithStartRetryOnClosedWorkflowAbort enables retrying Update-with-Start's update if it was aborted by a closing workflow.`,
	)
	EnableUpdateWithStartRetryableErrorOnClosedWorkflowAbort = NewNamespaceBoolSetting(
		"history.enableUpdateWithStartRetryableErrorOnClosedWorkflowAbort",
		true,
		`EnableUpdateWithStartRetryableErrorOnClosedWorkflowAbort enables sending back a retryable status code when the Update-with-Start's update was aborted by a closing workflow.`,
	)

	ReplicatorTaskBatchSize = NewGlobalIntSetting(
		"history.replicatorTaskBatchSize",
		100,
		`ReplicatorTaskBatchSize is batch size for ReplicatorProcessor`,
	)
	ReplicatorMaxSkipTaskCount = NewGlobalIntSetting(
		"history.replicatorMaxSkipTaskCount",
		250,
		`ReplicatorMaxSkipTaskCount is maximum number of tasks that can be skipped during tasks pagination due to not meeting filtering conditions (e.g. missed namespace).`,
	)
	ReplicatorProcessorMaxPollInterval = NewGlobalDurationSetting(
		"history.replicatorProcessorMaxPollInterval",
		1*time.Minute,
		`ReplicatorProcessorMaxPollInterval is max poll interval for ReplicatorProcessor`,
	)
	ReplicatorProcessorMaxPollIntervalJitterCoefficient = NewGlobalFloatSetting(
		"history.replicatorProcessorMaxPollIntervalJitterCoefficient",
		0.15,
		`ReplicatorProcessorMaxPollIntervalJitterCoefficient is the max poll interval jitter coefficient`,
	)
	MaximumBufferedEventsBatch = NewGlobalIntSetting(
		"history.maximumBufferedEventsBatch",
		100,
		`MaximumBufferedEventsBatch is the maximum permissible number of buffered events for any given mutable state.`,
	)
	MaximumBufferedEventsSizeInBytes = NewGlobalIntSetting(
		"history.maximumBufferedEventsSizeInBytes",
		2*1024*1024,
		`MaximumBufferedEventsSizeInBytes is the maximum permissible size of all buffered events for any given mutable
state. The total size is determined by the sum of the size, in bytes, of each HistoryEvent proto.`,
	)
	MaximumSignalsPerExecution = NewNamespaceIntSetting(
		"history.maximumSignalsPerExecution",
		10000,
		`MaximumSignalsPerExecution is max number of signals supported by single execution`,
	)
	ShardUpdateMinInterval = NewGlobalDurationSetting(
		"history.shardUpdateMinInterval",
		5*time.Minute,
		`ShardUpdateMinInterval is the minimal time interval which the shard info can be updated`,
	)
	ShardFirstUpdateInterval = NewGlobalDurationSetting(
		"history.shardFirstUpdateInterval",
		10*time.Second,
		`ShardFirstUpdateInterval is the time interval after which the first shard info update will happen.
		It should be smaller than ShardUpdateMinInterval`,
	)
	ShardUpdateMinTasksCompleted = NewGlobalIntSetting(
		"history.shardUpdateMinTasksCompleted",
		1000,
		`ShardUpdateMinTasksCompleted is the minimum number of tasks which must be completed (across all queues) before the shard info can be updated.
Note that once history.shardUpdateMinInterval amount of time has passed we'll update the shard info regardless of the number of tasks completed.
When the this config is zero or lower we will only update shard info at most once every history.shardUpdateMinInterval.`,
	)
	ShardSyncMinInterval = NewGlobalDurationSetting(
		"history.shardSyncMinInterval",
		5*time.Minute,
		`ShardSyncMinInterval is the minimal time interval which the shard info should be sync to remote`,
	)
	EmitShardLagLog = NewGlobalBoolSetting(
		"history.emitShardLagLog",
		false,
		`EmitShardLagLog whether emit the shard lag log`,
	)
	DefaultEventEncoding = NewNamespaceStringSetting(
		"history.defaultEventEncoding",
		enumspb.ENCODING_TYPE_PROTO3.String(),
		`DefaultEventEncoding is the encoding type for history events`,
	)
	DefaultActivityRetryPolicy = NewNamespaceTypedSetting(
		"history.defaultActivityRetryPolicy",
		retrypolicy.DefaultDefaultRetrySettings,
		`DefaultActivityRetryPolicy represents the out-of-box retry policy for activities where
the user has not specified an explicit RetryPolicy`,
	)
	DefaultWorkflowRetryPolicy = NewNamespaceTypedSetting(
		"history.defaultWorkflowRetryPolicy",
		retrypolicy.DefaultDefaultRetrySettings,
		`DefaultWorkflowRetryPolicy represents the out-of-box retry policy for unset fields
where the user has set an explicit RetryPolicy, but not specified all the fields`,
	)
	AllowResetWithPendingChildren = NewNamespaceBoolSetting(
		"history.allowResetWithPendingChildren",
		true,
		`Allows resetting of workflows with pending children when set to true`,
	)
	HistoryMaxAutoResetPoints = NewNamespaceIntSetting(
		"history.historyMaxAutoResetPoints",
		primitives.DefaultHistoryMaxAutoResetPoints,
		`HistoryMaxAutoResetPoints is the key for max number of auto reset points stored in mutableState`,
	)
	EnableParentClosePolicy = NewNamespaceBoolSetting(
		"history.enableParentClosePolicy",
		true,
		`EnableParentClosePolicy whether to  ParentClosePolicy`,
	)
	ParentClosePolicyThreshold = NewNamespaceIntSetting(
		"history.parentClosePolicyThreshold",
		10,
		`ParentClosePolicyThreshold decides that parent close policy will be processed by sys workers(if enabled) if
the number of children greater than or equal to this threshold`,
	)
	NumParentClosePolicySystemWorkflows = NewGlobalIntSetting(
		"history.numParentClosePolicySystemWorkflows",
		1000,
		`NumParentClosePolicySystemWorkflows is key for number of parentClosePolicy system workflows running in total`,
	)
	HistoryThrottledLogRPS = NewGlobalIntSetting(
		"history.throttledLogRPS",
		4,
		`HistoryThrottledLogRPS is the rate limit on number of log messages emitted per second for throttled logger`,
	)
	WorkflowTaskHeartbeatTimeout = NewNamespaceDurationSetting(
		"history.workflowTaskHeartbeatTimeout",
		time.Minute*30,
		`WorkflowTaskHeartbeatTimeout for workflow task heartbeat`,
	)
	WorkflowTaskCriticalAttempts = NewGlobalIntSetting(
		"history.workflowTaskCriticalAttempt",
		10,
		`WorkflowTaskCriticalAttempts is the number of attempts for a workflow task that's regarded as critical`,
	)
	WorkflowTaskRetryMaxInterval = NewGlobalDurationSetting(
		"history.workflowTaskRetryMaxInterval",
		time.Minute*10,
		`WorkflowTaskRetryMaxInterval is the maximum interval added to a workflow task's startToClose timeout for slowing down retry`,
	)
	EnableWorkflowTaskStampIncrementOnFailure = NewGlobalBoolSetting(
		"history.enableWorkflowTaskStampIncrementOnFailure",
		false,
		`EnableWorkflowTaskStampIncrementOnFailure controls whether the workflow task stamp is incremented when a workflow task fails and is rescheduled`,
	)
	DiscardSpeculativeWorkflowTaskMaximumEventsCount = NewGlobalIntSetting(
		"history.discardSpeculativeWorkflowTaskMaximumEventsCount",
		10,
		`If speculative workflow task shipped more than DiscardSpeculativeWorkflowTaskMaximumEventsCount events, it can't be discarded`,
	)
	EnableDropRepeatedWorkflowTaskFailures = NewNamespaceBoolSetting(
		"history.enableDropRepeatedWorkflowTaskFailures",
		false,
		`EnableDropRepeatedWorkflowTaskFailures whether to silently drop repeated workflow task failures`,
	)
	DefaultWorkflowTaskTimeout = NewNamespaceDurationSetting(
		"history.defaultWorkflowTaskTimeout",
		primitives.DefaultWorkflowTaskTimeout,
		`DefaultWorkflowTaskTimeout for a workflow task`,
	)
	SkipReapplicationByNamespaceID = NewNamespaceIDBoolSetting(
		"history.SkipReapplicationByNamespaceID",
		false,
		`SkipReapplicationByNamespaceID is whether skipping a event re-application for a namespace`,
	)
	StandbyTaskReReplicationContextTimeout = NewNamespaceIDDurationSetting(
		"history.standbyTaskReReplicationContextTimeout",
		30*time.Second,
		`StandbyTaskReReplicationContextTimeout is the context timeout for standby task re-replication`,
	)
	MaxBufferedQueryCount = NewGlobalIntSetting(
		"history.MaxBufferedQueryCount",
		1,
		`MaxBufferedQueryCount indicates max buffer query count`,
	)
	MutableStateChecksumGenProbability = NewNamespaceIntSetting(
		"history.mutableStateChecksumGenProbability",
		0,
		`MutableStateChecksumGenProbability is the probability [0-100] that checksum will be generated for mutable state`,
	)
	MutableStateChecksumVerifyProbability = NewNamespaceIntSetting(
		"history.mutableStateChecksumVerifyProbability",
		0,
		`MutableStateChecksumVerifyProbability is the probability [0-100] that checksum will be verified for mutable state`,
	)
	MutableStateChecksumInvalidateBefore = NewGlobalFloatSetting(
		"history.mutableStateChecksumInvalidateBefore",
		0,
		`MutableStateChecksumInvalidateBefore is the epoch timestamp before which all checksums are to be discarded`,
	)

	ReplicationTaskApplyTimeout = NewGlobalDurationSetting(
		"history.ReplicationTaskApplyTimeout",
		20*time.Second,
		`ReplicationTaskApplyTimeout is the context timeout for replication task apply`,
	)
	ReplicationTaskFetcherParallelism = NewGlobalIntSetting(
		"history.ReplicationTaskFetcherParallelism",
		4,
		`ReplicationTaskFetcherParallelism determines how many go routines we spin up for fetching tasks`,
	)
	ReplicationTaskFetcherAggregationInterval = NewGlobalDurationSetting(
		"history.ReplicationTaskFetcherAggregationInterval",
		2*time.Second,
		`ReplicationTaskFetcherAggregationInterval determines how frequently the fetch requests are sent`,
	)
	ReplicationTaskFetcherTimerJitterCoefficient = NewGlobalFloatSetting(
		"history.ReplicationTaskFetcherTimerJitterCoefficient",
		0.15,
		`ReplicationTaskFetcherTimerJitterCoefficient is the jitter for fetcher timer`,
	)
	ReplicationTaskFetcherErrorRetryWait = NewGlobalDurationSetting(
		"history.ReplicationTaskFetcherErrorRetryWait",
		time.Second,
		`ReplicationTaskFetcherErrorRetryWait is the wait time when fetcher encounters error`,
	)
	ReplicationTaskProcessorErrorRetryWait = NewShardIDDurationSetting(
		"history.ReplicationTaskProcessorErrorRetryWait",
		1*time.Second,
		`ReplicationTaskProcessorErrorRetryWait is the initial retry wait when we see errors in applying replication tasks`,
	)
	ReplicationTaskProcessorErrorRetryBackoffCoefficient = NewShardIDFloatSetting(
		"history.ReplicationTaskProcessorErrorRetryBackoffCoefficient",
		1.2,
		`ReplicationTaskProcessorErrorRetryBackoffCoefficient is the retry wait backoff time coefficient`,
	)
	ReplicationTaskProcessorErrorRetryMaxInterval = NewShardIDDurationSetting(
		"history.ReplicationTaskProcessorErrorRetryMaxInterval",
		5*time.Second,
		`ReplicationTaskProcessorErrorRetryMaxInterval is the retry wait backoff max duration`,
	)
	ReplicationTaskProcessorErrorRetryMaxAttempts = NewShardIDIntSetting(
		"history.ReplicationTaskProcessorErrorRetryMaxAttempts",
		80,
		`ReplicationTaskProcessorErrorRetryMaxAttempts is the max retry attempts for applying replication tasks`,
	)
	ReplicationTaskProcessorErrorRetryExpiration = NewShardIDDurationSetting(
		"history.ReplicationTaskProcessorErrorRetryExpiration",
		5*time.Minute,
		`ReplicationTaskProcessorErrorRetryExpiration is the max retry duration for applying replication tasks`,
	)
	ReplicationTaskProcessorNoTaskInitialWait = NewShardIDDurationSetting(
		"history.ReplicationTaskProcessorNoTaskInitialWait",
		2*time.Second,
		`ReplicationTaskProcessorNoTaskInitialWait is the wait time when not ask is returned`,
	)
	ReplicationTaskProcessorCleanupInterval = NewShardIDDurationSetting(
		"history.ReplicationTaskProcessorCleanupInterval",
		1*time.Minute,
		`ReplicationTaskProcessorCleanupInterval determines how frequently the cleanup replication queue`,
	)
	ReplicationTaskProcessorCleanupJitterCoefficient = NewShardIDFloatSetting(
		"history.ReplicationTaskProcessorCleanupJitterCoefficient",
		0.15,
		`ReplicationTaskProcessorCleanupJitterCoefficient is the jitter for cleanup timer`,
	)
	ReplicationTaskProcessorHostQPS = NewGlobalFloatSetting(
		"history.ReplicationTaskProcessorHostQPS",
		1500,
		`ReplicationTaskProcessorHostQPS is the qps of task processing rate limiter on host level`,
	)
	ReplicationTaskProcessorShardQPS = NewGlobalFloatSetting(
		"history.ReplicationTaskProcessorShardQPS",
		30,
		`ReplicationTaskProcessorShardQPS is the qps of task processing rate limiter on shard level`,
	)
	ReplicationEnableDLQMetrics = NewGlobalBoolSetting(
		"history.ReplicationEnableDLQMetrics",
		true,
		`ReplicationEnableDLQMetrics is the flag to emit DLQ metrics`,
	)
	ReplicationEnableUpdateWithNewTaskMerge = NewGlobalBoolSetting(
		"history.ReplicationEnableUpdateWithNewTaskMerge",
		false,
		`ReplicationEnableUpdateWithNewTaskMerge is the flag controlling whether replication task merging logic
should be enabled for non continuedAsNew workflow UpdateWithNew case.`,
	)
	ReplicationMultipleBatches = NewGlobalBoolSetting(
		"history.ReplicationMultipleBatches",
		false,
		`ReplicationMultipleBatches is the flag to enable replication of multiple history event batches`,
	)
	HistoryTaskDLQEnabled = NewGlobalBoolSetting(
		"history.TaskDLQEnabled",
		true,
		`HistoryTaskDLQEnabled enables the history task DLQ. This applies to internal tasks like transfer and timer tasks.
Do not turn this on if you aren't using Cassandra as the history task DLQ is not implemented for other databases.`,
	)
	HistoryTaskDLQUnexpectedErrorAttempts = NewGlobalIntSetting(
		"history.TaskDLQUnexpectedErrorAttempts",
		70,
		`HistoryTaskDLQUnexpectedErrorAttempts is the number of task execution attempts before sending the task to DLQ.`,
	)
	HistoryTaskDLQInternalErrors = NewGlobalBoolSetting(
		"history.TaskDLQInternalErrors",
		false,
		`HistoryTaskDLQInternalErrors causes history task processing to send tasks failing with serviceerror.Internal to
the dlq (or will drop them if not enabled)`,
	)
	HistoryTaskDLQErrorPattern = NewGlobalStringSetting(
		"history.TaskDLQErrorPattern",
		"",
		`HistoryTaskDLQErrorPattern specifies a regular expression. If a task processing error matches with this regex,
that task will be sent to DLQ.`,
	)

	MaxLocalParentWorkflowVerificationDuration = NewGlobalDurationSetting(
		"history.maxLocalParentWorkflowVerificationDuration",
		5*time.Minute,
		`MaxLocalParentWorkflowVerificationDuration controls the maximum duration to verify on the local cluster before requesting to resend parent workflow.`,
	)

	ReplicationStreamSyncStatusDuration = NewGlobalDurationSetting(
		"history.ReplicationStreamSyncStatusDuration",
		1*time.Second,
		`ReplicationStreamSyncStatusDuration sync replication status duration`,
	)
	ReplicationProcessorSchedulerQueueSize = NewGlobalIntSetting(
		"history.ReplicationProcessorSchedulerQueueSize",
		128,
		`ReplicationProcessorSchedulerQueueSize is the replication task executor queue size`,
	)
	ReplicationProcessorSchedulerWorkerCount = NewGlobalIntSetting(
		"history.ReplicationProcessorSchedulerWorkerCount",
		512,
		`ReplicationProcessorSchedulerWorkerCount is the replication task executor worker count`,
	)
	ReplicationLowPriorityProcessorSchedulerWorkerCount = NewGlobalIntSetting(
		"history.ReplicationLowPriorityProcessorSchedulerWorkerCount",
		128,
		`ReplicationLowPriorityProcessorSchedulerWorkerCount is the low priority replication task executor worker count`,
	)
	ReplicationLowPriorityTaskParallelism = NewGlobalIntSetting(
		"history.ReplicationLowPriorityTaskParallelism",
		1,
		`ReplicationLowPriorityTaskParallelism is the number of executions' low priority replication tasks that can be processed in parallel`,
	)

	EnableReplicationTaskBatching = NewGlobalBoolSetting(
		"history.EnableReplicationTaskBatching",
		false,
		`EnableReplicationTaskBatching is a feature flag for batching replicate history event task`,
	)
	EnableReplicationTaskTieredProcessing = NewGlobalBoolSetting(
		"history.EnableReplicationTaskTieredProcessing",
		false,
		`EnableReplicationTaskTieredProcessing is a feature flag for enabling tiered replication task processing stack`,
	)
	ReplicationStreamSenderHighPriorityQPS = NewGlobalIntSetting(
		"history.ReplicationStreamSenderHighPriorityQPS",
		100,
		`Maximum number of high priority replication tasks that can be sent per second per shard`,
	)
	ReplicationStreamSenderLowPriorityQPS = NewGlobalIntSetting(
		"history.ReplicationStreamSenderLowPriorityQPS",
		100,
		`Maximum number of low priority replication tasks that can be sent per second per shard`,
	)
	ReplicationStreamEventLoopRetryMaxAttempts = NewGlobalIntSetting(
		"history.ReplicationStreamEventLoopRetryMaxAttempts",
		100,
		`Max attempts for retrying replication stream event loop`,
	)
	ReplicationReceiverMaxOutstandingTaskCount = NewGlobalIntSetting(
		"history.ReplicationReceiverMaxOutstandingTaskCount",
		500,
		`Maximum number of outstanding tasks allowed for a single shard in the stream receiver`,
	)
	ReplicationResendMaxBatchCount = NewGlobalIntSetting(
		"history.ReplicationResendMaxBatchCount",
		10,
		`Maximum number of resend events batch for a single replication request`,
	)
	ReplicationProgressCacheMaxSize = NewGlobalIntSetting(
		"history.ReplicationProgressCacheMaxSize",
		128000,
		`ReplicationProgressCacheMaxSize is the maximum number of entries in the replication progress cache`,
	)
	ReplicationProgressCacheTTL = NewGlobalDurationSetting(
		"history.ReplicationProgressCacheTTL",
		time.Hour,
		`ReplicationProgressCacheTTL is TTL of replication progress cache`,
	)
	ReplicationStreamSendEmptyTaskDuration = NewGlobalDurationSetting(
		"history.ReplicationStreamSendEmptyTaskDuration",
		time.Minute,
		`ReplicationStreamSendEmptyTaskDuration is the interval to sync status when there is no replication task`,
	)
	ReplicationStreamReceiverLivenessMultiplier = NewGlobalIntSetting(
		"history.ReplicationReceiverLivenessMultiplier",
		3,
		"ReplicationStreamSendEmptyTask is the multiplier of liveness check interval on stream receiver",
	)
	ReplicationStreamSenderLivenessMultiplier = NewGlobalIntSetting(
		"history.ReplicationStreamSenderLivenessMultiplier",
		10,
		"ReplicationStreamSenderLivenessMultiplier is the multiplier of liveness check interval on stream sender",
	)
	EnableHistoryReplicationRateLimiter = NewNamespaceBoolSetting(
		"history.EnableHistoryReplicationRateLimiter",
		false,
		"EnableHistoryReplicationRateLimiter is the feature flag to enable rate limiter on history event replication",
	)
	ReplicationEnableRateLimit = NewGlobalBoolSetting(
		"history.ReplicationEnableRateLimit",
		true,
		`ReplicationEnableRateLimit is the feature flag to enable replication global rate limiter`,
	)
	ReplicationStreamSenderErrorRetryWait = NewGlobalDurationSetting(
		"history.ReplicationStreamSenderErrorRetryWait",
		1*time.Second,
		`ReplicationStreamSenderErrorRetryWait is the initial retry wait when we see errors in sending replication tasks`,
	)
	ReplicationStreamSenderErrorRetryBackoffCoefficient = NewGlobalFloatSetting(
		"history.ReplicationStreamSenderErrorRetryBackoffCoefficient",
		1.2,
		`ReplicationStreamSenderErrorRetryBackoffCoefficient is the retry wait backoff time coefficient`,
	)
	ReplicationStreamSenderErrorRetryMaxInterval = NewGlobalDurationSetting(
		"history.ReplicationStreamSenderErrorRetryMaxInterval",
		3*time.Second,
		`ReplicationStreamSenderErrorRetryMaxInterval is the retry wait backoff max duration`,
	)
	ReplicationStreamSenderErrorRetryMaxAttempts = NewGlobalIntSetting(
		"history.ReplicationStreamSenderErrorRetryMaxAttempts",
		80,
		`ReplicationStreamSenderErrorRetryMaxAttempts is the max retry attempts for sending replication tasks`,
	)
	ReplicationStreamSenderErrorRetryExpiration = NewGlobalDurationSetting(
		"history.ReplicationStreamSenderErrorRetryExpiration",
		3*time.Minute,
		`ReplicationStreamSenderErrorRetryExpiration is the max retry duration for sending replication tasks`,
	)
	ReplicationExecutableTaskErrorRetryWait = NewGlobalDurationSetting(
		"history.ReplicationExecutableTaskErrorRetryWait",
		1*time.Second,
		`ReplicationExecutableTaskErrorRetryWait is the initial retry wait when we see errors in executing replication tasks`,
	)
	ReplicationExecutableTaskErrorRetryBackoffCoefficient = NewGlobalFloatSetting(
		"history.ReplicationExecutableTaskErrorRetryBackoffCoefficient",
		1.2,
		`ReplicationExecutableTaskErrorRetryBackoffCoefficient is the retry wait backoff time coefficient`,
	)
	ReplicationExecutableTaskErrorRetryMaxInterval = NewGlobalDurationSetting(
		"history.ReplicationExecutableTaskErrorRetryMaxInterval",
		5*time.Second,
		`ReplicationExecutableTaskErrorRetryMaxInterval is the retry wait backoff max duration`,
	)
	ReplicationExecutableTaskErrorRetryMaxAttempts = NewGlobalIntSetting(
		"history.ReplicationExecutableTaskErrorRetryMaxAttempts",
		80,
		`ReplicationExecutableTaskErrorRetryMaxAttempts is the max retry attempts for executing replication tasks`,
	)
	ReplicationExecutableTaskErrorRetryExpiration = NewGlobalDurationSetting(
		"history.ReplicationExecutableTaskErrorRetryExpiration",
		10*time.Minute,
		`ReplicationExecutableTaskErrorRetryExpiration is the max retry duration for executing replication tasks`,
	)
	WorkflowIdReuseMinimalInterval = NewNamespaceDurationSetting(
		"history.workflowIdReuseMinimalInterval",
		1*time.Second,
		`WorkflowIdReuseMinimalInterval is used for timing how soon users can create new workflow with the same workflow ID.`,
	)
	EnableWorkflowIdReuseStartTimeValidation = NewNamespaceBoolSetting(
		"history.enableWorkflowIdReuseStartTimeValidation",
		false,
		`If true, validate the start time of the old workflow is older than WorkflowIdReuseMinimalInterval when reusing workflow ID.`,
	)
	HealthPersistenceLatencyFailure = NewGlobalFloatSetting(
		"history.healthPersistenceLatencyFailure",
		500,
		"History service health check on persistence average latency (millisecond) threshold",
	)
	HealthPersistenceErrorRatio = NewGlobalFloatSetting(
		"history.healthPersistenceErrorRatio",
		0.90,
		"History service health check on persistence error ratio",
	)
	HealthRPCLatencyFailure = NewGlobalFloatSetting(
		"history.healthRPCLatencyFailure",
		500,
		"History service health check on RPC average latency (millisecond) threshold",
	)
	HealthRPCErrorRatio = NewGlobalFloatSetting(
		"history.healthRPCErrorRatio",
		0.90,
		"History service health check on RPC error ratio",
	)
	SendRawHistoryBetweenInternalServices = NewGlobalBoolSetting(
		"history.sendRawHistoryBetweenInternalServices",
		false,
		`SendRawHistoryBetweenInternalServices is whether to send raw history events between internal temporal services`,
	)

	// TODO(rodrigozhou): This is temporary dynamic config to be removed before the next release.
	EnableRequestIdRefLinks = NewGlobalBoolSetting(
		"history.enableRequestIdRefLinks",
		false,
		"Enable generating request ID reference links",
	)

	EnableChasm = NewNamespaceBoolSetting(
		"history.enableChasm",
		false,
		"Use real chasm tree implementation instead of the noop one",
	)

	ChasmMaxInMemoryPureTasks = NewGlobalIntSetting(
		"history.chasmMaxInMemoryPureTasks",
		32,
		`ChasmMaxInMemoryPureTasks is the maximum number of physical pure tasks that can be held in memory for best effort task deletion.`,
	)

	EnableCHASMSchedulerCreation = NewNamespaceBoolSetting(
		"history.enableCHASMSchedulerCreation",
		false,
		`EnableCHASMSchedulerCreation controls whether new schedules are created using the CHASM (V2) implementation
instead of the existing (V1) implementation.`,
	)

	EnableCHASMSchedulerMigration = NewNamespaceBoolSetting(
		"history.enableCHASMSchedulerMigration",
		false,
		`EnableCHASMSchedulerMigration controls whether existing V1 schedules are automatically migrated
to the CHASM (V2) implementation on active scheduler workflows.`,
	)

	EnableCHASMCallbacks = NewNamespaceBoolSetting(
		"history.enableCHASMCallbacks",
		false,
		`Controls whether new callbacks are created using the CHASM implementation
instead of the previous HSM backed implementation.`,
	)

	VersionMembershipCacheTTL = NewGlobalDurationSetting(
		"history.versionMembershipCacheTTL",
		1*time.Second,
		`TTL for caching RPC results that check whether a version is present in a task queue.`,
	)

	VersionMembershipCacheMaxSize = NewGlobalIntSetting(
		"history.versionMembershipCacheMaxSize",
		10000,
		`Maximum number of entries in the version membership cache.`,
	)

	ExternalPayloadsEnabled = NewNamespaceBoolSetting(
		"history.externalPayloadsEnabled",
		false,
		`ExternalPayloadsEnabled controls whether external payload features are enabled for a namespace.`,
	)

	WorkerPersistenceMaxQPS = NewGlobalIntSetting(
		"worker.persistenceMaxQPS",
		500,
		`WorkerPersistenceMaxQPS is the max qps worker host can query DB`,
	)
	WorkerPersistenceGlobalMaxQPS = NewGlobalIntSetting(
		"worker.persistenceGlobalMaxQPS",
		0,
		`WorkerPersistenceGlobalMaxQPS is the max qps worker cluster can query DB`,
	)
	WorkerPersistenceNamespaceMaxQPS = NewNamespaceIntSetting(
		"worker.persistenceNamespaceMaxQPS",
		0,
		`WorkerPersistenceNamespaceMaxQPS is the max qps each namespace on worker host can query DB`,
	)
	WorkerPersistenceGlobalNamespaceMaxQPS = NewNamespaceIntSetting(
		"worker.persistenceGlobalNamespaceMaxQPS",
		0,
		`WorkerPersistenceNamespaceMaxQPS is the max qps each namespace in worker cluster can query DB`,
	)
	WorkerPersistenceDynamicRateLimitingParams = NewGlobalTypedSetting(
		"worker.persistenceDynamicRateLimitingParams",
		DefaultDynamicRateLimitingParams,
		`WorkerPersistenceDynamicRateLimitingParams is a struct that contains all adjustable dynamic rate limiting params.
Fields: Enabled, RefreshInterval, LatencyThreshold, ErrorThreshold, RateBackoffStepSize, RateIncreaseStepSize, RateMultiMin, RateMultiMax.
See DynamicRateLimitingParams comments for more details.`,
	)
	WorkerIndexerConcurrency = NewGlobalIntSetting(
		"worker.indexerConcurrency",
		100,
		`WorkerIndexerConcurrency is the max concurrent messages to be processed at any given time`,
	)
	WorkerESProcessorNumOfWorkers = NewGlobalIntSetting(
		"worker.ESProcessorNumOfWorkers",
		2,
		`WorkerESProcessorNumOfWorkers is num of workers for esProcessor`,
	)
	WorkerESProcessorBulkActions = NewGlobalIntSetting(
		"worker.ESProcessorBulkActions",
		500,
		`WorkerESProcessorBulkActions is max number of requests in bulk for esProcessor`,
	)
	WorkerESProcessorBulkSize = NewGlobalIntSetting(
		"worker.ESProcessorBulkSize",
		16*1024*1024,
		`WorkerESProcessorBulkSize is max total size of bulk in bytes for esProcessor`,
	)
	WorkerESProcessorFlushInterval = NewGlobalDurationSetting(
		"worker.ESProcessorFlushInterval",
		1*time.Second,
		`WorkerESProcessorFlushInterval is flush interval for esProcessor`,
	)
	WorkerESProcessorAckTimeout = NewGlobalDurationSetting(
		"worker.ESProcessorAckTimeout",
		30*time.Second,
		`WorkerESProcessorAckTimeout is the timeout that store will wait to get ack signal from ES processor.
Should be at least WorkerESProcessorFlushInterval+<time to process request>.`,
	)
	WorkerThrottledLogRPS = NewGlobalIntSetting(
		"worker.throttledLogRPS",
		20,
		`WorkerThrottledLogRPS is the rate limit on number of log messages emitted per second for throttled logger`,
	)
	WorkerScannerMaxConcurrentActivityExecutionSize = NewGlobalIntSetting(
		"worker.ScannerMaxConcurrentActivityExecutionSize",
		10,
		`WorkerScannerMaxConcurrentActivityExecutionSize indicates worker scanner max concurrent activity execution size`,
	)
	WorkerScannerMaxConcurrentWorkflowTaskExecutionSize = NewGlobalIntSetting(
		"worker.ScannerMaxConcurrentWorkflowTaskExecutionSize",
		10,
		`WorkerScannerMaxConcurrentWorkflowTaskExecutionSize indicates worker scanner max concurrent workflow execution size`,
	)
	WorkerScannerMaxConcurrentActivityTaskPollers = NewGlobalIntSetting(
		"worker.ScannerMaxConcurrentActivityTaskPollers",
		8,
		`WorkerScannerMaxConcurrentActivityTaskPollers indicates worker scanner max concurrent activity pollers`,
	)
	WorkerScannerMaxConcurrentWorkflowTaskPollers = NewGlobalIntSetting(
		"worker.ScannerMaxConcurrentWorkflowTaskPollers",
		8,
		`WorkerScannerMaxConcurrentWorkflowTaskPollers indicates worker scanner max concurrent workflow pollers`,
	)
	ScannerPersistenceMaxQPS = NewGlobalIntSetting(
		"worker.scannerPersistenceMaxQPS",
		100,
		`ScannerPersistenceMaxQPS is the maximum rate of persistence calls from worker.Scanner`,
	)
	ExecutionScannerPerHostQPS = NewGlobalIntSetting(
		"worker.executionScannerPerHostQPS",
		10,
		`ExecutionScannerPerHostQPS is the maximum rate of calls per host from executions.Scanner`,
	)
	ExecutionScannerPerShardQPS = NewGlobalIntSetting(
		"worker.executionScannerPerShardQPS",
		1,
		`ExecutionScannerPerShardQPS is the maximum rate of calls per shard from executions.Scanner`,
	)
	ExecutionDataDurationBuffer = NewGlobalDurationSetting(
		"worker.executionDataDurationBuffer",
		time.Hour*24*90,
		`ExecutionDataDurationBuffer is the data TTL duration buffer of execution data`,
	)
	ExecutionScannerWorkerCount = NewGlobalIntSetting(
		"worker.executionScannerWorkerCount",
		8,
		`ExecutionScannerWorkerCount is the execution scavenger worker count`,
	)
	ExecutionScannerHistoryEventIdValidator = NewGlobalBoolSetting(
		"worker.executionEnableHistoryEventIdValidator",
		true,
		`ExecutionScannerHistoryEventIdValidator is the flag to enable history event id validator`,
	)
	TaskQueueScannerEnabled = NewGlobalBoolSetting(
		"worker.taskQueueScannerEnabled",
		true,
		`TaskQueueScannerEnabled indicates if task queue scanner should be started as part of worker.Scanner`,
	)
	BuildIdScavengerEnabled = NewGlobalBoolSetting(
		"worker.buildIdScavengerEnabled",
		false,
		`BuildIdScavengerEnabled indicates if the build id scavenger should be started as part of worker.Scanner`,
	)
	HistoryScannerEnabled = NewGlobalBoolSetting(
		"worker.historyScannerEnabled",
		true,
		`HistoryScannerEnabled indicates if history scanner should be started as part of worker.Scanner`,
	)
	ExecutionsScannerEnabled = NewGlobalBoolSetting(
		"worker.executionsScannerEnabled",
		false,
		`ExecutionsScannerEnabled indicates if executions scanner should be started as part of worker.Scanner. This flag has no effect when SQL persistence is used,
because executions scanner support for SQL is not yet implemented.`,
	)
	HistoryScannerDataMinAge = NewGlobalDurationSetting(
		"worker.historyScannerDataMinAge",
		60*24*time.Hour,
		`HistoryScannerDataMinAge indicates the history scanner cleanup minimum age.`,
	)
	HistoryScannerVerifyRetention = NewGlobalBoolSetting(
		"worker.historyScannerVerifyRetention",
		true,
		`HistoryScannerVerifyRetention indicates the history scanner verify data retention.
If the service configures with archival feature enabled, update worker.historyScannerVerifyRetention to be double of the data retention.`,
	)
	EnableBatcherNamespace = NewNamespaceBoolSetting(
		"worker.enableNamespaceBatcher",
		true,
		`EnableBatcher decides whether to start new (per-namespace) batcher in our worker`,
	)
	BatcherRPS = NewNamespaceIntSetting(
		"worker.batcherRPS",
		50,
		`BatcherRPS controls number the rps of batch operations`,
	)
	BatcherConcurrency = NewNamespaceIntSetting(
		"worker.batcherConcurrency",
		5,
		`BatcherConcurrency controls the concurrency of one batch operation`,
	)
	WorkerParentCloseMaxConcurrentActivityExecutionSize = NewGlobalIntSetting(
		"worker.ParentCloseMaxConcurrentActivityExecutionSize",
		1000,
		`WorkerParentCloseMaxConcurrentActivityExecutionSize indicates worker parent close worker max concurrent activity execution size`,
	)
	WorkerParentCloseMaxConcurrentWorkflowTaskExecutionSize = NewGlobalIntSetting(
		"worker.ParentCloseMaxConcurrentWorkflowTaskExecutionSize",
		1000,
		`WorkerParentCloseMaxConcurrentWorkflowTaskExecutionSize indicates worker parent close worker max concurrent workflow execution size`,
	)
	WorkerParentCloseMaxConcurrentActivityTaskPollers = NewGlobalIntSetting(
		"worker.ParentCloseMaxConcurrentActivityTaskPollers",
		4,
		`WorkerParentCloseMaxConcurrentActivityTaskPollers indicates worker parent close worker max concurrent activity pollers`,
	)
	WorkerParentCloseMaxConcurrentWorkflowTaskPollers = NewGlobalIntSetting(
		"worker.ParentCloseMaxConcurrentWorkflowTaskPollers",
		4,
		`WorkerParentCloseMaxConcurrentWorkflowTaskPollers indicates worker parent close worker max concurrent workflow pollers`,
	)
	WorkerPerNamespaceWorkerCount = NewNamespaceIntSetting(
		"worker.perNamespaceWorkerCount",
		1,
		`WorkerPerNamespaceWorkerCount controls number of per-ns (scheduler, batcher, etc.) workers to run per namespace`,
	)
	WorkerPerNamespaceWorkerOptions = NewNamespaceTypedSetting(
		"worker.perNamespaceWorkerOptions",
		sdkworker.Options{},
		`WorkerPerNamespaceWorkerOptions are SDK worker options for per-namespace workers`,
	)
	WorkerPerNamespaceWorkerStartRate = NewGlobalFloatSetting(
		"worker.perNamespaceWorkerStartRate",
		10.0,
		`WorkerPerNamespaceWorkerStartRate controls how fast per-namespace workers can be started (workers/second)`,
	)
	WorkerEnableScheduler = NewNamespaceBoolSetting(
		"worker.enableScheduler",
		true,
		`WorkerEnableScheduler controls whether to start the worker for scheduled workflows`,
	)
	WorkerStickyCacheSize = NewGlobalIntSetting(
		"worker.stickyCacheSize",
		0,
		`WorkerStickyCacheSize controls the sticky cache size for SDK workers on worker nodes
(shared between all workers in the process, cannot be changed after startup)`,
	)
	SchedulerNamespaceStartWorkflowRPS = NewNamespaceFloatSetting(
		"worker.schedulerNamespaceStartWorkflowRPS",
		30.0,
		`SchedulerNamespaceStartWorkflowRPS is the per-namespace limit for starting workflows by schedules`,
	)
	SchedulerLocalActivitySleepLimit = NewNamespaceDurationSetting(
		"worker.schedulerLocalActivitySleepLimit",
		5*time.Second,
		`How long to sleep within a local activity before pushing to workflow level sleep (don't make this
close to or more than the workflow task timeout)`,
	)
	WorkerDeleteNamespaceActivityLimits = NewGlobalTypedSetting(
		"worker.deleteNamespaceActivityLimitsConfig",
		sdkworker.Options{},
		`WorkerDeleteNamespaceActivityLimitsConfig is a struct with relevant sdkworker.Options
settings for controlling remote activity concurrency for delete namespace workflows.
Valid fields: MaxConcurrentActivityExecutionSize, TaskQueueActivitiesPerSecond,
WorkerActivitiesPerSecond, MaxConcurrentActivityTaskPollers.
`,
	)
	WorkerGenerateMigrationTaskViaFrontend = NewGlobalBoolSetting(
		"worker.generateMigrationTaskViaFrontend",
		false,
		`WorkerGenerateMigrationTaskViaFrontend controls whether to generate migration tasks via frontend admin service.`,
	)
	WorkerEnableHistoryRateLimiter = NewGlobalBoolSetting(
		"worker.enableHistoryRateLimiter",
		false,
		`WorkerEnableHistoryRateLimiter decides whether to generate migration tasks with history length rate limiter.`,
	)
	MaxUserMetadataSummarySize = NewNamespaceIntSetting(
		"limit.userMetadataSummarySize",
		400,
		`MaxUserMetadataSummarySize is the maximum size of user metadata summary payloads in bytes.`,
	)
	MaxUserMetadataDetailsSize = NewNamespaceIntSetting(
		"limit.userMetadataDetailsSize",
		20000,
		`MaxUserMetadataDetailsSize is the maximum size of user metadata details payloads in bytes.`,
	)

	LogAllReqErrors = NewNamespaceBoolSetting(
		"system.logAllReqErrors",
		false,
		`When set to true, logs all RPC/request errors for the namespace, not just unexpected ones.`,
	)

	WorkflowRulesAPIsEnabled = NewNamespaceBoolSetting(
		"frontend.workflowRulesAPIsEnabled",
		false,
		`WorkflowRulesAPIsEnabled is a "feature enable" flag. `,
	)

	MaxWorkflowRulesPerNamespace = NewNamespaceIntSetting(
		"frontend.maxWorkflowRulesPerNamespace",
		10,
		`Maximum number of workflow rules in a given namespace`,
	)

	SlowRequestLoggingThreshold = NewGlobalDurationSetting(
		"rpc.slowRequestLoggingThreshold",
		5*time.Second,
		`SlowRequestLoggingThreshold is the threshold above which a gRPC request is considered slow and logged.`,
	)

	WorkerHeartbeatsEnabled = NewNamespaceBoolSetting(
		"frontend.WorkerHeartbeatsEnabled",
		true,
		`WorkerHeartbeatsEnabled is a "feature enable" flag. It allows workers to send periodic heartbeats to the server.`,
	)

	ListWorkersEnabled = NewNamespaceBoolSetting(
		"frontend.ListWorkersEnabled",
		true,
		`ListWorkersEnabled is a "feature enable" flag. It allows clients to get workers heartbeat information.`,
	)

	WorkerCommandsEnabled = NewNamespaceBoolSetting(
		"frontend.WorkerCommandsEnabled",
		false,
		`WorkerCommandsEnabled is a "feature enable" flag. It allows clients to send commands to the workers.`,
	)

	WorkflowPauseEnabled = NewNamespaceBoolSetting(
		"frontend.WorkflowPauseEnabled",
		false,
		`WorkflowPauseEnabled is a "feature enable" flag. When enabled it allows clients to pause workflows.`,
	)
)
View Source
var (
	MatchAnythingRE = regexp.MustCompile(".*")
	MatchNothingRE  = regexp.MustCompile(".^")
)
View Source
var DefaultDynamicRateLimitingParams = DynamicRateLimitingParams{
	Enabled:              false,
	RefreshInterval:      10 * time.Second,
	LatencyThreshold:     0.0,
	ErrorThreshold:       0.0,
	RateBackoffStepSize:  0.3,
	RateIncreaseStepSize: 0.1,
	RateMultiMin:         0.8,
	RateMultiMax:         1.0,
}
View Source
var DefaultHistoryCacheBackgroundEvictSettings = CacheBackgroundEvictSettings{
	Enabled:         false,
	LoopInterval:    1 * time.Minute,
	MaxEntryPerCall: 1024,
}
View Source
var DefaultPerShardNamespaceRPSMax = GetIntPropertyFnFilteredByNamespace(0)
View Source
var Module = fx.Options(
	fx.Provide(func(client Client, logger log.Logger, lc fx.Lifecycle) *Collection {
		col := NewCollection(client, logger)
		lc.Append(fx.StartStopHook(col.Start, col.Stop))
		return col
	}),
	fx.Provide(fx.Annotate(
		func(c *Collection) pingable.Pingable { return c },
		fx.ResultTags(`group:"deadlockDetectorRoots"`),
	)),
)
Functions ¶
func ConvertGradualChange ¶
added in v1.30.0
func ConvertGradualChange[T any](def T) func(v any) (GradualChange[T], error)

ConvertGradualChange is a conversion function that can handle a plain T (which represents a static value) as well as a GradualChange[T]. It can be used to turn settings that were not of type GradualChange into a GradualChange. nolint:revive // cognitive-complexity // this looks complicated but each case is fairly simple

func ConvertStructure ¶
added in v1.25.0
func ConvertStructure[T any](def T) func(v any) (T, error)

ConvertStructure can be used as a conversion function for New*TypedSettingWithConverter. The value from dynamic config will be converted to T, on top of the given default.

Note that any failure in conversion of _any_ field will result in the overall default being used, ignoring the fields that successfully converted.

Note that the default value will be deep-copied and then passed to mapstructure with the ZeroFields setting false, so the config value will be _merged_ on top of it. Be very careful when using non-empty maps or slices, the result may not be what you want.

To avoid confusion, the default passed to ConvertStructure should be either the same as the overall default for the setting (if you want any value set to be merged over the default, i.e. treat the fields independently), or the zero value of its type (if you want to treat the fields as a group and default unset fields to zero).

func ConvertWildcardStringListToRegexp ¶
added in v1.29.0
func ConvertWildcardStringListToRegexp(in any) (*regexp.Regexp, error)
func NewFileBasedClient ¶
func NewFileBasedClient(config *FileBasedClientConfig, logger log.Logger, doneCh <-chan interface{}) (*fileBasedClient, error)

NewFileBasedClient creates a file based client.

func NewFileBasedClientWithReader ¶
added in v1.16.0
func NewFileBasedClientWithReader(reader FileReader, config *FileBasedClientConfig, logger log.Logger, doneCh <-chan interface{}) (*fileBasedClient, error)
func ResetRegistryForTest ¶
added in v1.25.0
func ResetRegistryForTest()

For testing only; do not call from regular code!

func SubscribeGradualChange ¶
added in v1.30.0
func SubscribeGradualChange[T any](
	subscribable TypedSubscribable[GradualChange[T]],
	changeKey []byte,
	callback func(T),
	timeSource clock.TimeSource,
) (T, func())

SubscribeGradualChange is a helper that allows subscribing to a GradualChange[T] as if it was a T. It handles setting a timer for when the setting may change in the future.

Types ¶
type BoolPropertyFn ¶
type BoolPropertyFn = TypedPropertyFn[bool]
func GetBoolPropertyFn ¶
func GetBoolPropertyFn(value bool) BoolPropertyFn
type BoolPropertyFnWithDestinationFilter ¶
added in v1.24.0
type BoolPropertyFnWithDestinationFilter = TypedPropertyFnWithDestinationFilter[bool]
func GetBoolPropertyFnFilteredByDestination ¶
added in v1.25.0
func GetBoolPropertyFnFilteredByDestination(value bool) BoolPropertyFnWithDestinationFilter
type BoolPropertyFnWithNamespaceFilter ¶
type BoolPropertyFnWithNamespaceFilter = TypedPropertyFnWithNamespaceFilter[bool]
func GetBoolPropertyFnFilteredByNamespace ¶
func GetBoolPropertyFnFilteredByNamespace(value bool) BoolPropertyFnWithNamespaceFilter
type BoolPropertyFnWithNamespaceIDFilter ¶
type BoolPropertyFnWithNamespaceIDFilter = TypedPropertyFnWithNamespaceIDFilter[bool]
func GetBoolPropertyFnFilteredByNamespaceID ¶
added in v1.25.0
func GetBoolPropertyFnFilteredByNamespaceID(value bool) BoolPropertyFnWithNamespaceIDFilter
type BoolPropertyFnWithShardIDFilter ¶
added in v1.25.0
type BoolPropertyFnWithShardIDFilter = TypedPropertyFnWithShardIDFilter[bool]
func GetBoolPropertyFnFilteredByShardID ¶
added in v1.25.0
func GetBoolPropertyFnFilteredByShardID(value bool) BoolPropertyFnWithShardIDFilter
type BoolPropertyFnWithTaskQueueFilter ¶
added in v1.24.0
type BoolPropertyFnWithTaskQueueFilter = TypedPropertyFnWithTaskQueueFilter[bool]
func GetBoolPropertyFnFilteredByTaskQueue ¶
added in v1.25.0
func GetBoolPropertyFnFilteredByTaskQueue(value bool) BoolPropertyFnWithTaskQueueFilter
type BoolPropertyFnWithTaskTypeFilter ¶
added in v1.25.0
type BoolPropertyFnWithTaskTypeFilter = TypedPropertyFnWithTaskTypeFilter[bool]
func GetBoolPropertyFnFilteredByTaskType ¶
added in v1.25.0
func GetBoolPropertyFnFilteredByTaskType(value bool) BoolPropertyFnWithTaskTypeFilter
type CacheBackgroundEvictSettings ¶
added in v1.29.0
type CacheBackgroundEvictSettings struct {
	// Enabled controls whether background purging of expired entries is active. To enable,
	// this must be set to true at process start, but can be dynamically set to false to
	// stop scanning entries.
	Enabled bool
	// LoopInterval is the frequency that a background goroutine scans for expired entries.
	LoopInterval time.Duration
	// MaxEntryPerCall is the max number of entries that are scanned while the cache is locked.
	MaxEntryPerCall int
}
type CircuitBreakerSettings ¶
added in v1.25.0
type CircuitBreakerSettings struct {
	// MaxRequests: Maximum number of requests allowed to pass through when
	// it is in half-open state (default 1).
	MaxRequests int
	// Interval: Cyclic period in closed state to clear the internal counts;
	// if interval is 0, then it never clears the internal counts (default 0).
	Interval time.Duration
	// Timeout: Period of open state before changing to half-open state (default 60s).`
	Timeout time.Duration
}
type Client ¶
type Client interface {
	// GetValue returns a set of values and associated constraints for a key. Not all
	// constraints are valid for all keys.
	//
	// The returned slice of ConstrainedValues is treated as a set, and order does not
	// matter. The effective order of constraints is determined by server logic. See the
	// comment on Constraints below.
	//
	// If none of the ConstrainedValues match the constraints being used for the key, then
	// the server default value will be used.
	//
	// Note that GetValue is called very often! You should not synchronously call out to an
	// external system. Instead you should keep a set of all configured values, refresh it
	// periodically or when notified, and only do in-memory lookups inside of GetValue.
	//
	// Implementations should prefer to return the same slice in response to the same key
	// as long as the value hasn't changed. Value conversions are cached using weak
	// pointers into the returned slice, so new slices will result in unnecessary calls to
	// conversion functions.
	GetValue(key Key) []ConstrainedValue
}

Client is a source of dynamic configuration. The default Client, fileBasedClient, reads from a file in the filesystem, and refreshes it periodically. You can extend the server with an alternate Client using ServerOptions.

func NewNoopClient ¶
func NewNoopClient() Client

NewNoopClient returns a Client that has no keys (a Collection using it will always return default values).

type ClientUpdateFunc ¶
added in v1.25.0
type ClientUpdateFunc func(map[Key][]ConstrainedValue)

Called with modified keys on any change to the current value set. Deleted keys/constraints will get a nil value.

type Collection ¶
type Collection struct {
	// contains filtered or unexported fields
}

Collection implements lookup and constraint logic on top of a Client. The rest of the server code should use Collection as the interface to dynamic config, instead of the low-level Client.

func NewCollection ¶
func NewCollection(client Client, logger log.Logger) *Collection

NewCollection creates a new collection. For subscriptions to work, you must call Start/Stop. Get will work without Start/Stop.

func NewNoopCollection ¶
func NewNoopCollection() *Collection

NewNoopCollection creates a new noop collection.

func (*Collection) GetPingChecks ¶
added in v1.25.0
func (c *Collection) GetPingChecks() []pingable.Check

Implement pingable.Pingable

func (*Collection) Start ¶
added in v1.25.0
func (c *Collection) Start()
func (*Collection) Stop ¶
added in v1.25.0
func (c *Collection) Stop()
type ConfigValueMap ¶
added in v1.30.0
type ConfigValueMap map[Key][]ConstrainedValue
func DiffAndLogConfigs ¶
added in v1.30.0
func DiffAndLogConfigs(logger log.Logger, oldValues ConfigValueMap, newValues ConfigValueMap) ConfigValueMap

DiffAndLogConfigs computes the difference between two ConfigValueMaps. The result is returned as a ConfigValueMap that can be merged with old to produce new, except with deleted keys mapped to nil. It also logs the differences to a logger.

type ConstrainedValue ¶
added in v1.17.3
type ConstrainedValue struct {
	Constraints Constraints
	Value       any
}

ConstrainedValue is a value plus associated constraints.

The type of the Value field depends on the key. Acceptable types will be one of:

int, float64, bool, string, map[string]any, time.Duration


If time.Duration is expected, a string is also accepted, which will be converted using timestamp.ParseDurationDefaultDays. If float64 is expected, int is also accepted. In other cases, the exact type must be used. If a Value is returned with an unexpected type, it will be ignored.

type Constraints ¶
added in v1.18.0
type Constraints struct {
	Namespace     string
	NamespaceID   string
	TaskQueueName string
	Destination   string
	TaskQueueType enumspb.TaskQueueType
	ShardID       int32
	TaskType      enumsspb.TaskType
}

Constraints describe under what conditions a ConstrainedValue should be used. There are few standard "constraint precedence orders" that the server uses:

global precedence:
  no constraints
namespace precedence:
  Namespace
  no constraints
task queue precedence
  Namespace+TaskQueueName+TaskQueueType
  Namespace+TaskQueueName
  TaskQueueName
  Namespace
  no constraints
shard id precedence:
  ShardID
  no constraints


In each case, the constraints that the server is checking and the constraints that apply to the value must match exactly, including the fields that are not set (zero values). That is, for keys that use namespace precedence, you must either return a ConstrainedValue with only Namespace set, or with no fields set. (Or return one of each.) If you return a ConstrainedValue with Namespace and ShardID set, for example, that value will never be used, even if the Namespace matches.

type DestinationBoolConstrainedDefaultSetting ¶
added in v1.29.0
type DestinationBoolConstrainedDefaultSetting = DestinationTypedConstrainedDefaultSetting[bool]
func NewDestinationBoolSettingWithConstrainedDefault ¶
added in v1.25.0
func NewDestinationBoolSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[bool], description string) DestinationBoolConstrainedDefaultSetting
type DestinationBoolSetting ¶
added in v1.25.0
type DestinationBoolSetting = DestinationTypedSetting[bool]
func NewDestinationBoolSetting ¶
added in v1.25.0
func NewDestinationBoolSetting(key string, def bool, description string) DestinationBoolSetting
type DestinationDurationConstrainedDefaultSetting ¶
added in v1.29.0
type DestinationDurationConstrainedDefaultSetting = DestinationTypedConstrainedDefaultSetting[time.Duration]
func NewDestinationDurationSettingWithConstrainedDefault ¶
added in v1.25.0
func NewDestinationDurationSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[time.Duration], description string) DestinationDurationConstrainedDefaultSetting
type DestinationDurationSetting ¶
added in v1.25.0
type DestinationDurationSetting = DestinationTypedSetting[time.Duration]
func NewDestinationDurationSetting ¶
added in v1.25.0
func NewDestinationDurationSetting(key string, def time.Duration, description string) DestinationDurationSetting
type DestinationFloatConstrainedDefaultSetting ¶
added in v1.29.0
type DestinationFloatConstrainedDefaultSetting = DestinationTypedConstrainedDefaultSetting[float64]
func NewDestinationFloatSettingWithConstrainedDefault ¶
added in v1.25.0
func NewDestinationFloatSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[float64], description string) DestinationFloatConstrainedDefaultSetting
type DestinationFloatSetting ¶
added in v1.25.0
type DestinationFloatSetting = DestinationTypedSetting[float64]
func NewDestinationFloatSetting ¶
added in v1.25.0
func NewDestinationFloatSetting(key string, def float64, description string) DestinationFloatSetting
type DestinationIntConstrainedDefaultSetting ¶
added in v1.29.0
type DestinationIntConstrainedDefaultSetting = DestinationTypedConstrainedDefaultSetting[int]
func NewDestinationIntSettingWithConstrainedDefault ¶
added in v1.25.0
func NewDestinationIntSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[int], description string) DestinationIntConstrainedDefaultSetting
type DestinationIntSetting ¶
added in v1.25.0
type DestinationIntSetting = DestinationTypedSetting[int]
func NewDestinationIntSetting ¶
added in v1.25.0
func NewDestinationIntSetting(key string, def int, description string) DestinationIntSetting
type DestinationMapConstrainedDefaultSetting ¶
added in v1.29.0
type DestinationMapConstrainedDefaultSetting = DestinationTypedConstrainedDefaultSetting[map[string]any]
func NewDestinationMapSettingWithConstrainedDefault ¶
added in v1.25.0
func NewDestinationMapSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[map[string]any], description string) DestinationMapConstrainedDefaultSetting
type DestinationMapSetting ¶
added in v1.25.0
type DestinationMapSetting = DestinationTypedSetting[map[string]any]
func NewDestinationMapSetting ¶
added in v1.25.0
func NewDestinationMapSetting(key string, def map[string]any, description string) DestinationMapSetting
type DestinationStringConstrainedDefaultSetting ¶
added in v1.29.0
type DestinationStringConstrainedDefaultSetting = DestinationTypedConstrainedDefaultSetting[string]
func NewDestinationStringSettingWithConstrainedDefault ¶
added in v1.25.0
func NewDestinationStringSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[string], description string) DestinationStringConstrainedDefaultSetting
type DestinationStringSetting ¶
added in v1.25.0
type DestinationStringSetting = DestinationTypedSetting[string]
func NewDestinationStringSetting ¶
added in v1.25.0
func NewDestinationStringSetting(key string, def string, description string) DestinationStringSetting
type DestinationTypedConstrainedDefaultSetting ¶
added in v1.29.0
type DestinationTypedConstrainedDefaultSetting[T any] constrainedDefaultSetting[T, func(namespace string, destination string)]
func NewDestinationTypedSettingWithConstrainedDefault ¶
added in v1.25.0
func NewDestinationTypedSettingWithConstrainedDefault[T any](key string, convert func(any) (T, error), cdef []TypedConstrainedValue[T], description string) DestinationTypedConstrainedDefaultSetting[T]

NewDestinationTypedSettingWithConstrainedDefault creates a setting with a compound default value.

func (DestinationTypedConstrainedDefaultSetting[T]) Get ¶
added in v1.29.0
func (s DestinationTypedConstrainedDefaultSetting[T]) Get(c *Collection) TypedPropertyFnWithDestinationFilter[T]
func (DestinationTypedConstrainedDefaultSetting[T]) Key ¶
added in v1.29.0
func (s DestinationTypedConstrainedDefaultSetting[T]) Key() Key
func (DestinationTypedConstrainedDefaultSetting[T]) Precedence ¶
added in v1.29.0
func (s DestinationTypedConstrainedDefaultSetting[T]) Precedence() Precedence
func (DestinationTypedConstrainedDefaultSetting[T]) Subscribe ¶
added in v1.29.0
func (s DestinationTypedConstrainedDefaultSetting[T]) Subscribe(c *Collection) TypedSubscribableWithDestinationFilter[T]
func (DestinationTypedConstrainedDefaultSetting[T]) Validate ¶
added in v1.29.0
func (s DestinationTypedConstrainedDefaultSetting[T]) Validate(v any) error
type DestinationTypedSetting ¶
added in v1.25.0
type DestinationTypedSetting[T any] setting[T, func(namespace string, destination string)]
func NewDestinationTypedSetting ¶
added in v1.25.0
func NewDestinationTypedSetting[T any](key string, def T, description string) DestinationTypedSetting[T]

NewDestinationTypedSetting creates a setting that uses mapstructure to handle complex structured values. The value from dynamic config will be _merged_ over a deep copy of 'def'. Be very careful when using non-empty maps or slices as defaults, the result may not be what you want.

func NewDestinationTypedSettingWithConverter ¶
added in v1.25.0
func NewDestinationTypedSettingWithConverter[T any](key string, convert func(any) (T, error), def T, description string) DestinationTypedSetting[T]

NewDestinationTypedSettingWithConverter creates a setting with a custom converter function.

func (DestinationTypedSetting[T]) Get ¶
added in v1.25.0
func (s DestinationTypedSetting[T]) Get(c *Collection) TypedPropertyFnWithDestinationFilter[T]
func (DestinationTypedSetting[T]) Key ¶
added in v1.25.0
func (s DestinationTypedSetting[T]) Key() Key
func (DestinationTypedSetting[T]) Precedence ¶
added in v1.25.0
func (s DestinationTypedSetting[T]) Precedence() Precedence
func (DestinationTypedSetting[T]) Subscribe ¶
added in v1.25.0
func (s DestinationTypedSetting[T]) Subscribe(c *Collection) TypedSubscribableWithDestinationFilter[T]
func (DestinationTypedSetting[T]) Validate ¶
added in v1.25.0
func (s DestinationTypedSetting[T]) Validate(v any) error
func (DestinationTypedSetting[T]) WithDefault ¶
added in v1.25.0
func (s DestinationTypedSetting[T]) WithDefault(v T) DestinationTypedSetting[T]
type DurationPropertyFn ¶
type DurationPropertyFn = TypedPropertyFn[time.Duration]
func GetDurationPropertyFn ¶
func GetDurationPropertyFn(value time.Duration) DurationPropertyFn
type DurationPropertyFnWithDestinationFilter ¶
added in v1.24.0
type DurationPropertyFnWithDestinationFilter = TypedPropertyFnWithDestinationFilter[time.Duration]
func GetDurationPropertyFnFilteredByDestination ¶
added in v1.25.0
func GetDurationPropertyFnFilteredByDestination(value time.Duration) DurationPropertyFnWithDestinationFilter
type DurationPropertyFnWithNamespaceFilter ¶
type DurationPropertyFnWithNamespaceFilter = TypedPropertyFnWithNamespaceFilter[time.Duration]
func GetDurationPropertyFnFilteredByNamespace ¶
func GetDurationPropertyFnFilteredByNamespace(value time.Duration) DurationPropertyFnWithNamespaceFilter
type DurationPropertyFnWithNamespaceIDFilter ¶
type DurationPropertyFnWithNamespaceIDFilter = TypedPropertyFnWithNamespaceIDFilter[time.Duration]
func GetDurationPropertyFnFilteredByNamespaceID ¶
added in v1.25.0
func GetDurationPropertyFnFilteredByNamespaceID(value time.Duration) DurationPropertyFnWithNamespaceIDFilter
type DurationPropertyFnWithShardIDFilter ¶
type DurationPropertyFnWithShardIDFilter = TypedPropertyFnWithShardIDFilter[time.Duration]
func GetDurationPropertyFnFilteredByShardID ¶
added in v1.25.0
func GetDurationPropertyFnFilteredByShardID(value time.Duration) DurationPropertyFnWithShardIDFilter
type DurationPropertyFnWithTaskQueueFilter ¶
added in v1.24.0
type DurationPropertyFnWithTaskQueueFilter = TypedPropertyFnWithTaskQueueFilter[time.Duration]
func GetDurationPropertyFnFilteredByTaskQueue ¶
added in v1.25.0
func GetDurationPropertyFnFilteredByTaskQueue(value time.Duration) DurationPropertyFnWithTaskQueueFilter
type DurationPropertyFnWithTaskTypeFilter ¶
added in v1.18.1
type DurationPropertyFnWithTaskTypeFilter = TypedPropertyFnWithTaskTypeFilter[time.Duration]
func GetDurationPropertyFnFilteredByTaskType ¶
added in v1.25.0
func GetDurationPropertyFnFilteredByTaskType(value time.Duration) DurationPropertyFnWithTaskTypeFilter
type DynamicRateLimitingParams ¶
added in v1.25.0
type DynamicRateLimitingParams struct {
	// Enabled toggles whether dynamic rate limiting is enabled.
	Enabled bool
	// RefreshInterval is how often the rate limit and dynamic properties are refreshed. Should
	// be a string duratoin e.g. 10s even if the rate limiter is disabled, this property will
	// still determine how often the dynamic config is reevaluated.
	RefreshInterval time.Duration
	// LatencyThreshold is the maximum average latency in ms before the rate limiter should
	// backoff.
	LatencyThreshold float64
	// ErrorThreshold is the maximum ratio of errors:total_requests before the rate limiter
	// Should backoff. Should be between 0 and 1.
	ErrorThreshold float64
	// RateBackoffStepSize is the amount the rate limit multiplier is reduced when backing off.
	// Should be between 0 and 1
	RateBackoffStepSize float64
	// RateIncreaseStepSize is the amount the rate limit multiplier is increased when the
	// system is healthy and current rate < max rate. Should be between 0 and 1.
	RateIncreaseStepSize float64
	// RateMultiMin is the minimum the rate limit multiplier can be reduced to.
	RateMultiMin float64
	// RateMultiMax is the maximum the rate limit multiplier can be increased to.
	RateMultiMax float64
}

params for controlling dynamic rate limiting options

type FileBasedClientConfig ¶
type FileBasedClientConfig struct {
	Filepath     string        `yaml:"filepath"`
	PollInterval time.Duration `yaml:"pollInterval"`
}

FileBasedClientConfig is the config for the file based dynamic config client. It specifies where the config file is stored and how often the config should be updated by checking the config file again.

type FileReader ¶
added in v1.25.0
type FileReader interface {
	GetModTime() (time.Time, error)
	ReadFile() ([]byte, error)
}
type FloatPropertyFn ¶
type FloatPropertyFn = TypedPropertyFn[float64]
func GetFloatPropertyFn ¶
func GetFloatPropertyFn(value float64) FloatPropertyFn
type FloatPropertyFnWithDestinationFilter ¶
added in v1.24.0
type FloatPropertyFnWithDestinationFilter = TypedPropertyFnWithDestinationFilter[float64]
func GetFloatPropertyFnFilteredByDestination ¶
added in v1.25.0
func GetFloatPropertyFnFilteredByDestination(value float64) FloatPropertyFnWithDestinationFilter
type FloatPropertyFnWithNamespaceFilter ¶
type FloatPropertyFnWithNamespaceFilter = TypedPropertyFnWithNamespaceFilter[float64]
func GetFloatPropertyFnFilteredByNamespace ¶
added in v1.25.0
func GetFloatPropertyFnFilteredByNamespace(value float64) FloatPropertyFnWithNamespaceFilter
type FloatPropertyFnWithNamespaceIDFilter ¶
added in v1.25.0
type FloatPropertyFnWithNamespaceIDFilter = TypedPropertyFnWithNamespaceIDFilter[float64]
func GetFloatPropertyFnFilteredByNamespaceID ¶
added in v1.25.0
func GetFloatPropertyFnFilteredByNamespaceID(value float64) FloatPropertyFnWithNamespaceIDFilter
type FloatPropertyFnWithShardIDFilter ¶
type FloatPropertyFnWithShardIDFilter = TypedPropertyFnWithShardIDFilter[float64]
func GetFloatPropertyFnFilteredByShardID ¶
added in v1.25.0
func GetFloatPropertyFnFilteredByShardID(value float64) FloatPropertyFnWithShardIDFilter
type FloatPropertyFnWithTaskQueueFilter ¶
added in v1.24.0
type FloatPropertyFnWithTaskQueueFilter = TypedPropertyFnWithTaskQueueFilter[float64]
func GetFloatPropertyFnFilteredByTaskQueue ¶
added in v1.25.0
func GetFloatPropertyFnFilteredByTaskQueue(value float64) FloatPropertyFnWithTaskQueueFilter
type FloatPropertyFnWithTaskTypeFilter ¶
added in v1.25.0
type FloatPropertyFnWithTaskTypeFilter = TypedPropertyFnWithTaskTypeFilter[float64]
func GetFloatPropertyFnFilteredByTaskType ¶
added in v1.25.0
func GetFloatPropertyFnFilteredByTaskType(value float64) FloatPropertyFnWithTaskTypeFilter
type GenericParseHook ¶
added in v1.29.0
type GenericParseHook[S, T any] interface {
	DynamicConfigParseHook(S) (T, error)
}

GenericParseHook is an interface that may be implemented by a setting type or a field contained inside a struct setting type. It should be implemented with a non-pointer receiver that will be ignored, and return the parsed value and any parse error. Type "S" is usually "string", and "T" must be the same as the receiver type.

type GenericSetting ¶
added in v1.25.0
type GenericSetting interface {
	Key() Key
	Precedence() Precedence
	Validate(v any) error
	// contains filtered or unexported methods
}

GenericSetting is an interface that all instances of Setting implement (by generated code in setting_gen.go). It can be used to refer to settings of any type and deal with them generically..

type GlobalBoolConstrainedDefaultSetting ¶
added in v1.29.0
type GlobalBoolConstrainedDefaultSetting = GlobalTypedConstrainedDefaultSetting[bool]
func NewGlobalBoolSettingWithConstrainedDefault ¶
added in v1.25.0
func NewGlobalBoolSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[bool], description string) GlobalBoolConstrainedDefaultSetting
type GlobalBoolSetting ¶
added in v1.25.0
type GlobalBoolSetting = GlobalTypedSetting[bool]
func NewGlobalBoolSetting ¶
added in v1.25.0
func NewGlobalBoolSetting(key string, def bool, description string) GlobalBoolSetting
type GlobalDurationConstrainedDefaultSetting ¶
added in v1.29.0
type GlobalDurationConstrainedDefaultSetting = GlobalTypedConstrainedDefaultSetting[time.Duration]
func NewGlobalDurationSettingWithConstrainedDefault ¶
added in v1.25.0
func NewGlobalDurationSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[time.Duration], description string) GlobalDurationConstrainedDefaultSetting
type GlobalDurationSetting ¶
added in v1.25.0
type GlobalDurationSetting = GlobalTypedSetting[time.Duration]
func NewGlobalDurationSetting ¶
added in v1.25.0
func NewGlobalDurationSetting(key string, def time.Duration, description string) GlobalDurationSetting
type GlobalFloatConstrainedDefaultSetting ¶
added in v1.29.0
type GlobalFloatConstrainedDefaultSetting = GlobalTypedConstrainedDefaultSetting[float64]
func NewGlobalFloatSettingWithConstrainedDefault ¶
added in v1.25.0
func NewGlobalFloatSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[float64], description string) GlobalFloatConstrainedDefaultSetting
type GlobalFloatSetting ¶
added in v1.25.0
type GlobalFloatSetting = GlobalTypedSetting[float64]
func NewGlobalFloatSetting ¶
added in v1.25.0
func NewGlobalFloatSetting(key string, def float64, description string) GlobalFloatSetting
type GlobalIntConstrainedDefaultSetting ¶
added in v1.29.0
type GlobalIntConstrainedDefaultSetting = GlobalTypedConstrainedDefaultSetting[int]
func NewGlobalIntSettingWithConstrainedDefault ¶
added in v1.25.0
func NewGlobalIntSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[int], description string) GlobalIntConstrainedDefaultSetting
type GlobalIntSetting ¶
added in v1.25.0
type GlobalIntSetting = GlobalTypedSetting[int]
func NewGlobalIntSetting ¶
added in v1.25.0
func NewGlobalIntSetting(key string, def int, description string) GlobalIntSetting
type GlobalMapConstrainedDefaultSetting ¶
added in v1.29.0
type GlobalMapConstrainedDefaultSetting = GlobalTypedConstrainedDefaultSetting[map[string]any]
func NewGlobalMapSettingWithConstrainedDefault ¶
added in v1.25.0
func NewGlobalMapSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[map[string]any], description string) GlobalMapConstrainedDefaultSetting
type GlobalMapSetting ¶
added in v1.25.0
type GlobalMapSetting = GlobalTypedSetting[map[string]any]
func NewGlobalMapSetting ¶
added in v1.25.0
func NewGlobalMapSetting(key string, def map[string]any, description string) GlobalMapSetting
type GlobalStringConstrainedDefaultSetting ¶
added in v1.29.0
type GlobalStringConstrainedDefaultSetting = GlobalTypedConstrainedDefaultSetting[string]
func NewGlobalStringSettingWithConstrainedDefault ¶
added in v1.25.0
func NewGlobalStringSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[string], description string) GlobalStringConstrainedDefaultSetting
type GlobalStringSetting ¶
added in v1.25.0
type GlobalStringSetting = GlobalTypedSetting[string]
func NewGlobalStringSetting ¶
added in v1.25.0
func NewGlobalStringSetting(key string, def string, description string) GlobalStringSetting
type GlobalTypedConstrainedDefaultSetting ¶
added in v1.29.0
type GlobalTypedConstrainedDefaultSetting[T any] constrainedDefaultSetting[T, func()]
func NewGlobalTypedSettingWithConstrainedDefault ¶
added in v1.25.0
func NewGlobalTypedSettingWithConstrainedDefault[T any](key string, convert func(any) (T, error), cdef []TypedConstrainedValue[T], description string) GlobalTypedConstrainedDefaultSetting[T]

NewGlobalTypedSettingWithConstrainedDefault creates a setting with a compound default value.

func (GlobalTypedConstrainedDefaultSetting[T]) Get ¶
added in v1.29.0
func (s GlobalTypedConstrainedDefaultSetting[T]) Get(c *Collection) TypedPropertyFn[T]
func (GlobalTypedConstrainedDefaultSetting[T]) Key ¶
added in v1.29.0
func (s GlobalTypedConstrainedDefaultSetting[T]) Key() Key
func (GlobalTypedConstrainedDefaultSetting[T]) Precedence ¶
added in v1.29.0
func (s GlobalTypedConstrainedDefaultSetting[T]) Precedence() Precedence
func (GlobalTypedConstrainedDefaultSetting[T]) Subscribe ¶
added in v1.29.0
func (s GlobalTypedConstrainedDefaultSetting[T]) Subscribe(c *Collection) TypedSubscribable[T]
func (GlobalTypedConstrainedDefaultSetting[T]) Validate ¶
added in v1.29.0
func (s GlobalTypedConstrainedDefaultSetting[T]) Validate(v any) error
type GlobalTypedSetting ¶
added in v1.25.0
type GlobalTypedSetting[T any] setting[T, func()]
func NewGlobalTypedSetting ¶
added in v1.25.0
func NewGlobalTypedSetting[T any](key string, def T, description string) GlobalTypedSetting[T]

NewGlobalTypedSetting creates a setting that uses mapstructure to handle complex structured values. The value from dynamic config will be _merged_ over a deep copy of 'def'. Be very careful when using non-empty maps or slices as defaults, the result may not be what you want.

func NewGlobalTypedSettingWithConverter ¶
added in v1.25.0
func NewGlobalTypedSettingWithConverter[T any](key string, convert func(any) (T, error), def T, description string) GlobalTypedSetting[T]

NewGlobalTypedSettingWithConverter creates a setting with a custom converter function.

func (GlobalTypedSetting[T]) Get ¶
added in v1.25.0
func (s GlobalTypedSetting[T]) Get(c *Collection) TypedPropertyFn[T]
func (GlobalTypedSetting[T]) Key ¶
added in v1.25.0
func (s GlobalTypedSetting[T]) Key() Key
func (GlobalTypedSetting[T]) Precedence ¶
added in v1.25.0
func (s GlobalTypedSetting[T]) Precedence() Precedence
func (GlobalTypedSetting[T]) Subscribe ¶
added in v1.25.0
func (s GlobalTypedSetting[T]) Subscribe(c *Collection) TypedSubscribable[T]
func (GlobalTypedSetting[T]) Validate ¶
added in v1.25.0
func (s GlobalTypedSetting[T]) Validate(v any) error
func (GlobalTypedSetting[T]) WithDefault ¶
added in v1.25.0
func (s GlobalTypedSetting[T]) WithDefault(v T) GlobalTypedSetting[T]
type GradualChange ¶
added in v1.30.0
type GradualChange[T any] struct {
	Old, New   T
	Start, End time.Time
}

GradualChange represents a setting that can change its value over time in a controlled way. The value of a GradualChange is a function of a key and the current time. Before Start, the value is always Old for all keys, and after End it's always New. Between them, each key will change once at a specific time (returned by When).

A setting with type GradualChange can use ConvertGradualChange as a conversion function to handle plain values of the underlying type as well as GradualChange structs.

func StaticGradualChange ¶
added in v1.30.0
func StaticGradualChange[T any](def T) GradualChange[T]

StaticGradualChange returns a GradualChange whose Value always returns def and whose When always returns a time in the past.

func (*GradualChange[T]) Value ¶
added in v1.30.0
func (c *GradualChange[T]) Value(key []byte, now time.Time) T

Value returns the value for the given key at the given time.

func (*GradualChange[T]) When ¶
added in v1.30.0
func (c *GradualChange[T]) When(key []byte) time.Time

When returns the time when the value for key will switch from old to new. It may be the zero time for a static GradualChange.

type IntPropertyFn ¶
type IntPropertyFn = TypedPropertyFn[int]
func GetIntPropertyFn ¶
func GetIntPropertyFn(value int) IntPropertyFn
type IntPropertyFnWithDestinationFilter ¶
added in v1.24.0
type IntPropertyFnWithDestinationFilter = TypedPropertyFnWithDestinationFilter[int]
func GetIntPropertyFnFilteredByDestination ¶
added in v1.25.0
func GetIntPropertyFnFilteredByDestination(value int) IntPropertyFnWithDestinationFilter
type IntPropertyFnWithNamespaceFilter ¶
type IntPropertyFnWithNamespaceFilter = TypedPropertyFnWithNamespaceFilter[int]
func GetIntPropertyFnFilteredByNamespace ¶
added in v1.24.0
func GetIntPropertyFnFilteredByNamespace(value int) IntPropertyFnWithNamespaceFilter
type IntPropertyFnWithNamespaceIDFilter ¶
added in v1.25.0
type IntPropertyFnWithNamespaceIDFilter = TypedPropertyFnWithNamespaceIDFilter[int]
func GetIntPropertyFnFilteredByNamespaceID ¶
added in v1.25.0
func GetIntPropertyFnFilteredByNamespaceID(value int) IntPropertyFnWithNamespaceIDFilter
type IntPropertyFnWithShardIDFilter ¶
type IntPropertyFnWithShardIDFilter = TypedPropertyFnWithShardIDFilter[int]
func GetIntPropertyFnFilteredByShardID ¶
added in v1.25.0
func GetIntPropertyFnFilteredByShardID(value int) IntPropertyFnWithShardIDFilter
type IntPropertyFnWithTaskQueueFilter ¶
added in v1.24.0
type IntPropertyFnWithTaskQueueFilter = TypedPropertyFnWithTaskQueueFilter[int]
func GetIntPropertyFnFilteredByTaskQueue ¶
added in v1.24.0
func GetIntPropertyFnFilteredByTaskQueue(value int) IntPropertyFnWithTaskQueueFilter
type IntPropertyFnWithTaskTypeFilter ¶
added in v1.25.0
type IntPropertyFnWithTaskTypeFilter = TypedPropertyFnWithTaskTypeFilter[int]
func GetIntPropertyFnFilteredByTaskType ¶
added in v1.25.0
func GetIntPropertyFnFilteredByTaskType(value int) IntPropertyFnWithTaskTypeFilter
type Key ¶
type Key struct {
	// contains filtered or unexported fields
}

Key is a key/property stored in dynamic config.

func MakeKey ¶
added in v1.30.0
func MakeKey(s string) Key
func (Key) String ¶
func (k Key) String() string
type MapPropertyFn ¶
type MapPropertyFn = TypedPropertyFn[map[string]any]
func GetMapPropertyFn ¶
func GetMapPropertyFn(value map[string]any) MapPropertyFn
type MapPropertyFnWithDestinationFilter ¶
added in v1.24.0
type MapPropertyFnWithDestinationFilter = TypedPropertyFnWithDestinationFilter[map[string]any]
func GetMapPropertyFnFilteredByDestination ¶
added in v1.25.0
func GetMapPropertyFnFilteredByDestination(value map[string]any) MapPropertyFnWithDestinationFilter
type MapPropertyFnWithNamespaceFilter ¶
type MapPropertyFnWithNamespaceFilter = TypedPropertyFnWithNamespaceFilter[map[string]any]
func GetMapPropertyFnFilteredByNamespace ¶
added in v1.24.0
func GetMapPropertyFnFilteredByNamespace(value map[string]any) MapPropertyFnWithNamespaceFilter
type MapPropertyFnWithNamespaceIDFilter ¶
added in v1.25.0
type MapPropertyFnWithNamespaceIDFilter = TypedPropertyFnWithNamespaceIDFilter[map[string]any]
func GetMapPropertyFnFilteredByNamespaceID ¶
added in v1.25.0
func GetMapPropertyFnFilteredByNamespaceID(value map[string]any) MapPropertyFnWithNamespaceIDFilter
type MapPropertyFnWithShardIDFilter ¶
added in v1.25.0
type MapPropertyFnWithShardIDFilter = TypedPropertyFnWithShardIDFilter[map[string]any]
func GetMapPropertyFnFilteredByShardID ¶
added in v1.25.0
func GetMapPropertyFnFilteredByShardID(value map[string]any) MapPropertyFnWithShardIDFilter
type MapPropertyFnWithTaskQueueFilter ¶
added in v1.25.0
type MapPropertyFnWithTaskQueueFilter = TypedPropertyFnWithTaskQueueFilter[map[string]any]
func GetMapPropertyFnFilteredByTaskQueue ¶
added in v1.25.0
func GetMapPropertyFnFilteredByTaskQueue(value map[string]any) MapPropertyFnWithTaskQueueFilter
type MapPropertyFnWithTaskTypeFilter ¶
added in v1.25.0
type MapPropertyFnWithTaskTypeFilter = TypedPropertyFnWithTaskTypeFilter[map[string]any]
func GetMapPropertyFnFilteredByTaskType ¶
added in v1.25.0
func GetMapPropertyFnFilteredByTaskType(value map[string]any) MapPropertyFnWithTaskTypeFilter
type MemoryClient ¶
added in v1.25.0
type MemoryClient struct {
	NotifyingClientImpl
	// contains filtered or unexported fields
}
func NewMemoryClient ¶
added in v1.25.0
func NewMemoryClient() *MemoryClient

NewMemoryClient - returns a memory based dynamic config client

func (*MemoryClient) GetValue ¶
added in v1.25.0
func (d *MemoryClient) GetValue(key Key) []ConstrainedValue
func (*MemoryClient) OverrideSetting ¶
added in v1.26.2
func (d *MemoryClient) OverrideSetting(setting GenericSetting, value any) (cleanup func())
func (*MemoryClient) OverrideValue ¶
added in v1.25.0
func (d *MemoryClient) OverrideValue(key Key, value any) (cleanup func())
type MockFileReader ¶
added in v1.25.0
type MockFileReader struct {
	// contains filtered or unexported fields
}

MockFileReader is a mock of FileReader interface.

func NewMockFileReader ¶
added in v1.25.0
func NewMockFileReader(ctrl *gomock.Controller) *MockFileReader

NewMockFileReader creates a new mock instance.

func (*MockFileReader) EXPECT ¶
added in v1.25.0
func (m *MockFileReader) EXPECT() *MockFileReaderMockRecorder

EXPECT returns an object that allows the caller to indicate expected use.

func (*MockFileReader) GetModTime ¶
added in v1.25.0
func (m *MockFileReader) GetModTime() (time.Time, error)

GetModTime mocks base method.

func (*MockFileReader) ReadFile ¶
added in v1.25.0
func (m *MockFileReader) ReadFile() ([]byte, error)

ReadFile mocks base method.

type MockFileReaderMockRecorder ¶
added in v1.25.0
type MockFileReaderMockRecorder struct {
	// contains filtered or unexported fields
}

MockFileReaderMockRecorder is the mock recorder for MockFileReader.

func (*MockFileReaderMockRecorder) GetModTime ¶
added in v1.25.0
func (mr *MockFileReaderMockRecorder) GetModTime() *gomock.Call

GetModTime indicates an expected call of GetModTime.

func (*MockFileReaderMockRecorder) ReadFile ¶
added in v1.25.0
func (mr *MockFileReaderMockRecorder) ReadFile() *gomock.Call

ReadFile indicates an expected call of ReadFile.

type NamespaceBoolConstrainedDefaultSetting ¶
added in v1.29.0
type NamespaceBoolConstrainedDefaultSetting = NamespaceTypedConstrainedDefaultSetting[bool]
func NewNamespaceBoolSettingWithConstrainedDefault ¶
added in v1.25.0
func NewNamespaceBoolSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[bool], description string) NamespaceBoolConstrainedDefaultSetting
type NamespaceBoolSetting ¶
added in v1.25.0
type NamespaceBoolSetting = NamespaceTypedSetting[bool]
func NewNamespaceBoolSetting ¶
added in v1.25.0
func NewNamespaceBoolSetting(key string, def bool, description string) NamespaceBoolSetting
type NamespaceDurationConstrainedDefaultSetting ¶
added in v1.29.0
type NamespaceDurationConstrainedDefaultSetting = NamespaceTypedConstrainedDefaultSetting[time.Duration]
func NewNamespaceDurationSettingWithConstrainedDefault ¶
added in v1.25.0
func NewNamespaceDurationSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[time.Duration], description string) NamespaceDurationConstrainedDefaultSetting
type NamespaceDurationSetting ¶
added in v1.25.0
type NamespaceDurationSetting = NamespaceTypedSetting[time.Duration]
func NewNamespaceDurationSetting ¶
added in v1.25.0
func NewNamespaceDurationSetting(key string, def time.Duration, description string) NamespaceDurationSetting
type NamespaceFloatConstrainedDefaultSetting ¶
added in v1.29.0
type NamespaceFloatConstrainedDefaultSetting = NamespaceTypedConstrainedDefaultSetting[float64]
func NewNamespaceFloatSettingWithConstrainedDefault ¶
added in v1.25.0
func NewNamespaceFloatSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[float64], description string) NamespaceFloatConstrainedDefaultSetting
type NamespaceFloatSetting ¶
added in v1.25.0
type NamespaceFloatSetting = NamespaceTypedSetting[float64]
func NewNamespaceFloatSetting ¶
added in v1.25.0
func NewNamespaceFloatSetting(key string, def float64, description string) NamespaceFloatSetting
type NamespaceIDBoolConstrainedDefaultSetting ¶
added in v1.29.0
type NamespaceIDBoolConstrainedDefaultSetting = NamespaceIDTypedConstrainedDefaultSetting[bool]
func NewNamespaceIDBoolSettingWithConstrainedDefault ¶
added in v1.25.0
func NewNamespaceIDBoolSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[bool], description string) NamespaceIDBoolConstrainedDefaultSetting
type NamespaceIDBoolSetting ¶
added in v1.25.0
type NamespaceIDBoolSetting = NamespaceIDTypedSetting[bool]
func NewNamespaceIDBoolSetting ¶
added in v1.25.0
func NewNamespaceIDBoolSetting(key string, def bool, description string) NamespaceIDBoolSetting
type NamespaceIDDurationConstrainedDefaultSetting ¶
added in v1.29.0
type NamespaceIDDurationConstrainedDefaultSetting = NamespaceIDTypedConstrainedDefaultSetting[time.Duration]
func NewNamespaceIDDurationSettingWithConstrainedDefault ¶
added in v1.25.0
func NewNamespaceIDDurationSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[time.Duration], description string) NamespaceIDDurationConstrainedDefaultSetting
type NamespaceIDDurationSetting ¶
added in v1.25.0
type NamespaceIDDurationSetting = NamespaceIDTypedSetting[time.Duration]
func NewNamespaceIDDurationSetting ¶
added in v1.25.0
func NewNamespaceIDDurationSetting(key string, def time.Duration, description string) NamespaceIDDurationSetting
type NamespaceIDFloatConstrainedDefaultSetting ¶
added in v1.29.0
type NamespaceIDFloatConstrainedDefaultSetting = NamespaceIDTypedConstrainedDefaultSetting[float64]
func NewNamespaceIDFloatSettingWithConstrainedDefault ¶
added in v1.25.0
func NewNamespaceIDFloatSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[float64], description string) NamespaceIDFloatConstrainedDefaultSetting
type NamespaceIDFloatSetting ¶
added in v1.25.0
type NamespaceIDFloatSetting = NamespaceIDTypedSetting[float64]
func NewNamespaceIDFloatSetting ¶
added in v1.25.0
func NewNamespaceIDFloatSetting(key string, def float64, description string) NamespaceIDFloatSetting
type NamespaceIDIntConstrainedDefaultSetting ¶
added in v1.29.0
type NamespaceIDIntConstrainedDefaultSetting = NamespaceIDTypedConstrainedDefaultSetting[int]
func NewNamespaceIDIntSettingWithConstrainedDefault ¶
added in v1.25.0
func NewNamespaceIDIntSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[int], description string) NamespaceIDIntConstrainedDefaultSetting
type NamespaceIDIntSetting ¶
added in v1.25.0
type NamespaceIDIntSetting = NamespaceIDTypedSetting[int]
func NewNamespaceIDIntSetting ¶
added in v1.25.0
func NewNamespaceIDIntSetting(key string, def int, description string) NamespaceIDIntSetting
type NamespaceIDMapConstrainedDefaultSetting ¶
added in v1.29.0
type NamespaceIDMapConstrainedDefaultSetting = NamespaceIDTypedConstrainedDefaultSetting[map[string]any]
func NewNamespaceIDMapSettingWithConstrainedDefault ¶
added in v1.25.0
func NewNamespaceIDMapSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[map[string]any], description string) NamespaceIDMapConstrainedDefaultSetting
type NamespaceIDMapSetting ¶
added in v1.25.0
type NamespaceIDMapSetting = NamespaceIDTypedSetting[map[string]any]
func NewNamespaceIDMapSetting ¶
added in v1.25.0
func NewNamespaceIDMapSetting(key string, def map[string]any, description string) NamespaceIDMapSetting
type NamespaceIDStringConstrainedDefaultSetting ¶
added in v1.29.0
type NamespaceIDStringConstrainedDefaultSetting = NamespaceIDTypedConstrainedDefaultSetting[string]
func NewNamespaceIDStringSettingWithConstrainedDefault ¶
added in v1.25.0
func NewNamespaceIDStringSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[string], description string) NamespaceIDStringConstrainedDefaultSetting
type NamespaceIDStringSetting ¶
added in v1.25.0
type NamespaceIDStringSetting = NamespaceIDTypedSetting[string]
func NewNamespaceIDStringSetting ¶
added in v1.25.0
func NewNamespaceIDStringSetting(key string, def string, description string) NamespaceIDStringSetting
type NamespaceIDTypedConstrainedDefaultSetting ¶
added in v1.29.0
type NamespaceIDTypedConstrainedDefaultSetting[T any] constrainedDefaultSetting[T, func(namespaceID namespace.ID)]
func NewNamespaceIDTypedSettingWithConstrainedDefault ¶
added in v1.25.0
func NewNamespaceIDTypedSettingWithConstrainedDefault[T any](key string, convert func(any) (T, error), cdef []TypedConstrainedValue[T], description string) NamespaceIDTypedConstrainedDefaultSetting[T]

NewNamespaceIDTypedSettingWithConstrainedDefault creates a setting with a compound default value.

func (NamespaceIDTypedConstrainedDefaultSetting[T]) Get ¶
added in v1.29.0
func (s NamespaceIDTypedConstrainedDefaultSetting[T]) Get(c *Collection) TypedPropertyFnWithNamespaceIDFilter[T]
func (NamespaceIDTypedConstrainedDefaultSetting[T]) Key ¶
added in v1.29.0
func (s NamespaceIDTypedConstrainedDefaultSetting[T]) Key() Key
func (NamespaceIDTypedConstrainedDefaultSetting[T]) Precedence ¶
added in v1.29.0
func (s NamespaceIDTypedConstrainedDefaultSetting[T]) Precedence() Precedence
func (NamespaceIDTypedConstrainedDefaultSetting[T]) Subscribe ¶
added in v1.29.0
func (s NamespaceIDTypedConstrainedDefaultSetting[T]) Subscribe(c *Collection) TypedSubscribableWithNamespaceIDFilter[T]
func (NamespaceIDTypedConstrainedDefaultSetting[T]) Validate ¶
added in v1.29.0
func (s NamespaceIDTypedConstrainedDefaultSetting[T]) Validate(v any) error
type NamespaceIDTypedSetting ¶
added in v1.25.0
type NamespaceIDTypedSetting[T any] setting[T, func(namespaceID namespace.ID)]
func NewNamespaceIDTypedSetting ¶
added in v1.25.0
func NewNamespaceIDTypedSetting[T any](key string, def T, description string) NamespaceIDTypedSetting[T]

NewNamespaceIDTypedSetting creates a setting that uses mapstructure to handle complex structured values. The value from dynamic config will be _merged_ over a deep copy of 'def'. Be very careful when using non-empty maps or slices as defaults, the result may not be what you want.

func NewNamespaceIDTypedSettingWithConverter ¶
added in v1.25.0
func NewNamespaceIDTypedSettingWithConverter[T any](key string, convert func(any) (T, error), def T, description string) NamespaceIDTypedSetting[T]

NewNamespaceIDTypedSettingWithConverter creates a setting with a custom converter function.

func (NamespaceIDTypedSetting[T]) Get ¶
added in v1.25.0
func (s NamespaceIDTypedSetting[T]) Get(c *Collection) TypedPropertyFnWithNamespaceIDFilter[T]
func (NamespaceIDTypedSetting[T]) Key ¶
added in v1.25.0
func (s NamespaceIDTypedSetting[T]) Key() Key
func (NamespaceIDTypedSetting[T]) Precedence ¶
added in v1.25.0
func (s NamespaceIDTypedSetting[T]) Precedence() Precedence
func (NamespaceIDTypedSetting[T]) Subscribe ¶
added in v1.25.0
func (s NamespaceIDTypedSetting[T]) Subscribe(c *Collection) TypedSubscribableWithNamespaceIDFilter[T]
func (NamespaceIDTypedSetting[T]) Validate ¶
added in v1.25.0
func (s NamespaceIDTypedSetting[T]) Validate(v any) error
func (NamespaceIDTypedSetting[T]) WithDefault ¶
added in v1.25.0
func (s NamespaceIDTypedSetting[T]) WithDefault(v T) NamespaceIDTypedSetting[T]
type NamespaceIntConstrainedDefaultSetting ¶
added in v1.29.0
type NamespaceIntConstrainedDefaultSetting = NamespaceTypedConstrainedDefaultSetting[int]
func NewNamespaceIntSettingWithConstrainedDefault ¶
added in v1.25.0
func NewNamespaceIntSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[int], description string) NamespaceIntConstrainedDefaultSetting
type NamespaceIntSetting ¶
added in v1.25.0
type NamespaceIntSetting = NamespaceTypedSetting[int]
func NewNamespaceIntSetting ¶
added in v1.25.0
func NewNamespaceIntSetting(key string, def int, description string) NamespaceIntSetting
type NamespaceMapConstrainedDefaultSetting ¶
added in v1.29.0
type NamespaceMapConstrainedDefaultSetting = NamespaceTypedConstrainedDefaultSetting[map[string]any]
func NewNamespaceMapSettingWithConstrainedDefault ¶
added in v1.25.0
func NewNamespaceMapSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[map[string]any], description string) NamespaceMapConstrainedDefaultSetting
type NamespaceMapSetting ¶
added in v1.25.0
type NamespaceMapSetting = NamespaceTypedSetting[map[string]any]
func NewNamespaceMapSetting ¶
added in v1.25.0
func NewNamespaceMapSetting(key string, def map[string]any, description string) NamespaceMapSetting
type NamespaceStringConstrainedDefaultSetting ¶
added in v1.29.0
type NamespaceStringConstrainedDefaultSetting = NamespaceTypedConstrainedDefaultSetting[string]
func NewNamespaceStringSettingWithConstrainedDefault ¶
added in v1.25.0
func NewNamespaceStringSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[string], description string) NamespaceStringConstrainedDefaultSetting
type NamespaceStringSetting ¶
added in v1.25.0
type NamespaceStringSetting = NamespaceTypedSetting[string]
func NewNamespaceStringSetting ¶
added in v1.25.0
func NewNamespaceStringSetting(key string, def string, description string) NamespaceStringSetting
type NamespaceTypedConstrainedDefaultSetting ¶
added in v1.29.0
type NamespaceTypedConstrainedDefaultSetting[T any] constrainedDefaultSetting[T, func(namespace string)]
func NewNamespaceTypedSettingWithConstrainedDefault ¶
added in v1.25.0
func NewNamespaceTypedSettingWithConstrainedDefault[T any](key string, convert func(any) (T, error), cdef []TypedConstrainedValue[T], description string) NamespaceTypedConstrainedDefaultSetting[T]

NewNamespaceTypedSettingWithConstrainedDefault creates a setting with a compound default value.

func (NamespaceTypedConstrainedDefaultSetting[T]) Get ¶
added in v1.29.0
func (s NamespaceTypedConstrainedDefaultSetting[T]) Get(c *Collection) TypedPropertyFnWithNamespaceFilter[T]
func (NamespaceTypedConstrainedDefaultSetting[T]) Key ¶
added in v1.29.0
func (s NamespaceTypedConstrainedDefaultSetting[T]) Key() Key
func (NamespaceTypedConstrainedDefaultSetting[T]) Precedence ¶
added in v1.29.0
func (s NamespaceTypedConstrainedDefaultSetting[T]) Precedence() Precedence
func (NamespaceTypedConstrainedDefaultSetting[T]) Subscribe ¶
added in v1.29.0
func (s NamespaceTypedConstrainedDefaultSetting[T]) Subscribe(c *Collection) TypedSubscribableWithNamespaceFilter[T]
func (NamespaceTypedConstrainedDefaultSetting[T]) Validate ¶
added in v1.29.0
func (s NamespaceTypedConstrainedDefaultSetting[T]) Validate(v any) error
type NamespaceTypedSetting ¶
added in v1.25.0
type NamespaceTypedSetting[T any] setting[T, func(namespace string)]
func NewNamespaceTypedSetting ¶
added in v1.25.0
func NewNamespaceTypedSetting[T any](key string, def T, description string) NamespaceTypedSetting[T]

NewNamespaceTypedSetting creates a setting that uses mapstructure to handle complex structured values. The value from dynamic config will be _merged_ over a deep copy of 'def'. Be very careful when using non-empty maps or slices as defaults, the result may not be what you want.

func NewNamespaceTypedSettingWithConverter ¶
added in v1.25.0
func NewNamespaceTypedSettingWithConverter[T any](key string, convert func(any) (T, error), def T, description string) NamespaceTypedSetting[T]

NewNamespaceTypedSettingWithConverter creates a setting with a custom converter function.

func (NamespaceTypedSetting[T]) Get ¶
added in v1.25.0
func (s NamespaceTypedSetting[T]) Get(c *Collection) TypedPropertyFnWithNamespaceFilter[T]
func (NamespaceTypedSetting[T]) Key ¶
added in v1.25.0
func (s NamespaceTypedSetting[T]) Key() Key
func (NamespaceTypedSetting[T]) Precedence ¶
added in v1.25.0
func (s NamespaceTypedSetting[T]) Precedence() Precedence
func (NamespaceTypedSetting[T]) Subscribe ¶
added in v1.25.0
func (s NamespaceTypedSetting[T]) Subscribe(c *Collection) TypedSubscribableWithNamespaceFilter[T]
func (NamespaceTypedSetting[T]) Validate ¶
added in v1.25.0
func (s NamespaceTypedSetting[T]) Validate(v any) error
func (NamespaceTypedSetting[T]) WithDefault ¶
added in v1.25.0
func (s NamespaceTypedSetting[T]) WithDefault(v T) NamespaceTypedSetting[T]
type NotifyingClient ¶
added in v1.25.0
type NotifyingClient interface {
	// Adds a subscription to all updates from this Client. `update` will be called on any
	// change to the current value set. The caller should call `cancel` to cancel the
	// subscription.
	Subscribe(update ClientUpdateFunc) (cancel func())
}

NotifyingClient is an optional interface that a Client can also implement, that adds support for faster notifications of dynamic config changes.

type NotifyingClientImpl ¶
added in v1.30.0
type NotifyingClientImpl struct {
	// contains filtered or unexported fields
}

NotifyingClientImpl implements NotifyingClient and is intended to be embedded in another struct. NotifyingClientImpl must not be copied after first use.

func NewNotifyingClientImpl ¶
added in v1.30.0
func NewNotifyingClientImpl() NotifyingClientImpl
func (*NotifyingClientImpl) PublishUpdates ¶
added in v1.30.0
func (n *NotifyingClientImpl) PublishUpdates(changed map[Key][]ConstrainedValue)

PublishUpdates calls all subscribed update functions with the changed keys.

func (*NotifyingClientImpl) Subscribe ¶
added in v1.30.0
func (n *NotifyingClientImpl) Subscribe(f ClientUpdateFunc) (cancel func())

Subscribe adds a subscription to all updates from this Client.

type Precedence ¶
added in v1.25.0
type Precedence int

Precedence is an enum for the search order precedence of a dynamic config setting. E.g., use the global value, check namespace then global, check task queue then namespace then global, etc.

const (
	PrecedenceUnknown Precedence = iota
	PrecedenceGlobal
	PrecedenceNamespace
	PrecedenceNamespaceID
	PrecedenceTaskQueue
	PrecedenceShardID
	PrecedenceTaskType
	PrecedenceDestination
)
type ShardIDBoolConstrainedDefaultSetting ¶
added in v1.29.0
type ShardIDBoolConstrainedDefaultSetting = ShardIDTypedConstrainedDefaultSetting[bool]
func NewShardIDBoolSettingWithConstrainedDefault ¶
added in v1.25.0
func NewShardIDBoolSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[bool], description string) ShardIDBoolConstrainedDefaultSetting
type ShardIDBoolSetting ¶
added in v1.25.0
type ShardIDBoolSetting = ShardIDTypedSetting[bool]
func NewShardIDBoolSetting ¶
added in v1.25.0
func NewShardIDBoolSetting(key string, def bool, description string) ShardIDBoolSetting
type ShardIDDurationConstrainedDefaultSetting ¶
added in v1.29.0
type ShardIDDurationConstrainedDefaultSetting = ShardIDTypedConstrainedDefaultSetting[time.Duration]
func NewShardIDDurationSettingWithConstrainedDefault ¶
added in v1.25.0
func NewShardIDDurationSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[time.Duration], description string) ShardIDDurationConstrainedDefaultSetting
type ShardIDDurationSetting ¶
added in v1.25.0
type ShardIDDurationSetting = ShardIDTypedSetting[time.Duration]
func NewShardIDDurationSetting ¶
added in v1.25.0
func NewShardIDDurationSetting(key string, def time.Duration, description string) ShardIDDurationSetting
type ShardIDFloatConstrainedDefaultSetting ¶
added in v1.29.0
type ShardIDFloatConstrainedDefaultSetting = ShardIDTypedConstrainedDefaultSetting[float64]
func NewShardIDFloatSettingWithConstrainedDefault ¶
added in v1.25.0
func NewShardIDFloatSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[float64], description string) ShardIDFloatConstrainedDefaultSetting
type ShardIDFloatSetting ¶
added in v1.25.0
type ShardIDFloatSetting = ShardIDTypedSetting[float64]
func NewShardIDFloatSetting ¶
added in v1.25.0
func NewShardIDFloatSetting(key string, def float64, description string) ShardIDFloatSetting
type ShardIDIntConstrainedDefaultSetting ¶
added in v1.29.0
type ShardIDIntConstrainedDefaultSetting = ShardIDTypedConstrainedDefaultSetting[int]
func NewShardIDIntSettingWithConstrainedDefault ¶
added in v1.25.0
func NewShardIDIntSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[int], description string) ShardIDIntConstrainedDefaultSetting
type ShardIDIntSetting ¶
added in v1.25.0
type ShardIDIntSetting = ShardIDTypedSetting[int]
func NewShardIDIntSetting ¶
added in v1.25.0
func NewShardIDIntSetting(key string, def int, description string) ShardIDIntSetting
type ShardIDMapConstrainedDefaultSetting ¶
added in v1.29.0
type ShardIDMapConstrainedDefaultSetting = ShardIDTypedConstrainedDefaultSetting[map[string]any]
func NewShardIDMapSettingWithConstrainedDefault ¶
added in v1.25.0
func NewShardIDMapSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[map[string]any], description string) ShardIDMapConstrainedDefaultSetting
type ShardIDMapSetting ¶
added in v1.25.0
type ShardIDMapSetting = ShardIDTypedSetting[map[string]any]
func NewShardIDMapSetting ¶
added in v1.25.0
func NewShardIDMapSetting(key string, def map[string]any, description string) ShardIDMapSetting
type ShardIDStringConstrainedDefaultSetting ¶
added in v1.29.0
type ShardIDStringConstrainedDefaultSetting = ShardIDTypedConstrainedDefaultSetting[string]
func NewShardIDStringSettingWithConstrainedDefault ¶
added in v1.25.0
func NewShardIDStringSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[string], description string) ShardIDStringConstrainedDefaultSetting
type ShardIDStringSetting ¶
added in v1.25.0
type ShardIDStringSetting = ShardIDTypedSetting[string]
func NewShardIDStringSetting ¶
added in v1.25.0
func NewShardIDStringSetting(key string, def string, description string) ShardIDStringSetting
type ShardIDTypedConstrainedDefaultSetting ¶
added in v1.29.0
type ShardIDTypedConstrainedDefaultSetting[T any] constrainedDefaultSetting[T, func(shardID int32)]
func NewShardIDTypedSettingWithConstrainedDefault ¶
added in v1.25.0
func NewShardIDTypedSettingWithConstrainedDefault[T any](key string, convert func(any) (T, error), cdef []TypedConstrainedValue[T], description string) ShardIDTypedConstrainedDefaultSetting[T]

NewShardIDTypedSettingWithConstrainedDefault creates a setting with a compound default value.

func (ShardIDTypedConstrainedDefaultSetting[T]) Get ¶
added in v1.29.0
func (s ShardIDTypedConstrainedDefaultSetting[T]) Get(c *Collection) TypedPropertyFnWithShardIDFilter[T]
func (ShardIDTypedConstrainedDefaultSetting[T]) Key ¶
added in v1.29.0
func (s ShardIDTypedConstrainedDefaultSetting[T]) Key() Key
func (ShardIDTypedConstrainedDefaultSetting[T]) Precedence ¶
added in v1.29.0
func (s ShardIDTypedConstrainedDefaultSetting[T]) Precedence() Precedence
func (ShardIDTypedConstrainedDefaultSetting[T]) Subscribe ¶
added in v1.29.0
func (s ShardIDTypedConstrainedDefaultSetting[T]) Subscribe(c *Collection) TypedSubscribableWithShardIDFilter[T]
func (ShardIDTypedConstrainedDefaultSetting[T]) Validate ¶
added in v1.29.0
func (s ShardIDTypedConstrainedDefaultSetting[T]) Validate(v any) error
type ShardIDTypedSetting ¶
added in v1.25.0
type ShardIDTypedSetting[T any] setting[T, func(shardID int32)]
func NewShardIDTypedSetting ¶
added in v1.25.0
func NewShardIDTypedSetting[T any](key string, def T, description string) ShardIDTypedSetting[T]

NewShardIDTypedSetting creates a setting that uses mapstructure to handle complex structured values. The value from dynamic config will be _merged_ over a deep copy of 'def'. Be very careful when using non-empty maps or slices as defaults, the result may not be what you want.

func NewShardIDTypedSettingWithConverter ¶
added in v1.25.0
func NewShardIDTypedSettingWithConverter[T any](key string, convert func(any) (T, error), def T, description string) ShardIDTypedSetting[T]

NewShardIDTypedSettingWithConverter creates a setting with a custom converter function.

func (ShardIDTypedSetting[T]) Get ¶
added in v1.25.0
func (s ShardIDTypedSetting[T]) Get(c *Collection) TypedPropertyFnWithShardIDFilter[T]
func (ShardIDTypedSetting[T]) Key ¶
added in v1.25.0
func (s ShardIDTypedSetting[T]) Key() Key
func (ShardIDTypedSetting[T]) Precedence ¶
added in v1.25.0
func (s ShardIDTypedSetting[T]) Precedence() Precedence
func (ShardIDTypedSetting[T]) Subscribe ¶
added in v1.25.0
func (s ShardIDTypedSetting[T]) Subscribe(c *Collection) TypedSubscribableWithShardIDFilter[T]
func (ShardIDTypedSetting[T]) Validate ¶
added in v1.25.0
func (s ShardIDTypedSetting[T]) Validate(v any) error
func (ShardIDTypedSetting[T]) WithDefault ¶
added in v1.25.0
func (s ShardIDTypedSetting[T]) WithDefault(v T) ShardIDTypedSetting[T]
type StaticClient ¶
added in v1.18.0
type StaticClient map[Key]any

StaticClient is a simple implementation of Client that just looks up in a map. Values can be either plain values or []ConstrainedValue for a constrained value. A StaticClient should never be mutated or you'll create race conditions!

func (StaticClient) GetValue ¶
added in v1.18.0
func (s StaticClient) GetValue(key Key) []ConstrainedValue
type StringPropertyFn ¶
type StringPropertyFn = TypedPropertyFn[string]
func GetStringPropertyFn ¶
func GetStringPropertyFn(value string) StringPropertyFn
type StringPropertyFnWithDestinationFilter ¶
added in v1.24.0
type StringPropertyFnWithDestinationFilter = TypedPropertyFnWithDestinationFilter[string]
func GetStringPropertyFnFilteredByDestination ¶
added in v1.25.0
func GetStringPropertyFnFilteredByDestination(value string) StringPropertyFnWithDestinationFilter
type StringPropertyFnWithNamespaceFilter ¶
type StringPropertyFnWithNamespaceFilter = TypedPropertyFnWithNamespaceFilter[string]
func GetStringPropertyFnFilteredByNamespace ¶
added in v1.25.0
func GetStringPropertyFnFilteredByNamespace(value string) StringPropertyFnWithNamespaceFilter
type StringPropertyFnWithNamespaceIDFilter ¶
added in v1.21.0
type StringPropertyFnWithNamespaceIDFilter = TypedPropertyFnWithNamespaceIDFilter[string]
func GetStringPropertyFnFilteredByNamespaceID ¶
added in v1.25.0
func GetStringPropertyFnFilteredByNamespaceID(value string) StringPropertyFnWithNamespaceIDFilter
type StringPropertyFnWithShardIDFilter ¶
added in v1.25.0
type StringPropertyFnWithShardIDFilter = TypedPropertyFnWithShardIDFilter[string]
func GetStringPropertyFnFilteredByShardID ¶
added in v1.25.0
func GetStringPropertyFnFilteredByShardID(value string) StringPropertyFnWithShardIDFilter
type StringPropertyFnWithTaskQueueFilter ¶
added in v1.25.0
type StringPropertyFnWithTaskQueueFilter = TypedPropertyFnWithTaskQueueFilter[string]
func GetStringPropertyFnFilteredByTaskQueue ¶
added in v1.25.0
func GetStringPropertyFnFilteredByTaskQueue(value string) StringPropertyFnWithTaskQueueFilter
type StringPropertyFnWithTaskTypeFilter ¶
added in v1.25.0
type StringPropertyFnWithTaskTypeFilter = TypedPropertyFnWithTaskTypeFilter[string]
func GetStringPropertyFnFilteredByTaskType ¶
added in v1.25.0
func GetStringPropertyFnFilteredByTaskType(value string) StringPropertyFnWithTaskTypeFilter
type TaskQueueBoolConstrainedDefaultSetting ¶
added in v1.29.0
type TaskQueueBoolConstrainedDefaultSetting = TaskQueueTypedConstrainedDefaultSetting[bool]
func NewTaskQueueBoolSettingWithConstrainedDefault ¶
added in v1.25.0
func NewTaskQueueBoolSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[bool], description string) TaskQueueBoolConstrainedDefaultSetting
type TaskQueueBoolSetting ¶
added in v1.25.0
type TaskQueueBoolSetting = TaskQueueTypedSetting[bool]
func NewTaskQueueBoolSetting ¶
added in v1.25.0
func NewTaskQueueBoolSetting(key string, def bool, description string) TaskQueueBoolSetting
type TaskQueueDurationConstrainedDefaultSetting ¶
added in v1.29.0
type TaskQueueDurationConstrainedDefaultSetting = TaskQueueTypedConstrainedDefaultSetting[time.Duration]
func NewTaskQueueDurationSettingWithConstrainedDefault ¶
added in v1.25.0
func NewTaskQueueDurationSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[time.Duration], description string) TaskQueueDurationConstrainedDefaultSetting
type TaskQueueDurationSetting ¶
added in v1.25.0
type TaskQueueDurationSetting = TaskQueueTypedSetting[time.Duration]
func NewTaskQueueDurationSetting ¶
added in v1.25.0
func NewTaskQueueDurationSetting(key string, def time.Duration, description string) TaskQueueDurationSetting
type TaskQueueFloatConstrainedDefaultSetting ¶
added in v1.29.0
type TaskQueueFloatConstrainedDefaultSetting = TaskQueueTypedConstrainedDefaultSetting[float64]
func NewTaskQueueFloatSettingWithConstrainedDefault ¶
added in v1.25.0
func NewTaskQueueFloatSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[float64], description string) TaskQueueFloatConstrainedDefaultSetting
type TaskQueueFloatSetting ¶
added in v1.25.0
type TaskQueueFloatSetting = TaskQueueTypedSetting[float64]
func NewTaskQueueFloatSetting ¶
added in v1.25.0
func NewTaskQueueFloatSetting(key string, def float64, description string) TaskQueueFloatSetting
type TaskQueueIntConstrainedDefaultSetting ¶
added in v1.29.0
type TaskQueueIntConstrainedDefaultSetting = TaskQueueTypedConstrainedDefaultSetting[int]
func NewTaskQueueIntSettingWithConstrainedDefault ¶
added in v1.25.0
func NewTaskQueueIntSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[int], description string) TaskQueueIntConstrainedDefaultSetting
type TaskQueueIntSetting ¶
added in v1.25.0
type TaskQueueIntSetting = TaskQueueTypedSetting[int]
func NewTaskQueueIntSetting ¶
added in v1.25.0
func NewTaskQueueIntSetting(key string, def int, description string) TaskQueueIntSetting
type TaskQueueMapConstrainedDefaultSetting ¶
added in v1.29.0
type TaskQueueMapConstrainedDefaultSetting = TaskQueueTypedConstrainedDefaultSetting[map[string]any]
func NewTaskQueueMapSettingWithConstrainedDefault ¶
added in v1.25.0
func NewTaskQueueMapSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[map[string]any], description string) TaskQueueMapConstrainedDefaultSetting
type TaskQueueMapSetting ¶
added in v1.25.0
type TaskQueueMapSetting = TaskQueueTypedSetting[map[string]any]
func NewTaskQueueMapSetting ¶
added in v1.25.0
func NewTaskQueueMapSetting(key string, def map[string]any, description string) TaskQueueMapSetting
type TaskQueueStringConstrainedDefaultSetting ¶
added in v1.29.0
type TaskQueueStringConstrainedDefaultSetting = TaskQueueTypedConstrainedDefaultSetting[string]
func NewTaskQueueStringSettingWithConstrainedDefault ¶
added in v1.25.0
func NewTaskQueueStringSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[string], description string) TaskQueueStringConstrainedDefaultSetting
type TaskQueueStringSetting ¶
added in v1.25.0
type TaskQueueStringSetting = TaskQueueTypedSetting[string]
func NewTaskQueueStringSetting ¶
added in v1.25.0
func NewTaskQueueStringSetting(key string, def string, description string) TaskQueueStringSetting
type TaskQueueTypedConstrainedDefaultSetting ¶
added in v1.29.0
type TaskQueueTypedConstrainedDefaultSetting[T any] constrainedDefaultSetting[T, func(namespace string, taskQueue string, taskQueueType enumspb.TaskQueueType)]
func NewTaskQueueTypedSettingWithConstrainedDefault ¶
added in v1.25.0
func NewTaskQueueTypedSettingWithConstrainedDefault[T any](key string, convert func(any) (T, error), cdef []TypedConstrainedValue[T], description string) TaskQueueTypedConstrainedDefaultSetting[T]

NewTaskQueueTypedSettingWithConstrainedDefault creates a setting with a compound default value.

func (TaskQueueTypedConstrainedDefaultSetting[T]) Get ¶
added in v1.29.0
func (s TaskQueueTypedConstrainedDefaultSetting[T]) Get(c *Collection) TypedPropertyFnWithTaskQueueFilter[T]
func (TaskQueueTypedConstrainedDefaultSetting[T]) Key ¶
added in v1.29.0
func (s TaskQueueTypedConstrainedDefaultSetting[T]) Key() Key
func (TaskQueueTypedConstrainedDefaultSetting[T]) Precedence ¶
added in v1.29.0
func (s TaskQueueTypedConstrainedDefaultSetting[T]) Precedence() Precedence
func (TaskQueueTypedConstrainedDefaultSetting[T]) Subscribe ¶
added in v1.29.0
func (s TaskQueueTypedConstrainedDefaultSetting[T]) Subscribe(c *Collection) TypedSubscribableWithTaskQueueFilter[T]
func (TaskQueueTypedConstrainedDefaultSetting[T]) Validate ¶
added in v1.29.0
func (s TaskQueueTypedConstrainedDefaultSetting[T]) Validate(v any) error
type TaskQueueTypedSetting ¶
added in v1.25.0
type TaskQueueTypedSetting[T any] setting[T, func(namespace string, taskQueue string, taskQueueType enumspb.TaskQueueType)]
func NewTaskQueueTypedSetting ¶
added in v1.25.0
func NewTaskQueueTypedSetting[T any](key string, def T, description string) TaskQueueTypedSetting[T]

NewTaskQueueTypedSetting creates a setting that uses mapstructure to handle complex structured values. The value from dynamic config will be _merged_ over a deep copy of 'def'. Be very careful when using non-empty maps or slices as defaults, the result may not be what you want.

func NewTaskQueueTypedSettingWithConverter ¶
added in v1.25.0
func NewTaskQueueTypedSettingWithConverter[T any](key string, convert func(any) (T, error), def T, description string) TaskQueueTypedSetting[T]

NewTaskQueueTypedSettingWithConverter creates a setting with a custom converter function.

func (TaskQueueTypedSetting[T]) Get ¶
added in v1.25.0
func (s TaskQueueTypedSetting[T]) Get(c *Collection) TypedPropertyFnWithTaskQueueFilter[T]
func (TaskQueueTypedSetting[T]) Key ¶
added in v1.25.0
func (s TaskQueueTypedSetting[T]) Key() Key
func (TaskQueueTypedSetting[T]) Precedence ¶
added in v1.25.0
func (s TaskQueueTypedSetting[T]) Precedence() Precedence
func (TaskQueueTypedSetting[T]) Subscribe ¶
added in v1.25.0
func (s TaskQueueTypedSetting[T]) Subscribe(c *Collection) TypedSubscribableWithTaskQueueFilter[T]
func (TaskQueueTypedSetting[T]) Validate ¶
added in v1.25.0
func (s TaskQueueTypedSetting[T]) Validate(v any) error
func (TaskQueueTypedSetting[T]) WithDefault ¶
added in v1.25.0
func (s TaskQueueTypedSetting[T]) WithDefault(v T) TaskQueueTypedSetting[T]
type TaskTypeBoolConstrainedDefaultSetting ¶
added in v1.29.0
type TaskTypeBoolConstrainedDefaultSetting = TaskTypeTypedConstrainedDefaultSetting[bool]
func NewTaskTypeBoolSettingWithConstrainedDefault ¶
added in v1.25.0
func NewTaskTypeBoolSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[bool], description string) TaskTypeBoolConstrainedDefaultSetting
type TaskTypeBoolSetting ¶
added in v1.25.0
type TaskTypeBoolSetting = TaskTypeTypedSetting[bool]
func NewTaskTypeBoolSetting ¶
added in v1.25.0
func NewTaskTypeBoolSetting(key string, def bool, description string) TaskTypeBoolSetting
type TaskTypeDurationConstrainedDefaultSetting ¶
added in v1.29.0
type TaskTypeDurationConstrainedDefaultSetting = TaskTypeTypedConstrainedDefaultSetting[time.Duration]
func NewTaskTypeDurationSettingWithConstrainedDefault ¶
added in v1.25.0
func NewTaskTypeDurationSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[time.Duration], description string) TaskTypeDurationConstrainedDefaultSetting
type TaskTypeDurationSetting ¶
added in v1.25.0
type TaskTypeDurationSetting = TaskTypeTypedSetting[time.Duration]
func NewTaskTypeDurationSetting ¶
added in v1.25.0
func NewTaskTypeDurationSetting(key string, def time.Duration, description string) TaskTypeDurationSetting
type TaskTypeFloatConstrainedDefaultSetting ¶
added in v1.29.0
type TaskTypeFloatConstrainedDefaultSetting = TaskTypeTypedConstrainedDefaultSetting[float64]
func NewTaskTypeFloatSettingWithConstrainedDefault ¶
added in v1.25.0
func NewTaskTypeFloatSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[float64], description string) TaskTypeFloatConstrainedDefaultSetting
type TaskTypeFloatSetting ¶
added in v1.25.0
type TaskTypeFloatSetting = TaskTypeTypedSetting[float64]
func NewTaskTypeFloatSetting ¶
added in v1.25.0
func NewTaskTypeFloatSetting(key string, def float64, description string) TaskTypeFloatSetting
type TaskTypeIntConstrainedDefaultSetting ¶
added in v1.29.0
type TaskTypeIntConstrainedDefaultSetting = TaskTypeTypedConstrainedDefaultSetting[int]
func NewTaskTypeIntSettingWithConstrainedDefault ¶
added in v1.25.0
func NewTaskTypeIntSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[int], description string) TaskTypeIntConstrainedDefaultSetting
type TaskTypeIntSetting ¶
added in v1.25.0
type TaskTypeIntSetting = TaskTypeTypedSetting[int]
func NewTaskTypeIntSetting ¶
added in v1.25.0
func NewTaskTypeIntSetting(key string, def int, description string) TaskTypeIntSetting
type TaskTypeMapConstrainedDefaultSetting ¶
added in v1.29.0
type TaskTypeMapConstrainedDefaultSetting = TaskTypeTypedConstrainedDefaultSetting[map[string]any]
func NewTaskTypeMapSettingWithConstrainedDefault ¶
added in v1.25.0
func NewTaskTypeMapSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[map[string]any], description string) TaskTypeMapConstrainedDefaultSetting
type TaskTypeMapSetting ¶
added in v1.25.0
type TaskTypeMapSetting = TaskTypeTypedSetting[map[string]any]
func NewTaskTypeMapSetting ¶
added in v1.25.0
func NewTaskTypeMapSetting(key string, def map[string]any, description string) TaskTypeMapSetting
type TaskTypeStringConstrainedDefaultSetting ¶
added in v1.29.0
type TaskTypeStringConstrainedDefaultSetting = TaskTypeTypedConstrainedDefaultSetting[string]
func NewTaskTypeStringSettingWithConstrainedDefault ¶
added in v1.25.0
func NewTaskTypeStringSettingWithConstrainedDefault(key string, cdef []TypedConstrainedValue[string], description string) TaskTypeStringConstrainedDefaultSetting
type TaskTypeStringSetting ¶
added in v1.25.0
type TaskTypeStringSetting = TaskTypeTypedSetting[string]
func NewTaskTypeStringSetting ¶
added in v1.25.0
func NewTaskTypeStringSetting(key string, def string, description string) TaskTypeStringSetting
type TaskTypeTypedConstrainedDefaultSetting ¶
added in v1.29.0
type TaskTypeTypedConstrainedDefaultSetting[T any] constrainedDefaultSetting[T, func(taskType enumsspb.TaskType)]
func NewTaskTypeTypedSettingWithConstrainedDefault ¶
added in v1.25.0
func NewTaskTypeTypedSettingWithConstrainedDefault[T any](key string, convert func(any) (T, error), cdef []TypedConstrainedValue[T], description string) TaskTypeTypedConstrainedDefaultSetting[T]

NewTaskTypeTypedSettingWithConstrainedDefault creates a setting with a compound default value.

func (TaskTypeTypedConstrainedDefaultSetting[T]) Get ¶
added in v1.29.0
func (s TaskTypeTypedConstrainedDefaultSetting[T]) Get(c *Collection) TypedPropertyFnWithTaskTypeFilter[T]
func (TaskTypeTypedConstrainedDefaultSetting[T]) Key ¶
added in v1.29.0
func (s TaskTypeTypedConstrainedDefaultSetting[T]) Key() Key
func (TaskTypeTypedConstrainedDefaultSetting[T]) Precedence ¶
added in v1.29.0
func (s TaskTypeTypedConstrainedDefaultSetting[T]) Precedence() Precedence
func (TaskTypeTypedConstrainedDefaultSetting[T]) Subscribe ¶
added in v1.29.0
func (s TaskTypeTypedConstrainedDefaultSetting[T]) Subscribe(c *Collection) TypedSubscribableWithTaskTypeFilter[T]
func (TaskTypeTypedConstrainedDefaultSetting[T]) Validate ¶
added in v1.29.0
func (s TaskTypeTypedConstrainedDefaultSetting[T]) Validate(v any) error
type TaskTypeTypedSetting ¶
added in v1.25.0
type TaskTypeTypedSetting[T any] setting[T, func(taskType enumsspb.TaskType)]
func NewTaskTypeTypedSetting ¶
added in v1.25.0
func NewTaskTypeTypedSetting[T any](key string, def T, description string) TaskTypeTypedSetting[T]

NewTaskTypeTypedSetting creates a setting that uses mapstructure to handle complex structured values. The value from dynamic config will be _merged_ over a deep copy of 'def'. Be very careful when using non-empty maps or slices as defaults, the result may not be what you want.

func NewTaskTypeTypedSettingWithConverter ¶
added in v1.25.0
func NewTaskTypeTypedSettingWithConverter[T any](key string, convert func(any) (T, error), def T, description string) TaskTypeTypedSetting[T]

NewTaskTypeTypedSettingWithConverter creates a setting with a custom converter function.

func (TaskTypeTypedSetting[T]) Get ¶
added in v1.25.0
func (s TaskTypeTypedSetting[T]) Get(c *Collection) TypedPropertyFnWithTaskTypeFilter[T]
func (TaskTypeTypedSetting[T]) Key ¶
added in v1.25.0
func (s TaskTypeTypedSetting[T]) Key() Key
func (TaskTypeTypedSetting[T]) Precedence ¶
added in v1.25.0
func (s TaskTypeTypedSetting[T]) Precedence() Precedence
func (TaskTypeTypedSetting[T]) Subscribe ¶
added in v1.25.0
func (s TaskTypeTypedSetting[T]) Subscribe(c *Collection) TypedSubscribableWithTaskTypeFilter[T]
func (TaskTypeTypedSetting[T]) Validate ¶
added in v1.25.0
func (s TaskTypeTypedSetting[T]) Validate(v any) error
func (TaskTypeTypedSetting[T]) WithDefault ¶
added in v1.25.0
func (s TaskTypeTypedSetting[T]) WithDefault(v T) TaskTypeTypedSetting[T]
type TypedConstrainedValue ¶
added in v1.25.0
type TypedConstrainedValue[T any] struct {
	Constraints Constraints
	Value       T
}
type TypedPropertyFn ¶
added in v1.25.0
type TypedPropertyFn[T any] func() T
func GetTypedPropertyFn ¶
added in v1.25.0
func GetTypedPropertyFn[T any](value T) TypedPropertyFn[T]
type TypedPropertyFnWithDestinationFilter ¶
added in v1.25.0
type TypedPropertyFnWithDestinationFilter[T any] func(namespace string, destination string) T
func GetTypedPropertyFnFilteredByDestination ¶
added in v1.25.0
func GetTypedPropertyFnFilteredByDestination[T any](value T) TypedPropertyFnWithDestinationFilter[T]
type TypedPropertyFnWithNamespaceFilter ¶
added in v1.25.0
type TypedPropertyFnWithNamespaceFilter[T any] func(namespace string) T
func GetTypedPropertyFnFilteredByNamespace ¶
added in v1.25.0
func GetTypedPropertyFnFilteredByNamespace[T any](value T) TypedPropertyFnWithNamespaceFilter[T]
type TypedPropertyFnWithNamespaceIDFilter ¶
added in v1.25.0
type TypedPropertyFnWithNamespaceIDFilter[T any] func(namespaceID namespace.ID) T
func GetTypedPropertyFnFilteredByNamespaceID ¶
added in v1.25.0
func GetTypedPropertyFnFilteredByNamespaceID[T any](value T) TypedPropertyFnWithNamespaceIDFilter[T]
type TypedPropertyFnWithShardIDFilter ¶
added in v1.25.0
type TypedPropertyFnWithShardIDFilter[T any] func(shardID int32) T
func GetTypedPropertyFnFilteredByShardID ¶
added in v1.25.0
func GetTypedPropertyFnFilteredByShardID[T any](value T) TypedPropertyFnWithShardIDFilter[T]
type TypedPropertyFnWithTaskQueueFilter ¶
added in v1.25.0
type TypedPropertyFnWithTaskQueueFilter[T any] func(namespace string, taskQueue string, taskQueueType enumspb.TaskQueueType) T
func GetTypedPropertyFnFilteredByTaskQueue ¶
added in v1.25.0
func GetTypedPropertyFnFilteredByTaskQueue[T any](value T) TypedPropertyFnWithTaskQueueFilter[T]
type TypedPropertyFnWithTaskTypeFilter ¶
added in v1.25.0
type TypedPropertyFnWithTaskTypeFilter[T any] func(taskType enumsspb.TaskType) T
func GetTypedPropertyFnFilteredByTaskType ¶
added in v1.25.0
func GetTypedPropertyFnFilteredByTaskType[T any](value T) TypedPropertyFnWithTaskTypeFilter[T]
type TypedSubscribable ¶
added in v1.25.0
type TypedSubscribable[T any] func(callback func(T)) (v T, cancel func())
type TypedSubscribableWithDestinationFilter ¶
added in v1.25.0
type TypedSubscribableWithDestinationFilter[T any] func(namespace string, destination string, callback func(T)) (v T, cancel func())
type TypedSubscribableWithNamespaceFilter ¶
added in v1.25.0
type TypedSubscribableWithNamespaceFilter[T any] func(namespace string, callback func(T)) (v T, cancel func())
type TypedSubscribableWithNamespaceIDFilter ¶
added in v1.25.0
type TypedSubscribableWithNamespaceIDFilter[T any] func(namespaceID namespace.ID, callback func(T)) (v T, cancel func())
type TypedSubscribableWithShardIDFilter ¶
added in v1.25.0
type TypedSubscribableWithShardIDFilter[T any] func(shardID int32, callback func(T)) (v T, cancel func())
type TypedSubscribableWithTaskQueueFilter ¶
added in v1.25.0
type TypedSubscribableWithTaskQueueFilter[T any] func(namespace string, taskQueue string, taskQueueType enumspb.TaskQueueType, callback func(T)) (v T, cancel func())
type TypedSubscribableWithTaskTypeFilter ¶
added in v1.25.0
type TypedSubscribableWithTaskTypeFilter[T any] func(taskType enumsspb.TaskType, callback func(T)) (v T, cancel func())
type YamlLoader ¶
added in v1.30.0
type YamlLoader struct {
	Map      ConfigValueMap
	Warnings []error
	Errors   []error
}

YamlLoader loads files and individual values from yaml files. Intended usage is to create a YamlLoader and call LoadFile or LoadValue. The parsed values will be placed in Map (initialized if nil). You can place your own map in Map before calling LoadFile/LoadValue if desired.

Any warnings or errors encountered during parsing will be added to Warnings or Errors. Warnings should be reported but not block using the new values. Errors should abort the loading process.

func LoadYamlFile ¶
added in v1.30.0
func LoadYamlFile(contents []byte) *YamlLoader

LoadYamlFile is a convenience function to create a YamlLoader and call LoadFile.

func (*YamlLoader) Err ¶
added in v1.30.0
func (lr *YamlLoader) Err() error

Err returns a joined error of lr.Errors.

func (*YamlLoader) LoadFile ¶
added in v1.30.0
func (lr *YamlLoader) LoadFile(contents []byte)

LoadFile parses and processes the given file contents into lr.Map (initialized if nil).

func (*YamlLoader) LoadValue ¶
added in v1.30.0
func (lr *YamlLoader) LoadValue(key Key, contents []byte)

LoadValue parses and processes the given single value into lr.Map (initialized if nil).

 Source Files ¶
View all Source files
client.go
client_diff.go
client_subscriptions.go
collection.go
constants.go
deepcopy.go
file_based_client.go
file_based_client_mock.go
fx.go
gradual_change.go
key.go
memory_client.go
registry.go
setting.go
setting_gen.go
shared_constants.go
shared_structure.go
static_client.go
util.go
yaml_loader.go
Why Go
Use Cases
Case Studies
Get Started
Playground
Tour
Stack Overflow
Help
Packages
Standard Library
Sub-repositories
About Go Packages
About
Download
Blog
Issue Tracker
Release Notes
Brand Guidelines
Code of Conduct
Connect
Twitter
GitHub
Slack
r/golang
Meetup
Golang Weekly
Copyright
Terms of Service
Privacy Policy
Report an Issue

Theme Toggle

Shortcuts Modal
