# Module: SimpleForm::Components::Placeholders
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Inputs::Base
  
  

  
  
    Defined in:
    lib/simple_form/components/placeholders.rb
  
  

## Overview

  
    

Needs to be enabled in order to do automatic lookups.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**placeholder**(wrapper_options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**placeholder_text**(wrapper_options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**placeholder**(wrapper_options = nil)  ⇒ Object 
  

  

  

  
    
      

```

6
7
8
9
```

    
    
      

```
# File 'lib/simple_form/components/placeholders.rb', line 6

def placeholder(wrapper_options = nil)
  input_html_options[:placeholder] ||= placeholder_text
  nil
end
```

    
  

    
      
  
### 
  
    #**placeholder_text**(wrapper_options = nil)  ⇒ Object 
  

  

  

  
    
      

```

11
12
13
14
```

    
    
      

```
# File 'lib/simple_form/components/placeholders.rb', line 11

def placeholder_text(wrapper_options = nil)
  placeholder = options[:placeholder]
  placeholder.is_a?(String) ? placeholder : translate_from_namespace(:placeholders)
end
```