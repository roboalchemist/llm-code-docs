# Module: SimpleForm::Components::Pattern
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Inputs::Base
  
  

  
  
    Defined in:
    lib/simple_form/components/pattern.rb
  
  

## Overview

  
    

Needs to be enabled in order to do automatic lookups.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**pattern**(wrapper_options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**pattern**(wrapper_options = nil)  ⇒ Object 
  

  

  

  
    
      

```

6
7
8
9
```

    
    
      

```
# File 'lib/simple_form/components/pattern.rb', line 6

def pattern(wrapper_options = nil)
  input_html_options[:pattern] ||= pattern_source
  nil
end

```