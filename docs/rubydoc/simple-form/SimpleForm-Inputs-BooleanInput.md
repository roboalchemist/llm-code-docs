# Class: SimpleForm::Inputs::BooleanInput
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- SimpleForm::Inputs::BooleanInput
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/simple_form/inputs/boolean_input.rb
  
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#attribute_name, #column, #html_classes, #input_html_classes, #input_html_options, #input_type, #options, #reflection

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**input**(wrapper_options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**label_input**(wrapper_options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
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
15
16
17
18
19
20
21
```

    
    
      

```
# File 'lib/simple_form/inputs/boolean_input.rb', line 5

def input(wrapper_options = nil)
  merged_input_options = merge_wrapper_options(input_html_options, wrapper_options)

  if nested_boolean_style?
    build_hidden_field_for_checkbox +
      template.label_tag(nil, class: boolean_label_class) {
        build_check_box_without_hidden_field(merged_input_options) +
          inline_label
      }
  else
    if include_hidden?
      build_check_box(unchecked_value, merged_input_options)
    else
      build_check_box_without_hidden_field(merged_input_options)
    end
  end
end
```

    
  

    
      
  
### 
  
    #**label_input**(wrapper_options = nil)  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
```

    
    
      

```
# File 'lib/simple_form/inputs/boolean_input.rb', line 23

def label_input(wrapper_options = nil)
  if options[:label] == false || inline_label?
    input(wrapper_options)
  elsif nested_boolean_style?
    html_options = label_html_options.dup
    html_options[:class] ||= []
    html_options[:class].push(boolean_label_class) if boolean_label_class

    merged_input_options = merge_wrapper_options(input_html_options, wrapper_options)

    build_hidden_field_for_checkbox +
      @builder.label(label_target, html_options) {
        build_check_box_without_hidden_field(merged_input_options) + label_text
      }
  else
    input(wrapper_options) + label(wrapper_options)
  end
end
```