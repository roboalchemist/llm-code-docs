# Module: SimpleForm
  
  
  

  

  
  
  
      Extended by:
      ActiveSupport::Autoload
  
  
  
  
  

  

  
  
    Defined in:
    lib/simple_form.rb,

  lib/simple_form/tags.rb,
 lib/simple_form/inputs.rb,
 lib/simple_form/helpers.rb,
 lib/simple_form/railtie.rb,
 lib/simple_form/version.rb,
 lib/simple_form/map_type.rb,
 lib/simple_form/wrappers.rb,
 lib/simple_form/components.rb,
 lib/simple_form/inputs/base.rb,
 lib/simple_form/form_builder.rb,
 lib/simple_form/wrappers/leaf.rb,
 lib/simple_form/wrappers/many.rb,
 lib/simple_form/wrappers/root.rb,
 lib/simple_form/wrappers/single.rb,
 lib/simple_form/components/hints.rb,
 lib/simple_form/components/html5.rb,
 lib/simple_form/helpers/disabled.rb,
 lib/simple_form/helpers/readonly.rb,
 lib/simple_form/helpers/required.rb,
 lib/simple_form/wrappers/builder.rb,
 lib/simple_form/components/errors.rb,
 lib/simple_form/components/labels.rb,
 lib/simple_form/helpers/autofocus.rb,
 lib/simple_form/inputs/file_input.rb,
 lib/simple_form/inputs/text_input.rb,
 lib/simple_form/components/min_max.rb,
 lib/simple_form/components/pattern.rb,
 lib/simple_form/error_notification.rb,
 lib/simple_form/helpers/validators.rb,
 lib/simple_form/inputs/block_input.rb,
 lib/simple_form/inputs/color_input.rb,
 lib/simple_form/inputs/range_input.rb,
 lib/simple_form/components/readonly.rb,
 lib/simple_form/inputs/hidden_input.rb,
 lib/simple_form/inputs/string_input.rb,
 lib/simple_form/components/maxlength.rb,
 lib/simple_form/components/minlength.rb,
 lib/simple_form/inputs/boolean_input.rb,
 lib/simple_form/inputs/numeric_input.rb,
 lib/simple_form/inputs/weekday_input.rb,
 lib/simple_form/inputs/password_input.rb,
 lib/simple_form/inputs/priority_input.rb,
 lib/simple_form/components/label_input.rb,
 lib/simple_form/inputs/date_time_input.rb,
 lib/simple_form/components/placeholders.rb,
 lib/simple_form/inputs/collection_input.rb,
 lib/simple_form/inputs/rich_text_area_input.rb,
 lib/generators/simple_form/install_generator.rb,
 lib/simple_form/action_view_extensions/builder.rb,
 lib/simple_form/inputs/collection_select_input.rb,
 lib/simple_form/action_view_extensions/form_helper.rb,
 lib/simple_form/inputs/collection_check_boxes_input.rb,
 lib/simple_form/inputs/collection_radio_buttons_input.rb,
 lib/simple_form/inputs/grouped_collection_select_input.rb

  
  

## Defined Under Namespace

  
    
      **Modules:** ActionViewExtensions, Components, Generators, Helpers, Inputs, MapType, Tags, Wrappers
    
  
    
      **Classes:** ErrorNotification, FormBuilder, Railtie, WrapperNotFound
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        CUSTOM_INPUT_DEPRECATION_WARN =
          
        
        

```
<<-WARN
%{name} method now accepts a `wrapper_options` argument. The method definition without the argument is deprecated and will be removed in the next Simple Form version. Change your code from:

  def %{name}

to

  def %{name}(wrapper_options)

See https://github.com/heartcombo/simple_form/pull/997 for more information.
WARN
```

      
        FILE_METHODS_DEPRECATION_WARN =
          
        
        

```
<<-WARN
[SIMPLE_FORM] SimpleForm.file_methods is deprecated and has no effect.

Since version 5, Simple Form now supports automatically discover of file inputs for the following Gems: activestorage, carrierwave, paperclip, refile and shrine.
If you are using a custom method that is not from one of the supported Gems, please change your forms to pass the input type explicitly:

  <%= form.input :avatar, as: :file %>

See http://blog.plataformatec.com.br/2019/09/incorrect-access-control-in-simple-form-cve-2019-16676 for more information.
WARN
```

      
        VERSION =
          
        
        

```
"5.4.1".freeze
```

      
        @@configured =
          
        
        

```
false
```

      
        @@error_method =
          
        
        

```
:first
```

      
        @@error_notification_tag =
          
        
        

```
:p
```

      
        @@error_notification_class =
          
        
        

```
:error_notification
```

      
        @@collection_label_methods =
          
        
        

```
%i[to_label name title to_s]
```

      
        @@collection_value_methods =
          
        
        

```
%i[id to_s]
```

      
        @@collection_wrapper_tag =
          
        
        

