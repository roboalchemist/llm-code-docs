# Exception: Rantly::TooManyTries
  
  
  

  
  
    Inherits:
    
      RuntimeError
      
        

          
- Object
          
            
- RuntimeError
          
            
- Rantly::TooManyTries
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/rantly/generator.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**limit**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute limit.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(limit, nfailed)  ⇒ TooManyTries 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of TooManyTries.

  

      
        
- 
  
    
      #**tries**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(limit, nfailed)  ⇒ TooManyTries 
  

  

  

  
    

Returns a new instance of TooManyTries.

  

  

  
    
      

```

35
36
37
38
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 35

def initialize(limit, nfailed)
  @limit = limit
  @nfailed = nfailed
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**limit**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute limit.

  

  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 44

def limit
  @limit
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**tries**  ⇒ Object 
  

  

  

  
    
      

```

40
41
42
```

    
    
      

```
# File 'lib/rantly/generator.rb', line 40

def tries
  @nfailed
end

```