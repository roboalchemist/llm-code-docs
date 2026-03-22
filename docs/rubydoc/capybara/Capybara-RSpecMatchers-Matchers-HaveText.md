# Class: Capybara::RSpecMatchers::Matchers::HaveText
  
  
  

  
  
    Inherits:
    
      CountableWrappedElementMatcher
      
        

          
- Object
          
            
- Base
          
            
- WrappedElementMatcher
          
            
- CountableWrappedElementMatcher
          
            
- Capybara::RSpecMatchers::Matchers::HaveText
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/rspec/matchers/have_text.rb
  
  

  
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
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**format**(content)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from SpatialSugar

  

#above, #below, #left_of, #near, #right_of

  
  
  
  
  
  
  
  
  
### Methods included from CountSugar

  

#at_least, #at_most, #exactly, #once, #thrice, #times, #twice

  
  
  
  
  
  
  
  
  
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
# File 'lib/capybara/rspec/matchers/have_text.rb', line 17

def description
  "have text #{format(text)}"
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
# File 'lib/capybara/rspec/matchers/have_text.rb', line 13

def element_does_not_match?(el)
  el.assert_no_text(*@args, **@kw_args)
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
# File 'lib/capybara/rspec/matchers/have_text.rb', line 9

def element_matches?(el)
  el.assert_text(*@args, **@kw_args)
end
```

    
  

    
      
  
### 
  
    #**format**(content)  ⇒ Object 
  

  

  

  
    
      

```

21
22
23
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/have_text.rb', line 21

def format(content)
  content.inspect
end
```