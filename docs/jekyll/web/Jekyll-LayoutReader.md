# Class: Jekyll::LayoutReader
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::LayoutReader

        show all
      

    Defined in:
    lib/jekyll/readers/layout_reader.rb
  
## Instance Attribute Summary collapse

-
  
      #**site**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute site.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(site)  ⇒ LayoutReader 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of LayoutReader.

-
  
      #**layout_directory**  ⇒ Object 

-
  
      #**read**  ⇒ Object 

-
  
      #**theme_layout_directory**  ⇒ Object 

## Constructor Details

###
  
    #**initialize**(site)  ⇒ LayoutReader 
  

  

  

  
    

Returns a new instance of LayoutReader.

```

7
8
9
10
```

```
# File 'lib/jekyll/readers/layout_reader.rb', line 7

def initialize(site)
  @site = site
  @layouts = {}
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
# File 'lib/jekyll/readers/layout_reader.rb', line 5

def site
  @site
end

```

## Instance Method Details

###
  
    #**layout_directory**  ⇒ Object 
  

  

  

  
    
      

```

26
27
28
```

```
# File 'lib/jekyll/readers/layout_reader.rb', line 26

def layout_directory
  @layout_directory ||= site.in_source_dir(site.config["layouts_dir"])
end

```

###
  
    #**read**  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
15
16
17
18
19
20
21
22
23
24
```

```
# File 'lib/jekyll/readers/layout_reader.rb', line 12

def read
  layout_entries.each do |layout_file|
    @layouts[layout_name(layout_file)] = \
      Layout.new(site, layout_directory, layout_file)
  end

  theme_layout_entries.each do |layout_file|
    @layouts[layout_name(layout_file)] ||= \
      Layout.new(site, theme_layout_directory, layout_file)
  end

  @layouts
end

```

###
  
    #**theme_layout_directory**  ⇒ Object 
  

  

  

  
    
      

```

30
31
32
```

```
# File 'lib/jekyll/readers/layout_reader.rb', line 30

def theme_layout_directory
  @theme_layout_directory ||= site.theme.layouts_path if site.theme
end

```
