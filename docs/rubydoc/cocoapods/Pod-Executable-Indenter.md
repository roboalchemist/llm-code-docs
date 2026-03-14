# Class: Pod::Executable::Indenter
  
  
  

  
  
    Inherits:
    
      Array
      
        

          
- Object
          
            
- Array
          
            
- Pod::Executable::Indenter
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/executable.rb
  
  

## Overview

  
    

Helper class that allows to write to an IO instance taking into account the UI indentation level.

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**indent**  ⇒ Fixnum 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The indentation level of the UI.

  

    
      
- 
  
    
      #**io**  ⇒ IO 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The IO to which the output should be printed.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**<<**(value)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Stores a portion of the output and prints it to the IO instance.

  

      
        
- 
  
    
      #**initialize**(io = nil)  ⇒ Indenter 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Init a new Indenter.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(io = nil)  ⇒ Indenter 
  

  

  

  
    

Init a new Indenter

  

  

Parameters:

  
    
- 
      
        io
      
      
        (IO)
      
      
        *(defaults to: nil)*
      
      
        —
        

@see io

      
    
  

  
    
      

```

229
230
231
232
```

    
    
      

```
# File 'lib/cocoapods/executable.rb', line 229

def initialize(io = nil)
  @io = io
  @indent = ' ' * UI.indentation_level
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**indent**  ⇒ Fixnum  (readonly)
  

  

  

  
    

Returns The indentation level of the UI.

  

  

Returns:

  
    
- 
      
      
        (Fixnum)
      
      
      
        —
        

The indentation level of the UI.

      
    
  

  
    
      

```

219
220
221
```

    
    
      

```
# File 'lib/cocoapods/executable.rb', line 219

def indent
  @indent
end

```

    
  

    
      
      
      
  
### 
  
    #**io**  ⇒ IO  (readonly)
  

  

  

  
    

Returns the IO to which the output should be printed.

  

  

Returns:

  
    
- 
      
      
        (IO)
      
      
      
        —
        

the IO to which the output should be printed.

      
    
  

  
    
      

```

223
224
225
```

    
    
      

```
# File 'lib/cocoapods/executable.rb', line 223

def io
  @io
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**<<**(value)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Stores a portion of the output and prints it to the IO instance.

  

  

Parameters:

  
    
- 
      
        value
      
      
        (String)
      
      
      
        —
        

the output to print.

      
    
  

  
    
      

```

241
242
243
244
```

    
    
      

```
# File 'lib/cocoapods/executable.rb', line 241

def <<(value)
  super
  io << "#{indent}#{value}" if io
end

```