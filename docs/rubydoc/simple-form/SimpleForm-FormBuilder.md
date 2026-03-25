# Class: SimpleForm::FormBuilder
  
  
  

  
  
    Inherits:
    
      ActionView::Helpers::FormBuilder
      
        

          
- Object
          
            
- ActionView::Helpers::FormBuilder
          
            
- SimpleForm::FormBuilder
          
        

        show all
      
    
  
  

  
  
  
      Extended by:
      MapType
  
  
  
  
  
      Includes:
      Inputs
  
  
  

  

  
  
    Defined in:
    lib/simple_form/form_builder.rb
  
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        ACTIONS =
          
  
    

When action is create or update, we still should use new and edit

  

  

        
        

```
{
  'create' => 'new',
  'update' => 'edit'
}
```

      
        ATTRIBUTE_COMPONENTS =
          
        
        

```
%i[html5 min_max maxlength minlength placeholder pattern readonly]
```

      
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**object**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute object.

  

    
      
- 
  
    
      #**object_name**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute object_name.

  

    
      
- 
  
    
      #**template**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute template.

  

    
      
- 
  
    
      #**wrapper**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute wrapper.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**discovery_cache**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**association**(association, options = {}, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Helper for dealing with association selects/radios, generating the collection automatically.

  

      
        
- 
  
    
      #**button**(type, *args, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**button_button**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Creates a button:.

  

      
        
- 
  
    
      #**collection_check_boxes**(method, collection, value_method, text_method, options = {}, html_options = {}, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Creates a collection of check boxes for each item in the collection, associated with a clickable label.

  

      
        
- 
  
    
      #**collection_radio_buttons**(method, collection, value_method, text_method, options = {}, html_options = {}, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a collection of radio inputs for the attribute.

  

      
        
- 
  
    
      #**error**(attribute_name, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Creates an error tag based on the given attribute, only when the attribute contains errors.

  

      
        
- 
  
    
      #**error_notification**(options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Creates an error notification message that only appears when the form object has some error.

  

      
        
- 
  
    
      #**full_error**(attribute_name, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return the error but also considering its name.

  

      
        
- 
  
    
      #**hint**(attribute_name, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Creates a hint tag for the given attribute.

  

      
        
