# Class: RuboCop::Cop::Badge
  
    Inherits:
    
      Object
      
        

          
- Object

- RuboCop::Cop::Badge

        show all
      

    Defined in:
    lib/rubocop/cop/badge.rb
  
## Overview

Identifier of all cops containing a department and cop name.

All cops are identified by their badge. For example, the badge for `RuboCop::Cop::Layout::IndentationStyle` is `Layout/IndentationStyle`. Badges can be parsed as either `Department/CopName` or just `CopName` to allow for badge references in source files that omit the department for RuboCop to infer.

## Instance Attribute Summary collapse

-
  
      #**cop_name**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute cop_name.

-
  
      #**department**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute department.

-
  
      #**department_name**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute department_name.

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**camel_case**(name_part)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**for**(class_name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**parse**(identifier)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**==**(other)  ⇒ Object 
    

    
      (also: #eql?)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**hash**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**initialize**(class_name_parts)  ⇒ Badge 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Badge.

-
  
      #**match?**(other)  ⇒ Boolean 

-
  
      #**qualified?**  ⇒ Boolean 

-
  
      #**to_s**  ⇒ Object 

-
  
      #**with_department**(department)  ⇒ Object 

## Constructor Details

###
  
    #**initialize**(class_name_parts)  ⇒ Badge 
  

  

  

  
    

Returns a new instance of Badge.

```

34
35
36
37
38
39
```

```
# File 'lib/rubocop/cop/badge.rb', line 34

def initialize(class_name_parts)
  department_parts = class_name_parts[0...-1]
  @department = (department_parts.join('/').to_sym unless department_parts.empty?)
  @department_name = @department&.to_s
  @cop_name = class_name_parts.last
end

```

## Instance Attribute Details

###
  
    #**cop_name**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute cop_name.

```

13
14
15
```

```
# File 'lib/rubocop/cop/badge.rb', line 13

def cop_name
  @cop_name
end

```

###
  
    #**department**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute department.

```

13
14
15
```

```
# File 'lib/rubocop/cop/badge.rb', line 13

def department
  @department
end

```

###
  
    #**department_name**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute department_name.

```

13
14
15
```

```
# File 'lib/rubocop/cop/badge.rb', line 13

def department_name
  @department_name
end

```

## Class Method Details

###
  
    .**camel_case**(name_part)  ⇒ Object 
  

  

  

  
    
      

```

27
28
29
30
31
32
```

```
# File 'lib/rubocop/cop/badge.rb', line 27

def self.camel_case(name_part)
  return 'RSpec' if name_part == 'rspec'
  return name_part unless name_part.match?(/^[a-z]|_[a-z]/)

  name_part.gsub(/^[a-z]|_[a-z]/) { |match| match[-1, 1].upcase }
end

```

###
  
    .**for**(class_name)  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
18
19
```

```
# File 'lib/rubocop/cop/badge.rb', line 15

def self.for(class_name)
  parts = class_name.split('::')
  name_deep_enough = parts.length >= 4
  new(name_deep_enough ? parts[2..] : parts.last(2))
end

```

###
  
    .**parse**(identifier)  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
```

```
# File 'lib/rubocop/cop/badge.rb', line 23

def self.parse(identifier)
  @parse_cache[identifier] ||= new(identifier.split('/').map! { |i| camel_case(i) })
end

```

## Instance Method Details

###
  
    #**==**(other)  ⇒ Object 
  

  
    Also known as:
    eql?
    
  

  

  
    
      

```

41
42
43
```

```
# File 'lib/rubocop/cop/badge.rb', line 41

def ==(other)
  hash == other.hash
end

```

###
  
    #**hash**  ⇒ Object 
  

  

  

  
    
      

```

46
47
48
49
```

```
# File 'lib/rubocop/cop/badge.rb', line 46

def hash
  # Do hashing manually to reduce Array allocations.
  department.hash ^ cop_name.hash # rubocop:disable Security/CompoundHash
end

```

###
  
    #**match?**(other)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

51
52
53
```

```
# File 'lib/rubocop/cop/badge.rb', line 51

def match?(other)
  cop_name == other.cop_name && (!qualified? || department == other.department)
end

```

###
  
    #**qualified?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

59
60
61
```

```
# File 'lib/rubocop/cop/badge.rb', line 59

def qualified?
  !department.nil?
end

```

###
  
    #**to_s**  ⇒ Object 
  

  

  

  
    
      

```

55
56
57
```

```
# File 'lib/rubocop/cop/badge.rb', line 55

def to_s
  @to_s ||= qualified? ? "#{department}/#{cop_name}" : cop_name
end

```

###
  
    #**with_department**(department)  ⇒ Object 
  

  

  

  
    
      

```

63
64
65
```

```
# File 'lib/rubocop/cop/badge.rb', line 63

def with_department(department)
  self.class.new([department.to_s.split('/'), cop_name].flatten)
end

```
