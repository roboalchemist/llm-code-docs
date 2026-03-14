# Module: Formtastic::Helpers::ErrorsHelper
  
  
  

  

  
  
  
  
  
      Includes:
      LocalizedString
  
  
  

  
  
    Included in:
    FormBuilder
  
  

  
  
    Defined in:
    lib/formtastic/helpers/errors_helper.rb
  
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        INLINE_ERROR_TYPES =
          
        
        

```
[:sentence, :list, :first]
```

      
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**semantic_errors**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Generates an unordered list of error messages on the base object and optionally for a given set of named attribute.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from LocalizedString

  

#model_name

  
  
  
  
  
  
  
  
  
  
  
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**semantic_errors**(*args)  ⇒ Object 
  

  

  

  
    

Generates an unordered list of error messages on the base object and optionally for a given
set of named attribute. This is idea for rendering a block of error messages at the top of
the form for hidden/special/virtual attributes (the Paperclip Rails plugin does this), or
errors on the base model.

A hash can be used as the last set of arguments to pass HTML attributes to the `<ul>`
wrapper.

# in config/initializers/formtastic.rb

Setting `Formtastic::FormBuilder.semantic_errors_link_to_inputs = true`
will render attribute errors as links to the corresponding errored inputs.

  

  
  
    
#### Examples:

    
      
        
##### 

A list of errors on the base model

      
      

```
<%= semantic_form_for ... %>
  <%= f.semantic_errors %>
  ...
<% end %>
```

    
      
        
##### 

A list of errors on the base and named attributes

      
      

```
<%= semantic_form_for ... %>
  <%= f.semantic_errors :something_special %>
  ...
<% end %>
```

    
      
        
##### 

A list of errors on the base model, with custom HTML attributes

      
      

```
<%= semantic_form_for ... %>
  <%= f.semantic_errors :class => "awesome" %>
  ...
<% end %>
```

    
      
        
##### 

A list of errors on the base model and named attributes, with custom HTML attributes

      
      

```
<%= semantic_form_for ... %>
  <%= f.semantic_errors :something_special, :something_else, :class => "awesome", :onclick => "Awesome();" %>
  ...
<% end %>
```

    
  

  
    
      

```

46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
```

    
    
      

```
# File 'lib/formtastic/helpers/errors_helper.rb', line 46

def semantic_errors(*args)
  html_options = args.extract_options!
  html_options[:class] ||= "errors"

  if Formtastic::FormBuilder.semantic_errors_link_to_inputs
    attribute_error_hash = semantic_error_hash_from_attributes(args)
    return nil if @object.errors[:base].blank? && attribute_error_hash.blank?

    template.content_tag(:ul, html_options) do
      (
        @object.errors[:base].map { |base_error| template.content_tag(:li, base_error) } <<
        attribute_error_hash.map { |attribute, error_message|
          template.content_tag(:li) do
            template.content_tag(:a, href: "##{object_name}_#{attribute}") do
              error_message
            end
          end
        }
      ).join.html_safe
    end
  else
    full_errors = @object.errors[:base]
    full_errors += semantic_error_list_from_attributes(args)
    return nil if full_errors.blank?

    template.content_tag(:ul, html_options) do
      full_errors.map { |error| template.content_tag(:li, error) }.join.html_safe
    end
  end
end
```