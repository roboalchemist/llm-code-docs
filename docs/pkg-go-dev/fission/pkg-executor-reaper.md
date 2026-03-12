### Index ¶

- 
        func CleanupDeployments(ctx context.Context, logger *zap.Logger, client kubernetes.Interface, ...) error

- 
        func CleanupHpa(ctx context.Context, logger *zap.Logger, client kubernetes.Interface, ...) error

- 
        func CleanupKubeObject(ctx context.Context, logger *zap.Logger, kubeClient kubernetes.Interface, ...)

- 
        func CleanupPods(ctx context.Context, logger *zap.Logger, client kubernetes.Interface, ...) error

- 
        func CleanupServices(ctx context.Context, logger *zap.Logger, client kubernetes.Interface, ...) error

- 
        func GetReaperNamespace() map[string]string

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func CleanupDeployments ¶
  
    
      added in
      v1.7.0
    
  

    
    
      

```
func CleanupDeployments(ctx context.Context, logger *zap.Logger, client kubernetes.Interface, instanceID string, listOps metav1.ListOptions) error
```

    
  

CleanupDeployments deletes deployment(s) for a given instanceID

  

        
	  
  
  
    
#### 
      func CleanupHpa ¶
  
    
      added in
      v1.7.0
    
  

    
    
      

```
func CleanupHpa(ctx context.Context, logger *zap.Logger, client kubernetes.Interface, instanceID string, listOps metav1.ListOptions) error
```

    
  

CleanupHpa deletes horizontal pod autoscaler(s) for a given instanceID

  

        
	  
  
  
    
#### 
      func CleanupKubeObject ¶
  
    
  

    
    
      

```
func CleanupKubeObject(ctx context.Context, logger *zap.Logger, kubeClient kubernetes.Interface, kubeobj *apiv1.ObjectReference)
```

    
  

CleanupKubeObject deletes given kubernetes object

  

        
	  
  
  
    
#### 
      func CleanupPods ¶
  
    
      added in
      v1.7.0
    
  

    
    
      

```
func CleanupPods(ctx context.Context, logger *zap.Logger, client kubernetes.Interface, instanceID string, listOps metav1.ListOptions) error
```

    
  

CleanupPods deletes pod(s) for a given instanceID

  

        
	  
  
  
    
#### 
      func CleanupServices ¶
  
    
      added in
      v1.7.0
    
  

    
    
      

```
func CleanupServices(ctx context.Context, logger *zap.Logger, client kubernetes.Interface, instanceID string, listOps metav1.ListOptions) error
```

    
  

CleanupServices deletes service(s) for a given instanceID

  

        
	  
  
  
    
#### 
      func GetReaperNamespace ¶
  
    
      added in
      v1.18.0
    
  

    
    
      

```
func GetReaperNamespace() map[string]string
```