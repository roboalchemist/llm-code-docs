# Class: Formtastic::Inputs::CheckBoxesInput
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Formtastic::Inputs::CheckBoxesInput
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Base, Base::Choices, Base::Collections
  
  
  

  

  
  
    Defined in:
    lib/formtastic/inputs/check_boxes_input.rb
  
  

## Overview

  
    
  
    **TODO:**
    

Do/can we support the per-item HTML options like RadioInput?

  

A CheckBoxes input is used to render a series of checkboxes. This is an alternative input choice
for `has_many` or `has_and_belongs_to_many` associations like a `Post` belonging to many
`categories` (by default, a `:select` input is used, allowing multiple selections).

Within the standard `<li>` wrapper, the output is a `<fieldset>` with a `<legend>` to
represent the "label" for the input, and an `<ol>` containing `<li>`s for each choice in
the association. Each `<li>` choice contains a hidden `<input>` tag for the "unchecked"
value (like Rails), and a `<label>` containing the checkbox `<input>` and the label text
for each choice.

  

  
  
    
#### Examples:

    
      
        
##### 

Basic example with full form context

      
      

```

<%= semantic_form_for @post do |f| %>
  <%= f.inputs do %>
    <%= f.input :categories, :as => :check_boxes %>
  <% end %>
<% end %>

<li class='check_boxes'>
  <fieldset>
    <legend class="label"><label>Categories</label></legend>
    <ol>
      <li>
        <input type="hidden" name="post[category_ids][1]" value="">
        <label for="post_category_ids_1"><input id="post_category_ids_1" name="post[category_ids][1]" type="checkbox" value="1" /> Ruby</label>
      </li>
      <li>
        <input type="hidden" name="post[category_ids][2]" value="">
        <label for="post_category_ids_2"><input id="post_category_ids_2" name="post[category_ids][2]" type="checkbox" value="2" /> Rails</label>
      </li>
    </ol>
  </fieldset>
</li>
```

    
      
        
##### 

`:collection` can be used to customize the choices

      
      

```
<%= f.input :categories, :as => :check_boxes, :collection => @categories %>
<%= f.input :categories, :as => :check_boxes, :collection => Category.all %>
<%= f.input :categories, :as => :check_boxes, :collection => Category.some_named_scope %>
<%= f.input :categories, :as => :check_boxes, :collection => Category.pluck(:label, :id) %>
<%= f.input :categories, :as => :check_boxes, :collection => [Category.find_by_name("Ruby"), Category.find_by_name("Rails")] %>
<%= f.input :categories, :as => :check_boxes, :collection => ["Ruby", "Rails"] %>
<%= f.input :categories, :as => :check_boxes, :collection => [["Ruby", "ruby"], ["Rails", "rails"]] %>
<%= f.input :categories, :as => :check_boxes, :collection => [["Ruby", "1"], ["Rails", "2"]] %>
<%= f.input :categories, :as => :check_boxes, :collection => [["Ruby", 1], ["Rails", 2]] %>
<%= f.input :categories, :as => :check_boxes, :collection => [["Ruby", 1, {'data-attr' => 'attr-value'}]] %>
<%= f.input :categories, :as => :check_boxes, :collection => 1..5 %>
<%= f.input :categories, :as => :check_boxes, :collection => [:ruby, :rails] %>
<%= f.input :categories, :as => :check_boxes, :collection => [["Ruby", :ruby], ["Rails", :rails]] %>
<%= f.input :categories, :as => :check_boxes, :collection => Set.new([:ruby, :rails]) %>
```

    
      
        
##### 

`:hidden_fields` can be used to skip Rails' rendering of a hidden field before every checkbox

      
      

```
<%= f.input :categories, :as => :check_boxes, :hidden_fields => false %>
```

    
      
        
##### 

`:disabled` can be used to disable any checkboxes with a value found in the given Array

      
      

```
<%= f.input :categories, :as => :check_boxes, :collection => ["a", "b"], :disabled => ["a"] %>
```

    
      
        
##### 

`:value_as_class` can be used to add a class to the `<li>` wrapped around each choice using the checkbox value for custom styling of each choice

      
      

```
<%= f.input :categories, :as => :check_boxes, :value_as_class => true %>
```

    
  

  

See Also:
  

    
      
- InputsHelper#input for full documentation of all possible options.
    
      
- BooleanInput for a single checkbox for boolean (checked = true) inputs
    
  

  
## Instance Attribute Summary

  
  
### Attributes included from Base

  

