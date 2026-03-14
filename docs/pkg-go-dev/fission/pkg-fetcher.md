### Index ¶

- 
          type ArchiveUploadRequest

- 
          type ArchiveUploadResponse

- 
          type FetchRequestType

- 
          type Fetcher

- 

  - 
            func MakeFetcher(logger *zap.Logger, clientGen crd.ClientGeneratorInterface, ...) (*Fetcher, error)

- 

  - 
            func (fetcher *Fetcher) Fetch(ctx context.Context, pkg *fv1.Package, req FunctionFetchRequest) (int, error)

  - 
            func (fetcher *Fetcher) FetchHandler(w http.ResponseWriter, r *http.Request)

  - 
            func (fetcher *Fetcher) FetchSecretsAndCfgMaps(ctx context.Context, secrets []fv1.SecretReference, ...) (int, error)

  - 
            func (fetcher *Fetcher) SpecializeHandler(w http.ResponseWriter, r *http.Request)

  - 
            func (fetcher *Fetcher) SpecializePod(ctx context.Context, fetchReq FunctionFetchRequest, ...) error

  - 
            func (fetcher *Fetcher) UploadHandler(w http.ResponseWriter, r *http.Request)

  - 
            func (fetcher *Fetcher) VersionHandler(w http.ResponseWriter, r *http.Request)

  - 
            func (fetcher *Fetcher) WsEndHandler(w http.ResponseWriter, r *http.Request)

  - 
            func (fetcher *Fetcher) WsStartHandler(w http.ResponseWriter, r *http.Request)

- 
          type FunctionFetchRequest

- 
          type FunctionLoadRequest

- 
          type FunctionSpecializeRequest

- 
          type PodInfo

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type ArchiveUploadRequest ¶
  
    
      added in
      v1.8.0
    
  

    
    
      

```
type ArchiveUploadRequest struct {
	Filename       string `json:"filename"`
	StorageSvcUrl  string `json:"storagesvcurl"`
	ArchivePackage bool   `json:"archivepackage"`
}
```

    
  

ArchiveUploadRequest send from builder manager describes which
deployment package should be upload to storage service.

  

    
      
  
  
    
#### 
      type ArchiveUploadResponse ¶
  
    
      added in
      v1.8.0
    
  

    
    
      

```
type ArchiveUploadResponse struct {
	ArchiveDownloadUrl string       `json:"archiveDownloadUrl"`
	Checksum           fv1.Checksum `json:"checksum"`
}
```

    
  

ArchiveUploadResponse defines the download url of an archive and
its checksum.

  

    
      
  
  
    
#### 
      type FetchRequestType ¶
  
    
      added in
      v1.8.0
    
  

    
    
      

```
type FetchRequestType int
```

    
  

Fission-Environment interface. The following types are not
exposed in the Fission API, but rather used by Fission to
talk to environments.

  

    
      
  
  
    
#### 
      type Fetcher ¶
  
    
  

    
    
      

```
type Fetcher struct {
	Info PodInfo
	// contains filtered or unexported fields
}
```

    
  

    
  
  
    
#### 
      func MakeFetcher ¶
  
    
  

    
    
      

```
func MakeFetcher(logger *zap.Logger, clientGen crd.ClientGeneratorInterface, sharedVolumePath string, sharedSecretPath string,
	sharedConfigPath string, podInfoMountDir string) (*Fetcher, error)
```