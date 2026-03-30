# Class: Dry::Validation::Message
  
    Inherits:
    
      Schema::Message
      
        

          
- Object

- Schema::Message

- Dry::Validation::Message

        show all
      

    Defined in:
    lib/dry/validation/message.rb
  
## Overview

Message message

## Direct Known Subclasses

Localized

## Defined Under Namespace

      **Classes:** Localized
    
  
## Instance Attribute Summary collapse

-
  
      #**meta**  ⇒ Hash 

      readonly
    
    
  
  
  
  
  

  
    

Optional hash with meta-data.

-
  
      #**path**  ⇒ Array<Symbol, Integer> 

      readonly
    
    
  
  
  
  
  

  
    

The path to the value with the error.

-
  
      #**text**  ⇒ String 

      readonly
    
    
  
  
  
  
  

  
    

The error message text.

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**[]**(text, path, meta)  ⇒ Message, Message::Localized 
    

    
  
  private

Build an error.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**base?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Check if this is a base error not associated with any key.

-
  
      #**initialize**(text, path:, meta: EMPTY_HASH)  ⇒ Message 

    constructor
  
  private

Initialize a new error object.

-
  
      #**to_s**  ⇒ String 

Dump error to a string.

## Constructor Details

###
  
    #**initialize**(text, path:, meta: EMPTY_HASH)  ⇒ Message 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Initialize a new error object

rubocop: disable Lint/MissingSuper

```

69
70
71
72
73
```

```
# File 'lib/dry/validation/message.rb', line 69

def initialize(text, path:, meta: EMPTY_HASH)
  @text = text
  @path = Array(path)
  @meta = meta
end
```

## Instance Attribute Details

###
  
    #**meta**  ⇒ Hash  (readonly)
  

  

  

  
    

Optional hash with meta-data

Returns:

-

        (Hash)

```

30
31
32
```

```
# File 'lib/dry/validation/message.rb', line 30

def meta
  @meta
end
```

###
  
    #**path**  ⇒ Array<Symbol, Integer>  (readonly)
  

  

  

  
    

The path to the value with the error

Returns:

-

        (Array<Symbol, Integer>)

```

23
24
25
```

```
# File 'lib/dry/validation/message.rb', line 23

def path
  @path
end
```

###
  
    #**text**  ⇒ String  (readonly)
  

  

  

  
    

The error message text

Returns:

-

        (String)

        —
        

text

```

16
17
18
```

```
# File 'lib/dry/validation/message.rb', line 16

def text
  @text
end
```

## Class Method Details

###
  
    .**[]**(text, path, meta)  ⇒ Message, Message::Localized 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Build an error

Returns:

-

        (Message, Message::Localized)

```

60
61
62
63
```

```
# File 'lib/dry/validation/message.rb', line 60

def self.[](text, path, meta)
  klass = text.respond_to?(:call) ? Localized : Message
  klass.new(text, path: path, meta: meta)
end
```

## Instance Method Details

###
  
    #**base?**  ⇒ Boolean 
  

  

  

  
    

Check if this is a base error not associated with any key

Returns:

-

        (Boolean)

```

81
82
83
```

```
# File 'lib/dry/validation/message.rb', line 81

def base?
  @base ||= path.compact.empty?
end
```

###
  
    #**to_s**  ⇒ String 
  

  

  

  
    

Dump error to a string

Returns:

-

        (String)

```

90
91
92
```

```
# File 'lib/dry/validation/message.rb', line 90

def to_s
  text
end
```
