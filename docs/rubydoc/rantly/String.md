# Class: String
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- String
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/rantly/shrinks.rb
  
  

## Overview

  
    

String : shrink to “”

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**retry?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**shrink**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**shrinkable?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**retry?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

37
38
39
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 37

def retry?
  false
end

```

    
  

    
      
  
### 
  
    #**shrink**  ⇒ Object 
  

  

  

  
    
      

```

28
29
30
31
32
33
34
35
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 28

def shrink
  shrunk = dup
  unless empty?
    idx = Random.rand(size)
    shrunk[idx] = ''
  end
  shrunk
end

```

    
  

    
      
  
### 
  
    #**shrinkable?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

41
42
43
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 41

def shrinkable?
  self != ''
end

```