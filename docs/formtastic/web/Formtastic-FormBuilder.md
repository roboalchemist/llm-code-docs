# Class: Formtastic::FormBuilder
  
  
  

  
  
    Inherits:
    
      ActionView::Helpers::FormBuilder
      
        

          
- Object
          
            
- ActionView::Helpers::FormBuilder
          
            
- Formtastic::FormBuilder
          
        

        show all
      
    
  
  

  
  
  
      Extended by:
      Helpers::ActionHelper, Helpers::ActionsHelper, Helpers::ErrorsHelper, Helpers::InputHelper, Helpers::InputsHelper
  
  
  
  
  

  

  
  
    Defined in:
    lib/formtastic/form_builder.rb
  
  

  
## Constant Summary

  
  
### Constants included
     from Helpers::ErrorsHelper

  

Helpers::ErrorsHelper::INLINE_ERROR_TYPES

  
## Class Attribute Summary collapse

  

    
      
- 
  
    
      .**action_class_finder**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Check ActionClassFinder to see how are inputs resolved.

  

    
      
- 
  
    
      .**action_namespaces**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**all_fields_required_by_default**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**auto_index**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute auto_index.

  

    
      
- 
  
    
      .**collection_label_methods**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**collection_value_methods**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**custom_namespace**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**default_commit_button_accesskey**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**default_error_list_class**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**default_hint_class**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**default_inline_error_class**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**default_text_area_height**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**default_text_area_width**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**default_text_field_size**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**escape_html_entities_in_hints_and_labels**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**file_metadata_suffixes**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**file_methods**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**i18n_cache_lookups**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**i18n_localizer**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**i18n_lookups_by_default**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**include_blank_for_select_by_default**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**inline_errors**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**input_class_finder**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Check InputClassFinder to see how are inputs resolved.

  

    
      
- 
  
    
      .**input_namespaces**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**label_str_method**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**optional_string**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**perform_browser_validations**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**priority_countries**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**priority_time_zones**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**required_string**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**semantic_errors_link_to_inputs**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**skipped_columns**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      .**template**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute template.

  

    
      
