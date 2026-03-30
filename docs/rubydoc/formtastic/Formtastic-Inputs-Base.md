# Module: Formtastic::Inputs::Base
  
  
  

  

  
  
  
      Extended by:
      ActiveSupport::Autoload
  
  
  
  
  
      Includes:
      Aria, Associations, Database, Errors, Fileish, Hints, Html, Labelling, Naming, Options, Validations, Wrapping
  
  
  

  
  
    Included in:
    BooleanInput, CheckBoxesInput, ColorInput, CountryInput, DatalistInput, DatePickerInput, DateSelectInput, DatetimePickerInput, DatetimeSelectInput, EmailInput, FileInput, HiddenInput, NumberInput, PasswordInput, PhoneInput, RadioInput, RangeInput, SearchInput, SelectInput, StringInput, TextInput, TimePickerInput, TimeSelectInput, TimeZoneInput, UrlInput
  
  

  
  
    Defined in:
    lib/formtastic/inputs/base.rb,

  lib/formtastic/inputs/base/aria.rb,
 lib/formtastic/inputs/base/html.rb,
 lib/formtastic/inputs/base/hints.rb,
 lib/formtastic/inputs/base/errors.rb,
 lib/formtastic/inputs/base/naming.rb,
 lib/formtastic/inputs/base/choices.rb,
 lib/formtastic/inputs/base/fileish.rb,
 lib/formtastic/inputs/base/numeric.rb,
 lib/formtastic/inputs/base/options.rb,
 lib/formtastic/inputs/base/timeish.rb,
 lib/formtastic/inputs/base/database.rb,
 lib/formtastic/inputs/base/wrapping.rb,
 lib/formtastic/inputs/base/labelling.rb,
 lib/formtastic/inputs/base/stringish.rb,
 lib/formtastic/inputs/base/collections.rb,
 lib/formtastic/inputs/base/placeholder.rb,
 lib/formtastic/inputs/base/validations.rb,
 lib/formtastic/inputs/base/associations.rb,
 lib/formtastic/inputs/base/datetime_pickerish.rb

  
  

## Defined Under Namespace

  
    
      **Modules:** Aria, Associations, Choices, Collections, Database, DatetimePickerish, Errors, Fileish, Hints, Html, Labelling, Naming, Numeric, Options, Placeholder, Stringish, Timeish, Validations, Wrapping
    
  
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**builder**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute builder.

  

    
      
- 
  
    
      #**method**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute method.

  

    
      
- 
  
    
      #**object**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute object.

  

    
      
- 
  
    
      #**object_name**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute object_name.

  

    
      
- 
  
    
      #**options**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute options.

  

    
      
- 
  
    
      #**template**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute template.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(builder, template, object, object_name, method, options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**removed_option!**(old_option_name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Useful for raising an error on previously supported option.

  

      
        
- 
  
    
      #**warn_and_correct_option!**(old_option_name, new_option_name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Useful for deprecating options.

  

      
        
- 
  
    
      #**warn_deprecated_option!**(old_option_name, instructions)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Useful for deprecating options.

  

      
    

  

  
  
  
  
  
  
  
  
  
  
### Methods included from Aria

  

#describedby, #error_aria_attributes

  
  
  
  
  
  
  
  
  
### Methods included from Wrapping

  

#input_wrapping, #wrapper_classes, #wrapper_classes_raw, #wrapper_dom_id, #wrapper_html_options, #wrapper_html_options_raw

  
  
  
  
  
  
  
  
  
### Methods included from Labelling

  

#label_from_options, #label_html, #label_html_options, #label_text, #localized_label, #render_label?, #requirement_text, #requirement_text_or_proc

  
  
  
  
  
  
  
  
  
### Methods included from LocalizedString

  

#model_name

  
  
  
  
  
  
  
  
  
### Methods included from Associations

  

#association, #association_primary_key, #belongs_to?, #has_many?, #reflection

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from Fileish

  

#file?

  
  
  
  
  
  
  
  
  
### Methods included from Validations

  

#autofocus?, #column_limit, #limit, #not_required_through_negated_validation!, #not_required_through_negated_validation?, #optional?, #readonly?, #readonly_attribute?, #readonly_from_options?, #required?, #required_attribute?, #responds_to_global_required?, #validation_integer_only?, #validation_limit, #validation_max, #validation_min, #validation_step, #validations, #validations?, #validator_relevant?

  
  
  
  
  
  
  
  
  
### Methods included from Naming

  

