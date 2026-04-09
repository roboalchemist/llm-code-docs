# Module: Formtastic::Inputs::Base::Options
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Formtastic::Inputs::Base
  
  

  
  
    Defined in:
    lib/formtastic/inputs/base/options.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**formtastic_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**input_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**formtastic_options**  ⇒ Object 
  

  

  

  
    
      

```

11
12
13
```

    
    
      

```
# File 'lib/formtastic/inputs/base/options.rb', line 11

def formtastic_options
  [:priority_countries, :priority_zones, :member_label, :member_value, :collection, :required, :label, :as, :hint, :input_html, :value_as_class, :class]
end
```

    
  

    
      
  
### 
  
    #**input_options**  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/formtastic/inputs/base/options.rb', line 7

def input_options
  options.except(*formtastic_options)
end
```