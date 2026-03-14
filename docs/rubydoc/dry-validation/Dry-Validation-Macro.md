# Class: Dry::Validation::Macro
  
    Inherits:
    
      Function
      
        

          
- Object

- Function

- Dry::Validation::Macro

        show all
      

    Defined in:
    lib/dry/validation/macro.rb
  
## Overview

A wrapper for macro validation blocks

## Instance Attribute Summary collapse

-
  
      #**args**  ⇒ Array 

      readonly
    
    
  
  
  
  
  

  
    
  

    
      
-
  
      #**block**  ⇒ Proc 
    

    
  
  
  
  
    
      readonly
    
    
  
  private

-
  
      #**name**  ⇒ Symbol 

      readonly
    
    
  
  
  
  
  

  
    
  

    
  
### Attributes inherited from Function

# block_options

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**extract_block_options**(options)  ⇒ Object 
    

    
  
  private

-
  
      #**with**(args)  ⇒ Object 

  private

## Instance Attribute Details

###
  
    #**args**  ⇒ Array  (readonly)
  

  

  

  
    

Returns:

-

        (Array)

```

19
```

```
# File 'lib/dry/validation/macro.rb', line 19

option :args
```

###
  
    #**block**  ⇒ Proc  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Proc)

```

24
```

```
# File 'lib/dry/validation/macro.rb', line 24

option :block
```

###
  
    #**name**  ⇒ Symbol  (readonly)
  

  

  

  
    

Returns:

-

        (Symbol)

```

14
```

```
# File 'lib/dry/validation/macro.rb', line 14

param :name
```

## Instance Method Details

###
  
    #**extract_block_options**(options)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

32
33
34
```

```
# File 'lib/dry/validation/macro.rb', line 32

def extract_block_options(options)
  block_options.transform_values { options[_1] }
end
```

###
  
    #**with**(args)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

27
28
29
```

```
# File 'lib/dry/validation/macro.rb', line 27

def with(args)
  self.class.new(name, args: args, block: block)
end
```
