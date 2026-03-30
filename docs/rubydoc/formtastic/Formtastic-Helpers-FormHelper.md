# Module: Formtastic::Helpers::FormHelper
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/formtastic/helpers/form_helper.rb
  
  

## Overview

  
    

FormHelper provides a handful of wrappers around Rails' built-in form helpers methods to set
the `:builder` option to `Formtastic::FormBuilder` and apply some class names to the `<form>`
tag.

The following methods are wrapped:

- `semantic_form_for` to `form_for`

- `semantic_fields_for` to `fields_for`

- `semantic_remote_form_for` and `semantic_form_remote_for` to `remote_form_for`

The following two examples are effectively equivalent:

```
<%= form_for(@post, :builder => Formtastic::FormBuilder, :class => 'formtastic post') do |f| %>
  #...
<% end %>

<%= semantic_form_for(@post) do |f| %>
  #...
<% end %>

```

This simple wrapping means that all arguments, options and variations supported by Rails' own
helpers are also supported by Formtastic.

Since `Formtastic::FormBuilder` subclasses Rails' own `FormBuilder`, you have access to all
of Rails' built-in form helper methods such as `text_field`, `check_box`, `radio_button`,
etc **in addition to** all of Formtastic's additional helpers like inputs,
input, buttons, etc:

```
<%= semantic_form_for(@post) do |f| %>

  <!-- Formtastic -->
  <%= f.input :title %>

  <!-- Rails -->
  <li class='something-custom'>
    <%= f.label :title %>
    <%= f.text_field :title %>
    <p class='hints'>...</p>
  </li>
<% end %>

```

Formtastic is a superset of Rails' FormBuilder. It deliberately avoids overriding or modifying
the behavior of Rails' own form helpers so that you can use Formtastic helpers when suited,
and fall back to regular Rails helpers, ERB and HTML when needed. In other words, you're never
fully committed to The Formtastic Way.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        @@builder =
          
  
    

Allows the `:builder` option on `form_for` etc to be changed to your own which subclasses
`Formtastic::FormBuilder`. Change this from `config/initializers/formtastic.rb`.

  

  

        
        

```
Formtastic::FormBuilder
```

      
        @@default_form_class =
          
  
    

Allows the default class we add to all `<form>` tags to be changed from `formtastic` to
`whatever`. Change this from `config/initializers/formtastic.rb`.

  

  

        
        

```
'formtastic'
```

      
        @@default_form_model_class_proc =
          
  
    

Allows to set a custom proc to handle the class inferred from the model's name. By default it
will infer the name from the class name (eg. Post will be "post").

  

  

        
        

```
proc { |model_class_name| model_class_name }
```

      
        @@formtastic_field_error_proc =
          
  
    

Allows to set a custom field_error_proc wrapper. By default this wrapper
is disabled since `formtastic` already adds an error class to the LI tag
containing the input. Change this from `config/initializers/formtastic.rb`.

  

  

        
        

