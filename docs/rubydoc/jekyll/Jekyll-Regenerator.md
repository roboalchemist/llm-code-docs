# Class: Jekyll::Regenerator
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::Regenerator

        show all
      

    Defined in:
    lib/jekyll/regenerator.rb
  
## Instance Attribute Summary collapse

-
  
      #**cache**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute cache.

-
  
      #**metadata**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute metadata.

-
  
      #**site**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute site.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**add**(path)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Add a path to the metadata.

-
  
      #**add_dependency**(path, dependency)  ⇒ Object 

Add a dependency of a path.

-
  
      #**clear**  ⇒ Object 

Clear the metadata and cache.

-
  
      #**clear_cache**  ⇒ Object 

Clear just the cache.

-
  
      #**disabled?**  ⇒ Boolean 

Check if metadata has been disabled.

-
  
      #**force**(path)  ⇒ Object 

Force a path to regenerate.

-
  
      #**initialize**(site)  ⇒ Regenerator 

    constructor
  
  
  
  
  
  

  
    

A new instance of Regenerator.

-
  
      #**metadata_file**  ⇒ Object 

Produce the absolute path of the metadata file.

-
  
      #**modified?**(path)  ⇒ Boolean 

Checks if a path’s (or one of its dependencies) mtime has changed.

-
  
      #**regenerate?**(document)  ⇒ Boolean 

Checks if a renderable object needs to be regenerated.

-
  
      #**source_modified_or_dest_missing?**(source_path, dest_path)  ⇒ Boolean 

Checks if the source has been modified or the destination is missing.

-
  
      #**write_metadata**  ⇒ Object 

Write the metadata to disk.

## Constructor Details

###
  
    #**initialize**(site)  ⇒ Regenerator 
  

  

  

  
    

Returns a new instance of Regenerator.

```

9
10
11
12
13
14
15
16
17
```

```
# File 'lib/jekyll/regenerator.rb', line 9

def initialize(site)
  @site = site

  # Read metadata from file
  read_metadata

  # Initialize cache to an empty hash
  clear_cache
end
```

## Instance Attribute Details

###
  
    #**cache**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute cache.

```

5
6
7
```

```
# File 'lib/jekyll/regenerator.rb', line 5

def cache
  @cache
end
```

###
  
    #**metadata**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute metadata.

```

5
6
7
```

```
# File 'lib/jekyll/regenerator.rb', line 5

def metadata
  @metadata
end
```

###
  
    #**site**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute site.

```

5
6
7
```

```
# File 'lib/jekyll/regenerator.rb', line 5

def site
  @site
end
```

## Instance Method Details

###
  
    #**add**(path)  ⇒ Object 
  

  

  

  
    

Add a path to the metadata

Returns true, also on failure.

```

40
41
42
43
44
45
46
47
48
```

```
# File 'lib/jekyll/regenerator.rb', line 40

def add(path)
  return true unless File.exist?(path)

  metadata[path] = {
    "mtime" => File.mtime(path),
    "deps"  => [],
  }
  cache[path] = true
end
```

###
  
    #**add_dependency**(path, dependency)  ⇒ Object 
  

  

  

  
    

Add a dependency of a path

Returns nothing.

```

106
107
108
109
110
111
112
113
114
```

```
# File 'lib/jekyll/regenerator.rb', line 106

def add_dependency(path, dependency)
  return if metadata[path].nil? || disabled

  unless metadata[path]["deps"].include? dependency
    metadata[path]["deps"] << dependency
    add(dependency) unless metadata.include?(dependency)
  end
  regenerate? dependency
end
```

###
  
    #**clear**  ⇒ Object 
  

  

  

  
    

Clear the metadata and cache

Returns nothing

```

60
61
62
63
```

```
# File 'lib/jekyll/regenerator.rb', line 60

def clear
  @metadata = {}
  clear_cache
end
```

###
  
    #**clear_cache**  ⇒ Object 
  

  

  

  
    

Clear just the cache

Returns nothing

```

68
69
70
```

```
# File 'lib/jekyll/regenerator.rb', line 68

def clear_cache
  @cache = {}
end
```

###
  
    #**disabled?**  ⇒ Boolean 
  

  

  

  
    

Check if metadata has been disabled

Returns a Boolean (true for disabled, false for enabled).

Returns:

-

        (Boolean)

```

136
137
138
139
```

```
# File 'lib/jekyll/regenerator.rb', line 136

def disabled?
  self.disabled = !site.incremental? if disabled.nil?
  disabled
end
```

###
  
    #**force**(path)  ⇒ Object 
  

  

  

  
    

Force a path to regenerate

Returns true.

```

53
54
55
```

```
# File 'lib/jekyll/regenerator.rb', line 53

def force(path)
  cache[path] = true
end
```

###
  
    #**metadata_file**  ⇒ Object 
  

  

  

  
    

Produce the absolute path of the metadata file

Returns the String path of the file.

```

129
130
131
```

```
# File 'lib/jekyll/regenerator.rb', line 129

def metadata_file
  @metadata_file ||= site.in_source_dir(".jekyll-metadata")
end
```

###
  
    #**modified?**(path)  ⇒ Boolean 
  

  

  

  
    

Checks if a path’s (or one of its dependencies) mtime has changed

Returns a boolean.

Returns:

-

        (Boolean)

```

84
85
86
87
88
89
90
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
101
```

```
# File 'lib/jekyll/regenerator.rb', line 84

def modified?(path)
  return true if disabled?

  # objects that don't have a path are always regenerated
  return true if path.nil?

  # Check for path in cache
  return cache[path] if cache.key? path

  if metadata[path]
    # If we have seen this file before,
    # check if it or one of its dependencies has been modified
    existing_file_modified?(path)
  else
    # If we have not seen this file before, add it to the metadata and regenerate it
    add(path)
  end
end
```

###
  
    #**regenerate?**(document)  ⇒ Boolean 
  

  

  

  
    

Checks if a renderable object needs to be regenerated

Returns a boolean.

Returns:

-

        (Boolean)

```

22
23
24
25
26
27
28
29
30
31
32
33
34
35
```

```
# File 'lib/jekyll/regenerator.rb', line 22

def regenerate?(document)
  return true if disabled

  case document
  when Page
    regenerate_page?(document)
  when Document
    regenerate_document?(document)
  else
    source_path = document.respond_to?(:path) ? document.path : nil
    dest_path = document.destination(@site.dest) if document.respond_to?(:destination)
    source_modified_or_dest_missing?(source_path, dest_path)
  end
end
```

###
  
    #**source_modified_or_dest_missing?**(source_path, dest_path)  ⇒ Boolean 
  

  

  

  
    

Checks if the source has been modified or the destination is missing

returns a boolean

Returns:

-

        (Boolean)

```

76
77
78
```

```
# File 'lib/jekyll/regenerator.rb', line 76

def source_modified_or_dest_missing?(source_path, dest_path)
  modified?(source_path) || (dest_path && !File.exist?(dest_path))
end
```

###
  
    #**write_metadata**  ⇒ Object 
  

  

  

  
    

Write the metadata to disk

Returns nothing.

```

119
120
121
122
123
124
```

```
# File 'lib/jekyll/regenerator.rb', line 119

def write_metadata
  unless disabled?
    Jekyll.logger.debug "Writing Metadata:", ".jekyll-metadata"
    File.binwrite(metadata_file, Marshal.dump(metadata))
  end
end
```
