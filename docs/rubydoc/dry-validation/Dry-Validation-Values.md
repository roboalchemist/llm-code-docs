# Class: Dry::Validation::Values
  
    Inherits:
    
      Object
      
        

          
- Object

- Dry::Validation::Values

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Enumerable
  
    Defined in:
    lib/dry/validation/values.rb
  
## Overview

A convenient wrapper for data processed by schemas

Values are available within the rule blocks. They act as hash-like objects and expose a convenient API for accessing data.

## Instance Attribute Summary collapse

-
  
      #**data**  ⇒ Hash 

      readonly
    
    
  
  private

Schema’s result output.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**[]**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Read from the provided key.

-
  
      #**initialize**(data)  ⇒ Values 

    constructor
  
  private

A new instance of Values.

-
  
      #**key?**(key, hash = data)  ⇒ Boolean 

rubocop: disable Metrics/PerceivedComplexity.

-
  
      #**respond_to_missing?**(meth, include_private = false)  ⇒ Boolean 

  private

## Constructor Details

###
  
    #**initialize**(data)  ⇒ Values 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns a new instance of Values.

```

26
27
28
```

```
# File 'lib/dry/validation/values.rb', line 26

def initialize(data)
  @data = data
end
```

## Dynamic Method Handling

    This class handles dynamic methods through the method_missing method
    
  
  
    
  
###
  
    #**method_missing**(meth)  ⇒ Object  (private)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

90
91
92
93
94
95
96
```

```
# File 'lib/dry/validation/values.rb', line 90

def method_missing(meth, ...)
  if data.respond_to?(meth)
    data.public_send(meth, ...)
  else
    super
  end
end
```

## Instance Attribute Details

###
  
    #**data**  ⇒ Hash  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Schema’s result output

Returns:

-

        (Hash)

```

23
24
25
```

```
# File 'lib/dry/validation/values.rb', line 23

def data
  @data
end
```

## Instance Method Details

###
  
    #**[]**(*args)  ⇒ Object 
  

  

  

  
    

Read from the provided key

#### Examples

```
rule(:age) do
  key.failure('must be > 18') if values[:age] <= 18
end
```

Parameters:

-

        args

        (Symbol, String, Hash, Array<Symbol>)
      
      
      
        —
        

If given as a single Symbol, String, Array or Hash, build a key array using Schema::Path digging for data. If given as positional arguments, use these with Hash#dig on the data directly.

Returns:

-

        (Object)

```

45
46
47
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
# File 'lib/dry/validation/values.rb', line 45

def [](*args)
  return data.dig(*args) if args.size > 1

  case (key = args[0])
  when ::Symbol, ::String, ::Array, ::Hash
    keys = ::Dry::Schema::Path[key].to_a

    return data.dig(*keys) unless keys.last.is_a?(Array)

    last = keys.pop
    vals = self.class.new(data.dig(*keys))
    vals.fetch_values(*last) { nil }
  else
    raise ::ArgumentError, "+key+ must be a valid path specification"
  end
end
```

###
  
    #**key?**(key, hash = data)  ⇒ Boolean 
  

  

  

  
    

rubocop: disable Metrics/PerceivedComplexity

Returns:

-

        (Boolean)

```

64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
```

```
# File 'lib/dry/validation/values.rb', line 64

def key?(key, hash = data)
  return hash.key?(key) if key.is_a?(::Symbol)

  Schema::Path[key].reduce(hash) do |a, e|
    if e.is_a?(::Array)
      return e.all? { |k| key?(k, a) }
    elsif (e.is_a?(::Symbol) && a.is_a?(::Array)) || a.nil? || a.is_a?(::String)
      return false
    else
      return false unless a.is_a?(::Array) ? (e >= 0 && e < a.size) : a.key?(e)
    end

    a[e]
  end
  true
end
```

###
  
    #**respond_to_missing?**(meth, include_private = false)  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Boolean)

```

83
84
85
```

```
# File 'lib/dry/validation/values.rb', line 83

def respond_to_missing?(meth, include_private = false)
  super || data.respond_to?(meth, include_private)
end
```
