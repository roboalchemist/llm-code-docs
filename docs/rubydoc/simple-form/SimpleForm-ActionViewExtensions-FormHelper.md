# Module: SimpleForm::ActionViewExtensions::FormHelper
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/simple_form/action_view_extensions/form_helper.rb
  
  

## Overview

  
    

This module creates SimpleForm wrappers around default form_for and fields_for.

Example:

```
simple_form_for @user do |f|
  f.input :name, hint: 'My hint'
end

```

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**simple_fields_for**(record_name, record_object = nil, options = {}, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**simple_form_for**(record, options = {}, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**simple_fields_for**(record_name, record_object = nil, options = {}, &block)  ⇒ Object 
  

  

  

  
    
      

```

31
32
33
34
35
36
37
38
```

    
    
      

```
# File 'lib/simple_form/action_view_extensions/form_helper.rb', line 31

def simple_fields_for(record_name, record_object = nil, options = {}, &block)
  options, record_object = record_object, nil if record_object.is_a?(Hash) && record_object.extractable_options?
  options[:builder] ||= SimpleForm::FormBuilder

  with_simple_form_field_error_proc do
    fields_for(record_name, record_object, options, &block)
  end
end
```

    
  

    
      
  
### 
  
    #**simple_form_for**(record, options = {}, &block)  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
```

    
    
      

```
# File 'lib/simple_form/action_view_extensions/form_helper.rb', line 14

def simple_form_for(record, options = {}, &block)
  options[:builder] ||= SimpleForm::FormBuilder
  options[:html] ||= {}
  unless options[:html].key?(:novalidate)
    options[:html][:novalidate] = !SimpleForm.browser_validations
  end
  if options[:html].key?(:class)
    options[:html][:class] = [SimpleForm.form_class, options[:html][:class]].compact
  else
    options[:html][:class] = [SimpleForm.form_class, SimpleForm.default_form_class, simple_form_css_class(record, options)].compact
  end

  with_simple_form_field_error_proc do
    form_for(record, options, &block)
  end
end
```