# Class: Formtastic::Inputs::DatalistInput
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Formtastic::Inputs::DatalistInput
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Base, Base::Collections, Base::Stringish
  
  
  

  

  
  
    Defined in:
    lib/formtastic/inputs/datalist_input.rb
  
  

## Overview

  
    

Outputs a label and a text field, along with a datalist tag
datalist tag provides a list of options which drives a simple autocomplete
on the text field. This is a HTML5 feature, more info can be found at
 at MDN
This input accepts a :collection option which takes data in all the usual formats accepted by
options_for_select

  

  
  
    
#### Examples:

    
      
        
##### 

Input is used as follows

      
      

```
f.input :fav_book, :as => :datalist, :collection => Book.pluck(:name)
```

    
  

  
## Instance Attribute Summary

  
  
### Attributes included from Base

  

#builder, #method, #object, #object_name, #options, #template

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**data_list_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**html_id_of_datalist**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**input_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Base::Collections

  

#collection, #collection_for_boolean, #collection_from_association, #collection_from_enum, #collection_from_enum?, #collection_from_options, #label_and_value_method, #label_and_value_method_from_collection, #label_method, #label_method_from_options, #raw_collection, #send_or_call, #send_or_call_or_object, #value_method, #value_method_from_options

  
  
  
  
  
  
  
  
  
### Methods included from Base::Stringish

  

#maxlength, #size, #wrapper_html_options

  
  
  
  
  
  
  
  
  
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

  

#dom_id, #dom_index

  
    
## Instance Method Details

    
      
  
### 
  
    #**data_list_html**  ⇒ Object 
  

  

  

  
    
      

```

36
37
38
39
```

    
    
      

```
# File 'lib/formtastic/inputs/datalist_input.rb', line 36

def data_list_html
  html = builder.template.options_for_select(collection)
  builder.template.content_tag(:datalist,html, { :id => html_id_of_datalist }, false)
end
```

    
  

    
      
  
### 
  
    #**html_id_of_datalist**  ⇒ Object 
  

  

  

  
    
      

```

32
33
34
```

    
    
      

```
# File 'lib/formtastic/inputs/datalist_input.rb', line 32

def html_id_of_datalist
  "#{@name}_datalist"
end
```

    
  

    
      
  
### 
  
    #**input_html_options**  ⇒ Object 
  

  

  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/formtastic/inputs/datalist_input.rb', line 28

def input_html_options
  super.merge(:list => html_id_of_datalist)
end
```

    
  

    
      
  
### 
  
    #**to_html**  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
22
23
24
25
26
```

    
    
      

```
# File 'lib/formtastic/inputs/datalist_input.rb', line 19

def to_html
  @name = input_html_options[:id].gsub(/_id$/, "")
  input_wrapping do
    label_html <<
    builder.text_field(method, input_html_options) << # standard input
    data_list_html # append new datalist element
  end
end
```