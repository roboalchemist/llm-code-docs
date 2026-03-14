# Module: Formtastic::Inputs::Base::Stringish
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    ColorInput, DatalistInput, DatePickerInput, DatetimePickerInput, EmailInput, PasswordInput, PhoneInput, SearchInput, StringInput, TimePickerInput, UrlInput
  
  

  
  
    Defined in:
    lib/formtastic/inputs/base/stringish.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**input_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Overrides standard `input_html_options` to provide a `maxlength` and `size` attribute.

  

      
        
- 
  
    
      #**maxlength**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**size**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_html**  ⇒ Object 
    

    
  
  
  
  
  
  abstract
  
  

  
    
  

      
        
- 
  
    
      #**wrapper_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**input_html_options**  ⇒ Object 
  

  

  

  
    

Overrides standard `input_html_options` to provide a `maxlength` and `size` attribute.

  

  

  
    
      

```

16
17
18
19
20
21
```

    
    
      

```
# File 'lib/formtastic/inputs/base/stringish.rb', line 16

def input_html_options
  {
    :maxlength => maxlength,
    :size => size
  }.merge(super)
end
```

    
  

    
      
  
### 
  
    #**maxlength**  ⇒ Object 
  

  

  

  
    
      

```

27
28
29
```

    
    
      

```
# File 'lib/formtastic/inputs/base/stringish.rb', line 27

def maxlength
  options[:input_html].try(:[], :maxlength) || limit
end
```

    
  

    
      
  
### 
  
    #**size**  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/formtastic/inputs/base/stringish.rb', line 23

def size
  builder.default_text_field_size
end
```

    
  

    
      
  
### 
  
    #**to_html**  ⇒ Object 
  

  

  

  
    
  **This method is abstract.**
  

Override this method in your input class to describe how the input should render itself.

  

  

  
    
      

```

8
9
10
11
12
13
```

    
    
      

```
# File 'lib/formtastic/inputs/base/stringish.rb', line 8

def to_html
  input_wrapping do
    label_html <<
    builder.text_field(method, input_html_options)
  end
end
```

    
  

    
      
  
### 
  
    #**wrapper_html_options**  ⇒ Object 
  

  

  

  
    
      

```

31
32
33
34
```

    
    
      

```
# File 'lib/formtastic/inputs/base/stringish.rb', line 31

def wrapper_html_options
  new_class = [super[:class], "stringish"].compact.join(" ")
  super.merge(:class => new_class)
end
```