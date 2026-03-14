# Class: Formtastic::Inputs::HiddenInput
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Formtastic::Inputs::HiddenInput
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Base
  
  
  

  

  
  
    Defined in:
    lib/formtastic/inputs/hidden_input.rb
  
  

## Overview

  
    

Outputs a simple `<input type="hidden">` wrapped in the standard `<li>` wrapper. This is
provided for situations where a hidden field needs to be rendered in the flow of a form with
many inputs that form an `<ol>`. Wrapping the hidden input inside the `<li>` maintains the
HTML validity. The `<li>` is marked with a `class` of `hidden` so that stylesheet authors can
hide these list items with CSS (formtastic.css does this out of the box).

  

  
  
    
#### Examples:

    
      
        
##### 

Full form context, output and CSS

      
      

```

<%= semantic_form_for(@something) do |f| %>
  <%= f.inputs do %>
    <%= f.input :secret, :as => :hidden %>
  <% end %>
<% end %>

<form...>
  <fieldset>
    <ol>
      <li class="hidden">
        <input type="hidden" id="something_secret" name="something[secret]">
      </li>
    </ol>
  </fieldset>
</form>

form.formtastic li.hidden { display:none; }
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
  
    
      #**error_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**errors?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**hint?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**hint_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**input_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
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

  

#hint_text, #hint_text_from_options

  
  
  
  
  
  
  
  
  
### Methods included from Base::Errors

  

#error_first_html, #error_keys, #error_list_html, #error_none_html, #error_sentence_html, #errors

  
  
  
  
  
  
  
  
  
### Methods included from Base::Database

  

#column, #column?

  
  
  
  
  
  
  
  
  
### Methods included from Base::Options

  

#formtastic_options, #input_options

  
  
  
  
  
  
  
  
  
### Methods included from Base::Html

  

#dom_id, #dom_index

  
    
## Instance Method Details

    
      
  
### 
  
    #**error_html**  ⇒ Object 
  

  

  

  
    
      

```

45
46
47
```

    
    
      

```
# File 'lib/formtastic/inputs/hidden_input.rb', line 45

def error_html
  +""
end
```

    
  

    
      
  
### 
  
    #**errors?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

49
50
51
```

    
    
      

```
# File 'lib/formtastic/inputs/hidden_input.rb', line 49

def errors?
  false
end
```

    
  

    
      
  
### 
  
    #**hint?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

57
58
59
```

    
    
      

```
# File 'lib/formtastic/inputs/hidden_input.rb', line 57

def hint?
  false
end
```

    
  

    
      
  
### 
  
    #**hint_html**  ⇒ Object 
  

  

  

  
    
      

```

53
54
55
```

    
    
      

```
# File 'lib/formtastic/inputs/hidden_input.rb', line 53

def hint_html
  +""
end
```

    
  

    
      
  
### 
  
    #**input_html_options**  ⇒ Object 
  

  

  

  
    
      

```

35
36
37
```

    
    
      

```
# File 'lib/formtastic/inputs/hidden_input.rb', line 35

def input_html_options
  super.merge(:required => nil).merge(:autofocus => nil)
end
```

    
  

    
      
  
### 
  
    #**to_html**  ⇒ Object 
  

  

  

  
    
      

```

39
40
41
42
43
```

    
    
      

```
# File 'lib/formtastic/inputs/hidden_input.rb', line 39

def to_html
  input_wrapping do
    builder.hidden_field(method, input_html_options)
  end
end
```