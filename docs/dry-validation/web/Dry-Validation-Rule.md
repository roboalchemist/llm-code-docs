# Class: Dry::Validation::Rule
  
    Inherits:
    
      Function
      
        

          
- Object

- Function

- Dry::Validation::Rule

        show all
      

    Defined in:
    lib/dry/validation/rule.rb
  
## Overview

Rules capture configuration and evaluator blocks

When a rule is applied, it creates an `Evaluator` using schema result and its block will be evaluated in the context of the evaluator.

See Also:
  
- Contract::ClassInterface#rule

## Instance Attribute Summary collapse

-
  
      #**keys**  ⇒ Array<Symbol, String, Hash> 

      readonly
    
    
  
  private

-
  
      #**macros**  ⇒ Array<Symbol> 

      readonly
    
    
  
  private

### Attributes inherited from Function

# block, #block_options

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**add_macro_from_hash**(macros, spec)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**call**(contract, result)  ⇒ Object 
    

    
  
  private

Evaluate the rule within the provided context.

-
  
      #**each**(*macros, &block)  ⇒ Rule 

Define a validation function for each element of an array.

-
  
      #**inspect**  ⇒ String 

Return a nice string representation.

-
  
      #**parse_macros**(*args)  ⇒ Array 

  private

Parse function arguments into macros structure.

-
  
      #**validate**(*macros, &block)  ⇒ Rule 

Define which macros should be executed.

## Instance Attribute Details

###
  
    #**keys**  ⇒ Array<Symbol, String, Hash>  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Array<Symbol, String, Hash>)

```

21
```

```
# File 'lib/dry/validation/rule.rb', line 21

option :keys
```

###
  
    #**macros**  ⇒ Array<Symbol>  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Array<Symbol>)

```

26
```

```
# File 'lib/dry/validation/rule.rb', line 26

option :macros, default: proc { EMPTY_ARRAY.dup }
```

## Instance Method Details

###
  
    #**add_macro_from_hash**(macros, spec)  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

128
129
130
131
132
```

```
# File 'lib/dry/validation/rule.rb', line 128

def add_macro_from_hash(macros, spec)
  spec.each do |k, v|
    macros << [k, v.is_a?(::Array) ? v : [v]]
  end
end
```

###
  
    #**call**(contract, result)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Evaluate the rule within the provided context

Parameters:

-

        contract

        (Contract)
      
      
      
    
  
    
-

        result
      
      
        (Result)
      
      
      
    
  

  
    
      

```

34
35
36
37
38
39
40
41
42
43
44
45
```

```
# File 'lib/dry/validation/rule.rb', line 34

def call(contract, result)
  Evaluator.new(
    contract,
    keys: keys,
    macros: macros,
    block_options: block_options,
    result: result,
    values: result.values,
    _context: result.context,
    &block
  )
end
```

###
  
    #**each**(*macros, &block)  ⇒ Rule 
  

  

  

  
    

Define a validation function for each element of an array

The function will be applied only if schema checks passed for a given array item.

rubocop:disable Metrics/AbcSize

#### Examples

```
rule(:nums).each do |index:|
  key([:number, index]).failure("must be greater than 0") if value < 0
end
rule(:nums).each(min: 3)
rule(address: :city) do
   key.failure("oops") if value != 'Munich'
end
```

Returns:

-

        (Rule)

```

78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
```

```
# File 'lib/dry/validation/rule.rb', line 78

def each(*macros, &block)
  root = keys[0]
  macros = parse_macros(*macros)
  @keys = []

  @block = proc do
    unless result.base_error?(root) || !values.key?(root) || values[root].nil?
      values[root].each_with_index do |_, idx|
        path = [*Schema::Path[root].to_a, idx]

        next if result.schema_error?(path)

        evaluator = with(macros: macros, keys: [path], index: idx, &block)

        failures.concat(evaluator.failures)
      end
    end
  end

  @block_options = map_keywords(block) if block

  self
end
```

###
  
    #**inspect**  ⇒ String 
  

  

  

  
    

Return a nice string representation

Returns:

-

        (String)

```

108
109
110
```

```
# File 'lib/dry/validation/rule.rb', line 108

def inspect
  %(#<#{self.class} keys=#{keys.inspect}>)
end
```

###
  
    #**parse_macros**(*args)  ⇒ Array 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Parse function arguments into macros structure

Returns:

-

        (Array)

```

117
118
119
120
121
122
123
124
125
126
```

```
# File 'lib/dry/validation/rule.rb', line 117

def parse_macros(*args)
  args.each_with_object([]) do |spec, macros|
    case spec
    when Hash
      add_macro_from_hash(macros, spec)
    else
      macros << Array(spec)
    end
  end
end
```

###
  
    #**validate**(*macros, &block)  ⇒ Rule 
  

  

  

  
    

Define which macros should be executed

Returns:

-

        (Rule)

See Also:
  
- Contract::ClassInterface#rule

```

53
54
55
56
57
```

```
# File 'lib/dry/validation/rule.rb', line 53

def validate(*macros, &block)
  @macros = parse_macros(*macros)
  @block = block if block
  self
end
```
