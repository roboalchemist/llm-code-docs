# Class: Formtastic::Inputs::CountryInput
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Formtastic::Inputs::CountryInput
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Base
  
  
  

  

  
  
    Defined in:
    lib/formtastic/inputs/country_input.rb
  
  

## Overview

  
    

Outputs a country select input, wrapping around a regular country_select helper.
Rails doesn't come with a `country_select` helper by default any more, so you'll need to do
one of the following:

- install the country_select gem

- install any other country_select plugin that behaves in a similar way

- roll your own `country_select` helper with the same args and options as the Rails one

By default, Formtastic includes a handful of English-speaking countries as "priority
countries", which can be set in the `priority_countries` configuration array in the
formtastic.rb initializer to suit your market and user base (see README for more info on
configuration). Additionally, it is possible to set the :priority_countries on a per-input
basis through the `:priority_countries` option. These priority countries will be passed down
to the `country_select` helper of your choice, and may or may not be used by the helper.

  

  
  
    
#### Examples:

    
      
        
##### 

Basic example with full form context using `priority_countries` from config

      
      

```

<%= semantic_form_for @user do |f| %>
  <%= f.inputs do %>
    <%= f.input :nationality, :as => :country %>
  <% end %>
<% end %>

<li class='country'>
  <label for="user_nationality">Country</label>
  <select id="user_nationality" name="user[nationality]">
    <option value="...">...</option>
    # ...
</li>
```

    
      
        
##### 

`:priority_countries` set on a specific input (country_select 1.x)

      
      

```

<%= semantic_form_for @user do |f| %>
  <%= f.inputs do %>
    <%= f.input :nationality, :as => :country, :priority_countries => ["Australia", "New Zealand"] %>
  <% end %>
<% end %>

<li class='country'>
  <label for="user_nationality">Country</label>
  <select id="user_nationality" name="user[nationality]">
    <option value="...">...</option>
    # ...
</li>
```

    
      
        
##### 

`:priority_countries` set on a specific input (country_select 2.x)

      
      

```

<%= semantic_form_for @user do |f| %>
  <%= f.inputs do %>
    <%= f.input :nationality, :as => :country, :priority_countries => ["AU", "NZ"] %>
  <% end %>
<% end %>

<li class='country'>
  <label for="user_nationality">Country</label>
  <select id="user_nationality" name="user[nationality]">
    <option value="...">...</option>
    # ...
</li>
```

    
  

  

See Also:
  

    
      
- InputsHelper#input for full documentation of all possible options.
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        CountrySelectPluginMissing =
          
        
        

```
Class.new(StandardError)
```

      
    
  

  
## Instance Attribute Summary

  
  
### Attributes included from Base

  

#builder, #method, #object, #object_name, #options, #template

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**input_options_including_priorities**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**priority_countries**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
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
  
    #**input_options_including_priorities**  ⇒ Object 
  

  

  

  
    
      

```

78
79
80
81
82
```

    
    
      

```
# File 'lib/formtastic/inputs/country_input.rb', line 78

def input_options_including_priorities
  return input_options unless priority_countries

  input_options.merge(:priority_countries => priority_countries)
end
```

    
  

    
      
  
### 
  
    #**priority_countries**  ⇒ Object 
  

  

  

  
    
      

```

84
85
86
```

    
    
      

```
# File 'lib/formtastic/inputs/country_input.rb', line 84

def priority_countries
  options[:priority_countries] || builder.priority_countries
end
```

    
  

    
      
  
### 
  
    #**to_html**  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (CountrySelectPluginMissing)
      
      
      
    
  

  
    
      

```

70
71
72
73
74
75
76
```

    
    
      

```
# File 'lib/formtastic/inputs/country_input.rb', line 70

def to_html
  raise CountrySelectPluginMissing, "To use the :country input, please install a country_select plugin, like this one: https://github.com/countries/country_select" unless builder.respond_to?(:country_select)
  input_wrapping do
    label_html <<
    builder.country_select(method, input_options_including_priorities, input_html_options)
  end
end
```