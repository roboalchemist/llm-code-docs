# Module: SimpleForm::Components::HTML5
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Inputs::Base
  
  

  
  
    Defined in:
    lib/simple_form/components/html5.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**has_required?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**html5**(wrapper_options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**html5?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**input_html_required_option**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**has_required?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

25
26
27
28
29
30
```

    
    
      

```
# File 'lib/simple_form/components/html5.rb', line 25

def has_required?
  # We need to check browser_validations because
  # some browsers are still checking required even
  # if novalidate was given.
  required_field? && SimpleForm.browser_validations
end
```

    
  

    
      
  
### 
  
    #**html5**(wrapper_options = nil)  ⇒ Object 
  

  

  

  
    
      

```

9
10
11
12
13
14
15
```

    
    
      

```
# File 'lib/simple_form/components/html5.rb', line 9

def html5(wrapper_options = nil)
  @html5 = true

  input_html_options[:required]        = input_html_required_option
  input_html_options[:'aria-invalid']  = has_errors? || nil
  nil
end
```

    
  

    
      
  
### 
  
    #**html5?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/simple_form/components/html5.rb', line 17

def html5?
  @html5
end
```

    
  

    
      
  
### 
  
    #**initialize**  ⇒ Object 
  

  

  

  
    
      

```

5
6
7
```

    
    
      

```
# File 'lib/simple_form/components/html5.rb', line 5

def initialize(*)
  @html5 = false
end
```

    
  

    
      
  
### 
  
    #**input_html_required_option**  ⇒ Object 
  

  

  

  
    
      

```

21
22
23
```

    
    
      

```
# File 'lib/simple_form/components/html5.rb', line 21

def input_html_required_option
  !options[:required].nil? ? required_field? : has_required?
end
```