# Class: Jekyll::Layout
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::Layout

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Convertible
  
    Defined in:
    lib/jekyll/layout.rb
  
## Instance Attribute Summary collapse

-
  
      #**content**  ⇒ Object 

content of layout.

-
  
      #**data**  ⇒ Object 

content of layout.

-
  
      #**ext**  ⇒ Object 

content of layout.

-
  
      #**name**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

name of layout.

-
  
      #**path**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

name of layout.

-
  
      #**relative_path**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

name of layout.

-
  
      #**site**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

name of layout.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(site, base, name)  ⇒ Layout 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize a new Layout.

-
  
      #**inspect**  ⇒ Object 

Returns the object as a debug String.

-
  
      #**process**(name)  ⇒ Object 

Extract information from the layout filename.

### Methods included from Convertible

# [], #asset_file?, #coffeescript_file?, #converters, #do_layout, #hook_owner, #invalid_layout?, #output_ext, #place_in_layout?, #published?, #read_yaml, #render_all_layouts, #render_liquid, #render_with_liquid?, #renderer, #sass_file?, #to_liquid, #to_s, #transform, #type, #validate_data!, #validate_permalink!, #write

## Constructor Details

###
  
    #**initialize**(site, base, name)  ⇒ Layout 
  

  

  

  
    

Initialize a new Layout.

site - The Site. base - The String path to the source. name - The String filename of the post file.

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
# File 'lib/jekyll/layout.rb', line 21

def initialize(site, base, name)
  @site = site
  @base = base
  @name = name

  if site.theme && site.theme.layouts_path.eql?(base)
    @base_dir = site.theme.root
    @path = site.in_theme_dir(base, name)
  else
    @base_dir = site.source
    @path = site.in_source_dir(base, name)
  end
  @relative_path = @path.sub(@base_dir, "")

  self.data = {}

  process(name)
  read_yaml(base, name)
end
```

## Instance Attribute Details

###
  
    #**content**  ⇒ Object 
  

  

  

  
    

content of layout

```

7
8
9
```

```
# File 'lib/jekyll/layout.rb', line 7

def content
  @content
end
```

###
  
    #**data**  ⇒ Object 
  

  

  

  
    

content of layout

```

7
8
9
```

```
# File 'lib/jekyll/layout.rb', line 7

def data
  @data
end
```

###
  
    #**ext**  ⇒ Object 
  

  

  

  
    

content of layout

```

7
8
9
```

```
# File 'lib/jekyll/layout.rb', line 7

def ext
  @ext
end
```

###
  
    #**name**  ⇒ Object  (readonly)
  

  

  

  
    

name of layout

```

11
12
13
```

```
# File 'lib/jekyll/layout.rb', line 11

def name
  @name
end
```

###
  
    #**path**  ⇒ Object  (readonly)
  

  

  

  
    

name of layout

```

11
12
13
```

```
# File 'lib/jekyll/layout.rb', line 11

def path
  @path
end
```

###
  
    #**relative_path**  ⇒ Object  (readonly)
  

  

  

  
    

name of layout

```

11
12
13
```

```
# File 'lib/jekyll/layout.rb', line 11

def relative_path
  @relative_path
end
```

###
  
    #**site**  ⇒ Object  (readonly)
  

  

  

  
    

name of layout

```

11
12
13
```

```
# File 'lib/jekyll/layout.rb', line 11

def site
  @site
end
```

## Instance Method Details

###
  
    #**inspect**  ⇒ Object 
  

  

  

  
    

Returns the object as a debug String.

```

51
52
53
```

```
# File 'lib/jekyll/layout.rb', line 51

def inspect
  "#<#{self.class} @path=#{@path.inspect}>"
end
```

###
  
    #**process**(name)  ⇒ Object 
  

  

  

  
    

Extract information from the layout filename.

name - The String filename of the layout file.

Returns nothing.

```

46
47
48
```

```
# File 'lib/jekyll/layout.rb', line 46

def process(name)
  self.ext = File.extname(name)
end
```
