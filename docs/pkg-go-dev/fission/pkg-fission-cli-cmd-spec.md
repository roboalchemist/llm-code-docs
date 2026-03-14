### Index ¶

- Constants

- 
        func Apply(input cli.Input) error

- 
        func Commands() *cobra.Command

- 
        func Destroy(input cli.Input) error

- 
        func Init(input cli.Input) error

- 
        func List(input cli.Input) error

- 
        func ShowAppliedKubeWatchers(ws []fv1.KubernetesWatchTrigger)

- 
        func ShowCanaryConfigs(canaryCfgs []fv1.CanaryConfig)

- 
        func ShowEnvironments(envs []fv1.Environment)

- 
        func ShowFunctions(fns []fv1.Function)

- 
        func ShowHTTPTriggers(hts []fv1.HTTPTrigger)

- 
        func ShowMQTriggers(mqts []fv1.MessageQueueTrigger)

- 
        func ShowPackages(pkgList []fv1.Package)

- 
        func ShowTimeTriggers(tts []fv1.TimeTrigger)

- 
        func SpecDry(resource interface{}) error

- 
        func SpecSave(resource interface{}, specFile string, update bool) error

- 
        func Validate(input cli.Input) error

- 
          type ApplySubCommand

- 
          type DestroySubCommand

- 
          type FissionResources

- 

  - 
            func ReadSpecs(specDir, specIgnore string, applyCommitLabel bool) (*FissionResources, error)

- 

  - 
            func (fr *FissionResources) ExistsInSpecs(resource interface{}) (bool, error)

  - 
            func (fr *FissionResources) ParseYaml(b []byte, loc *Location, commitLabelVal string) error

  - 
            func (fr *FissionResources) SpecExists(resource interface{}, compareMetadata bool, compareSpec bool) interface{}

  - 
            func (fr *FissionResources) Validate(input cli.Input, client cmd.Client) ([]string, error)

- 
          type InitSubCommand

- 
          type ListSubCommand

- 
          type Location

- 

  - 
            func (loc Location) String() string

- 
          type ResourceApplyStatus

- 
          type SourceMap

- 
          type ValidateSubCommand

### Constants ¶

  
    
      View Source
      

```
const (
	FISSION_DEPLOYMENT_NAME_KEY = "fission-name"
	FISSION_DEPLOYMENT_UID_KEY  = "fission-uid"

	SPEC_API_VERSION          = "fission.io/v1"
	ARCHIVE_URL_PREFIX string = "archive://"
	SPEC_README               = `` /* 1789-byte string literal not displayed */

)
```

    
  

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func Apply ¶
  
    
      added in
      v1.7.0
    
  

    
    
      

```
func Apply(input cli.Input) error
```

    
  

Apply compares the specs in the spec/config/ directory to the
deployed resources on the cluster, and reconciles the differences
by creating, updating or deleting resources on the cluster.

Apply is idempotent.

Apply is *not* transactional -- if the user hits Ctrl-C, or their laptop dies
etc, while doing an apply, they will get a partially applied deployment.  However,
they can retry their apply command once they're back online.

  

        
	  
  
  
    
#### 
      func Commands ¶
  
    
      added in
      v1.7.0
    
  

    
    
      

```
func Commands() *cobra.Command
```