# Class: Capybara::RSpecMatchers::Matchers::HaveAllSelectors
  
  
  

  
  
    Inherits:
    
      WrappedElementMatcher
      
        

          
- Object
          
            
- Base
          
            
- WrappedElementMatcher
          
            
- Capybara::RSpecMatchers::Matchers::HaveAllSelectors
          
        

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
  
    
      #**does_not_match?**(_actual)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
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

41
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/have_selector.rb', line 41

def description = 'have all selectors'
```

    
  

    
      
  
### 
  
    #**does_not_match?**(_actual)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

Raises:

  
    
- 
      
      
        (ArgumentError)
      
      
      
    
  

  
    
      

```

37
38
39
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/have_selector.rb', line 37

def does_not_match?(_actual)
  raise ArgumentError, 'The have_all_selectors matcher does not support use with not_to/should_not'
end
```

    
  

    
      
  
### 
  
    #**element_matches?**(el)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

33
34
35
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/have_selector.rb', line 33

def element_matches?(el)
  el.assert_all_of_selectors(*@args, **session_query_options, &@filter_block)
end
```