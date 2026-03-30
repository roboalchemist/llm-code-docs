# Class: Jekyll::Reader
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::Reader

        show all
      

    Defined in:
    lib/jekyll/reader.rb
  
## Instance Attribute Summary collapse

-
  
      #**site**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute site.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**filter_entries**(entries, base_directory = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Filter out any files/directories that are hidden or backup files (start with “.” or “#” or end with “~”), or contain site content (start with “_”), or are excluded in the site configuration, unless they are web server files such as ‘.htaccess’.

-
  
      #**get_entries**(dir, subfolder)  ⇒ Object 

Read the entries from a particular directory for processing.

-
  
      #**initialize**(site)  ⇒ Reader 

    constructor
  
  
  
  
  
  

  
    

A new instance of Reader.

-
  
      #**read**  ⇒ Object 

Read Site data from disk and load it into internal data structures.

-
  
      #**read_data**  ⇒ Object 

Read and merge the data files.

-
  
      #**read_directories**(dir = "")  ⇒ Object 

Recursively traverse directories to find pages and static files that will become part of the site according to the rules in filter_entries.

-
  
      #**retrieve_dirs**(_base, dir, dot_dirs)  ⇒ Object 

Recursively traverse directories with the read_directories function.

-
  
      #**retrieve_pages**(dir, dot_pages)  ⇒ Object 

Retrieve all the pages from the current directory, add them to the site and sort them.

-
  
      #**retrieve_posts**(dir)  ⇒ Object 

Retrieves all the posts(posts/drafts) from the given directory and add them to the site and sort them.

-
  
      #**retrieve_static_files**(dir, dot_static_files)  ⇒ Object 

Retrieve all the static files from the current directory, add them to the site and sort them.

-
  
      #**sort_files!**  ⇒ Object 

Sorts posts, pages, and static files.

## Constructor Details

###
  
    #**initialize**(site)  ⇒ Reader 
  

  

  

  
    

Returns a new instance of Reader.

```

7
8
9
```

```
# File 'lib/jekyll/reader.rb', line 7

def initialize(site)
  @site = site
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
# File 'lib/jekyll/reader.rb', line 5

def site
  @site
end

```

## Instance Method Details

###
  
    #**filter_entries**(entries, base_directory = nil)  ⇒ Object 
  

  

  

  
    

