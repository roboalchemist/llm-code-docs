### Index ¶

- 
          type ClientInterface

- 

  - 
            func MakeClient(logger *zap.Logger, executorURL string) ClientInterface

- 
          type TapServiceRequest

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type ClientInterface ¶
  
    
      added in
      v1.20.0
    
  

    
    
      

```
type ClientInterface interface {
	GetServiceForFunction(ctx context.Context, fn *fv1.Function) (string, error)
	TapService(fnMeta metav1.ObjectMeta, executorType fv1.ExecutorType, serviceURL url.URL)
	UnTapService(ctx context.Context, fnMeta metav1.ObjectMeta, executorType fv1.ExecutorType, serviceURL *url.URL) error
}
```

    
  

ClientInterface is the interface for executor client.

    
  
  
    
#### 
      func MakeClient ¶
  
    
  

    
    
      

```
func MakeClient(logger *zap.Logger, executorURL string) ClientInterface
```

    
  

MakeClient initializes and returns a Client instance.