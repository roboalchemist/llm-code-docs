# Module: Formtastic::Inputs::Base::Choices
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    CheckBoxesInput, RadioInput
  
  

  
  
    Defined in:
    lib/formtastic/inputs/base/choices.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**choice_html**(choice)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**choice_html_options**(choice)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**choice_html_safe_value**(choice)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**choice_input_dom_id**(choice)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**choice_label**(choice)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**choice_value**(choice)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**choice_wrapping**(html_options, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**choice_wrapping_html_options**(choice)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**choices_group_wrapping**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**choices_group_wrapping_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**choices_wrapping**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**choices_wrapping_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**custom_choice_html_options**(choice)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**default_choice_html_options**(choice)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**label_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Override to remove the for attribute since this isn't associated with any element, as it's nested inside the legend.

  

      
        
- 
  
    
      #**legend_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**value_as_class?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**choice_html**(choice)  ⇒ Object 
  

  

  

  
    
      

```

43
44
45
```

    
    
      

```
# File 'lib/formtastic/inputs/base/choices.rb', line 43

def choice_html(choice)
  raise "choice_html() needs to be implemented when including Formtastic::Inputs::Base::Choices"
end
```

    
  

    
      
  
### 
  
    #**choice_html_options**(choice)  ⇒ Object 
  

  

  

  
    
      

```

59
60
61
```

    
    
      

```
# File 'lib/formtastic/inputs/base/choices.rb', line 59

def choice_html_options(choice)
  custom_choice_html_options(choice).merge(default_choice_html_options(choice))
end
```

    
  

    
      
  
### 
  
    #**choice_html_safe_value**(choice)  ⇒ Object 
  

  

  

  
    
      

```

71
72
73
```

    
    
      

```
# File 'lib/formtastic/inputs/base/choices.rb', line 71

def choice_html_safe_value(choice)
  choice_value(choice).to_s.gsub(/\s/, '_').gsub(/[^\w-]/, '').downcase
end
```

    
  

    
      
  
### 
  
    #**choice_input_dom_id**(choice)  ⇒ Object 
  

  

  

  
    
      

```

75
76
77
78
79
80
81
82
83
```

    
    
      

```
# File 'lib/formtastic/inputs/base/choices.rb', line 75

def choice_input_dom_id(choice)
  [
    builder.dom_id_namespace,
    sanitized_object_name,
    builder.options[:index],
    association_primary_key || method,
    choice_html_safe_value(choice)
  ].compact.reject { |i| i.blank? }.join("_")
end
```

    
  

    
      
  
### 
  
    #**choice_label**(choice)  ⇒ Object 
  

  

  

  
    
      

```

47
48
49
50
51
52
53
```

    
    
      

```
# File 'lib/formtastic/inputs/base/choices.rb', line 47

def choice_label(choice)
  if choice.is_a?(Array)
    choice.first
  else
    choice
  end.to_s
end
```

    
  

    
      
  
### 
  
    #**choice_value**(choice)  ⇒ Object 
  

  

  

  
    
      

```

55
56
57
```

    
    
      

```
# File 'lib/formtastic/inputs/base/choices.rb', line 55

def choice_value(choice)
  choice.is_a?(Array) ? choice[1] : choice
end
```

    
  

    
      
  
### 
  
    #**choice_wrapping**(html_options, &block)  ⇒ Object 
  

  

  

  
    
      

```

29
30
31
32
33
34
```

    
    
      

```
# File 'lib/formtastic/inputs/base/choices.rb', line 29

def choice_wrapping(html_options, &block)
  template.content_tag(:li,
    template.capture(&block),
    html_options
  )
end
```

    
  

    
      
  
### 
  
    #**choice_wrapping_html_options**(choice)  ⇒ Object 
  

  

  

  
    
      

```

36
37
38
39
40
41
```

    
    
      

```
# File 'lib/formtastic/inputs/base/choices.rb', line 36

def choice_wrapping_html_options(choice)
  classes = ['choice']
  classes << "#{sanitized_method_name.singularize}_#{choice_html_safe_value(choice)}" if value_as_class?

  { :class => classes.join(" ") }
end
```

    
  

    
      
  
### 
  
    #**choices_group_wrapping**(&block)  ⇒ Object 
  

  

  

  
    
      

```

18
19
20
21
22
23
```

    
    
      

```
# File 'lib/formtastic/inputs/base/choices.rb', line 18

def choices_group_wrapping(&block)
  template.content_tag(:ol,
    template.capture(&block),
    choices_group_wrapping_html_options
  )
end
```

    
  

    
      
  
### 
  
    #**choices_group_wrapping_html_options**  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/formtastic/inputs/base/choices.rb', line 25

def choices_group_wrapping_html_options
  { :class => "choices-group" }
end
```

    
  

    
      
  
### 
  
    #**choices_wrapping**(&block)  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
10
11
12
```

    
    
      

```
# File 'lib/formtastic/inputs/base/choices.rb', line 7

def choices_wrapping(&block)
  template.content_tag(:fieldset,
    template.capture(&block),
    choices_wrapping_html_options
  )
end
```

    
  

    
      
  
### 
  
    #**choices_wrapping_html_options**  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/formtastic/inputs/base/choices.rb', line 14

def choices_wrapping_html_options
  { :class => "choices" }
end
```

    
  

    
      
  
### 
  
    #**custom_choice_html_options**(choice)  ⇒ Object 
  

  

  

  
    
      

```

67
68
69
```

    
    
      

```
# File 'lib/formtastic/inputs/base/choices.rb', line 67

def custom_choice_html_options(choice)
  (choice.is_a?(Array) && choice.size > 2) ? choice[-1] : {}
end
```

    
  

    
      
  
### 
  
    #**default_choice_html_options**(choice)  ⇒ Object 
  

  

  

  
    
      

```

63
64
65
```

    
    
      

```
# File 'lib/formtastic/inputs/base/choices.rb', line 63

def default_choice_html_options(choice)
  { :id => choice_input_dom_id(choice) }
end
```

    
  

    
      
  
### 
  
    #**label_html_options**  ⇒ Object 
  

  

  

  
    

Override to remove the for attribute since this isn't associated with any element, as it's
nested inside the legend.

  

  

  
    
      

```

102
103
104
```

    
    
      

```
# File 'lib/formtastic/inputs/base/choices.rb', line 102

def label_html_options
  super.merge(:for => nil)
end
```

    
  

    
      
  
### 
  
    #**legend_html**  ⇒ Object 
  

  

  

  
    
      

```

89
90
91
92
93
94
95
96
97
98
```

    
    
      

```
# File 'lib/formtastic/inputs/base/choices.rb', line 89

def legend_html
  if render_label?
    template.content_tag(:legend,
      template.content_tag(:label, label_text),
      label_html_options.merge(:class => "label")
    )
  else
    +"".html_safe
  end
end
```

    
  

    
      
  
### 
  
    #**value_as_class?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

85
86
87
```

    
    
      

```
# File 'lib/formtastic/inputs/base/choices.rb', line 85

def value_as_class?
  options[:value_as_class]
end
```