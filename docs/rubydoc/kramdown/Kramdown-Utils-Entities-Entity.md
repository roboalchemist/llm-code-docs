# Class: Kramdown::Utils::Entities::Entity
  
  
  

  
  
    Inherits:
    
      Struct
      
        

          
- Object
          
            
- Struct
          
            
- Kramdown::Utils::Entities::Entity
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/kramdown/utils/entities.rb
  
  

## Overview

  
    

Represents an entity that has a `code_point` and `name`.

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**code_point**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute code_point.

  

    
      
- 
  
    
      #**name**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute name.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**char**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return the UTF8 representation of the entity.

  

      
    

  

  
  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**code_point**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute code_point

  

  

Returns:

  
    
- 
      
      
      
      
        
        

the current value of code_point

      
    
  

  
    
      

```

18
19
20
```

    
    
      

```
# File 'lib/kramdown/utils/entities.rb', line 18

def code_point
  @code_point
end

```

    
  

    
      
      
      
  
### 
  
    #**name**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute name

  

  

Returns:

  
    
- 
      
      
      
      
        
        

the current value of name

      
    
  

  
    
      

```

18
19
20
```

    
    
      

```
# File 'lib/kramdown/utils/entities.rb', line 18

def name
  @name
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**char**  ⇒ Object 
  

  

  

  
    

Return the UTF8 representation of the entity.

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/kramdown/utils/entities.rb', line 20

def char
  [code_point].pack('U*') rescue nil
end

```