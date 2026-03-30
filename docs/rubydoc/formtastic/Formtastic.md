# Module: Formtastic
  
  
  

  

  
  
  
      Extended by:
      ActiveSupport::Autoload
  
  
  
  
  

  

  
  
    Defined in:
    lib/formtastic.rb,

  lib/formtastic/i18n.rb,
 lib/formtastic/inputs.rb,
 lib/formtastic/actions.rb,
 lib/formtastic/helpers.rb,
 lib/formtastic/version.rb,
 lib/formtastic/localizer.rb,
 lib/formtastic/deprecation.rb,
 lib/formtastic/inputs/base.rb,
 lib/formtastic/actions/base.rb,
 lib/formtastic/form_builder.rb,
 lib/formtastic/helpers/enum.rb,
 lib/formtastic/html_attributes.rb,
 lib/formtastic/inputs/base/aria.rb,
 lib/formtastic/inputs/base/html.rb,
 lib/formtastic/inputs/url_input.rb,
 lib/formtastic/localized_string.rb,
 lib/formtastic/actions/buttonish.rb,
 lib/formtastic/inputs/base/hints.rb,
 lib/formtastic/inputs/file_input.rb,
 lib/formtastic/inputs/text_input.rb,
 lib/formtastic/helpers/reflection.rb,
 lib/formtastic/input_class_finder.rb,
 lib/formtastic/inputs/base/errors.rb,
 lib/formtastic/inputs/base/naming.rb,
 lib/formtastic/inputs/color_input.rb,
 lib/formtastic/inputs/email_input.rb,
 lib/formtastic/inputs/phone_input.rb,
 lib/formtastic/inputs/radio_input.rb,
 lib/formtastic/inputs/range_input.rb,
 lib/formtastic/action_class_finder.rb,
 lib/formtastic/actions/link_action.rb,
 lib/formtastic/helpers/form_helper.rb,
 lib/formtastic/inputs/base/choices.rb,
 lib/formtastic/inputs/base/fileish.rb,
 lib/formtastic/inputs/base/numeric.rb,
 lib/formtastic/inputs/base/options.rb,
 lib/formtastic/inputs/base/timeish.rb,
 lib/formtastic/inputs/hidden_input.rb,
 lib/formtastic/inputs/number_input.rb,
 lib/formtastic/inputs/search_input.rb,
 lib/formtastic/inputs/select_input.rb,
 lib/formtastic/inputs/string_input.rb,
 lib/formtastic/actions/input_action.rb,
 lib/formtastic/helpers/input_helper.rb,
 lib/formtastic/inputs/base/database.rb,
 lib/formtastic/inputs/base/wrapping.rb,
 lib/formtastic/inputs/boolean_input.rb,
 lib/formtastic/inputs/country_input.rb,
 lib/formtastic/actions/button_action.rb,
 lib/formtastic/helpers/action_helper.rb,
 lib/formtastic/helpers/errors_helper.rb,
 lib/formtastic/helpers/inputs_helper.rb,
 lib/formtastic/inputs/base/labelling.rb,
 lib/formtastic/inputs/base/stringish.rb,
 lib/formtastic/inputs/datalist_input.rb,
 lib/formtastic/inputs/password_input.rb,
 lib/formtastic/helpers/actions_helper.rb,
 lib/formtastic/inputs/time_zone_input.rb,
 lib/formtastic/inputs/base/collections.rb,
 lib/formtastic/inputs/base/placeholder.rb,
 lib/formtastic/inputs/base/validations.rb,
 lib/formtastic/namespaced_class_finder.rb,
 lib/formtastic/helpers/fieldset_wrapper.rb,
 lib/formtastic/inputs/base/associations.rb,
 lib/formtastic/inputs/check_boxes_input.rb,
 lib/formtastic/inputs/date_picker_input.rb,
 lib/formtastic/inputs/date_select_input.rb,
 lib/formtastic/inputs/time_picker_input.rb,
 lib/formtastic/inputs/time_select_input.rb,
 lib/formtastic/inputs/datetime_picker_input.rb,
 lib/formtastic/inputs/datetime_select_input.rb,
 lib/formtastic/helpers/file_column_detection.rb,
 lib/formtastic/inputs/base/datetime_pickerish.rb,
 lib/generators/formtastic/form/form_generator.rb,
 lib/generators/formtastic/input/input_generator.rb,
 lib/generators/formtastic/install/install_generator.rb,
 lib/generators/formtastic/stylesheets/stylesheets_generator.rb

  
  

## Defined Under Namespace

  
    
      **Modules:** Actions, Helpers, Inputs, LocalizedString
    
  
    
      **Classes:** ActionClassFinder, FormBuilder, FormGenerator, InputClassFinder, InputGenerator, InstallGenerator, Localizer, NamespacedClassFinder, StylesheetsGenerator, UnknownInputError
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        VERSION =
          
        
        

```
"6.0.0"
```

      
        Deprecation =
          
        
        

```
ActiveSupport::Deprecation.new("5.0.0", "Formtastic")
```