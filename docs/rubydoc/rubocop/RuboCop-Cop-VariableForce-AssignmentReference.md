# Class: RuboCop::Cop::VariableForce::AssignmentReference
  
  Private

    Inherits:
    
      Struct
      
        

          
- Object

- Struct

- RuboCop::Cop::VariableForce::AssignmentReference

        show all
      

    Defined in:
    lib/rubocop/cop/variable_force.rb
  
  **This class is part of a private API.**
  You should avoid using this class if possible, as it may be removed or be changed in the future.

## Instance Attribute Summary collapse

-
  
      #**node**  ⇒ Object 

Returns the value of attribute node.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**assignment?**  ⇒ Boolean 
    

    
  
  private

## Instance Attribute Details

###
  
    #**node**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute node

Returns:

-

        (Object)

        —
        

the current value of node

```

68
69
70
```

```
# File 'lib/rubocop/cop/variable_force.rb', line 68

def node
  @node
end
```

## Instance Method Details

###
  
    #**assignment?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Boolean)

```

69
70
71
```

```
# File 'lib/rubocop/cop/variable_force.rb', line 69

def assignment?
  true
end
```
