### Overview ¶

+k8s:deepcopy-gen=package
+k8s:defaulter-gen=TypeMeta
+groupName=fission.io
+groupGoName=core

Package v1 contains API Schema definitions for the fission.io v1 API group
+kubebuilder:object:generate=true
+groupName=fission.io

    
### Index ¶

- Constants

- Variables

- 
        func AggregateValidationErrors(objName string, err error) error

- 
        func IsValidCronSpec(spec string) error

- 
        func RegisterDefaults(scheme *runtime.Scheme) error

- 
        func Resource(resource string) schema.GroupResource

- 
        func SetObjectDefaults_Environment(in *Environment)

- 
        func SetObjectDefaults_EnvironmentList(in *EnvironmentList)

- 
        func SetObjectDefaults_Function(in *Function)

- 
        func SetObjectDefaults_FunctionList(in *FunctionList)

- 
        func SetObjectDefaults_MessageQueueTrigger(in *MessageQueueTrigger)

- 
        func SetObjectDefaults_MessageQueueTriggerList(in *MessageQueueTriggerList)

- 
        func ValidateKubeLabel(field string, labels map[string]string) error

- 
        func ValidateKubeName(field string, val string) error

- 
        func ValidateKubePort(field string, port int) error

- 
        func ValidateKubeReference(refName string, name string, namespace string) error

- 
          type AllowedFunctionsPerContainer

- 
          type Archive

- 

  - 
            func (in *Archive) DeepCopy() *Archive

  - 
            func (in *Archive) DeepCopyInto(out *Archive)

  - 
            func (a Archive) IsEmpty() bool

  - 
            func (Archive) SwaggerDoc() map[string]string

  - 
            func (archive Archive) Validate() error

- 
          type ArchiveType

- 
          type AuthLogin

- 

  - 
            func (in *AuthLogin) DeepCopy() *AuthLogin

  - 
            func (in *AuthLogin) DeepCopyInto(out *AuthLogin)

  - 
            func (AuthLogin) SwaggerDoc() map[string]string

- 
          type BuildStatus

- 
          type Builder

- 

  - 
            func (in *Builder) DeepCopy() *Builder

  - 
            func (in *Builder) DeepCopyInto(out *Builder)

  - 
            func (Builder) SwaggerDoc() map[string]string

  - 
            func (builder Builder) Validate() error

- 
          type CanaryConfig

- 

  - 
            func (in *CanaryConfig) DeepCopy() *CanaryConfig

  - 
            func (in *CanaryConfig) DeepCopyInto(out *CanaryConfig)

  - 
            func (in *CanaryConfig) DeepCopyObject() runtime.Object

  - 
            func (CanaryConfig) SwaggerDoc() map[string]string

- 
          type CanaryConfigList

- 

  - 
            func (in *CanaryConfigList) DeepCopy() *CanaryConfigList

  - 
            func (in *CanaryConfigList) DeepCopyInto(out *CanaryConfigList)

  - 
            func (in *CanaryConfigList) DeepCopyObject() runtime.Object

  - 
            func (CanaryConfigList) SwaggerDoc() map[string]string

- 
          type CanaryConfigSpec

- 

  - 
            func (in *CanaryConfigSpec) DeepCopy() *CanaryConfigSpec

  - 
            func (in *CanaryConfigSpec) DeepCopyInto(out *CanaryConfigSpec)

  - 
            func (CanaryConfigSpec) SwaggerDoc() map[string]string

- 
          type CanaryConfigStatus

- 

  - 
            func (in *CanaryConfigStatus) DeepCopy() *CanaryConfigStatus

  - 
            func (in *CanaryConfigStatus) DeepCopyInto(out *CanaryConfigStatus)

  - 
            func (CanaryConfigStatus) SwaggerDoc() map[string]string

- 
          type Checksum

- 

  - 
            func (in *Checksum) DeepCopy() *Checksum

  - 
            func (in *Checksum) DeepCopyInto(out *Checksum)

  - 
            func (Checksum) SwaggerDoc() map[string]string

  - 
            func (checksum Checksum) Validate() error

