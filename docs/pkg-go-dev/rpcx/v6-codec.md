### Index ¶

- 
          type ByteCodec

- 

  - 
            func (c ByteCodec) Decode(data []byte, i interface{}) error

  - 
            func (c ByteCodec) Encode(i interface{}) ([]byte, error)

- 
          type Codec

- 
          type JSONCodec

- 

  - 
            func (c JSONCodec) Decode(data []byte, i interface{}) error

  - 
            func (c JSONCodec) Encode(i interface{}) ([]byte, error)

- 
          type MsgpackCodec

- 

  - 
            func (c MsgpackCodec) Decode(data []byte, i interface{}) error

  - 
            func (c MsgpackCodec) Encode(i interface{}) ([]byte, error)

- 
          type PBCodec

- 

  - 
            func (c PBCodec) Decode(data []byte, i interface{}) error

  - 
            func (c PBCodec) Encode(i interface{}) ([]byte, error)

- 
          type ThriftCodec

- 

  - 
            func (c ThriftCodec) Decode(data []byte, i interface{}) error

  - 
            func (c ThriftCodec) Encode(i interface{}) ([]byte, error)

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type ByteCodec ¶
  
    
  

    
    
      

```
type ByteCodec struct{}
```

    
  

ByteCodec uses raw slice pf bytes and don't encode/decode.

    
  
  
    
#### 
      func (ByteCodec) Decode ¶
  
    
  

    
    
      

```
func (c ByteCodec) Decode(data []byte, i interface{}) error
```

    
  

Decode returns raw slice of bytes.

  

  
    
  
  
    
#### 
      func (ByteCodec) Encode ¶
  
    
  

    
    
      

```
func (c ByteCodec) Encode(i interface{}) ([]byte, error)
```

    
  

Encode returns raw slice of bytes.