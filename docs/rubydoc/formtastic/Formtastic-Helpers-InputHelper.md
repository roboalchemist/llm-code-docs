# Module: Formtastic::Helpers::InputHelper
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    FormBuilder
  
  

  
  
    Defined in:
    lib/formtastic/helpers/input_helper.rb
  
  

## Overview

  
    

#input is used to render all content (labels, form widgets, error messages, hints, etc) for
a single form input (or field), usually representing a single method or attribute on the
form's object or model.

The content is wrapped in an `<li>` tag, so it's usually called inside an inputs block
(which renders an `<ol>` inside a `<fieldset>`), which should be inside a `semantic_form_for`
block:

```
<%= semantic_form_for @post do |f| %>
  <%= f.inputs do %>
    <%= f.input :title %>
    <%= f.input :body %>
  <% end %>
<% end %>

```

The HTML output will be something like:

```
<form class="formtastic" method="post" action="...">
  <fieldset>
    <ol>
      <li class="string required" id="post_title_input">
        ...
      </li>
      <li class="text required" id="post_body_input">
        ...
      </li>
    </ol>
  </fieldset>
</form>

```

  

  

  

See Also:
  

    
      
- #input
    
      
- Formtastic::Helpers::InputsHelper#inputs
    
      
- FormHelper#semantic_form_for
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**input**(method, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns a chunk of HTML markup for a given `method` on the form object, wrapped in an `<li>` wrapper tag with appropriate `class` and `id` attribute hooks for CSS and JS.

  

      
    

  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**input**(method, options = {})  ⇒ Object 
  

  

  

  
    
  
    **TODO:**
    

document the "guessing" of input style

  

  
    **TODO:**
    

Can we deprecate & kill `:label`, `:hint` & `:prompt`? All strings could be shifted to i18n!

  

  
    **TODO:**
    

Many many more examples. Some of the detail probably needs to be pushed out to the relevant methods too.

  

  
    **TODO:**
    

More i18n examples.

  

Returns a chunk of HTML markup for a given `method` on the form object, wrapped in
an `<li>` wrapper tag with appropriate `class` and `id` attribute hooks for CSS and JS.
In many cases, the contents of the wrapper will be as simple as a `<label>` and an `<input>`:

```
<%= f.input :title, :as => :string, :required => true %>

<li class="string required" id="post_title_input">
  <label for="post_title">Title<abbr title="Required">*</abbr></label>
  <input type="text" name="post[title]" value="" id="post_title" required="required">
</li>

```

In other cases (like a series of checkboxes for a `has_many` relationship), the wrapper may
include more complex markup, like a nested `<fieldset>` with a `<legend>` and an `<ol>` of
checkbox/label pairs for each choice:

```
<%= f.input :categories, :as => :check_boxes, :collection => Category.active.ordered %>

<li class="check_boxes" id="post_categories_input">
  <fieldset>
    <legend>Categories</legend>
    <ol>
      <li>
        <label><input type="checkbox" name="post[categories][1]" value="1"> Ruby</label>
      </li>
      <li>
        <label><input type="checkbox" name="post[categories][2]" value="2"> Rails</label>
      </li>
      <li>
        <label><input type="checkbox" name="post[categories][2]" value="2"> Awesome</label>
      </li>
    </ol>
  </fieldset>
</li>

```

Sensible defaults for all options are guessed by looking at the method name, database column
information, association information, validation information, etc. For example, a `:string`
database column will map to a `:string` input, but if the method name contains 'email', will
map to an `:email` input instead. `belongs_to` associations will have a `:select` input, etc.

Formtastic supports many different styles of inputs, and you can/should override the default
with the `:as` option. Internally, the symbol is used to map to a protected method
responsible for the details. For example, `:as => :string` will map to `string_input`,
defined in a module of the same name. Detailed documentation for each input style and it's
supported options is available on the `*_input` method in each module (links provided below).

Available input styles:

- `:boolean`          (see Inputs::BooleanInput)

- `:check_boxes`      (see Inputs::CheckBoxesInput)

- `:color`            (see Inputs::ColorInput)

- `:country`          (see Inputs::CountryInput)

- `:datetime_select`  (see Inputs::DatetimeSelectInput)

- `:date_select`      (see Inputs::DateSelectInput)

- `:email`            (see Inputs::EmailInput)

- `:file`             (see Inputs::FileInput)

- `:hidden`           (see Inputs::HiddenInput)

- `:number`           (see Inputs::NumberInput)

- `:password`         (see Inputs::PasswordInput)

- `:phone`            (see Inputs::PhoneInput)

- `:radio`            (see Inputs::RadioInput)

- `:search`           (see Inputs::SearchInput)

- `:select`           (see Inputs::SelectInput)

- `:string`           (see Inputs::StringInput)

- `:text`             (see Inputs::TextInput)

- `:time_zone`        (see Inputs::TimeZoneInput)

- `:time_select`      (see Inputs::TimeSelectInput)

- `:url`              (see Inputs::UrlInput)

Calling `:as => :string` (for example) will call `#to_html` on a new instance of
`Formtastic::Inputs::StringInput`. Before this, Formtastic will try to instantiate a top-level
namespace StringInput, meaning you can subclass and modify `Formtastic::Inputs::StringInput`
in `app/inputs/`. This also means you can create your own new input types in `app/inputs/`.

  

  
  
    
#### Examples:

    
      
        
##### 

Accept all default options

      
      

```
<%= f.input :title %>
```

    
      
        
##### 

Change the input type

      
      

```
<%= f.input :title, :as => :string %>
```

    
      
        
##### 

Changing the label with a String

      
      

```
<%= f.input :title, :label => "Post title" %>
```

    
      
        
##### 

Disabling the label with false, even if an i18n translation exists

      
      

```
<%= f.input :title, :label => false  %>
```

    
      
        
##### 

Changing the hint with a String

      
      

```
<%= f.input :title, :hint => "Every post needs a title!" %>
```

    
      
        
##### 

Disabling the hint with false, even if an i18n translation exists

      
      

```
<%= f.input :title, :hint => false  %>
```

    
      
        
##### 

Marking a field as required or not (even if validations do not enforce it)

      
      

```
<%= f.input :title, :required => true  %>
<%= f.input :title, :required => false  %>
```

    
      
        
##### 

Changing or adding to HTML attributes in the main `<input>` or `<select>` tag

      
      

```
<%= f.input :title, :input_html => { :onchange => "somethingAwesome();", :class => 'awesome' } %>
```

    
      
        
##### 

Changing or adding to HTML attributes in the main `<label>` tag

      
      

```
<%= f.input :title, :label_html => { :data => { :tooltip => 'Great Tooltip' } } %>
```

    
      
        
##### 

Changing or adding to HTML attributes in the wrapper `<li>` tag

      
      

```
<%= f.input :title, :wrapper_html => { :class => "important-input" } %>
```

    
      
        
##### 

Changing the association choices with `:collection`

      
      

```
<%= f.input :author,     :collection => User.active %>
<%= f.input :categories, :collection => Category.where(...).order(...) %>
<%= f.input :status,     :collection => ["Draft", "Published"] %>
<%= f.input :status,     :collection => [:draft, :published] %>
<%= f.input :status,     :collection => {"Draft" => 0, "Published" => 1} %>
<%= f.input :status,     :collection => OrderedHash.new("Draft" => 0, "Published" => 1) %>
<%= f.input :status,     :collection => [["Draft", 0], ["Published", 1]] %>
<%= f.input :status,     :collection => grouped_options_for_select(...) %>
<%= f.input :status,     :collection => options_for_select(...) %>
```

    
      
        
##### 

Specifying if a `:select` should allow multiple selections:

      
      

```
<%= f.input :cateogies, :as => :select, :multiple => true %>
<%= f.input :cateogies, :as => :select, :multiple => false %>
```

    
      
        
##### 

Specifying if a `:select` should have a 'blank' first option to prompt selection:

      
      

```
<%= f.input :author, :as => :select, :include_blank => true %>
<%= f.input :author, :as => :select, :include_blank => false %>
```

    
      
        
##### 

Specifying the text for a `:select` input's 'blank' first option to prompt selection:

      
      

```
<%= f.input :author, :as => :select, :prompt => "Select an Author" %>
```

    
      
        
##### 

Modifying an input to suit your needs in `app/inputs`:

      
      

```
class StringInput < Formtastic::Inputs::StringInput
  def to_html
    puts "this is my custom version of StringInput"
    super
  end
end
```

    
      
        
##### 

Creating your own input to suit your needs in `app/inputs`:

      
      

```
class DatePickerInput
  include Formtastic::Inputs::Base
  def to_html
    # ...
  end
end
```

    
      
        
##### 

Providing HTML5 placeholder text through i18n:

      
      

```
en:
 formtastic:
   placeholders:
     user:
       email: "[email protected]"
       first_name: "Joe"
       last_name: "Smith"
```

    
  

Parameters:

  
    
- 
      
        method
      
      
        (Symbol)
      
      
      
        —
        

The database column or method name on the form object that this input represents

      
    
  
    
- 
      
        options
      
      
        (Hash)
      
      
        *(defaults to: {})*
      
      
        —
        

a customizable set of options

      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :as
          (Symbol)
          
            
          
          
            — 

Override the style of input should be rendered

          
        
      
        
- 
          :label
          (String, Symbol, false)
          
            
          
          
            — 

Override the label text

          
        
      
        
- 
          :hint
          (String, Symbol, false)
          
            
          
          
            — 

Override hint text

          
        
      
        
- 
          :required
          (Boolean)
          
            
          
          
            — 

Override to mark the input as required (or not) — adds a required/optional class to the wrapper, and a HTML5 required attribute to the `<input>`

          
        
      
        
- 
          :input_html
          (Hash)
          
            
          
          
            — 

Override or add to the HTML attributes to be passed down to the `<input>` tag
(If you use attr_readonly method in your model, formtastic will automatically set those attributes's input readonly)

          
        
      
        
- 
          :wrapper_html
          (Hash)
          
            
          
          
            — 

Override or add to the HTML attributes to be passed down to the wrapping `<li>` tag

          
        
      
        
- 
          :collection
          (Array<ActiveModel, String, Symbol>, Hash{String => String, Boolean}, OrderedHash{String => String, Boolean})
          
            
          
          
            — 

Override collection of objects in the association (`:select`, `:radio` & `:check_boxes` inputs only)

          
        
      
        
- 
          :multiple
          (Boolean)
          
            
          
          
            — 

Specify if the `:select` input should allow multiple selections or not (defaults to `belongs_to` associations, and `true` for `has_many` and `has_and_belongs_to_many` associations)

          
        
      
        
- 
          :include_blank
          (Boolean)
          
            
          
          
            — 

Specify if a `:select` input should include a blank option or not (defaults to `include_blank_for_select_by_default` configuration)

          
        
      
        
- 
          :prompt
          (String)
          
            
          
          
            — 

Specify the text in the first ('blank') `:select` input `<option>` to prompt a user to make a selection (implicitly sets `:include_blank` to `true`)

          
        
      
    

  

  

See Also:
  

    
      
- #namespaced_input_class
    
  

  
    
      

```

235
236
237
238
239
240
241
242
243
```

    
    
      

```
# File 'lib/formtastic/helpers/input_helper.rb', line 235

def input(method, options = {})
  method = method.to_sym
  options = options.dup # Allow options to be shared without being tainted by Formtastic
  options[:as] ||= default_input_type(method, options)

  klass = namespaced_input_class(options[:as])

  klass.new(self, template, @object, @object_name, method, options).to_html
end
```