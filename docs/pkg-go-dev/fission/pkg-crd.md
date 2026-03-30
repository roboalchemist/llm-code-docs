### Index ¶

- Constants

- 
        func CacheKeyUIDFromMeta(metadata *metav1.ObjectMeta) types.UID

- 
        func EnsureFissionCRDs(ctx context.Context, logger *zap.Logger, ...) error

- 
        func WaitForFunctionCRDs(ctx context.Context, logger *zap.Logger, fissionClient versioned.Interface) error

- 
          type CacheKeyUR

- 

  - 
            func CacheKeyURFromMeta(metadata *metav1.ObjectMeta) CacheKeyUR

  - 
            func CacheKeyURFromObject(obj metav1.Object) CacheKeyUR

- 

  - 
            func (ck CacheKeyUR) String() string

- 
          type CacheKeyURG

- 

  - 
            func CacheKeyURGFromMeta(metadata *metav1.ObjectMeta) CacheKeyURG

- 

  - 
            func (ck CacheKeyURG) String() string

- 
          type ClientGenerator

- 

  - 
            func NewClientGenerator() *ClientGenerator

  - 
            func NewClientGeneratorWithRestConfig(restConfig *rest.Config) *ClientGenerator

- 

  - 
            func (cg *ClientGenerator) GetApiExtensionsClient() (apiextensionsclient.Interface, error)

  - 
            func (cg *ClientGenerator) GetFissionClient() (versioned.Interface, error)

  - 
            func (cg *ClientGenerator) GetKedaClient() (kedaClient.Interface, error)

  - 
            func (cg *ClientGenerator) GetKubernetesClient() (kubernetes.Interface, error)

  - 
            func (cg *ClientGenerator) GetMetricsClient() (metricsclient.Interface, error)

  - 
            func (cg *ClientGenerator) GetRestConfig() (*rest.Config, error)

- 
          type ClientGeneratorInterface

### Constants ¶

  
    
      View Source
      

```
const (
	EnvKubeClientQps   = "KUBE_CLIENT_QPS"
	EnvKubeClientBurst = "KUBE_CLIENT_BURST"
)
```

    
  

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func CacheKeyUIDFromMeta ¶
  
    
      added in
      v1.20.0
    
  

    
    
      

```
func CacheKeyUIDFromMeta(metadata *metav1.ObjectMeta) types.UID
```

    
  

CacheKeyUIDFromMeta create a key that uniquely identifies the
of the object. Since resourceVersion changes on every update and
UIDs are unique, we don't use resource version here

  

        
	  
  
  
    
#### 
      func EnsureFissionCRDs ¶
  
    
  

    
    
      

```
func EnsureFissionCRDs(ctx context.Context, logger *zap.Logger, clientset apiextensionsclient.Interface) error
```

    
  

EnsureFissionCRDs checks if all Fission CRDs are present

  

        
	  
  
  
    
#### 
      func WaitForFunctionCRDs ¶
  
    
      added in
      v1.20.0
    
  

    
    
      

```
func WaitForFunctionCRDs(ctx context.Context, logger *zap.Logger, fissionClient versioned.Interface) error
```

    
  

WaitForFunctionCRDs does a timeout to check if CRDs have been installed

  

        

  
### Types ¶

  
      
  
  
    
#### 
      type CacheKeyUR ¶
  
    
      added in
      v1.20.0
    
  

    
    
      

```
type CacheKeyUR struct {
	UID             types.UID
	ResourceVersion string
}
```

    
  

    
  
  
    
#### 
      func CacheKeyURFromMeta ¶
  
    
      added in
      v1.20.0
    
  

    
    
      

```
func CacheKeyURFromMeta(metadata *metav1.ObjectMeta) CacheKeyUR
```

    
  

CacheKeyURFromMeta : Given metadata, create a key that uniquely identifies the contents
of the object. Since resourceVersion changes on every update and
UIDs are unique, uid+resourceVersion identifies the
content. (ResourceVersion may also update on status updates, so
this will result in some unnecessary cache misses. That should be
ok.)

  

  
    
  
  
    
#### 
      func CacheKeyURFromObject ¶
  
    
      added in
      v1.20.0
    
  

    
    
      

```
func CacheKeyURFromObject(obj metav1.Object) CacheKeyUR
```