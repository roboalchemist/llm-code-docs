### Overview ¶

Copyright 2019 The Fission Authors.

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
        func DownloadStrorageURL(ctx context.Context, client cmd.Client, fileUrl string) (io.ReadCloser, error)

- 
        func DownloadToTempFile(fileUrl string) (string, error)

- 
        func DownloadURL(fileUrl string) (io.ReadCloser, error)

- 
        func GetContents(filePath string) ([]byte, error)

- 
        func PrintPackageSummary(writer io.Writer, pkg *fv1.Package)

- 
        func UploadArchiveFile(ctx context.Context, client cmd.Client, fileName string) (*fv1.Archive, error)

- 
        func WriteArchiveToFile(fileName string, reader io.Reader) error

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func DownloadStrorageURL ¶
  
    
      added in
      v1.18.0
    
  

    
    
      

```
func DownloadStrorageURL(ctx context.Context, client cmd.Client, fileUrl string) (io.ReadCloser, error)
```