# Module: SimpleForm::Components::Minlength
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Inputs::Base
  
  

  
  
    Defined in:
    lib/simple_form/components/minlength.rb
  
  

## Overview

  
    

Needs to be enabled in order to do automatic lookups.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**minlength**(wrapper_options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**minlength**(wrapper_options = nil)  ⇒ Object 
  

  

  

  
    
      

```

6
7
8
9
```

    
    
      

```
# File 'lib/simple_form/components/minlength.rb', line 6

def minlength(wrapper_options = nil)
  input_html_options[:minlength] ||= minimum_length_from_validation
  nil
end
```