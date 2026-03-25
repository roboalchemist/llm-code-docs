# Class: RuboCop::Cop::VariableForce::Assignment
  
  Private

    Inherits:
    
      Object
      
        

          
- Object

- RuboCop::Cop::VariableForce::Assignment

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Branchable
  
    Defined in:
    lib/rubocop/cop/variable_force/assignment.rb
  
## Overview

  **This class is part of a private API.**
  You should avoid using this class if possible, as it may be removed or be changed in the future.

This class represents each assignment of a variable.

##

      Constant Summary
      collapse
    

    
      
        MULTIPLE_LEFT_HAND_SIDE_TYPE =
          
  
    

  **This constant is part of a private API.**
  You should avoid using this constant if possible, as it may be removed or be changed in the future.

```
:mlhs
```

## Instance Attribute Summary collapse

-
  
      #**node**  ⇒ Object 

      readonly
    
    
  
  private

-
  
      #**reassigned**  ⇒ Object 

      (also: #reassigned?)
    
  
  
  
  
    
      readonly
    
    
  
  private

-
  
      #**referenced**  ⇒ Object 

      (also: #referenced?)
    
  
  
  
  
    
      readonly
    
    
  
  private

-
  
      #**references**  ⇒ Object 

      readonly
    
    
  
  private

-
  
      #**variable**  ⇒ Object 

      readonly
    
    
  
  private

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**exception_assignment?**  ⇒ Boolean 
    

    
  
  private

-
  
      #**for_assignment?**  ⇒ Boolean 

  private

-
  
      #**initialize**(node, variable)  ⇒ Assignment 

    constructor
  
  private

A new instance of Assignment.

-
  
      #**meta_assignment_node**  ⇒ Object 

  private

-
  
      #**multiple_assignment?**  ⇒ Boolean 

  private

-
  
      #**name**  ⇒ Object 

  private

-
  
      #**operator**  ⇒ Object 

  private

-
  
      #**operator_assignment?**  ⇒ Boolean 

  private

-
  
      #**reassigned!**  ⇒ Object 

  private

-
  
      #**reference!**(node)  ⇒ Object 

  private

-
  
      #**regexp_named_capture?**  ⇒ Boolean 

  private

-
  
      #**rest_assignment?**  ⇒ Boolean 

  private

-
  
      #**scope**  ⇒ Object 

  private

-
  
      #**used?**  ⇒ Boolean 

  private

### Methods included from Branchable

# branch, #run_exclusively_with?

## Constructor Details

###
  
    #**initialize**(node, variable)  ⇒ Assignment 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns a new instance of Assignment.

```

17
18
19
20
21
22
23
24
25
26
27
28
29
```

```
# File 'lib/rubocop/cop/variable_force/assignment.rb', line 17

def initialize(node, variable)
  unless VARIABLE_ASSIGNMENT_TYPES.include?(node.type)
    raise ArgumentError,
          "Node type must be any of #{VARIABLE_ASSIGNMENT_TYPES}, " \
          "passed #{node.type}"
  end

  @node = node
  @variable = variable
  @referenced = false
  @references = []
  @reassigned = false
end
```

## Instance Attribute Details

###
  
    #**node**  ⇒ Object  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

12
13
14
```

```
# File 'lib/rubocop/cop/variable_force/assignment.rb', line 12

def node
  @node
end
```

###
  
    #**reassigned**  ⇒ Object  (readonly)
  

  
    Also known as:
    reassigned?
    
  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

12
13
14
```

```
# File 'lib/rubocop/cop/variable_force/assignment.rb', line 12

def reassigned
  @reassigned
end
```

###
  
    #**referenced**  ⇒ Object  (readonly)
  

  
    Also known as:
    referenced?
    
  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

12
13
14
```

```
# File 'lib/rubocop/cop/variable_force/assignment.rb', line 12

def referenced
  @referenced
end
```

###
  
    #**references**  ⇒ Object  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

12
13
14
```

```
# File 'lib/rubocop/cop/variable_force/assignment.rb', line 12

def references
  @references
end
```

###
  
    #**variable**  ⇒ Object  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

12
13
14
```

```
# File 'lib/rubocop/cop/variable_force/assignment.rb', line 12

def variable
  @variable
end
```

## Instance Method Details

###
  
    #**exception_assignment?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Boolean)

```

58
59
60
```

```
# File 'lib/rubocop/cop/variable_force/assignment.rb', line 58

def exception_assignment?
  node.parent&.resbody_type? && node.parent.exception_variable == node
end
```

###
  
    #**for_assignment?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Boolean)

```

80
81
82
83
84
```

```
# File 'lib/rubocop/cop/variable_force/assignment.rb', line 80

def for_assignment?
  return false unless meta_assignment_node

  meta_assignment_node.for_type?
end
```

###
  
    #**meta_assignment_node**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

91
92
93
94
95
96
97
98
99
100
```

```
# File 'lib/rubocop/cop/variable_force/assignment.rb', line 91

def meta_assignment_node
  unless instance_variable_defined?(:@meta_assignment_node)
    @meta_assignment_node = operator_assignment_node ||
                            multiple_assignment_node ||
                            rest_assignment_node ||
                            for_assignment_node
  end

  @meta_assignment_node
end
```

###
  
    #**multiple_assignment?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Boolean)

```

68
69
70
71
72
```

```
# File 'lib/rubocop/cop/variable_force/assignment.rb', line 68

def multiple_assignment?
  return false unless meta_assignment_node

  meta_assignment_node.type == MULTIPLE_ASSIGNMENT_TYPE
end
```

###
  
    #**name**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

31
32
33
```

```
# File 'lib/rubocop/cop/variable_force/assignment.rb', line 31

def name
  @node.children.first
end
```

###
  
    #**operator**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

86
87
88
89
```

```
# File 'lib/rubocop/cop/variable_force/assignment.rb', line 86

def operator
  assignment_node = meta_assignment_node || @node
  assignment_node.loc.operator.source
end
```

###
  
    #**operator_assignment?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Boolean)

```

62
63
64
65
66
```

```
# File 'lib/rubocop/cop/variable_force/assignment.rb', line 62

def operator_assignment?
  return false unless meta_assignment_node

  OPERATOR_ASSIGNMENT_TYPES.include?(meta_assignment_node.type)
end
```

###
  
    #**reassigned!**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

44
45
46
47
48
```

```
# File 'lib/rubocop/cop/variable_force/assignment.rb', line 44

def reassigned!
  return if referenced?

  @reassigned = true
end
```

###
  
    #**reference!**(node)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

39
40
41
42
```

```
# File 'lib/rubocop/cop/variable_force/assignment.rb', line 39

def reference!(node)
  @references << node
  @referenced = true
end
```

###
  
    #**regexp_named_capture?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Boolean)

```

54
55
56
```

```
# File 'lib/rubocop/cop/variable_force/assignment.rb', line 54

def regexp_named_capture?
  @node.type == REGEXP_NAMED_CAPTURE_TYPE
end
```

###
  
    #**rest_assignment?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Boolean)

```

74
75
76
77
78
```

```
# File 'lib/rubocop/cop/variable_force/assignment.rb', line 74

def rest_assignment?
  return false unless meta_assignment_node

  meta_assignment_node.type == REST_ASSIGNMENT_TYPE
end
```

###
  
    #**scope**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

35
36
37
```

```
# File 'lib/rubocop/cop/variable_force/assignment.rb', line 35

def scope
  @variable.scope
end
```

###
  
    #**used?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Boolean)

```

50
51
52
```

```
# File 'lib/rubocop/cop/variable_force/assignment.rb', line 50

def used?
  (!reassigned? && @variable.captured_by_block?) || @referenced
end
```
