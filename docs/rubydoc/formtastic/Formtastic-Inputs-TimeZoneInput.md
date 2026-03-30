# Class: Formtastic::Inputs::TimeZoneInput
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Formtastic::Inputs::TimeZoneInput
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Base
  
  
  

  

  
  
    Defined in:
    lib/formtastic/inputs/time_zone_input.rb
  
  

## Overview

  
    

This is the default input choice for attributes matching /time_zone/, but can be applied to
any text-like input with `:as => :time_zone`.

The priority_zones option:
  Since this input actually uses Rails' `time_zone_select` helper, the :priority_zones
  option needs to be an array of ActiveSupport::TimeZone objects.

And you can configure default value using

```
    Formtastic::FormBuilder.priority_time_zones = [timezone1, timezone2]

```

See https://apidock.com/rails/ActionView/Helpers/FormOptionsHelper/time_zone_select for more information.

  

  
  
    
#### Examples:

    
      
        
##### 

Full form context and output

      
      

```

<%= semantic_form_for(@user) do |f| %>
  <%= f.inputs do %>
    <%= f.input :time_zone, :as => :time_zone %>
  <% end %>
<% end %>

<form...>
  <fieldset>
    <ol>
      <li class="time_zone">
        <label for="user_time_zone">Time zone</label>
        <input type="text" id="user_time_zone" name="user[time_zone]">
      </li>
    </ol>
  </fieldset>
</form>
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
  
    
      #**priority_zones**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
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

  

#dom_id, #dom_index, #input_html_options

  
    
## Instance Method Details

    
      
  
### 
  
    #**priority_zones**  ⇒ Object 
  

  

  

  
    
      

```

54
55
56
```

    
    
      

```
# File 'lib/formtastic/inputs/time_zone_input.rb', line 54

def priority_zones
  options[:priority_zones] || Formtastic::FormBuilder.priority_time_zones
end
```

    
  

    
      
  
### 
  
    #**to_html**  ⇒ Object 
  

  

  

  
    
      

```

47
48
49
50
51
52
```

    
    
      

```
# File 'lib/formtastic/inputs/time_zone_input.rb', line 47

def to_html
  input_wrapping do
    label_html <<
    builder.time_zone_select(method, priority_zones, input_options, input_html_options)
  end
end
```