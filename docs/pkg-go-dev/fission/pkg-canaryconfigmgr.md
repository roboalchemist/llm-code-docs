### Index ¶

- 
        func ConfigureFeatures(ctx context.Context, logger *zap.Logger, unitTestMode bool, ...) error

- 
        func MakeCanaryConfigMgr(ctx context.Context, logger *zap.Logger, fissionClient versioned.Interface, ...) (*canaryConfigMgr, error)

- 
        func StartCanaryServer(ctx context.Context, clientGen crd.ClientGeneratorInterface, ...) error

- 
          type CanaryProcessingInfo

- 
          type PrometheusApiClient

- 

  - 
            func MakePrometheusClient(logger *zap.Logger, prometheusSvc string) (*PrometheusApiClient, error)

- 

  - 
            func (promApiClient *PrometheusApiClient) GetFunctionFailurePercentage(ctx context.Context, path string, methods []string, funcName, funcNs string, ...) (float64, error)

  - 
            func (promApiClient *PrometheusApiClient) GetRequestsToFuncInWindow(ctx context.Context, path string, method string, funcName string, ...) (float64, error)

  - 
            func (promApiClient *PrometheusApiClient) GetTotalFailedRequestsToFuncInWindow(ctx context.Context, funcName string, funcNs string, path string, ...) (float64, error)

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func ConfigureFeatures ¶
  
    
      added in
      v1.18.0
    
  

    
    
      

```
func ConfigureFeatures(ctx context.Context, logger *zap.Logger, unitTestMode bool, fissionClient versioned.Interface,
	kubeClient kubernetes.Interface, mgr manager.Interface) error
```

    
  

ConfigureFeatures gets the feature config and configures the features that are enabled

  

        
	  
  
  
    
#### 
      func MakeCanaryConfigMgr ¶
  
    
  

    
    
      

```
func MakeCanaryConfigMgr(ctx context.Context, logger *zap.Logger, fissionClient versioned.Interface, kubeClient kubernetes.Interface, prometheusSvc string) (*canaryConfigMgr, error)
```