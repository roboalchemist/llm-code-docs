# Module: Formtastic::LocalizedString
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Actions::Base, Helpers::ErrorsHelper, Helpers::InputsHelper, Inputs::Base::Labelling
  
  

  
  
    Defined in:
    lib/formtastic/localized_string.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**model_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**model_name**  ⇒ Object 
  

  

  

  
    
      

```

5
6
7
```

    
    
      

```
# File 'lib/formtastic/localized_string.rb', line 5

def model_name
  @object.present? ? @object.class.name : @object_name.to_s.classify
end
```