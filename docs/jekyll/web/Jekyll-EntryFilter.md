# Class: Jekyll::EntryFilter
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::EntryFilter

        show all
      

    Defined in:
    lib/jekyll/entry_filter.rb
  
##

      Constant Summary
      collapse
    

    
      
        SPECIAL_LEADING_CHAR_REGEX =
          
        
        

```
%r!\A#{Regexp.union([".", "_", "#", "~"])}!o.freeze

```

## Instance Attribute Summary collapse

-
  
      #**site**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute site.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**backup?**(entry)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**base_directory**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**derive_base_directory**(site, base_dir)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**excluded?**(entry)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**filter**(entries)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**glob_include?**(enumerator, entry)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Check if an entry matches a specific pattern.

-
  
      #**included?**(entry)  ⇒ Boolean 

-
  
      #**initialize**(site, base_directory = nil)  ⇒ EntryFilter 

    constructor
  
  
  
  
  
  

  
    

A new instance of EntryFilter.

-
  
      #**relative_to_source**(entry)  ⇒ Object 

-
  
      #**special?**(entry)  ⇒ Boolean 

-
  
      #**symlink?**(entry)  ⇒ Boolean 

– Check if a file is a symlink.

-
  
      #**symlink_outside_site_source?**(entry)  ⇒ Boolean 

– Check if given path is outside of current site’s configured source directory.

## Constructor Details

###
  
    #**initialize**(site, base_directory = nil)  ⇒ EntryFilter 
  

  

  

  
    

Returns a new instance of EntryFilter.

```

9
10
11
12
13
14
```

```
# File 'lib/jekyll/entry_filter.rb', line 9

def initialize(site, base_directory = nil)
  @site = site
  @base_directory = derive_base_directory(
    @site, base_directory.to_s.dup
  )
end

```

## Instance Attribute Details

###
  
    #**site**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute site.

```

5
6
7
```

```
# File 'lib/jekyll/entry_filter.rb', line 5

def site
  @site
end

```

## Instance Method Details

###
  
    #**backup?**(entry)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

64
65
66
```

```
# File 'lib/jekyll/entry_filter.rb', line 64

def backup?(entry)
  entry.end_with?("~")
end

```

###
  
    #**base_directory**  ⇒ Object 
  

  

  

  
    
      

```

16
17
18
```

```
# File 'lib/jekyll/entry_filter.rb', line 16

def base_directory
  @base_directory.to_s
end

```

###
  
    #**derive_base_directory**(site, base_dir)  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
23
```

```
# File 'lib/jekyll/entry_filter.rb', line 20

def derive_base_directory(site, base_dir)
  base_dir[site.source] = "" if base_dir.start_with?(site.source)
  base_dir
end

```

###
  
    #**excluded?**(entry)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

68
69
70
71
72
73
74
75
76
77
```

```
# File 'lib/jekyll/entry_filter.rb', line 68

def excluded?(entry)
  glob_include?(site.exclude - site.include, relative_to_source(entry)).tap do |excluded|
    if excluded
      Jekyll.logger.debug(
        "EntryFilter:",
        "excluded #{relative_to_source(entry)}"
      )
    end
  end
end

```

###
  
    #**filter**(entries)  ⇒ Object 
  

  

  

  
    
      

```

31
32
33
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
44
45
46
47
48
49
50
51
52
```

```
# File 'lib/jekyll/entry_filter.rb', line 31

def filter(entries)
  entries.reject do |e|
    # Reject this entry if it is just a "dot" representation.
    #   e.g.: '.', '..', '_movies/.', 'music/..', etc
    next true if e.end_with?(".")

    # Check if the current entry is explicitly included and cache the result
    included = included?(e)

    # Reject current entry if it is excluded but not explicitly included as well.
    next true if excluded?(e) && !included

    # Reject current entry if it is a symlink.
    next true if symlink?(e)

    # Do not reject current entry if it is explicitly included.
    next false if included

    # Reject current entry if it is special or a backup file.
    special?(e) || backup?(e)
  end
end

```

###
  
    #**glob_include?**(enumerator, entry)  ⇒ Boolean 
  

  

  

  
    

Check if an entry matches a specific pattern. Returns true if path matches against any glob pattern, else false.

Returns:

-

        (Boolean)

```

97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
```

```
# File 'lib/jekyll/entry_filter.rb', line 97

def glob_include?(enumerator, entry)
  entry_with_source = PathManager.join(site.source, entry)
  entry_is_directory = File.directory?(entry_with_source)

  enumerator.any? do |pattern|
    case pattern
    when String
      pattern_with_source = PathManager.join(site.source, pattern)

      File.fnmatch?(pattern_with_source, entry_with_source) ||
        entry_with_source.start_with?(pattern_with_source) ||
        (pattern_with_source == "#{entry_with_source}/" if entry_is_directory)
    when Regexp
      pattern.match?(entry_with_source)
    else
      false
    end
  end
end

```

###
  
    #**included?**(entry)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

54
55
56
57
```

```
# File 'lib/jekyll/entry_filter.rb', line 54

def included?(entry)
  glob_include?(site.include, entry) ||
    glob_include?(site.include, File.basename(entry))
end

```

###
  
    #**relative_to_source**(entry)  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
28
29
```

```
# File 'lib/jekyll/entry_filter.rb', line 25

def relative_to_source(entry)
  File.join(
    base_directory, entry
  )
end

```

###
  
    #**special?**(entry)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

59
60
61
62
```

```
# File 'lib/jekyll/entry_filter.rb', line 59

def special?(entry)
  SPECIAL_LEADING_CHAR_REGEX.match?(entry) ||
    SPECIAL_LEADING_CHAR_REGEX.match?(File.basename(entry))
end

```

###
  
    #**symlink?**(entry)  ⇒ Boolean 
  

  

  

  
    

– Check if a file is a symlink. NOTE: This can be converted to allowing even in safe,

```
since we use Pathutil#in_path? now.

```

–

Returns:

-

        (Boolean)

```

84
85
86
```

```
# File 'lib/jekyll/entry_filter.rb', line 84

def symlink?(entry)
  site.safe && File.symlink?(entry) && symlink_outside_site_source?(entry)
end

```

###
  
    #**symlink_outside_site_source?**(entry)  ⇒ Boolean 
  

  

  

  
    

– Check if given path is outside of current site’s configured source directory. –

Returns:

-

        (Boolean)

```

91
92
93
```

```
# File 'lib/jekyll/entry_filter.rb', line 91

def symlink_outside_site_source?(entry)
  !File.realpath(entry).start_with?(site.in_source_dir)
end

```