- 
          type ChecksumType

- 
          type ConfigMapReference

- 

  - 
            func (in *ConfigMapReference) DeepCopy() *ConfigMapReference

  - 
            func (in *ConfigMapReference) DeepCopyInto(out *ConfigMapReference)

  - 
            func (ConfigMapReference) SwaggerDoc() map[string]string

  - 
            func (ref ConfigMapReference) Validate() error

- 
          type Environment

- 

  - 
            func (in *Environment) DeepCopy() *Environment

  - 
            func (in *Environment) DeepCopyInto(out *Environment)

  - 
            func (in *Environment) DeepCopyObject() runtime.Object

  - 
            func (Environment) SwaggerDoc() map[string]string

  - 
            func (e *Environment) Validate() error

- 
          type EnvironmentList

- 

  - 
            func (in *EnvironmentList) DeepCopy() *EnvironmentList

  - 
            func (in *EnvironmentList) DeepCopyInto(out *EnvironmentList)

  - 
            func (in *EnvironmentList) DeepCopyObject() runtime.Object

  - 
            func (EnvironmentList) SwaggerDoc() map[string]string

  - 
            func (el *EnvironmentList) Validate() error

- 
          type EnvironmentReference

- 

  - 
            func (in *EnvironmentReference) DeepCopy() *EnvironmentReference

  - 
            func (in *EnvironmentReference) DeepCopyInto(out *EnvironmentReference)

  - 
            func (EnvironmentReference) SwaggerDoc() map[string]string

  - 
            func (ref EnvironmentReference) Validate() error

- 
          type EnvironmentSpec

- 

  - 
            func (in *EnvironmentSpec) DeepCopy() *EnvironmentSpec

  - 
            func (in *EnvironmentSpec) DeepCopyInto(out *EnvironmentSpec)

  - 
            func (EnvironmentSpec) SwaggerDoc() map[string]string

  - 
            func (spec EnvironmentSpec) Validate() error

- 
          type ExecutionStrategy

- 

  - 
            func (in *ExecutionStrategy) DeepCopy() *ExecutionStrategy

  - 
            func (in *ExecutionStrategy) DeepCopyInto(out *ExecutionStrategy)

  - 
            func (ExecutionStrategy) SwaggerDoc() map[string]string

  - 
            func (es ExecutionStrategy) Validate() error

- 
          type ExecutorType

- 
          type FailureType

- 
          type Function

- 

  - 
            func (in *Function) DeepCopy() *Function

  - 
            func (in *Function) DeepCopyInto(out *Function)

  - 
            func (in *Function) DeepCopyObject() runtime.Object

  - 
            func (fn Function) GetConcurrency() int

  - 
            func (fn Function) GetRequestPerPod() int

  - 
            func (fn Function) GetRetainPods() int

  - 
            func (Function) SwaggerDoc() map[string]string

  - 
            func (f *Function) Validate() error

- 
          type FunctionList

- 

  - 
            func (in *FunctionList) DeepCopy() *FunctionList

  - 
            func (in *FunctionList) DeepCopyInto(out *FunctionList)

  - 
            func (in *FunctionList) DeepCopyObject() runtime.Object

  - 
            func (FunctionList) SwaggerDoc() map[string]string

  - 
            func (fl *FunctionList) Validate() error

- 
          type FunctionPackageRef

- 

  - 
            func (in *FunctionPackageRef) DeepCopy() *FunctionPackageRef

  - 
            func (in *FunctionPackageRef) DeepCopyInto(out *FunctionPackageRef)

  - 
            func (FunctionPackageRef) SwaggerDoc() map[string]string

  - 
            func (ref FunctionPackageRef) Validate() error

- 
          type FunctionReference

- 

  - 
            func (in *FunctionReference) DeepCopy() *FunctionReference

  - 
            func (in *FunctionReference) DeepCopyInto(out *FunctionReference)

  - 
            func (FunctionReference) SwaggerDoc() map[string]string

  - 
            func (ref FunctionReference) Validate() error

