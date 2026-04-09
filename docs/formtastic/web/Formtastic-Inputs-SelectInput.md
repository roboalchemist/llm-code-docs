# Class: Formtastic::Inputs::SelectInput
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Formtastic::Inputs::SelectInput
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Base, Base::Collections
  
  
  

  

  
  
    Defined in:
    lib/formtastic/inputs/select_input.rb
  
  

## Overview

  
    
  
    **TODO:**
    

Do/can we support the per-item HTML options like RadioInput?

  

A select input is used to render a `<select>` tag with a series of options to choose from.
It works for both single selections (like a `belongs_to` relationship, or "yes/no" boolean),
as well as multiple selections (like a `has_and_belongs_to_many`/`has_many` relationship,
for assigning many genres to a song, for example).

This is the default input choice when:

- the database column type is an `:integer` and there is an association (`belongs_to`)

- the database column type is an `:integer` and there is an enum defined (`enum`)

- the database column type is a `:string` and the `:collection` option is used

- there an object with an association, but no database column on the object (`has_many`, etc)

- there is no object and the `:collection` option is used

The flexibility of the `:collection` option (see examples) makes the :select input viable as
an alternative for many other input types. For example, instead of...

- a `:string` input (where you want to force the user to choose from a few specific strings rather than entering anything)

- a `:boolean` checkbox input (where the user could choose yes or no, rather than checking a box)

- a `:date_select`, `:time_select` or `:datetime_select` input (where the user could choose from pre-selected dates)

- a `:number` input (where the user could choose from a set of pre-defined numbers)

- a `:time_zone` input (where you want to provide your own set of choices instead of relying on Rails)

- a `:country` input (no need for a plugin really)

Within the standard `<li>` wrapper, the output is a `<label>` tag followed by a `<select>`
tag containing `<option>` tags.

For inputs that map to associations on the object model, Formtastic will automatically load
in a collection of objects on the association as options to choose from. This might be an
`Author.all` on a `Post` form with an input for a `belongs_to :user` association, or a
`Tag.all` for a `Post` form with an input for a `has_and_belongs_to_many :tags` association.
You can override or customise this collection and the `<option>` tags it will render through
the `:collection` option (see examples).

The way on which Formtastic renders the `value` attribute and content of each `<option>` tag
is customisable through the `:member_label` and `:member_value` options. When not provided,
we fall back to a list of methods to try on each object such as `:to_label`, `:name` and
`:to_s`, which are defined in the configurations `collection_label_methods` and
`collection_value_methods` (see examples below).

For select inputs that map to ActiveRecord `enum` attributes, Formtastic will automatically
load in your enum options to be used as the select's options. This can be overridden with
the `:collection` option, or augmented with I18n translations. See examples below.
An error is raised if you try to render a multi-select with an enum, as ActiveRecord can
only store one choice in the database.

  

  
  
    
#### Examples:

    
      
        
##### 

Basic `belongs_to` example with full form context

      
      

```

<%= semantic_form_for @post do |f| %>
  <%= f.inputs do %>
    <%= f.input :author, :as => :select %>
  <% end %>
<% end %>

<form...>
  <fieldset>
    <ol>
      <li class='select'>
        <label for="post_author_id">Author</label>
        <select id="post_author_id" name="post[post_author_id]">
          <option value=""></option>
          <option value="1">Justin</option>
          <option value="3">Kate</option>
          <option value="2">Amelia</option>
        </select>
      </li>
    </ol>
  </fieldset>
</form>
```

    
      
        
##### 

Basic `has_many` or `has_and_belongs_to_many` example with full form context

      
      

```

<%= semantic_form_for @post do |f| %>
  <%= f.inputs do %>
    <%= f.input :tags, :as => :select %>
  <% end %>
<% end %>

<form...>
  <fieldset>
    <ol>
      <li class='select'>
        <label for="post_tag_ids">Author</label>
        <select id="post_tag_ids" name="post[tag_ids]" multiple="true">
          <option value="1">Ruby</option>
          <option value="6">Rails</option>
          <option value="3">Forms</option>
          <option value="4">Awesome</option>
        </select>
      </li>
    </ol>
  </fieldset>
</form>
```

    
      
        
##### 

