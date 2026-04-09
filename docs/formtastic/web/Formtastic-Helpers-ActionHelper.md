# Module: Formtastic::Helpers::ActionHelper
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    FormBuilder
  
  

  
  
    Defined in:
    lib/formtastic/helpers/action_helper.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**action**(method, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Renders an action for the form (such as a subit/reset button, or a cancel link).

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**action**(method, options = {})  ⇒ Object 
  

  

  

  
    
  
    **TODO:**
    

document i18n keys

  

Renders an action for the form (such as a subit/reset button, or a cancel link).

Each action is wrapped in an `<li class="action">` tag with other classes added based on the
type of action being rendered, and is intended to be rendered inside a #buttons
block which wraps the button in a `fieldset` and `ol`.

The textual value of the label can be changed from the default through the `:label`
argument or through i18n.

If using i18n, you'll need to provide the following translations:

en:
    formtastic:
      actions:
        create: "Create new %model"
        update: "Save %model"
        cancel: "Cancel"
        reset: "Reset form"
        submit: "Submit"

For forms with an object present, the `update` key will be used if calling `persisted?` on
the object returns true (saving changes to a record), otherwise the `create` key will be
used. The `submit` key is used as a fallback when there is no object or we cannot determine
if `create` or `update` is appropriate.

  

  
  
    
#### Examples:

    
      
        
##### 

Basic usage

      
      

```
# form
<%= semantic_form_for @post do |f| %>
  ...
  <%= f.actions do %>
    <%= f.action :submit %>
    <%= f.action :reset %>
    <%= f.action :cancel %>
  <% end %>
<% end %>

# output
<form ...>
  ...
  <fieldset class="buttons">
    <ol>
      <li class="action input_action">
        <input name="commit" type="submit" value="Create Post">
      </li>
      <li class="action input_action">
        <input name="commit" type="reset" value="Reset Post">
      </li>
      <li class="action link_action">
        <a href="/posts">Cancel Post</a>
      </li>
    </ol>
  </fieldset>
</form>
```

    
      
        
##### 

Set the value through the `:label` option

      
      

```
<%= f.action :submit, :label => "Go" %>
```

    
      
        
##### 

Pass HTML attributes down to the tag inside the wrapper

      
      

```
<%= f.action :submit, :button_html => { :class => 'pretty', :accesskey => 'g', :disable_with => "Wait..." } %>
```

    
      
        
##### 

Pass HTML attributes down to the `<li>` wrapper

      
      

```
<%= f.action :submit, :wrapper_html => { :class => 'special', :id => 'whatever' } %>
```

    
  

Parameters:

  
    
- 
      
        *args
      
      
        (Hash)
      
      
      
        —
        

a customizable set of options

      
    
  

  
    
    
    
    

  
    
      

```

78
79
80
81
82
83
84
85
```

    
    
      

```
# File 'lib/formtastic/helpers/action_helper.rb', line 78

def action(method, options = {})
  options = options.dup # Allow options to be shared without being tainted by Formtastic
  options[:as] ||= default_action_type(method, options)

  klass = namespaced_action_class(options[:as])

  klass.new(self, template, @object, @object_name, method, options).to_html
end
```