# Module: SimpleForm::Components::Maxlength
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Inputs::Base
  
  

  
  
    Defined in:
    lib/simple_form/components/maxlength.rb
  
  

## Overview

  
    

Needs to be enabled in order to do automatic lookups.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**maxlength**(wrapper_options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**maxlength**(wrapper_options = nil)  ⇒ Object 
  

  

  

  
    
      

```

6
7
8
9
```

    
    
      

```
# File 'lib/simple_form/components/maxlength.rb', line 6

def maxlength(wrapper_options = nil)
  input_html_options[:maxlength] ||= maximum_length_from_validation || limit
  nil
end
```