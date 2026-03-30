# Module: Capybara::DSLRSpecProxyInstaller
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    DSL
  
  

  
  
    Defined in:
    lib/capybara/rspec/matcher_proxies.rb
  
  

## Overview

  
    

:nocov:

  

  

## Defined Under Namespace

  
    
      **Modules:** ClassMethods
    
  
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**prepended**(base)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**prepended**(base)  ⇒ Object 
  

  

  

  
    
      

```

57
58
59
60
61
```

    
    
      

```
# File 'lib/capybara/rspec/matcher_proxies.rb', line 57

def self.prepended(base)
  class << base
    prepend ClassMethods
  end
end

```