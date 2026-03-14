# Class: SimpleForm::Inputs::NumericInput
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- SimpleForm::Inputs::NumericInput
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/simple_form/inputs/numeric_input.rb
  
  

  
## Direct Known Subclasses

  

RangeInput

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#attribute_name, #column, #html_classes, #input_html_classes, #input_html_options, #input_type, #options, #reflection

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**input**(wrapper_options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
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

7
8
9
10
11
12
13
14
15
16
17
```

    
    
      

```
# File 'lib/simple_form/inputs/numeric_input.rb', line 7

def input(wrapper_options = nil)
  input_html_classes.unshift("numeric")
  if html5?
    input_html_options[:type] ||= "number"
    input_html_options[:step] ||= integer? ? 1 : "any"
  end

  merged_input_options = merge_wrapper_options(input_html_options, wrapper_options)

  @builder.text_field(attribute_name, merged_input_options)
end
```