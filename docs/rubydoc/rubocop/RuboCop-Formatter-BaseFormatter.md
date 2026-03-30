# Class: RuboCop::Formatter::BaseFormatter
  
    Inherits:
    
      Object
      
        

          
- Object

- RuboCop::Formatter::BaseFormatter

        show all
      

    Defined in:
    lib/rubocop/formatter/base_formatter.rb
  
## Overview

Abstract base class for formatter, implements all public API methods.

## Creating Custom Formatter

You can create a custom formatter by subclassing `RuboCop::Formatter::BaseFormatter` and overriding some methods or by implementing all the methods by duck typing.

## Using Custom Formatter in Command Line

You can tell RuboCop to use your custom formatter with a combination of `--format` and `--require` option. For example, when you have defined `MyCustomFormatter` in `./path/to/my_custom_formatter.rb`, you would type this command:

```
rubocop --require ./path/to/my_custom_formatter --format MyCustomFormatter

```

Note: The path passed to `--require` is directly passed to `Kernel.require`. If your custom formatter file is not in ‘$LOAD_PATH`, you need to specify the path as relative path prefixed with`./` explicitly or absolute path.

## Method Invocation Order

For example, when RuboCop inspects 2 files, the invocation order should be like this:

-

`#initialize`

-

`#started`

-

`#file_started`

-

`#file_finished`

-

`#file_started`

-

`#file_finished`

-

`#finished`

## Direct Known Subclasses

DisabledConfigFormatter, EmacsStyleFormatter, FileListFormatter, GitHubActionsFormatter, HTMLFormatter, JSONFormatter, JUnitFormatter, MarkdownFormatter, OffenseCountFormatter, SimpleTextFormatter, WorstOffendersFormatter

## Instance Attribute Summary collapse

-
  
      #**options**  ⇒ Hash 

      readonly
    
    
  
  
  
  
  

  
    
  

    
      
-
  
      #**output**  ⇒ IO 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The IO object passed to `#initialize`.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**file_finished**(file, offenses)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Invoked at the end of inspecting each files.

-
  
      #**file_started**(file, options)  ⇒ void 

Invoked at the beginning of inspecting each files.

-
  
      #**finished**(inspected_files)  ⇒ void 

Invoked after all files are inspected or interrupted by user.

-
  
      #**initialize**(output, options = {})  ⇒ BaseFormatter 

    constructor
  
  
  
  
  
  

  
    

A new instance of BaseFormatter.

-
  
      #**started**(target_files)  ⇒ void 

Invoked once before any files are inspected.

## Constructor Details

###
  
    #**initialize**(output, options = {})  ⇒ BaseFormatter 
  

  

  

  
    

Returns a new instance of BaseFormatter.

Parameters:

-

        output

        (IO)
      
      
      
        —
        

‘$stdout` or opened file

```

63
64
65
66
```

```
# File 'lib/rubocop/formatter/base_formatter.rb', line 63

def initialize(output, options = {})
  @output = output
  @options = options
end
```

## Instance Attribute Details

###
  
    #**options**  ⇒ Hash  (readonly)
  

  

  

  
    

Returns:

-

        (Hash)

```

57
58
59
```

```
# File 'lib/rubocop/formatter/base_formatter.rb', line 57

def options
  @options
end
```

###
  
    #**output**  ⇒ IO  (readonly)
  

  

  

  
    

Returns the IO object passed to `#initialize`.

Returns:

-

        (IO)

        —
        

the IO object passed to `#initialize`

See Also:
  
- #initialize

```

50
51
52
```

```
# File 'lib/rubocop/formatter/base_formatter.rb', line 50

def output
  @output
end
```

## Instance Method Details

###
  
    #**file_finished**(file, offenses)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Invoked at the end of inspecting each files.

Parameters:

-

        file

        (String)
      
      
      
        —
        

the file path

-

        offenses

        (Array(RuboCop::Cop::Offense))
      
      
      
        —
        

all detected offenses for the file

See Also:
  
- Cop::Offense

```

104
```

```
# File 'lib/rubocop/formatter/base_formatter.rb', line 104

def file_finished(file, offenses); end
```

###
  
    #**file_started**(file, options)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Invoked at the beginning of inspecting each files.

Parameters:

-

        file

        (String)
      
      
      
        —
        

the file path

-

        options

        (Hash)
      
      
      
        —
        

file specific information, currently this is always empty.

```

89
```

```
# File 'lib/rubocop/formatter/base_formatter.rb', line 89

def file_started(file, options); end
```

###
  
    #**finished**(inspected_files)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Invoked after all files are inspected or interrupted by user.

Parameters:

-

        inspected_files

        (Array(String))
      
      
      
        —
        

the inspected file paths. This would be same as `target_files` passed to `#started` unless RuboCop is interrupted by user.

```

116
```

```
# File 'lib/rubocop/formatter/base_formatter.rb', line 116

def finished(inspected_files); end
```

###
  
    #**started**(target_files)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Invoked once before any files are inspected.

Parameters:

-

        target_files

        (Array(String))
      
      
      
        —
        

all target file paths to be inspected

```

76
```

```
# File 'lib/rubocop/formatter/base_formatter.rb', line 76

def started(target_files); end
```
