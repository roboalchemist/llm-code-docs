### Index ¶

- Constants

- Variables

- 
        func FreeMsg(msg *Message)

- 
        func MagicNumber() byte

- 
        func PutData(data *[]byte)

- 
          type CompressType

- 
          type Compressor

- 
          type GzipCompressor

- 

  - 
            func (c GzipCompressor) Unzip(data []byte) ([]byte, error)

  - 
            func (c GzipCompressor) Zip(data []byte) ([]byte, error)

- 
          type Header

- 

  - 
            func (h Header) CheckMagicNumber() bool

  - 
            func (h Header) CompressType() CompressType

  - 
            func (h Header) IsHeartbeat() bool

  - 
            func (h Header) IsOneway() bool

  - 
            func (h Header) MessageStatusType() MessageStatusType

  - 
            func (h Header) MessageType() MessageType

  - 
            func (h Header) Seq() uint64

  - 
            func (h Header) SerializeType() SerializeType

  - 
            func (h *Header) SetCompressType(ct CompressType)

  - 
            func (h *Header) SetHeartbeat(hb bool)

  - 
            func (h *Header) SetMessageStatusType(mt MessageStatusType)

  - 
            func (h *Header) SetMessageType(mt MessageType)

  - 
            func (h *Header) SetOneway(oneway bool)

  - 
            func (h *Header) SetSeq(seq uint64)

  - 
            func (h *Header) SetSerializeType(st SerializeType)

  - 
            func (h *Header) SetVersion(v byte)

  - 
            func (h Header) Version() byte

- 
          type Message

- 

  - 
            func GetPooledMsg() *Message

  - 
            func NewMessage() *Message

  - 
            func Read(r io.Reader) (*Message, error)

- 

  - 
            func (m Message) Clone() *Message

  - 
            func (m *Message) Decode(r io.Reader) error

  - 
            func (m Message) Encode() []byte

  - 
            func (m Message) EncodeSlicePointer() *[]byte

  - 
            func (m *Message) Reset()

  - 
            func (m Message) WriteTo(w io.Writer) (int64, error)

- 
          type MessageStatusType

- 
          type MessageType

- 
          type RawDataCompressor

- 

  - 
            func (c RawDataCompressor) Unzip(data []byte) ([]byte, error)

  - 
            func (c RawDataCompressor) Zip(data []byte) ([]byte, error)

- 
          type SerializeType

- 
          type SnappyCompressor

- 

  - 
            func (c *SnappyCompressor) Unzip(data []byte) ([]byte, error)

  - 
            func (c *SnappyCompressor) Zip(data []byte) ([]byte, error)

### Constants ¶

  
    
      View Source
      

```
const (
	// ServiceError contains error info of service invocation
	ServiceError = "__rpcx_error__"
)
```

    
  

  
### Variables ¶

  
    
      View Source
      

```
var (
	// ErrMetaKVMissing some keys or values are missing.
	ErrMetaKVMissing = errors.New("wrong metadata lines. some keys or values are missing")
	// ErrMessageTooLong message is too long
	ErrMessageTooLong = errors.New("message is too long")

	ErrUnsupportedCompressor = errors.New("unsupported compressor")
)
```

    
  

    
      View Source
      

```
var (
	// Compressors are compressors supported by rpcx. You can add customized compressor in Compressors.
	Compressors = map[CompressType]Compressor{
		None: &RawDataCompressor{},
		Gzip: &GzipCompressor{},
	}
)
```

    
  

    
      View Source
      

```
var MaxMessageLength = 0
```

    
  

MaxMessageLength is the max length of a message.
Default is 0 that means does not limit length of messages.
It is used to validate when read messages from io.Reader.

  
### Functions ¶

  
	  
  
  
    
#### 
      func FreeMsg ¶
  
    
  

    
    
      

```
func FreeMsg(msg *Message)
```

    
  

FreeMsg puts a msg into the pool.

  

        
	  
  
  
    
#### 
      func MagicNumber ¶
  
    
  

    
    
      

```
func MagicNumber() byte
```