### Overview ¶

Copyright 2021 The Fission Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

```
http://www.apache.org/licenses/LICENSE-2.0

```

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

    
### Index ¶

- Constants

- 
        func FunctionEventHandlers(ctx context.Context, logger *zap.Logger, kubernetesClient kubernetes.Interface, ...) k8sCache.ResourceEventHandlerFuncs

- 
        func IsIPv6(podIP string) bool

- 
        func IsPodActive(p *v1.Pod) bool

- 
        func MakeGenericPoolManager(ctx context.Context, logger *zap.Logger, fissionClient versioned.Interface, ...) (executortype.ExecutorType, error)

- 
          type GenericPool

- 

  - 
            func MakeGenericPool(logger *zap.Logger, fissionClient versioned.Interface, ...) *GenericPool

- 
          type GenericPoolManager

- 

  - 
            func (gpm *GenericPoolManager) AdoptExistingResources(ctx context.Context)

  - 
            func (gpm *GenericPoolManager) CleanupOldExecutorObjects(ctx context.Context)

  - 
            func (gpm *GenericPoolManager) DeleteFuncSvcFromCache(ctx context.Context, fsvc *fscache.FuncSvc)

  - 
            func (gpm *GenericPoolManager) DumpDebugInfo(ctx context.Context) error

  - 
            func (gpm *GenericPoolManager) GetFuncSvc(ctx context.Context, fn *fv1.Function) (fnSvc *fscache.FuncSvc, fErr error)

  - 
            func (gpm *GenericPoolManager) GetFuncSvcFromCache(ctx context.Context, fn *fv1.Function) (*fscache.FuncSvc, error)

  - 
            func (gpm *GenericPoolManager) GetTypeName(ctx context.Context) fv1.ExecutorType

  - 
            func (gpm *GenericPoolManager) IsValid(ctx context.Context, fsvc *fscache.FuncSvc) bool

  - 
            func (gpm *GenericPoolManager) MarkSpecializationFailure(ctx context.Context, fnMeta *metav1.ObjectMeta)

  - 
            func (gpm *GenericPoolManager) NoActiveConnectionEventChecker(ctx context.Context, kubeClient kubernetes.Interface) error

  - 
            func (gpm *GenericPoolManager) RefreshFuncPods(ctx context.Context, logger *zap.Logger, f fv1.Function) error

  - 
            func (gpm *GenericPoolManager) Run(ctx context.Context, mgr manager.Interface)

  - 
            func (gpm *GenericPoolManager) TapService(ctx context.Context, svcHost string) error

  - 
            func (gpm *GenericPoolManager) UnTapService(ctx context.Context, fnMeta *metav1.ObjectMeta, svcHost string)

  - 
            func (gpm *GenericPoolManager) WebsocketStartEventChecker(ctx context.Context, kubeClient kubernetes.Interface) error

- 
          type PoolPodController

- 

  - 
            func NewPoolPodController(ctx context.Context, logger *zap.Logger, kubernetesClient kubernetes.Interface, ...) (*PoolPodController, error)

- 

  - 
            func (p *PoolPodController) InjectGpm(gpm *GenericPoolManager)

  - 
            func (p *PoolPodController) Run(ctx context.Context, stopCh <-chan struct{}, mgr manager.Interface)

### Constants ¶

  
    
      View Source
      

```
const (
	GET_POOL requestType = iota
	CLEANUP_POOL
)
```

    
  

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func FunctionEventHandlers ¶
  
    
      added in
      v1.15.0
    
  

    
    
      

```
func FunctionEventHandlers(ctx context.Context, logger *zap.Logger, kubernetesClient kubernetes.Interface, fissionfnNamespace string, istioEnabled bool) k8sCache.ResourceEventHandlerFuncs
```

    
  

FunctionEventHandlers provides handlers for function resource events.
Based on function create/update/delete event, we create role binding
for the secret/configmap access which is used by fetcher component.
If istio is enabled, we create a service for the function.

  

        
	  
  
  
    
#### 
      func IsIPv6 ¶
  
    
  

    
    
      

```
func IsIPv6(podIP string) bool
```

    
  

IsIPv6 validates if the podIP follows to IPv6 protocol

  

        
	  
  
  
    
#### 
      func IsPodActive ¶
  
    
      added in
      v1.15.0
    
  

    
    
      

```
func IsPodActive(p *v1.Pod) bool
```