# Class: Jekyll::FrontmatterDefaults
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::FrontmatterDefaults

        show all
      

    Defined in:
    lib/jekyll/frontmatter_defaults.rb
  
## Overview

This class handles custom defaults for YAML frontmatter settings. These are set in _config.yml and apply both to internal use (e.g. layout) and the data available to liquid.

It is exposed via the frontmatter_defaults method on the site class.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**all**(path, type)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Collects a hash with all default values for a page or post.

-
  
      #**ensure_time!**(set)  ⇒ Object 

-
  
      #**find**(path, type, setting)  ⇒ Object 

Finds a default value for a given setting, filtered by path and type.

-
  
      #**initialize**(site)  ⇒ FrontmatterDefaults 

    constructor
  
  
  
  
  
  

  
    

Initializes a new instance.

-
  
      #**reset**  ⇒ Object 

-
  
      #**update_deprecated_types**(set)  ⇒ Object 

## Constructor Details

###
  
    #**initialize**(site)  ⇒ FrontmatterDefaults 
  

  

  

  
    

Initializes a new instance.

```

11
12
13
```

```
# File 'lib/jekyll/frontmatter_defaults.rb', line 11

def initialize(site)
  @site = site
end

```

## Instance Method Details

###
  
    #**all**(path, type)  ⇒ Object 
  

  

  

  
    

Collects a hash with all default values for a page or post

path - the relative path of the page or post type - a symbol indicating the type (:post, :page or :draft)

Returns a hash with all default values (an empty hash if there are none)

```

78
79
80
81
82
83
84
85
86
87
88
89
90
```

```
# File 'lib/jekyll/frontmatter_defaults.rb', line 78

def all(path, type)
  defaults = {}
  old_scope = nil
  matching_sets(path, type).each do |set|
    if has_precedence?(old_scope, set["scope"])
      defaults = Utils.deep_merge_hashes(defaults, set["values"])
      old_scope = set["scope"]
    else
      defaults = Utils.deep_merge_hashes(set["values"], defaults)
    end
  end
  defaults
end

```

###
  
    #**ensure_time!**(set)  ⇒ Object 
  

  

  

  
    
      

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
49
```

```
# File 'lib/jekyll/frontmatter_defaults.rb', line 40

def ensure_time!(set)
  return set unless set.key?("values") && set["values"].key?("date")
  return set if set["values"]["date"].is_a?(Time)

  set["values"]["date"] = Utils.parse_date(
    set["values"]["date"],
    "An invalid date format was found in a front-matter default set: #{set}"
  )
  set
end

```

###
  
    #**find**(path, type, setting)  ⇒ Object 
  

  

  

  
    

Finds a default value for a given setting, filtered by path and type

path - the path (relative to the source) of the page, post or :draft the default is used in type - a symbol indicating whether a :page, a :post or a :draft calls this method

Returns the default value or nil if none was found

```

59
60
61
62
63
64
65
66
67
68
69
70
```

```
# File 'lib/jekyll/frontmatter_defaults.rb', line 59

def find(path, type, setting)
  value = nil
  old_scope = nil

  matching_sets(path, type).each do |set|
    if set["values"].key?(setting) && has_precedence?(old_scope, set["scope"])
      value = set["values"][setting]
      old_scope = set["scope"]
    end
  end
  value
end

```

###
  
    #**reset**  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
```

```
# File 'lib/jekyll/frontmatter_defaults.rb', line 15

def reset
  @glob_cache = {} if @glob_cache
end

```

###
  
    #**update_deprecated_types**(set)  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
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
36
37
38
```

```
# File 'lib/jekyll/frontmatter_defaults.rb', line 19

def update_deprecated_types(set)
  return set unless set.key?("scope") && set["scope"].key?("type")

  set["scope"]["type"] =
    case set["scope"]["type"]
    when "page"
      Deprecator.defaults_deprecate_type("page", "pages")
      "pages"
    when "post"
      Deprecator.defaults_deprecate_type("post", "posts")
      "posts"
    when "draft"
      Deprecator.defaults_deprecate_type("draft", "drafts")
      "drafts"
    else
      set["scope"]["type"]
    end

  set
end

```
