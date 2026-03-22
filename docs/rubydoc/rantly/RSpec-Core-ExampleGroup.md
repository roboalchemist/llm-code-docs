# Class: RSpec::Core::ExampleGroup
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- RSpec::Core::ExampleGroup
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/rantly/rspec_extensions.rb
  
  

  
    
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
# File 'lib/rantly/rspec_extensions.rb', line 5

def property_of(&block)
  Rantly::Property.new(block)
end

```