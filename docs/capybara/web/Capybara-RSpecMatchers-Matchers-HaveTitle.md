# Class: Capybara::RSpecMatchers::Matchers::HaveTitle
  
  
  

  
  
    Inherits:
    
      WrappedElementMatcher
      
        

          
- Object
          
            
- Base
          
            
- WrappedElementMatcher
          
            
- Capybara::RSpecMatchers::Matchers::HaveTitle
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/rspec/matchers/have_title.rb
  
  

  
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
# File 'lib/capybara/rspec/matchers/have_title.rb', line 17

def description
  "have title #{title.inspect}"
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
# File 'lib/capybara/rspec/matchers/have_title.rb', line 13

def element_does_not_match?(el)
  el.assert_no_title(*@args, **@kw_args)
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
# File 'lib/capybara/rspec/matchers/have_title.rb', line 9

def element_matches?(el)
  el.assert_title(*@args, **@kw_args)
end

```