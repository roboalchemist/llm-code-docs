# Class: Nokogiri::CSS::Node
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Nokogiri::CSS::Node
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/css/node.rb
  
  

## Overview

  
    

:nodoc:

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        ALLOW_COMBINATOR_ON_SELF =
          
        
        

```
[:DIRECT_ADJACENT_SELECTOR, :FOLLOWING_SELECTOR, :CHILD_SELECTOR]
```

      
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**type**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Get the type of this node.

  

    
      
- 
  
    
      #**value**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Get the value of this node.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**accept**(visitor)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Accept `visitor`.

  

      
        
- 
  
    
      #**find_by_type**(types)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Find a node by type using `types`.

  

      
        
- 
  
    
      #**initialize**(type, value)  ⇒ Node 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Create a new Node with `type` and `value`.

  

      
        
- 
  
    
      #**to_a**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convert to array.

  

      
        
- 
  
    
      #**to_type**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convert to_type.

  

      
        
- 
  
    
      #**to_xpath**(visitor)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convert this CSS node to xpath with `prefix` using `visitor`.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(type, value)  ⇒ Node 
  

  

  

  
    

Create a new Node with `type` and `value`

  

  

  
    
      

```

14
15
16
17
```

    
    
      

```
# File 'lib/nokogiri/css/node.rb', line 14

def initialize(type, value)
  @type = type
  @value = value
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**type**  ⇒ Object 
  

  

  

  
    

Get the type of this node

  

  

  
    
      

```

9
10
11
```

    
    
      

```
# File 'lib/nokogiri/css/node.rb', line 9

def type
  @type
end
```

    
  

    
      
      
      
  
### 
  
    #**value**  ⇒ Object 
  

  

  

  
    

Get the value of this node

  

  

  
    
      

```

11
12
13
```

    
    
      

```
# File 'lib/nokogiri/css/node.rb', line 11

def value
  @value
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**accept**(visitor)  ⇒ Object 
  

  

  

  
    

Accept `visitor`

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/nokogiri/css/node.rb', line 20

def accept(visitor)
  visitor.send(:"visit_#{type.to_s.downcase}", self)
end
```

    
  

    
      
  
### 
  
    #**find_by_type**(types)  ⇒ Object 
  

  

  

  
    

Find a node by type using `types`

  

  

  
    
      

```

36
37
38
39
40
41
42
43
```

    
    
      

```
# File 'lib/nokogiri/css/node.rb', line 36

def find_by_type(types)
  matches = []
  matches << self if to_type == types
  @value.each do |v|
    matches += v.find_by_type(types) if v.respond_to?(:find_by_type)
  end
  matches
end
```

    
  

    
      
  
### 
  
    #**to_a**  ⇒ Object 
  

  

  

  
    

Convert to array

  

  

  
    
      

```

53
54
55
```

    
    
      

```
# File 'lib/nokogiri/css/node.rb', line 53

def to_a
  [@type] + @value.map { |n| n.respond_to?(:to_a) ? n.to_a : [n] }
end
```

    
  

    
      
  
### 
  
    #**to_type**  ⇒ Object 
  

  

  

  
    

Convert to_type

  

  

  
    
      

```

46
47
48
49
50
```

    
    
      

```
# File 'lib/nokogiri/css/node.rb', line 46

def to_type
  [@type] + @value.filter_map do |n|
    n.to_type if n.respond_to?(:to_type)
  end
end
```

    
  

    
      
  
### 
  
    #**to_xpath**(visitor)  ⇒ Object 
  

  

  

  
    

Convert this CSS node to xpath with `prefix` using `visitor`

  

  

  
    
      

```

26
27
28
29
30
31
32
33
```

    
    
      

```
# File 'lib/nokogiri/css/node.rb', line 26

def to_xpath(visitor)
  prefix = if ALLOW_COMBINATOR_ON_SELF.include?(type) && value.first.nil?
    "."
  else
    visitor.prefix
  end
  prefix + visitor.accept(self)
end
```