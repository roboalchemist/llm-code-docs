# Module: SimpleForm::Components::Errors
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Inputs::Base
  
  

  
  
    Defined in:
    lib/simple_form/components/errors.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**error**(wrapper_options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**full_error**(wrapper_options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**has_errors?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**has_value?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**valid?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**error**(wrapper_options = nil)  ⇒ Object 
  

  

  

  
    
      

```

5
6
7
```

    
    
      

```
# File 'lib/simple_form/components/errors.rb', line 5

def error(wrapper_options = nil)
  error_text if has_errors?
end
```

    
  

    
      
  
### 
  
    #**full_error**(wrapper_options = nil)  ⇒ Object 
  

  

  

  
    
      

```

9
10
11
```

    
    
      

```
# File 'lib/simple_form/components/errors.rb', line 9

def full_error(wrapper_options = nil)
  full_error_text if options[:error] != false && has_errors?
end
```

    
  

    
      
  
### 
  
    #**has_errors?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/simple_form/components/errors.rb', line 13

def has_errors?
  object_with_errors? || !object && has_custom_error?
end
```

    
  

    
      
  
### 
  
    #**has_value?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/simple_form/components/errors.rb', line 17

def has_value?
  object && object.respond_to?(attribute_name) && object.send(attribute_name).present?
end
```

    
  

    
      
  
### 
  
    #**valid?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

21
22
23
```

    
    
      

```
# File 'lib/simple_form/components/errors.rb', line 21

def valid?
  !has_errors? && has_value?
end
```