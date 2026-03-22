# Class: Capybara::RSpecMatchers::Matchers::HaveAnySelectors
  
  
  

  
  
    Inherits:
    
      WrappedElementMatcher
      
        

          
- Object
          
            
- Base
          
            
- WrappedElementMatcher
          
            
- Capybara::RSpecMatchers::Matchers::HaveAnySelectors
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/rspec/matchers/have_selector.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#failure_message, #failure_message_when_negated

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**description**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**does_not_match?**(el)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**element_matches?**(el)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from WrappedElementMatcher

  

#matches?

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#initialize

  
  
  
  
  
  
  
  
  
### Methods included from Compound

  

#and, #and_then, #or

  
  
## Constructor Details

  
    

This class inherits a constructor from Capybara::RSpecMatchers::Matchers::Base
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**description**  ⇒ Object 
  

  

  

  
    
      

```

65
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/have_selector.rb', line 65

def description = 'have any selectors'

```

    
  

    
      
  
### 
  
    #**does_not_match?**(el)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

61
62
63
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/have_selector.rb', line 61

def does_not_match?(el)
  el.assert_none_of_selectors(*@args, **session_query_options, &@filter_block)
end

```

    
  

    
      
  
### 
  
    #**element_matches?**(el)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

57
58
59
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/have_selector.rb', line 57

def element_matches?(el)
  el.assert_any_of_selectors(*@args, **session_query_options, &@filter_block)
end

```