# Class: Dry::Validation::Failures
  
    Inherits:
    
      Object
      
        

          
- Object

- Dry::Validation::Failures

        show all
      

    Defined in:
    lib/dry/validation/failures.rb
  
## Overview

Failure accumulator object

## Instance Attribute Summary collapse

-
  
      #**opts**  ⇒ Hash 

      readonly
    
    
  
  private

Options for messages.

-
  
      #**path**  ⇒ Dry::Schema::Path 

      readonly
    
    
  
  private

The path for messages accumulated by failures object.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**empty?**  ⇒ Boolean 
    

    
  
  private

-
  
      #**failure**(message, tokens = EMPTY_HASH)  ⇒ Object 

Set failure.

-
  
      #**initialize**(path = ROOT_PATH)  ⇒ Failures 

    constructor
  
  private

A new instance of Failures.

## Constructor Details

###
  
    #**initialize**(path = ROOT_PATH)  ⇒ Failures 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns a new instance of Failures.

```

29
30
31
32
```

```
# File 'lib/dry/validation/failures.rb', line 29

def initialize(path = ROOT_PATH)
  @path = ::Dry::Schema::Path[path]
  @opts = EMPTY_ARRAY.dup
end
```

## Instance Attribute Details

###
  
    #**opts**  ⇒ Hash  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Options for messages

These options are used by MessageResolver

Returns:

-

        (Hash)

```

26
27
28
```

```
# File 'lib/dry/validation/failures.rb', line 26

def opts
  @opts
end
```

###
  
    #**path**  ⇒ Dry::Schema::Path  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

The path for messages accumulated by failures object

Returns:

-

        (Dry::Schema::Path)

```

17
18
19
```

```
# File 'lib/dry/validation/failures.rb', line 17

def path
  @path
end
```

## Instance Method Details

###
  
    #**empty?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Boolean)

```

65
66
67
```

```
# File 'lib/dry/validation/failures.rb', line 65

def empty?
  opts.empty?
end
```

###
  
      #**failure**(message)  ⇒ Object 
    
      #**failure**(id)  ⇒ Object 
    
      #**failure**(meta_hash)  ⇒ Object 
    
  

  

  

  
    

Set failure

Overloads:
  
-
        #**failure**(message)  ⇒ Object 
        
  
Set message text explicitly

#### Examples

```
failure('this failed')
```

Parameters:

-

        message

        (String)
      
      
      
        —
        

The message text

-
        #**failure**(id)  ⇒ Object 
        
  
Use message identifier (needs localized messages setup)

#### Examples

```
failure(:taken)
```

Parameters:

-

        id

        (Symbol)
      
      
      
        —
        

The message id

-
        #**failure**(meta_hash)  ⇒ Object 
        
  
Use meta_hash as a message (either explicitely or as an identifier), setting the rest of the hash as error meta attribute

#### Examples

```
failure({text: :invalid, key: value})
```

Parameters:

-

        meta

        (Hash)
      
      
      
        —
        

The hash containing the message as value for the :text key

See Also:
  
- Evaluator#key

- Evaluator#base

```

59
60
61
62
```

```
# File 'lib/dry/validation/failures.rb', line 59

def failure(message, tokens = EMPTY_HASH)
  opts << {message: message, tokens: tokens, path: path}
  self
end
```
