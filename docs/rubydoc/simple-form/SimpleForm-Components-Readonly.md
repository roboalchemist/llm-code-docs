# Module: SimpleForm::Components::Readonly
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Inputs::Base
  
  

  
  
    Defined in:
    lib/simple_form/components/readonly.rb
  
  

## Overview

  
    

Needs to be enabled in order to do automatic lookups.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**readonly**(wrapper_options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**readonly**(wrapper_options = nil)  ⇒ Object 
  

  

  

  
    
      

```

6
7
8
9
10
11
12
```

    
    
      

```
# File 'lib/simple_form/components/readonly.rb', line 6

def readonly(wrapper_options = nil)
  if readonly_attribute? && !has_readonly?
    input_html_options[:readonly] ||= true
    input_html_classes << :readonly
  end
  nil
end
```