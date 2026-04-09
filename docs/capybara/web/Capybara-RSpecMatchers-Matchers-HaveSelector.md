# Class: Capybara::RSpecMatchers::Matchers::HaveSelector
  
  
  

  
  
    Inherits:
    
      CountableWrappedElementMatcher
      
        

          
- Object
          
            
- Base
          
            
- WrappedElementMatcher
          
            
- CountableWrappedElementMatcher
          
            
- Capybara::RSpecMatchers::Matchers::HaveSelector
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/rspec/matchers/have_selector.rb
  
  

  
## Direct Known Subclasses

  

MatchSelector

  
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
  
    
      #**initialize**(*args, **kw_args, &filter_block)  ⇒ HaveSelector 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of HaveSelector.

  

      
        
- 
  
    
      #**query**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from SpatialSugar

  

#above, #below, #left_of, #near, #right_of

  
  
  
  
  
  
  
  
  
### Methods included from CountSugar

  

#at_least, #at_most, #exactly, #once, #thrice, #times, #twice

  
  
  
  
  
  
  
  
  
### Methods inherited from WrappedElementMatcher

  

#does_not_match?, #matches?

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from Compound

  

#and, #and_then, #or

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(*args, **kw_args, &filter_block)  ⇒ HaveSelector 
  

  

  

  
    

Returns a new instance of HaveSelector.

  

  

  
    
      

```

9
10
11
12
13
14
15
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/have_selector.rb', line 9

def initialize(*args, **kw_args, &filter_block)
  super
  return unless (@args.size < 2) && @kw_args.keys.any?(String)

  @args.push(@kw_args)
  @kw_args = {}
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**description**  ⇒ Object 
  

  

  

  
    
      

```

25
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/have_selector.rb', line 25

def description = "have #{query.description}"
```

    
  

    
      
  
### 
  
    #**element_does_not_match?**(el)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

21
22
23
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/have_selector.rb', line 21

def element_does_not_match?(el)
  el.assert_no_selector(*@args, **session_query_options, &@filter_block)
end
```

    
  

    
      
  
### 
  
    #**element_matches?**(el)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/have_selector.rb', line 17

def element_matches?(el)
  el.assert_selector(*@args, **session_query_options, &@filter_block)
end
```

    
  

    
      
  
### 
  
    #**query**  ⇒ Object 
  

  

  

  
    
      

```

27
28
29
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/have_selector.rb', line 27

def query
  @query ||= Capybara::Queries::SelectorQuery.new(*session_query_args, **session_query_options, &@filter_block)
end
```