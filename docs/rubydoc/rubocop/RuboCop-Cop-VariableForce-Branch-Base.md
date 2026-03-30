# Class: RuboCop::Cop::VariableForce::Branch::Base
  
  Private

    Inherits:
    
      Struct
      
        

          
- Object

- Struct

- RuboCop::Cop::VariableForce::Branch::Base

        show all
      

    Defined in:
    lib/rubocop/cop/variable_force/branch.rb
  
## Overview

  **This class is part of a private API.**
  You should avoid using this class if possible, as it may be removed or be changed in the future.

Abstract base class for branch classes. A branch represents a conditional branch in a scope.

#### Examples

```
def some_scope
  do_something     # no branch

  if foo
    do_something   # branch A
    do_something   # branch A
  else
    do_something   # branch B
    if bar
      do_something # branch C (whose parent is branch B)
    end
  end

  do_something     # no branch
end
```

## Direct Known Subclasses

And, AndAsgn, Case, CaseMatch, Ensure, For, If, OpAsgn, Or, OrAsgn, Rescue, Until, UntilPost, While, WhilePost

## Instance Attribute Summary collapse

-
  
      #**child_node**  ⇒ Object 

Returns the value of attribute child_node.

-
  
      #**scope**  ⇒ Object 

Returns the value of attribute scope.

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**classes**  ⇒ Object 
    

    
  
  private

-
  
      .**define_predicate**(name, child_index: nil)  ⇒ Object 

  private

-
  
      .**inherited**(subclass)  ⇒ Object 

  private

-
  
      .**type**  ⇒ Object 

  private

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**==**(other)  ⇒ Object 
    

    
      (also: #eql?)
    
  
  private

-
  
      #**always_run?**  ⇒ Boolean 

  private

-
  
      #**branched?**  ⇒ Boolean 

  private

-
  
      #**control_node**  ⇒ Object 

  private

-
  
      #**each_ancestor**(include_self: false) {|_self| ... } ⇒ Object 

  private

-
  
      #**exclusive_with?**(other)  ⇒ Boolean 

  private

-
  
      #**hash**  ⇒ Object 

  private

-
  
      #**may_jump_to_other_branch?**  ⇒ Boolean 

  private

-
  
      #**may_run_incompletely?**  ⇒ Boolean 

  private

-
  
      #**parent**  ⇒ Object 

  private

## Instance Attribute Details

###
  
    #**child_node**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute child_node

Returns:

-

        (Object)

        —
        

the current value of child_node

```

42
43
44
```

```
# File 'lib/rubocop/cop/variable_force/branch.rb', line 42

def child_node
  @child_node
end
```

###
  
    #**scope**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute scope

Returns:

-

        (Object)

        —
        

the current value of scope

```

42
43
44
```

```
# File 'lib/rubocop/cop/variable_force/branch.rb', line 42

def scope
  @scope
end
```

## Class Method Details

###
  
    .**classes**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

43
44
45
```

```
# File 'lib/rubocop/cop/variable_force/branch.rb', line 43

def self.classes
  @classes ||= []
end
```

###
  
    .**define_predicate**(name, child_index: nil)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

56
57
58
59
60
61
62
63
64
65
66
67
68
```

```
# File 'lib/rubocop/cop/variable_force/branch.rb', line 56

def self.define_predicate(name, child_index: nil)
  define_method(name) do
    target_node = control_node.children[child_index]

    # We don't use Kernel#Array here
    # because it invokes Node#to_a rather than wrapping with an array.
    if target_node.is_a?(Array)
      target_node.any? { |node| node.equal?(child_node) }
    else
      target_node.equal?(child_node)
    end
  end
end
```

###
  
    .**inherited**(subclass)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

47
48
49
50
```

```
# File 'lib/rubocop/cop/variable_force/branch.rb', line 47

def self.inherited(subclass)
  super
  classes << subclass
end
```

###
  
    .**type**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

52
53
54
```

```
# File 'lib/rubocop/cop/variable_force/branch.rb', line 52

def self.type
  name.split('::').last.gsub(/(.)([A-Z])/, '\1_\2').downcase.to_sym
end
```

## Instance Method Details

###
  
    #**==**(other)  ⇒ Object 
  

  
    Also known as:
    eql?
    
  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

121
122
123
124
125
```

```
# File 'lib/rubocop/cop/variable_force/branch.rb', line 121

def ==(other)
  return false unless other

  control_node.equal?(other.control_node) && child_node.equal?(other.child_node)
end
```

###
  
    #**always_run?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Boolean)

Raises:

-

        (NotImplementedError)

```

92
93
94
```

```
# File 'lib/rubocop/cop/variable_force/branch.rb', line 92

def always_run?
  raise NotImplementedError
end
```

###
  
    #**branched?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Boolean)

```

88
89
90
```

```
# File 'lib/rubocop/cop/variable_force/branch.rb', line 88

def branched?
  !always_run?
end
```

###
  
    #**control_node**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

70
71
72
```

```
# File 'lib/rubocop/cop/variable_force/branch.rb', line 70

def control_node
  child_node.parent
end
```

###
  
    #**each_ancestor**(include_self: false) {|_self| ... } ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Yields:

-

        (_self)

Yield Parameters:

-

        _self

        (RuboCop::Cop::VariableForce::Branch::Base)
      
      
      
        —
        

the object that the method was called on

```

80
81
82
83
84
85
86
```

```
# File 'lib/rubocop/cop/variable_force/branch.rb', line 80

def each_ancestor(include_self: false, &block)
  return to_enum(__method__, include_self: include_self) unless block

  yield self if include_self
  scan_ancestors(&block)
  self
end
```

###
  
    #**exclusive_with?**(other)  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Boolean)

```

104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
```

```
# File 'lib/rubocop/cop/variable_force/branch.rb', line 104

def exclusive_with?(other)
  return false unless other
  return false if may_jump_to_other_branch?

  other.each_ancestor(include_self: true) do |other_ancestor|
    if control_node.equal?(other_ancestor.control_node)
      return !child_node.equal?(other_ancestor.child_node)
    end
  end

  if parent
    parent.exclusive_with?(other)
  else
    false
  end
end
```

###
  
    #**hash**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

129
130
131
```

```
# File 'lib/rubocop/cop/variable_force/branch.rb', line 129

def hash
  [control_node.object_id, control_node.object_id].hash
end
```

###
  
    #**may_jump_to_other_branch?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Boolean)

```

96
97
98
```

```
# File 'lib/rubocop/cop/variable_force/branch.rb', line 96

def may_jump_to_other_branch?
  false
end
```

###
  
    #**may_run_incompletely?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Boolean)

```

100
101
102
```

```
# File 'lib/rubocop/cop/variable_force/branch.rb', line 100

def may_run_incompletely?
  false
end
```

###
  
    #**parent**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

74
75
76
77
78
```

```
# File 'lib/rubocop/cop/variable_force/branch.rb', line 74

def parent
  return @parent if instance_variable_defined?(:@parent)

  @parent = Branch.of(control_node, scope: scope)
end
```
