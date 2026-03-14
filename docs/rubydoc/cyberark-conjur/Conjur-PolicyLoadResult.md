# Class: Conjur::PolicyLoadResult
  
    Inherits:
    
      Object
      
        

          
- Object

- Conjur::PolicyLoadResult

        show all
      

    Defined in:
    lib/conjur/policy_load_result.rb
  
## Overview

The result of loading a policy. When a policy is loaded, two types of data
are always provided:

- #created_roles the API keys of any new roles which were created

- #version the new version of the policy.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**created_roles**  ⇒ Hash 
    

    
  
  
  
  
  
  
  
  

  
    

API keys for roles which were created when loading the policy.

-
  
      #**initialize**(data)  ⇒ PolicyLoadResult 

    constructor
  
  
  
  
  
  

  
    

A new instance of PolicyLoadResult.

-
  
      #**version**  ⇒ Object 

The new version of the policy.

## Constructor Details

###
  
    #**initialize**(data)  ⇒ PolicyLoadResult 
  

  

  

  
    

Returns a new instance of PolicyLoadResult.

```

28
29
30
```

```
# File 'lib/conjur/policy_load_result.rb', line 28

def initialize data
  @data = data
end
```

## Instance Method Details

###
  
    #**created_roles**  ⇒ Hash 
  

  

  

  
    

API keys for roles which were created when loading the policy.

Returns:

-

        (Hash)

        —
        

Hash keys are the role ids, and hash values are the API keys.

```

50
51
52
```

```
# File 'lib/conjur/policy_load_result.rb', line 50

def created_roles
  @data['created_roles']
end
```

###
  
    #**version**  ⇒ Object 
  

  

  

  
    

The new version of the policy. When a policy is updated, a new version is appended
to that policy. The YAML of previous versions of the policy can be obtained
by fetching the policy resource using API#resource.

```

57
58
59
```

```
# File 'lib/conjur/policy_load_result.rb', line 57

def version
  @data['version']
end
```
