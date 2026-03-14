# Class: Formtastic::Inputs::TimePickerInput
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Formtastic::Inputs::TimePickerInput
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Base, Base::DatetimePickerish, Base::Stringish
  
  
  

  

  
  
    Defined in:
    lib/formtastic/inputs/time_picker_input.rb
  
  

## Overview

  
    

Outputs a simple `<label>` with a HTML5 `<input type="time">` wrapped in the standard
`<li>` wrapper. This is an alternative to `:time_select` for `:date`, `:time`, `:datetime` 
database columns. You can use this input with `:as => :time_picker`.

*Please note:* Formtastic only provides suitable markup for a date picker, but does not supply
any additional CSS or Javascript to render calendar-style date pickers. Browsers that support
this input type (such as Mobile Webkit and Opera on the desktop) will render a native widget.
Browsers that don't will default to a plain text field`<input type="text">` and can be 
poly-filled with some Javascript and a UI library of your choice.

  

  
  
    
#### Examples:

    
      
        
##### 

Full form context and output

      
      

```

<%= semantic_form_for(@post) do |f| %>
  <%= f.inputs do %>
    <%= f.input :publish_at, :as => :time_picker %>
  <% end %>
<% end %>

<form...>
  <fieldset>
    <ol>
      <li class="string">
        <label for="post_publish_at">First name</label>
        <input type="date" id="post_publish_at" name="post[publish_at]">
      </li>
    </ol>
  </fieldset>
</form>
```

    
      
        
##### 

Setting the size (defaults to 5 for HH:MM)

      
      

```
<%= f.input :publish_at, :as => :time_picker, :size => 20 %>
<%= f.input :publish_at, :as => :time_picker, :input_html => { :size => 20 } %>
```

    
      
        
##### 

Setting the maxlength (defaults to 5 for HH:MM)

      
      

```
<%= f.input :publish_at, :as => :time_picker, :maxlength => 20 %>
<%= f.input :publish_at, :as => :time_picker, :input_html => { :maxlength => 20 } %>
```

    
      
        
##### 

Setting the value (defaults to HH:MM for Date and Time objects, otherwise renders string)

      
      

```
<%= f.input :publish_at, :as => :time_picker, :input_html => { :value => "14:14" } %>
```

    
      
        
##### 

Setting the step attribute (defaults to 60)

      
      

```
<%= f.input :publish_at, :as => :time_picker, :step => 120 %>
<%= f.input :publish_at, :as => :time_picker, :input_html => { :step => 120 } %>
```

    
      
        
##### 

Setting the step attribute with a macro

      
      

```
<%= f.input :publish_at, :as => :time_picker, :step => :second %>
<%= f.input :publish_at, :as => :time_picker, :step => :minute %>
<%= f.input :publish_at, :as => :time_picker, :step => :quarter_hour %>
<%= f.input :publish_at, :as => :time_picker, :step => :fifteen_minutes %>
<%= f.input :publish_at, :as => :time_picker, :step => :half_hour %>
<%= f.input :publish_at, :as => :time_picker, :step => :thirty_minutes %>
<%= f.input :publish_at, :as => :time_picker, :step => :hour %>
<%= f.input :publish_at, :as => :time_picker, :step => :sixty_minutes %>
```

    
      
        
##### 

Setting the min attribute

      
      

```
<%= f.input :publish_at, :as => :time_picker, :min => "09:00" %>
<%= f.input :publish_at, :as => :time_picker, :input_html => { :min => "01:00" } %>
```

    
      
        
##### 

Setting the max attribute

      
      

```
<%= f.input :publish_at, :as => :time_picker, :max => "18:00" %>
<%= f.input :publish_at, :as => :time_picker, :input_html => { :max => "18:00" } %>
```

    
      
        
##### 

Setting the placeholder attribute

      
      

```
<%= f.input :publish_at, :as => :time_picker, :placeholder => "HH:MM" %>
<%= f.input :publish_at, :as => :time_picker, :input_html => { :placeholder => "HH:MM" } %>
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
  
    
      #**default_size**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**default_step**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**html_input_type**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**value**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Base::DatetimePickerish

  

#default_maxlength, #extra_input_html_options, #input_html_options, #maxlength, #size, #step

  
  
  
  
  
  
  
  
  
### Methods included from Base::Placeholder

  

#input_html_options, #placeholder_text

  
  
  
  
  
  
  
  
  
### Methods included from Base::Stringish

  

#input_html_options, #maxlength, #size, #to_html, #wrapper_html_options

  
  
  
  
  
  
  
  
  
### Methods included from Base

  

#initialize, #removed_option!, #warn_and_correct_option!, #warn_deprecated_option!

  
  
  
  
  
  
  
  
  
  
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

  

#as, #attributized_method_name, #humanized_method_name, #input_name, #sanitized_method_name, #sanitized_object_name

  
  
  
  
  
  
  
  
  
### Methods included from Base::Hints

  

#hint?, #hint_html, #hint_text, #hint_text_from_options

  
  
  
  
  
  
  
  
  
### Methods included from Base::Errors

  

#error_first_html, #error_html, #error_keys, #error_list_html, #error_none_html, #error_sentence_html, #errors, #errors?

  
  
  
  
  
  
  
  
  
### Methods included from Base::Database

  

#column, #column?

  
  
  
  
  
  
  
  
  
### Methods included from Base::Options

  

#formtastic_options, #input_options

  
  
  
  
  
  
  
  
  
### Methods included from Base::Html

  

#dom_id, #dom_index, #input_html_options, #to_html

  
    
## Instance Method Details

    
      
  
### 
  
    #**default_size**  ⇒ Object 
  

  

  

  
    
      

```

81
82
83
```

    
    
      

```
# File 'lib/formtastic/inputs/time_picker_input.rb', line 81

def default_size
  5
end
```

    
  

    
      
  
### 
  
    #**default_step**  ⇒ Object 
  

  

  

  
    
      

```

94
95
96
```

    
    
      

```
# File 'lib/formtastic/inputs/time_picker_input.rb', line 94

def default_step
  60
end
```

    
  

    
      
  
### 
  
    #**html_input_type**  ⇒ Object 
  

  

  

  
    
      

```

77
78
79
```

    
    
      

```
# File 'lib/formtastic/inputs/time_picker_input.rb', line 77

def html_input_type
  "time"
end
```

    
  

    
      
  
### 
  
    #**value**  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/formtastic/inputs/time_picker_input.rb', line 85

def value
  return options[:input_html][:value] if options[:input_html] && options[:input_html].key?(:value)
  val = object.send(method)
  return "00:00" if val.is_a?(Date)
  return val.strftime("%H:%M") if val.is_a?(Time)
  return val if val.nil?
  val.to_s
end
```