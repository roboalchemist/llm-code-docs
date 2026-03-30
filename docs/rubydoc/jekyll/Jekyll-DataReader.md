# Class: Jekyll::DataReader
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::DataReader

        show all
      

    Defined in:
    lib/jekyll/readers/data_reader.rb
  
## Instance Attribute Summary collapse

-
  
      #**content**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute content.

-
  
      #**site**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute site.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(site, in_source_dir: nil)  ⇒ DataReader 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of DataReader.

-
  
      #**read**(dir)  ⇒ Object 

Read all the files in <dir> and adds them to @content.

-
  
      #**read_data_file**(path)  ⇒ Object 

Determines how to read a data file.

-
  
      #**read_data_to**(dir, data)  ⇒ Object 

Read and parse all .yaml, .yml, .json, .csv and .tsv files under <dir> and add them to the <data> variable.

-
  
      #**sanitize_filename**(name)  ⇒ Object 

## Constructor Details

###
  
    #**initialize**(site, in_source_dir: nil)  ⇒ DataReader 
  

  

  

  
    

Returns a new instance of DataReader.

```

7
8
9
10
11
12
13
```

```
# File 'lib/jekyll/readers/data_reader.rb', line 7

def initialize(site, in_source_dir: nil)
  @site = site
  @content = {}
  @entry_filter = EntryFilter.new(site)
  @in_source_dir = in_source_dir || @site.method(:in_source_dir)
  @source_dir = @in_source_dir.call("/")
end

```

## Instance Attribute Details

###
  
    #**content**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute content.

```

5
6
7
```

```
# File 'lib/jekyll/readers/data_reader.rb', line 5

def content
  @content
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
# File 'lib/jekyll/readers/data_reader.rb', line 5

def site
  @site
end

```

## Instance Method Details

###
  
    #**read**(dir)  ⇒ Object 
  

  

  

  
    

Read all the files in <dir> and adds them to @content

dir - The String relative path of the directory to read.

Returns @content, a Hash of the .yaml, .yml, .json, and .csv files in the base directory

```

21
22
23
24
25
```

```
# File 'lib/jekyll/readers/data_reader.rb', line 21

def read(dir)
  base = @in_source_dir.call(dir)
  read_data_to(base, @content)
  @content
end

```

###
  
    #**read_data_file**(path)  ⇒ Object 
  

  

  

  
    

Determines how to read a data file.

Returns the contents of the data file.

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
```

```
# File 'lib/jekyll/readers/data_reader.rb', line 57

def read_data_file(path)
  Jekyll.logger.debug "Reading:", path.sub(@source_dir, "")

  case File.extname(path).downcase
  when ".csv"
    CSV.read(path, **csv_config).map { |row| convert_row(row) }
  when ".tsv"
    CSV.read(path, **tsv_config).map { |row| convert_row(row) }
  else
    SafeYAML.load_file(path)
  end
end

```

###
  
    #**read_data_to**(dir, data)  ⇒ Object 
  

  

  

  
    

Read and parse all .yaml, .yml, .json, .csv and .tsv files under <dir> and add them to the <data> variable.

dir - The string absolute path of the directory to read. data - The variable to which data will be added.

Returns nothing

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
# File 'lib/jekyll/readers/data_reader.rb', line 34

def read_data_to(dir, data)
  return unless File.directory?(dir) && !@entry_filter.symlink?(dir)

  entries = Dir.chdir(dir) do
    Dir["*.{yaml,yml,json,csv,tsv}"] + Dir["*"].select { |fn| File.directory?(fn) }
  end

  entries.each do |entry|
    path = @in_source_dir.call(dir, entry)
    next if @entry_filter.symlink?(path)

    if File.directory?(path)
      read_data_to(path, data[sanitize_filename(entry)] = {})
    else
      key = sanitize_filename(File.basename(entry, ".*"))
      data[key] = read_data_file(path)
    end
  end
end

```

###
  
    #**sanitize_filename**(name)  ⇒ Object 
  

  

  

  
    
      

```

70
71
72
73
```

```
# File 'lib/jekyll/readers/data_reader.rb', line 70

def sanitize_filename(name)
  name.gsub(%r![^\w\s-]+|(?<=^|\b\s)\s+(?=$|\s?\b)!, "")
    .gsub(%r!\s+!, "_")
end

```
