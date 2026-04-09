# Class: Jekyll::Tags::Link
  
    Inherits:
    
      Liquid::Tag
      
        

          
- Object

- Liquid::Tag

- Jekyll::Tags::Link

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Filters::URLFilters
  
    Defined in:
    lib/jekyll/tags/link.rb
  
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**tag_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(tag_name, relative_path, tokens)  ⇒ Link 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Link.

-
  
      #**render**(context)  ⇒ Object 

### Methods included from Filters::URLFilters

# absolute_url, #relative_url, #strip_index

## Constructor Details

###
  
    #**initialize**(tag_name, relative_path, tokens)  ⇒ Link 
  

  

  

  
    

Returns a new instance of Link.

```

14
15
16
17
18
```

```
# File 'lib/jekyll/tags/link.rb', line 14

def initialize(tag_name, relative_path, tokens)
  super

  @relative_path = relative_path.strip
end

```

## Class Method Details

###
  
    .**tag_name**  ⇒ Object 
  

  

  

  
    
      

```

9
10
11
```

```
# File 'lib/jekyll/tags/link.rb', line 9

def tag_name
  name.split("::").last.downcase
end

```

## Instance Method Details

###
  
    #**render**(context)  ⇒ Object 
  

  

  

  
    

Raises:

-

```

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
```

```
# File 'lib/jekyll/tags/link.rb', line 20

def render(context)
  @context = context
  site = context.registers[:site]
  relative_path = Liquid::Template.parse(@relative_path).render(context)
  relative_path_with_leading_slash = PathManager.join("", relative_path)

  site.each_site_file do |item|
    return relative_url(item) if item.relative_path == relative_path
    # This takes care of the case for static files that have a leading /
    return relative_url(item) if item.relative_path == relative_path_with_leading_slash
  end

  raise ArgumentError, "    Could not find document '\#{relative_path}' in tag '\#{self.class.tag_name}'.\n\n    Make sure the document exists and the path is correct.\n  MSG\nend\n"

```