- 
  
    
      .**use_required_attribute**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    
  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**initialize**(object_name, object, template, options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**semantic_fields_for**(record_or_name_or_array, *args, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

This is a wrapper around Rails' `ActionView::Helpers::FormBuilder#fields_for`, originally provided to ensure that the `:builder` from `semantic_form_for` was passed down into the nested `fields_for`.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Helpers::ErrorsHelper

  

semantic_errors

  
  
  
  
  
  
  
  
  
### Methods included from LocalizedString

  

#model_name

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from Helpers::ActionsHelper

  

actions

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from Helpers::ActionHelper

  

action

  
  
  
  
  
  
  
  
  
### Methods included from Helpers::InputsHelper

  

inputs

  
  
  
  
  
  
  
  
  
### Methods included from Helpers::InputHelper

  

input

  
  
  
  
  
  
  
  
  
  
  
  
  
  
    
## Class Attribute Details

    
      
      
      
  
### 
  
    .**action_class_finder**  ⇒ Object 
  

  

  

  
    

Check ActionClassFinder to see how are inputs resolved.

  

  

  
    
      

```

20
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 20

configure :action_class_finder, Formtastic::ActionClassFinder
```

    
  

    
      
      
      
  
### 
  
    .**action_namespaces**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

21
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 21

configure :action_namespaces, [::Object, ::Formtastic::Actions]
```

    
  

    
      
      
      
  
### 
  
    .**all_fields_required_by_default**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

22
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 22

configure :all_fields_required_by_default, true
```

    
  

    
      
      
      
  
### 
  
    .**auto_index**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute auto_index.

  

  

  
    
      

```

56
57
58
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 56

def auto_index
  @auto_index
end
```

    
  

    
      
      
      
  
### 
  
    .**collection_label_methods**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

23
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 23

configure :collection_label_methods, %w[to_label display_name full_name name title username login value to_s]
```

    
  

    
      
      
      
  
### 
  
    .**collection_value_methods**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

24
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 24

configure :collection_value_methods, %w[id to_s]
```

    
  

    
      
      
      
  
### 
  
    .**custom_namespace**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

25
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 25

configure :custom_namespace
```

    
  

    
      
      
      
  
### 
  
    .**default_commit_button_accesskey**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

26
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 26

configure :default_commit_button_accesskey
```

    
  

    
      
      
      
  
### 
  
    .**default_error_list_class**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

27
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 27

configure :default_error_list_class, 'errors'
```

    
  

    
      
      
      
  
### 
  
    .**default_hint_class**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

28
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 28

configure :default_hint_class, 'inline-hints'
```

    
  

    
      
      
      
  
### 
  
    .**default_inline_error_class**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

29
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 29

configure :default_inline_error_class, 'inline-errors'
```

    
  

    
      
      
      
  
### 
  
    .**default_text_area_height**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

30
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 30

configure :default_text_area_height, 20
```

    
  

    
      
      
      
  
### 
  
    .**default_text_area_width**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

31
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 31

configure :default_text_area_width
```

    
  

    
      
      
      
  
### 
  
    .**default_text_field_size**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

32
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 32

configure :default_text_field_size
```

    
  

    
      
      
      
  
### 
  
    .**escape_html_entities_in_hints_and_labels**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

33
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 33

configure :escape_html_entities_in_hints_and_labels, true
```

    
  

    
      
      
      
  
### 
  
    .**file_metadata_suffixes**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

34
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 34

configure :file_metadata_suffixes, ['content_type', 'file_name', 'file_size']
```

    
  

    
      
      
      
  
### 
  
    .**file_methods**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

35
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 35

configure :file_methods, [ :file?, :public_filename, :filename ]
```

    
  

    
      
      
      
  
### 
  
    .**i18n_cache_lookups**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

36
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 36

configure :i18n_cache_lookups, true
```

    
  

    
      
      
      
  
### 
  
    .**i18n_localizer**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

37
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 37

configure :i18n_localizer, Formtastic::Localizer
```

    
  

    
      
      
      
  
### 
  
    .**i18n_lookups_by_default**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

38
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 38

configure :i18n_lookups_by_default, true
```

    
  

    
      
      
      
  
### 
  
    .**include_blank_for_select_by_default**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

39
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 39

configure :include_blank_for_select_by_default, true
```

    
  

    
      
      
      
  
### 
  
    .**inline_errors**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

40
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 40

configure :inline_errors, :sentence
```

    
  

    
      
      
      
  
### 
  
    .**input_class_finder**  ⇒ Object 
  

  

  

  
    

Check InputClassFinder to see how are inputs resolved.

  

  

  
    
      

```

42
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 42

configure :input_class_finder, Formtastic::InputClassFinder
```

    
  

    
      
      
      
  
### 
  
    .**input_namespaces**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

43
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 43

configure :input_namespaces, [::Object, ::Formtastic::Inputs]
```

    
  

    
      
      
      
  
### 
  
    .**label_str_method**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

44
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 44

configure :label_str_method, :humanize
```

    
  

    
      
      
      
  
### 
  
    .**optional_string**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

45
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 45

configure :optional_string, ''
```

    
  

    
      
      
      
  
### 
  
    .**perform_browser_validations**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

46
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 46

configure :perform_browser_validations, false
```

    
  

    
      
      
      
  
### 
  
    .**priority_countries**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

47
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 47

configure :priority_countries, ["Australia", "Canada", "United Kingdom", "United States"]
```

    
  

    
      
      
      
  
### 
  
    .**priority_time_zones**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

48
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 48

configure :priority_time_zones, []
```

    
  

    
      
      
      
  
### 
  
    .**required_string**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

49
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 49

configure :required_string, proc { %{<abbr title="#{Formtastic::I18n.t(:required)}">*</abbr>}.html_safe }
```

    
  

    
      
      
      
  
### 
  
    .**semantic_errors_link_to_inputs**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

50
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 50

configure :semantic_errors_link_to_inputs, false
```

    
  

    
      
      
      
  
### 
  
    .**skipped_columns**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

51
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 51

configure :skipped_columns, [:created_at, :updated_at, :created_on, :updated_on, :lock_version, :version]
```

    
  

    
      
      
      
  
### 
  
    .**template**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute template.

  

  

  
    
      

```

54
55
56
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 54

def template
  @template
end
```

    
  

    
      
      
      
  
### 
  
    .**use_required_attribute**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

52
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 52

configure :use_required_attribute, false
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**initialize**(object_name, object, template, options)  ⇒ Object 
  

  

  

  
    
      

```

98
99
100
101
102
103
104
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 98

def initialize(object_name, object, template, options)
  super

  if respond_to?('multipart=') && options.is_a?(Hash) && options[:html]
    self.multipart = options[:html][:multipart]
  end
end
```

    
  

    
      
  
### 
  
    .**semantic_fields_for**(record_or_name_or_array, *args, &block)  ⇒ Object 
  

  

  

  
    
  
    **TODO:**
    

is there a way to test the params structure of the Rails helper we wrap to ensure forward compatibility?

  

This is a wrapper around Rails' `ActionView::Helpers::FormBuilder#fields_for`, originally
provided to ensure that the `:builder` from `semantic_form_for` was passed down into
the nested `fields_for`. Our supported versions of Rails no longer require us to do this,
so this method is provided purely for backwards compatibility and DSL consistency.

When constructing a `fields_for` form fragment *outside* of `semantic_form_for`, please use
`Formtastic::Helpers::FormHelper#semantic_fields_for`.

  

  
  
    
#### Examples:

    
      
      

```
<% semantic_form_for @post do |post| %>
  <% post.semantic_fields_for :author do |author| %>
    <% author.inputs :name %>
  <% end %>
<% end %>

<form ...>
  <fieldset class="inputs">
    <ol>
      <li class="string"><input type='text' name='post[author][name]' id='post_author_name' /></li>
    </ol>
  </fieldset>
</form>
```

    
  

  

See Also:
  

    
      
- ActionView::Helpers::FormBuilder#fields_for
    
      
- ActionView::Helpers::FormHelper#fields_for
    
      
- Helpers::FormHelper#semantic_fields_for
    
  

  
    
      

```

94
95
96
```

    
    
      

```
# File 'lib/formtastic/form_builder.rb', line 94

def semantic_fields_for(record_or_name_or_array, *args, &block)
  fields_for(record_or_name_or_array, *args, &block)
end
```