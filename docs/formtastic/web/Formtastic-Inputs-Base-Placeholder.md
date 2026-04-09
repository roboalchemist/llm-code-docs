# Module: Formtastic::Inputs::Base::Placeholder
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    DatetimePickerish, ColorInput, EmailInput, NumberInput, PasswordInput, PhoneInput, SearchInput, StringInput, TextInput, UrlInput
  
  

  
  
    Defined in:
    lib/formtastic/inputs/base/placeholder.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**input_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**placeholder_text**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**input_html_options**  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/formtastic/inputs/base/placeholder.rb', line 7

def input_html_options
  {:placeholder => placeholder_text}.merge(super)
end
```

    
  

    
      
  
### 
  
    #**placeholder_text**  ⇒ Object 
  

  

  

  
    
      

```

11
12
13
```

    
    
      

```
# File 'lib/formtastic/inputs/base/placeholder.rb', line 11

def placeholder_text
  localized_string(method, options[:placeholder], :placeholder)
end
```