Override Formtastic's assumption on when you need a multi select

      
      

```
<%= f.input :authors, :as => :select, :input_html => { :multiple => true } %>
<%= f.input :authors, :as => :select, :input_html => { :multiple => false } %>
```

    
      
        
##### 

The `:collection` option can be used to customize the choices

      
      

```
<%= f.input :author, :as => :select, :collection => @authors %>
<%= f.input :author, :as => :select, :collection => Author.all %>
<%= f.input :author, :as => :select, :collection => Author.some_named_scope %>
<%= f.input :author, :as => :select, :collection => Author.pluck(:full_name, :id) %>
<%= f.input :author, :as => :select, :collection => Author.pluck(Arel.sql("CONCAT(`first_name`, ' ', `last_name`)"), :id)) %>
<%= f.input :author, :as => :select, :collection => [Author.find_by_login("justin"), Category.find_by_name("kate")] %>
<%= f.input :author, :as => :select, :collection => ["Justin", "Kate"] %>
<%= f.input :author, :as => :select, :collection => [["Justin", "justin"], ["Kate", "kate"]] %>
<%= f.input :author, :as => :select, :collection => [["Justin", "1"], ["Kate", "3"]] %>
<%= f.input :author, :as => :select, :collection => [["Justin", 1], ["Kate", 3]] %>
<%= f.input :author, :as => :select, :collection => 1..5 %>
<%= f.input :author, :as => :select, :collection => "<option>your own options HTML string</option>" %>
<%= f.input :author, :as => :select, :collection => options_for_select(...) %>
<%= f.input :author, :as => :select, :collection => options_from_collection_for_select(...) %>
<%= f.input :author, :as => :select, :collection => grouped_options_for_select(...) %>
<%= f.input :author, :as => :select, :collection => time_zone_options_for_select(...) %>
```

    
      
        
##### 

Set HTML attributes on the `<select>` tag with `:input_html`

      
      

```
<%= f.input :authors, :as => :select, :input_html => { :size => 20, :multiple => true, :class => "special" } %>
```

    
      
        
##### 

Set HTML attributes on the `<li>` wrapper with `:wrapper_html`

      
      

```
<%= f.input :authors, :as => :select, :wrapper_html => { :class => "special" } %>
```

    
      
        
##### 

Exclude, include, or customize the blank option at the top of the select. Always shown, even if the field already has a value. Suitable for optional inputs.

      
      

```
<%= f.input :author, :as => :select, :include_blank => false %>
<%= f.input :author, :as => :select, :include_blank => true %>   =>   <option value=""></option>
<%= f.input :author, :as => :select, :include_blank => "No author" %>
```

    
      
        
##### 

Exclude, include, or customize the prompt at the top of the select. Only shown if the field does not have a value. Suitable for required inputs.

      
      

```
<%= f.input :author, :as => :select, :prompt => false %>
<%= f.input :author, :as => :select, :prompt => true %>   =>   <option value="">Please select</option>
<%= f.input :author, :as => :select, :prompt => "Please select an author" %>
```

    
      
        
##### 

Using ActiveRecord enum attribute with i18n translation:

      
      

```
# post.rb
class Post < ActiveRecord::Base
  enum :status => [ :active, :archived ]
end
# en.yml
en:
  activerecord:
    attributes:
      post:
        statuses:
          active: I am active!
          archived: I am archived!
# form
<%= f.input :status, :as => :select %>
```

    
  

  

See Also:
  

    
      
- InputsHelper#input for full documentation of all possible options.
    
      
- CheckBoxesInput as an alternative for `has_many` and `has_and_belongs_to_many` associations
    
      
- RadioInput as an alternative for `belongs_to` associations
    
  

  
## Instance Attribute Summary

  
  
### Attributes included from Base

  

