# Class: Jekyll::PageExcerpt
  
    Inherits:
    
      Excerpt
      
        

          
- Object

- Excerpt

- Jekyll::PageExcerpt

        show all
      

    Defined in:
    lib/jekyll/page_excerpt.rb
  
## Instance Attribute Summary collapse

-
  
      #**doc**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute doc.

### Attributes inherited from Excerpt

# content, #ext, #output

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**inspect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**render_with_liquid?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**to_liquid**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods inherited from Excerpt

# data, #include?, #initialize, #path, #place_in_layout?, #relative_path, #to_s, #trigger_hooks

## Constructor Details

This class inherits a constructor from Jekyll::Excerpt
  
## Instance Attribute Details

###
  
    #**doc**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute doc.

```

5
6
7
```

```
# File 'lib/jekyll/page_excerpt.rb', line 5

def doc
  @doc
end

```

## Instance Method Details

###
  
    #**inspect**  ⇒ Object 
  

  

  

  
    
      

```

21
22
23
```

```
# File 'lib/jekyll/page_excerpt.rb', line 21

def inspect
  "#<#{self.class} id=#{id.inspect}>"
end

```

###
  
    #**render_with_liquid?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

```

15
16
17
18
19
```

```
# File 'lib/jekyll/page_excerpt.rb', line 15

def render_with_liquid?
  return false if data["render_with_liquid"] == false

  Jekyll::Utils.has_liquid_construct?(content)
end

```

###
  
    #**to_liquid**  ⇒ Object 
  

  

  

  
    
      

```

11
12
13
```

```
# File 'lib/jekyll/page_excerpt.rb', line 11

def to_liquid
  @to_liquid ||= doc.to_liquid(EXCERPT_ATTRIBUTES)
end

```
