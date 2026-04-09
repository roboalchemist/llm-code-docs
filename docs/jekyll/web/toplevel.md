# Top Level Namespace
  
## Defined Under Namespace

      **Modules:** Jekyll, Kramdown
    
  
    
  

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**require_all**(path)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Require all of the Ruby files in the given directory.

## Instance Method Details

###
  
    #**require_all**(path)  ⇒ Object 
  

  

  

  
    

Require all of the Ruby files in the given directory.

path - The String relative path from here to the directory.

Returns nothing.

```

10
11
12
13
14
15
```

```
# File 'lib/jekyll.rb', line 10

def require_all(path)
  glob = File.join(__dir__, path, "*.rb")
  Dir[glob].sort.each do |f|
    require f
  end
end

```
