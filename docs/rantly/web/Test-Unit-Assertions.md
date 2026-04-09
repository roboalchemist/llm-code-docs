# Module: Test::Unit::Assertions
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/rantly/testunit_extensions.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**property_of**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**property_of**(&block)  ⇒ Object 
  

  

  

  
    
      

```

5
6
7
```

    
    
      

```
# File 'lib/rantly/testunit_extensions.rb', line 5

def property_of(&block)
  Rantly::Property.new(block)
end

```