# Class: Capybara::RSpecMatchers::Matchers::HaveStyle
  
  Deprecated
  

  
  
    Inherits:
    
      MatchStyle
      
        

          
- Object
          
            
- Base
          
            
- WrappedElementMatcher
          
            
- MatchStyle
          
            
- Capybara::RSpecMatchers::Matchers::HaveStyle
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/rspec/matchers/match_style.rb
  
  

## Overview

  
    **Deprecated.** 

  

  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#failure_message, #failure_message_when_negated

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(*args, **kw_args, &filter_block)  ⇒ HaveStyle 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of HaveStyle.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from MatchStyle

  

#description, #does_not_match?, #element_matches?

  
  
  
  
  
  
  
  
  
### Methods inherited from WrappedElementMatcher

  

#does_not_match?, #matches?

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from Compound

  

#and, #and_then, #or

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(*args, **kw_args, &filter_block)  ⇒ HaveStyle 
  

  

  

  
    

Returns a new instance of HaveStyle.

  

  

  
    
      

```

36
37
38
39
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/match_style.rb', line 36

def initialize(*args, **kw_args, &filter_block)
  warn 'HaveStyle matcher is deprecated, please use the MatchStyle matcher instead'
  super
end
```