# Module: Capybara::DSLRSpecProxyInstaller::ClassMethods
  
  
  

  

  
  
  
  
  

  

  
  
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

51
52
53
54
```

    
    
      

```
# File 'lib/capybara/rspec/matcher_proxies.rb', line 51

def included(base)
  base.include(::Capybara::RSpecMatcherProxies) if defined?(::RSpec::Matchers) && base.include?(::RSpec::Matchers)
  super
end
```