# Class: Dry::Validation::Result
  
    Inherits:
    
      Object
      
        

          
- Object

- Dry::Validation::Result

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Monads::Result::Mixin, Hints::ResultExtensions
  
    Defined in:
    lib/dry/validation/result.rb,

  lib/dry/validation/extensions/monads.rb

## Overview

Monad extension for contract results

#### Examples

```
Dry::Validation.load_extensions(:monads)

contract = Dry::Validation::Contract.build do
  schema do
    required(:name).filled(:string)
  end
end

contract.call(name: nil).to_monad
```

## Instance Attribute Summary collapse

-
  
      #**context**  ⇒ Concurrent::Map 

      readonly
    
    
  
  
  
  
  

  
    

Context that’s shared between rules.

-
  
      #**options**  ⇒ Hash 

      readonly
    
    
  
  private

Result options.

-
  
      #**schema_result**  ⇒ Dry::Schema::Result 

      readonly
    
    
  
  private

Result from contract’s schema.

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**new**(schema_result, context = ::Concurrent::Map.new, options = EMPTY_HASH) {|result| ... } ⇒ Object 
    

    
  
  private

Build a new result.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**[]**(key)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Read a value under provided key.

-
  
      #**add_error**(error)  ⇒ Object 

  private

Add a new error for the provided key.

-
  
      #**base_error?**(key)  ⇒ Boolean 

  private

Check if there’s any error for the provided key.

-
  
      #**base_rule_error?**  ⇒ Boolean 

  private

Check if the result contains any base rule errors.

-
  
      #**deconstruct**  ⇒ Object 

  private

Pattern matching.

-
  
      #**deconstruct_keys**(keys)  ⇒ Object 

  private

Pattern matching.

-
  
      #**error?**(key)  ⇒ Boolean 

Check if values include an error for the provided key.

-
  
      #**errors**(new_options = EMPTY_HASH)  ⇒ MessageSet 

Get error set.

-
  
      #**failure?**  ⇒ Bool 

Check if result is not successful.

-
  
      #**freeze**  ⇒ Object 

  private

Freeze result and its error set.

-
  
      #**initialize**(schema_result, context, options)  ⇒ Result 

    constructor
  
  private

Initialize a new result.

-
  
      #**inspect**  ⇒ Object 

Return a string representation.

-
  
      #**key?**(key)  ⇒ Bool 

Check if a key was set.

-
  
      #**rule_error?**(key)  ⇒ Boolean 

  private

Check if the rules includes an error for the provided key.

-
  
      #**schema_error?**(key)  ⇒ Boolean 

  private

Check if the base schema (without rules) includes an error for the provided key.

-
  
      #**success?**  ⇒ Bool 

Check if result is successful.

-
  
      #**to_h**  ⇒ Object 

Coerce to a hash.

-
  
      #**to_monad**  ⇒ Dry::Monads::Result 

Returns a result monad.

-
  
      #**values**  ⇒ Values 

Return values wrapper with the input processed by schema.

### Methods included from Hints::ResultExtensions

# hints, #messages

## Constructor Details

###
  
    #**initialize**(schema_result, context, options)  ⇒ Result 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Initialize a new result

```

50
51
52
53
54
55
```

```
# File 'lib/dry/validation/result.rb', line 50

def initialize(schema_result, context, options)
  @schema_result = schema_result
  @context = context
  @options = options
  @errors = initialize_errors
end
```

## Instance Attribute Details

###
  
    #**context**  ⇒ Concurrent::Map  (readonly)
  

  

  

  
    

Context that’s shared between rules

Returns:

-

        (Concurrent::Map)

```

31
32
33
```

```
# File 'lib/dry/validation/result.rb', line 31

def context
  @context
end
```

###
  
    #**options**  ⇒ Hash  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Result options

Returns:

-

        (Hash)

```

45
46
47
```

```
# File 'lib/dry/validation/result.rb', line 45

def options
  @options
end
```

###
  
    #**schema_result**  ⇒ Dry::Schema::Result  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Result from contract’s schema

Returns:

-

        (Dry::Schema::Result)

```

38
39
40
```

```
# File 'lib/dry/validation/result.rb', line 38

def schema_result
  @schema_result
end
```

## Class Method Details

###
  
    .**new**(schema_result, context = ::Concurrent::Map.new, options = EMPTY_HASH) {|result| ... } ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Build a new result

Parameters:

-

        schema_result

        (Dry::Schema::Result)
      
      
      
    
  
Yields:

-

        (result)

```

20
21
22
23
24
```

```
# File 'lib/dry/validation/result.rb', line 20

def self.new(schema_result, context = ::Concurrent::Map.new, options = EMPTY_HASH)
  result = super
  yield(result) if block_given?
  result.freeze
end
```

## Instance Method Details

###
  
    #**[]**(key)  ⇒ Object 
  

  

  

  
    

Read a value under provided key

Parameters:

-

        key

        (Symbol)
      
      
      
    
  
Returns:

-

        (Object)

```

158
159
160
```

```
# File 'lib/dry/validation/result.rb', line 158

def [](key)
  values[key]
end
```

###
  
    #**add_error**(error)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Add a new error for the provided key

```

146
147
148
149
```

```
# File 'lib/dry/validation/result.rb', line 146

def add_error(error)
  @errors.add(error)
  self
end
```

