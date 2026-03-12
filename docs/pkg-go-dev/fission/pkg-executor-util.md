### Index ¶

- 
        func ApplyImagePullSecret(secret string, podspec apiv1.PodSpec) *apiv1.PodSpec

- 
        func ConvertConfigSecrets(ctx context.Context, fn *fv1.Function, kc kubernetes.Interface) ([]apiv1.EnvFromSource, error)

- 
        func CreateDumpFile(logger *zap.Logger) (*os.File, error)

- 
        func DoesContainerExistInPodSpec(containerName string, podSpec *apiv1.PodSpec) bool

- 
        func GetObjectReaperInterval(logger *zap.Logger, executorType fv1.ExecutorType, defaultReaperInterval uint) uint

- 
        func GetSpecFromConfigMap(filePath string) (*apiv1.PodSpec, error)

- 
        func MergeContainer(dst *apiv1.Container, src *apiv1.Container) (*apiv1.Container, error)

- 
        func MergePodSpec(srcPodSpec *apiv1.PodSpec, targetPodSpec *apiv1.PodSpec) (*apiv1.PodSpec, error)

- 
        func WaitTimeout(wg *sync.WaitGroup, timeout time.Duration)

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func ApplyImagePullSecret ¶
  
    
      added in
      v1.7.0
    
  

    
    
      

```
func ApplyImagePullSecret(secret string, podspec apiv1.PodSpec) *apiv1.PodSpec
```

    
  

ApplyImagePullSecret applies image pull secret to the give pod spec.
It's intentional not to check the existence of secret here.
First, Kubernetes will set Pod status to "ImagePullBackOff" once
kubelet failed to pull image so that users will know what's happening.
Second, Fission no longer need to handle "secret not found" error
when creating the environment deployment since kubelet will retry to
pull image until successes.

  

        
	  
  
  
    
#### 
      func ConvertConfigSecrets ¶
  
    
      added in
      v1.14.1
    
  

    
    
      

```
func ConvertConfigSecrets(ctx context.Context, fn *fv1.Function, kc kubernetes.Interface) ([]apiv1.EnvFromSource, error)
```

    
  

ConvertConfigSecrets returns envFromSource which can be passed directly into the pod spec

  

        
	  
  
  
    
#### 
      func CreateDumpFile ¶
  
    
      added in
      v1.19.0
    
  

    
    
      

```
func CreateDumpFile(logger *zap.Logger) (*os.File, error)
```

    
  

CreateDumpFile => create dump file inside temp directory

  

        
	  
  
  
    
#### 
      func DoesContainerExistInPodSpec ¶
  
    
      added in
      v1.21.0
    
  

    
    
      

```
func DoesContainerExistInPodSpec(containerName string, podSpec *apiv1.PodSpec) bool
```

    
  

DoesContainerExistInPodSpec checks if the container with the given name exists in the pod spec

  

        
	  
  
  
    
#### 
      func GetObjectReaperInterval ¶
  
    
      added in
      v1.18.0
    
  

    
    
      

```
func GetObjectReaperInterval(logger *zap.Logger, executorType fv1.ExecutorType, defaultReaperInterval uint) uint
```