- 
          type FunctionReferenceType

- 
          type FunctionSpec

- 

  - 
            func (in *FunctionSpec) DeepCopy() *FunctionSpec

  - 
            func (in *FunctionSpec) DeepCopyInto(out *FunctionSpec)

  - 
            func (FunctionSpec) SwaggerDoc() map[string]string

  - 
            func (spec FunctionSpec) Validate() error

- 
          type HTTPTrigger

- 

  - 
            func (in *HTTPTrigger) DeepCopy() *HTTPTrigger

  - 
            func (in *HTTPTrigger) DeepCopyInto(out *HTTPTrigger)

  - 
            func (in *HTTPTrigger) DeepCopyObject() runtime.Object

  - 
            func (HTTPTrigger) SwaggerDoc() map[string]string

  - 
            func (h *HTTPTrigger) Validate() error

- 
          type HTTPTriggerList

- 

  - 
            func (in *HTTPTriggerList) DeepCopy() *HTTPTriggerList

  - 
            func (in *HTTPTriggerList) DeepCopyInto(out *HTTPTriggerList)

  - 
            func (in *HTTPTriggerList) DeepCopyObject() runtime.Object

  - 
            func (HTTPTriggerList) SwaggerDoc() map[string]string

  - 
            func (hl *HTTPTriggerList) Validate() error

- 
          type HTTPTriggerSpec

- 

  - 
            func (in *HTTPTriggerSpec) DeepCopy() *HTTPTriggerSpec

  - 
            func (in *HTTPTriggerSpec) DeepCopyInto(out *HTTPTriggerSpec)

  - 
            func (HTTPTriggerSpec) SwaggerDoc() map[string]string

  - 
            func (spec HTTPTriggerSpec) Validate() error

- 
          type IngressConfig

- 

  - 
            func (in *IngressConfig) DeepCopy() *IngressConfig

  - 
            func (in *IngressConfig) DeepCopyInto(out *IngressConfig)

  - 
            func (IngressConfig) SwaggerDoc() map[string]string

  - 
            func (config IngressConfig) Validate() error

- 
          type InvokeStrategy

- 

  - 
            func (in *InvokeStrategy) DeepCopy() *InvokeStrategy

  - 
            func (in *InvokeStrategy) DeepCopyInto(out *InvokeStrategy)

  - 
            func (InvokeStrategy) SwaggerDoc() map[string]string

  - 
            func (is InvokeStrategy) Validate() error

- 
          type KubernetesWatchTrigger

- 

  - 
            func (in *KubernetesWatchTrigger) DeepCopy() *KubernetesWatchTrigger

  - 
            func (in *KubernetesWatchTrigger) DeepCopyInto(out *KubernetesWatchTrigger)

  - 
            func (in *KubernetesWatchTrigger) DeepCopyObject() runtime.Object

  - 
            func (KubernetesWatchTrigger) SwaggerDoc() map[string]string

  - 
            func (k *KubernetesWatchTrigger) Validate() error

- 
          type KubernetesWatchTriggerList

- 

  - 
            func (in *KubernetesWatchTriggerList) DeepCopy() *KubernetesWatchTriggerList

  - 
            func (in *KubernetesWatchTriggerList) DeepCopyInto(out *KubernetesWatchTriggerList)

  - 
            func (in *KubernetesWatchTriggerList) DeepCopyObject() runtime.Object

  - 
            func (KubernetesWatchTriggerList) SwaggerDoc() map[string]string

  - 
            func (kl *KubernetesWatchTriggerList) Validate() error

- 
          type KubernetesWatchTriggerSpec

- 

  - 
            func (in *KubernetesWatchTriggerSpec) DeepCopy() *KubernetesWatchTriggerSpec

  - 
            func (in *KubernetesWatchTriggerSpec) DeepCopyInto(out *KubernetesWatchTriggerSpec)

  - 
            func (KubernetesWatchTriggerSpec) SwaggerDoc() map[string]string

  - 
            func (spec KubernetesWatchTriggerSpec) Validate() error

