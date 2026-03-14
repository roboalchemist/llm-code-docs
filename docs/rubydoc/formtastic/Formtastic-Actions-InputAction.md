# Class: Formtastic::Actions::InputAction
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Formtastic::Actions::InputAction
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Base, Buttonish
  
  
  

  

  
  
    Defined in:
    lib/formtastic/actions/input_action.rb
  
  

## Overview

  
    
  
    **TODO:**
    

document i18n keys

  

  
    **TODO:**
    

document i18n translation with :label (?)

  

Outputs an `<input type="submit">` or `<input type="reset">` wrapped in the standard `<li>`
wrapper. This the default for `:submit` and `:reset` actions, but `:as => :button` is also
available as an alternative.

  

  
  
    
#### Examples:

    
      
        
##### 

The `:as` can be omitted, these are functionally equivalent

      
      

```
<%= f.action :submit, :as => :input %>
<%= f.action :submit %>
```

    
      
        
##### 

Full form context and output

      
      

```

<%= semantic_form_for(@post) do |f| %>
  <%= f.actions do %>
    <%= f.action :reset, :as => :input %>
    <%= f.action :submit, :as => :input %>
  <% end %>
<% end %>

<form...>
  <fieldset class="actions">
    <ol>
      <li class="action input_action" id="post_reset_action">
        <input type="reset" value="Reset">
      </li>
      <li class="action input_action" id="post_submit_action">
        <input type="submit" value="Create Post">
      </li>
    </ol>
  </fieldset>
</form>
```

    
      
        
##### 

Specifying a label with a String

      
      

```
<%= f.action :submit, :as => :input, :label => "Go" %>
```

    
      
        
##### 

Pass HTML attributes down to the `<input>`

      
      

```
<%= f.action :submit, :as => :input, :button_html => { :class => 'pretty', :accesskey => 'g', :disable_with => "Wait..." } %>
```

    
      
        
##### 

Access key can also be set as a top-level option

      
      

```
<%= f.action :submit, :as => :input, :accesskey => 'g' %>
```

    
      
        
##### 

Pass HTML attributes down to the `<li>` wrapper (classes are appended to the existing classes)

      
      

```
<%= f.action :submit, :as => :input, :wrapper_html => { :class => 'special', :id => 'whatever' } %>
<%= f.action :submit, :as => :input, :wrapper_html => { :class => ['extra', 'special'], :id => 'whatever' } %>
```

    
  

  
## Instance Attribute Summary

  
  
### Attributes included from Base

  

#builder, #method, #object, #object_name, #options, #template

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**to_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Buttonish

  

#extra_button_html_options, #supported_methods

  
  
  
  
  
  
  
  
  
### Methods included from Base

  

#accesskey, #button_html, #button_html_from_options, #default_button_html, #default_wrapper_classes, #default_wrapper_html_options, #default_wrapper_id, #extra_button_html_options, #initialize, #supported_methods, #text, #wrapper, #wrapper_class, #wrapper_classes_from_options, #wrapper_html_options, #wrapper_html_options_from_options, #wrapper_id, #wrapper_id_from_options

  
  
  
  
  
  
  
  
  
### Methods included from LocalizedString

  

#model_name

  
    
## Instance Method Details

    
      
  
### 
  
    #**to_html**  ⇒ Object 
  

  

  

  
    

  

  

Parameters:

  
    
- 
      
        *args
      
      
        (Hash)
      
      
      
        —
        

a customizable set of options

      
    
  

  

  

See Also:
  

    
      
- Helpers::ActionHelper#action
    
  

  
    
      

```

64
65
66
67
68
```

    
    
      

```
# File 'lib/formtastic/actions/input_action.rb', line 64

def to_html
  wrapper do
    builder.submit(text, button_html)
  end
end
```