#builder, #method, #object, #object_name, #options, #template

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**extra_input_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**include_blank**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(*args)  ⇒ SelectInput 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of SelectInput.

  

      
        
- 
  
    
      #**input_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**input_html_options_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**input_html_options_name_multiple**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**input_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**label_html_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**multiple?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**multiple_by_association?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**multiple_by_options?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**prompt?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**select_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**single?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Base::Collections

  

#collection, #collection_for_boolean, #collection_from_association, #collection_from_enum, #collection_from_enum?, #collection_from_options, #label_and_value_method, #label_and_value_method_from_collection, #label_method, #label_method_from_options, #raw_collection, #send_or_call, #send_or_call_or_object, #value_method, #value_method_from_options

  
  
  
  
  
  
  
  
  
### Methods included from Base

  

#removed_option!, #warn_and_correct_option!, #warn_deprecated_option!

  
  
  
  
  
  
  
  
  
  
### Methods included from Base::Aria

  

#describedby, #error_aria_attributes

  
  
  
  
  
  
  
  
  
### Methods included from Base::Wrapping

  

#input_wrapping, #wrapper_classes, #wrapper_classes_raw, #wrapper_dom_id, #wrapper_html_options, #wrapper_html_options_raw

  
  
  
  
  
  
  
  
  
### Methods included from Base::Labelling

  

#label_from_options, #label_html, #label_text, #localized_label, #render_label?, #requirement_text, #requirement_text_or_proc

  
  
  
  
  
  
  
  
  
### Methods included from LocalizedString

  

#model_name

  
  
  
  
  
  
  
  
  
### Methods included from Base::Associations

  

#association, #association_primary_key, #belongs_to?, #has_many?, #reflection

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from Base::Fileish

  

#file?

  
  
  
  
  
  
  
  
  
### Methods included from Base::Validations

  

#autofocus?, #column_limit, #limit, #not_required_through_negated_validation!, #not_required_through_negated_validation?, #optional?, #readonly?, #readonly_attribute?, #readonly_from_options?, #required?, #required_attribute?, #responds_to_global_required?, #validation_integer_only?, #validation_limit, #validation_max, #validation_min, #validation_step, #validations, #validations?, #validator_relevant?

  
  
  
  
  
  
  
  
  
### Methods included from Base::Naming

  

#as, #attributized_method_name, #humanized_method_name, #input_name, #sanitized_method_name, #sanitized_object_name

  
  
  
  
  
  
  
  
  
### Methods included from Base::Hints

  

#hint?, #hint_html, #hint_text, #hint_text_from_options

  
  
  
  
  
  
  
  
  
### Methods included from Base::Errors

  

#error_first_html, #error_html, #error_keys, #error_list_html, #error_none_html, #error_sentence_html, #errors, #errors?

  
  
  
  
  
  
  
  
  
### Methods included from Base::Database

  

#column, #column?

  
  
  
  
  
  
  
  
  
### Methods included from Base::Options

  

#formtastic_options

  
  
  
  
  
  
  
  
  
### Methods included from Base::Html

  

#dom_id, #dom_index

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(*args)  ⇒ SelectInput 
  

  

  

  
    

Returns a new instance of SelectInput.

  

  

Raises:

  
    
- 
      
      
        (Formtastic::UnsupportedEnumCollection)
      
      
      
    
  

  
    
      

```

161
162
163
164
```

    
    
      

```
# File 'lib/formtastic/inputs/select_input.rb', line 161

def initialize(*args)
  super
  raise Formtastic::UnsupportedEnumCollection if collection_from_enum? && multiple?
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**extra_input_html_options**  ⇒ Object 
  

  

  

  
    
      

```

197
198
199
200
201
202
203
204
```

    
    
      

```
# File 'lib/formtastic/inputs/select_input.rb', line 197

def extra_input_html_options
  {
    :multiple => multiple?,
    :name => multiple? ? input_html_options_name_multiple : input_html_options_name
  }
  
  
