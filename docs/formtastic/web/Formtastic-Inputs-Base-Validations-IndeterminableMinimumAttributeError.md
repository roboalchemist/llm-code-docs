# Exception: Formtastic::Inputs::Base::Validations::IndeterminableMinimumAttributeError
  
  
  

  
  
    Inherits:
    
      ArgumentError
      
        

          
- Object
          
            
- ArgumentError
          
            
- Formtastic::Inputs::Base::Validations::IndeterminableMinimumAttributeError
          
        

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

8
9
10
11
12
13
```

    
    
      

```
# File 'lib/formtastic/inputs/base/validations.rb', line 8

def message
  [
    "A minimum value can not be determined when the validation uses :greater_than on a :decimal or :float column type.",
    "Please alter the validation to use :greater_than_or_equal_to, or provide a value for this attribute explicitly with the :min option on input()."
  ].join("\n")
end
```