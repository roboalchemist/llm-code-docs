# Class: Formtastic::Inputs::FileInput
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Formtastic::Inputs::FileInput
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Base
  
  
  

  

  
  
    Defined in:
    lib/formtastic/inputs/file_input.rb
  
  

## Overview

  
    

Outputs a simple `<label>` with a `<input type="file">` wrapped in the standard
`<li>` wrapper. This is the default input choice for objects with attributes that appear
to be for file uploads, by detecting some common method names used by popular file upload
libraries such as Paperclip and CarrierWave. You can add to or alter these method names
through the `file_methods` config, but can be applied to any input with `:as => :file`.

Don't forget to set the multipart attribute in your `<form>` tag!

  

  
  
    
#### Examples:

    
      
        
##### 

Full form context and output

      
      

```

<%= semantic_form_for(@user, :html => { :multipart => true }) do |f| %>
  <%= f.inputs do %>
    <%= f.input :avatar, :as => :file %>
  <% end %>
<% end %>

<form...>
  <fieldset>
    <ol>
      <li class="file">
        <label for="user_avatar">Avatar</label>
        <input type="file" id="user_avatar" name="user[avatar]">
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
  
    #**to_html**  ⇒ Object 
  

  

  

  
    
      

```

35
36
37
38
39
40
```

    
    
      

```
# File 'lib/formtastic/inputs/file_input.rb', line 35

def to_html
  input_wrapping do
    label_html <<
    builder.file_field(method, input_html_options)
  end
end
```