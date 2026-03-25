# Class: RuboCop::ArgumentsEnv
  
  Private

    Inherits:
    
      Object
      
        

          
- Object

- RuboCop::ArgumentsEnv

        show all
      

    Defined in:
    lib/rubocop/arguments_env.rb
  
## Overview

  **This class is part of a private API.**
  You should avoid using this class if possible, as it may be removed or be changed in the future.

This is a class that reads optional command line arguments to rubocop from environment variable.

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**read_as_arguments**  ⇒ Object 
    

    
  
  private

## Class Method Details

###
  
    .**read_as_arguments**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

7
8
9
10
11
12
13
14
15
```

```
# File 'lib/rubocop/arguments_env.rb', line 7

def self.read_as_arguments
  if (arguments = ENV.fetch('RUBOCOP_OPTS', '')).empty?
    []
  else
    require 'shellwords'

    Shellwords.split(arguments)
  end
end
```
