# Class: RuboCop::Cop::HashTransformMethod::Autocorrection
  
    Inherits:
    
      Struct
      
        

          
- Object

- Struct

- RuboCop::Cop::HashTransformMethod::Autocorrection

        show all
      

    Defined in:
    lib/rubocop/cop/mixin/hash_transform_method/autocorrection.rb
  
## Overview

Internal helper class to hold autocorrect data

## Instance Attribute Summary collapse

-
  
      #**block_node**  ⇒ Object 

Returns the value of attribute block_node.

-
  
      #**leading**  ⇒ Object 

Returns the value of attribute leading.

-
  
      #**match**  ⇒ Object 

Returns the value of attribute match.

-
  
      #**trailing**  ⇒ Object 

Returns the value of attribute trailing.

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**from_each_with_object**(node, match)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**from_hash_brackets_map**(node, match)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**from_map_to_h**(node, match)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**from_to_h**(node, match)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**set_new_arg_name**(transformed_argname, corrector)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**set_new_body_expression**(transforming_body_expr, corrector)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**set_new_method_name**(new_method_name, corrector)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**strip_prefix_and_suffix**(node, corrector)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
    
## Instance Attribute Details

###
  
    #**block_node**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute block_node

Returns:

-

        (Object)

        —
        

the current value of block_node

```

7
8
9
```

```
# File 'lib/rubocop/cop/mixin/hash_transform_method/autocorrection.rb', line 7

def block_node
  @block_node
end
```

###
  
    #**leading**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute leading

Returns:

-

        (Object)

        —
        

the current value of leading

```

7
8
9
```

```
# File 'lib/rubocop/cop/mixin/hash_transform_method/autocorrection.rb', line 7

def leading
  @leading
end
```

###
  
    #**match**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute match

Returns:

-

        (Object)

        —
        

the current value of match

```

7
8
9
```

```
# File 'lib/rubocop/cop/mixin/hash_transform_method/autocorrection.rb', line 7

def match
  @match
end
```

###
  
    #**trailing**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute trailing

Returns:

-

        (Object)

        —
        

the current value of trailing

```

7
8
9
```

```
# File 'lib/rubocop/cop/mixin/hash_transform_method/autocorrection.rb', line 7

def trailing
  @trailing
end
```

## Class Method Details

###
  
    .**from_each_with_object**(node, match)  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
```

```
# File 'lib/rubocop/cop/mixin/hash_transform_method/autocorrection.rb', line 8

def self.from_each_with_object(node, match)
  new(match, node, 0, 0)
end
```

###
  
    .**from_hash_brackets_map**(node, match)  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
```

```
# File 'lib/rubocop/cop/mixin/hash_transform_method/autocorrection.rb', line 12

def self.from_hash_brackets_map(node, match)
  new(match, node.children.last, 'Hash['.length, ']'.length)
end
```

###
  
    .**from_map_to_h**(node, match)  ⇒ Object 
  

  

  

  
    
      

```

16
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
```

```
# File 'lib/rubocop/cop/mixin/hash_transform_method/autocorrection.rb', line 16

def self.from_map_to_h(node, match)
  if node.parent&.block_type? && node.parent.send_node == node
    strip_trailing_chars = 0
  else
    map_range = node.children.first.source_range
    node_range = node.source_range
    strip_trailing_chars = node_range.end_pos - map_range.end_pos
  end

  new(match, node.children.first, 0, strip_trailing_chars)
end
```

###
  
    .**from_to_h**(node, match)  ⇒ Object 
  

  

  

  
    
      

```

28
29
30
```

```
# File 'lib/rubocop/cop/mixin/hash_transform_method/autocorrection.rb', line 28

def self.from_to_h(node, match)
  new(match, node, 0, 0)
end
```

## Instance Method Details

###
  
    #**set_new_arg_name**(transformed_argname, corrector)  ⇒ Object 
  

  

  

  
    
      

```

48
49
50
```

```
# File 'lib/rubocop/cop/mixin/hash_transform_method/autocorrection.rb', line 48

def set_new_arg_name(transformed_argname, corrector)
  corrector.replace(block_node.arguments, "|#{transformed_argname}|")
end
```

###
  
    #**set_new_body_expression**(transforming_body_expr, corrector)  ⇒ Object 
  

  

  

  
    
      

```

52
53
54
55
56
57
58
59
```

```
# File 'lib/rubocop/cop/mixin/hash_transform_method/autocorrection.rb', line 52

def set_new_body_expression(transforming_body_expr, corrector)
  body_source = transforming_body_expr.source
  if transforming_body_expr.hash_type? && !transforming_body_expr.braces?
    body_source = "{ #{body_source} }"
  end

  corrector.replace(block_node.body, body_source)
end
```

###
  
    #**set_new_method_name**(new_method_name, corrector)  ⇒ Object 
  

  

  

  
    
      

```

38
39
40
41
42
43
44
45
46
```

```
# File 'lib/rubocop/cop/mixin/hash_transform_method/autocorrection.rb', line 38

def set_new_method_name(new_method_name, corrector)
  range = block_node.send_node.loc.selector
  if (send_end = block_node.send_node.loc.end)
    # If there are arguments (only true in the `each_with_object`
    # case)
    range = range.begin.join(send_end)
  end
  corrector.replace(range, new_method_name)
end
```

###
  
    #**strip_prefix_and_suffix**(node, corrector)  ⇒ Object 
  

  

  

  
    
      

```

32
33
34
35
36
```

```
# File 'lib/rubocop/cop/mixin/hash_transform_method/autocorrection.rb', line 32

def strip_prefix_and_suffix(node, corrector)
  expression = node.source_range
  corrector.remove_leading(expression, leading)
  corrector.remove_trailing(expression, trailing)
end
```
