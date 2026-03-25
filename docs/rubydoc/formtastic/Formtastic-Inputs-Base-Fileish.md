# Module: Formtastic::Inputs::Base::Fileish
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Formtastic::Inputs::Base
  
  

  
  
    Defined in:
    lib/formtastic/inputs/base/fileish.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**file?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**file?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

7
8
9
10
11
12
```

    
    
      

```
# File 'lib/formtastic/inputs/base/fileish.rb', line 7

def file?
  @file ||= begin
    # TODO return true if self.is_a?(Formtastic::Inputs::FileInput::Woo)
    object && object.respond_to?(method) && builder.file_methods.any? { |m| object.send(method).respond_to?(m) }
  end
end
```