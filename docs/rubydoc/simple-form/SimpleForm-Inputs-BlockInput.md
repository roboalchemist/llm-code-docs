# Class: SimpleForm::Inputs::BlockInput
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- SimpleForm::Inputs::BlockInput
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/simple_form/inputs/block_input.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#attribute_name, #column, #html_classes, #input_html_classes, #input_html_options, #input_type, #options, #reflection

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(*args, &block)  ⇒ BlockInput 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of BlockInput.

  

      
        
- 
  
    
      #**input**(wrapper_options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#additional_classes, disable, enable, #input_class, #input_options

  
  
  
  
  
  
  
  
  
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

  

#has_required?, #html5, #html5?, #input_html_required_option

  
  
  
  
  
  
  
  
  
### Methods included from Components::Hints

  

#has_hint?, #hint

  
  
  
  
  
  
  
  
  
### Methods included from Components::Errors

  

#error, #full_error, #has_errors?, #has_value?, #valid?

  
  
  
  
  
  
  
  
  
### Methods included from Helpers::Validators

  

#has_validators?

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(*args, &block)  ⇒ BlockInput 
  

  

  

  
    

Returns a new instance of BlockInput.

  

  

  
    
      

```

5
6
7
8
```

    
    
      

```
# File 'lib/simple_form/inputs/block_input.rb', line 5

def initialize(*args, &block)
  super
  @block = block
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**input**(wrapper_options = nil)  ⇒ Object 
  

  

  

  
    
      

```

10
11
12
```

    
    
      

```
# File 'lib/simple_form/inputs/block_input.rb', line 10

def input(wrapper_options = nil)
  template.capture(&@block)
end
```