```
nil
```

      
        @@collection_wrapper_class =
          
        
        

```
nil
```

      
        @@item_wrapper_tag =
          
        
        

```
:span
```

      
        @@item_wrapper_class =
          
        
        

```
nil
```

      
        @@label_text =
          
        
        

```
->(label, required, explicit_label) { "#{required} #{label}" }
```

      
        @@label_class =
          
        
        

```
nil
```

      
        @@boolean_style =
          
        
        

```
:inline
```

      
        @@form_class =
          
        
        

```
:simple_form
```

      
        @@default_form_class =
          
        
        

```
nil
```

      
        @@generate_additional_classes_for =
          
        
        

```
%i[wrapper label input]
```

      
        @@required_by_default =
          
        
        

```
true
```

      
        @@browser_validations =
          
        
        

```
true
```

      
        @@input_mappings =
          
        
        

```
nil
```

      
        @@wrapper_mappings =
          
        
        

```
nil
```

      
        @@custom_inputs_namespaces =
          
        
        

```
[]
```

      
        @@time_zone_priority =
          
        
        

```
nil
```

      
        @@country_priority =
          
        
        

```
nil
```

      
        @@translate_labels =
          
        
        

```
true
```

      
        @@inputs_discovery =
          
        
        

```
true
```

      
        @@cache_discovery =
          
        
        

```
defined?(Rails.env) && !Rails.env.development?
```

      
        @@button_class =
          
        
        

```
'button'
```

      
        @@field_error_proc =
          
        
        

```
proc do |html_tag, instance_tag|
  html_tag
end
```

      
        @@input_class =
          
        
        

```
nil
```

      
        @@include_default_input_wrapper_class =
          
        
        

```
true
```

      
        @@boolean_label_class =
          
        
        

```
'checkbox'
```

      
        @@default_wrapper =
          
        
        

```
:default
```

      
        @@wrappers =
          
  
    

:nodoc:

  

  

        
        

```
{}
```

      
        @@i18n_scope =
          
        
        

```
'simple_form'
```

      
        @@input_field_error_class =
          
        
        

```
nil
```

      
        @@input_field_valid_class =
          
        
        

