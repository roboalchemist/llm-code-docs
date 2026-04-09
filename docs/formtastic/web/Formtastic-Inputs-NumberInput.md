# Class: Formtastic::Inputs::NumberInput
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Formtastic::Inputs::NumberInput
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Base, Base::Numeric, Base::Placeholder
  
  
  

  

  
  
    Defined in:
    lib/formtastic/inputs/number_input.rb
  
  

## Overview

  
    

Outputs a simple `<label>` with a HTML5 `<input type="number">` wrapped in the standard
`<li>` wrapper. This is the default input choice for all database columns of the type `:float`
and `:decimal`, as well as `:integer` columns that aren't used for `belongs_to` associations,
but can be applied to any text-like input with `:as => :number`.

Sensible default values for the `min`, `max` and `step` attributes are found by reflecting on 
the model's validations (when provided). An `IndeterminableMinimumAttributeError` exception 
will be raised when the following conditions are all true:

- you haven't specified a `:min` or `:max` for the input

- the model's database column type is a `:float` or `:decimal`

- the validation uses `:less_than` or `:greater_than`

The solution is to either:

- manually specify the `:min` or `:max` for the input

- change the database column type to an `:integer` (if appropriate)

- change the validations to use `:less_than_or_equal_to` or `:greater_than_or_equal_to`

  

  
  
    
#### Examples:

    
      
        
##### 

Full form context and output

      
      

```

<%= semantic_form_for(@user) do |f| %>
  <%= f.inputs do %>
    <%= f.input :shoe_size, :as => :number %>
  <% end %>
<% end %>

<form...>
  <fieldset>
    <ol>
      <li class="numeric">
        <label for="user_shoe_size">Shoe size</label>
        <input type="number" id="user_shoe_size" name="user[shoe_size]">
      </li>
    </ol>
  </fieldset>
</form>
```

    
      
        
##### 

Default HTML5 min/max/step attributes are detected from the numericality validations

      
      

```

class Person < ActiveRecord::Base
  validates_numericality_of :age, 
    :less_than_or_equal_to => 100, 
    :greater_than_or_equal_to => 18, 
    :only_integer => true
end

<%= f.input :age, :as => :number %>

<li class="numeric">
  <label for="persom_age">Age</label>
  <input type="number" id="person_age" name="person[age]" min="18" max="100" step="1">
</li>
```

    
      
        
##### 

Pass attributes down to the `<input>` tag with :input_html

      
      

```
<%= f.input :shoe_size, :as => :number, :input_html => { :min => 3, :max => 15, :step => 1, :class => "special" } %>
```

    
      
        
##### 

Min/max/step also work as options

      
      

```
<%= f.input :shoe_size, :as => :number, :min => 3, :max => 15, :step => 1, :input_html => { :class => "special" } %>
```

    
      
        
##### 

Use :in with a Range as a shortcut for :min/:max

      
      

```
<%= f.input :shoe_size, :as => :number, :in => 3..15, :step => 1 %>
<%= f.input :shoe_size, :as => :number, :input_html => { :in => 3..15, :step => 1 } %>
```

    
  

  

See Also:
  

    
      
- InputsHelper#input for full documentation of all possible options.
    
      
- Rails' Numericality validation documentation
    
  

  
## Instance Attribute Summary

  
  
### Attributes included from Base

  

#builder, #method, #object, #object_name, #options, #template

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**step_option**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Base::Placeholder

  

#input_html_options, #placeholder_text

  
  
  
  
  
  
  
  
  
### Methods included from Base::Numeric

  

#in_option, #input_html_options, #max_option, #min_option, #wrapper_html_options

  
  
  
  
  
  
  
  
  
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
  
    #**step_option**  ⇒ Object 
  

  

  

  
    
      

```

83
84
85
```

    
    
      

```
# File 'lib/formtastic/inputs/number_input.rb', line 83

def step_option
  super || "any"
end
```

    
  

    
      
  
### 
  
    #**to_html**  ⇒ Object 
  

  

  

  
    
      

```

76
77
78
79
80
81
```

    
    
      

```
# File 'lib/formtastic/inputs/number_input.rb', line 76

def to_html
  input_wrapping do
    label_html <<
    builder.number_field(method, input_html_options)
  end
end
```