#as, #attributized_method_name, #humanized_method_name, #input_name, #sanitized_method_name, #sanitized_object_name

  
  
  
  
  
  
  
  
  
### Methods included from Hints

  

#hint?, #hint_html, #hint_text, #hint_text_from_options

  
  
  
  
  
  
  
  
  
### Methods included from Errors

  

#error_first_html, #error_html, #error_keys, #error_list_html, #error_none_html, #error_sentence_html, #errors, #errors?

  
  
  
  
  
  
  
  
  
### Methods included from Database

  

#column, #column?

  
  
  
  
  
  
  
  
  
### Methods included from Options

  

#formtastic_options, #input_options

  
  
  
  
  
  
  
  
  
### Methods included from Html

  

#dom_id, #dom_index, #input_html_options, #to_html

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**builder**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute builder.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/formtastic/inputs/base.rb', line 6

def builder
  @builder
end

```

    
  

    
      
      
      
  
### 
  
    #**method**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute method.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/formtastic/inputs/base.rb', line 6

def method
  @method
end

```

    
  

    
      
      
      
  
### 
  
    #**object**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute object.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/formtastic/inputs/base.rb', line 6

def object
  @object
end

```

    
  

    
      
      
      
  
### 
  
    #**object_name**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute object_name.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/formtastic/inputs/base.rb', line 6

def object_name
  @object_name
end

```

    
  

    
      
      
      
  
### 
  
    #**options**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute options.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/formtastic/inputs/base.rb', line 6

def options
  @options
end

```

    
  

    
      
      
      
  
### 
  
    #**template**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute template.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/formtastic/inputs/base.rb', line 6

def template
  @template
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**initialize**(builder, template, object, object_name, method, options)  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
11
12
13
14
15
16
17
18
19
20
```

    
    
      

```
# File 'lib/formtastic/inputs/base.rb', line 8

def initialize(builder, template, object, object_name, method, options)
  @builder = builder
  @template = template
  @object = object
  @object_name = object_name
  @method = method
  @options = options.dup

  # Deprecate :member_label and :member_value, remove v4.0
  member_deprecation_message = "passing an Array of label/value pairs like [['Justin', 2], ['Kate', 3]] into :collection directly (consider building the array in your model using Model.pluck)"
  warn_deprecated_option!(:member_label, member_deprecation_message)
  warn_deprecated_option!(:member_value, member_deprecation_message)
end

```

    
  

    
      
  
### 
  
    #**removed_option!**(old_option_name)  ⇒ Object 
  

  

  

  
    

Useful for raising an error on previously supported option.

  

  

Raises:

  
    
- 
      
      
      
      
    
  

  
    
      

```

38
39
40
```

    
    
      

```
# File 'lib/formtastic/inputs/base.rb', line 38

def removed_option!(old_option_name)
  raise ArgumentError, ":#{old_option_name} is no longer available" if options.key?(old_option_name)
end

```

    
  

    
      
  
### 
  
    #**warn_and_correct_option!**(old_option_name, new_option_name)  ⇒ Object 
  

  

  

  
    

Useful for deprecating options.

  

  

  
    
      

```

23
24
25
26
27
28
```

    
    
      

```
# File 'lib/formtastic/inputs/base.rb', line 23

def warn_and_correct_option!(old_option_name, new_option_name)
  if options.key?(old_option_name)
    Deprecation.warn("The :#{old_option_name} option is deprecated in favour of :#{new_option_name} and will be removed from Formtastic in the next version", caller_locations(6))
    options[new_option_name] = options.delete(old_option_name)
  end
end

```

    
  

    
      
  
### 
  
    #**warn_deprecated_option!**(old_option_name, instructions)  ⇒ Object 
  

  

  

  
    

Useful for deprecating options.

  

  

  
    
      

```

31
32
33
34
35
```

    
    
      

```
# File 'lib/formtastic/inputs/base.rb', line 31

def warn_deprecated_option!(old_option_name, instructions)
  if options.key?(old_option_name)
    Deprecation.warn("The :#{old_option_name} option is deprecated in favour of `#{instructions}`. :#{old_option_name} will be removed in the next version", caller_locations(6))
  end
end

```