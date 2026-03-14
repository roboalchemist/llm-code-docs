### Index ¶

- 
        func StartExecutor(ctx context.Context, clientGen crd.ClientGeneratorInterface, ...) error

- 
          type Executor

- 

  - 
            func MakeExecutor(ctx context.Context, logger *zap.Logger, mgr manager.Interface, ...) (*Executor, error)

- 

  - 
            func (executor *Executor) GetHandler() http.Handler

  - 
            func (executor *Executor) Serve(ctx context.Context, mgr manager.Interface, port int)

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func StartExecutor ¶
  
    
  

    
    
      

```
func StartExecutor(ctx context.Context, clientGen crd.ClientGeneratorInterface, logger *zap.Logger, mgr manager.Interface, port int) error
```

    
  

StartExecutor Starts executor and the executor components such as Poolmgr,
deploymgr and potential future executor types

  

        

  
### Types ¶

  
      
  
  
    
#### 
      type Executor ¶
  
    
  

    
    
      

```
type Executor struct {
	// contains filtered or unexported fields
}
```

    
  

Executor defines a fission function executor.

    
  
  
    
#### 
      func MakeExecutor ¶
  
    
  

    
    
      

```
func MakeExecutor(ctx context.Context, logger *zap.Logger, mgr manager.Interface, cms *cms.ConfigSecretController,
	fissionClient versioned.Interface, types map[fv1.ExecutorType]executortype.ExecutorType,
	informers ...k8sCache.SharedIndexInformer) (*Executor, error)
```

    
  

MakeExecutor returns an Executor for given ExecutorType(s).

  

  
    
  
  
    
#### 
      func (*Executor) GetHandler ¶
  
    
      added in
      v1.7.0
    
  

    
    
      

```
func (executor *Executor) GetHandler() http.Handler
```

    
  

GetHandler returns an http.Handler.

  

  
    
  
  
    
#### 
      func (*Executor) Serve ¶
  
    
  

    
    
      

```
func (executor *Executor) Serve(ctx context.Context, mgr manager.Interface, port int)
```

    
  

Serve starts an HTTP server.