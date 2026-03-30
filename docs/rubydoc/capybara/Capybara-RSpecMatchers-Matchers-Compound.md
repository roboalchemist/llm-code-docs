# Module: Capybara::RSpecMatchers::Matchers::Compound
  
  
  

  

  
  
  
  
  
      Includes:
      RSpec::Matchers::Composable
  
  
  

  
  
    Included in:
    Base, NegatedMatcher
  
  

  
  
    Defined in:
    lib/capybara/rspec/matchers/compound.rb
  
  

## Defined Under Namespace

  
    
      **Modules:** Synchronizer
    
  
    
      **Classes:** And, CapybaraEvaluator, Or
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**and**(matcher)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**and_then**(matcher)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**or**(matcher)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**and**(matcher)  ⇒ Object 
  

  

  

  
    
      

```

10
11
12
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/compound.rb', line 10

def and(matcher)
  And.new(self, matcher)
end

```

    
  

    
      
  
### 
  
    #**and_then**(matcher)  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/compound.rb', line 14

def and_then(matcher)
  ::RSpec::Matchers::BuiltIn::Compound::And.new(self, matcher)
end

```

    
  

    
      
  
### 
  
    #**or**(matcher)  ⇒ Object 
  

  

  

  
    
      

```

18
19
20
```

    
    
      

```
# File 'lib/capybara/rspec/matchers/compound.rb', line 18

def or(matcher)
  Or.new(self, matcher)
end

```