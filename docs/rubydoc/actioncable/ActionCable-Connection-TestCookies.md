# Class: ActionCable::Connection::TestCookies
  
  
  

  
  
    Inherits:
    
      ActiveSupport::HashWithIndifferentAccess
      
        

          
- Object
          
            
- ActiveSupport::HashWithIndifferentAccess
          
            
- ActionCable::Connection::TestCookies
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/connection/test_case.rb
  
  

## Overview

  
    

:nodoc:

  

  

  
## Direct Known Subclasses

  

TestCookieJar

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**[]=**(name, options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**[]=**(name, options)  ⇒ Object 
  

  

  

  
    
      

```

34
35
36
37
```

    
    
      

```
# File 'lib/action_cable/connection/test_case.rb', line 34

def []=(name, options)
  value = options.is_a?(Hash) ? options.symbolize_keys[:value] : options
  super(name, value)
end
```