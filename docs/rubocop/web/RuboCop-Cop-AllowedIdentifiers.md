# Module: RuboCop::Cop::AllowedIdentifiers
  
    Included in:
    Naming::VariableName, Naming::VariableNumber
  
  

  
  
    Defined in:
    lib/rubocop/cop/mixin/allowed_identifiers.rb
  
## Overview

This module encapsulates the ability to allow certain identifiers in a cop.

##

      Constant Summary
      collapse
    

    
      
        SIGILS =
          
  
    

if a variable starts with a sigil it will be removed

```
'@$'

```

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**allowed_identifier?**(name)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**allowed_identifiers**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

###
  
    #**allowed_identifier?**(name)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

```

9
10
11
```

```
# File 'lib/rubocop/cop/mixin/allowed_identifiers.rb', line 9

def allowed_identifier?(name)
  !allowed_identifiers.empty? && allowed_identifiers.include?(name.to_s.delete(SIGILS))
end

```

###
  
    #**allowed_identifiers**  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
```

```
# File 'lib/rubocop/cop/mixin/allowed_identifiers.rb', line 13

def allowed_identifiers
  cop_config.fetch('AllowedIdentifiers') { [] }
end

```