end
```

    
  

    
      
  
### 
  
    #**include_blank**  ⇒ Object 
  

  

  

  
    
      

```

177
178
179
```

    
    
      

```
# File 'lib/formtastic/inputs/select_input.rb', line 177

def include_blank
  options.key?(:include_blank) ? options[:include_blank] : (single? && builder.include_blank_for_select_by_default)
end
```

    
  

    
      
  
### 
  
    #**input_html_options**  ⇒ Object 
  

  

  

  
    
      

```

193
194
195
```

    
    
      

```
# File 'lib/formtastic/inputs/select_input.rb', line 193

def input_html_options
  extra_input_html_options.merge(super.reject {|k,v| k==:name && v.nil?} )
end
```

    
  

    
      
  
### 
  
    #**input_html_options_name**  ⇒ Object 
  

  

  

  
    
      

```

206
207
208
209
210
211
212
```

    
    
      

```
# File 'lib/formtastic/inputs/select_input.rb', line 206

def input_html_options_name
  if builder.options.key?(:index)
    "#{object_name}[#{builder.options[:index]}][#{association_primary_key}]"
  else
    "#{object_name}[#{association_primary_key}]"
  end
end
```

    
  

    
      
  
### 
  
    #**input_html_options_name_multiple**  ⇒ Object 
  

  

  

  
    
      

```

214
215
216
```

    
    
      

```
# File 'lib/formtastic/inputs/select_input.rb', line 214

def input_html_options_name_multiple
  input_html_options_name + "[]"
end
```

    
  

    
      
  
### 
  
    #**input_options**  ⇒ Object 
  

  

  

  
    
      

```

189
190
191
```

    
    
      

```
# File 'lib/formtastic/inputs/select_input.rb', line 189

def input_options
  super.merge :include_blank => (include_blank unless prompt?)
end
```

    
  

    
      
  
### 
  
    #**label_html_options**  ⇒ Object 
  

  

  

  
    
      

```

185
186
187
```

    
    
      

```
# File 'lib/formtastic/inputs/select_input.rb', line 185

def label_html_options
  super.merge(:for => input_html_options[:id])
end
```

    
  

    
      
  
### 
  
    #**multiple?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

226
227
228
```

    
    
      

```
# File 'lib/formtastic/inputs/select_input.rb', line 226

def multiple?
  multiple_by_options? || multiple_by_association?
end
```

    
  

    
      
  
### 
  
    #**multiple_by_association?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

218
219
220
```

    
    
      

```
# File 'lib/formtastic/inputs/select_input.rb', line 218

def multiple_by_association?
  reflection && [ :has_many, :has_and_belongs_to_many ].include?(reflection.macro)
end
```

    
  

    
      
  
### 
  
    #**multiple_by_options?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

222
223
224
```

    
    
      

```
# File 'lib/formtastic/inputs/select_input.rb', line 222

def multiple_by_options?
  options[:multiple] || (options[:input_html] && options[:input_html][:multiple])
end
```

    
  

    
      
  
### 
  
    #**prompt?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

181
182
183
```

    
    
      

```
# File 'lib/formtastic/inputs/select_input.rb', line 181

def prompt?
  !!options[:prompt]
end
```

    
  

    
      
  
### 
  
    #**select_html**  ⇒ Object 
  

  

  

  
    
      

```

173
174
175
```

    
    
      

```
# File 'lib/formtastic/inputs/select_input.rb', line 173

def select_html
  builder.select(input_name, collection, input_options, input_html_options)
end
```

    
  

    
      
  
### 
  
    #**single?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

230
231
232
```

    
    
      

```
# File 'lib/formtastic/inputs/select_input.rb', line 230

def single?
  !multiple?
end
```

    
  

    
      
  
### 
  
    #**to_html**  ⇒ Object 
  

  

  

  
    
      

```

166
167
168
169
170
171
```

    
    
      

```
# File 'lib/formtastic/inputs/select_input.rb', line 166

def to_html
  input_wrapping do
    label_html <<
    select_html
  end
end
```