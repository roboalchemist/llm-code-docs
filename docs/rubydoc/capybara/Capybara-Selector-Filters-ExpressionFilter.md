# Class: Capybara::Selector::Filters::ExpressionFilter
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- Capybara::Selector::Filters::ExpressionFilter
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/selector/filters/expression_filter.rb
  
  

  
## Direct Known Subclasses

  

IdentityExpressionFilter

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**apply_filter**(expr, name, value, selector)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#boolean?, #default, #default?, #format, #handles_option?, #initialize, #matcher?, #skip?

  
## Constructor Details

  
    

This class inherits a constructor from Capybara::Selector::Filters::Base
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**apply_filter**(expr, name, value, selector)  ⇒ Object 
  

  

  

  
    
      

```

9
10
11
```

    
    
      

```
# File 'lib/capybara/selector/filters/expression_filter.rb', line 9

def apply_filter(expr, name, value, selector)
  apply(expr, name, value, expr, selector)
end
```