###
  
    #**base_error?**(key)  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Check if there’s any error for the provided key

This does not consider errors from the nested values

Returns:

-

        (Boolean)

```

132
133
134
135
136
137
138
139
140
141
```

```
# File 'lib/dry/validation/result.rb', line 132

def base_error?(key)
  schema_result.errors.any? { |error|
    key_path = Schema::Path[key]
    err_path = Schema::Path[error.path]

    next unless key_path.same_root?(err_path)

    key_path == err_path
  }
end
```

###
  
    #**base_rule_error?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Check if the result contains any base rule errors

Returns:

-

        (Boolean)

```

123
124
125
```

```
# File 'lib/dry/validation/result.rb', line 123

def base_rule_error?
  !errors.filter(:base?).empty?
end
```

###
  
    #**deconstruct**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Pattern matching

```

210
211
212
```

```
# File 'lib/dry/validation/result.rb', line 210

def deconstruct
  [values, context.each.to_h]
end
```

###
  
    #**deconstruct_keys**(keys)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Pattern matching

```

203
204
205
```

```
# File 'lib/dry/validation/result.rb', line 203

def deconstruct_keys(keys)
  values.deconstruct_keys(keys)
end
```

###
  
    #**error?**(key)  ⇒ Boolean 
  

  

  

  
    

Check if values include an error for the provided key

Returns:

-

        (Boolean)

```

102
103
104
```

```
# File 'lib/dry/validation/result.rb', line 102

def error?(key)
  errors.any? { |msg| Schema::Path[msg.path].include?(Schema::Path[key]) }
end
```

###
  
    #**errors**(new_options = EMPTY_HASH)  ⇒ MessageSet 
  

  

  

  
    

Get error set

Parameters:

-

        new_options

        (Hash)
      
      
        *(defaults to: EMPTY_HASH)*
      
      
    
  

  
    
    
    

Options Hash (new_options):

-
          :locale
          (Symbol)
          
            
          
          
            — 

Set locale for messages

-
          :hints
          (Boolean)
          
            
          
          
            — 

Enable/disable hints

-
          :full
          (Boolean)
          
            
          
          
            — 

Get messages that include key names

Returns:

-

        (MessageSet)

```

77
78
79
```

```
# File 'lib/dry/validation/result.rb', line 77

def errors(new_options = EMPTY_HASH)
  new_options.empty? ? @errors : @errors.with(schema_errors(new_options), new_options)
end
```

###
  
    #**failure?**  ⇒ Bool 
  

  

  

  
    

Check if result is not successful

Returns:

-

        (Bool)

```

95
96
97
```

```
# File 'lib/dry/validation/result.rb', line 95

def failure?
  !success?
end
```

###
  
    #**freeze**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Freeze result and its error set

```

194
195
196
197
198
```

```
# File 'lib/dry/validation/result.rb', line 194

def freeze
  values.freeze
  errors.freeze
  super
end
```

###
  
    #**inspect**  ⇒ Object 
  

  

  

  
    

Return a string representation

```

183
184
185
186
187
188
189
```

```
# File 'lib/dry/validation/result.rb', line 183

def inspect
  if context.empty?
    "#<#{self.class}#{to_h} errors=#{errors.to_h}>"
  else
    "#<#{self.class}#{to_h} errors=#{errors.to_h} context=#{context.each.to_h}>"
  end
end
```

###
  
    #**key?**(key)  ⇒ Bool 
  

  

  

  
    

Check if a key was set

Parameters:

-

        key

        (Symbol)
      
      
      
    
  
Returns:

-

        (Bool)

```

169
170
171
```

```
# File 'lib/dry/validation/result.rb', line 169

def key?(key)
  values.key?(key)
end
```

###
  
    #**rule_error?**(key)  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Check if the rules includes an error for the provided key

Returns:

-

        (Boolean)

```

116
117
118
```

```
# File 'lib/dry/validation/result.rb', line 116

def rule_error?(key)
  !schema_error?(key) && error?(key)
end
```

###
  
    #**schema_error?**(key)  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Check if the base schema (without rules) includes an error for the provided key

Returns:

-

        (Boolean)

```

109
110
111
```

```
# File 'lib/dry/validation/result.rb', line 109

def schema_error?(key)
  schema_result.error?(key)
end
```

###
  
    #**success?**  ⇒ Bool 
  

  

  

  
    

Check if result is successful

Returns:

-

        (Bool)

```

86
87
88
```

```
# File 'lib/dry/validation/result.rb', line 86

def success?
  @errors.empty?
end
```

###
  
    #**to_h**  ⇒ Object 
  

  

  

  
    

Coerce to a hash

```

176
177
178
```

```
# File 'lib/dry/validation/result.rb', line 176

def to_h
  values.to_h
end
```

###
  
    #**to_monad**  ⇒ Dry::Monads::Result 
  

  

  

  
    

Returns a result monad

Returns:

-

        (Dry::Monads::Result)

```

34
35
36
```

```
# File 'lib/dry/validation/extensions/monads.rb', line 34

def to_monad
  success? ? Success(self) : Failure(self)
end
```

###
  
    #**values**  ⇒ Values 
  

  

  

  
    

Return values wrapper with the input processed by schema

Returns:

-

        (Values)

```

62
63
64
```

```
# File 'lib/dry/validation/result.rb', line 62

def values
  @values ||= Values.new(schema_result.to_h)
end
```