Filter out any files/directories that are hidden or backup files (start with “.” or “#” or end with “~”), or contain site content (start with “_”), or are excluded in the site configuration, unless they are web server files such as ‘.htaccess’.

entries - The Array of String file/directory entries to filter. base_directory - The string representing the optional base directory.

Returns the Array of filtered entries.

```

141
142
143
```

```
# File 'lib/jekyll/reader.rb', line 141

def filter_entries(entries, base_directory = nil)
  EntryFilter.new(site, base_directory).filter(entries)
end

```

###
  
    #**get_entries**(dir, subfolder)  ⇒ Object 
  

  

  

  
    

Read the entries from a particular directory for processing

dir - The String representing the relative path of the directory to read. subfolder - The String representing the directory to read.

Returns the list of entries to process

```

151
152
153
154
155
156
157
```

```
# File 'lib/jekyll/reader.rb', line 151

def get_entries(dir, subfolder)
  base = site.in_source_dir(dir, subfolder)
  return [] unless File.exist?(base)

  entries = Dir.chdir(base) { filter_entries(Dir["**/*"], base) }
  entries.delete_if { |e| File.directory?(site.in_source_dir(base, e)) }
end

```

###
  
    #**read**  ⇒ Object 
  

  

  

  
    

Read Site data from disk and load it into internal data structures.

Returns nothing.

```

14
15
16
17
18
19
20
21
22
```

```
# File 'lib/jekyll/reader.rb', line 14

def read
  @site.layouts = LayoutReader.new(site).read
  read_directories
  read_included_excludes
  sort_files!
  CollectionReader.new(site).read
  ThemeAssetsReader.new(site).read
  read_data
end

```

###
  
    #**read_data**  ⇒ Object 
  

  

  

  
    

Read and merge the data files. If a theme is specified and it contains data, it will be read. Site data will overwrite theme data with the same key using the semantics of Utils.deep_merge_hashes.

Returns nothing.

```

30
31
32
33
34
35
36
37
38
39
```

```
# File 'lib/jekyll/reader.rb', line 30

def read_data
  @site.data = DataReader.new(site).read(site.config["data_dir"])
  return unless site.theme&.data_path

  theme_data = DataReader.new(
    site,
    :in_source_dir => site.method(:in_theme_dir)
  ).read(site.theme.data_path)
  @site.data = Jekyll::Utils.deep_merge_hashes(theme_data, @site.data)
end

```

###
  
    #**read_directories**(dir = "")  ⇒ Object 
  

  

  

  
    

Recursively traverse directories to find pages and static files that will become part of the site according to the rules in filter_entries.

dir - The String relative path of the directory to read. Default: ”.

Returns nothing.

```

55
56
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
71
72
73
74
75
76
77
78
79
80
```

```
# File 'lib/jekyll/reader.rb', line 55

def read_directories(dir = "")
  base = site.in_source_dir(dir)

  return unless File.directory?(base)

  dot_dirs = []
  dot_pages = []
  dot_static_files = []

  dot = Dir.chdir(base) { filter_entries(Dir.entries("."), base) }
  dot.each do |entry|
    file_path = @site.in_source_dir(base, entry)
    if File.directory?(file_path)
      dot_dirs << entry
    elsif Utils.has_yaml_header?(file_path)
      dot_pages << entry
    else
      dot_static_files << entry
    end
  end

  retrieve_posts(dir)
  retrieve_dirs(base, dir, dot_dirs)
  retrieve_pages(dir, dot_pages)
  retrieve_static_files(dir, dot_static_files)
end

```

###
  
    #**retrieve_dirs**(_base, dir, dot_dirs)  ⇒ Object 
  

  

  

  
    

Recursively traverse directories with the read_directories function.

base - The String representing the site’s base directory. dir - The String representing the directory to traverse down. dot_dirs - The Array of subdirectories in the dir.

Returns nothing.

```

102
103
104
105
106
107
108
```

```
# File 'lib/jekyll/reader.rb', line 102

def retrieve_dirs(_base, dir, dot_dirs)
  dot_dirs.each do |file|
    dir_path = site.in_source_dir(dir, file)
    rel_path = PathManager.join(dir, file)
    @site.reader.read_directories(rel_path) unless @site.dest.chomp("/") == dir_path
  end
end

```

###
  
    #**retrieve_pages**(dir, dot_pages)  ⇒ Object 
  

  

  

  
    

Retrieve all the pages from the current directory, add them to the site and sort them.

dir - The String representing the directory retrieve the pages from. dot_pages - The Array of pages in the dir.

Returns nothing.

```

117
118
119
```

```
# File 'lib/jekyll/reader.rb', line 117

def retrieve_pages(dir, dot_pages)
  site.pages.concat(PageReader.new(site, dir).read(dot_pages))
end

```

###
  
    #**retrieve_posts**(dir)  ⇒ Object 
  

  

  

  
    

Retrieves all the posts(posts/drafts) from the given directory and add them to the site and sort them.

dir - The String representing the directory to retrieve the posts from.

Returns nothing.

```

88
89
90
91
92
93
```

```
# File 'lib/jekyll/reader.rb', line 88

def retrieve_posts(dir)
  return if outside_configured_directory?(dir)

  site.posts.docs.concat(post_reader.read_posts(dir))
  site.posts.docs.concat(post_reader.read_drafts(dir)) if site.show_drafts
end

```

###
  
    #**retrieve_static_files**(dir, dot_static_files)  ⇒ Object 
  

  

  

  
    

Retrieve all the static files from the current directory, add them to the site and sort them.

dir - The directory retrieve the static files from. dot_static_files - The static files in the dir.

Returns nothing.

```

128
129
130
```

```
# File 'lib/jekyll/reader.rb', line 128

def retrieve_static_files(dir, dot_static_files)
  site.static_files.concat(StaticFileReader.new(site, dir).read(dot_static_files))
end

```

###
  
    #**sort_files!**  ⇒ Object 
  

  

  

  
    

Sorts posts, pages, and static files.

```

42
43
44
45
46
```

```
# File 'lib/jekyll/reader.rb', line 42

def sort_files!
  site.collections.each_value { |c| c.docs.sort! }
  site.pages.sort_by!(&:name)
  site.static_files.sort_by!(&:relative_path)
end

```
