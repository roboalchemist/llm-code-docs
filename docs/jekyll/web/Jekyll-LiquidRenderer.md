# Class: Jekyll::LiquidRenderer
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::LiquidRenderer

        show all
      

    Defined in:
    lib/jekyll/liquid_renderer.rb,

  lib/jekyll/liquid_renderer/file.rb,
 lib/jekyll/liquid_renderer/table.rb

## Defined Under Namespace

      **Classes:** File, Table
    
  

  
    
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**format_error**(error, path)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**cache**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

A persistent cache to store and retrieve parsed templates based on the filename via ‘LiquidRenderer::File#parse`.

-
  
      #**file**(filename)  ⇒ Object 

-
  
      #**increment_bytes**(filename, bytes)  ⇒ Object 

-
  
      #**increment_count**(filename)  ⇒ Object 

-
  
      #**increment_time**(filename, time)  ⇒ Object 

-
  
      #**initialize**(site)  ⇒ LiquidRenderer 

    constructor
  
  
  
  
  
  

  
    

A new instance of LiquidRenderer.

-
  
      #**reset**  ⇒ Object 

-
  
      #**stats_table**(num_of_rows = 50)  ⇒ Object 

## Constructor Details

###
  
    #**initialize**(site)  ⇒ LiquidRenderer 
  

  

  

  
    

Returns a new instance of LiquidRenderer.

```

8
9
10
11
12
```

```
# File 'lib/jekyll/liquid_renderer.rb', line 8

def initialize(site)
  @site = site
  Liquid::Template.error_mode = @site.config["liquid"]["error_mode"].to_sym
  reset
end
```

## Class Method Details

###
  
    .**format_error**(error, path)  ⇒ Object 
  

  

  

  
    
      

```

42
43
44
```

```
# File 'lib/jekyll/liquid_renderer.rb', line 42

def self.format_error(error, path)
  "#{error.message} in #{path}"
end
```

## Instance Method Details

###
  
    #**cache**  ⇒ Object 
  

  

  

  
    

A persistent cache to store and retrieve parsed templates based on the filename via ‘LiquidRenderer::File#parse`

It is emptied when `self.reset` is called.

```

50
51
52
```

```
# File 'lib/jekyll/liquid_renderer.rb', line 50

def cache
  @cache ||= {}
end
```

###
  
    #**file**(filename)  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
22
23
24
```

```
# File 'lib/jekyll/liquid_renderer.rb', line 19

def file(filename)
  filename = normalize_path(filename)
  LiquidRenderer::File.new(self, filename).tap do
    @stats[filename] ||= new_profile_hash
  end
end
```

###
  
    #**increment_bytes**(filename, bytes)  ⇒ Object 
  

  

  

  
    
      

```

26
27
28
```

```
# File 'lib/jekyll/liquid_renderer.rb', line 26

def increment_bytes(filename, bytes)
  @stats[filename][:bytes] += bytes
end
```

###
  
    #**increment_count**(filename)  ⇒ Object 
  

  

  

  
    
      

```

34
35
36
```

```
# File 'lib/jekyll/liquid_renderer.rb', line 34

def increment_count(filename)
  @stats[filename][:count] += 1
end
```

###
  
    #**increment_time**(filename, time)  ⇒ Object 
  

  

  

  
    
      

```

30
31
32
```

```
# File 'lib/jekyll/liquid_renderer.rb', line 30

def increment_time(filename, time)
  @stats[filename][:time] += time
end
```

###
  
    #**reset**  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
17
```

```
# File 'lib/jekyll/liquid_renderer.rb', line 14

def reset
  @stats = {}
  @cache = {}
end
```

###
  
    #**stats_table**(num_of_rows = 50)  ⇒ Object 
  

  

  

  
    
      

```

38
39
40
```

```
# File 'lib/jekyll/liquid_renderer.rb', line 38

def stats_table(num_of_rows = 50)
  LiquidRenderer::Table.new(@stats).to_s(num_of_rows)
end
```
