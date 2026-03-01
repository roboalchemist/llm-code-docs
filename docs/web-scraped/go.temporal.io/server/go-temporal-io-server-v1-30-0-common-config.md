# Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config

Title: config package - go.temporal.io/server/common/config - Go Packages

URL Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config

Markdown Content:
*   [Constants](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#pkg-constants)
*   [Variables](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#pkg-variables)
*   [func ListenIP() (net.IP, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#ListenIP)
*   [func WithConfigDir(configDir string) loadOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#WithConfigDir)
*   [func WithConfigFile(configFilePath string) loadOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#WithConfigFile)
*   [func WithEmbedded() loadOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#WithEmbedded)
*   [func WithEnv(env string) loadOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#WithEnv)
*   [func WithZone(zone string) loadOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#WithZone)
*   [type Archival](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Archival)
*       *   [func (a *Archival) Validate(namespaceDefaults *ArchivalNamespaceDefaults) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Archival.Validate)

*   [type ArchivalNamespaceDefaults](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#ArchivalNamespaceDefaults)
*   [type Authorization](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Authorization)
*   [type Cassandra](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Cassandra)
*   [type CassandraAddressTranslator](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#CassandraAddressTranslator)
*   [type CassandraConsistencySettings](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#CassandraConsistencySettings)
*   [type CassandraStoreConsistency](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#CassandraStoreConsistency)
*       *   [func (c *CassandraStoreConsistency) GetConsistency() gocql.Consistency](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#CassandraStoreConsistency.GetConsistency)
    *   [func (c *CassandraStoreConsistency) GetSerialConsistency() gocql.SerialConsistency](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#CassandraStoreConsistency.GetSerialConsistency)

*   [type CertExpirationValidation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#CertExpirationValidation)
*   [type ClientConnectionConfig](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#ClientConnectionConfig)
*       *   [func (c *ClientConnectionConfig) GetKeepAliveClientParameters() keepalive.ClientParameters](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#ClientConnectionConfig.GetKeepAliveClientParameters)

*   [type ClientTLS](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#ClientTLS)
*   [type Config](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Config)
*       *   [func Load(opts ...loadOption) (*Config, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Load)

*       *   [func (c *Config) String() string](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Config.String)
    *   [func (c *Config) Validate() error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Config.Validate)

*   [type CustomDatastoreConfig](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#CustomDatastoreConfig)
*   [type DCRedirectionPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#DCRedirectionPolicy)
*   [type DataStore](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#DataStore)
*       *   [func (ds *DataStore) GetIndexName() string](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#DataStore.GetIndexName)
    *   [func (ds *DataStore) Validate() error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#DataStore.Validate)

*   [type DataStoreName](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#DataStoreName)
*   [type FaultInjection](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#FaultInjection)
*       *   [func DefaultFaultInjection() *FaultInjection](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#DefaultFaultInjection)

*       *   [func (fi *FaultInjection) WithError(storeName DataStoreName, methodName, errorName string, probability float64) *FaultInjection](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#FaultInjection.WithError)
    *   [func (fi *FaultInjection) WithMethodSeed(storeName DataStoreName, methodName string, seed int64) *FaultInjection](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#FaultInjection.WithMethodSeed)

*   [type FaultInjectionDataStoreConfig](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#FaultInjectionDataStoreConfig)
*   [type FaultInjectionMethodConfig](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#FaultInjectionMethodConfig)
*   [type FaultInjectionTargets](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#FaultInjectionTargets)
*   [type FilestoreArchiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#FilestoreArchiver)
*   [type Global](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Global)
*   [type GroupTLS](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#GroupTLS)
*       *   [func (r *GroupTLS) IsClientEnabled() bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#GroupTLS.IsClientEnabled)
    *   [func (r *GroupTLS) IsServerEnabled() bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#GroupTLS.IsServerEnabled)

*   [type GstorageArchiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#GstorageArchiver)
*   [type HistoryArchival](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#HistoryArchival)
*   [type HistoryArchivalNamespaceDefaults](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#HistoryArchivalNamespaceDefaults)
*   [type HistoryArchiverProvider](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#HistoryArchiverProvider)
*   [type JWTKeyProvider](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#JWTKeyProvider)
*       *   [func (p *JWTKeyProvider) HasSourceURIsConfigured() bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#JWTKeyProvider.HasSourceURIsConfigured)

*   [type KeepAliveClientParameters](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#KeepAliveClientParameters)
*   [type KeepAliveServerConfig](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#KeepAliveServerConfig)
*       *   [func (k *KeepAliveServerConfig) GetKeepAliveEnforcementPolicy() keepalive.EnforcementPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#KeepAliveServerConfig.GetKeepAliveEnforcementPolicy)
    *   [func (k *KeepAliveServerConfig) GetKeepAliveServerParameters() keepalive.ServerParameters](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#KeepAliveServerConfig.GetKeepAliveServerParameters)

*   [type KeepAliveServerEnforcementPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#KeepAliveServerEnforcementPolicy)
*   [type KeepAliveServerParameters](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#KeepAliveServerParameters)
*   [type Membership](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Membership)
*   [type NamespaceDefaults](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#NamespaceDefaults)
*   [type PProf](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#PProf)
*   [type Persistence](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Persistence)
*       *   [func (c *Persistence) DefaultStoreType() string](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Persistence.DefaultStoreType)
    *   [func (c *Persistence) GetSecondaryVisibilityStoreConfig() DataStore](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Persistence.GetSecondaryVisibilityStoreConfig)
    *   [func (c *Persistence) GetVisibilityStoreConfig() DataStore](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Persistence.GetVisibilityStoreConfig)
    *   [func (c *Persistence) IsCustomVisibilityStore() bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Persistence.IsCustomVisibilityStore)
    *   [func (c *Persistence) IsSQLVisibilityStore() bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Persistence.IsSQLVisibilityStore)
    *   [func (c *Persistence) SecondaryVisibilityConfigExist() bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Persistence.SecondaryVisibilityConfigExist)
    *   [func (c *Persistence) Validate() error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Persistence.Validate)
    *   [func (c *Persistence) VisibilityConfigExist() bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Persistence.VisibilityConfigExist)

*   [type PublicClient](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#PublicClient)
*   [type RPC](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#RPC)
*   [type ReplicationTaskProcessorConfig](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#ReplicationTaskProcessorConfig)
*   [type Replicator](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Replicator)
*   [type RootTLS](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#RootTLS)
*   [type S3Archiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#S3Archiver)
*   [type SQL](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#SQL)
*   [type ServerTLS](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#ServerTLS)
*   [type Service](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Service)
*   [type ServicePortMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#ServicePortMap)
*   [type Visibility](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Visibility)
*   [type VisibilityArchival](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#VisibilityArchival)
*   [type VisibilityArchivalNamespaceDefaults](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#VisibilityArchivalNamespaceDefaults)
*   [type VisibilityArchiverProvider](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#VisibilityArchiverProvider)
*   [type WorkerTLS](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#WorkerTLS)

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/common/config/archival.go#L7)

const (
	ArchivalEnabled = "enabled"
	ArchivalDisabled = "disabled"
	ArchivalPaused = "paused"
)

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/common/config/config.go#L642)

const (
 ForceTLSConfigAuto = ""  ForceTLSConfigInternode = "internode"  ForceTLSConfigFrontend = "frontend" )

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/common/config/loader.go#L28)

const (
	EnvKeyRoot = "TEMPORAL_ROOT"
	EnvKeyConfigDir = "TEMPORAL_CONFIG_DIR"
	EnvKeyEnvironment = "TEMPORAL_ENVIRONMENT"
	EnvKeyAvailabilityZone = "TEMPORAL_AVAILABILITY_ZONE"
	
	
	EnvKeyAvailabilityZoneTypo = "TEMPORAL_AVAILABILTY_ZONE"
	EnvKeyAllowNoAuth = "TEMPORAL_ALLOW_NO_AUTH"
	EnvKeyConfigFile = "TEMPORAL_SERVER_CONFIG_FILE_PATH"
)

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/common/config/persistence.go#L13)

const (
	StoreTypeSQL = "sql"
	StoreTypeNoSQL = "nosql"
)

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/common/config/fx.go#L11)

var Module = [fx](https://pkg.go.dev/go.uber.org/fx).[Provide](https://pkg.go.dev/go.uber.org/fx#Provide)( 	provideRPCConfig,
	provideMembershipConfig,
	provideServicePortMap,
)

ListenIP returns the IP to bind to in Listen. It tries to find an IP that can be used by other machines to reach this machine.

func WithConfigDir(configDir [string](https://pkg.go.dev/builtin#string)) loadOption

WithConfigDir sets the directory path where configuration files are located. If empty, defaults to "config".

func WithConfigFile(configFilePath [string](https://pkg.go.dev/builtin#string)) loadOption

WithConfigFile sets a specific configuration file path to load. When provided, only this file will be loaded, bypassing the legacy hierarchical loading.

func WithEmbedded() loadOption

WithEmbedded forces the loader to use only the embedded configuration template. This loads configuration from environment variables only, using the embedded template.

func WithEnv(env [string](https://pkg.go.dev/builtin#string)) loadOption

WithEnv sets the environment name for configuration loading (e.g., "development", "production"). If empty, defaults to "development".

func WithZone(zone [string](https://pkg.go.dev/builtin#string)) loadOption

WithZone sets the availability zone for configuration loading. This is used to load zone-specific configuration overrides (e.g., "us-east-1a").

type Archival struct {
	History [HistoryArchival](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#HistoryArchival) `yaml:"history"`
	Visibility [VisibilityArchival](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#VisibilityArchival) `yaml:"visibility"`
}

Archival contains the config for archival

func (a *[Archival](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Archival)) Validate(namespaceDefaults *[ArchivalNamespaceDefaults](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#ArchivalNamespaceDefaults)) [error](https://pkg.go.dev/builtin#error)

Validate validates the archival config

type ArchivalNamespaceDefaults struct {
	History [HistoryArchivalNamespaceDefaults](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#HistoryArchivalNamespaceDefaults) `yaml:"history"`
	Visibility [VisibilityArchivalNamespaceDefaults](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#VisibilityArchivalNamespaceDefaults) `yaml:"visibility"`
}

ArchivalNamespaceDefaults is the default archival config for each namespace

type Authorization struct {
	
 JWTKeyProvider [JWTKeyProvider](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#JWTKeyProvider) `yaml:"jwtKeyProvider"`  PermissionsClaimName [string](https://pkg.go.dev/builtin#string) `yaml:"permissionsClaimName"` 	
	PermissionsRegex [string](https://pkg.go.dev/builtin#string) `yaml:"permissionsRegex"`
	Authorizer [string](https://pkg.go.dev/builtin#string) `yaml:"authorizer"`
	ClaimMapper [string](https://pkg.go.dev/builtin#string) `yaml:"claimMapper"`
	AuthHeaderName [string](https://pkg.go.dev/builtin#string) `yaml:"authHeaderName"`
	AuthExtraHeaderName [string](https://pkg.go.dev/builtin#string) `yaml:"authExtraHeaderName"`
	Audience [string](https://pkg.go.dev/builtin#string) `yaml:"audience"`
}

#### type [Cassandra](https://github.com/temporalio/temporal/blob/v1.30.0/common/config/config.go#L348)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Cassandra "Go to Cassandra")

type Cassandra struct {
	Hosts [string](https://pkg.go.dev/builtin#string) `yaml:"hosts" validate:"nonzero"`
	Port [int](https://pkg.go.dev/builtin#int) `yaml:"port"`
	User [string](https://pkg.go.dev/builtin#string) `yaml:"user"`
	Password [string](https://pkg.go.dev/builtin#string) `yaml:"password"`
	AllowedAuthenticators [][string](https://pkg.go.dev/builtin#string) `yaml:"allowedAuthenticators"`
	Keyspace [string](https://pkg.go.dev/builtin#string) `yaml:"keyspace" validate:"nonzero"`
	Datacenter [string](https://pkg.go.dev/builtin#string) `yaml:"datacenter"`
	MaxConns [int](https://pkg.go.dev/builtin#int) `yaml:"maxConns"`
	ConnectTimeout [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `yaml:"connectTimeout"`
	Timeout [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `yaml:"timeout"`
	WriteTimeout [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `yaml:"writeTimeout"`
	TLS *[auth](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/auth).[TLS](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/auth#TLS) `yaml:"tls"`
	Consistency *[CassandraStoreConsistency](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#CassandraStoreConsistency) `yaml:"consistency"`
	DisableInitialHostLookup [bool](https://pkg.go.dev/builtin#bool) `yaml:"disableInitialHostLookup"`
	AddressTranslator *[CassandraAddressTranslator](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#CassandraAddressTranslator) `yaml:"addressTranslator"`
}

Cassandra contains configuration to connect to Cassandra cluster

#### type [CassandraConsistencySettings](https://github.com/temporalio/temporal/blob/v1.30.0/common/config/config.go#L396)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#CassandraConsistencySettings "Go to CassandraConsistencySettings")

type CassandraConsistencySettings struct {
	Consistency [string](https://pkg.go.dev/builtin#string) `yaml:"consistency"`
	SerialConsistency [string](https://pkg.go.dev/builtin#string) `yaml:"serialConsistency"`
}

CassandraConsistencySettings sets the default consistency level for regular & serial queries to Cassandra.

#### type [CassandraStoreConsistency](https://github.com/temporalio/temporal/blob/v1.30.0/common/config/config.go#L382)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#CassandraStoreConsistency "Go to CassandraStoreConsistency")

type CassandraStoreConsistency struct {
	
	Default *[CassandraConsistencySettings](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#CassandraConsistencySettings) `yaml:"default"`
}

CassandraStoreConsistency enables you to set the consistency settings for each Cassandra Persistence Store for Temporal

#### func (*CassandraStoreConsistency) [GetConsistency](https://github.com/temporalio/temporal/blob/v1.30.0/common/config/persistence.go#L190)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#CassandraStoreConsistency.GetConsistency "Go to CassandraStoreConsistency.GetConsistency")

GetConsistency returns the gosql.Consistency setting from the configuration for the given store type

#### func (*CassandraStoreConsistency) [GetSerialConsistency](https://github.com/temporalio/temporal/blob/v1.30.0/common/config/persistence.go#L195)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#CassandraStoreConsistency.GetSerialConsistency "Go to CassandraStoreConsistency.GetSerialConsistency")

GetSerialConsistency returns the gosql.SerialConsistency setting from the configuration for the store

type CertExpirationValidation struct {
	WarningWindow [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `yaml:"warningWindow"`
	ErrorWindow [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `yaml:"errorWindow"`
	CheckInterval [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `yaml:"checkInterval"`
}

CertExpirationValidation contains settings for periodic checks of TLS certificate expiration

type ClientConnectionConfig struct {
 KeepAliveClientConfig *[KeepAliveClientParameters](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#KeepAliveClientParameters) `yaml:"keepAliveClientParameters"` }

type ClientTLS struct {
	
	
	ServerName [string](https://pkg.go.dev/builtin#string) `yaml:"serverName"`

	
	
	DisableHostVerification [bool](https://pkg.go.dev/builtin#bool) `yaml:"disableHostVerification"`

	
	RootCAFiles [][string](https://pkg.go.dev/builtin#string) `yaml:"rootCaFiles"`

	
	RootCAData [][string](https://pkg.go.dev/builtin#string) `yaml:"rootCaData"`

	
	ForceTLS [bool](https://pkg.go.dev/builtin#bool) `yaml:"forceTLS"`
}

ClientTLS contains TLS configuration for clients within the Temporal Cluster to connect to Temporal nodes.

type Config struct {
	Global [Global](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Global) `yaml:"global"`
	Persistence [Persistence](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Persistence) `yaml:"persistence"`
	Log [log](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/log).[Config](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/log#Config) `yaml:"log"`
	ClusterMetadata *[cluster](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster).[Config](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#Config) `yaml:"clusterMetadata"`
	DCRedirectionPolicy [DCRedirectionPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#DCRedirectionPolicy) `yaml:"dcRedirectionPolicy"`
	Services map[[string](https://pkg.go.dev/builtin#string)][Service](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Service) `yaml:"services"`
	Archival [Archival](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Archival) `yaml:"archival"`
	PublicClient [PublicClient](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#PublicClient) `yaml:"publicClient"`
	
	DynamicConfigClient *[dynamicconfig](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/dynamicconfig).[FileBasedClientConfig](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/dynamicconfig#FileBasedClientConfig) `yaml:"dynamicConfigClient"`
	NamespaceDefaults [NamespaceDefaults](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#NamespaceDefaults) `yaml:"namespaceDefaults"`
	ExporterConfig [telemetry](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/telemetry).[ExportConfig](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/telemetry#ExportConfig) `yaml:"otel"`
	Visibility [Visibility](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Visibility) `yaml:"visibility"`
}

Config contains the configuration for a set of temporal services

func Load(opts ...loadOption) (*[Config](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Config), [error](https://pkg.go.dev/builtin#error))

Load loads and validates the Temporal server configuration. It supports multiple loading strategies based on the provided options:

*   Embedded template with environment variables (WithEmbedded)
*   Single config file (WithConfigFile)
*   Legacy hierarchical config directory (WithConfigDir, WithEnv, WithZone)

Configuration files can be templated using Go template syntax with sprig-compatible functions. To enable templating, add "# enable-template" comment in the first 1KB of the file.

Returns the loaded configuration or an error if loading or validation fails.

String converts the config object into a string

Validate validates this config

type CustomDatastoreConfig struct {
	Name [string](https://pkg.go.dev/builtin#string) `yaml:"name"`
	
	
	
	
	IndexName [string](https://pkg.go.dev/builtin#string) `yaml:"indexName"`
	Options map[[string](https://pkg.go.dev/builtin#string)][any](https://pkg.go.dev/builtin#any) `yaml:"options"`
}

CustomDatastoreConfig is the configuration for connecting to a custom datastore that is not supported by temporal core

type DCRedirectionPolicy struct {
 Policy [string](https://pkg.go.dev/builtin#string) `yaml:"policy"` }

DCRedirectionPolicy contains the frontend datacenter redirection policy

type DataStore struct {
	FaultInjection *[FaultInjection](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#FaultInjection) `yaml:"faultInjection"`
	Cassandra *[Cassandra](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Cassandra) `yaml:"cassandra"`
	SQL *[SQL](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#SQL) `yaml:"sql"`
	CustomDataStoreConfig *[CustomDatastoreConfig](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#CustomDatastoreConfig) `yaml:"customDatastore"`
	Elasticsearch *[client](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/persistence/visibility/store/elasticsearch/client).[Config](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/persistence/visibility/store/elasticsearch/client#Config) `yaml:"elasticsearch"`
}

DataStore is the configuration for a single datastore

Validate validates the data store config

DataStoreName is the name of a datastore, e.g. "ShardStore". The full list is defined later in this file.

const (
 ShardStoreName [DataStoreName](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#DataStoreName) = "ShardStore"  TaskStoreName [DataStoreName](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#DataStoreName) = "TaskStore"  MetadataStoreName [DataStoreName](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#DataStoreName) = "MetadataStore"  ExecutionStoreName [DataStoreName](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#DataStoreName) = "ExecutionStore"  QueueName [DataStoreName](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#DataStoreName) = "Queue"  QueueV2Name [DataStoreName](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#DataStoreName) = "QueueV2"  ClusterMDStoreName [DataStoreName](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#DataStoreName) = "ClusterMDStore"  NexusEndpointStoreName [DataStoreName](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#DataStoreName) = "NexusEndpointStore" )

type FaultInjection struct {
	
	
	
	
	
	Targets [FaultInjectionTargets](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#FaultInjectionTargets) `yaml:"targets"`
}

func DefaultFaultInjection() *[FaultInjection](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#FaultInjection)

func (fi *[FaultInjection](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#FaultInjection)) WithError(storeName [DataStoreName](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#DataStoreName), methodName, errorName [string](https://pkg.go.dev/builtin#string), probability [float64](https://pkg.go.dev/builtin#float64)) *[FaultInjection](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#FaultInjection)

type FaultInjectionDataStoreConfig struct {
	
	
	
	
	
	Methods map[[string](https://pkg.go.dev/builtin#string)][FaultInjectionMethodConfig](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#FaultInjectionMethodConfig) `yaml:"methods"`
}

FaultInjectionDataStoreConfig is the fault injection config for a single datastore, e.g., the ShardStore.

type FaultInjectionMethodConfig struct {
	
	
	
	
	
	
	
	Errors map[[string](https://pkg.go.dev/builtin#string)][float64](https://pkg.go.dev/builtin#float64) `yaml:"errors"`

	
	
	
	Seed [int64](https://pkg.go.dev/builtin#int64) `yaml:"seed"`
}

FaultInjectionMethodConfig is the fault injection config for a single method of a data store.

type FaultInjectionTargets struct {
	
	
	DataStores map[[DataStoreName](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#DataStoreName)][FaultInjectionDataStoreConfig](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#FaultInjectionDataStoreConfig) `yaml:"dataStores"`
}

FaultInjectionTargets is the set of targets for fault injection. A target is a method of a data store.

type FilestoreArchiver struct {
 FileMode [string](https://pkg.go.dev/builtin#string) `yaml:"fileMode"`  DirMode [string](https://pkg.go.dev/builtin#string) `yaml:"dirMode"` }

FilestoreArchiver contain the config for filestore archiver

type Global struct {
	Membership [Membership](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Membership) `yaml:"membership"`
	PProf [PProf](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#PProf) `yaml:"pprof"`
	TLS [RootTLS](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#RootTLS) `yaml:"tls"`
	Metrics *[metrics](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/metrics).[Config](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/metrics#Config) `yaml:"metrics"`
	Authorization [Authorization](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Authorization) `yaml:"authorization"`
}

Global contains config items that apply process-wide to all services

type GroupTLS struct {
	Client [ClientTLS](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#ClientTLS) `yaml:"client"`
	Server [ServerTLS](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#ServerTLS) `yaml:"server"`

	
	
	
	PerHostOverrides map[[string](https://pkg.go.dev/builtin#string)][ServerTLS](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#ServerTLS) `yaml:"hostOverrides"`
}

GroupTLS contains an instance client and server TLS settings

func (r *[GroupTLS](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#GroupTLS)) IsClientEnabled() [bool](https://pkg.go.dev/builtin#bool)

func (r *[GroupTLS](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#GroupTLS)) IsServerEnabled() [bool](https://pkg.go.dev/builtin#bool)

type GstorageArchiver struct {
 CredentialsPath [string](https://pkg.go.dev/builtin#string) `yaml:"credentialsPath"` }

GstorageArchiver contain the config for google storage archiver

type HistoryArchival struct {
	State [string](https://pkg.go.dev/builtin#string) `yaml:"state"`
	EnableRead [bool](https://pkg.go.dev/builtin#bool) `yaml:"enableRead"`
	Provider *[HistoryArchiverProvider](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#HistoryArchiverProvider) `yaml:"provider"`
}

HistoryArchival contains the config for history archival

type HistoryArchivalNamespaceDefaults struct {
	State [string](https://pkg.go.dev/builtin#string) `yaml:"state"`
	URI [string](https://pkg.go.dev/builtin#string) `yaml:"URI"`
}

HistoryArchivalNamespaceDefaults is the default history archival config for each namespace

type HistoryArchiverProvider struct {
 Filestore *[FilestoreArchiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#FilestoreArchiver) `yaml:"filestore"`  Gstorage *[GstorageArchiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#GstorageArchiver) `yaml:"gstorage"`  S3store *[S3Archiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#S3Archiver) `yaml:"s3store"` }

HistoryArchiverProvider contains the config for all history archivers

type JWTKeyProvider struct {
 KeySourceURIs [][string](https://pkg.go.dev/builtin#string) `yaml:"keySourceURIs"`  RefreshInterval [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `yaml:"refreshInterval"` }

@@@SNIPSTART temporal-common-service-config-jwtkeyprovider Contains the config for signing key provider for validating JWT tokens

func (p *[JWTKeyProvider](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#JWTKeyProvider)) HasSourceURIsConfigured() [bool](https://pkg.go.dev/builtin#bool)

type KeepAliveClientParameters struct {
 Time *[time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `yaml:"keepAliveTime"`  Timeout *[time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `yaml:"keepAliveTimeout"`  PermitWithoutStream *[bool](https://pkg.go.dev/builtin#bool) `yaml:"keepAlivePermitWithoutStream"` }

type KeepAliveServerConfig struct {
 KeepAliveServerParameters *[KeepAliveServerParameters](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#KeepAliveServerParameters) `yaml:"keepAliveServerParameters"`  KeepAliveEnforcementPolicy *[KeepAliveServerEnforcementPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#KeepAliveServerEnforcementPolicy) `yaml:"keepAliveEnforcementPolicy"` }

type KeepAliveServerEnforcementPolicy struct {
 MinTime *[time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `yaml:"minTime"`  PermitWithoutStream *[bool](https://pkg.go.dev/builtin#bool) `yaml:"permitWithoutStream"` }

type KeepAliveServerParameters struct {
 MaxConnectionIdle *[time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `yaml:"maxConnectionIdle"`  MaxConnectionAge *[time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `yaml:"maxConnectionAge"`  MaxConnectionAgeGrace *[time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `yaml:"maxConnectionAgeGrace"`  Time *[time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `yaml:"keepAliveTime"`  Timeout *[time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `yaml:"keepAliveTimeout"` }

type Membership struct {
	MaxJoinDuration [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `yaml:"maxJoinDuration"`
	
	
	BroadcastAddress [string](https://pkg.go.dev/builtin#string) `yaml:"broadcastAddress"`
}

Membership contains config items related to the membership layer of temporal

type NamespaceDefaults struct {
	Archival [ArchivalNamespaceDefaults](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#ArchivalNamespaceDefaults) `yaml:"archival"`
}

NamespaceDefaults is the default config for each namespace

type PProf struct {
	Port [int](https://pkg.go.dev/builtin#int) `yaml:"port"`
	
	Host [string](https://pkg.go.dev/builtin#string) `yaml:"host"`
}

PProf contains the config items for the pprof utility

type Persistence struct {
	DefaultStore [string](https://pkg.go.dev/builtin#string) `yaml:"defaultStore" validate:"nonzero"`
	VisibilityStore [string](https://pkg.go.dev/builtin#string) `yaml:"visibilityStore"`
	SecondaryVisibilityStore [string](https://pkg.go.dev/builtin#string) `yaml:"secondaryVisibilityStore"`
	
	NumHistoryShards [int32](https://pkg.go.dev/builtin#int32) `yaml:"numHistoryShards" validate:"nonzero"`
	DataStores map[[string](https://pkg.go.dev/builtin#string)][DataStore](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#DataStore) `yaml:"datastores"`
	TransactionSizeLimit [dynamicconfig](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/dynamicconfig).[IntPropertyFn](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/dynamicconfig#IntPropertyFn) `yaml:"-" json:"-"`
}

Persistence contains the configuration for data store / persistence layer

func (c *[Persistence](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Persistence)) DefaultStoreType() [string](https://pkg.go.dev/builtin#string)

DefaultStoreType returns the storeType for the default persistence store

func (c *[Persistence](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Persistence)) GetSecondaryVisibilityStoreConfig() [DataStore](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#DataStore)

func (c *[Persistence](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Persistence)) GetVisibilityStoreConfig() [DataStore](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#DataStore)

func (c *[Persistence](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Persistence)) IsCustomVisibilityStore() [bool](https://pkg.go.dev/builtin#bool)

func (c *[Persistence](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Persistence)) IsSQLVisibilityStore() [bool](https://pkg.go.dev/builtin#bool)

func (c *[Persistence](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Persistence)) SecondaryVisibilityConfigExist() [bool](https://pkg.go.dev/builtin#bool)

SecondaryVisibilityConfigExist returns whether user specified secondaryVisibilityStore in config

Validate validates the persistence config

func (c *[Persistence](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#Persistence)) VisibilityConfigExist() [bool](https://pkg.go.dev/builtin#bool)

VisibilityConfigExist returns whether user specified visibilityStore in config

type PublicClient struct {
	
	HostPort [string](https://pkg.go.dev/builtin#string) `yaml:"hostPort"`
	
	HTTPHostPort [string](https://pkg.go.dev/builtin#string) `yaml:"httpHostPort"`
	
	ForceTLSConfig [string](https://pkg.go.dev/builtin#string) `yaml:"forceTLSConfig"`
}

PublicClient is the config for internal nodes (history/matching/worker) connecting to frontend. There are three methods of connecting:

1.   Use membership to locate "internal-frontend" and connect to them using the Internode TLS config (which can be "no TLS"). This is recommended for deployments that use an Authorizer and ClaimMapper. To use this, leave this section out of your config, and make sure there is an "internal-frontend" section in Services.
2.   Use membership to locate "frontend" and connect to them using the Frontend TLS config (which can be "no TLS"). This is recommended for deployments that don't use an Authorizer or ClaimMapper, or have implemented a custom ClaimMapper that correctly identifies the system worker using mTLS and assigns it an Admin-level claim. To use this, leave this section out of your config and make sure there is _no_ "internal-frontend" section in Services.
3.   Connect to an explicit endpoint using the SystemWorker (falling back to Frontend) TLS config (which can be "no TLS"). You can use this if you want to force frontend connections to go through an external load balancer. If you use this with a ClaimMapper+Authorizer, you need to ensure that your ClaimMapper assigns Admin claims to worker nodes, and your Authorizer correctly handles those claims.

type RPC struct {
	GRPCPort [int](https://pkg.go.dev/builtin#int) `yaml:"grpcPort"`
	MembershipPort [int](https://pkg.go.dev/builtin#int) `yaml:"membershipPort"`
	
	
	BindOnLocalHost [bool](https://pkg.go.dev/builtin#bool) `yaml:"bindOnLocalHost"`
	
	
	BindOnIP [string](https://pkg.go.dev/builtin#string) `yaml:"bindOnIP"`
	
	HTTPPort [int](https://pkg.go.dev/builtin#int) `yaml:"httpPort"`
	
	
	HTTPAdditionalForwardedHeaders [][string](https://pkg.go.dev/builtin#string) `yaml:"httpAdditionalForwardedHeaders"`
	KeepAliveServerConfig [KeepAliveServerConfig](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#KeepAliveServerConfig) `yaml:"keepAliveServerConfig"`
	
	ClientConnectionConfig [ClientConnectionConfig](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#ClientConnectionConfig) `yaml:"clientConnectionConfig"`
}

RPC contains the rpc config items

type ReplicationTaskProcessorConfig struct {
 NoTaskInitialWaitIntervalSecs [int](https://pkg.go.dev/builtin#int) `yaml:"noTaskInitialWaitIntervalSecs"`  NoTaskWaitBackoffCoefficient [float64](https://pkg.go.dev/builtin#float64) `yaml:"noTaskWaitBackoffCoefficient"`  NoTaskMaxWaitIntervalSecs [int](https://pkg.go.dev/builtin#int) `yaml:"noTaskMaxWaitIntervalSecs"` }

ReplicationTaskProcessorConfig is the config for replication task processor.

type Replicator struct{}

Replicator describes the configuration of replicator

type RootTLS struct {
	
	Internode [GroupTLS](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#GroupTLS) `yaml:"internode"`
	
	
	Frontend [GroupTLS](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#GroupTLS) `yaml:"frontend"`
	SystemWorker [WorkerTLS](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#WorkerTLS) `yaml:"systemWorker"`
	RemoteClusters map[[string](https://pkg.go.dev/builtin#string)][GroupTLS](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#GroupTLS) `yaml:"remoteClusters"`
	ExpirationChecks [CertExpirationValidation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#CertExpirationValidation) `yaml:"expirationChecks"`
	RefreshInterval [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `yaml:"refreshInterval"`
}

RootTLS contains all TLS settings for the Temporal server

type S3Archiver struct {
 Region [string](https://pkg.go.dev/builtin#string) `yaml:"region"`  Endpoint *[string](https://pkg.go.dev/builtin#string) `yaml:"endpoint"`  S3ForcePathStyle [bool](https://pkg.go.dev/builtin#bool) `yaml:"s3ForcePathStyle"`  LogLevel [uint](https://pkg.go.dev/builtin#uint) `yaml:"logLevel"` }

S3Archiver contains the config for S3 archiver

type SQL struct {
	Connect func(sqlConfig *[SQL](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#SQL)) (*[sqlx](https://pkg.go.dev/github.com/jmoiron/sqlx).[DB](https://pkg.go.dev/github.com/jmoiron/sqlx#DB), [error](https://pkg.go.dev/builtin#error)) `yaml:"-" json:"-"`
	User [string](https://pkg.go.dev/builtin#string) `yaml:"user"`
	Password [string](https://pkg.go.dev/builtin#string) `yaml:"password"`
	PluginName [string](https://pkg.go.dev/builtin#string) `yaml:"pluginName" validate:"nonzero"`
	DatabaseName [string](https://pkg.go.dev/builtin#string) `yaml:"databaseName" validate:"nonzero"`
	ConnectAddr [string](https://pkg.go.dev/builtin#string) `yaml:"connectAddr" validate:"nonzero"`
	ConnectProtocol [string](https://pkg.go.dev/builtin#string) `yaml:"connectProtocol" validate:"nonzero"`
	ConnectAttributes map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `yaml:"connectAttributes"`
	MaxConns [int](https://pkg.go.dev/builtin#int) `yaml:"maxConns"`
	MaxIdleConns [int](https://pkg.go.dev/builtin#int) `yaml:"maxIdleConns"`
	MaxConnLifetime [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `yaml:"maxConnLifetime"`
	
	
	TaskScanPartitions [int](https://pkg.go.dev/builtin#int) `yaml:"taskScanPartitions"`
	TLS *[auth](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/auth).[TLS](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/auth#TLS) `yaml:"tls"`
}

SQL is the configuration for connecting to a SQL backed datastore

type ServerTLS struct {
	CertFile [string](https://pkg.go.dev/builtin#string) `yaml:"certFile"`
	KeyFile [string](https://pkg.go.dev/builtin#string) `yaml:"keyFile"`
	
	ClientCAFiles [][string](https://pkg.go.dev/builtin#string) `yaml:"clientCaFiles"`

	
	
 CertData [string](https://pkg.go.dev/builtin#string) `yaml:"certData"`  KeyData [string](https://pkg.go.dev/builtin#string) `yaml:"keyData"`  ClientCAData [][string](https://pkg.go.dev/builtin#string) `yaml:"clientCaData"` 
	RequireClientAuth [bool](https://pkg.go.dev/builtin#bool) `yaml:"requireClientAuth"`
}

ServerTLS contains items to load server TLS configuration

type Service struct {
	RPC [RPC](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#RPC) `yaml:"rpc"`
}

Service contains the service specific config items

ServicePortMap contains the gRPC ports for our services.

type Visibility struct {
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	PersistenceCustomSearchAttributes map[[string](https://pkg.go.dev/builtin#string)][int](https://pkg.go.dev/builtin#int) `yaml:"persistenceCustomSearchAttributes" validate:"persistence_custom_search_attributes"`
}

type VisibilityArchival struct {
	State [string](https://pkg.go.dev/builtin#string) `yaml:"state"`
	EnableRead [bool](https://pkg.go.dev/builtin#bool) `yaml:"enableRead"`
	Provider *[VisibilityArchiverProvider](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#VisibilityArchiverProvider) `yaml:"provider"`
}

VisibilityArchival contains the config for visibility archival

type VisibilityArchivalNamespaceDefaults struct {
	State [string](https://pkg.go.dev/builtin#string) `yaml:"state"`
	URI [string](https://pkg.go.dev/builtin#string) `yaml:"URI"`
}

VisibilityArchivalNamespaceDefaults is the default visibility archival config for each namespace

type VisibilityArchiverProvider struct {
 Filestore *[FilestoreArchiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#FilestoreArchiver) `yaml:"filestore"`  S3store *[S3Archiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#S3Archiver) `yaml:"s3store"`  Gstorage *[GstorageArchiver](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#GstorageArchiver) `yaml:"gstorage"` }

VisibilityArchiverProvider contains the config for all visibility archivers

type WorkerTLS struct {
	CertFile [string](https://pkg.go.dev/builtin#string) `yaml:"certFile"`
	KeyFile [string](https://pkg.go.dev/builtin#string) `yaml:"keyFile"`
	
	
 CertData [string](https://pkg.go.dev/builtin#string) `yaml:"certData"`  KeyData [string](https://pkg.go.dev/builtin#string) `yaml:"keyData"` 
	Client [ClientTLS](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/config#ClientTLS) `yaml:"client"`
}

WorkerTLS contains TLS configuration for system workers within the Temporal Cluster to connect to Temporal frontend.
