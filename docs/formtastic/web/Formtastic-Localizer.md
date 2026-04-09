# Class: Formtastic::Localizer
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Formtastic::Localizer
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/formtastic/localizer.rb
  
  

## Overview

  
    

Implementation for looking up localized values within Formtastic using I18n, if no
explicit value (like the `:label` option) is set and I18n-lookups are enabled in the
configuration.

You can subclass this to implement your own Localizer, and configure Formtastic to use this
localizer with:

Formtastic::FormBuilder.i18n_localizer

Enabled/disable i18n lookups completely with:

Formtastic::FormBuilder.i18n_lookups_by_default = true/false

Lookup priority:

'formtastic.%type.%model.%action.%attribute'
  'formtastic.%type.%model.%attribute'
  'formtastic.%type.%attribute'

Example:

'formtastic.labels.post.edit.title'
  'formtastic.labels.post.title'
  'formtastic.labels.title'

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** Cache
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**builder**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute builder.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**cache**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(current_builder)  ⇒ Localizer 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Localizer.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(current_builder)  ⇒ Localizer 
  

  

  

  
    

Returns a new instance of Localizer.

  

  

  
    
      

```

56
57
58
```

    
    
      

```
# File 'lib/formtastic/localizer.rb', line 56

def initialize(current_builder)
  self.builder = current_builder
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**builder**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute builder.

  

  

  
    
      

```

50
51
52
```

    
    
      

```
# File 'lib/formtastic/localizer.rb', line 50

def builder
  @builder
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**cache**  ⇒ Object 
  

  

  

  
    
      

```

52
53
54
```

    
    
      

```
# File 'lib/formtastic/localizer.rb', line 52

def self.cache
  @cache ||= Cache.new
end
```