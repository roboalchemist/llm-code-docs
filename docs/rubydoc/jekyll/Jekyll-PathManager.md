# Class: Jekyll::PathManager
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::PathManager

        show all
      

    Defined in:
    lib/jekyll/path_manager.rb
  
## Overview

A singleton class that caches frozen instances of path strings returned from its methods.

NOTE:

```
This class exists because `File.join` allocates an Array and returns a new String on every
call using **the same arguments**. Caching the result means reduced memory usage.
However, the caches are never flushed so that they can be used even when a site is
regenerating. The results are frozen to deter mutation of the cached string.

Therefore, employ this class only for situations where caching the result is necessary
for performance reasons.

```

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**join**(base, item)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Wraps `File.join` to cache the frozen result.

-
  
      .**sanitized_path**(base_directory, questionable_path)  ⇒ Object 

Ensures the questionable path is prefixed with the base directory and prepends the questionable path with the base directory if false.

## Class Method Details

###
  
    .**join**(base, item)  ⇒ Object 
  

  

  

  
    

Wraps `File.join` to cache the frozen result. Reassigns `nil`, empty strings and empty arrays to a frozen empty string beforehand.

Returns a frozen string.

```

24
25
26
27
28
29
30
```

```
# File 'lib/jekyll/path_manager.rb', line 24

def join(base, item)
  base = "" if base.nil? || base.empty?
  item = "" if item.nil? || item.empty?
  @join ||= {}
  @join[base] ||= {}
  @join[base][item] ||= File.join(base, item).freeze
end

```

###
  
    .**sanitized_path**(base_directory, questionable_path)  ⇒ Object 
  

  

  

  
    

Ensures the questionable path is prefixed with the base directory and prepends the questionable path with the base directory if false.

Returns a frozen string.

```

36
37
38
39
40
41
42
43
44
45
46
```

```
# File 'lib/jekyll/path_manager.rb', line 36

def sanitized_path(base_directory, questionable_path)
  @sanitized_path ||= {}
  @sanitized_path[base_directory] ||= {}
  @sanitized_path[base_directory][questionable_path] ||= if questionable_path.nil?
                                                           base_directory.freeze
                                                         else
                                                           sanitize_and_join(
                                                             base_directory, questionable_path
                                                           ).freeze
                                                         end
end

```
