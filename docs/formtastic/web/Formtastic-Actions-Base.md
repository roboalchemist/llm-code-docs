# Module: Formtastic::Actions::Base
  
  
  

  

  
  
  
  
  
      Includes:
      LocalizedString
  
  
  

  
  
    Included in:
    ButtonAction, InputAction, LinkAction
  
  

  
  
    Defined in:
    lib/formtastic/actions/base.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**builder**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute builder.

  

    
      
- 
  
    
      #**method**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute method.

  

    
      
- 
  
    
      #**object**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute object.

  

    
      
- 
  
    
      #**object_name**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute object_name.

  

    
      
- 
  
    
      #**options**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute options.

  

    
      
- 
  
    
      #**template**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute template.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**accesskey**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**button_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**button_html_from_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**default_button_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**default_wrapper_classes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**default_wrapper_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**default_wrapper_id**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**extra_button_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(builder, template, object, object_name, method, options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**supported_methods**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**text**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**wrapper**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**wrapper_class**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**wrapper_classes_from_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**wrapper_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**wrapper_html_options_from_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**wrapper_id**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**wrapper_id_from_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from LocalizedString

  

#model_name

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**builder**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute builder.

  

  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 7

def builder
  @builder
end
```

    
  

    
      
      
      
  
### 
  
    #**method**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute method.

  

  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 7

def method
  @method
end
```

    
  

    
      
      
      
  
### 
  
    #**object**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute object.

  

  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 7

def object
  @object
end
```

    
  

    
      
      
      
  
### 
  
    #**object_name**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute object_name.

  

  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 7

def object_name
  @object_name
end
```

    
  

    
      
      
      
  
### 
  
    #**options**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute options.

  

  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 7

def options
  @options
end
```

    
  

    
      
      
      
  
### 
  
    #**template**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute template.

  

  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 7

def template
  @template
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**accesskey**  ⇒ Object 
  

  

  

  
    
      

```

103
104
105
106
107
108
109
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 103

def accesskey
  # TODO could be cleaner and separated, remember that nil is an allowed value for all of these
  return options[:accesskey] if options.key?(:accesskey)
  return options[:button_html][:accesskey] if options.key?(:button_html) && options[:button_html].key?(:accesskey)
  # TODO might be different for cancel, etc?
  return builder.default_commit_button_accesskey
end
```

    
  

    
      
  
### 
  
    #**button_html**  ⇒ Object 
  

  

  

  
    
      

```

87
88
89
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 87

def button_html
  default_button_html.merge(button_html_from_options || {}).merge(extra_button_html_options)
end
```

    
  

    
      
  
### 
  
    #**button_html_from_options**  ⇒ Object 
  

  

  

  
    
      

```

91
92
93
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 91

def button_html_from_options
  options[:button_html]
end
```

    
  

    
      
  
### 
  
    #**default_button_html**  ⇒ Object 
  

  

  

  
    
      

```

99
100
101
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 99

def default_button_html
  { :accesskey => accesskey }
end
```

    
  

    
      
  
### 
  
    #**default_wrapper_classes**  ⇒ Object 
  

  

  

  
    
      

```

50
51
52
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 50

def default_wrapper_classes
  ["action", "#{options[:as]}_action"]
end
```

    
  

    
      
  
### 
  
    #**default_wrapper_html_options**  ⇒ Object 
  

  

  

  
    
      

```

39
40
41
42
43
44
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 39

def default_wrapper_html_options
  {
    :class => wrapper_class,
    :id => wrapper_id
  }
end
```

    
  

    
      
  
### 
  
    #**default_wrapper_id**  ⇒ Object 
  

  

  

  
    
      

```

72
73
74
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 72

def default_wrapper_id
  "#{object_name}_#{method}_action"
end
```

    
  

    
      
  
### 
  
    #**extra_button_html_options**  ⇒ Object 
  

  

  

  
    
      

```

95
96
97
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 95

def extra_button_html_options
  {}
end
```

    
  

    
      
  
### 
  
    #**initialize**(builder, template, object, object_name, method, options)  ⇒ Object 
  

  

  

  
    
      

```

9
10
11
12
13
14
15
16
17
18
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 9

def initialize(builder, template, object, object_name, method, options)
  @builder = builder
  @template = template
  @object = object
  @object_name = object_name
  @method = method
  @options = options.dup
  
  check_supported_methods!
end
```

    
  

    
      
  
### 
  
    #**supported_methods**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

76
77
78
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 76

def supported_methods
  raise NotImplementedError
end
```

    
  

    
      
  
### 
  
    #**text**  ⇒ Object 
  

  

  

  
    
      

```

80
81
82
83
84
85
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 80

def text
  text = options[:label]
  text = (localized_string(i18n_key, text, :action, :model => sanitized_object_name) ||
         Formtastic::I18n.t(i18n_key, :model => sanitized_object_name)) unless text.is_a?(::String)
  text
end
```

    
  

    
      
  
### 
  
    #**to_html**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 20

def to_html
  raise NotImplementedError
end
```

    
  

    
      
  
### 
  
    #**wrapper**(&block)  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
27
28
29
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 24

def wrapper(&block)
  template.content_tag(:li, 
    template.capture(&block), 
    wrapper_html_options
  )
end
```

    
  

    
      
  
### 
  
    #**wrapper_class**  ⇒ Object 
  

  

  

  
    
      

```

46
47
48
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 46

def wrapper_class
  (default_wrapper_classes << wrapper_classes_from_options).join(" ")
end
```

    
  

    
      
  
### 
  
    #**wrapper_classes_from_options**  ⇒ Object 
  

  

  

  
    
      

```

54
55
56
57
58
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 54

def wrapper_classes_from_options
  classes = wrapper_html_options_from_options[:class] || []
  classes = classes.split(" ") if classes.is_a? String
  classes
end
```

    
  

    
      
  
### 
  
    #**wrapper_html_options**  ⇒ Object 
  

  

  

  
    
      

```

31
32
33
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 31

def wrapper_html_options
  wrapper_html_options_from_options.merge(default_wrapper_html_options)
end
```

    
  

    
      
  
### 
  
    #**wrapper_html_options_from_options**  ⇒ Object 
  

  

  

  
    
      

```

35
36
37
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 35

def wrapper_html_options_from_options
  options[:wrapper_html] || {}
end
```

    
  

    
      
  
### 
  
    #**wrapper_id**  ⇒ Object 
  

  

  

  
    
      

```

64
65
66
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 64

def wrapper_id
  wrapper_id_from_options || default_wrapper_id
end
```

    
  

    
      
  
### 
  
    #**wrapper_id_from_options**  ⇒ Object 
  

  

  

  
    
      

```

68
69
70
```

    
    
      

```
# File 'lib/formtastic/actions/base.rb', line 68

def wrapper_id_from_options
  wrapper_html_options_from_options[:id]
end
```