- 
          type MessageQueueTrigger

- 

  - 
            func (in *MessageQueueTrigger) DeepCopy() *MessageQueueTrigger

  - 
            func (in *MessageQueueTrigger) DeepCopyInto(out *MessageQueueTrigger)

  - 
            func (in *MessageQueueTrigger) DeepCopyObject() runtime.Object

  - 
            func (MessageQueueTrigger) SwaggerDoc() map[string]string

  - 
            func (m *MessageQueueTrigger) Validate() error

- 
          type MessageQueueTriggerList

- 

  - 
            func (in *MessageQueueTriggerList) DeepCopy() *MessageQueueTriggerList

  - 
            func (in *MessageQueueTriggerList) DeepCopyInto(out *MessageQueueTriggerList)

  - 
            func (in *MessageQueueTriggerList) DeepCopyObject() runtime.Object

  - 
            func (MessageQueueTriggerList) SwaggerDoc() map[string]string

  - 
            func (ml *MessageQueueTriggerList) Validate() error

- 
          type MessageQueueTriggerSpec

- 

  - 
            func (in *MessageQueueTriggerSpec) DeepCopy() *MessageQueueTriggerSpec

  - 
            func (in *MessageQueueTriggerSpec) DeepCopyInto(out *MessageQueueTriggerSpec)

  - 
            func (MessageQueueTriggerSpec) SwaggerDoc() map[string]string

  - 
            func (spec MessageQueueTriggerSpec) Validate() error

- 
          type MessageQueueType

- 
          type Package

- 

  - 
            func (in *Package) DeepCopy() *Package

  - 
            func (in *Package) DeepCopyInto(out *Package)

  - 
            func (in *Package) DeepCopyObject() runtime.Object

  - 
            func (Package) SwaggerDoc() map[string]string

  - 
            func (p *Package) Validate() error

- 
          type PackageList

- 

  - 
            func (in *PackageList) DeepCopy() *PackageList

  - 
            func (in *PackageList) DeepCopyInto(out *PackageList)

  - 
            func (in *PackageList) DeepCopyObject() runtime.Object

  - 
            func (PackageList) SwaggerDoc() map[string]string

  - 
            func (pl *PackageList) Validate() error

- 
          type PackageRef

- 

  - 
            func (in *PackageRef) DeepCopy() *PackageRef

  - 
            func (in *PackageRef) DeepCopyInto(out *PackageRef)

  - 
            func (PackageRef) SwaggerDoc() map[string]string

  - 
            func (ref PackageRef) Validate() error

- 
          type PackageSpec

- 

  - 
            func (in *PackageSpec) DeepCopy() *PackageSpec

  - 
            func (in *PackageSpec) DeepCopyInto(out *PackageSpec)

  - 
            func (PackageSpec) SwaggerDoc() map[string]string

  - 
            func (spec PackageSpec) Validate() error

- 
          type PackageStatus

- 

  - 
            func (in *PackageStatus) DeepCopy() *PackageStatus

  - 
            func (in *PackageStatus) DeepCopyInto(out *PackageStatus)

  - 
            func (PackageStatus) SwaggerDoc() map[string]string

  - 
            func (sts PackageStatus) Validate() error

- 
          type RouterAuthToken

- 

  - 
            func (in *RouterAuthToken) DeepCopy() *RouterAuthToken

  - 
            func (in *RouterAuthToken) DeepCopyInto(out *RouterAuthToken)

  - 
            func (RouterAuthToken) SwaggerDoc() map[string]string

- 
          type Runtime

- 

  - 
            func (in *Runtime) DeepCopy() *Runtime

  - 
            func (in *Runtime) DeepCopyInto(out *Runtime)

  - 
            func (Runtime) SwaggerDoc() map[string]string

  - 
            func (runtime Runtime) Validate() error

