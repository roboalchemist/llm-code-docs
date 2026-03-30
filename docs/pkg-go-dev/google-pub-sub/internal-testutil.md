### Index ¶

- 
        func VerifyKeyOrdering(publishData, receiveData []OrderedKeyMsg) error

- 
          type OrderedKeyMsg

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func VerifyKeyOrdering ¶
  
    
  

    
    
      

```
func VerifyKeyOrdering(publishData, receiveData []OrderedKeyMsg) error
```

    
  

VerifyKeyOrdering verifies that received data was published and received in
key order.

TODO(deklerk): account for consistent redelivery.

  

        

  
### Types ¶

  
      
  
  
    
#### 
      type OrderedKeyMsg ¶
  
    
  

    
    
      

```
type OrderedKeyMsg struct {
	Key  string
	Data string
}
```

    
  

OrderedKeyMsg is a message with key and data.