# Class: Jekyll::Excerpt
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::Excerpt

        show all
      
    
  
  

  
  
  
      Extended by:
      Forwardable
  
    Defined in:
    lib/jekyll/excerpt.rb
  
## Direct Known Subclasses

PageExcerpt

## Instance Attribute Summary collapse

-
  
      #**content**  ⇒ Object 

Returns the value of attribute content.

-
  
      #**doc**  ⇒ Object 

Returns the value of attribute doc.

-
  
      #**ext**  ⇒ Object 

Returns the value of attribute ext.

-
  
      #**output**  ⇒ Object 

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**data**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Fetch YAML front-matter data from related doc, without layout key.

-
  
      #**id**  ⇒ Object 

The UID for this doc (useful in feeds).

-
  
      #**include?**(something)  ⇒ Boolean 

Check if excerpt includes a string.

-
  
      #**initialize**(doc)  ⇒ Excerpt 

    constructor
  
  
  
  
  
  

  
    

Initialize this Excerpt instance.

-
  
      #**inspect**  ⇒ Object 

Returns the shorthand String identifier of this doc.

-
  
      #**path**  ⇒ Object 

‘Path’ of the excerpt.

-
  
      #**place_in_layout?**  ⇒ Boolean 

-
  
      #**relative_path**  ⇒ Object 

‘Relative Path’ of the excerpt.

-
  
      #**render_with_liquid?**  ⇒ Boolean 

-
  
      #**to_liquid**  ⇒ Object 

-
  
      #**to_s**  ⇒ Object 

-
  
      #**trigger_hooks**  ⇒ Object 

## Constructor Details

###
  
    #**initialize**(doc)  ⇒ Excerpt 
  

  

  

  
    

Initialize this Excerpt instance.

doc - The Document.

Returns the new Excerpt.

```

23
24
25
26
```

```
# File 'lib/jekyll/excerpt.rb', line 23

def initialize(doc)
  self.doc = doc
  self.content = extract_excerpt(doc.content)
end
```

## Instance Attribute Details

###
  
    #**content**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute content.

```

7
8
9
```

```
# File 'lib/jekyll/excerpt.rb', line 7

def content
  @content
end
```

###
  
    #**doc**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute doc.

```

7
8
9
```

```
# File 'lib/jekyll/excerpt.rb', line 7

def doc
  @doc
end
```

###
  
    #**ext**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute ext.

```

7
8
9
```

```
# File 'lib/jekyll/excerpt.rb', line 7

def ext
  @ext
end
```

###
  
    #**output**  ⇒ Object 
  

  

  

  
    
      

```

82
83
84
```

```
# File 'lib/jekyll/excerpt.rb', line 82

def output
  @output ||= Renderer.new(doc.site, self, site.site_payload).run
end
```

## Instance Method Details

###
  
    #**data**  ⇒ Object 
  

  

  

  
    

Fetch YAML front-matter data from related doc, without layout key

Returns Hash of doc data

```

31
32
33
34
35
36
```

```
# File 'lib/jekyll/excerpt.rb', line 31

def data
  @data ||= doc.data.dup
  @data.delete("layout")
  @data.delete("excerpt")
  @data
end
```

###
  
    #**id**  ⇒ Object 
  

  

  

  
    

The UID for this doc (useful in feeds). e.g. /2008/11/05/my-awesome-doc

Returns the String UID.

```

65
66
67
```

```
# File 'lib/jekyll/excerpt.rb', line 65

def id
  "#{doc.id}#excerpt"
end
```

###
  
    #**include?**(something)  ⇒ Boolean 
  

  

  

  
    

Check if excerpt includes a string

Returns true if the string passed in

Returns:

-

        (Boolean)

```

57
58
59
```

```
# File 'lib/jekyll/excerpt.rb', line 57

def include?(something)
  output&.include?(something) || content.include?(something)
end
```

###
  
    #**inspect**  ⇒ Object 
  

  

  

  
    

Returns the shorthand String identifier of this doc.

```

78
79
80
```

```
# File 'lib/jekyll/excerpt.rb', line 78

def inspect
  "<#{self.class} id=#{id}>"
end
```

###
  
    #**path**  ⇒ Object 
  

  

  

  
    

‘Path’ of the excerpt.

Returns the path for the doc this excerpt belongs to with #excerpt appended

```

43
44
45
```

```
# File 'lib/jekyll/excerpt.rb', line 43

def path
  File.join(doc.path, "#excerpt")
end
```

###
  
    #**place_in_layout?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

86
87
88
```

```
# File 'lib/jekyll/excerpt.rb', line 86

def place_in_layout?
  false
end
```

###
  
    #**relative_path**  ⇒ Object 
  

  

  

  
    

‘Relative Path’ of the excerpt.

Returns the relative_path for the doc this excerpt belongs to with #excerpt appended

```

50
51
52
```

```
# File 'lib/jekyll/excerpt.rb', line 50

def relative_path
  @relative_path ||= File.join(doc.relative_path, "#excerpt")
end
```

###
  
    #**render_with_liquid?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

90
91
92
93
94
```

```
# File 'lib/jekyll/excerpt.rb', line 90

def render_with_liquid?
  return false if data["render_with_liquid"] == false

  !(coffeescript_file? || yaml_file? || !Utils.has_liquid_construct?(content))
end
```

###
  
    #**to_liquid**  ⇒ Object 
  

  

  

  
    
      

```

73
74
75
```

```
# File 'lib/jekyll/excerpt.rb', line 73

def to_liquid
  Jekyll::Drops::ExcerptDrop.new(self)
end
```

###
  
    #**to_s**  ⇒ Object 
  

  

  

  
    
      

```

69
70
71
```

```
# File 'lib/jekyll/excerpt.rb', line 69

def to_s
  output || content
end
```

###
  
    #**trigger_hooks**  ⇒ Object 
  

  

  

  
    
      

```

38
```

```
# File 'lib/jekyll/excerpt.rb', line 38

def trigger_hooks(*); end
```
