# Class: Kramdown::Utils::LRUCache
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Kramdown::Utils::LRUCache
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/kramdown/utils/lru_cache.rb
  
  

## Overview

  
    

A simple least recently used (LRU) cache.

The cache relies on the fact that Ruby’s Hash class maintains insertion order. So deleting and re-inserting a key-value pair on access moves the key to the last position. When an entry is added and the cache is full, the first entry is removed.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**[]**(key)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the stored value for `key` or `nil` if no value was stored under the key.

  

      
        
- 
  
    
      #**[]=**(key, value)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Stores the `value` under the `key`.

  

      
        
- 
  
    
      #**initialize**(size)  ⇒ LRUCache 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Creates a new LRUCache that can hold `size` entries.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(size)  ⇒ LRUCache 
  

  

  

  
    

Creates a new LRUCache that can hold `size` entries.

  

  

  
    
      

```

21
22
23
24
```

    
    
      

```
# File 'lib/kramdown/utils/lru_cache.rb', line 21

def initialize(size)
  @size = size
  @cache = {}
end

```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**[]**(key)  ⇒ Object 
  

  

  

  
    

Returns the stored value for `key` or `nil` if no value was stored under the key.

  

  

  
    
      

```

27
28
29
```

    
    
      

```
# File 'lib/kramdown/utils/lru_cache.rb', line 27

def [](key)
  (val = @cache.delete(key)).nil? ? nil : @cache[key] = val
end

```

    
  

    
      
  
### 
  
    #**[]=**(key, value)  ⇒ Object 
  

  

  

  
    

Stores the `value` under the `key`.

  

  

  
    
      

```

32
33
34
35
36
```

    
    
      

```
# File 'lib/kramdown/utils/lru_cache.rb', line 32

def []=(key, value)
  @cache.delete(key)
  @cache[key] = value
  @cache.shift if @cache.length > @size
end

```