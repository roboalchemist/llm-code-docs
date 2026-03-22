# Module: XPath::DSL
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/selector/xpath_extensions.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**join**(*expressions)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**join**(*expressions)  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/capybara/selector/xpath_extensions.rb', line 13

def join(*expressions)
  XPath::Expression.new(:join, *[self, expressions].flatten)
end

```