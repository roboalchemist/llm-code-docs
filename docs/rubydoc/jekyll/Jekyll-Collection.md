# Class: Jekyll::Collection
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::Collection

        show all
      

    Defined in:
    lib/jekyll/collection.rb
  
## Instance Attribute Summary collapse

-
  
      #**docs**  ⇒ Object 

Fetch the Documents in this collection.

-
  
      #**label**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute label.

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
  
      #**collection_dir**(*files)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The full path to the directory containing the collection, with   optional subpaths.

-
  
      #**directory**  ⇒ Object 

The full path to the directory containing the collection.

-
  
      #**entries**  ⇒ Object 

All the entries in this collection.

-
  
      #**entry_filter**  ⇒ Object 

The entry filter for this collection.

-
  
      #**exists?**  ⇒ Boolean 

Checks whether the directory “exists” for this collection.

-
  
      #**extract_metadata**  ⇒ Object 

Extract options for this collection from the site configuration.

-
  
      #**files**  ⇒ Object 

Fetch the static files in this collection.

-
  
      #**filtered_entries**  ⇒ Object 

Filtered version of the entries in this collection.

-
  
      #**initialize**(site, label)  ⇒ Collection 

    constructor
  
  
  
  
  
  

  
    

Create a new Collection.

-
  
      #**inspect**  ⇒ Object 

An inspect string.

-
  
      #**method_missing**(method, *args, &blck)  ⇒ Object 

Override of method_missing to check in @data for the key.

-
  
      #**read**  ⇒ Object 

Read the allowed documents into the collection’s array of docs.

-
  
      #**relative_directory**  ⇒ Object 

The directory for this Collection, relative to the site source or the directory containing the collection.

-
  
      #**respond_to_missing?**(method, include_private = false)  ⇒ Boolean 

Override of normal respond_to? to match method_missing’s logic for looking in @data.

-
  
      #**sanitize_label**(label)  ⇒ Object 

Produce a sanitized label name Label names may not contain anything but alphanumeric characters,   underscores, and hyphens.

-
  
      #**to_liquid**  ⇒ Object 

Produce a representation of this Collection for use in Liquid.

-
  
      #**url_template**  ⇒ Object 

The URL template to render collection’s documents at.

-
  
      #**write?**  ⇒ Boolean 

Whether the collection’s documents ought to be written as individual   files in the output.

## Constructor Details

###
  
    #**initialize**(site, label)  ⇒ Collection 
  

  

  

  
    

Create a new Collection.

site - the site to which this collection belongs. label - the name of the collection

Returns nothing.

```

14
15
16
17
18
```

```
# File 'lib/jekyll/collection.rb', line 14

def initialize(site, label)
  @site     = site
  @label    = sanitize_label(label)
  @metadata = extract_metadata
end

```

## Dynamic Method Handling

    This class handles dynamic methods through the method_missing method
    
  
  
    
  
###
  
    #**method_missing**(method, *args, &blck)  ⇒ Object 
  

  

  

  
    

Override of method_missing to check in @data for the key.

```

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
```

```
# File 'lib/jekyll/collection.rb', line 35

def method_missing(method, *args, &blck)
  if docs.respond_to?(method.to_sym)
    Jekyll.logger.warn "Deprecation:",
                       "#{label}.#{method} should be changed to #{label}.docs.#{method}."
    Jekyll.logger.warn "", "Called by #{caller(0..0)}."
    docs.public_send(method.to_sym, *args, &blck)
  else
    super
  end
end

```

## Instance Attribute Details

###
  
    #**docs**  ⇒ Object 
  

  

  

  
    

Fetch the Documents in this collection. Defaults to an empty array if no documents have been read in.

Returns an array of Jekyll::Document objects.

```

24
25
26
```

```
# File 'lib/jekyll/collection.rb', line 24

def docs
  @docs ||= []
end

```

###
  
    #**label**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute label.

```

5
6
7
```

```
# File 'lib/jekyll/collection.rb', line 5

def label
  @label
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
# File 'lib/jekyll/collection.rb', line 5

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
# File 'lib/jekyll/collection.rb', line 5

def site
  @site
end

```

## Instance Method Details

###
  
    #**collection_dir**(*files)  ⇒ Object 
  

  

  

  
    

The full path to the directory containing the collection, with

```
optional subpaths.

```

*files - (optional) any other path pieces relative to the

```
directory to append to the path

```

Returns a String containing th directory name where the collection

```
is stored on the filesystem.

```

```

131
132
133
134
135
```

```
# File 'lib/jekyll/collection.rb', line 131

def collection_dir(*files)
  return directory if files.empty?

  site.in_source_dir(container, relative_directory, *files)
end

```

###
  
    #**directory**  ⇒ Object 
  

  

  

  
    

The full path to the directory containing the collection.

Returns a String containing th directory name where the collection

```
is stored on the filesystem.

```

```

117
118
119
120
121
```

```
# File 'lib/jekyll/collection.rb', line 117

def directory
  @directory ||= site.in_source_dir(
    File.join(container, relative_directory)
  )
end

```

###
  
    #**entries**  ⇒ Object 
  

  

  

  
    

All the entries in this collection.

Returns an Array of file paths to the documents in this collection

```
relative to the collection's directory

```

```

76
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
# File 'lib/jekyll/collection.rb', line 76

def entries
  return [] unless exists?

  @entries ||= begin
    collection_dir_slash = "#{collection_dir}/"
    Utils.safe_glob(collection_dir, ["**", "*"], File::FNM_DOTMATCH).map do |entry|
      entry[collection_dir_slash] = ""
      entry
    end
  end
end

```

