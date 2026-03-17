# Class: Prawn::SynchronizedCache
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Prawn::SynchronizedCache
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/utilities.rb
  
  

## Overview

  
    

Throughout the Prawn codebase, repeated calculations which can benefit from caching are made.  n some cases, caching and reusing results can not only save CPU cycles but also greatly reduce memory requirements But at the same time, we don’t want to throw away thread safety.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**[]**(key)  ⇒ any 
    

    
  
  
  
  
  
  
  
  

  
    

Get cache entry.

  

      
        
- 
  
    
      #**[]=**(key, value)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Set cache entry.

  

      
        
- 
  
    
      #**initialize**  ⇒ SynchronizedCache 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

As an optimization, this could access the hash directly on VMs with a global interpreter lock (like MRI).

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ SynchronizedCache 
  

  

  

  
    

As an optimization, this could access the hash directly on VMs with a global interpreter lock (like MRI).

  

  

  
    
      

```

12
13
14
15
```

    
    
      

```
# File 'lib/prawn/utilities.rb', line 12

def initialize
  @cache = {}
  @mutex = Mutex.new
end

```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**[]**(key)  ⇒ any 
  

  

  

  
    

Get cache entry.

  

  

Parameters:

  
    
- 
      
        key
      
      
        (any)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (any)
      
      
      
    
  

  
    
      

```

21
22
23
```

    
    
      

```
# File 'lib/prawn/utilities.rb', line 21

def [](key)
  @mutex.synchronize { @cache[key] }
end

```

    
  

    
      
  
### 
  
    #**[]=**(key, value)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Set cache entry.

  

  

Parameters:

  
    
- 
      
        key
      
      
        (any)
      
      
      
    
  
    
- 
      
        value
      
      
        (any)
      
      
      
    
  

  
    
      

```

30
31
32
```

    
    
      

```
# File 'lib/prawn/utilities.rb', line 30

def []=(key, value)
  @mutex.synchronize { @cache[key] = value }
end

```