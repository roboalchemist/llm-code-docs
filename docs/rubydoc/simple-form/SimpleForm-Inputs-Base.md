# Class: SimpleForm::Inputs::Base
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- SimpleForm::Inputs::Base
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      ActionView::Helpers::TranslationHelper, ERB::Util, Components::Errors, Components::HTML5, Components::Hints, Components::LabelInput, Components::Maxlength, Components::MinMax, Components::Minlength, Components::Pattern, Components::Placeholders, Components::Readonly, Helpers::Autofocus, Helpers::Disabled, Helpers::Readonly, Helpers::Required, Helpers::Validators
  
  
  

  

  
  
    Defined in:
    lib/simple_form/inputs/base.rb
  
  

  
## Direct Known Subclasses

  

BlockInput, BooleanInput, CollectionInput, ColorInput, DateTimeInput, FileInput, HiddenInput, NumericInput, PasswordInput, RichTextAreaInput, StringInput, TextInput

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**attribute_name**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute attribute_name.

  

    
      
- 
  
    
      #**column**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute column.

  

    
      
- 
  
    
      #**html_classes**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute html_classes.

  

    
      
- 
  
    
      #**input_html_classes**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute input_html_classes.

  

    
      
- 
  
    
      #**input_html_options**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute input_html_options.

  

    
      
- 
  
    
      #**input_type**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute input_type.

  

    
      
- 
  
    
      #**options**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute options.

  

    
      
- 
  
    
      #**reflection**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute reflection.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**disable**(*keys)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**enable**(*keys)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**additional_classes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(builder, attribute_name, column, input_type, options = {})  ⇒ Base 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Base.

  

      
        
- 
  
    
      #**input**(wrapper_options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**input_class**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**input_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Components::Readonly

  

#readonly

  
  
  
  
  
  
  
  
  
### Methods included from Components::Placeholders

  

#placeholder, #placeholder_text

  
  
  
  
  
  
  
  
  
### Methods included from Components::Pattern

  

#pattern

  
  
  
  
  
  
  
  
  
### Methods included from Components::MinMax

  

#min_max

  
  
  
  
  
  
  
  
  
### Methods included from Components::Minlength

  

#minlength

  
  
  
  
  
  
  
  
  
### Methods included from Components::Maxlength

  

#maxlength

  
  
  
  
  
  
  
  
  
### Methods included from Components::LabelInput

  

#label_input

  
  
  
  
  
  
  
  
  
  
### Methods included from Components::HTML5

  

#has_required?, #html5, #html5?, #input_html_required_option

  
  
  
  
  
  
  
  
  
### Methods included from Components::Hints

  

#has_hint?, #hint

  
  
  
  
  
  
  
  
  
### Methods included from Components::Errors

  

#error, #full_error, #has_errors?, #has_value?, #valid?

  
  
  
  
  
  
  
  
  
### Methods included from Helpers::Validators

  

#has_validators?

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(builder, attribute_name, column, input_type, options = {})  ⇒ Base 
  

  

  

  
    

Returns a new instance of Base.

  

  

  
    
      

```

54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
```

    
    
      

```
# File 'lib/simple_form/inputs/base.rb', line 54

def initialize(builder, attribute_name, column, input_type, options = {})
  super

  options         = options.dup
  @builder        = builder
  @attribute_name = attribute_name
  @column         = column
  @input_type     = input_type
  @reflection     = options.delete(:reflection)
  @options        = options.reverse_merge!(self.class.default_options)
  @required       = calculate_required

  # Notice that html_options_for receives a reference to input_html_classes.
  # This means that classes added dynamically to input_html_classes will
  # still propagate to input_html_options.
  @html_classes = SimpleForm.additional_classes_for(:input) { additional_classes }

  @input_html_classes = @html_classes.dup

  input_html_classes = self.input_html_classes

  if SimpleForm.input_class && input_html_classes.any?
    input_html_classes << SimpleForm.input_class
  end

  @input_html_options = html_options_for(:input, input_html_classes).tap do |o|
    o[:readonly]  = true if has_readonly?
    o[:disabled]  = true if has_disabled?
    o[:autofocus] = true if has_autofocus?
  end
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**attribute_name**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute attribute_name.

  

  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/simple_form/inputs/base.rb', line 28

def attribute_name
  @attribute_name
end
```

    
  

    
      
      
      
  
### 
  
    #**column**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute column.

  

  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/simple_form/inputs/base.rb', line 28

def column
  @column
end
```

    
  

    
      
      
      
  
### 
  
    #**html_classes**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute html_classes.

  

  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/simple_form/inputs/base.rb', line 28

def html_classes
  @html_classes
end
```

    
  

    
      
      
      
  
### 
  
    #**input_html_classes**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute input_html_classes.

  

  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/simple_form/inputs/base.rb', line 28

def input_html_classes
  @input_html_classes
end
```

    
  

    
      
      
      
  
### 
  
    #**input_html_options**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute input_html_options.

  

  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/simple_form/inputs/base.rb', line 28

def input_html_options
  @input_html_options
end
```

    
  

    
      
      
      
  
### 
  
    #**input_type**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute input_type.

  

  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/simple_form/inputs/base.rb', line 28

def input_type
  @input_type
end
```

    
  

    
      
      
      
  
### 
  
    #**options**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute options.

  

  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/simple_form/inputs/base.rb', line 28

def options
  @options
end
```

    
  

    
      
      
      
  
### 
  
    #**reflection**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute reflection.

  

  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/simple_form/inputs/base.rb', line 28

def reflection
  @reflection
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**disable**(*keys)  ⇒ Object 
  

  

  

  
    
      

```

42
43
44
45
46
```

    
    
      

```
# File 'lib/simple_form/inputs/base.rb', line 42

def self.disable(*keys)
  options = self.default_options.dup
  keys.each { |key| options[key] = false }
  self.default_options = options
end
```

    
  

    
      
  
### 
  
    .**enable**(*keys)  ⇒ Object 
  

  

  

  
    
      

```

36
37
38
39
40
```

    
    
      

```
# File 'lib/simple_form/inputs/base.rb', line 36

def self.enable(*keys)
  options = self.default_options.dup
  keys.each { |key| options.delete(key) }
  self.default_options = options
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**additional_classes**  ⇒ Object 
  

  

  

  
    
      

```

94
95
96
```

    
    
      

```
# File 'lib/simple_form/inputs/base.rb', line 94

def additional_classes
  @additional_classes ||= [input_type, required_class, readonly_class, disabled_class].compact
end
```

    
  

    
      
  
### 
  
    #**input**(wrapper_options = nil)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

86
87
88
```

    
    
      

```
# File 'lib/simple_form/inputs/base.rb', line 86

def input(wrapper_options = nil)
  raise NotImplementedError
end
```

    
  

    
      
  
### 
  
    #**input_class**  ⇒ Object 
  

  

  

  
    
      

```

98
99
100
```

    
    
      

```
# File 'lib/simple_form/inputs/base.rb', line 98

def input_class
  "#{lookup_model_names.join('_')}_#{reflection_or_attribute_name}"
end
```

    
  

    
      
  
### 
  
    #**input_options**  ⇒ Object 
  

  

  

  
    
      

```

90
91
92
```

    
    
      

```
# File 'lib/simple_form/inputs/base.rb', line 90

def input_options
  options
end
```