```
proc { |html_tag, instance_tag| html_tag }
```

      
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**semantic_fields_for**(record_name, record_object = nil, options = {}, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Wrapper around Rails' own `fields_for` helper to set the `:builder` option to `Formtastic::FormBuilder`.

  

      
        
- 
  
    
      #**semantic_form_for**(record_or_name_or_array, *args, &proc)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Wrapper around Rails' own `form_for` helper to set the `:builder` option to `Formtastic::FormBuilder` and to set some class names on the `<form>` tag such as `formtastic` and the downcased and underscored model name (eg `post`).

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**semantic_fields_for**(record_name, record_object = nil, options = {}, &block)  ⇒ Object 
  

  

  

  
    

Wrapper around Rails' own `fields_for` helper to set the `:builder` option to
`Formtastic::FormBuilder`.

  

  

  

See Also:
  

    
      
- #semantic_form_for
    
  

  
    
      

```

183
184
185
186
187
188
189
190
191
```

    
    
      

```
# File 'lib/formtastic/helpers/form_helper.rb', line 183

def semantic_fields_for(record_name, record_object = nil, options = {}, &block)
  options, record_object = record_object, nil if record_object.is_a?(Hash) && record_object.extractable_options?
  options[:builder] ||= @@builder
  options[:custom_namespace] = options.delete(:namespace)

  with_custom_field_error_proc do
    self.fields_for(record_name, record_object, options, &block)
  end
end
```

    
  

    
      
  
### 
  
    #**semantic_form_for**(record_or_name_or_array, *args, &proc)  ⇒ Object 
  

  

  

  
    

Wrapper around Rails' own `form_for` helper to set the `:builder` option to
`Formtastic::FormBuilder` and to set some class names on the `<form>` tag such as
`formtastic` and the downcased and underscored model name (eg `post`).

See Rails' `form_for` for full documentation of all supported arguments and options.

Since `Formtastic::FormBuilder` subclasses Rails' own FormBuilder, you have access to all
of Rails' built-in form helper methods such as `text_field`, `check_box`, `radio_button`,
etc **in addition to** all of Formtastic's additional helpers like inputs,
input, buttons, etc.

Most of the examples below have been adapted from the examples found in the Rails `form_for`
documentation.

  

  
  
    
#### Examples:

    
      
        
##### 

Resource-oriented form generation

      
      

```
<%= semantic_form_for @user do |f| %>
  <%= f.input :name %>
  <%= f.input :email %>
  <%= f.input :password %>
<% end %>
```

    
      
        
##### 

Generic form generation

      
      

```
<%= semantic_form_for :user do |f| %>
  <%= f.input :name %>
  <%= f.input :email %>
  <%= f.input :password %>
<% end %>
```

    
      
        
##### 

Resource-oriented with custom URL

      
      

```
<%= semantic_form_for(@post, :url => super_post_path(@post)) do |f| %>
  ...
<% end %>
```

    
      
        
##### 

Resource-oriented with namespaced routes

      
      

```
<%= semantic_form_for([:admin, @post]) do |f| %>
  ...
<% end %>
```

    
      
        
##### 

Resource-oriented with nested routes

      
      

```
<%= semantic_form_for([@user, @post]) do |f| %>
  ...
<% end %>
```

    
      
        
##### 

Rename the resource

      
      

```
<%= semantic_form_for(@post, :as => :article) do |f| %>
  ...
<% end %>
```

    
      
        
##### 

Remote forms (unobtrusive JavaScript)

      
      

```
<%= semantic_form_for(@post, :remote => true) do |f| %>
  ...
<% end %>
```

    
      
        
##### 

Namespaced forms all multiple Formtastic forms to exist on the one page without DOM id clashes and invalid HTML documents.

      
      

```
<%= semantic_form_for(@post, :namespace => 'first') do |f| %>
  ...
<% end %>
```

    
      
        
##### 

Accessing a mixture of Formtastic helpers and Rails FormBuilder helpers.

      
      

```
<%= semantic_form_for(@post) do |f| %>
  <%= f.input :title %>
  <%= f.input :body %>
  <li class="something-custom">
    <label><%= f.check_box :published %></label>
  </li>
<% end %>
```

    
  

Parameters:

  
    
- 
      
        record_or_name_or_array
      
      
        
      
      
      
        —
        

Same behavior as Rails' `form_for`

      
    
  
    
- 
      
        *args
      
      
        (Hash)
      
      
      
        —
        

a customizable set of options

      
    
  

  
    
    
    
    
    
    

  

See Also:
  

    
      
- Rails' FormHelper documentation (`form_for`, etc)
    
      
- Rails' FormBuilder documentation (`text_field`, etc)
    
      
- The overview of the FormBuilder module
    
  

  
    
      

```

154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
```

    
    
      

```
# File 'lib/formtastic/helpers/form_helper.rb', line 154

def semantic_form_for(record_or_name_or_array, *args, &proc)
  options = args.extract_options!
  options[:builder] ||= @@builder
  options[:html] ||= {}
  options[:html][:novalidate] = !@@builder.perform_browser_validations unless options[:html].key?(:novalidate)
  options[:custom_namespace] = options.delete(:namespace)

  singularizer = defined?(ActiveModel::Naming.singular) ? ActiveModel::Naming.method(:singular) : ActionController::RecordIdentifier.method(:singular_class_name)

  class_names = options[:html][:class] ? options[:html][:class].split(" ") : []
  class_names << @@default_form_class
  model_class_name = case record_or_name_or_array
    when String, Symbol then record_or_name_or_array.to_s                                  # :post => "post"
    when Array then options[:as] || singularizer.call(record_or_name_or_array[-1].class)  # [@post, @comment] # => "comment"
    else options[:as] || singularizer.call(record_or_name_or_array.class)                  # @post => "post"
  end
  class_names << @@default_form_model_class_proc.call(model_class_name)

  options[:html][:class] = class_names.compact.join(" ")

  with_custom_field_error_proc do
    self.form_for(record_or_name_or_array, *(args << options), &proc)
  end
end
```