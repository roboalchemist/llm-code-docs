# Module: Prawn::TransformationStack
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Document
  
  

  
  
    Defined in:
    lib/prawn/transformation_stack.rb
  
  

## Overview

  
    

Stores the transformations that have been applied to the document.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**add_to_transformation_stack**(a, b, c, d, e, f)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Add transformation to the stack.

  

      
        
- 
  
    
      #**current_transformation_matrix_with_translation**(x = 0, y = 0)  ⇒ Array(Number, Number, Number, Number, Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

Get current transformation matrix.

  

      
        
- 
  
    
      #**restore_transformation_stack**  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Restore previous transformation.

  

      
        
- 
  
    
      #**save_transformation_stack**  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Save transformation stack.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**add_to_transformation_stack**(a, b, c, d, e, f)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Add transformation to the stack.

  

  

Parameters:

  
    
- 
      
        a
      
      
        (Number)
      
      
      
    
  
    
- 
      
        b
      
      
        (Number)
      
      
      
    
  
    
- 
      
        c
      
      
        (Number)
      
      
      
    
  
    
- 
      
        d
      
      
        (Number)
      
      
      
    
  
    
- 
      
        e
      
      
        (Number)
      
      
      
    
  
    
- 
      
        f
      
      
        (Number)
      
      
      
    
  

  
    
      

```

20
21
22
23
```

    
    
      

```
# File 'lib/prawn/transformation_stack.rb', line 20

def add_to_transformation_stack(a, b, c, d, e, f)
  @transformation_stack ||= [[]]
  @transformation_stack.last.push([a, b, c, d, e, f].map { |i| Float(i) })
end

```

    
  

    
      
  
### 
  
    #**current_transformation_matrix_with_translation**(x = 0, y = 0)  ⇒ Array(Number, Number, Number, Number, Number, Number) 
  

  

  

  
    

Get current transformation matrix. It’s a result of multiplication of the whole transformation stack with additional translation.

  

  

Parameters:

  
    
- 
      
        x
      
      
        (Number)
      
      
        *(defaults to: 0)*
      
      
    
  
    
- 
      
        y
      
      
        (Number)
      
      
        *(defaults to: 0)*
      
      
    
  

Returns:

  
    
- 
      
      
        (Array(Number, Number, Number, Number, Number, Number))
      
      
      
    
  

  
    
      

```

48
49
50
51
52
53
54
55
56
57
58
59
60
```

    
    
      

```
# File 'lib/prawn/transformation_stack.rb', line 48

def current_transformation_matrix_with_translation(x = 0, y = 0)
  transformations = (@transformation_stack || [[]]).last

  matrix = Matrix.identity(3)

  transformations.each do |a, b, c, d, e, f|
    matrix *= Matrix[[a, c, e], [b, d, f], [0, 0, 1]]
  end

  matrix *= Matrix[[1, 0, x], [0, 1, y], [0, 0, 1]]

  matrix.to_a[0..1].transpose.flatten
end

```

    
  

    
      
  
### 
  
    #**restore_transformation_stack**  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Restore previous transformation.

Effectively pops the last transformation off of the transformation stack.

  

  

  
    
      

```

38
39
40
```

    
    
      

```
# File 'lib/prawn/transformation_stack.rb', line 38

def restore_transformation_stack
  @transformation_stack&.pop
end

```

    
  

    
      
  
### 
  
    #**save_transformation_stack**  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Save transformation stack.

  

  

  
    
      

```

28
29
30
31
```

    
    
      

```
# File 'lib/prawn/transformation_stack.rb', line 28

def save_transformation_stack
  @transformation_stack ||= [[]]
  @transformation_stack.push(@transformation_stack.last.dup)
end

```