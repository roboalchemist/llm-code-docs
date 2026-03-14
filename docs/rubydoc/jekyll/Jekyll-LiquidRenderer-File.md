# Class: Jekyll::LiquidRenderer::File
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::LiquidRenderer::File

        show all
      

    Defined in:
    lib/jekyll/liquid_renderer/file.rb
  
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(renderer, filename)  ⇒ File 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of File.

-
  
      #**parse**(content)  ⇒ Object 

-
  
      #**render**(*args)  ⇒ Object 

-
  
      #**render!**(*args)  ⇒ Object 

This method simply ‘rethrows any error’ before attempting to render the template.

-
  
      #**warnings**  ⇒ Object 

## Constructor Details

###
  
    #**initialize**(renderer, filename)  ⇒ File 
  

  

  

  
    

Returns a new instance of File.

```

6
7
8
9
```

```
# File 'lib/jekyll/liquid_renderer/file.rb', line 6

def initialize(renderer, filename)
  @renderer = renderer
  @filename = filename
end
```

## Instance Method Details

###
  
    #**parse**(content)  ⇒ Object 
  

  

  

  
    
      

```

11
12
13
14
15
16
17
18
```

```
# File 'lib/jekyll/liquid_renderer/file.rb', line 11

def parse(content)
  measure_time do
    @renderer.cache[@filename] ||= Liquid::Template.parse(content, :line_numbers => true)
  end
  @template = @renderer.cache[@filename]

  self
end
```

###
  
    #**render**(*args)  ⇒ Object 
  

  

  

  
    
      

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
```

```
# File 'lib/jekyll/liquid_renderer/file.rb', line 20

def render(*args)
  reset_template_assigns

  measure_time do
    measure_bytes do
      measure_counts do
        @template.render(*args)
      end
    end
  end
end
```

###
  
    #**render!**(*args)  ⇒ Object 
  

  

  

  
    

This method simply ‘rethrows any error’ before attempting to render the template.

```

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
```

```
# File 'lib/jekyll/liquid_renderer/file.rb', line 33

def render!(*args)
  reset_template_assigns

  measure_time do
    measure_bytes do
      measure_counts do
        @template.render!(*args)
      end
    end
  end
end
```

###
  
    #**warnings**  ⇒ Object 
  

  

  

  
    
      

```

45
46
47
```

```
# File 'lib/jekyll/liquid_renderer/file.rb', line 45

def warnings
  @template.warnings
end
```