- 
  
    
      #**initialize**  ⇒ FormBuilder 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**input**(attribute_name, options = {}, &block)  ⇒ Object 
    

    
      (also: #attribute)
    
  
  
  
  
  
  
  
  

  
    

Basic input helper, combines all components in the stack to generate input html based on options the user define and some guesses through database column information.

  

      
        
- 
  
    
      #**input_field**(attribute_name, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Creates a input tag for the given attribute.

  

      
        
- 
  
    
      #**label**(attribute_name, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Creates a default label tag for the given attribute.

  

      
        
- 
  
    
      #**lookup_action**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The action to be used in lookup.

  

      
        
- 
  
    
      #**lookup_model_names**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Extract the model names from the object_name mess, ignoring numeric and explicit child indexes.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from MapType

  

extended, map_type

  
  
  
  
  
  
  
  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ FormBuilder 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

41
42
43
44
45
46
```

    
    
      

```
# File 'lib/simple_form/form_builder.rb', line 41

def initialize(*) #:nodoc:
  super
  @object   = convert_to_model(@object)
  @defaults = options[:defaults]
  @wrapper  = SimpleForm.wrapper(options[:wrapper] || SimpleForm.default_wrapper)
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**object**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute object.

  

  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/simple_form/form_builder.rb', line 8

def object
  @object
end
```

    
  

    
      
      
      
  
### 
  
    #**object_name**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute object_name.

  

  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/simple_form/form_builder.rb', line 8

def object_name
  @object_name
end
```

    
  

    
      
      
      
  
### 
  
    #**template**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute template.

  

  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/simple_form/form_builder.rb', line 8

def template
  @template
end
```

    
  

    
      
      
      
  
### 
  
    #**wrapper**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute wrapper.

  

  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/simple_form/form_builder.rb', line 8

def wrapper
  @wrapper
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**discovery_cache**  ⇒ Object 
  

  

  

  
    
      

```

37
38
39
```

    
    
      

```
# File 'lib/simple_form/form_builder.rb', line 37

def self.discovery_cache
  @discovery_cache ||= {}
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**association**(association, options = {}, &block)  ⇒ Object 
  

  

  

  
    

Helper for dealing with association selects/radios, generating the collection automatically. It’s just a wrapper to input, so all options supported in input are also supported by association. Some extra options can also be given:

## Examples

```
simple_form_for @user do |f|
  f.association :company          # Company.all
end

f.association :company, collection: Company.all(order: 'name')
# Same as using :order option, but overriding collection

```

## Block

When a block is given, association simple behaves as a proxy to simple_fields_for:

```
f.association :company do |c|
  c.input :name
  c.input :type
end

```

From the options above, only :collection can also be supplied.

Please note that the association helper is currently only tested with Active Record. Depending on the ORM you are using your mileage may vary.

  

  

Raises:

  
    
- 
      
      
        (ArgumentError)
      
      
      
    
  

  
    
      

```

207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
```

    
    
      

```
# File 'lib/simple_form/form_builder.rb', line 207

def association(association, options = {}, &block)
  options = options.dup

  return simple_fields_for(*[association,
    options.delete(:collection), options].compact, &block) if block_given?

  raise ArgumentError, "Association cannot be used in forms not associated with an object" unless @object

  reflection = find_association_reflection(association)
  raise "Association #{association.inspect} not found" unless reflection

  options[:as] ||= :select
  options[:collection] ||= fetch_association_collection(reflection, options)

  attribute = build_association_attribute(reflection, association, options)

  input(attribute, options.merge(reflection: reflection))
end
```

    
  

    
      
  
### 
  
    #**button**(type, *args, &block)  ⇒ Object 
  

  

  

  
    
      

```

237
238
239
240
241
242
243
244
245
246
```

    
    
      

```
# File 'lib/simple_form/form_builder.rb', line 237

def button(type, *args, &block)
  options = args.extract_options!.dup
  options[:class] = [SimpleForm.button_class, options[:class]].compact
  args << options
  if respond_to?(:"#{type}_button")
    send(:"#{type}_button", *args, &block)
  else
    send(type, *args, &block)
  end
end
```

    
  

    
      
  
### 
  
    #**button_button**  ⇒ Object 
  

  

  

  
    

Creates a button:

```
form_for @user do |f|
  f.button :submit
end

```

It just acts as a proxy to method name given. We also alias original Rails button implementation (3.2 forward (to delegate to the original when calling ‘f.button :button`.

  

  

  
    
      

```

236
```

    
    
      

```
# File 'lib/simple_form/form_builder.rb', line 236

alias_method :button_button, :button
```

    
  

    
      
  
### 
  
    #**collection_check_boxes**(method, collection, value_method, text_method, options = {}, html_options = {}, &block)  ⇒ Object 
  

  

  

  
    

Creates a collection of check boxes for each item in the collection, associated with a clickable label. Use value_method and text_method to convert items in the collection for use as text/value in check boxes. You can give a symbol or a proc to both value_method and text_method, that will be evaluated for each item in the collection.

## Examples

```
form_for @user do |f|
  f.collection_check_boxes :options, [[true, 'Yes'] ,[false, 'No']], :first, :last
end

<input name="user[options][]" type="hidden" value="" />
<input id="user_options_true" name="user[options][]" type="checkbox" value="true" />
<label class="collection_check_boxes" for="user_options_true">Yes</label>
<input name="user[options][]" type="hidden" value="" />
<input id="user_options_false" name="user[options][]" type="checkbox" value="false" />
<label class="collection_check_boxes" for="user_options_false">No</label>

```

It is also possible to give a block that should generate the check box + label. To wrap the check box with the label, for instance:

```
form_for @user do |f|
  f.collection_check_boxes(
    :options, [[true, 'Yes'] ,[false, 'No']], :first, :last
  ) do |b|
    b.label { b.check_box + b.text }
  end
end

```

## Options

Collection check box accepts some extra options:

```
* checked  => the value or values that should be checked initially. Accepts
              a single item or an array of items. It overrides existing associations.

* disabled => the value or values that should be disabled. Accepts a single
              item or an array of items.

* collection_wrapper_tag   => the tag to wrap the entire collection.

* collection_wrapper_class => the CSS class to use for collection_wrapper_tag. This option
                              is ignored if the :collection_wrapper_tag option is blank.

* item_wrapper_tag         => the tag to wrap each item in the collection.

* item_wrapper_class       => the CSS class to use for item_wrapper_tag

* a block                  => to generate the label + check box or any other component.

```

  

  

  
    
      

```

451
452
453
```

    
    
      

```
# File 'lib/simple_form/form_builder.rb', line 451

def collection_check_boxes(method, collection, value_method, text_method, options = {}, html_options = {}, &block)
  SimpleForm::Tags::CollectionCheckBoxes.new(@object_name, method, @template, collection, value_method, text_method, objectify_options(options), @default_options.merge(html_options)).render(&block)
end
```

    
  

    
      
  
### 
  
    #**collection_radio_buttons**(method, collection, value_method, text_method, options = {}, html_options = {}, &block)  ⇒ Object 
  

  

  

  
    

Create a collection of radio inputs for the attribute. Basically this helper will create a radio input associated with a label for each text/value option in the collection, using value_method and text_method to convert these text/value. You can give a symbol or a proc to both value_method and text_method, that will be evaluated for each item in the collection.

## Examples

```
form_for @user do |f|
  f.collection_radio_buttons :options, [[true, 'Yes'] ,[false, 'No']], :first, :last
end

<input id="user_options_true" name="user[options]" type="radio" value="true" />
<label class="collection_radio_buttons" for="user_options_true">Yes</label>
<input id="user_options_false" name="user[options]" type="radio" value="false" />
<label class="collection_radio_buttons" for="user_options_false">No</label>

```

It is also possible to give a block that should generate the radio + label. To wrap the radio with the label, for instance:

```
form_for @user do |f|
  f.collection_radio_buttons(
    :options, [[true, 'Yes'] ,[false, 'No']], :first, :last
  ) do |b|
    b.label { b.radio_button + b.text }
  end
end

```

## Options

Collection radio accepts some extra options:

```
* checked  => the value that should be checked initially.

* disabled => the value or values that should be disabled. Accepts a single
              item or an array of items.

* collection_wrapper_tag   => the tag to wrap the entire collection.

* collection_wrapper_class => the CSS class to use for collection_wrapper_tag

* item_wrapper_tag         => the tag to wrap each item in the collection.

* item_wrapper_class       => the CSS class to use for item_wrapper_tag

* a block                  => to generate the label + radio or any other component.

```

  

  

  
    
      

```

397
398
399
```

    
    
      

```
# File 'lib/simple_form/form_builder.rb', line 397

def collection_radio_buttons(method, collection, value_method, text_method, options = {}, html_options = {}, &block)
  SimpleForm::Tags::CollectionRadioButtons.new(@object_name, method, @template, collection, value_method, text_method, objectify_options(options), @default_options.merge(html_options)).render(&block)
end
```

    
  

    
      
  
### 
  
    #**error**(attribute_name, options = {})  ⇒ Object 
  

  

  

  
    

Creates an error tag based on the given attribute, only when the attribute contains errors. All the given options are sent as :error_html.

## Examples

```
f.error :name
f.error :name, id: "cool_error"

```

  

  

  
    
      

```

256
257
258
259
260
261
262
263
264
```

    
    
      

```
# File 'lib/simple_form/form_builder.rb', line 256

def error(attribute_name, options = {})
  options = options.dup

  options[:error_html] = options.except(:error_tag, :error_prefix, :error_method)
  column      = find_attribute_column(attribute_name)
  input_type  = default_input_type(attribute_name, column, options)
  wrapper.find(:error).
    render(SimpleForm::Inputs::Base.new(self, attribute_name, column, input_type, options))
end
```

    
  

    
      
  
### 
  
    #**error_notification**(options = {})  ⇒ Object 
  

  

  

  
    

Creates an error notification message that only appears when the form object has some error. You can give a specific message with the :message option, otherwise it will look for a message using I18n. All other options given are passed straight as html options to the html tag.

## Examples

```
f.error_notification
f.error_notification message: 'Something went wrong'
f.error_notification id: 'user_error_message', class: 'form_error'

```

  

  

  
    
      

```

346
347
348
```

    
    
      

```
# File 'lib/simple_form/form_builder.rb', line 346

def error_notification(options = {})
  SimpleForm::ErrorNotification.new(self, options).render
end
```

    
  

    
      
  
### 
  
    #**full_error**(attribute_name, options = {})  ⇒ Object 
  

  

  

  
    

Return the error but also considering its name. This is used when errors for a hidden field need to be shown.

## Examples

```
f.full_error :token #=> <span class="error">Token is invalid</span>

```

  

  

  
    
      

```

273
274
275
276
277
278
279
280
281
282
283
```

    
    
      

```
# File 'lib/simple_form/form_builder.rb', line 273

def full_error(attribute_name, options = {})
  options = options.dup

  options[:error_prefix] ||= if object.class.respond_to?(:human_attribute_name)
    object.class.human_attribute_name(attribute_name.to_s, { base: object })
  else
    attribute_name.to_s.humanize
  end

  error(attribute_name, options)
end
```

    
  

    
      
  
### 
  
    #**hint**(attribute_name, options = {})  ⇒ Object 
  

  

  

  
    

Creates a hint tag for the given attribute. Accepts a symbol indicating an attribute for I18n lookup or a string. All the given options are sent as :hint_html.

## Examples

```
f.hint :name # Do I18n lookup
f.hint :name, id: "cool_hint"
f.hint "Don't forget to accept this"

```

  

  

  
    
      

```

295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
```

    
    
      

```
# File 'lib/simple_form/form_builder.rb', line 295

def hint(attribute_name, options = {})
  options = options.dup

  options[:hint_html] = options.except(:hint_tag, :hint)
  if attribute_name.is_a?(String)
    options[:hint] = attribute_name
    attribute_name, column, input_type = nil, nil, nil
  else
    column      = find_attribute_column(attribute_name)
    input_type  = default_input_type(attribute_name, column, options)
  end

  wrapper.find(:hint).
    render(SimpleForm::Inputs::Base.new(self, attribute_name, column, input_type, options))
end
```

    
  

    
      
  
### 
  
    #**input**(attribute_name, options = {}, &block)  ⇒ Object 
  

  
    Also known as:
    attribute
    
  

  

  
    

Basic input helper, combines all components in the stack to generate input html based on options the user define and some guesses through database column information. By default a call to input will generate label + input + hint (when defined) + errors (when exists), and all can be configured inside a wrapper html.

If a block is given, the contents of the block will replace the input field that would otherwise be generated automatically. The content will be given a label and wrapper div to make it consistent with the other elements in the form.

## Examples

```
# Imagine @user has error "can't be blank" on name
simple_form_for @user do |f|
  f.input :name, hint: 'My hint'
end

```

This is the output html (only the input portion, not the form):

```

  * Super User Name!

My hint
can't be blank

```

Each database type will render a default input, based on some mappings and heuristic to determine which is the best option.

You have some options for the input to enable/disable some functions:

```
as: allows you to define the input type you want, for instance you
       can use it to generate a text field for a date column.

required: defines whether this attribute is required or not. True
            by default.

```

The fact SimpleForm is built in components allow the interface to be unified. So, for instance, if you need to disable :hint for a given input, you can pass hint: false. The same works for :error, :label and :wrapper.

Besides the html for any component can be changed. So, if you want to change the label html you just need to give a hash to :label_html. To configure the input html, supply :input_html instead and so on.

## Options

Some inputs, as datetime, time and select allow you to give extra options, like prompt and/or include blank. Such options are given in plainly:

```
f.input :created_at, include_blank: true

```

## Collection

When playing with collections (:radio_buttons, :check_boxes and :select inputs), you have three extra options:

```
collection: use to determine the collection to generate the radio or select

label_method: the method to apply on the array collection to get the label

value_method: the method to apply on the array collection to get the value

```

## Priority

Some inputs, as :time_zone and :country accepts a :priority option. If none is given SimpleForm.time_zone_priority and SimpleForm.country_priority are used respectively.

  

  

  
    
      

```

118
119
120
121
122
123
124
125
```

    
    
      

```
# File 'lib/simple_form/form_builder.rb', line 118

def input(attribute_name, options = {}, &block)
  options = @defaults.deep_dup.deep_merge(options) if @defaults

  input   = find_input(attribute_name, options, &block)
  wrapper = find_wrapper(input.input_type, options)

  wrapper.render input
end
```

    
  

    
      
  
### 
  
    #**input_field**(attribute_name, options = {})  ⇒ Object 
  

  

  

  
    

Creates a input tag for the given attribute. All the given options are sent as :input_html.

## Examples

```
simple_form_for @user do |f|
  f.input_field :name
end

```

This is the output html (only the input portion, not the form):

```
<input class="string required" id="user_name" maxlength="100"
   name="user[name]" type="text" value="Carlos" />

```

It also support validation classes once it is configured.

```
# config/initializers/simple_form.rb
SimpleForm.setup do |config|
  config.input_field_valid_class = 'is-valid'
  config.input_field_error_class = 'is-invalid'
end

simple_form_for @user do |f|
  f.input_field :name
end

```

When the validation happens, the input will be rendered with the class configured according to the validation:

- 

when the input is valid:

```
<input class="is-valid string required" id="user_name" value="Carlos" />

```

- 

when the input is invalid:

```
<input class="is-invalid string required" id="user_name" value="" />

```

  

  

  
    
      

```

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
# File 'lib/simple_form/form_builder.rb', line 165

def input_field(attribute_name, options = {})
  components = (wrapper.components.map(&:namespace) & ATTRIBUTE_COMPONENTS)

  options = options.dup
  options[:input_html] = options.except(:as, :boolean_style, :collection, :disabled, :label_method, :value_method, :prompt, *components)
  options = @defaults.deep_dup.deep_merge(options) if @defaults

  input      = find_input(attribute_name, options)
  wrapper    = find_wrapper(input.input_type, options)
  components = build_input_field_components(components.push(:input))

  SimpleForm::Wrappers::Root.new(components, wrapper.options.merge(wrapper: false)).render input
end
```

    
  

    
      
  
### 
  
    #**label**(attribute_name, *args)  ⇒ Object 
  

  

  

  
    

Creates a default label tag for the given attribute. You can give a label through the :label option or using i18n. All the given options are sent as :label_html.

## Examples

```
f.label :name                     # Do I18n lookup
f.label :name, "Name"             # Same behavior as Rails, do not add required tag
f.label :name, label: "Name"      # Same as above, but adds required tag

f.label :name, required: false
f.label :name, id: "cool_label"

```

  

  

  
    
      

```

324
325
326
327
328
329
330
331
332
333
```

    
    
      

```
# File 'lib/simple_form/form_builder.rb', line 324

def label(attribute_name, *args)
  return super if args.first.is_a?(String) || block_given?

  options = args.extract_options!.dup
  options[:label_html] = options.except(:label, :label_text, :required, :as)

  column      = find_attribute_column(attribute_name)
  input_type  = default_input_type(attribute_name, column, options)
  SimpleForm::Inputs::Base.new(self, attribute_name, column, input_type, options).label
end
```

    
  

    
      
  
### 
  
    #**lookup_action**  ⇒ Object 
  

  

  

  
    

The action to be used in lookup.

  

  

  
    
      

```

474
475
476
477
478
479
480
481
```

    
    
      

```
# File 'lib/simple_form/form_builder.rb', line 474

def lookup_action #:nodoc:
  @lookup_action ||= begin
    action = template.controller && template.controller.action_name
    return unless action
    action = action.to_s
    ACTIONS[action] || action
  end
end
```

    
  

    
      
  
### 
  
    #**lookup_model_names**  ⇒ Object 
  

  

  

  
    

Extract the model names from the object_name mess, ignoring numeric and explicit child indexes.

Example:

route[0][1]
“route”, “blocks”, “blocks_learning_object”, “foo”

  

  

  
    
      

```

463
464
465
466
467
468
469
470
471
```

    
    
      

```
# File 'lib/simple_form/form_builder.rb', line 463

def lookup_model_names #:nodoc:
  @lookup_model_names ||= begin
    child_index = options[:child_index]
    names = object_name.to_s.scan(/(?!\d)\w+/).flatten
    names.delete(child_index) if child_index
    names.each { |name| name.gsub!('_attributes', '') }
    names.freeze
  end
end
```