#builder, #method, #object, #object_name, #options, #template

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**check_box_with_hidden_input**(choice)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**check_box_without_hidden_input**(choice)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**checked?**(value)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**choice_html**(choice)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**disabled?**(value)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**disabled_values**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**extra_html_options**(choice)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**hidden_field_for_all**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**hidden_fields_for_every?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(*args)  ⇒ CheckBoxesInput 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of CheckBoxesInput.

  

      
        
- 
  
    
      #**input_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**selected_values**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**unchecked_value**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Base::Choices

  

#choice_html_options, #choice_html_safe_value, #choice_input_dom_id, #choice_label, #choice_value, #choice_wrapping, #choice_wrapping_html_options, #choices_group_wrapping, #choices_group_wrapping_html_options, #choices_wrapping, #choices_wrapping_html_options, #custom_choice_html_options, #default_choice_html_options, #label_html_options, #legend_html, #value_as_class?

  
  
  
  
  
  
  
  
  
### Methods included from Base::Collections

  

#collection, #collection_for_boolean, #collection_from_association, #collection_from_enum, #collection_from_enum?, #collection_from_options, #label_and_value_method, #label_and_value_method_from_collection, #label_method, #label_method_from_options, #raw_collection, #send_or_call, #send_or_call_or_object, #value_method, #value_method_from_options

  
  
  
  
  
  
  
  
  
### Methods included from Base

  

#removed_option!, #warn_and_correct_option!, #warn_deprecated_option!

  
  
  
  
  
  
  
  
  
  
### Methods included from Base::Aria

  

#describedby, #error_aria_attributes

  
  
  
  
  
  
  
  
  
### Methods included from Base::Wrapping

  

#input_wrapping, #wrapper_classes, #wrapper_classes_raw, #wrapper_dom_id, #wrapper_html_options, #wrapper_html_options_raw

  
  
  
  
  
  
  
  
  
### Methods included from Base::Labelling

  

#label_from_options, #label_html, #label_html_options, #label_text, #localized_label, #render_label?, #requirement_text, #requirement_text_or_proc

  
  
  
  
  
  
  
  
  
### Methods included from LocalizedString

  

#model_name

  
  
  
  
  
  
  
  
  
### Methods included from Base::Associations

  

#association, #association_primary_key, #belongs_to?, #has_many?, #reflection

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from Base::Fileish

  

#file?

  
  
  
  
  
  
  
  
  
### Methods included from Base::Validations

  

#autofocus?, #column_limit, #limit, #not_required_through_negated_validation!, #not_required_through_negated_validation?, #optional?, #readonly?, #readonly_attribute?, #readonly_from_options?, #required?, #required_attribute?, #responds_to_global_required?, #validation_integer_only?, #validation_limit, #validation_max, #validation_min, #validation_step, #validations, #validations?, #validator_relevant?

  
  
  
  
  
  
  
  
  
### Methods included from Base::Naming

  

#as, #attributized_method_name, #humanized_method_name, #sanitized_method_name, #sanitized_object_name

  
  
  
  
  
  
  
  
  
### Methods included from Base::Hints

  

#hint?, #hint_html, #hint_text, #hint_text_from_options

  
  
  
  
  
  
  
  
  
### Methods included from Base::Errors

  

#error_first_html, #error_html, #error_keys, #error_list_html, #error_none_html, #error_sentence_html, #errors, #errors?

  
  
  
  
  
  
  
  
  
### Methods included from Base::Database

  

#column, #column?

  
  
  
  
  
  
  
  
  
### Methods included from Base::Options

  

#formtastic_options, #input_options

  
  
  
  
  
  
  
  
  
### Methods included from Base::Html

  

#dom_id, #dom_index, #input_html_options

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(*args)  ⇒ CheckBoxesInput 
  

  

  

  
    

Returns a new instance of CheckBoxesInput.

  

  

Raises:

  
    
- 
      
      
        (Formtastic::UnsupportedEnumCollection)
      
      
      
    
  

  
    
      

```

73
74
75
76
```

    
    
      

```
# File 'lib/formtastic/inputs/check_boxes_input.rb', line 73

def initialize(*args)
  super
  raise Formtastic::UnsupportedEnumCollection if collection_from_enum?
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**check_box_with_hidden_input**(choice)  ⇒ Object 
  

  

  

  
    
      

```

117
118
119
120
121
122
123
124
125
```

    
    
      

```
# File 'lib/formtastic/inputs/check_boxes_input.rb', line 117

def check_box_with_hidden_input(choice)
  value = choice_value(choice)
  builder.check_box(
    association_primary_key || method,
    extra_html_options(choice).merge(:id => choice_input_dom_id(choice), :name => input_name, :disabled => disabled?(value), :required => false),
    value,
    unchecked_value
  )
end
```

    
  

    
      
  
### 
  
    #**check_box_without_hidden_input**(choice)  ⇒ Object 
  

  

  

  
    
      

```

