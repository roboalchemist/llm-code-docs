# Module: Formtastic::Inputs::Base::Wrapping
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Formtastic::Inputs::Base
  
  

  
  
    Defined in:
    lib/formtastic/inputs/base/wrapping.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**input_wrapping**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Override this method if you want to change the display order (for example, rendering the errors before the body of the input).

  

      
        
- 
  
    
      #**wrapper_classes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**wrapper_classes_raw**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**wrapper_dom_id**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**wrapper_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**wrapper_html_options_raw**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**input_wrapping**(&block)  ⇒ Object 
  

  

  

  
    

Override this method if you want to change the display order (for example, rendering the
errors before the body of the input).

  

  

  
    
      

```

10
11
12
13
14
15
```

    
    
      

```
# File 'lib/formtastic/inputs/base/wrapping.rb', line 10

def input_wrapping(&block)
  template.content_tag(:li,
    [template.capture(&block), error_html, hint_html].join("\n").html_safe,
    wrapper_html_options
  )
end
```

    
  

    
      
  
### 
  
    #**wrapper_classes**  ⇒ Object 
  

  

  

  
    
      

```

32
33
34
35
36
37
38
39
40
41
42
```

    
    
      

```
# File 'lib/formtastic/inputs/base/wrapping.rb', line 32

def wrapper_classes
  classes = wrapper_classes_raw
  classes << as
  classes << "input"
  classes << "error" if errors?
  classes << "optional" if optional?
  classes << "required" if required?
  classes << "autofocus" if autofocus?

  classes.join(' ')
end
```

    
  

    
      
  
### 
  
    #**wrapper_classes_raw**  ⇒ Object 
  

  

  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/formtastic/inputs/base/wrapping.rb', line 28

def wrapper_classes_raw
  [*wrapper_html_options_raw[:class]]
end
```

    
  

    
      
  
### 
  
    #**wrapper_dom_id**  ⇒ Object 
  

  

  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/formtastic/inputs/base/wrapping.rb', line 44

def wrapper_dom_id
  @wrapper_dom_id ||= "#{dom_id.to_s.gsub((association_primary_key || method).to_s, sanitized_method_name.to_s)}_input"
end
```

    
  

    
      
  
### 
  
    #**wrapper_html_options**  ⇒ Object 
  

  

  

  
    
      

```

17
18
19
20
21
22
```

    
    
      

```
# File 'lib/formtastic/inputs/base/wrapping.rb', line 17

def wrapper_html_options
  opts = wrapper_html_options_raw
  opts[:class] = wrapper_classes
  opts[:id] = wrapper_dom_id unless opts.has_key? :id
  opts
end
```

    
  

    
      
  
### 
  
    #**wrapper_html_options_raw**  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
```

    
    
      

```
# File 'lib/formtastic/inputs/base/wrapping.rb', line 24

def wrapper_html_options_raw
  (options[:wrapper_html] || {}).dup
end
```