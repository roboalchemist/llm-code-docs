# Class: Jekyll::Inclusion
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::Inclusion

        show all
      

    Defined in:
    lib/jekyll/inclusion.rb
  
## Instance Attribute Summary collapse

-
  
      #**name**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute name.

-
  
      #**path**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute path.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**content**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**initialize**(site, base, name)  ⇒ Inclusion 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Inclusion.

-
  
      #**inspect**  ⇒ Object 

      (also: #to_s)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**render**(context)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

## Constructor Details

###
  
    #**initialize**(site, base, name)  ⇒ Inclusion 
  

  

  

  
    

Returns a new instance of Inclusion.

```

8
9
10
11
12
```

```
# File 'lib/jekyll/inclusion.rb', line 8

def initialize(site, base, name)
  @site = site
  @name = name
  @path = PathManager.join(base, name)
end
```

## Instance Attribute Details

###
  
    #**name**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute name.

```

5
6
7
```

```
# File 'lib/jekyll/inclusion.rb', line 5

def name
  @name
end
```

###
  
    #**path**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute path.

```

5
6
7
```

```
# File 'lib/jekyll/inclusion.rb', line 5

def path
  @path
end
```

## Instance Method Details

###
  
    #**content**  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
```

```
# File 'lib/jekyll/inclusion.rb', line 23

def content
  @content ||= File.read(path, **site.file_read_opts)
end
```

###
  
    #**inspect**  ⇒ Object 
  

  
    Also known as:
    to_s
    
  

  

  
    
      

```

27
28
29
```

```
# File 'lib/jekyll/inclusion.rb', line 27

def inspect
  "#{self.class} #{path.inspect}"
end
```

###
  
    #**render**(context)  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
17
18
19
20
21
```

```
# File 'lib/jekyll/inclusion.rb', line 14

def render(context)
  @template ||= site.liquid_renderer.file(path).parse(content)
  @template.render!(context)
rescue Liquid::Error => e
  e.template_name  = path
  e.markup_context = "included " if e.markup_context.nil?
  raise e
end
```
