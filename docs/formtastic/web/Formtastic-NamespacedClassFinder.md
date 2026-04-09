# Class: Formtastic::NamespacedClassFinder
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Formtastic::NamespacedClassFinder
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/formtastic/namespaced_class_finder.rb
  
  

## Overview

  
    

This class implements class resolution in a namespace chain. It
is used both by Formtastic::Helpers::InputHelper and
Formtastic::Helpers::ActionHelper to look up action and input classes.

  

  
  
    
#### Examples:

    
      
        
##### 

Implementing own class finder

      
      

```
# You can implement own class finder that for example prefixes the class name or uses custom module.
class MyInputClassFinder < Formtastic::NamespacedClassFinder
  def initialize(namespaces)
    super [MyNamespace] + namespaces # first lookup in MyNamespace then the defaults
  end

  private

  def class_name(as)
    "My#{super}Input" # for example MyStringInput
  end
end

# in config/initializers/formtastic.rb
Formtastic::FormBuilder.input_class_finder = MyInputClassFinder
```

    
  

  
## Direct Known Subclasses

  

ActionClassFinder, InputClassFinder

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**finder_method**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**use_const_defined?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**class_name**(as)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Converts symbol to class name Overridden in subclasses to create `StringInput` and `ButtonAction`.

  

      
        
- 
  
    
      #**find**(as)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Looks up the given reference in the configured namespaces.

  

      
        
- 
  
    
      #**initialize**(namespaces)  ⇒ NamespacedClassFinder 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of NamespacedClassFinder.

  

      
        
- 
  
    
      #**resolve**(as)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(namespaces)  ⇒ NamespacedClassFinder 
  

  

  

  
    

Returns a new instance of NamespacedClassFinder.

  

  

Parameters:

  
    
- 
      
        namespaces
      
      
        (Array<Module>)
      
      
      
    
  

  
    
      

```

41
42
43
44
```

    
    
      

```
# File 'lib/formtastic/namespaced_class_finder.rb', line 41

def initialize(namespaces)
  @namespaces = namespaces.flatten
  @cache = {}
end
```

    
  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**finder_method**  ⇒ Object 
  

  

  

  
    
      

```

36
37
38
```

    
    
      

```
# File 'lib/formtastic/namespaced_class_finder.rb', line 36

def self.finder_method
  @finder_method ||= use_const_defined? ? :find_with_const_defined : :find_by_trying
end
```

    
  

    
      
  
### 
  
    .**use_const_defined?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

32
33
34
```

    
    
      

```
# File 'lib/formtastic/namespaced_class_finder.rb', line 32

def self.use_const_defined?
  defined?(Rails) && ::Rails.application && ::Rails.application.config.respond_to?(:eager_load) && ::Rails.application.config.eager_load
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**class_name**(as)  ⇒ Object 
  

  

  

  
    

Converts symbol to class name
Overridden in subclasses to create `StringInput` and `ButtonAction`

  

  
  
    
#### Examples:

    
      
      

```
class_name(:string) == "String"
```

    
  

  
    
      

```

68
69
70
```

    
    
      

```
# File 'lib/formtastic/namespaced_class_finder.rb', line 68

def class_name(as)
  as.to_s.camelize
end
```

    
  

    
      
  
### 
  
    #**find**(as)  ⇒ Object 
  

  

  

  
    

Looks up the given reference in the configured namespaces.

Two finder methods are provided, one for development tries to
reference the constant directly, triggering Rails' autoloading
const_missing machinery; the second one instead for production
checks with .const_defined before referencing the constant.

  

  

  
    
      

```

53
54
55
```

    
    
      

```
# File 'lib/formtastic/namespaced_class_finder.rb', line 53

def find(as)
  @cache[as] ||= resolve(as)
end
```

    
  

    
      
  
### 
  
    #**resolve**(as)  ⇒ Object 
  

  

  

  
    
      

```

57
58
59
60
61
```

    
    
      

```
# File 'lib/formtastic/namespaced_class_finder.rb', line 57

def resolve(as)
  class_name = class_name(as)

  finder(class_name) or raise NotFoundError, "class #{class_name}"
end
```