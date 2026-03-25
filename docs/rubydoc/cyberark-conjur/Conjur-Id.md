# Class: Conjur::Id
  
    Inherits:
    
      Object
      
        

          
- Object

- Conjur::Id

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Escape
  
    Defined in:
    lib/conjur/id.rb
  
## Overview

Encapsulates a Conjur id, which consists of account, kind, and identifier.

## Instance Attribute Summary collapse

-
  
      #**id**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute id.

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**normalize**(id)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**==**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Defines id equivalence using the string representation.

-
  
      #**account**  ⇒ Object 

The organization account, obtained from the first component of the id.

-
  
      #**as_json**(options = {})  ⇒ String 

The id string.

-
  
      #**identifier**  ⇒ Object 

The object identifier, obtained from the third component of the id.

-
  
      #**initialize**(id)  ⇒ Id 

    constructor
  
  
  
  
  
  

  
    

A new instance of Id.

-
  
      #**kind**  ⇒ Object 

The object kind, obtained from the second component of the id.

-
  
      #**to_s**  ⇒ String 

The id string.

-
  
      #**to_url_path**  ⇒ Object 

Splits the id into 3 components, and then joins them with a forward-slash `/`.

### Methods included from Escape

# fully_escape, #path_escape, #query_escape

## Constructor Details

###
  
    #**initialize**(id)  ⇒ Id 
  

  

  

  
    

Returns a new instance of Id.

```

26
27
28
```

```
# File 'lib/conjur/id.rb', line 26

def initialize id
  @id = Id.normalize id
end
```

## Instance Attribute Details

###
  
    #**id**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute id.

```

24
25
26
```

```
# File 'lib/conjur/id.rb', line 24

def id
  @id
end
```

## Class Method Details

###
  
    .**normalize**(id)  ⇒ Object 
  

  

  

  
    
      

```

64
65
66
67
68
69
```

```
# File 'lib/conjur/id.rb', line 64

def self.normalize id
  Array(id).join(':').tap do |id|
    raise ArgumentError, "id must be fully qualified: #{id}" \
      unless id =~ /.*:.*:.*/
  end
end
```

## Instance Method Details

###
  
    #**==**(other)  ⇒ Object 
  

  

  

  
    

Defines id equivalence using the string representation.

```

39
40
41
42
43
44
45
```

```
# File 'lib/conjur/id.rb', line 39

def == other
  if other.is_a?(String)
    to_s == other
  else
    super
  end
end
```

###
  
    #**account**  ⇒ Object 
  

  

  

  
    

The organization account, obtained from the first component of the id.

```

31
```

```
# File 'lib/conjur/id.rb', line 31

def account; id.split(':', 3)[0]; end
```

###
  
    #**as_json**(options = {})  ⇒ String 
  

  

  

  
    

Returns the id string.

Returns:

-

the id string.

```

48
49
50
```

```
# File 'lib/conjur/id.rb', line 48

def as_json options={}
  @id
end
```

###
  
    #**identifier**  ⇒ Object 
  

  

  

  
    

The object identifier, obtained from the third component of the id. The
identifier must be unique within the `account` and `kind`.

```

36
```

```
# File 'lib/conjur/id.rb', line 36

def identifier; id.split(':', 3)[2]; end
```

###
  
    #**kind**  ⇒ Object 
  

  

  

  
    

The object kind, obtained from the second component of the id.

```

33
```

```
# File 'lib/conjur/id.rb', line 33

def kind; id.split(':', 3)[1]; end
```

###
  
    #**to_s**  ⇒ String 
  

  

  

  
    

Returns the id string.

Returns:

-

the id string

```

60
61
62
```

```
# File 'lib/conjur/id.rb', line 60

def to_s
  id
end
```

###
  
    #**to_url_path**  ⇒ Object 
  

  

  

  
    

Splits the id into 3 components, and then joins them with a forward-slash `/`.

```

53
54
55
56
57
```

```
# File 'lib/conjur/id.rb', line 53

def to_url_path
  id.split(':', 3)
    .map(&method(:fully_escape))
    .join('/')
end
```
