# Class: Formtastic::Inputs::BooleanInput
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Formtastic::Inputs::BooleanInput
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Base
  
  
  

  

  
  
    Defined in:
    lib/formtastic/inputs/boolean_input.rb
  
  

## Overview

  
    

Boolean inputs are used to render an input for a single checkbox, typically for attributes
with a simple yes/no or true/false value. Boolean inputs are used by default for boolean
database columns.

  

  
  
    
#### Examples:

    
      
        
##### 

Full form context and markup

      
      

```
<%= semantic_form_for @post %>
  <%= f.inputs do %>
    <%= f.input :published, :as => :boolean %>
  <% end %>
<% end %>

<form...>
  <fieldset>
    <ol>
      <li class="boolean" id="post_published_input">
        <input type="hidden" name="post[published]" id="post_published" value="0">
        <label for="post_published">
          <input type="checkbox" name="post[published]" id="post_published" value="1">
          Published?
        </label>
      </li>
    </ol>
  </fieldset>
</form>
```

    
      
        
##### 

Set the values for the checked and unchecked states

      
      

```
<%= f.input :published, :checked_value => "yes", :unchecked_value => "no" %>
```

    
  

  

See Also:
  

    
      
- InputsHelper#input for full documentation of all possible options.
    
  

  
## Instance Attribute Summary

  
  
### Attributes included from Base

  

#builder, #method, #object, #object_name, #options, #template

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**check_box_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**checked?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**checked_value**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**hidden_field_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**input_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**input_html_options_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**label_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**label_text_with_embedded_checkbox**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**label_with_nested_checkbox**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**responds_to_global_required?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**unchecked_value**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Base

  

#initialize, #removed_option!, #warn_and_correct_option!, #warn_deprecated_option!

  
  
  
  
  
  
  
  
  
  
### Methods included from Formtastic::Inputs::Base::Aria

  

#describedby, #error_aria_attributes

  
  
  
  
  
  
  
  
  
### Methods included from Formtastic::Inputs::Base::Wrapping

  

#input_wrapping, #wrapper_classes, #wrapper_classes_raw, #wrapper_dom_id, #wrapper_html_options, #wrapper_html_options_raw

  
  
  
  
  
  
  
  
  
### Methods included from Formtastic::Inputs::Base::Labelling

  

#label_from_options, #label_html, #label_text, #localized_label, #render_label?, #requirement_text, #requirement_text_or_proc

  
  
  
  
  
  
  
  
  
### Methods included from LocalizedString

  

#model_name

  
  
  
  
  
  
  
  
  
### Methods included from Formtastic::Inputs::Base::Associations

  

#association, #association_primary_key, #belongs_to?, #has_many?, #reflection

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from Formtastic::Inputs::Base::Fileish

  

#file?

  
  
  
  
  
  
  
  
  
### Methods included from Formtastic::Inputs::Base::Validations

  

#autofocus?, #column_limit, #limit, #not_required_through_negated_validation!, #not_required_through_negated_validation?, #optional?, #readonly?, #readonly_attribute?, #readonly_from_options?, #required?, #required_attribute?, #validation_integer_only?, #validation_limit, #validation_max, #validation_min, #validation_step, #validations, #validations?, #validator_relevant?

  
  
  
  
  
  
  
  
  
### Methods included from Formtastic::Inputs::Base::Naming

  

#as, #attributized_method_name, #humanized_method_name, #input_name, #sanitized_method_name, #sanitized_object_name

  
  
  
  
  
  
  
  
  
### Methods included from Formtastic::Inputs::Base::Hints

  

#hint?, #hint_html, #hint_text, #hint_text_from_options

  
  
  
  
  
  
  
  
  
### Methods included from Formtastic::Inputs::Base::Errors

  

#error_first_html, #error_html, #error_keys, #error_list_html, #error_none_html, #error_sentence_html, #errors, #errors?

  
  
  
  
  
  
  
  
  
### Methods included from Formtastic::Inputs::Base::Database

  

#column, #column?

  
  
  
  
  
  
  
  
  
### Methods included from Formtastic::Inputs::Base::Options

  

#formtastic_options, #input_options

  
  
  
  
  
  
  
  
  
### Methods included from Formtastic::Inputs::Base::Html

  

