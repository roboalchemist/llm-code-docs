# Class: SimpleForm::Inputs::CollectionSelectInput
  
  
  

  
  
    Inherits:
    
      CollectionInput
      
        

          
- Object
          
            
- Base
          
            
- CollectionInput
          
            
- SimpleForm::Inputs::CollectionSelectInput
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/simple_form/inputs/collection_select_input.rb
  
  

  
## Direct Known Subclasses

  

PriorityInput, WeekdayInput

  
## Constant Summary

  
  
### Constants inherited
     from CollectionInput

  

SimpleForm::Inputs::CollectionInput::BASIC_OBJECT_CLASSES

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#attribute_name, #column, #html_classes, #input_html_classes, #input_html_options, #input_type, #options, #reflection

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**input**(wrapper_options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from CollectionInput

  

boolean_collection, #input_options

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#additional_classes, disable, enable, #initialize, #input_class, #input_options

  
  
  
  
  
  
  
  
  
### Methods included from Components::Readonly

  

#readonly

  
  
  
  
  
  
  
  
  
### Methods included from Components::Placeholders

  

#placeholder, #placeholder_text

  
  
  
  
  
  
  
  
  
### Methods included from Components::Pattern

  

#pattern

  
  
  
  
  
  
  
  
  
### Methods included from Components::MinMax

  

#min_max

  
  
  
  
  
  
  
  
  
### Methods included from Components::Minlength

  

#minlength

  
  
  
  
  
  
  
  
  
### Methods included from Components::Maxlength

  

#maxlength

  
  
  
  
  
  
  
  
  
### Methods included from Components::LabelInput

  

#label_input

  
  
  
  
  
  
  
  
  
  
### Methods included from Components::HTML5

  

#has_required?, #html5, #html5?, #initialize, #input_html_required_option

  
  
  
  
  
  
  
  
  
### Methods included from Components::Hints

  

#has_hint?, #hint

  
  
  
  
  
  
  
  
  
### Methods included from Components::Errors

  

#error, #full_error, #has_errors?, #has_value?, #valid?

  
  
  
  
  
  
  
  
  
### Methods included from Helpers::Validators

  

#has_validators?

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
## Constructor Details

  
    

This class inherits a constructor from SimpleForm::Inputs::Base
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**input**(wrapper_options = nil)  ⇒ Object 
  

  

  

  
    
      

```

5
6
7
8
9
10
11
12
13
14
```

    
    
      

```
# File 'lib/simple_form/inputs/collection_select_input.rb', line 5

def input(wrapper_options = nil)
  label_method, value_method = detect_collection_methods

  merged_input_options = merge_wrapper_options(input_html_options, wrapper_options)

  @builder.collection_select(
    attribute_name, collection, value_method, label_method,
    input_options, merged_input_options
  )
end
```