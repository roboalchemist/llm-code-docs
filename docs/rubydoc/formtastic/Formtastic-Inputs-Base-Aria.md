# Module: Formtastic::Inputs::Base::Aria
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Formtastic::Inputs::Base
  
  

  
  
    Defined in:
    lib/formtastic/inputs/base/aria.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**describedby**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**error_aria_attributes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**describedby**  ⇒ Object 
  

  

  

  
    
      

```

17
18
19
20
21
```

    
    
      

```
# File 'lib/formtastic/inputs/base/aria.rb', line 17

def describedby
  describedby = options.dig(:input_html, :'aria-describedby') || ''
  describedby += ' ' unless describedby.empty?
  describedby += "#{method}_error"
end
```

    
  

    
      
  
### 
  
    #**error_aria_attributes**  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
10
11
12
13
14
15
```

    
    
      

```
# File 'lib/formtastic/inputs/base/aria.rb', line 7

def error_aria_attributes
  return {} unless builder.semantic_errors_link_to_inputs
  return {} unless errors?

  {
    'aria-describedby': describedby,
    'aria-invalid': options.dig(:input_html, :'aria-invalid') || 'true'
  }
end
```