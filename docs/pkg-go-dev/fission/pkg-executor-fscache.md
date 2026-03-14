### Index ¶

- Constants

- 
        func GetAttributesForFuncSvc(fsvc *FuncSvc) []attribute.KeyValue

- 
        func IsNameExistError(err error) bool

- 
        func IsNotFoundError(err error) bool

- 
        func NewFuncSvcGroup() *funcSvcGroup

- 
          type FuncSvc

- 
          type FunctionServiceCache

- 

  - 
            func MakeFunctionServiceCache(logger *zap.Logger) *FunctionServiceCache

- 

  - 
            func (fsc *FunctionServiceCache) Add(fsvc FuncSvc) (*FuncSvc, error)

  - 
            func (fsc *FunctionServiceCache) AddFunc(ctx context.Context, fsvc FuncSvc, requestsPerPod, svcsRetain int)

  - 
            func (fsc *FunctionServiceCache) DeleteEntry(fsvc *FuncSvc)

  - 
            func (fsc *FunctionServiceCache) DeleteFunctionSvc(ctx context.Context, fsvc *FuncSvc)

  - 
            func (fsc *FunctionServiceCache) DeleteOld(fsvc *FuncSvc, minAge time.Duration) (bool, error)

  - 
            func (fsc *FunctionServiceCache) DeleteOldPoolCache(ctx context.Context, fsvc *FuncSvc, minAge time.Duration) (bool, error)

  - 
            func (fsc *FunctionServiceCache) DumpDebugInfo(ctx context.Context) error

  - 
            func (fsc *FunctionServiceCache) GetByFunction(m *metav1.ObjectMeta) (*FuncSvc, error)

  - 
            func (fsc *FunctionServiceCache) GetByFunctionUID(uid types.UID) (*FuncSvc, error)

  - 
            func (fsc *FunctionServiceCache) GetFuncSvc(ctx context.Context, m *metav1.ObjectMeta, requestsPerPod int, concurrency int) (*FuncSvc, error)

  - 
            func (fsc *FunctionServiceCache) ListOld(age time.Duration) ([]*FuncSvc, error)

  - 
            func (fsc *FunctionServiceCache) ListOldForPool(age time.Duration) ([]*FuncSvc, error)

  - 
            func (fsc *FunctionServiceCache) Log()

  - 
            func (fsc *FunctionServiceCache) MarkAvailable(key crd.CacheKeyURG, svcHost string)

  - 
            func (fsc *FunctionServiceCache) MarkFuncDeleted(key crd.CacheKeyURG)

  - 
            func (fsc *FunctionServiceCache) MarkSpecializationFailure(key crd.CacheKeyURG)

  - 
            func (fsc *FunctionServiceCache) SetCPUUtilizaton(key crd.CacheKeyURG, svcHost string, cpuUsage resource.Quantity)

  - 
            func (fsc *FunctionServiceCache) TouchByAddress(address string) error

- 
          type PoolCache

- 

  - 
            func NewPoolCache(logger *zap.Logger) *PoolCache

- 

  - 
            func (c *PoolCache) DeleteValue(ctx context.Context, function crd.CacheKeyURG, address string) error

  - 
            func (c *PoolCache) GetSvcValue(ctx context.Context, function crd.CacheKeyURG, requestsPerPod int, ...) (*FuncSvc, error)

  - 
            func (c *PoolCache) ListAvailableValue() []*FuncSvc

  - 
            func (c *PoolCache) LogFnSvcGroup(ctx context.Context, file io.Writer) error

  - 
            func (c *PoolCache) MarkAvailable(function crd.CacheKeyURG, address string)

  - 
            func (c *PoolCache) MarkFuncDeleted(function crd.CacheKeyURG)

  - 
            func (c *PoolCache) MarkSpecializationFailure(function crd.CacheKeyURG)

  - 
            func (c *PoolCache) SetCPUUtilization(function crd.CacheKeyURG, address string, cpuUsage resource.Quantity)

  - 
            func (c *PoolCache) SetSvcValue(ctx context.Context, function crd.CacheKeyURG, address string, value *FuncSvc, ...)

- 
          type Queue

- 

  - 
            func NewQueue() *Queue

- 

  - 
            func (q *Queue) Expired() int

  - 
            func (q *Queue) Len() int

  - 
            func (q *Queue) Pop() *svcWait

  - 
            func (q *Queue) Push(item *svcWait)

### Constants ¶

  
    
      View Source
      

```
const (
	TOUCH fscRequestType = iota
	LISTOLD
	LOG
	LISTOLDPOOL
)
```

    
  

FunctionServiceCache Request Types

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func GetAttributesForFuncSvc ¶
  
    
      added in
      v1.15.0
    
  

    
    
      

```
func GetAttributesForFuncSvc(fsvc *FuncSvc) []attribute.KeyValue
```