- 
          type SecretReference

- 

  - 
            func (in *SecretReference) DeepCopy() *SecretReference

  - 
            func (in *SecretReference) DeepCopyInto(out *SecretReference)

  - 
            func (SecretReference) SwaggerDoc() map[string]string

  - 
            func (ref SecretReference) Validate() error

- 
          type StrategyType

- 
          type TimeTrigger

- 

  - 
            func (in *TimeTrigger) DeepCopy() *TimeTrigger

  - 
            func (in *TimeTrigger) DeepCopyInto(out *TimeTrigger)

  - 
            func (in *TimeTrigger) DeepCopyObject() runtime.Object

  - 
            func (TimeTrigger) SwaggerDoc() map[string]string

  - 
            func (t *TimeTrigger) Validate() error

- 
          type TimeTriggerList

- 

  - 
            func (in *TimeTriggerList) DeepCopy() *TimeTriggerList

  - 
            func (in *TimeTriggerList) DeepCopyInto(out *TimeTriggerList)

  - 
            func (in *TimeTriggerList) DeepCopyObject() runtime.Object

  - 
            func (TimeTriggerList) SwaggerDoc() map[string]string

  - 
            func (tl *TimeTriggerList) Validate() error

- 
          type TimeTriggerSpec

- 

  - 
            func (in *TimeTriggerSpec) DeepCopy() *TimeTriggerSpec

  - 
            func (in *TimeTriggerSpec) DeepCopyInto(out *TimeTriggerSpec)

  - 
            func (TimeTriggerSpec) SwaggerDoc() map[string]string

  - 
            func (spec TimeTriggerSpec) Validate() error

- 
          type ValidationError

- 

  - 
            func MakeValidationErr(errType ValidationErrorType, field string, val interface{}, detail ...string) ValidationError

- 

  - 
            func (in *ValidationError) DeepCopy() *ValidationError

  - 
            func (in *ValidationError) DeepCopyInto(out *ValidationError)

  - 
            func (e ValidationError) Error() string

- 
          type ValidationErrorType

### Constants ¶

  
    
      View Source
      

```
const (
	EXECUTOR_INSTANCEID_LABEL string = "executorInstanceId"
	DEFAULT_FUNCTION_TIMEOUT  int    = 60
)
```

    
  

    
      View Source
      

```
const (
	BuildStatusPending   = "pending"
	BuildStatusRunning   = "running"
	BuildStatusSucceeded = "succeeded"
	BuildStatusFailed    = "failed"
	BuildStatusNone      = "none"
)
```

    
  

    
      View Source
      

```
const (
	AllowedFunctionsPerContainerSingle   = "single"
	AllowedFunctionsPerContainerInfinite = "infinite"
)
```

    
  

    
      View Source
      

```
const (
	RuntimePodSpecPath = "/etc/fission/runtime-podspec-patch.yaml"
	BuilderPodSpecPath = "/etc/fission/builder-podspec-patch.yaml"
)
```

    
  

    
      View Source
      

```
const (
	SharedVolumeUserfunc   = "userfunc"
	SharedVolumePackages   = "packages"
	SharedVolumeSecrets    = "secrets"
	SharedVolumeConfigmaps = "configmaps"
	PodInfoVolume          = "podinfo"
	PodInfoMount           = "/etc/podinfo"
)
```

    
  

    
      View Source
      

```
const (
	// FunctionReferenceFunctionName means that the function
	// reference is simply by function name.
	FunctionReferenceTypeFunctionName = "name"

	FunctionReferenceTypeFunctionWeights = "function-weights"
)
```

    
  

    
      View Source
      

```
const (
	// failure type currently supported is http status code. This could be extended
	// in the future.
	FailureTypeStatusCode FailureType = "status-code"

	// Status of canary config can be one of the following
	CanaryConfigStatusPending   = "pending"
	CanaryConfigStatusSucceeded = "succeeded"
	CanaryConfigStatusFailed    = "failed"
	CanaryConfigStatusAborted   = "aborted"

	// set a max number for iterations to prevent infinite processing of canary config
	MaxIterationsForCanaryConfig = 10
)
```

    
  

    
      View Source
      

