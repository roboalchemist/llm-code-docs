# Class: RuboCop::CLI::Command::Base
  
  Private

    Inherits:
    
      Object
      
        

          
- Object

- RuboCop::CLI::Command::Base

        show all
      

    Defined in:
    lib/rubocop/cli/command/base.rb
  
## Overview

  **This class is part of a private API.**
  You should avoid using this class if possible, as it may be removed or be changed in the future.

A subcommand in the CLI.

## Direct Known Subclasses

AutoGenerateConfig, ExecuteRunner, InitDotfile, LSP, MCP, ShowCops, ShowDocsUrl, SuggestExtensions, Version

## Class Attribute Summary collapse

-
  
      .**command_name**  ⇒ Object 

  private

## Instance Attribute Summary collapse

-
  
      #**env**  ⇒ Object 

      readonly
    
    
  
  private

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**by_command_name**(name)  ⇒ Object 
    

    
  
  private

-
  
      .**inherited**(subclass)  ⇒ Object 

  private

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(env)  ⇒ Base 
    

    
  
  
  
    constructor
  
  private

A new instance of Base.

## Constructor Details

###
  
    #**initialize**(env)  ⇒ Base 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns a new instance of Base.

```

26
27
28
29
30
31
```

```
# File 'lib/rubocop/cli/command/base.rb', line 26

def initialize(env)
  @env = env
  @options = env.options
  @config_store = env.config_store
  @paths = env.paths
end

```

## Class Attribute Details

###
  
    .**command_name**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

14
15
16
```

```
# File 'lib/rubocop/cli/command/base.rb', line 14

def command_name
  @command_name
end

```

## Instance Attribute Details

###
  
    #**env**  ⇒ Object  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

9
10
11
```

```
# File 'lib/rubocop/cli/command/base.rb', line 9

def env
  @env
end

```

## Class Method Details

###
  
    .**by_command_name**(name)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

21
22
23
```

```
# File 'lib/rubocop/cli/command/base.rb', line 21

def by_command_name(name)
  @subclasses.detect { |s| s.command_name == name }
end

```

###
  
    .**inherited**(subclass)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

16
17
18
19
```

```
# File 'lib/rubocop/cli/command/base.rb', line 16

def inherited(subclass)
  super
  @subclasses << subclass
end

```
