### Index ¶

- 
        func GoToValue(raw interface{}) (*proto.Value, error)

- 
        func ValueToGo(v *proto.Value, t reflect.Type) (interface{}, error)

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func GoToValue ¶
  
    
  

    
    
      

```
func GoToValue(raw interface{}) (*proto.Value, error)
```

    
  

GoToValue converts the Go value to a protobuf Object.

The Go value must contain only primitives, collections of primitives,
and structures. It must not contain any other type of value or an error
will be returned.

The primitive types byte and rune are aliases to integer types (as
defined by the Go spec) and are treated as integers in conversion.

  

        
	  
  
  
    
#### 
      func ValueToGo ¶
  
    
  

    
    
      

```
func ValueToGo(v *proto.Value, t reflect.Type) (interface{}, error)
```

    
  

ValueToGo converts a protobuf Value structure to a native Go value.

  

        

  
### Types ¶

  

This section is empty.