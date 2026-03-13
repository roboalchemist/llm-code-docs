# Class: Dry::Validation::Function
  
  Private

    Inherits:
    
      Object
      
        

          
- Object

- Dry::Validation::Function

        show all
      
    
  
  

  
  
  
      Extended by:
      Initializer
  
    Defined in:
    lib/dry/validation/function.rb
  
## Overview

  **This class is part of a private API.**
  You should avoid using this class if possible, as it may be removed or be changed in the future.

Abstract class for handling rule blocks

See Also:
  
- Rule

- Macro

## Direct Known Subclasses

Macro, Rule

## Instance Attribute Summary collapse

-
  
      #**block**  ⇒ Proc 

      readonly
    
    
  
  private

-
  
      #**block_options**  ⇒ Hash 

      readonly
    
    
  
  private

## Instance Attribute Details

###
  
    #**block**  ⇒ Proc  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Proc)

```

20
```

```
# File 'lib/dry/validation/function.rb', line 20

option :block
```

###
  
    #**block_options**  ⇒ Hash  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Hash)

```

25
```

```
# File 'lib/dry/validation/function.rb', line 25

option :block_options, default: -> { block ? map_keywords(block) : EMPTY_HASH }
```
