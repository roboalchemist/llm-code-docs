# Class: RuboCop::Cop::Style::ParallelAssignment::AssignmentSorter
  
    Inherits:
    
      Object
      
        

          
- Object

- RuboCop::Cop::Style::ParallelAssignment::AssignmentSorter

        show all
      
    
  
  

  
  
  
      Extended by:
      Macros
  
    Defined in:
    lib/rubocop/cop/style/parallel_assignment.rb
  
## Overview

Topologically sorts the assignments with Kahn’s algorithm. en.wikipedia.org/wiki/Topological_sorting#Kahn’s_algorithm

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**accesses?**(rhs, lhs)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

`lhs` is an assignment method call like `obj.attr=` or `ary[idx]=`.

-
  
      #**dependencies_for_assignment**(assignment)  ⇒ Object 

Returns all the assignments which must come after `assignment` (due to dependencies on the previous value of the assigned var).

-
  
      #**dependency?**(lhs, rhs)  ⇒ Boolean 

-
  
      #**initialize**(assignments)  ⇒ AssignmentSorter 

    constructor
  
  
  
  
  
  

  
    

A new instance of AssignmentSorter.

-
  
      #**matching_calls**(node, receiver, method_name)  ⇒ Object 

-
  
      #**tsort**  ⇒ Object 

-
  
      #**uses_var?**(node)  ⇒ Object 

-
  
      #**var_name**(node)  ⇒ Object 

## Constructor Details

###
  
    #**initialize**(assignments)  ⇒ AssignmentSorter 
  

  

  

  
    

Returns a new instance of AssignmentSorter.

```

130
131
132
```

```
# File 'lib/rubocop/cop/style/parallel_assignment.rb', line 130

def initialize(assignments)
  @assignments = assignments
end

```

## Instance Method Details

###
  
    #**accesses?**(rhs, lhs)  ⇒ Boolean 
  

  

  

  
    

`lhs` is an assignment method call like `obj.attr=` or `ary[idx]=`. Does `rhs` access the same value which is assigned by `lhs`?

Returns:

-

        (Boolean)

```

177
178
179
180
181
182
183
184
185
186
187
```

```
# File 'lib/rubocop/cop/style/parallel_assignment.rb', line 177

def accesses?(rhs, lhs)
  if lhs.method?(:[]=)
    # FIXME: Workaround `rubocop:disable` comment for JRuby.
    # rubocop:disable Performance/RedundantEqualityComparisonBlock
    matching_calls(rhs, lhs.receiver, :[]).any? { |args| args == lhs.arguments }
    # rubocop:enable Performance/RedundantEqualityComparisonBlock
  else
    access_method = lhs.method_name.to_s.chop.to_sym
    matching_calls(rhs, lhs.receiver, access_method).any?
  end
end

```

###
  
    #**dependencies_for_assignment**(assignment)  ⇒ Object 
  

  

  

  
    

Returns all the assignments which must come after `assignment` (due to dependencies on the previous value of the assigned var)

```

156
157
158
159
160
161
162
163
164
165
166
167
168
```

```
# File 'lib/rubocop/cop/style/parallel_assignment.rb', line 156

def dependencies_for_assignment(assignment)
  my_lhs, _my_rhs = *assignment

  @assignments.filter_map do |other|
    # Exclude self, there are no dependencies in cases such as `a, b = a, b`.
    next if other == assignment

    _other_lhs, other_rhs = *other
    next unless dependency?(my_lhs, other_rhs)

    other
  end
end

```

###
  
    #**dependency?**(lhs, rhs)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

170
171
172
173
```

```
# File 'lib/rubocop/cop/style/parallel_assignment.rb', line 170

def dependency?(lhs, rhs)
  uses_var?(rhs, var_name(lhs)) ||
    (lhs.send_type? && lhs.assignment_method? && accesses?(rhs, lhs))
end

```

###
  
    #**matching_calls**(node, receiver, method_name)  ⇒ Object 
  

  

  

  
    
      

```

128
```

```
# File 'lib/rubocop/cop/style/parallel_assignment.rb', line 128

def_node_search :matching_calls, '(send %1 %2 $...)'

```

###
  
    #**tsort**  ⇒ Object 
  

  

  

  
    
      

```

134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
```

```
# File 'lib/rubocop/cop/style/parallel_assignment.rb', line 134

def tsort
  dependencies = @assignments.to_h do |assignment|
    [assignment, dependencies_for_assignment(assignment)]
  end
  result = []

  while (matched_node, = dependencies.find { |_node, edges| edges.empty? })
    dependencies.delete(matched_node)
    result.push(matched_node)

    dependencies.each do |node, edges|
      dependencies[node].delete(matched_node) if edges.include?(matched_node)
    end
  end
  # Cyclic dependency
  return nil if dependencies.any?

  result
end

```

###
  
    #**uses_var?**(node)  ⇒ Object 
  

  

  

  
    
      

```

125
```

```
# File 'lib/rubocop/cop/style/parallel_assignment.rb', line 125

def_node_search :uses_var?, '{({lvar ivar cvar gvar} %) (const _ %)}'

```

###
  
    #**var_name**(node)  ⇒ Object 
  

  

  

  
    
      

```

122
```

```
# File 'lib/rubocop/cop/style/parallel_assignment.rb', line 122

def_node_matcher :var_name, '{(casgn _ $_) (_ $_)}'

```
