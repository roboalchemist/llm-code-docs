# Class: Integer
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Integer
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/rantly/shrinks.rb
  
  

## Overview

  
    

Integer : shrink to zero

  

  

  
    
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

17
18
19
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 17

def retry?
  false
end

```

    
  

    
      
  
### 
  
    #**shrink**  ⇒ Object 
  

  

  

  
    
      

```

3
4
5
6
7
8
9
10
11
12
13
14
15
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 3

def shrink
  if self > 8
    self / 2
  elsif self > 0
    self - 1
  elsif self < -8
    (self + 1) / 2
  elsif self < 0
    self + 1
  else
    0
  end
end

```

    
  

    
      
  
### 
  
    #**shrinkable?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

21
22
23
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 21

def shrinkable?
  self != 0
end

```