127
128
129
130
131
132
133
134
135
```

    
    
      

```
# File 'lib/formtastic/inputs/check_boxes_input.rb', line 127

def check_box_without_hidden_input(choice)
  value = choice_value(choice)
  template.check_box_tag(
    input_name,
    value,
    checked?(value),
    extra_html_options(choice).merge(:id => choice_input_dom_id(choice), :disabled => disabled?(value), :required => false)
  )
end
```

    
  

    
      
  
### 
  
    #**checked?**(value)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

141
142
143
```

    
    
      

```
# File 'lib/formtastic/inputs/check_boxes_input.rb', line 141

def checked?(value)
  selected_values.include?(value)
end
```

    
  

    
      
  
### 
  
    #**choice_html**(choice)  ⇒ Object 
  

  

  

  
    
      

```

94
95
96
97
98
99
100
```

    
    
      

```
# File 'lib/formtastic/inputs/check_boxes_input.rb', line 94

def choice_html(choice)
  template.content_tag(
    :label,
    checkbox_input(choice) + choice_label(choice),
    label_html_options.merge(:for => choice_input_dom_id(choice), :class => nil)
  )
end
```

    
  

    
      
  
### 
  
    #**disabled?**(value)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

145
146
147
```

    
    
      

```
# File 'lib/formtastic/inputs/check_boxes_input.rb', line 145

def disabled?(value)
  disabled_values.include?(value)
end
```

    
  

    
      
  
### 
  
    #**disabled_values**  ⇒ Object 
  

  

  

  
    
      

```

153
154
155
156
157
```

    
    
      

```
# File 'lib/formtastic/inputs/check_boxes_input.rb', line 153

def disabled_values
  vals = options[:disabled] || []
  vals = [vals] unless vals.is_a?(Array)
  vals
end
```

    
  

    
      
  
### 
  
    #**extra_html_options**(choice)  ⇒ Object 
  

  

  

  
    
      

```

137
138
139
```

    
    
      

```
# File 'lib/formtastic/inputs/check_boxes_input.rb', line 137

def extra_html_options(choice)
  input_html_options.merge(custom_choice_html_options(choice))
end
```

    
  

    
      
  
### 
  
    #**hidden_field_for_all**  ⇒ Object 
  

  

  

  
    
      

```

102
103
104
105
106
107
108
109
110
111
```

    
    
      

```
# File 'lib/formtastic/inputs/check_boxes_input.rb', line 102

def hidden_field_for_all
  if hidden_fields_for_every?
    +''
  else
    options = {}
    options[:class] = [method.to_s.singularize, 'default'].join('_') if value_as_class?
    options[:id] = [object_name, method, 'none'].join('_')
    template.hidden_field_tag(input_name, '', options)
  end
end
```

    
  

    
      
  
### 
  
    #**hidden_fields_for_every?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

113
114
115
```

    
    
      

```
# File 'lib/formtastic/inputs/check_boxes_input.rb', line 113

def hidden_fields_for_every?
  options[:hidden_fields]
end
```

    
  

    
      
  
### 
  
    #**input_name**  ⇒ Object 
  

  

  

  
    
      

```

163
164
165
166
167
168
169
```

    
    
      

```
# File 'lib/formtastic/inputs/check_boxes_input.rb', line 163

def input_name
  if builder.options.key?(:index)
    "#{object_name}[#{builder.options[:index]}][#{association_primary_key || method}][]"
  else
    "#{object_name}[#{association_primary_key || method}][]"
  end
end
```

    
  

    
      
  
### 
  
    #**selected_values**  ⇒ Object 
  

  

  

  
    
      

```

149
150
151
```

    
    
      

```
# File 'lib/formtastic/inputs/check_boxes_input.rb', line 149

def selected_values
  @selected_values ||= make_selected_values
end
```

    
  

    
      
  
### 
  
    #**to_html**  ⇒ Object 
  

  

  

  
    
      

```

78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
```

    
    
      

```
# File 'lib/formtastic/inputs/check_boxes_input.rb', line 78

def to_html
  input_wrapping do
    choices_wrapping do
      legend_html <<
      hidden_field_for_all <<
      choices_group_wrapping do
        collection.map { |choice|
          choice_wrapping(choice_wrapping_html_options(choice)) do
            choice_html(choice)
          end
        }.join("\n").html_safe
      end
    end
  end
end
```

    
  

    
      
  
### 
  
    #**unchecked_value**  ⇒ Object 
  

  

  

  
    
      

```

159
160
161
```

    
    
      

```
# File 'lib/formtastic/inputs/check_boxes_input.rb', line 159

def unchecked_value
  options[:unchecked_value] || ''
end
```