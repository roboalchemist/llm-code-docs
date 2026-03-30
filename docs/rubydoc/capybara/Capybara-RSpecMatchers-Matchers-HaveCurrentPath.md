# Class: Capybara::RSpecMatchers::Matchers::HaveCurrentPath
  
  
  

  
  
    Inherits:
    
      WrappedElementMatcher
      
        

          
- Object
          
            
- Base
          
            
- WrappedElementMatcher
          
            
- Capybara::RSpecMatchers::Matchers::HaveCurrentPath
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/rspec/matchers/have_current_path.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#failure_message, #failure_message_when_negated

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**description**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**element_does_not_match?**(el)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**element_matches?**(el)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from WrappedElementMatcher

  

#does_not_match?, #matches?

  
  
  
  
  
  
  
  
  
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

17
18
19
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/have_current_path.rb', line 17

def description
  "have current path #{current_path.inspect}"
end
```

    
  

    
      
  
### 
  
    #**element_does_not_match?**(el)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/have_current_path.rb', line 13

def element_does_not_match?(el)
  el.assert_no_current_path(current_path, **@kw_args, &@filter_block)
end
```

    
  

    
      
  
### 
  
    #**element_matches?**(el)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

9
10
11
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/have_current_path.rb', line 9

def element_matches?(el)
  el.assert_current_path(current_path, **@kw_args, &@filter_block)
end
```