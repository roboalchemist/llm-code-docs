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

- 
        func MakeNewDeploy(ctx context.Context, logger *zap.Logger, fissionClient versioned.Interface, ...) (executortype.ExecutorType, error)

- 
          type NewDeploy

- 

  - 
            func (deploy *NewDeploy) AdoptExistingResources(ctx context.Context)

  - 
            func (deploy *NewDeploy) CleanupOldExecutorObjects(ctx context.Context)

  - 
            func (deploy *NewDeploy) DeleteFuncSvcFromCache(ctx context.Context, fsvc *fscache.FuncSvc)

  - 
            func (deploy *NewDeploy) DumpDebugInfo(ctx context.Context) error

  - 
            func (deploy *NewDeploy) EnvEventHandlers(ctx context.Context) k8sCache.ResourceEventHandlerFuncs

  - 
            func (deploy *NewDeploy) FunctionEventHandlers(ctx context.Context) k8sCache.ResourceEventHandlerFuncs

  - 
            func (deploy *NewDeploy) GetFuncSvc(ctx context.Context, fn *fv1.Function) (*fscache.FuncSvc, error)

  - 
            func (deploy *NewDeploy) GetFuncSvcFromCache(ctx context.Context, fn *fv1.Function) (*fscache.FuncSvc, error)

  - 
            func (deploy *NewDeploy) GetTypeName(ctx context.Context) fv1.ExecutorType

  - 
            func (deploy *NewDeploy) IsValid(ctx context.Context, fsvc *fscache.FuncSvc) bool

  - 
            func (deploy *NewDeploy) MarkSpecializationFailure(ctx context.Context, fnMeta *metav1.ObjectMeta)

  - 
            func (deploy *NewDeploy) RefreshFuncPods(ctx context.Context, logger *zap.Logger, f fv1.Function) error

  - 
            func (deploy *NewDeploy) Run(ctx context.Context, mgr manager.Interface)

  - 
            func (deploy *NewDeploy) TapService(ctx context.Context, svcHost string) error

  - 
            func (deploy *NewDeploy) UnTapService(ctx context.Context, fnMeta *metav1.ObjectMeta, svcHost string)

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func MakeNewDeploy ¶
  
    
  

    
    
      

```
func MakeNewDeploy(
	ctx context.Context,
	logger *zap.Logger,
	fissionClient versioned.Interface,
	kubernetesClient kubernetes.Interface,
	fetcherConfig *fetcherConfig.Config,
	instanceID string,
	finformerFactory map[string]genInformer.SharedInformerFactory,
	ndmInformerFactory map[string]k8sInformers.SharedInformerFactory,
	podSpecPatch *apiv1.PodSpec,
) (executortype.ExecutorType, error)
```

    
  

MakeNewDeploy initializes and returns an instance of NewDeploy.

  

        

  
### Types ¶

  
      
  
  
    
#### 
      type NewDeploy ¶
  
    
  

    
    
      

```
type NewDeploy struct {
	// contains filtered or unexported fields
}
```

    
  

NewDeploy represents an ExecutorType

    
  
  
    
#### 
      func (*NewDeploy) AdoptExistingResources ¶
  
    
  

    
    
      

```
func (deploy *NewDeploy) AdoptExistingResources(ctx context.Context)
```

    
  

AdoptExistingResources attempts to adopt resources for functions in all namespaces.

  

  
    
  
  
    
#### 
      func (*NewDeploy) CleanupOldExecutorObjects ¶
  
    
  

    
    
      

```
func (deploy *NewDeploy) CleanupOldExecutorObjects(ctx context.Context)
```

    
  

CleanupOldExecutorObjects cleans orphaned resources.

  

  
    
  
  
    
#### 
      func (*NewDeploy) DeleteFuncSvcFromCache ¶
  
    
  

    
    
      

```
func (deploy *NewDeploy) DeleteFuncSvcFromCache(ctx context.Context, fsvc *fscache.FuncSvc)
```

    
  

DeleteFuncSvcFromCache deletes a function service from cache.

  

  
    
  
  
    
#### 
      func (*NewDeploy) DumpDebugInfo ¶
  
    
      added in
      v1.19.0
    
  

    
    
      

```
func (deploy *NewDeploy) DumpDebugInfo(ctx context.Context) error
```