```
nil
```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**additional_classes_for**(component)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**build**(options = {}) {|builder| ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Builds a new wrapper using SimpleForm::Wrappers::Builder.

  

      
        
- 
  
    
      .**configured?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      .**default_input_size=**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

SETUP.

  

      
        
- 
  
    
      .**deprecator**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**eager_load!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**file_methods**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**file_methods=**(file_methods)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**form_class=**(value)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**include_component**(component)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Includes a component to be used by Simple Form.

  

      
        
- 
  
    
      .**setup** {|_self| ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Default way to setup Simple Form.

  

      
        
- 
  
    
      .**wrapper**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Retrieves a given wrapper.

  

      
        
- 
  
    
      .**wrappers**(*args, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Define a new wrapper using SimpleForm::Wrappers::Builder and store it in the given name.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**default_wrapper**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

WRAPPER CONFIGURATION The default wrapper to be used by the FormBuilder.

  

      
    

  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**additional_classes_for**(component)  ⇒ Object 
  

  

  

  
    
      

```

264
265
266
```

    
    
      

```
# File 'lib/simple_form.rb', line 264

def self.additional_classes_for(component)
  generate_additional_classes_for.include?(component) ? yield : []
end
```

    
  

    
      
  
### 
  
    .**build**(options = {}) {|builder| ... } ⇒ Object 
  

  

  

  
    

Builds a new wrapper using SimpleForm::Wrappers::Builder.

  

  

Yields:

  
    
- 
      
      
        (builder)
      
      
      
    
  

  
    
      

```

242
243
244
245
246
247
```

    
    
      

```
# File 'lib/simple_form.rb', line 242

def self.build(options = {})
  options[:tag] = :div if options[:tag].nil?
  builder = SimpleForm::Wrappers::Builder.new(options)
  yield builder
  SimpleForm::Wrappers::Root.new(builder.to_a, options)
end
```

    
  

    
      
  
### 
  
    .**configured?**  ⇒ Boolean 
  

  

  

  
    

:nodoc:

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

54
55
56
```

    
    
      

```
# File 'lib/simple_form.rb', line 54

def self.configured? #:nodoc:
  @@configured
end
```

    
  

    
      
  
### 
  
    .**default_input_size=**  ⇒ Object 
  

  

  

  
    

SETUP

  

  

  
    
      

```

270
271
272
```

    
    
      

```
# File 'lib/simple_form.rb', line 270

def self.default_input_size=(*)
  SimpleForm.deprecator.warn "[SIMPLE_FORM] SimpleForm.default_input_size= is deprecated and has no effect", caller
end
```

    
  

    
      
  
### 
  
    .**deprecator**  ⇒ Object 
  

  

  

  
    
      

```

58
59
60
```

    
    
      

```
# File 'lib/simple_form.rb', line 58

def self.deprecator
  @deprecator ||= ActiveSupport::Deprecation.new("5.3", "SimpleForm")
end
```

    
  

    
      
  
### 
  
    .**eager_load!**  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
26
27
```

    
    
      

```
# File 'lib/simple_form.rb', line 23

def self.eager_load!
  super
  SimpleForm::Inputs.eager_load!
  SimpleForm::Components.eager_load!
end
```

    
  

    
      
  
### 
  
    .**file_methods**  ⇒ Object 
  

  

  

  
    
      

```

284
285
286
287
```

    
    
      

```
# File 'lib/simple_form.rb', line 284

def self.file_methods
  SimpleForm.deprecator.warn(FILE_METHODS_DEPRECATION_WARN, caller)
  @@file_methods
end
```

    
  

    
      
  
### 
  
    .**file_methods=**(file_methods)  ⇒ Object 
  

  

  

  
    
      

```

279
280
281
282
```

    
    
      

```
# File 'lib/simple_form.rb', line 279

def self.file_methods=(file_methods)
  SimpleForm.deprecator.warn(FILE_METHODS_DEPRECATION_WARN, caller)
  @@file_methods = file_methods
end
```

    
  

    
      
  
### 
  
    .**form_class=**(value)  ⇒ Object 
  

  

  

  
    
      

```

274
275
276
277
```

    
    
      

```
# File 'lib/simple_form.rb', line 274

def self.form_class=(value)
  SimpleForm.deprecator.warn "[SIMPLE_FORM] SimpleForm.form_class= is deprecated and will be removed in 4.x. Use SimpleForm.default_form_class= instead", caller
  @@form_class = value
end
```

    
  

    
      
  
### 
  
    .**include_component**(component)  ⇒ Object 
  

  

  

  
    

Includes a component to be used by Simple Form. Methods defined in a component will be exposed to be used in the wrapper as Simple::Components

Examples

```
# The application needs to tell where the components will be.
Dir[Rails.root.join('lib/components/**/*.rb')].each { |f| require f }

# Create a custom component in the path specified above.
# lib/components/input_group_component.rb
module InputGroupComponent
  def prepend
    ...
  end

  def append
    ...
  end
end

SimpleForm.setup do |config|
  # Create a wrapper using the custom component.
  config.wrappers :input_group, tag: :div, error_class: :error do |b|
    b.use :label
    b.optional :prepend
    b.use :input
    b.use :append
  end
end

# Using the custom component in the form.
<%= simple_form_for @blog, wrapper: input_group do |f| %>
  <%= f.input :title, prepend: true %>
<% end %>

```

  

  

  
    
      

```

331
332
333
334
335
336
337
```

    
    
      

```
# File 'lib/simple_form.rb', line 331

def self.include_component(component)
  if Module === component
    SimpleForm::Inputs::Base.include(component)
  else
    raise TypeError, "SimpleForm.include_component expects a module but got: #{component.class}"
  end
end
```

    
  

    
      
  
### 
  
    .**setup** {|_self| ... } ⇒ Object 
  

  

  

  
    

Default way to setup Simple Form. Run rails generate simple_form:install to create a fresh initializer with all configuration values.

  

  

Yields:

  
    
- 
      
      
        (_self)
      
      
      
    
  

Yield Parameters:

  
    
- 
      
        _self
      
      
        (SimpleForm)
      
      
      
        —
        

the object that the method was called on

      
    
  

  
    
      

```

291
292
293
294
```

    
    
      

```
# File 'lib/simple_form.rb', line 291

def self.setup
  @@configured = true
  yield self
end
```

    
  

    
      
  
### 
  
    .**wrapper**(name)  ⇒ Object 
  

  

  

  
    

Retrieves a given wrapper

  

  

  
    
      

```

221
222
223
```

    
    
      

```
# File 'lib/simple_form.rb', line 221

def self.wrapper(name)
  @@wrappers[name.to_s] or raise WrapperNotFound, "Couldn't find wrapper with name #{name}"
end
```

    
  

    
      
  
### 
  
    .**wrappers**(*args, &block)  ⇒ Object 
  

  

  

  
    

Define a new wrapper using SimpleForm::Wrappers::Builder and store it in the given name.

  

  

  
    
      

```

231
232
233
234
235
236
237
238
239
```

    
    
      

```
# File 'lib/simple_form.rb', line 231

def self.wrappers(*args, &block)
  if block_given?
    options                 = args.extract_options!
    name                    = args.first || :default
    @@wrappers[name.to_s]   = build(options, &block)
  else
    @@wrappers
  end
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**default_wrapper**  ⇒ Object 
  

  

  

  
    

WRAPPER CONFIGURATION The default wrapper to be used by the FormBuilder.

  

  

  
    
      

```

207
```

    
    
      

```
# File 'lib/simple_form.rb', line 207

mattr_accessor :default_wrapper
```