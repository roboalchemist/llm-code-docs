# Class: Formtastic::Inputs::DateSelectInput
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Formtastic::Inputs::DateSelectInput
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Base, Base::Timeish
  
  
  

  

  
  
    Defined in:
    lib/formtastic/inputs/date_select_input.rb
  
  

## Overview

  
    

Outputs a series of select boxes for the fragments that make up a date (year, month, day).

  

  

  

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
  
    
      #**hidden_date_fragments**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**hidden_fragments**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**time_fragments**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

We don't want hour and minute fragments on a date input.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Base::Timeish

  

#date_fragments, #default_date_fragments, #fragment_id, #fragment_input_html, #fragment_label, #fragment_label_html, #fragment_name, #fragment_prefix, #fragment_wrapping, #fragment_wrapping_html_options, #fragments, #fragments_inner_wrapping, #fragments_label, #fragments_wrapping, #fragments_wrapping_html_options, #hidden_field_name, #i18n_date_fragments, #include_blank?, #position, #positions, #to_html, #value

  
  
  
  
  
  
  
  
  
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

26
27
28
29
30
31
32
```

    
    
      

```
# File 'lib/formtastic/inputs/date_select_input.rb', line 26

def fragment_value(fragment)
  if fragment == :year
    Time.now.year
  else
    '1'
  end
end
```

    
  

    
      
  
### 
  
    #**hidden_date_fragments**  ⇒ Object 
  

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/formtastic/inputs/date_select_input.rb', line 16

def hidden_date_fragments
  default_date_fragments - date_fragments
end
```

    
  

    
      
  
### 
  
    #**hidden_fragments**  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
23
24
```

    
    
      

```
# File 'lib/formtastic/inputs/date_select_input.rb', line 20

def hidden_fragments
  hidden_date_fragments.map do |fragment|
    template.hidden_field_tag(hidden_field_name(fragment), fragment_value(fragment), :id => fragment_id(fragment), :disabled => input_html_options[:disabled] )
  end.join.html_safe
end
```

    
  

    
      
  
### 
  
    #**time_fragments**  ⇒ Object 
  

  

  

  
    

We don't want hour and minute fragments on a date input

  

  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/formtastic/inputs/date_select_input.rb', line 12

def time_fragments
  []
end
```