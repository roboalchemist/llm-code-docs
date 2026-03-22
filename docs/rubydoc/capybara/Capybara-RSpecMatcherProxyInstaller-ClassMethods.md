# Module: Capybara::RSpecMatcherProxyInstaller::ClassMethods
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/rspec/matcher_proxies.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**included**(base)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**included**(base)  ⇒ Object 
  

  

  

  
    
      

```

66
67
68
69
```

    
    
      

```
# File 'lib/capybara/rspec/matcher_proxies.rb', line 66

def included(base)
  base.include(::Capybara::RSpecMatcherProxies) if base.include?(::Capybara::DSL)
  super
end
```