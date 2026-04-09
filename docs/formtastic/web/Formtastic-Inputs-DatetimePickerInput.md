# Class: Formtastic::Inputs::DatetimePickerInput
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Formtastic::Inputs::DatetimePickerInput
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Base, Base::DatetimePickerish, Base::Stringish
  
  
  

  

  
  
    Defined in:
    lib/formtastic/inputs/datetime_picker_input.rb
  
  

## Overview

  
    

Outputs a simple `<label>` with a HTML5 `<input type="datetime-local">` (or 
`<input type="datetime">`) wrapped in the standard `<li>` wrapper. This is an alternative to 
`:date_select` for `:date`, `:time`, `:datetime` database columns. You can use this input with
`:as => :datetime_picker`.

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
    <%= f.input :publish_at, :as => :datetime_picker %>
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

Setting the size (defaults to 16 for YYYY-MM-DD HH:MM)

      
      

```
<%= f.input :publish_at, :as => :datetime_picker, :size => 20 %>
<%= f.input :publish_at, :as => :datetime_picker, :input_html => { :size => 20 } %>
```

    
      
        
##### 

Setting the maxlength (defaults to 16 for YYYY-MM-DD HH:MM)

      
      

```
<%= f.input :publish_at, :as => :datetime_picker, :maxlength => 20 %>
<%= f.input :publish_at, :as => :datetime_picker, :input_html => { :maxlength => 20 } %>
```

    
      
        
##### 

Setting the value (defaults to YYYY-MM-DD HH:MM for Date and Time objects, otherwise renders string)

      
      

```
<%= f.input :publish_at, :as => :datetime_picker, :input_html => { :value => "1970-01-01 00:00" } %>
```

    
      
        
##### 

Setting the step attribute (defaults to 1)

      
      

```
<%= f.input :publish_at, :as => :datetime_picker, :step => 60 %>
<%= f.input :publish_at, :as => :datetime_picker, :input_html => { :step => 60 } %>
```

    
      
        
##### 

Setting the step attribute with a macro

      
      

```
<%= f.input :publish_at, :as => :datetime_picker, :step => :second %>
<%= f.input :publish_at, :as => :datetime_picker, :step => :minute %>
<%= f.input :publish_at, :as => :datetime_picker, :step => :quarter_hour %>
<%= f.input :publish_at, :as => :datetime_picker, :step => :fifteen_minutes %>
<%= f.input :publish_at, :as => :datetime_picker, :step => :half_hour %>
<%= f.input :publish_at, :as => :datetime_picker, :step => :thirty_minutes %>
<%= f.input :publish_at, :as => :datetime_picker, :step => :hour %>
<%= f.input :publish_at, :as => :datetime_picker, :step => :sixty_minutes %>
```

    
      
        
##### 

Setting the min attribute

      
      

```
<%= f.input :publish_at, :as => :datetime_picker, :min => "2012-01-01 09:00" %>
<%= f.input :publish_at, :as => :datetime_picker, :input_html => { :min => "2012-01-01 09:00" } %>
```

    
      
        
##### 

Setting the max attribute

      
      

```
<%= f.input :publish_at, :as => :datetime_picker, :max => "2012-12-31 16:00" %>
<%= f.input :publish_at, :as => :datetime_picker, :input_html => { :max => "2012-12-31 16:00" } %>
```

    
      
        
##### 

Setting the placeholder attribute

      
      

```
<%= f.input :publish_at, :as => :datetime_picker, :placeholder => "YYYY-MM-DD HH:MM" %>
<%= f.input :publish_at, :as => :datetime_picker, :input_html => { :placeholder => "YYYY-MM-DD HH:MM" } %>
```

    
      
        
##### 

Using `type=datetime-local` with `:local` option (this is the default, and recommended for browser support on iOS7 and Chrome)

      
      

```
<%= f.input :publish_at, :as => :datetime_picker, :local => true %>
```

    
      
        
##### 

Using `type=datetime` with `:local` option (not recommended)

      
      

```
<%= f.input :publish_at, :as => :datetime_picker, :local => false %>
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
  
    
      #**html_input_type**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**value**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Base::DatetimePickerish

  

#default_maxlength, #default_step, #extra_input_html_options, #input_html_options, #maxlength, #size, #step

  
  
  
  
  
  
  
  
  
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

89
90
91
```

    
    
      

```
# File 'lib/formtastic/inputs/datetime_picker_input.rb', line 89

def default_size
  16
end
```

    
  

    
      
  
### 
  
    #**html_input_type**  ⇒ Object 
  

  

  

  
    
      

```

84
85
86
87
```

    
    
      

```
# File 'lib/formtastic/inputs/datetime_picker_input.rb', line 84

def html_input_type
  options[:local] = true unless options.key?(:local)
  options[:local] ? "datetime-local" : "datetime"
end
```

    
  

    
      
  
### 
  
    #**value**  ⇒ Object 
  

  

  

  
    
      

```

93
94
95
96
97
98
99
100
```

    
    
      

```
# File 'lib/formtastic/inputs/datetime_picker_input.rb', line 93

def value
  return options[:input_html][:value] if options[:input_html] && options[:input_html].key?(:value)
  val = object.send(method)
  return val.strftime("%Y-%m-%dT%H:%M:%S") if val.is_a?(Time)
  return "#{val.year}-#{val.month}-#{val.day}T00:00:00" if val.is_a?(Date)
  return val if val.nil?
  val.to_s
end
```