```
const (
	FETCH_SOURCE = iota
	FETCH_DEPLOYMENT
	FETCH_URL
)
```

    
  

    
      View Source
      

```
const (
	ENVIRONMENT_NAMESPACE     = "environmentNamespace"
	ENVIRONMENT_NAME          = "environmentName"
	ENVIRONMENT_UID           = "environmentUid"
	FUNCTION_NAMESPACE        = "functionNamespace"
	FUNCTION_NAME             = "functionName"
	FUNCTION_UID              = "functionUid"
	FUNCTION_RESOURCE_VERSION = "functionResourceVersion"
	EXECUTOR_TYPE             = "executorType"
	MANAGED                   = "managed"
)
```

    
  

executor kubernetes object label key

    
      View Source
      

```
const (
	FissionBuilderSA = "fission-builder"
	FissionFetcherSA = "fission-fetcher"
)
```

    
  

    
      View Source
      

```
const (
	CanaryConfigResource    = "canaryconfigs"
	EnvironmentResource     = "environments"
	FunctionResource        = "functions"
	HttpTriggerResource     = "httptriggers"
	KubernetesWatchResource = "kuberneteswatchtriggers"
	MessageQueueResource    = "messagequeuetriggers"
	PackagesResource        = "packages"
	TimeTriggerResource     = "timetriggers"
)
```

    
  

    
      View Source
      

```
const (
	Pods        = "pods"
	Deployments = "deployments"
	ReplicaSets = "replicasets"
	Services    = "services"
	ConfigMaps  = "configmaps"
	Secrets     = "secrets"
)
```

    
  

    
      View Source
      

```
const (
	CRD_VERSION          = "fission.io/v1"
	CRD_NAME_ENVIRONMENT = "Environment"
)
```

    
  

    
      View Source
      

```
const (
	DefaultConcurrency    = 500
	DefaultRequestsPerPod = 1
)
```

    
  

    
      View Source
      

```
const (
	ErrorUnsupportedType = iota
	ErrorInvalidValue
	ErrorInvalidObject
)
```

    
  

    
      View Source
      

```
const (
	ANNOTATION_SVC_HOST = "svcHost"
)
```

    
  

    
      View Source
      

```
const (
	ArchiveLiteralSizeLimit int64 = 256 * 1024
)
```

    
  

    
      View Source
      

```
const (
	BuilderContainerName = "builder"
)
```

    
  

    
      View Source
      

```
const (
	DefaultSpecializationTimeOut = 120
)
```

    
  

    
      View Source
      

```
const (
	MessageQueueTypeKafka = "kafka"
)
```

    
  

    
      View Source
      

```
const (
	// ResourceVersionCount env variable is used for updating configmaps and secrets in pods
	ResourceVersionCount string = "RESOURCE_VERSION_COUNT"
)
```

    
  

    
      View Source
      

```
const (
	StrategyTypeExecution = "execution"
)
```

    
  

  
### Variables ¶

  
    
      View Source
      

```
var (
	// GroupVersion is group version used to register these objects
	SchemeGroupVersion = schema.GroupVersion{Group: "fission.io", Version: "v1"}

	// SchemeBuilder is used to add go types to the GroupVersionKind scheme
	SchemeBuilder = &scheme.Builder{GroupVersion: SchemeGroupVersion}

	// AddToScheme adds the types in this group-version to the given scheme.
	AddToScheme = SchemeBuilder.AddToScheme
)
```

    
  

    
      View Source
      

```
var (
	MinimumKubernetesVersion = [3]int{1, 19, 0}
)
```

    
  

  
### Functions ¶

  
	  
  
  
    
#### 
      func AggregateValidationErrors ¶
  
    
  

    
    
      

```
func AggregateValidationErrors(objName string, err error) error
```