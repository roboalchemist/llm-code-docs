### Index ¶

- 
        func ConvertMap2String(meta map[string]string) string

- 
        func ConvertMeta2Map(meta string) map[string]string

- 
        func CopyMeta(src, dst map[string]string)

- 
        func ExternalIPV4() (string, error)

- 
        func ExternalIPV6() (string, error)

- 
        func GetFreePort() (port int, err error)

- 
        func ParseRpcxAddress(addr string) (network string, ip string, port int, err error)

- 
        func SliceByteToString(b []byte) string

- 
        func StringToSliceByte(s string) []byte

- 
        func Unzip(data []byte) ([]byte, error)

- 
        func Zip(data []byte) ([]byte, error)

- 
          type LimitedPool

- 

  - 
            func NewLimitedPool(minSize, maxSize int) *LimitedPool

- 

  - 
            func (p *LimitedPool) Get(size int) *[]byte

  - 
            func (p *LimitedPool) Put(b *[]byte)

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func ConvertMap2String ¶
  
    
      added in
      v1.6.2
    
  

    
    
      

```
func ConvertMap2String(meta map[string]string) string
```