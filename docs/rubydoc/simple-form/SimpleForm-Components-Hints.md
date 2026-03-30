# Module: SimpleForm::Components::Hints
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Inputs::Base
  
  

  
  
    Defined in:
    lib/simple_form/components/hints.rb
  
  

## Overview

  
    

Needs to be enabled in order to do automatic lookups.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**has_hint?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**hint**(wrapper_options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**has_hint?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

19
20
21
```

    
    
      

```
# File 'lib/simple_form/components/hints.rb', line 19

def has_hint?
  options[:hint] != false && hint.present?
end
```

    
  

    
      
  
### 
  
    #**hint**(wrapper_options = nil)  ⇒ Object 
  

  

  

  
    
      

```

6
7
8
9
10
11
12
13
14
15
16
17
```

    
    
      

```
# File 'lib/simple_form/components/hints.rb', line 6

def hint(wrapper_options = nil)
  @hint ||= begin
    hint = options[:hint]

    if hint.is_a?(String)
      html_escape(hint)
    else
      content = translate_from_namespace(:hints)
      content.html_safe if content
    end
  end
end
```