# Module: SimpleForm::Components::MinMax
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Inputs::Base
  
  

  
  
    Defined in:
    lib/simple_form/components/min_max.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**min_max**(wrapper_options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**min_max**(wrapper_options = nil)  ⇒ Object 
  

  

  

  
    
      

```

5
6
7
8
9
10
11
12
```

    
    
      

```
# File 'lib/simple_form/components/min_max.rb', line 5

def min_max(wrapper_options = nil)
  if numeric_validator = find_numericality_validator
    validator_options = numeric_validator.options
    input_html_options[:min] ||= minimum_value(validator_options)
    input_html_options[:max] ||= maximum_value(validator_options)
  end
  nil
end
```