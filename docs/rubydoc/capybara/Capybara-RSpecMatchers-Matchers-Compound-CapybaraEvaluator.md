# Class: Capybara::RSpecMatchers::Matchers::Compound::CapybaraEvaluator
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Capybara::RSpecMatchers::Matchers::Compound::CapybaraEvaluator
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/rspec/matchers/compound.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(actual)  ⇒ CapybaraEvaluator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of CapybaraEvaluator.

  

      
        
- 
  
    
      #**matcher_matches?**(matcher)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**reset**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(actual)  ⇒ CapybaraEvaluator 
  

  

  

  
    

Returns a new instance of CapybaraEvaluator.

  

  

  
    
      

```

23
24
25
26
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/compound.rb', line 23

def initialize(actual)
  @actual = actual
  @match_results = Hash.new { |hsh, matcher| hsh[matcher] = matcher.matches?(@actual) }
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**matcher_matches?**(matcher)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/compound.rb', line 28

def matcher_matches?(matcher)
  @match_results[matcher]
end
```

    
  

    
      
  
### 
  
    #**reset**  ⇒ Object 
  

  

  

  
    
      

```

32
33
34
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/compound.rb', line 32

def reset
  @match_results.clear
end
```