# Module: Pod::CoreUI
  
    Defined in:
    lib/cocoapods/user_interface.rb
  
## Overview

Redirects cocoapods-core UI.

##

      Helpers
      collapse
    

    

      
        
-
  
      .**print**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**puts**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**warn**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

###
  
    .**print**(message)  ⇒ Object 
  

  

  

  
    
      

```

438
439
440
```

```
# File 'lib/cocoapods/user_interface.rb', line 438

def print(message)
  UI.print(message)
end
```

###
  
    .**puts**(message)  ⇒ Object 
  

  

  

  
    
      

```

434
435
436
```

```
# File 'lib/cocoapods/user_interface.rb', line 434

def puts(message)
  UI.puts message
end
```

###
  
    .**warn**(message)  ⇒ Object 
  

  

  

  
    
      

```

442
443
444
```

```
# File 'lib/cocoapods/user_interface.rb', line 442

def warn(message)
  UI.warn message
end
```
