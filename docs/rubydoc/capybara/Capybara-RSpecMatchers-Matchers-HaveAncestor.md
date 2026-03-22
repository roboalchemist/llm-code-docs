# Class: Capybara::RSpecMatchers::Matchers::HaveAncestor
  
  
  

  
  
    Inherits:
    
      CountableWrappedElementMatcher
      
        

          
- Object
          
            
- Base
          
            
- WrappedElementMatcher
          
            
- CountableWrappedElementMatcher
          
            
- Capybara::RSpecMatchers::Matchers::HaveAncestor
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/rspec/matchers/have_ancestor.rb
  
  

  
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
  
    
      #**query**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
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
# File 'lib/capybara/rspec/matchers/have_ancestor.rb', line 17

def description
  "have ancestor #{query.description}"
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
# File 'lib/capybara/rspec/matchers/have_ancestor.rb', line 13

def element_does_not_match?(el)
  el.assert_no_ancestor(*@args, **session_query_options, &@filter_block)
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
# File 'lib/capybara/rspec/matchers/have_ancestor.rb', line 9

def element_matches?(el)
  el.assert_ancestor(*@args, **session_query_options, &@filter_block)
end

```

    
  

    
      
  
### 
  
    #**query**  ⇒ Object 
  

  

  

  
    
      

```

21
22
23
24
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/have_ancestor.rb', line 21

def query
  # @query ||= Capybara::Queries::AncestorQuery.new(*session_query_args, &@filter_block)
  @query ||= Capybara::Queries::AncestorQuery.new(*session_query_args, **session_query_options, &@filter_block)
end

```