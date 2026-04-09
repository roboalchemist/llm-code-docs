# Module: Prawn::Errors
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/errors.rb
  
  

## Overview

  
    

Custom error classes for Prawn.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        InvalidTableSpan =
          
  
    

Raised when a table is spanned in an impossible way.

  

  

        
        

```
Class.new(StandardError)

```

      
        NotOnPage =
          
  
    

This error is raised when a method requiring a current page is called without being on a page.

  

  

        
        

```
Class.new(StandardError)

```

      
        UnknownFont =
          
  
    

This error is raised when Prawn cannot find a specified font.

  

  

        
        

```
Class.new(StandardError)

```

      
        CannotFit =
          
  
    

Raised when Prawn is asked to draw something into a too-small box.

  

  

        
        

```
Class.new(StandardError)

```

      
        CannotGroup =
          
  
    

Raised if #group is called with a block that is too big to be rendered in the current context.

  

  

        
        

```
Class.new(StandardError)

```

      
        IncompatibleStringEncoding =
          
  
    

This error is raised when Prawn is being used on a M17N aware VM, and the user attempts to add text that isn’t compatible with UTF-8 to their document.

  

  

        
        

```
Class.new(StandardError)

```

      
        UnknownOption =
          
  
    

This error is raised when Prawn encounters an unknown key in functions that accept an options hash.  This usually means there is a typo in your code or that the option you are trying to use has a different name than what you have specified.

  

  

        
        

```
Class.new(StandardError)

```

      
        UnsupportedImageType =
          
  
    

This error is raised when a user attempts to embed an image of an unsupported type. This can either a completely unsupported format, or a dialect of a supported format (i.e. some types of PNG).

  

  

        
        

```
Class.new(StandardError)

```

      
        NameTaken =
          
  
    

This error is raised when a named element has already been created. For example, in the stamp module, stamps must have unique names within a document.

  

  

        
        

```
Class.new(StandardError)

```

      
        InvalidName =
          
  
    

This error is raised when a name is not a valid format.

  

  

        
        

```
Class.new(StandardError)

```

      
        UndefinedObjectName =
          
  
    

This error is raised when an object is attempted to be referenced by name, but no such name is associated with an object.

  

  

        
        

```
Class.new(StandardError)

```

      
        RequiredOption =
          
  
    

This error is raised when a required option has not been set.

  

  

        
        

```
Class.new(StandardError)

```

      
        UnknownOutlineTitle =
          
  
    

This error is raised when a requested outline item with a given title does not exist.

  

  

        
        

```
Class.new(StandardError)

```

      
        BlockRequired =
          
  
    

This error is raised when a block is required, but not provided.

  

  

        
        

```
Class.new(StandardError)

```

      
        InvalidGraphicsPath =
          
  
    

This error is raised when a graphics method is called with improper arguments.

  

  

        
        

```
Class.new(StandardError)

```

      
        UnrecognizedTableContent =
          
  
    

Raised when unrecognized content is provided for a table cell.

  

  

        
        

```
Class.new(StandardError)

```

      
        InvalidJoinStyle =
          
  
    

This error is raised when an incompatible join style is specified.

  

  

        
        

```
Class.new(StandardError)

```