###
  
    #**entry_filter**  ⇒ Object 
  

  

  

  
    

The entry filter for this collection. Creates an instance of Jekyll::EntryFilter.

Returns the instance of Jekyll::EntryFilter for this collection.

```

151
152
153
```

```
# File 'lib/jekyll/collection.rb', line 151

def entry_filter
  @entry_filter ||= Jekyll::EntryFilter.new(site, relative_directory)
end

```

###
  
    #**exists?**  ⇒ Boolean 
  

  

  

  
    

Checks whether the directory “exists” for this collection. The directory must exist on the filesystem and must not be a symlink

```
if in safe mode.

```

Returns false if the directory doesn’t exist or if it’s a symlink

```
and we're in safe mode.

```

Returns:

-

        (Boolean)

```

143
144
145
```

```
# File 'lib/jekyll/collection.rb', line 143

def exists?
  File.directory?(directory) && !entry_filter.symlink?(directory)
end

```

###
  
    #**extract_metadata**  ⇒ Object 
  

  

  

  
    

Extract options for this collection from the site configuration.

Returns the metadata for this collection

```

203
204
205
206
207
208
209
```

```
# File 'lib/jekyll/collection.rb', line 203

def extract_metadata
  if site.config["collections"].is_a?(Hash)
    site.config["collections"][label] || {}
  else
    {}
  end
end

```

###
  
    #**files**  ⇒ Object 
  

  

  

  
    

Fetch the static files in this collection. Defaults to an empty array if no static files have been read in.

Returns an array of Jekyll::StaticFile objects.

```

50
51
52
```

```
# File 'lib/jekyll/collection.rb', line 50

def files
  @files ||= []
end

```

###
  
    #**filtered_entries**  ⇒ Object 
  

  

  

  
    

Filtered version of the entries in this collection. See ‘Jekyll::EntryFilter#filter` for more information.

Returns a list of filtered entry paths.

```

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
102
```

```
# File 'lib/jekyll/collection.rb', line 92

def filtered_entries
  return [] unless exists?

  @filtered_entries ||=
    Dir.chdir(directory) do
      entry_filter.filter(entries).reject do |f|
        path = collection_dir(f)
        File.directory?(path) || entry_filter.symlink?(f)
      end
    end
end

```

###
  
    #**inspect**  ⇒ Object 
  

  

  

  
    

An inspect string.

Returns the inspect string

```

158
159
160
```

```
# File 'lib/jekyll/collection.rb', line 158

def inspect
  "#<#{self.class} @label=#{label} docs=#{docs}>"
end

```

###
  
    #**read**  ⇒ Object 
  

  

  

  
    

Read the allowed documents into the collection’s array of docs.

Returns the sorted array of docs.

```

57
58
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
# File 'lib/jekyll/collection.rb', line 57

def read
  filtered_entries.each do |file_path|
    full_path = collection_dir(file_path)
    next if File.directory?(full_path)

    if Utils.has_yaml_header? full_path
      read_document(full_path)
    else
      read_static_file(file_path, full_path)
    end
  end
  site.static_files.concat(files) unless files.empty?
  sort_docs!
end

```

###
  
    #**relative_directory**  ⇒ Object 
  

  

  

  
    

The directory for this Collection, relative to the site source or the directory containing the collection.

Returns a String containing the directory name where the collection

```
is stored on the filesystem.

```

```

109
110
111
```

```
# File 'lib/jekyll/collection.rb', line 109

def relative_directory
  @relative_directory ||= "_#{label}"
end

```

###
  
    #**respond_to_missing?**(method, include_private = false)  ⇒ Boolean 
  

  

  

  
    

Override of normal respond_to? to match method_missing’s logic for looking in @data.

Returns:

-

        (Boolean)

```

30
31
32
```

```
# File 'lib/jekyll/collection.rb', line 30

def respond_to_missing?(method, include_private = false)
  docs.respond_to?(method.to_sym, include_private) || super
end

```

###
  
    #**sanitize_label**(label)  ⇒ Object 
  

  

  

  
    

Produce a sanitized label name Label names may not contain anything but alphanumeric characters,

```
underscores, and hyphens.

```

label - the possibly-unsafe label

Returns a sanitized version of the label.

```

169
170
171
```

```
# File 'lib/jekyll/collection.rb', line 169

def sanitize_label(label)
  label.gsub(%r![^a-z0-9_\-.]!i, "")
end

```

###
  
    #**to_liquid**  ⇒ Object 
  

  

  

  
    

Produce a representation of this Collection for use in Liquid. Exposes two attributes:

```
- label
- docs

```

Returns a representation of this collection for use in Liquid.

```

179
180
181
```

```
# File 'lib/jekyll/collection.rb', line 179

def to_liquid
  Drops::CollectionDrop.new self
end

```

###
  
    #**url_template**  ⇒ Object 
  

  

  

  
    

The URL template to render collection’s documents at.

Returns the URL template to render collection’s documents at.

```

194
195
196
197
198
```

```
# File 'lib/jekyll/collection.rb', line 194

def url_template
  @url_template ||= metadata.fetch("permalink") do
    Utils.add_permalink_suffix("/:collection/:path", site.permalink_style)
  end
end

```

###
  
    #**write?**  ⇒ Boolean 
  

  

  

  
    

Whether the collection’s documents ought to be written as individual

```
files in the output.

```

Returns true if the ‘write’ metadata is true, false otherwise.

Returns:

-

        (Boolean)

```

187
188
189
```

```
# File 'lib/jekyll/collection.rb', line 187

def write?
  !!metadata.fetch("output", false)
end

```
