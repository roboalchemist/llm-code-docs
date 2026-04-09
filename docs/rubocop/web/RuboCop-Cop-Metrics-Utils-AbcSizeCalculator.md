# Class: RuboCop::Cop::Metrics::Utils::AbcSizeCalculator
  
    Inherits:
    
      Object
      
        

          
- Object

- RuboCop::Cop::Metrics::Utils::AbcSizeCalculator

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      IteratingBlock, RepeatedAttributeDiscount, RepeatedCsendDiscount
  
    Defined in:
    lib/rubocop/cop/metrics/utils/abc_size_calculator.rb
  
## Overview

> ABC is .. a software size metric .. computed by counting the number > of assignments, branches and conditions for a section of code. > c2.com/cgi/wiki?AbcMetric

We separate the **calculator** from the **cop** so that the calculation, the formula itself, is easier to test.

## Constant Summary

### Constants included

     from IteratingBlock

IteratingBlock::KNOWN_ITERATING_METHODS

### Constants included

     from RepeatedAttributeDiscount

RepeatedAttributeDiscount::VAR_SETTER_TO_GETTER

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**calculate**(node, discount_repeated_attributes: false)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**calculate**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**else_branch?**(node)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**evaluate_branch_nodes**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**evaluate_condition_node**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**initialize**(node)  ⇒ AbcSizeCalculator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of AbcSizeCalculator.

### Methods included from RepeatedCsendDiscount

# discount_for_repeated_csend?, #reset_on_lvasgn, #reset_repeated_csend

### Methods included from IteratingBlock

# block_method_name, #iterating_block?, #iterating_method?

### Methods included from RepeatedAttributeDiscount

# discount_repeated_attributes?

## Constructor Details

###
  
    #**initialize**(node)  ⇒ AbcSizeCalculator 
  

  

  

  
    

Returns a new instance of AbcSizeCalculator.

```

34
35
36
37
38
39
40
```

```
# File 'lib/rubocop/cop/metrics/utils/abc_size_calculator.rb', line 34

def initialize(node)
  @assignment = 0
  @branch = 0
  @condition = 0
  @node = node
  reset_repeated_csend
end
```

## Class Method Details

###
  
    .**calculate**(node, discount_repeated_attributes: false)  ⇒ Object 
  

  

  

  
    
      

```

30
31
32
```

```
# File 'lib/rubocop/cop/metrics/utils/abc_size_calculator.rb', line 30

def self.calculate(node, discount_repeated_attributes: false)
  new(node, discount_repeated_attributes: discount_repeated_attributes).calculate
end
```

## Instance Method Details

###
  
    #**calculate**  ⇒ Object 
  

  

  

  
    
      

```

42
43
44
45
46
47
48
49
```

```
# File 'lib/rubocop/cop/metrics/utils/abc_size_calculator.rb', line 42

def calculate
  visit_depth_last(@node) { |child| calculate_node(child) }

  [
    Math.sqrt((@assignment**2) + (@branch**2) + (@condition**2)).round(2),
    "<#{@assignment}, #{@branch}, #{@condition}>"
  ]
end
```

###
  
    #**else_branch?**(node)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

65
66
67
```

```
# File 'lib/rubocop/cop/metrics/utils/abc_size_calculator.rb', line 65

def else_branch?(node)
  %i[case if].include?(node.type) && node.else? && node.loc.else.is?('else')
end
```

###
  
    #**evaluate_branch_nodes**(node)  ⇒ Object 
  

  

  

  
    
      

```

51
52
53
54
55
56
57
58
```

```
# File 'lib/rubocop/cop/metrics/utils/abc_size_calculator.rb', line 51

def evaluate_branch_nodes(node)
  if node.comparison_method?
    @condition += 1
  else
    @branch += 1
    @condition += 1 if node.csend_type? && !discount_for_repeated_csend?(node)
  end
end
```

###
  
    #**evaluate_condition_node**(node)  ⇒ Object 
  

  

  

  
    
      

```

60
61
62
63
```

```
# File 'lib/rubocop/cop/metrics/utils/abc_size_calculator.rb', line 60

def evaluate_condition_node(node)
  @condition += 1 if else_branch?(node)
  @condition += 1
end
```
