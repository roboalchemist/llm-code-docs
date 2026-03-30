# Class: Jekyll::Cache
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::Cache

        show all
      

    Defined in:
    lib/jekyll/cache.rb
  
## Class Attribute Summary collapse

-
  
      .**base_cache**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

class-wide base cache reader.

-
  
      .**cache_dir**  ⇒ Object 

class-wide cache location.

-
  
      .**disk_cache_enabled**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

class-wide base cache reader.

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**clear**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Clear all caches.

-
  
      .**clear_if_config_changed**(config)  ⇒ Object 

Compare the current config to the cached config If they are different, clear all caches.

-
  
      .**disable_disk_cache!**  ⇒ Object 

Disable Marshaling cached items to disk.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**[]**(key)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Retrieve a cached item Raises if key does not exist in cache.

-
  
      #**[]=**(key, value)  ⇒ Object 

Add an item to cache.

-
  
      #**clear**  ⇒ Object 

Clear this particular cache.

-
  
      #**delete**(key)  ⇒ Object 

Remove one particular item from the cache.

-
  
      #**disk_cache_enabled?**  ⇒ Boolean 

-
  
      #**getset**(key)  ⇒ Object 

If an item already exists in the cache, retrieve it.

-
  
      #**initialize**(name)  ⇒ Cache 

    constructor
  
  
  
  
  
  

  
    

Get an existing named cache, or create a new one if none exists.

-
  
      #**key?**(key)  ⇒ Boolean 

Check if `key` already exists in this cache.

## Constructor Details

###
  
    #**initialize**(name)  ⇒ Cache 
  

  

  

  
    

Get an existing named cache, or create a new one if none exists

name - name of the cache

Returns nothing.

```

62
63
64
65
```

```
# File 'lib/jekyll/cache.rb', line 62

def initialize(name)
  @cache = Jekyll::Cache.base_cache[name] ||= {}
  @name = name.gsub(%r![^\w\s-]!, "-")
end
```

## Class Attribute Details

###
  
    .**base_cache**  ⇒ Object  (readonly)
  

  

  

  
    

class-wide base cache reader

```

16
17
18
```

```
# File 'lib/jekyll/cache.rb', line 16

def base_cache
  @base_cache
end
```

###
  
    .**cache_dir**  ⇒ Object 
  

  

  

  
    

class-wide cache location

```

14
15
16
```

```
# File 'lib/jekyll/cache.rb', line 14

def cache_dir
  @cache_dir
end
```

###
  
    .**disk_cache_enabled**  ⇒ Object  (readonly)
  

  

  

  
    

class-wide base cache reader

```

16
17
18
```

```
# File 'lib/jekyll/cache.rb', line 16

def disk_cache_enabled
  @disk_cache_enabled
end
```

## Class Method Details

###
  
    .**clear**  ⇒ Object 
  

  

  

  
    

Clear all caches

```

25
26
27
28
```

```
# File 'lib/jekyll/cache.rb', line 25

def clear
  delete_cache_files
  base_cache.each_value(&:clear)
end
```

###
  
    .**clear_if_config_changed**(config)  ⇒ Object 
  

  

  

  
    

Compare the current config to the cached config If they are different, clear all caches

Returns nothing.

```

34
35
36
37
38
39
40
41
42
43
```

```
# File 'lib/jekyll/cache.rb', line 34

def clear_if_config_changed(config)
  config = config.inspect
  cache = Jekyll::Cache.new "Jekyll::Cache"
  return if cache.key?("config") && cache["config"] == config

  clear
  cache = Jekyll::Cache.new "Jekyll::Cache"
  cache["config"] = config
  nil
end
```

###
  
    .**disable_disk_cache!**  ⇒ Object 
  

  

  

  
    

Disable Marshaling cached items to disk

```

20
21
22
```

```
# File 'lib/jekyll/cache.rb', line 20

def disable_disk_cache!
  @disk_cache_enabled = false
end
```

## Instance Method Details

###
  
    #**[]**(key)  ⇒ Object 
  

  

  

  
    

Retrieve a cached item Raises if key does not exist in cache

Returns cached value

```

77
78
79
80
81
82
83
84
85
86
```

```
# File 'lib/jekyll/cache.rb', line 77

def [](key)
  return @cache[key] if @cache.key?(key)

  path = path_to(hash(key))
  if disk_cache_enabled? && File.file?(path) && File.readable?(path)
    @cache[key] = load(path)
  else
    raise
  end
end
```

###
  
    #**[]=**(key, value)  ⇒ Object 
  

  

  

  
    

Add an item to cache

Returns nothing.

```

91
92
93
94
95
96
97
98
99
100
```

```
# File 'lib/jekyll/cache.rb', line 91

def []=(key, value)
  @cache[key] = value
  return unless disk_cache_enabled?

  path = path_to(hash(key))
  value = new Hash(value) if value.is_a?(Hash) && !value.default.nil?
  dump(path, value)
rescue TypeError
  Jekyll.logger.debug "Cache:", "Cannot dump object #{key}"
end
```

###
  
    #**clear**  ⇒ Object 
  

  

  

  
    

Clear this particular cache

```

68
69
70
71
```

```
# File 'lib/jekyll/cache.rb', line 68

def clear
  delete_cache_files
  @cache.clear
end
```

###
  
    #**delete**(key)  ⇒ Object 
  

  

  

  
    

Remove one particular item from the cache

Returns nothing.

```

115
116
117
118
```

```
# File 'lib/jekyll/cache.rb', line 115

def delete(key)
  @cache.delete(key)
  File.delete(path_to(hash(key))) if disk_cache_enabled?
end
```

###
  
    #**disk_cache_enabled?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

134
135
136
```

```
# File 'lib/jekyll/cache.rb', line 134

def disk_cache_enabled?
  !!Jekyll::Cache.disk_cache_enabled
end
```

###
  
    #**getset**(key)  ⇒ Object 
  

  

  

  
    

If an item already exists in the cache, retrieve it. Else execute code block, and add the result to the cache, and return that result.

```

104
105
106
107
108
109
110
```

```
# File 'lib/jekyll/cache.rb', line 104

def getset(key)
  self[key]
rescue StandardError
  value = yield
  self[key] = value
  value
end
```

###
  
    #**key?**(key)  ⇒ Boolean 
  

  

  

  
    

Check if `key` already exists in this cache

Returns true if key exists in the cache, false otherwise

Returns:

-

        (Boolean)

```

123
124
125
126
127
128
129
130
131
132
```

```
# File 'lib/jekyll/cache.rb', line 123

def key?(key)
  # First, check if item is already cached in memory
  return true if @cache.key?(key)
  # Otherwise, it might be cached on disk
  # but we should not consider the disk cache if it is disabled
  return false unless disk_cache_enabled?

  path = path_to(hash(key))
  File.file?(path) && File.readable?(path)
end
```
