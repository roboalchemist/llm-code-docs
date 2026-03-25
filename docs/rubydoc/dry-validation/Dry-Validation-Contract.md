# Class: Dry::Validation::Contract
  
    Inherits:
    
      Object
      
        

          
- Object

- Dry::Validation::Contract

        show all
      
    
  
  

  
  
  
      Extended by:
      Initializer, ClassInterface
  
    Defined in:
    lib/dry/validation/contract.rb,

  lib/dry/validation/contract/class_interface.rb,
 lib/dry/validation/extensions/predicates_as_macros.rb

## Overview

Extension to use dry-logic predicates as macros.

#### Examples

```
Dry::Validation.load_extensions(:predicates_as_macros)

class ApplicationContract < Dry::Validation::Contract
  import_predicates_as_macros
end

class AgeContract < ApplicationContract
  schema do
    required(:age).filled(:integer)
  end

  rule(:age).validate(gteq?: 18)
end

AgeContract.new.(age: 17).errors.first.text
# => 'must be greater than or equal to 18'
```

See Also:
  
- Available predicates

## Defined Under Namespace

      **Modules:** ClassInterface
    
  
    
  
## Instance Attribute Summary collapse

-
  
      #**config**  ⇒ Config 

      readonly
    
    
  
  
  
  
  

  
    

Contract’s configuration object.

-
  
      #**default_context**  ⇒ Hash 

      readonly
    
    
  
  
  
  
  

  
    

Default context for rules.

-
  
      #**macros**  ⇒ Macros::Container 

      readonly
    
    
  
  
  
  
  

  
    

Configured macros.

-
  
      #**message_resolver**  ⇒ Messages::Resolver 

      readonly
    
    
  
  private

-
  
      #**rules**  ⇒ Hash 

      readonly
    
    
  
  private

-
  
      #**schema**  ⇒ Dry::Schema::Params, ... 

      readonly
    
    
  
  private

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**import_predicates_as_macros**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Make macros available for self and its descendants.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**call**(input, context = EMPTY_HASH)  ⇒ Result 
    

    
  
  
  
  
  
  
  
  

  
    

Apply the contract to an input.

-
  
      #**inspect**  ⇒ String 

Return a nice string representation.

### Methods included from ClassInterface

__schema__, build, inherited, json, params, rule

### Methods included from Macros::Registrar

# register_macro

## Instance Attribute Details

###
  
    #**config**  ⇒ Config  (readonly)
  

  

  

  
    

Returns Contract’s configuration object.

Returns:

-

        (Config)

        —
        

Contract’s configuration object

```

55
```

```
# File 'lib/dry/validation/contract.rb', line 55

option :config, default: -> { self.class.config }
```

###
  
    #**default_context**  ⇒ Hash  (readonly)
  

  

  

  
    

Returns Default context for rules.

Returns:

-

        (Hash)

        —
        

Default context for rules

```

66
```

```
# File 'lib/dry/validation/contract.rb', line 66

option :default_context, default: -> { EMPTY_HASH }
```

###
  
    #**macros**  ⇒ Macros::Container  (readonly)
  

  

  

  
    

Returns Configured macros.

Returns:

-

        (Macros::Container)

        —
        

Configured macros

See Also:
  
- Macros::Container#register

```

61
```

```
# File 'lib/dry/validation/contract.rb', line 61

option :macros, default: -> { config.macros }
```

###
  
    #**message_resolver**  ⇒ Messages::Resolver  (readonly)
  

  

  

  
    

  __This method is part of a private API.__
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Messages::Resolver)

```

81
```

```
# File 'lib/dry/validation/contract.rb', line 81

option :message_resolver, default: -> { Messages::Resolver.new(messages) }
```

###
  
    #**rules**  ⇒ Hash  (readonly)
  

  

  

  
    

  __This method is part of a private API.__
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Hash)

```

76
```

```
# File 'lib/dry/validation/contract.rb', line 76

option :rules, default: -> { self.class.rules }
```

###
  
    #**schema**  ⇒ Dry::Schema::Params, ...  (readonly)
  

  

  

  
    

  __This method is part of a private API.__
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Dry::Schema::Params, Dry::Schema::JSON, Dry::Schema::Processor)

```

71
```

```
# File 'lib/dry/validation/contract.rb', line 71

option :schema, default: -> { self.class.__schema__ || raise(SchemaMissingError, self.class) }
```

## Class Method Details

###
  
    .**import_predicates_as_macros**  ⇒ Object 
  

  

  

  
    

Make macros available for self and its descendants.

```

58
59
60
61
62
63
64
65
66
67
68
69
```

```
# File 'lib/dry/validation/extensions/predicates_as_macros.rb', line 58

def self.import_predicates_as_macros
  registry = PredicateRegistry.new

  PredicateRegistry::WHITELIST.each do |name|
    register_macro(name) do |macro:|
      predicate_args = [*macro.args, value]
      message_opts = registry.message_opts(name, predicate_args)

      key.failure(name, message_opts) unless registry.(name, predicate_args)
    end
  end
end
```

## Instance Method Details

###
  
    #**call**(input, context = EMPTY_HASH)  ⇒ Result 
  

  

  

  
    

Apply the contract to an input

rubocop: disable Metrics/AbcSize

Parameters:

-

        input

        (Hash)
      
      
      
        —
        

The input to validate

-

        context

        (Hash)
      
      
        *(defaults to: EMPTY_HASH)*
      
      
        —
        

Initial context for rules

Returns:

-

        (Result)

```

92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
```

```
# File 'lib/dry/validation/contract.rb', line 92

def call(input, context = EMPTY_HASH)
  validate_input_type(input)

  context_map = ::Concurrent::Map.new.tap do |map|
    default_context.each { |key, value| map[key] = value }
    context.each { |key, value| map[key] = value }
  end

  Result.new(schema.(input), context_map) do |result|
    rules.each do |rule|
      next if rule.keys.any? { |key| error?(result, key) }

      rule_result = rule.(self, result)

      rule_result.failures.each do |failure|
        result.add_error(message_resolver.(**failure))
      end
    end
  end
end
```

###
  
    #**inspect**  ⇒ String 
  

  

  

  
    

Return a nice string representation

Returns:

-

        (String)

```

119
120
121
```

```
# File 'lib/dry/validation/contract.rb', line 119

def inspect
  %(#<#{self.class} schema=#{schema.inspect} rules=#{rules.inspect}>)
end
```
