# Class: FactoryBot::Generators::Base
  
  
  

  
  
    Inherits:
    
      Rails::Generators::NamedBase
      
        

          
- Object
          
            
- Rails::Generators::NamedBase
          
            
- FactoryBot::Generators::Base
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/generators/factory_bot.rb
  
  

## Overview

  
    

:nodoc:

  

  

  
## Direct Known Subclasses

  

ModelGenerator

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**source_root**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**explicit_class_option**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**factory_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**source_root**  ⇒ Object 
  

  

  

  
    
      

```

6
7
8
9
10
11
12
13
14
15
```

    
    
      

```
# File 'lib/generators/factory_bot.rb', line 6

def self.source_root
  path = File.join(
    File.dirname(__FILE__),
    "factory_bot",
    generator_name,
    "templates"
  )

  File.expand_path(path)
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**explicit_class_option**  ⇒ Object 
  

  

  

  
    
      

```

21
22
23
24
25
```

    
    
      

```
# File 'lib/generators/factory_bot.rb', line 21

def explicit_class_option
  return if class_name.underscore == factory_name

  ", class: '#{class_name}'"
end
```

    
  

    
      
  
### 
  
    #**factory_name**  ⇒ Object 
  

  

  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/generators/factory_bot.rb', line 17

def factory_name
  class_name.gsub("::", "").underscore
end
```