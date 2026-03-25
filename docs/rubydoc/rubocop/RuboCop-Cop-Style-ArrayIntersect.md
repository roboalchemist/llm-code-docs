# Class: RuboCop::Cop::Style::ArrayIntersect
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Style::ArrayIntersect

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector, TargetRubyVersion
  
    Defined in:
    lib/rubocop/cop/style/array_intersect.rb
  
## Overview

In Ruby 3.1, ‘Array#intersect?` has been added.

This cop identifies places where:

-

‘(array1 & array2).any?`

-

‘(array1.intersection(array2)).any?`

-

‘array1.any? { |elem| array2.member?(elem) }`

-

‘(array1 & array2).count > 0`

-

‘(array1 & array2).size > 0`

can be replaced with ‘array1.intersect?(array2)`.

‘array1.intersect?(array2)` is faster and more readable.

In cases like the following, compatibility is not ensured, so it will not be detected when using block argument.
source,ruby

---

([1] & [1,2]).any? { |x| false }    # => false [1].intersect?() { |x| false } # => true

---

NOTE: Although ‘Array#intersection` can take zero or multiple arguments, only cases where exactly one argument is provided can be replaced with `Array#intersect?` and are handled by this cop.

#### Examples

```
# bad
(array1 & array2).any?
(array1 & array2).empty?
(array1 & array2).none?

# bad
array1.intersection(array2).any?
array1.intersection(array2).empty?
array1.intersection(array2).none?

# bad
array1.any? { |elem| array2.member?(elem) }
array1.none? { |elem| array2.member?(elem) }

# good
array1.intersect?(array2)
!array1.intersect?(array2)

# bad
(array1 & array2).count > 0
(array1 & array2).count.positive?
(array1 & array2).count != 0

(array1 & array2).count == 0
(array1 & array2).count.zero?

# good
array1.intersect?(array2)

!array1.intersect?(array2)
```

#####

AllCops:ActiveSupportExtensionsEnabled: false (default)

```
# good
(array1 & array2).present?
(array1 & array2).blank?
```

#####

AllCops:ActiveSupportExtensionsEnabled: true

```
# bad
(array1 & array2).present?
(array1 & array2).blank?

# good
array1.intersect?(array2)
!array1.intersect?(array2)
```

##

      Constant Summary
      collapse
    

    
      
        PREDICATES =
          
        
        

```
%i[any? empty? none?].to_set.freeze
```

        ACTIVE_SUPPORT_PREDICATES =
          
        
        

```
(PREDICATES + %i[present? blank?]).freeze
```

        ARRAY_SIZE_METHODS =
          
        
        

```
%i[count length size].to_set.freeze
```

        MSG =
          
        
        

```
'Use `%<replacement>s` instead of `%<existing>s`.'
```

        STRAIGHT_METHODS =
          
        
        

```
%i[present? any? > positive? !=].freeze
```

        NEGATED_METHODS =
          
        
        

```
%i[blank? empty? none? == zero?].freeze
```

        RESTRICT_ON_SEND =
          
        
        

```
(STRAIGHT_METHODS + NEGATED_METHODS).freeze
```

## Instance Attribute Summary

### Attributes inherited from Base

