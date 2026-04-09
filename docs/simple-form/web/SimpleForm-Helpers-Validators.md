# Module: SimpleForm::Helpers::Validators
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Inputs::Base
  
  

  
  
    Defined in:
    lib/simple_form/helpers/validators.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**has_validators?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**has_validators?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

5
6
7
```

    
    
      

```
# File 'lib/simple_form/helpers/validators.rb', line 5

def has_validators?
  @has_validators ||= attribute_name && object.class.respond_to?(:validators_on)
end
```