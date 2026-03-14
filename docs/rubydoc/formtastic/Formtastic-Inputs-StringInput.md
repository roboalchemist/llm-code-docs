# Class: Formtastic::Inputs::StringInput
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Formtastic::Inputs::StringInput
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Base, Base::Placeholder, Base::Stringish
  
  
  

  

  
  
    Defined in:
    lib/formtastic/inputs/string_input.rb
  
  

## Overview

  
    

Outputs a simple `<label>` with a `<input type="text">` wrapped in the standard
`<li>` wrapper. This is the default input choice for database columns of the `:string` type,
and is the default choice for all inputs when no other logical input type can be inferred.
You can force any input to be a string input with `:as => :string`.

  

  
  
    
#### Examples:

    
      
        
##### 

Full form context and output

      
      

```

<%= semantic_form_for(@user) do |f| %>
  <%= f.inputs do %>
    <%= f.input :first_name, :as => :string %>
  <% end %>
<% end %>

<form...>
  <fieldset>
    <ol>
      <li class="string">
        <label for="user_first_name">First name</label>
        <input type="text" id="user_first_name" name="user[first_name]">
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

  
  
  
  
  
  
  
## Method Summary

  
  
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