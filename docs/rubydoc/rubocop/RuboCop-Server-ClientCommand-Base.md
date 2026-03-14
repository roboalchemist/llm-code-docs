# Class: RuboCop::Server::ClientCommand::Base
  
  Private

    Inherits:
    
      Object
      
        

          
- Object

- RuboCop::Server::ClientCommand::Base

        show all
      

    Defined in:
    lib/rubocop/server/client_command/base.rb
  
## Overview

  **This class is part of a private API.**
  You should avoid using this class if possible, as it may be removed or be changed in the future.

Abstract base class for server client command.

## Direct Known Subclasses

Exec, Restart, Start, Status, Stop

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**args_config_file_path**  ⇒ Object 
    

    
  
  private

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**run**  ⇒ Object 
    

    
  
  private

## Class Method Details

###
  
    .**args_config_file_path**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

43
44
45
46
47
48
49
```

```
# File 'lib/rubocop/server/client_command/base.rb', line 43

def args_config_file_path
  first_args_config_key_index = ARGV.index { |value| ['-c', '--config'].include?(value) }

  return if first_args_config_key_index.nil?

  ARGV[first_args_config_key_index + 1]
end
```

## Instance Method Details

###
  
    #**run**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Raises:

-

        (NotImplementedError)

```

21
22
23
```

```
# File 'lib/rubocop/server/client_command/base.rb', line 21

def run
  raise NotImplementedError
end
```
