# Class: Capybara::Selector::Filters::IdentityExpressionFilter
  
  
  

  
  
    Inherits:
    
      ExpressionFilter
      
        

          
- Object
          
            
- Base
          
            
- ExpressionFilter
          
            
- Capybara::Selector::Filters::IdentityExpressionFilter
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/selector/filters/expression_filter.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**apply_filter**(expr, _name, _value, _ctx)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**default?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(name)  ⇒ IdentityExpressionFilter 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of IdentityExpressionFilter.

  

      
        
- 
  
    
      #**matcher?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#boolean?, #default, #format, #handles_option?, #skip?

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name)  ⇒ IdentityExpressionFilter 
  

  

  

  
    

Returns a new instance of IdentityExpressionFilter.

  

  

  
    
      

```

15
```

    
    
      

```
# File 'lib/capybara/selector/filters/expression_filter.rb', line 15

def initialize(name); super(name, nil, nil); end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**apply_filter**(expr, _name, _value, _ctx)  ⇒ Object 
  

  

  

  
    
      

```

18
```

    
    
      

```
# File 'lib/capybara/selector/filters/expression_filter.rb', line 18

def apply_filter(expr, _name, _value, _ctx); expr; end
```

    
  

    
      
  
### 
  
    #**default?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

16
```

    
    
      

```
# File 'lib/capybara/selector/filters/expression_filter.rb', line 16

def default?; false; end
```

    
  

    
      
  
### 
  
    #**matcher?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

17
```

    
    
      

```
# File 'lib/capybara/selector/filters/expression_filter.rb', line 17

def matcher?; false; end
```