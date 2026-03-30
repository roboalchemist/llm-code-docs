### Index ¶

- 
        func MakeContainer(ctx context.Context, logger *zap.Logger, fissionClient versioned.Interface, ...) (executortype.ExecutorType, error)

- 
          type Container

- 

  - 
            func (caaf *Container) AdoptExistingResources(ctx context.Context)

  - 
            func (caaf *Container) CleanupOldExecutorObjects(ctx context.Context)

  - 
            func (caaf *Container) DeleteFuncSvcFromCache(ctx context.Context, fsvc *fscache.FuncSvc)

  - 
            func (caaf *Container) DumpDebugInfo(ctx context.Context) error

  - 
            func (caaf *Container) FuncInformerHandler(ctx context.Context) k8sCache.ResourceEventHandlerFuncs

  - 
            func (caaf *Container) GetFuncSvc(ctx context.Context, fn *fv1.Function) (*fscache.FuncSvc, error)

  - 
            func (caaf *Container) GetFuncSvcFromCache(ctx context.Context, fn *fv1.Function) (*fscache.FuncSvc, error)

  - 
            func (caaf *Container) GetTotalAvailable(fn *fv1.Function) int

  - 
            func (caaf *Container) GetTypeName(ctx context.Context) fv1.ExecutorType

  - 
            func (caaf *Container) IsValid(ctx context.Context, fsvc *fscache.FuncSvc) bool

  - 
            func (caaf *Container) MarkSpecializationFailure(ctx context.Context, fnMeta *metav1.ObjectMeta)

  - 
            func (caaf *Container) RefreshFuncPods(ctx context.Context, logger *zap.Logger, f fv1.Function) error

  - 
            func (caaf *Container) Run(ctx context.Context, mgr manager.Interface)

  - 
            func (caaf *Container) TapService(ctx context.Context, svcHost string) error

  - 
            func (caaf *Container) UnTapService(ctx context.Context, fnMeta *metav1.ObjectMeta, svcHost string)

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func MakeContainer ¶
  
    
  

    
    
      

```
func MakeContainer(
	ctx context.Context,
	logger *zap.Logger,
	fissionClient versioned.Interface,
	kubernetesClient kubernetes.Interface,
	instanceID string,
	finformerFactory map[string]genInformer.SharedInformerFactory,
	cnmInformerFactory map[string]k8sInformers.SharedInformerFactory,
) (executortype.ExecutorType, error)
```

    
  

MakeContainer initializes and returns an instance of CaaF

  

        

  
### Types ¶

  
      
  
  
    
#### 
      type Container ¶
  
    
  

    
    
      

```
type Container struct {
	// contains filtered or unexported fields
}
```

    
  

Container represents an executor type

    
  
  
    
#### 
      func (*Container) AdoptExistingResources ¶
  
    
  

    
    
      

```
func (caaf *Container) AdoptExistingResources(ctx context.Context)
```

    
  

AdoptExistingResources attempts to adopt resources for functions in all namespaces.

  

  
    
  
  
    
#### 
      func (*Container) CleanupOldExecutorObjects ¶
  
    
  

    
    
      

```
func (caaf *Container) CleanupOldExecutorObjects(ctx context.Context)
```

    
  

CleanupOldExecutorObjects cleans orphaned resources.

  

  
    
  
  
    
#### 
      func (*Container) DeleteFuncSvcFromCache ¶
  
    
  

    
    
      

```
func (caaf *Container) DeleteFuncSvcFromCache(ctx context.Context, fsvc *fscache.FuncSvc)
```

    
  

DeleteFuncSvcFromCache deletes a function service from cache.

  

  
    
  
  
    
#### 
      func (*Container) DumpDebugInfo ¶
  
    
      added in
      v1.19.0
    
  

    
    
      

```
func (caaf *Container) DumpDebugInfo(ctx context.Context) error
```