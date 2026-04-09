### Index ¶

- 
        func Commands() *cobra.Command

- 
        func Create(input cli.Input) error

- 
        func CreateArchive(client cmd.Client, input cli.Input, includeFiles []string, noZip bool, ...) (*fv1.Archive, error)

- 
        func CreatePackage(input cli.Input, client cmd.Client, pkgName string, pkgNamespace string, ...) (*metav1.ObjectMeta, error)

- 
        func Delete(input cli.Input) error

- 
        func GetDeploy(input cli.Input) error

- 
        func GetFunctionsByPackage(ctx context.Context, client cmd.Client, pkgName, pkgNamespace string) ([]fv1.Function, error)

- 
        func GetSrc(input cli.Input) error

- 
        func Info(input cli.Input) error

- 
        func List(input cli.Input) error

- 
        func Rebuild(input cli.Input) error

- 
        func Update(input cli.Input) error

- 
        func UpdateFunctionPackageResourceVersion(ctx context.Context, client cmd.Client, pkgMeta *metav1.ObjectMeta, ...) error

- 
        func UpdatePackage(input cli.Input, client cmd.Client, specFile string, pkg *fv1.Package) (*metav1.ObjectMeta, error)

- 
          type CreateSubCommand

- 
          type DeleteSubCommand

- 
          type GetSubCommand

- 
          type InfoSubCommand

- 
          type ListSubCommand

- 
          type RebuildSubCommand

- 
          type UpdateSubCommand

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func Commands ¶
  
    
  

    
    
      

```
func Commands() *cobra.Command
```