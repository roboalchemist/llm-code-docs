# Class: SimpleForm::Inputs::CollectionInput
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- SimpleForm::Inputs::CollectionInput
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/simple_form/inputs/collection_input.rb
  
  

  
## Direct Known Subclasses

  

CollectionRadioButtonsInput, CollectionSelectInput, GroupedCollectionSelectInput

  
    
## 
      Constant Summary
      collapse
    

    
      
        BASIC_OBJECT_CLASSES =
          
        
        

```
[String, Integer, Float, NilClass, Symbol, TrueClass, FalseClass]
```

      
    
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#attribute_name, #column, #html_classes, #input_html_classes, #input_html_options, #input_type, #options, #reflection

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**boolean_collection**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Default boolean collection for use with selects/radios when no collection is given.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**input**(wrapper_options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**input_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#additional_classes, disable, enable, #initialize, #input_class

  
  
  
  
  
  
  
  
  
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

  

#html5, #html5?, #initialize, #input_html_required_option

  
  
  
  
  
  
  
  
  
### Methods included from Components::Hints

  

#has_hint?, #hint

  
  
  
  
  
  
  
  
  
### Methods included from Components::Errors

  

#error, #full_error, #has_errors?, #has_value?, #valid?

  
  
  
  
  
  
  
  
  
### Methods included from Helpers::Validators

  

#has_validators?

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
## Constructor Details

  
    

This class inherits a constructor from SimpleForm::Inputs::Base
  

  
    
## Class Method Details

    
      
  
### 
  
    .**boolean_collection**  ⇒ Object 
  

  

  

  
    

Default boolean collection for use with selects/radios when no collection is given. Always fallback to this boolean collection. Texts can be translated using i18n in “simple_form.yes” and “simple_form.no” keys. See the example locale file.

  

  

  
    
      

```

12
13
14
15
```

    
    
      

```
# File 'lib/simple_form/inputs/collection_input.rb', line 12

def self.boolean_collection
  [ [I18n.t(:"simple_form.yes", default: 'Yes'), true],
    [I18n.t(:"simple_form.no", default: 'No'), false] ]
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**input**(wrapper_options = nil)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

17
18
19
20
```

    
    
      

```
# File 'lib/simple_form/inputs/collection_input.rb', line 17

def input(wrapper_options = nil)
  raise NotImplementedError,
    "input should be implemented by classes inheriting from CollectionInput"
end
```

    
  

    
      
  
### 
  
    #**input_options**  ⇒ Object 
  

  

  

  
    
      

```

22
23
24
25
26
27
28
29
30
```

    
    
      

```
# File 'lib/simple_form/inputs/collection_input.rb', line 22

def input_options
  options = super

  options[:include_blank] = true unless skip_include_blank?
  translate_option options, :prompt
  translate_option options, :include_blank

  options
end
```