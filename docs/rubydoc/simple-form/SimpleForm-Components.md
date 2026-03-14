# Module: SimpleForm::Components
  
  
  

  

  
  
  
      Extended by:
      ActiveSupport::Autoload
  
  
  
  
  

  

  
  
    Defined in:
    lib/simple_form/components.rb,

  lib/simple_form/components/hints.rb,
 lib/simple_form/components/html5.rb,
 lib/simple_form/components/errors.rb,
 lib/simple_form/components/labels.rb,
 lib/simple_form/components/min_max.rb,
 lib/simple_form/components/pattern.rb,
 lib/simple_form/components/readonly.rb,
 lib/simple_form/components/maxlength.rb,
 lib/simple_form/components/minlength.rb,
 lib/simple_form/components/label_input.rb,
 lib/simple_form/components/placeholders.rb

  
  

## Overview

  
    

Components are a special type of helpers that can work on their own. For example, by using a component, it will automatically change the output under given circumstances without user input. For example, the disabled helper always need a disabled: true option given to the input in order to be enabled. On the other hand, things like hints can generate output automatically by doing I18n lookups.

  

  

## Defined Under Namespace

  
    
      **Modules:** Errors, HTML5, Hints, LabelInput, Labels, Maxlength, MinMax, Minlength, Pattern, Placeholders, Readonly