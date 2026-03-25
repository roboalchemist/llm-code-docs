# Module: Kramdown::Utils
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/kramdown/utils.rb,

  lib/kramdown/utils/html.rb,
 lib/kramdown/utils/entities.rb,
 lib/kramdown/utils/lru_cache.rb,
 lib/kramdown/utils/unidecoder.rb,
 lib/kramdown/utils/configurable.rb,
 lib/kramdown/utils/string_scanner.rb

  
  

## Overview

  
    

## Utils Module

This module contains utility class/modules/methods that can be used by both parsers and converters.

  

  

## Defined Under Namespace

  
    
      **Modules:** Configurable, Entities, Html, Unidecoder
    
  
    
      **Classes:** LRUCache, StringScanner
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**camelize**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Treat `name` as if it were snake cased (e.g. snake_case) and camelize it (e.g. SnakeCase).

  

      
        
- 
  
    
      .**deep_const_get**(str)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**snake_case**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Treat `name` as if it were camelized (e.g. CamelizedName) and snake-case it (e.g. camelized_name).

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**camelize**(name)  ⇒ Object 
  

  

  

  
    

Treat `name` as if it were snake cased (e.g. snake_case) and camelize it (e.g. SnakeCase).

  

  

  
    
      

```

26
27
28
```

    
    
      

```
# File 'lib/kramdown/utils.rb', line 26

def self.camelize(name)
  name.split('_').inject(+'') {|s, x| s << x[0..0].upcase << x[1..-1] }
end

```

    
  

    
      
  
### 
  
    .**deep_const_get**(str)  ⇒ Object 
  

  

  

  
    
      

```

39
40
41
```

    
    
      

```
# File 'lib/kramdown/utils.rb', line 39

def self.deep_const_get(str)
  ::Object.const_get(str)
end

```

    
  

    
      
  
### 
  
    .**snake_case**(name)  ⇒ Object 
  

  

  

  
    

Treat `name` as if it were camelized (e.g. CamelizedName) and snake-case it (e.g. camelized_name).

  

  

  
    
      

```

31
32
33
34
35
36
37
```

    
    
      

```
# File 'lib/kramdown/utils.rb', line 31

def self.snake_case(name)
  name = name.dup
  name.gsub!(/([A-Z]+)([A-Z][a-z])/, '\1_\2')
  name.gsub!(/([a-z])([A-Z])/, '\1_\2')
  name.downcase!
  name
end

```