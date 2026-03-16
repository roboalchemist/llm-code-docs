# Module: Nokogiri::CSS::SelectorCache
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/css/selector_cache.rb
  
  

## Overview

  
    

:nodoc:

  

  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**[]**(key)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Retrieve the cached XPath expressions for the key.

  

      
        
- 
  
    
      .**[]=**(key, value)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Insert the XPath expressions `value` at the cache key.

  

      
        
- 
  
    
      .**clear_cache**(create_new_object = false)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Clear the cache.

  

      
        
- 
  
    
      .**key**(selector:, visitor:)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Construct a unique key cache key.

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**[]**(key)  ⇒ Object 
  

  

  

  
    

Retrieve the cached XPath expressions for the key

  

  

  
    
      

```

11
12
13
```

    
    
      

```
# File 'lib/nokogiri/css/selector_cache.rb', line 11

def [](key)
  @mutex.synchronize { @cache[key] }
end
```

    
  

    
      
  
### 
  
    .**[]=**(key, value)  ⇒ Object 
  

  

  

  
    

Insert the XPath expressions `value` at the cache key

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/nokogiri/css/selector_cache.rb', line 16

def []=(key, value)
  @mutex.synchronize { @cache[key] = value }
end
```

    
  

    
      
  
### 
  
    .**clear_cache**(create_new_object = false)  ⇒ Object 
  

  

  

  
    

Clear the cache

  

  

  
    
      

```

21
22
23
24
25
26
27
28
29
```

    
    
      

```
# File 'lib/nokogiri/css/selector_cache.rb', line 21

def clear_cache(create_new_object = false)
  @mutex.synchronize do
    if create_new_object # used in tests to avoid 'method redefined' warnings when injecting spies
      @cache = {}
    else
      @cache.clear
    end
  end
end
```

    
  

    
      
  
### 
  
    .**key**(selector:, visitor:)  ⇒ Object 
  

  

  

  
    

Construct a unique key cache key

  

  

  
    
      

```

32
33
34
```

    
    
      

```
# File 'lib/nokogiri/css/selector_cache.rb', line 32

def key(selector:, visitor:)
  [selector, visitor.config]
end
```