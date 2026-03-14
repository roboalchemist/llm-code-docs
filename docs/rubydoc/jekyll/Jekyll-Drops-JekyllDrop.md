# Class: Jekyll::Drops::JekyllDrop
  
    Inherits:
    
      Liquid::Drop
      
        

          
- Object

- Liquid::Drop

- Jekyll::Drops::JekyllDrop

        show all
      

    Defined in:
    lib/jekyll/drops/jekyll_drop.rb
  
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**global**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**environment**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**to_h**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**to_json**(state = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**version**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Class Method Details

###
  
    .**global**  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
```

```
# File 'lib/jekyll/drops/jekyll_drop.rb', line 7

def global
  @global ||= JekyllDrop.new
end
```

## Instance Method Details

###
  
    #**environment**  ⇒ Object 
  

  

  

  
    
      

```

16
17
18
```

```
# File 'lib/jekyll/drops/jekyll_drop.rb', line 16

def environment
  Jekyll.env
end
```

###
  
    #**to_h**  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
23
24
25
```

```
# File 'lib/jekyll/drops/jekyll_drop.rb', line 20

def to_h
  @to_h ||= {
    "version"     => version,
    "environment" => environment,
  }
end
```

###
  
    #**to_json**(state = nil)  ⇒ Object 
  

  

  

  
    
      

```

27
28
29
```

```
# File 'lib/jekyll/drops/jekyll_drop.rb', line 27

def to_json(state = nil)
  JSON.generate(to_h, state)
end
```

###
  
    #**version**  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
```

```
# File 'lib/jekyll/drops/jekyll_drop.rb', line 12

def version
  Jekyll::VERSION
end
```
