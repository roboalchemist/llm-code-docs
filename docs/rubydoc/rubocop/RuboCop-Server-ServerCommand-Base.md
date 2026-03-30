# Class: RuboCop::Server::ServerCommand::Base
  
  Private

    Inherits:
    
      Object
      
        

          
- Object

- RuboCop::Server::ServerCommand::Base

        show all
      

    Defined in:
    lib/rubocop/server/server_command/base.rb
  
## Overview

  **This class is part of a private API.**
  You should avoid using this class if possible, as it may be removed or be changed in the future.

Abstract base class for server command.

API:

-

private

## Direct Known Subclasses

Exec, Stop

## Defined Under Namespace

      **Modules:** Runner
    
  
    
  

  
    
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**inherited**(child)  ⇒ Object 
    

    
  
  private

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(args, token: '', cwd: Dir.pwd)  ⇒ Base 
    

    
  
  
  
    constructor
  
  private

A new instance of Base.

-
  
      #**run**  ⇒ Object 

  private

## Constructor Details

###
  
    #**initialize**(args, token: '', cwd: Dir.pwd)  ⇒ Base 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns a new instance of Base.

API:

-

private

```

34
35
36
37
38
```

```
# File 'lib/rubocop/server/server_command/base.rb', line 34

def initialize(args, token: '', cwd: Dir.pwd)
  @args = args
  @token = token
  @cwd = cwd
end

```

## Class Method Details

###
  
    .**inherited**(child)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

API:

-

private

```

29
30
31
32
```

```
# File 'lib/rubocop/server/server_command/base.rb', line 29

def self.inherited(child)
  super
  child.prepend Runner
end

```

## Instance Method Details

###
  
    #**run**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

API:

-

private

```

40
```

```
# File 'lib/rubocop/server/server_command/base.rb', line 40

def run; end

```
