### Index ¶

- 
          type ExecutorType

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type ExecutorType ¶
  
    
  

    
    
      

```
type ExecutorType interface {
	// Run runs background job.
	Run(context.Context, manager.Interface)

	// GetTypeName returns the name of executor type
	GetTypeName(context.Context) fv1.ExecutorType

	// GetFuncSvc specializes function pod(s) and returns a service URL for the function.
	GetFuncSvc(context.Context, *fv1.Function) (*fscache.FuncSvc, error)

	// GetFuncSvcFromCache retrieves function service from cache.
	GetFuncSvcFromCache(context.Context, *fv1.Function) (*fscache.FuncSvc, error)

	// DumpDebugInfo dump function service cache to temporary directory of executor pod.
	DumpDebugInfo(context.Context) error

	// DeleteFuncSvcFromCache deletes function service entry in cache.
	DeleteFuncSvcFromCache(context.Context, *fscache.FuncSvc)

	// TapService updates the access time of function service entry to
	// avoid idle pod reaper recycles pods.
	TapService(ctx context.Context, serviceUrl string) error

	// UnTapService updates the isActive to false
	UnTapService(ctx context.Context, fnMeta *metav1.ObjectMeta, svcHost string)

	// ReduceSpecializationInProgress updates the svcWaiting count in funcSvcGroup
	MarkSpecializationFailure(ctx context.Context, fnMeta *metav1.ObjectMeta)

	// IsValid returns true if a function service is valid. Different executor types
	// use distinct ways to examine the function service.
	IsValid(context.Context, *fscache.FuncSvc) bool

	// RefreshFuncPods refreshes function pods if the secrets/configmaps pods reference to get updated.
	RefreshFuncPods(context.Context, *zap.Logger, fv1.Function) error

	// AdoptOrphanResources adopts existing resources created by the deleted executor.
	AdoptExistingResources(context.Context)

	// CleanupOldExecutorObjects cleans up resources created by old executor instances
	CleanupOldExecutorObjects(context.Context)
}
```