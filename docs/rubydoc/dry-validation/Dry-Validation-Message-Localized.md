# Class: Dry::Validation::Message::Localized
  
    Inherits:
    
      Dry::Validation::Message
      
        

          
- Object

- Schema::Message

- Dry::Validation::Message

- Dry::Validation::Message::Localized

        show all
      

    Defined in:
    lib/dry/validation/message.rb
  
## Overview

A localized message type

Localized messsages can be translated to other languages at run-time

## Instance Attribute Summary

### Attributes inherited from Dry::Validation::Message

# meta, #path, #text

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**evaluate**(**opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Evaluate message text using provided locale.

### Methods inherited from Dry::Validation::Message

[], #base?, #initialize, #to_s

## Constructor Details

This class inherits a constructor from Dry::Validation::Message
  
## Instance Method Details

###
  
    #**evaluate**(**opts)  ⇒ Object 
  

  

  

  
    

Evaluate message text using provided locale

#### Examples

```
result.errors[:email].evaluate(locale: :en, full: true)
# "email is invalid"
```

Parameters:

-

        opts

        (Hash)
      
      
      
    
  

  
    
    
    

Options Hash (**opts):

-
          :locale
          (Symbol)
          
            
          
          
            — 

Which locale to use

-
          :full
          (Boolean)
          
            
          
          
            — 

Whether message text should include the key name

```

49
50
51
52
```

```
# File 'lib/dry/validation/message.rb', line 49

def evaluate(**opts)
  evaluated_text, rest = text.(**opts)
  Message.new(evaluated_text, path: path, meta: rest.merge(meta))
end
```
