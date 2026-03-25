### Index ¶

- Constants

- 
        func Start(ctx context.Context, clientGen crd.ClientGeneratorInterface, ...) error

### Constants ¶

  
    
      View Source
      

```
const (
	LABEL_ENV_NAME            = "envName"
	LABEL_ENV_NAMESPACE       = "envNamespace"
	LABEL_ENV_RESOURCEVERSION = "envResourceVersion"
	LABEL_DEPLOYMENT_OWNER    = "owner"
	BUILDER_MGR               = "buildermgr"
)
```

    
  

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func Start ¶
  
    
  

    
    
      

```
func Start(ctx context.Context, clientGen crd.ClientGeneratorInterface, logger *zap.Logger, mgr manager.Interface, storageSvcUrl string) error
```

    
  

Start the buildermgr service.

  

        

  
### Types ¶

  

This section is empty.