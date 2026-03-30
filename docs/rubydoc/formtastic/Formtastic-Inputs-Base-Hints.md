# Module: Formtastic::Inputs::Base::Hints
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Formtastic::Inputs::Base
  
  

  
  
    Defined in:
    lib/formtastic/inputs/base/hints.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**hint?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**hint_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**hint_text**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**hint_text_from_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**hint?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/formtastic/inputs/base/hints.rb', line 17

def hint?
  !hint_text.blank? && !hint_text.kind_of?(Hash)
end
```

    
  

    
      
  
### 
  
    #**hint_html**  ⇒ Object 
  

  

  

  
    
      

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
# File 'lib/formtastic/inputs/base/hints.rb', line 7

def hint_html
  if hint?
    template.content_tag(
      :p, 
      hint_text.html_safe, 
      :class => builder.default_hint_class
    )
  end
end
```

    
  

    
      
  
### 
  
    #**hint_text**  ⇒ Object 
  

  

  

  
    
      

```

21
22
23
```

    
    
      

```
# File 'lib/formtastic/inputs/base/hints.rb', line 21

def hint_text
  localized_string(method, options[:hint], :hint)
end
```

    
  

    
      
  
### 
  
    #**hint_text_from_options**  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/formtastic/inputs/base/hints.rb', line 25

def hint_text_from_options
  options[:hint]
end
```