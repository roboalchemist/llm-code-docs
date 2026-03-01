# Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster

Title: cluster package - go.temporal.io/server/common/cluster - Go Packages

URL Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster

Markdown Content:
Package cluster is a generated GoMock package.

*   [Constants](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#pkg-constants)
*   [Variables](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#pkg-variables)
*   [func GetAllClustersIter(ctx context.Context, metadataStore persistence.ClusterMetadataManager) collection.Iterator[*persistence.GetClusterMetadataResponse]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#GetAllClustersIter)
*   [func IsReplicationEnabledForCluster(clusterInfo ClusterInformation, enableSeparateReplicationFlag bool) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#IsReplicationEnabledForCluster)
*   [func MetadataLifetimeHooks(lc fx.Lifecycle, clusterMetadata Metadata)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MetadataLifetimeHooks)
*   [type CallbackFn](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#CallbackFn)
*   [type ClusterInformation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#ClusterInformation)
*       *   [func ClusterInformationFromDB(getClusterResp *persistence.GetClusterMetadataResponse) *ClusterInformation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#ClusterInformationFromDB)
    *   [func ShallowCopyClusterInformation(information *ClusterInformation) *ClusterInformation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#ShallowCopyClusterInformation)

*   [type Config](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#Config)
*       *   [func NewTestClusterMetadataConfig(enableGlobalNamespace bool, isMasterCluster bool) *Config](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#NewTestClusterMetadataConfig)

*   [type FrontendHTTPClientCache](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#FrontendHTTPClientCache)
*       *   [func NewFrontendHTTPClientCache(metadata Metadata, tlsProvider tlsConfigProvider) *FrontendHTTPClientCache](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#NewFrontendHTTPClientCache)

*       *   [func (c *FrontendHTTPClientCache) Get(targetClusterName string) (*common.FrontendHTTPClient, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#FrontendHTTPClientCache.Get)

*   [type Metadata](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#Metadata)
*       *   [func NewMetadata(enableGlobalNamespace bool, failoverVersionIncrement int64, ...) Metadata](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#NewMetadata)
    *   [func NewMetadataFromConfig(config *Config, clusterMetadataStore persistence.ClusterMetadataManager, ...) Metadata](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#NewMetadataFromConfig)

*   [type MockMetadata](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata)
*       *   [func NewMockMetadata(ctrl *gomock.Controller) *MockMetadata](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#NewMockMetadata)

*       *   [func (m *MockMetadata) ClusterNameForFailoverVersion(isGlobalNamespace bool, failoverVersion int64) string](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata.ClusterNameForFailoverVersion)
    *   [func (m *MockMetadata) EXPECT() *MockMetadataMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata.EXPECT)
    *   [func (m *MockMetadata) GetAllClusterInfo() map[string]ClusterInformation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata.GetAllClusterInfo)
    *   [func (m *MockMetadata) GetClusterID() int64](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata.GetClusterID)
    *   [func (m *MockMetadata) GetCurrentClusterName() string](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata.GetCurrentClusterName)
    *   [func (m *MockMetadata) GetFailoverVersionIncrement() int64](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata.GetFailoverVersionIncrement)
    *   [func (m *MockMetadata) GetMasterClusterName() string](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata.GetMasterClusterName)
    *   [func (m *MockMetadata) GetNextFailoverVersion(arg0 string, arg1 int64) int64](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata.GetNextFailoverVersion)
    *   [func (m *MockMetadata) GetPingChecks() []pingable.Check](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata.GetPingChecks)
    *   [func (m *MockMetadata) IsGlobalNamespaceEnabled() bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata.IsGlobalNamespaceEnabled)
    *   [func (m *MockMetadata) IsMasterCluster() bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata.IsMasterCluster)
    *   [func (m *MockMetadata) IsVersionFromSameCluster(version1, version2 int64) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata.IsVersionFromSameCluster)
    *   [func (m *MockMetadata) RegisterMetadataChangeCallback(callbackId any, cb CallbackFn)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata.RegisterMetadataChangeCallback)
    *   [func (m *MockMetadata) Start()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata.Start)
    *   [func (m *MockMetadata) Stop()](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata.Stop)
    *   [func (m *MockMetadata) UnRegisterMetadataChangeCallback(callbackId any)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata.UnRegisterMetadataChangeCallback)

*   [type MockMetadataMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadataMockRecorder)
*       *   [func (mr *MockMetadataMockRecorder) ClusterNameForFailoverVersion(isGlobalNamespace, failoverVersion any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadataMockRecorder.ClusterNameForFailoverVersion)
    *   [func (mr *MockMetadataMockRecorder) GetAllClusterInfo() *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadataMockRecorder.GetAllClusterInfo)
    *   [func (mr *MockMetadataMockRecorder) GetClusterID() *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadataMockRecorder.GetClusterID)
    *   [func (mr *MockMetadataMockRecorder) GetCurrentClusterName() *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadataMockRecorder.GetCurrentClusterName)
    *   [func (mr *MockMetadataMockRecorder) GetFailoverVersionIncrement() *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadataMockRecorder.GetFailoverVersionIncrement)
    *   [func (mr *MockMetadataMockRecorder) GetMasterClusterName() *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadataMockRecorder.GetMasterClusterName)
    *   [func (mr *MockMetadataMockRecorder) GetNextFailoverVersion(arg0, arg1 any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadataMockRecorder.GetNextFailoverVersion)
    *   [func (mr *MockMetadataMockRecorder) GetPingChecks() *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadataMockRecorder.GetPingChecks)
    *   [func (mr *MockMetadataMockRecorder) IsGlobalNamespaceEnabled() *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadataMockRecorder.IsGlobalNamespaceEnabled)
    *   [func (mr *MockMetadataMockRecorder) IsMasterCluster() *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadataMockRecorder.IsMasterCluster)
    *   [func (mr *MockMetadataMockRecorder) IsVersionFromSameCluster(version1, version2 any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadataMockRecorder.IsVersionFromSameCluster)
    *   [func (mr *MockMetadataMockRecorder) RegisterMetadataChangeCallback(callbackId, cb any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadataMockRecorder.RegisterMetadataChangeCallback)
    *   [func (mr *MockMetadataMockRecorder) Start() *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadataMockRecorder.Start)
    *   [func (mr *MockMetadataMockRecorder) Stop() *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadataMockRecorder.Stop)
    *   [func (mr *MockMetadataMockRecorder) UnRegisterMetadataChangeCallback(callbackId any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadataMockRecorder.UnRegisterMetadataChangeCallback)

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/common/cluster/metadata_test_config.go#L7)

const (
	TestCurrentClusterInitialFailoverVersion = [int64](https://pkg.go.dev/builtin#int64)(1)
	TestAlternativeClusterInitialFailoverVersion = [int64](https://pkg.go.dev/builtin#int64)(2)
	TestFailoverVersionIncrement = [int64](https://pkg.go.dev/builtin#int64)(10)
	TestCurrentClusterName = "active"
	TestAlternativeClusterName = "standby"
	TestCurrentClusterFrontendAddress = "127.0.0.1:7134"
	TestAlternativeClusterFrontendAddress = "127.0.0.1:8134"
	TestCurrentClusterFrontendHTTPAddress = "127.0.0.1:7144"
	TestAlternativeClusterFrontendHTTPAddress = "127.0.0.1:8144"
)

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/common/cluster/metadata_test_config.go#L28)

var (
	TestAllClusterNames = [][string](https://pkg.go.dev/builtin#string){[TestCurrentClusterName](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#TestCurrentClusterName), [TestAlternativeClusterName](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#TestAlternativeClusterName)}
	TestAllClusterInfo = map[[string](https://pkg.go.dev/builtin#string)][ClusterInformation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#ClusterInformation){
		[TestCurrentClusterName](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#TestCurrentClusterName): {
			Enabled:                [true](https://pkg.go.dev/builtin#true),
			InitialFailoverVersion: [TestCurrentClusterInitialFailoverVersion](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#TestCurrentClusterInitialFailoverVersion),
			RPCAddress:             [TestCurrentClusterFrontendAddress](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#TestCurrentClusterFrontendAddress),
			HTTPAddress:            [TestCurrentClusterFrontendHTTPAddress](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#TestCurrentClusterFrontendHTTPAddress),
			ShardCount:             8,
			ClusterID:              [uuid](https://pkg.go.dev/github.com/google/uuid).[NewString](https://pkg.go.dev/github.com/google/uuid#NewString)(),
		},
		[TestAlternativeClusterName](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#TestAlternativeClusterName): {
			Enabled:                [true](https://pkg.go.dev/builtin#true),
			InitialFailoverVersion: [TestAlternativeClusterInitialFailoverVersion](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#TestAlternativeClusterInitialFailoverVersion),
			RPCAddress:             [TestAlternativeClusterFrontendAddress](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#TestAlternativeClusterFrontendAddress),
			HTTPAddress:            [TestAlternativeClusterFrontendHTTPAddress](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#TestAlternativeClusterFrontendHTTPAddress),
			ShardCount:             4,
			ClusterID:              [uuid](https://pkg.go.dev/github.com/google/uuid).[NewString](https://pkg.go.dev/github.com/google/uuid#NewString)(),
		},
	}

	TestSingleDCAllClusterNames = [][string](https://pkg.go.dev/builtin#string){[TestCurrentClusterName](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#TestCurrentClusterName)}
	TestSingleDCClusterInfo = map[[string](https://pkg.go.dev/builtin#string)][ClusterInformation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#ClusterInformation){
		[TestCurrentClusterName](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#TestCurrentClusterName): {
			Enabled:                [true](https://pkg.go.dev/builtin#true),
			InitialFailoverVersion: [TestCurrentClusterInitialFailoverVersion](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#TestCurrentClusterInitialFailoverVersion),
			RPCAddress:             [TestCurrentClusterFrontendAddress](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#TestCurrentClusterFrontendAddress),
			HTTPAddress:            [TestCurrentClusterFrontendHTTPAddress](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#TestCurrentClusterFrontendHTTPAddress),
			ClusterID:              [uuid](https://pkg.go.dev/github.com/google/uuid).[NewString](https://pkg.go.dev/github.com/google/uuid#NewString)(),
		},
	}
)

GetAllClustersIter returns an iterator that can be used to iterate over all clusters in the metadata store.

func IsReplicationEnabledForCluster(clusterInfo [ClusterInformation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#ClusterInformation), enableSeparateReplicationFlag [bool](https://pkg.go.dev/builtin#bool)) [bool](https://pkg.go.dev/builtin#bool)

IsReplicationEnabledForCluster checks if replication is enabled for a cluster, considering the feature flag. When enableSeparateReplicationFlag is false, it falls back to only checking the Enabled flag. This is a shared helper function used across history service components.

func MetadataLifetimeHooks(
	lc [fx](https://pkg.go.dev/go.uber.org/fx).[Lifecycle](https://pkg.go.dev/go.uber.org/fx#Lifecycle),
	clusterMetadata [Metadata](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#Metadata),
)

type CallbackFn func(oldClusterMetadata map[[string](https://pkg.go.dev/builtin#string)]*[ClusterInformation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#ClusterInformation), newClusterMetadata map[[string](https://pkg.go.dev/builtin#string)]*[ClusterInformation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#ClusterInformation))

type ClusterInformation struct {
 Enabled [bool](https://pkg.go.dev/builtin#bool) `yaml:"enabled"`  InitialFailoverVersion [int64](https://pkg.go.dev/builtin#int64) `yaml:"initialFailoverVersion"` 	RPCAddress [string](https://pkg.go.dev/builtin#string) `yaml:"rpcAddress"`
	
	HTTPAddress [string](https://pkg.go.dev/builtin#string) `yaml:"httpAddress"`
	
 ClusterID [string](https://pkg.go.dev/builtin#string) `yaml:"-"`  ShardCount [int32](https://pkg.go.dev/builtin#int32) `yaml:"-"`  Tags map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `yaml:"-"` 	ReplicationEnabled [bool](https://pkg.go.dev/builtin#bool) `yaml:"-"`
	
}

ClusterInformation contains information for a single cluster.

func ShallowCopyClusterInformation(information *[ClusterInformation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#ClusterInformation)) *[ClusterInformation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#ClusterInformation)

ShallowCopyClusterInformation returns a shallow copy of the given ClusterInformation. The [ClusterInformation.Tags] field is not deep-copied, so you must be careful when modifying it.

type Config struct {
 EnableGlobalNamespace [bool](https://pkg.go.dev/builtin#bool) `yaml:"enableGlobalNamespace"` 	FailoverVersionIncrement [int64](https://pkg.go.dev/builtin#int64) `yaml:"failoverVersionIncrement"`
	
	MasterClusterName [string](https://pkg.go.dev/builtin#string) `yaml:"masterClusterName"`
	CurrentClusterName [string](https://pkg.go.dev/builtin#string) `yaml:"currentClusterName"`
	ClusterInformation map[[string](https://pkg.go.dev/builtin#string)][ClusterInformation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#ClusterInformation) `yaml:"clusterInformation"`
	Tags map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `yaml:"tags"`
}

Config contains the all cluster which participated in cross DC

func NewTestClusterMetadataConfig(enableGlobalNamespace [bool](https://pkg.go.dev/builtin#bool), isMasterCluster [bool](https://pkg.go.dev/builtin#bool)) *[Config](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#Config)

NewTestClusterMetadataConfig return an cluster metadata config

type FrontendHTTPClientCache struct {
	
}

func NewFrontendHTTPClientCache(
	metadata [Metadata](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#Metadata),
	tlsProvider tlsConfigProvider,
) *[FrontendHTTPClientCache](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#FrontendHTTPClientCache)

Get returns a cached HttpClient if available, or constructs a new one for the given cluster name.

type Metadata interface {
	[pingable](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/pingable).[Pingable](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/pingable#Pingable)

	
	IsGlobalNamespaceEnabled() [bool](https://pkg.go.dev/builtin#bool)
	IsMasterCluster() [bool](https://pkg.go.dev/builtin#bool)
	GetClusterID() [int64](https://pkg.go.dev/builtin#int64)
	GetNextFailoverVersion([string](https://pkg.go.dev/builtin#string), [int64](https://pkg.go.dev/builtin#int64)) [int64](https://pkg.go.dev/builtin#int64)
	IsVersionFromSameCluster(version1 [int64](https://pkg.go.dev/builtin#int64), version2 [int64](https://pkg.go.dev/builtin#int64)) [bool](https://pkg.go.dev/builtin#bool)
	GetMasterClusterName() [string](https://pkg.go.dev/builtin#string)
	GetCurrentClusterName() [string](https://pkg.go.dev/builtin#string)
	GetAllClusterInfo() map[[string](https://pkg.go.dev/builtin#string)][ClusterInformation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#ClusterInformation)
	ClusterNameForFailoverVersion(isGlobalNamespace [bool](https://pkg.go.dev/builtin#bool), failoverVersion [int64](https://pkg.go.dev/builtin#int64)) [string](https://pkg.go.dev/builtin#string)
	
 GetFailoverVersionIncrement() [int64](https://pkg.go.dev/builtin#int64) RegisterMetadataChangeCallback(callbackId [any](https://pkg.go.dev/builtin#any), cb [CallbackFn](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#CallbackFn))  UnRegisterMetadataChangeCallback(callbackId [any](https://pkg.go.dev/builtin#any))  Start()  Stop() }

Metadata provides information about the current cluster and other registered remote clusters.

type MockMetadata struct {
	
}

MockMetadata is a mock of Metadata interface.

NewMockMetadata creates a new mock instance.

func (m *[MockMetadata](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata)) ClusterNameForFailoverVersion(isGlobalNamespace [bool](https://pkg.go.dev/builtin#bool), failoverVersion [int64](https://pkg.go.dev/builtin#int64)) [string](https://pkg.go.dev/builtin#string)

ClusterNameForFailoverVersion mocks base method.

func (m *[MockMetadata](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata)) EXPECT() *[MockMetadataMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadataMockRecorder)

EXPECT returns an object that allows the caller to indicate expected use.

GetAllClusterInfo mocks base method.

func (m *[MockMetadata](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata)) GetClusterID() [int64](https://pkg.go.dev/builtin#int64)

GetClusterID mocks base method.

func (m *[MockMetadata](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata)) GetCurrentClusterName() [string](https://pkg.go.dev/builtin#string)

GetCurrentClusterName mocks base method.

func (m *[MockMetadata](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata)) GetFailoverVersionIncrement() [int64](https://pkg.go.dev/builtin#int64)

GetFailoverVersionIncrement mocks base method.

func (m *[MockMetadata](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata)) GetMasterClusterName() [string](https://pkg.go.dev/builtin#string)

GetMasterClusterName mocks base method.

GetNextFailoverVersion mocks base method.

GetPingChecks mocks base method.

func (m *[MockMetadata](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata)) IsGlobalNamespaceEnabled() [bool](https://pkg.go.dev/builtin#bool)

IsGlobalNamespaceEnabled mocks base method.

func (m *[MockMetadata](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata)) IsMasterCluster() [bool](https://pkg.go.dev/builtin#bool)

IsMasterCluster mocks base method.

func (m *[MockMetadata](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata)) IsVersionFromSameCluster(version1, version2 [int64](https://pkg.go.dev/builtin#int64)) [bool](https://pkg.go.dev/builtin#bool)

IsVersionFromSameCluster mocks base method.

func (m *[MockMetadata](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata)) RegisterMetadataChangeCallback(callbackId [any](https://pkg.go.dev/builtin#any), cb [CallbackFn](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#CallbackFn))

RegisterMetadataChangeCallback mocks base method.

func (m *[MockMetadata](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata)) Start()

Start mocks base method.

func (m *[MockMetadata](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata)) Stop()

Stop mocks base method.

func (m *[MockMetadata](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadata)) UnRegisterMetadataChangeCallback(callbackId [any](https://pkg.go.dev/builtin#any))

UnRegisterMetadataChangeCallback mocks base method.

type MockMetadataMockRecorder struct {
	
}

MockMetadataMockRecorder is the mock recorder for MockMetadata.

func (mr *[MockMetadataMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/cluster#MockMetadataMockRecorder)) ClusterNameForFailoverVersion(isGlobalNamespace, failoverVersion [any](https://pkg.go.dev/builtin#any)) *[gomock](https://pkg.go.dev/go.uber.org/mock/gomock).[Call](https://pkg.go.dev/go.uber.org/mock/gomock#Call)

ClusterNameForFailoverVersion indicates an expected call of ClusterNameForFailoverVersion.

GetAllClusterInfo indicates an expected call of GetAllClusterInfo.

GetClusterID indicates an expected call of GetClusterID.

GetCurrentClusterName indicates an expected call of GetCurrentClusterName.

GetFailoverVersionIncrement indicates an expected call of GetFailoverVersionIncrement.

GetMasterClusterName indicates an expected call of GetMasterClusterName.

GetNextFailoverVersion indicates an expected call of GetNextFailoverVersion.

GetPingChecks indicates an expected call of GetPingChecks.

IsGlobalNamespaceEnabled indicates an expected call of IsGlobalNamespaceEnabled.

IsMasterCluster indicates an expected call of IsMasterCluster.

IsVersionFromSameCluster indicates an expected call of IsVersionFromSameCluster.

RegisterMetadataChangeCallback indicates an expected call of RegisterMetadataChangeCallback.

Start indicates an expected call of Start.

Stop indicates an expected call of Stop.

UnRegisterMetadataChangeCallback indicates an expected call of UnRegisterMetadataChangeCallback.
