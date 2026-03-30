# Top Level Namespace
  
  
  

  

  
  
  
  
  

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** Deflating, Hash, Integer, Rantly, String, Tuple
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**Rantly**(n = 1, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**Rantly**(n = 1, &block)  ⇒ Object 
  

  

  

  
    
      

```

9
10
11
12
13
14
15
```

    
    
      

```
# File 'lib/rantly.rb', line 9

def Rantly(n = 1, &block)
  if n > 1
    Rantly.map(n, &block)
  else
    Rantly.value(&block)
  end
end

```