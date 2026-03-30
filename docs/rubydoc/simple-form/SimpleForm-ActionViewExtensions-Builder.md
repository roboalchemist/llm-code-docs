# Module: SimpleForm::ActionViewExtensions::Builder
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    ActionView::Helpers::FormBuilder
  
  

  
  
    Defined in:
    lib/simple_form/action_view_extensions/builder.rb
  
  

## Overview

  
    

A collection of methods required by simple_form but added to rails default form. This means that you can use such methods outside simple_form context.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**simple_fields_for**(*args, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Wrapper for using SimpleForm inside a default rails form.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**simple_fields_for**(*args, &block)  ⇒ Object 
  

  

  

  
    

Wrapper for using SimpleForm inside a default rails form. Example:

```
form_for @user do |f|
  f.simple_fields_for :posts do |posts_form|
    # Here you have all simple_form methods available
    posts_form.input :title
  end
end

```

  

  

  
    
      

```

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
# File 'lib/simple_form/action_view_extensions/builder.rb', line 17

def simple_fields_for(*args, &block)
  options = args.extract_options!
  options[:wrapper] = self.options[:wrapper] if options[:wrapper].nil?
  options[:defaults] ||= self.options[:defaults]
  options[:wrapper_mappings] ||= self.options[:wrapper_mappings]

  if self.class < ActionView::Helpers::FormBuilder
    options[:builder] ||= self.class
  else
    options[:builder] ||= SimpleForm::FormBuilder
  end
  fields_for(*args, options, &block)
end
```