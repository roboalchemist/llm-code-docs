# Class: Formtastic::Actions::ButtonAction
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Formtastic::Actions::ButtonAction
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Base, Buttonish
  
  
  

  

  
  
    Defined in:
    lib/formtastic/actions/button_action.rb
  
  

## Overview

  
    
  
    **TODO:**
    

document i18n keys

  

  
    **TODO:**
    

document i18n translation with :label (?)

  

Outputs a `<button type="submit">` or `<button type="reset">` wrapped in the standard `<li>`
wrapper. This is an alternative choice for `:submit` and `:reset` actions, which render with
`<input type="submit">` and `<input type="reset">` by default.

  

  
  
    
#### Examples:

    
      
        
##### 

Full form context and output

      
      

```

<%= semantic_form_for(@post) do |f| %>
  <%= f.actions do %>
    <%= f.action :reset, :as => :button %>
    <%= f.action :submit, :as => :button %>
  <% end %>
<% end %>

<form...>
  <fieldset class="actions">
    <ol>
      <li class="action button_action" id="post_reset_action">
        <button type="reset" value="Reset">
      </li>
      <li class="action button_action" id="post_submit_action">
        <button type="submit" value="Create Post">
      </li>
    </ol>
  </fieldset>
</form>
```

    
      
        
##### 

Specifying a label with a String

      
      

```
<%= f.action :submit, :as => :button, :label => "Go" %>
```

    
      
        
##### 

Pass HTML attributes down to the `<button>`

      
      

```
<%= f.action :submit, :as => :button, :button_html => { :class => 'pretty', :accesskey => 'g', :disable_with => "Wait..." } %>
```

    
      
        
##### 

Access key can also be set as a top-level option

      
      

```
<%= f.action :submit, :as => :button, :accesskey => 'g' %>
```

    
      
        
##### 

Pass HTML attributes down to the `<li>` wrapper (classes are appended to the existing classes)

      
      

```
<%= f.action :submit, :as => :button, :wrapper_html => { :class => 'special', :id => 'whatever' } %>
<%= f.action :submit, :as => :button, :wrapper_html => { :class => ['extra', 'special'], :id => 'whatever' } %>
```

    
  

  
## Instance Attribute Summary

  
  
### Attributes included from Base

  

#builder, #method, #object, #object_name, #options, #template

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**to_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

TODO reset_action class?.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Buttonish

  

#extra_button_html_options, #supported_methods

  
  
  
  
  
  
  
  
  
### Methods included from Base

  

#accesskey, #button_html, #button_html_from_options, #default_button_html, #default_wrapper_classes, #default_wrapper_html_options, #default_wrapper_id, #extra_button_html_options, #initialize, #supported_methods, #text, #wrapper, #wrapper_class, #wrapper_classes_from_options, #wrapper_html_options, #wrapper_html_options_from_options, #wrapper_id, #wrapper_id_from_options

  
  
  
  
  
  
  
  
  
### Methods included from LocalizedString

  

#model_name

  
    
## Instance Method Details

    
      
  
### 
  
    #**to_html**  ⇒ Object 
  

  

  

  
    

TODO reset_action class?

  

  

  
    
      

```

61
62
63
64
65
```

    
    
      

```
# File 'lib/formtastic/actions/button_action.rb', line 61

def to_html
  wrapper do
    template.button_tag(text, button_html)
  end
end
```