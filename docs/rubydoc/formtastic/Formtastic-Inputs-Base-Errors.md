# Module: Formtastic::Inputs::Base::Errors
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Formtastic::Inputs::Base
  
  

  
  
    Defined in:
    lib/formtastic/inputs/base/errors.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**error_first_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**error_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**error_keys**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**error_list_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**error_none_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**error_sentence_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**errors**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**errors?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**error_first_html**  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
28
```

    
    
      

```
# File 'lib/formtastic/inputs/base/errors.rb', line 25

def error_first_html
  error_class = builder.default_inline_error_class
  template.content_tag(:p, errors.first.untaint.html_safe, :class => error_class)
end
```

    
  

    
      
  
### 
  
    #**error_html**  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/formtastic/inputs/base/errors.rb', line 7

def error_html
  errors? ? send(:"error_#{builder.inline_errors}_html") : +""
end
```

    
  

    
      
  
### 
  
    #**error_keys**  ⇒ Object 
  

  

  

  
    
      

```

48
49
50
51
52
53
```

    
    
      

```
# File 'lib/formtastic/inputs/base/errors.rb', line 48

def error_keys
  keys = [method.to_sym]
  keys << builder.file_metadata_suffixes.map{|suffix| "#{method}_#{suffix}".to_sym} if file?
  keys << association_primary_key if belongs_to? || has_many?
  keys.flatten.compact.uniq
end
```

    
  

    
      
  
### 
  
    #**error_list_html**  ⇒ Object 
  

  

  

  
    
      

```

16
17
18
19
20
21
22
23
```

    
    
      

```
# File 'lib/formtastic/inputs/base/errors.rb', line 16

def error_list_html
  error_class = builder.default_error_list_class
  list_elements = []
  errors.each do |error|
    list_elements << template.content_tag(:li, error.html_safe)
  end
  template.content_tag(:ul, list_elements.join("\n").html_safe, :class => error_class)
end
```

    
  

    
      
  
### 
  
    #**error_none_html**  ⇒ Object 
  

  

  

  
    
      

```

30
31
32
```

    
    
      

```
# File 'lib/formtastic/inputs/base/errors.rb', line 30

def error_none_html
  +""
end
```

    
  

    
      
  
### 
  
    #**error_sentence_html**  ⇒ Object 
  

  

  

  
    
      

```

11
12
13
14
```

    
    
      

```
# File 'lib/formtastic/inputs/base/errors.rb', line 11

def error_sentence_html
  error_class = builder.default_inline_error_class
  template.content_tag(:p, errors.to_sentence, id: "#{method}_error", :class => error_class)
end
```

    
  

    
      
  
### 
  
    #**errors**  ⇒ Object 
  

  

  

  
    
      

```

38
39
40
41
42
43
44
45
46
```

    
    
      

```
# File 'lib/formtastic/inputs/base/errors.rb', line 38

def errors
  errors = []
  if object && object.respond_to?(:errors)
    error_keys.each do |key| 
      errors << object.errors[key] unless object.errors[key].blank?
    end
  end
  errors.flatten.compact.uniq
end
```

    
  

    
      
  
### 
  
    #**errors?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

34
35
36
```

    
    
      

```
# File 'lib/formtastic/inputs/base/errors.rb', line 34

def errors?
  !errors.blank?
end
```