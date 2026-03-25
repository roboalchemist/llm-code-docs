# Module: Formtastic::Inputs::Base::Labelling
  
  
  

  

  
  
  
  
  
      Includes:
      LocalizedString
  
  
  

  
  
    Included in:
    Formtastic::Inputs::Base
  
  

  
  
    Defined in:
    lib/formtastic/inputs/base/labelling.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**label_from_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**label_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**label_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**label_text**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**localized_label**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**render_label?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**requirement_text**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**requirement_text_or_proc**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

TODO: why does this need to be memoized in order to make the inputs_spec tests pass?.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from LocalizedString

  

#model_name

  
    
## Instance Method Details

    
      
  
### 
  
    #**label_from_options**  ⇒ Object 
  

  

  

  
    
      

```

37
38
39
```

    
    
      

```
# File 'lib/formtastic/inputs/base/labelling.rb', line 37

def label_from_options
  options[:label]
end
```

    
  

    
      
  
### 
  
    #**label_html**  ⇒ Object 
  

  

  

  
    
      

```

9
10
11
```

    
    
      

```
# File 'lib/formtastic/inputs/base/labelling.rb', line 9

def label_html
  render_label? ? builder.label(input_name, label_text, label_html_options) : +"".html_safe
end
```

    
  

    
      
  
### 
  
    #**label_html_options**  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
16
17
18
```

    
    
      

```
# File 'lib/formtastic/inputs/base/labelling.rb', line 13

def label_html_options
  {
    :for => input_html_options[:id],
    :class => ['label'],
  }.merge(options[:label_html] || {})
end
```

    
  

    
      
  
### 
  
    #**label_text**  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/formtastic/inputs/base/labelling.rb', line 20

def label_text
  ((localized_label || humanized_method_name) + requirement_text).html_safe
end
```

    
  

    
      
  
### 
  
    #**localized_label**  ⇒ Object 
  

  

  

  
    
      

```

41
42
43
```

    
    
      

```
# File 'lib/formtastic/inputs/base/labelling.rb', line 41

def localized_label
  localized_string(method, label_from_options || method, :label)
end
```

    
  

    
      
  
### 
  
    #**render_label?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

45
46
47
48
```

    
    
      

```
# File 'lib/formtastic/inputs/base/labelling.rb', line 45

def render_label?
  return false if options[:label] == false
  true
end
```

    
  

    
      
  
### 
  
    #**requirement_text**  ⇒ Object 
  

  

  

  
    
      

```

29
30
31
32
33
34
35
```

    
    
      

```
# File 'lib/formtastic/inputs/base/labelling.rb', line 29

def requirement_text
  if requirement_text_or_proc.respond_to?(:call)
    requirement_text_or_proc.call
  else
    requirement_text_or_proc
  end
end
```

    
  

    
      
  
### 
  
    #**requirement_text_or_proc**  ⇒ Object 
  

  

  

  
    

TODO: why does this need to be memoized in order to make the inputs_spec tests pass?

  

  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/formtastic/inputs/base/labelling.rb', line 25

def requirement_text_or_proc
  @requirement_text_or_proc ||= required? ? builder.required_string : builder.optional_string
end
```