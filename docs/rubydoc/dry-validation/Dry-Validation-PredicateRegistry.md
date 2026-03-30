# Class: Dry::Validation::PredicateRegistry
  
    Inherits:
    
      Schema::PredicateRegistry
      
        

          
- Object

- Schema::PredicateRegistry

- Dry::Validation::PredicateRegistry

        show all
      

    Defined in:
    lib/dry/validation/extensions/predicates_as_macros.rb
  
## Overview

Predicate registry with additional needed methods.

##

      Constant Summary
      collapse
    

    
      
        WHITELIST =
          
  
    

List of predicates to be imported by `:predicates_as_macros` extension.

See Also:
  
- Contract

```
i[
  filled? format? gt? gteq? included_in? includes? inclusion? is? lt?
  lteq? max_size? min_size? not_eql? odd? respond_to? size? true?
  uuid_v4?
].freeze

```

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**arg_names**(name)  ⇒ Object 
    

    
  
  private

-
  
      #**call**(name, args)  ⇒ Object 

  private

-
  
      #**message_opts**(name, arg_values)  ⇒ Object 

  private

## Instance Method Details

###
  
    #**arg_names**(name)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

18
19
20
```

```
# File 'lib/dry/validation/extensions/predicates_as_macros.rb', line 18

def arg_names(name)
  arg_list(name).map(&:first)
end

```

###
  
    #**call**(name, args)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

23
24
25
```

```
# File 'lib/dry/validation/extensions/predicates_as_macros.rb', line 23

def call(name, args)
  self[name].(*args)
end

```

###
  
    #**message_opts**(name, arg_values)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

28
29
30
```

```
# File 'lib/dry/validation/extensions/predicates_as_macros.rb', line 28

def message_opts(name, arg_values)
  arg_names(name).zip(arg_values).to_h
end

```
