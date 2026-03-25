# Class: Formtastic::Inputs::TimeSelectInput
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Formtastic::Inputs::TimeSelectInput
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Base, Base::Timeish
  
  
  

  

  
  
    Defined in:
    lib/formtastic/inputs/time_select_input.rb
  
  

## Overview

  
    

Outputs a series of select boxes for the fragments that make up a time (hour, minute, second).
Unless `:ignore_date` is true, it will render hidden inputs for the year, month and day as 
well, defaulting to `Time.current` if the form object doesn't have a value, much like Rails' 
own `time_select`.

  

  

  

See Also:
  

    
      
- Timeish module for documentation of date, time and datetime input options.
    
  

  
## Instance Attribute Summary

  
  
### Attributes included from Base

  

#builder, #method, #object, #object_name, #options, #template

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**fragment_value**(fragment)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fragments**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

we don't want year / month / day fragments if :ignore_date => true.

  

      
        
- 
  
    
      #**hidden_fragments**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**value_or_default_value**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Base::Timeish

  

#date_fragments, #default_date_fragments, #fragment_id, #fragment_input_html, #fragment_label, #fragment_label_html, #fragment_name, #fragment_prefix, #fragment_wrapping, #fragment_wrapping_html_options, #fragments_inner_wrapping, #fragments_label, #fragments_wrapping, #fragments_wrapping_html_options, #hidden_field_name, #i18n_date_fragments, #include_blank?, #position, #positions, #time_fragments, #to_html, #value

  
  
  
  
  
  
  
  
  
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
  
    #**fragment_value**(fragment)  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/formtastic/inputs/time_select_input.rb', line 23

def fragment_value(fragment)
  value_or_default_value.send(fragment)
end
```

    
  

    
      
  
### 
  
    #**fragments**  ⇒ Object 
  

  

  

  
    

we don't want year / month / day fragments if :ignore_date => true

  

  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/formtastic/inputs/time_select_input.rb', line 15

def fragments
  time_fragments
end
```

    
  

    
      
  
### 
  
    #**hidden_fragments**  ⇒ Object 
  

  

  

  
    
      

```

27
28
29
30
31
32
33
34
35
```

    
    
      

```
# File 'lib/formtastic/inputs/time_select_input.rb', line 27

def hidden_fragments
  if !options[:ignore_date]
    date_fragments.map do |fragment|
      template.hidden_field_tag(hidden_field_name(fragment), fragment_value(fragment), :id => fragment_id(fragment), :disabled => input_html_options[:disabled] )
    end.join.html_safe
  else
    super
  end
end
```

    
  

    
      
  
### 
  
    #**value_or_default_value**  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
```

    
    
      

```
# File 'lib/formtastic/inputs/time_select_input.rb', line 19

def value_or_default_value
  value ? value : Time.current
end
```