# config, #processed_source

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**any_none_block_intersection**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**bad_intersection_check?**(node, predicates)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**intersection_size_check?**(node, predicates)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**on_block**(node)  ⇒ Object 
    

    
      (also: #on_numblock, #on_itblock)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**on_send**(node)  ⇒ Object 
    

    
      (also: #on_csend)
    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods included from AutoCorrector

support_autocorrect?

### Methods included from TargetRubyVersion

maximum_target_ruby_version, minimum_target_ruby_version, required_maximum_ruby_version, required_minimum_ruby_version, support_target_ruby_version?

### Methods inherited from Base

# active_support_extensions_enabled?, #add_global_offense, #add_offense, #always_autocorrect?, autocorrect_incompatible_with, badge, #begin_investigation, #callbacks_needed, callbacks_needed, #config_to_allow_offenses, #config_to_allow_offenses=, #contextual_autocorrect?, #cop_config, #cop_name, cop_name, department, documentation_url, exclude_from_registry, #excluded_file?, #external_dependency_checksum, inherited, #initialize, #inspect, joining_forces, lint?, match?, #message, #offenses, #on_investigation_end, #on_new_investigation, #on_other_file, #parse, #parser_engine, #ready, #relevant_file?, requires_gem, #string_literals_frozen_by_default?, support_autocorrect?, support_multiple_source?, #target_gem_version, #target_rails_version, #target_ruby_version

### Methods included from ExcludeLimit

# exclude_limit

### Methods included from AutocorrectLogic

# autocorrect?, #autocorrect_enabled?, #autocorrect_requested?, #autocorrect_with_disable_uncorrectable?, #correctable?, #disable_uncorrectable?, #safe_autocorrect?

### Methods included from IgnoredNode

# ignore_node, #ignored_node?, #part_of_ignored_node?

### Methods included from Util

silence_warnings

## Constructor Details

This class inherits a constructor from RuboCop::Cop::Base
  
## Instance Method Details

###
  
    #**any_none_block_intersection**(node)  ⇒ Object 
  

  

  

  
    
      

```

119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
```

```
# File 'lib/rubocop/cop/style/array_intersect.rb', line 119

def_node_matcher :any_none_block_intersection, <<~PATTERN
  {
    (block
      (call $_receiver ${:any? :none?})
      (args (arg _key))
      (send $_argument :member? (lvar _key))
    )
    (numblock
      (call $_receiver ${:any? :none?}) 1
      (send $_argument :member? (lvar :_1))
    )
    (itblock
      (call $_receiver ${:any? :none?}) :it
      (send $_argument :member? (lvar :it))
    )
  }
PATTERN
```

###
  
    #**bad_intersection_check?**(node, predicates)  ⇒ Object 
  

  

  

  
    
      

```

94
95
96
97
98
99
100
101
102
```

```
# File 'lib/rubocop/cop/style/array_intersect.rb', line 94

def_node_matcher :bad_intersection_check?, <<~PATTERN
  $(call
    {
      (begin (send $_ :& $_))
      (call $!nil? :intersection $_)
    }
    $%1
  )
PATTERN
```

###
  
    #**intersection_size_check?**(node, predicates)  ⇒ Object 
  

  

  

  
    
      

```

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
```

```
# File 'lib/rubocop/cop/style/array_intersect.rb', line 105

def_node_matcher :intersection_size_check?, <<~PATTERN
  (call
    $(call
      {
        (begin (send $_ :& $_))
        (call $!nil? :intersection $_)
      }
      %ARRAY_SIZE_METHODS
    )
    {$:> (int 0) | $:positive? | $:!= (int 0) | $:== (int 0) | $:zero?}
  )
PATTERN
```

###
  
    #**on_block**(node)  ⇒ Object 
  

  
    Also known as:
    on_numblock, on_itblock
    
  

  

  
    
      

```

154
155
156
157
158
159
160
161
162
```

```
# File 'lib/rubocop/cop/style/array_intersect.rb', line 154

def on_block(node)
  return unless (receiver, method_name, argument = any_none_block_intersection(node))

  dot = node.send_node.loc.dot.source
  bang = method_name == :any? ? '' : '!'
  replacement = "#{bang}#{receiver.source}#{dot}intersect?(#{argument.source})"

  register_offense(node, replacement)
end
```

###
  
    #**on_send**(node)  ⇒ Object 
  

  
    Also known as:
    on_csend
    
  

  

  
    
      

```

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
```

```
# File 'lib/rubocop/cop/style/array_intersect.rb', line 142

def on_send(node)
  return if node.block_literal?
  return unless (dot_node, receiver, argument, method_name = bad_intersection?(node))

  dot = dot_node.loc.dot.source
  bang = straight?(method_name) ? '' : '!'
  replacement = "#{bang}#{receiver.source}#{dot}intersect?(#{argument.source})"

  register_offense(node, replacement)
end
```
