# Exception: Formtastic::Inputs::Base::Validations::IndeterminableMaximumAttributeError
  
  
  

  
  
    Inherits:
    
      ArgumentError
      
        

          
- Object
          
            
- ArgumentError
          
            
- Formtastic::Inputs::Base::Validations::IndeterminableMaximumAttributeError
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/formtastic/inputs/base/validations.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**message**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**message**  ⇒ Object 
  

  

  

  
    
      

```

17
18
19
20
21
22
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 17

def message
  [
    "A maximum value can not be determined when the validation uses :less_than on a :decimal or :float column type.",
    "Please alter the validation to use :less_than_or_equal_to, or provide a value for this attribute explicitly with the :max option on input()."
  ].join("\n")
end
```