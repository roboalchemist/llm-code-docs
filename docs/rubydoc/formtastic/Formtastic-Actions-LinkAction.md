# Class: Formtastic::Actions::LinkAction
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Formtastic::Actions::LinkAction
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Base
  
  
  

  

  
  
    Defined in:
    lib/formtastic/actions/link_action.rb
  
  

## Overview

  
    
  
    **TODO:**
    

document i18n keys

  

  
    **TODO:**
    

document i18n translation with :label (?)

  

  
    **TODO:**
    

:prefix and :suffix options? (can also be done with CSS or subclassing for custom Actions)

  

Outputs a link wrapped in the standard `<li>` wrapper. This the default for `:cancel` actions.
The link's URL defaults to Rails' built-in `:back` macro (the HTTP referrer, or Javascript for the
browser's history), but can be altered with the `:url` option.

  

  
  
    
#### Examples:

    
      
        
##### 

The `:as` can be omitted, these are functionally equivalent

      
      

```
<%= f.action :cancel, :as => :link %>
<%= f.action :cancel %>
```

    
      
        
##### 

Full form context and output

      
      

```

<%= semantic_form_for(@post) do |f| %>
  <%= f.actions do %>
    <%= f.action :submit, :as => :input %>
    <%= f.action :cancel, :as => :link %>
  <% end %>
<% end %>

<form...>
  <fieldset class="actions">
    <ol>
      <li class="action input_action" id="post_submit_action">
        <input type="submit" value="Create Post">
      </li>
      <li class="action link_action" id="post_cancel_action">
        <a href="javascript:history.back()">Cancel</a>
      </li>
    </ol>
  </fieldset>
</form>
```

    
      
        
##### 

Modifying the URL for the link

      
      

```
<%= f.action :cancel, :as => :link, :url => "http://example.com/path" %>
<%= f.action :cancel, :as => :link, :url => "/path" %>
<%= f.action :cancel, :as => :link, :url => posts_path %>
<%= f.action :cancel, :as => :link, :url => url_for(...) %>
<%= f.action :cancel, :as => :link, :url => { :controller => "posts", :action => "index" } %>
```

    
      
        
##### 

Specifying a label with a String

      
      

```
<%= f.action :cancel, :as => :link, :label => "Stop" %>
```

    
      
        
##### 

Pass HTML attributes down to the `<a>`

      
      

```
<%= f.action :cancel, :as => :link, :button_html => { :class => 'pretty', :accesskey => 'x' } %>
```

    
      
        
##### 

Access key can also be set as a top-level option

      
      

```
<%= f.action :cancel, :as => :link, :accesskey => 'x' %>
```

    
      
        
##### 

Pass HTML attributes down to the `<li>` wrapper (classes are appended to the existing classes)

      
      

```
<%= f.action :cancel, :as => :link, :wrapper_html => { :class => 'special', :id => 'whatever' } %>
<%= f.action :cancel, :as => :link, :wrapper_html => { :class => ['extra', 'special'], :id => 'whatever' } %>
```

    
  

  
## Instance Attribute Summary

  
  
### Attributes included from Base

  

#builder, #method, #object, #object_name, #options, #template

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**supported_methods**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

TODO reset_action class?.

  

      
        
- 
  
    
      #**url**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Base

  

#accesskey, #button_html, #button_html_from_options, #default_button_html, #default_wrapper_classes, #default_wrapper_html_options, #default_wrapper_id, #extra_button_html_options, #initialize, #text, #wrapper, #wrapper_class, #wrapper_classes_from_options, #wrapper_html_options, #wrapper_html_options_from_options, #wrapper_id, #wrapper_id_from_options

  
  
  
  
  
  
  
  
  
### Methods included from LocalizedString

  

#model_name

  
    
## Instance Method Details

    
      
  
### 
  
    #**supported_methods**  ⇒ Object 
  

  

  

  
    

  

  

Parameters:

  
    
- 
      
        *args
      
      
        (Hash)
      
      
      
        —
        

a customizable set of options

      
    
  

  

  

See Also:
  

    
      
- Helpers::ActionHelper#action
    
  

  
    
      

```

71
72
73
```

    
    
      

```
# File 'lib/formtastic/actions/link_action.rb', line 71

def supported_methods
  [:cancel]
end
```

    
  

    
      
  
### 
  
    #**to_html**  ⇒ Object 
  

  

  

  
    

TODO reset_action class?

  

  

  
    
      

```

76
77
78
79
80
```

    
    
      

```
# File 'lib/formtastic/actions/link_action.rb', line 76

def to_html
  wrapper do
    template.link_to(text, url, button_html)
  end
end
```

    
  

    
      
  
### 
  
    #**url**  ⇒ Object 
  

  

  

  
    
      

```

82
83
84
85
```

    
    
      

```
# File 'lib/formtastic/actions/link_action.rb', line 82

def url
  return options[:url] if options.key?(:url)
  :back
end
```