#dom_id, #dom_index

  
    
## Instance Method Details

    
      
  
### 
  
    #**check_box_html**  ⇒ Object 
  

  

  

  
    
      

```

66
67
68
```

    
    
      

```
# File 'lib/formtastic/inputs/boolean_input.rb', line 66

def check_box_html
  template.check_box_tag("#{object_name}[#{method}]", checked_value, checked?, input_html_options)
end
```

    
  

    
      
  
### 
  
    #**checked?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

94
95
96
```

    
    
      

```
# File 'lib/formtastic/inputs/boolean_input.rb', line 94

def checked?
  object && boolean_checked?(object.send(method), checked_value) 
end
```

    
  

    
      
  
### 
  
    #**checked_value**  ⇒ Object 
  

  

  

  
    
      

```

74
75
76
```

    
    
      

```
# File 'lib/formtastic/inputs/boolean_input.rb', line 74

def checked_value
  options[:checked_value] || '1'
end
```

    
  

    
      
  
### 
  
    #**hidden_field_html**  ⇒ Object 
  

  

  

  
    
      

```

43
44
45
```

    
    
      

```
# File 'lib/formtastic/inputs/boolean_input.rb', line 43

def hidden_field_html
  template.hidden_field_tag(input_html_options[:name], unchecked_value, :id => nil, :disabled => input_html_options[:disabled] )
end
```

    
  

    
      
  
### 
  
    #**input_html_options**  ⇒ Object 
  

  

  

  
    
      

```

82
83
84
```

    
    
      

```
# File 'lib/formtastic/inputs/boolean_input.rb', line 82

def input_html_options
  {:name => input_html_options_name}.merge(super)
end
```

    
  

    
      
  
### 
  
    #**input_html_options_name**  ⇒ Object 
  

  

  

  
    
      

```

86
87
88
89
90
91
92
```

    
    
      

```
# File 'lib/formtastic/inputs/boolean_input.rb', line 86

def input_html_options_name
  if builder.options.key?(:index)
    "#{object_name}[#{builder.options[:index]}][#{method}]"
  else
    "#{object_name}[#{method}]"
  end
end
```

    
  

    
      
  
### 
  
    #**label_html_options**  ⇒ Object 
  

  

  

  
    
      

```

55
56
57
58
59
60
```

    
    
      

```
# File 'lib/formtastic/inputs/boolean_input.rb', line 55

def label_html_options
  {
    :for => input_html_options[:id],
    :class => super[:class] - ['label'] # remove 'label' class
  }
end
```

    
  

    
      
  
### 
  
    #**label_text_with_embedded_checkbox**  ⇒ Object 
  

  

  

  
    
      

```

62
63
64
```

    
    
      

```
# File 'lib/formtastic/inputs/boolean_input.rb', line 62

def label_text_with_embedded_checkbox
  check_box_html << +"" << label_text
end
```

    
  

    
      
  
### 
  
    #**label_with_nested_checkbox**  ⇒ Object 
  

  

  

  
    
      

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
# File 'lib/formtastic/inputs/boolean_input.rb', line 47

def label_with_nested_checkbox
  builder.label(
    method,
    label_text_with_embedded_checkbox,
    label_html_options
  )
end
```

    
  

    
      
  
### 
  
    #**responds_to_global_required?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

78
79
80
```

    
    
      

```
# File 'lib/formtastic/inputs/boolean_input.rb', line 78

def responds_to_global_required?
  false
end
```

    
  

    
      
  
### 
  
    #**to_html**  ⇒ Object 
  

  

  

  
    
      

```

36
37
38
39
40
41
```

    
    
      

```
# File 'lib/formtastic/inputs/boolean_input.rb', line 36

def to_html
  input_wrapping do
    hidden_field_html <<
    label_with_nested_checkbox
  end
end
```

    
  

    
      
  
### 
  
    #**unchecked_value**  ⇒ Object 
  

  

  

  
    
      

```

70
71
72
```

    
    
      

```
# File 'lib/formtastic/inputs/boolean_input.rb', line 70

def unchecked_value
  options[:unchecked_value] || '0'
end
```