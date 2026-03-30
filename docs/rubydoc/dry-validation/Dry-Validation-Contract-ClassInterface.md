# Module: Dry::Validation::Contract::ClassInterface
  
      Includes:
      Macros::Registrar
  
  
  

  
  
    Included in:
    Dry::Validation::Contract
  
  

  
  
    Defined in:
    lib/dry/validation/contract/class_interface.rb
  
## Overview

Contract’s class interface

See Also:
  
- Dry::Validation::Contract

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**__schema__**  ⇒ Object 
    

    
  
  private

-
  
      #**build**(options = EMPTY_HASH)  ⇒ Contract 

A shortcut that can be used to define contracts that won’t be reused or inherited.

-
  
      #**config**  ⇒ Config 

Configuration.

-
  
      #**inherited**(klass)  ⇒ Object 

  private

-
  
      #**json**(*external_schemas)  ⇒ Dry::Schema::JSON, NilClass 

Define a JSON schema for your contract.

-
  
      #**macros**  ⇒ Macros::Container 

Return macros registered for this class.

-
  
      #**messages**  ⇒ Dry::Schema::Messages 

  private

Return messages configured for this class.

-
  
      #**params**(*external_schemas)  ⇒ Dry::Schema::Params, NilClass 

Define a params schema for your contract.

-
  
      #**rule**(*keys, &block)  ⇒ Rule 

Define a rule for your contract.

-
  
      #**rules**  ⇒ Array<Rule> 

  private

Return rules defined in this class.

-
  
      #**schema**(*external_schemas)  ⇒ Dry::Schema::Processor, NilClass 

Define a plain schema for your contract.

### Methods included from Macros::Registrar

# register_macro

## Instance Method Details

###
  
    #**__schema__**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

123
124
125
```

```
# File 'lib/dry/validation/contract/class_interface.rb', line 123

def __schema__
  @__schema__ if defined?(@__schema__)
end

```

###
  
    #**build**(options = EMPTY_HASH)  ⇒ Contract 
  

  

  

  
    

A shortcut that can be used to define contracts that won’t be reused or inherited

#### Examples

```
my_contract = Dry::Validation::Contract.build do
  params do
    required(:name).filled(:string)
  end
end

my_contract.call(name: "Jane")

```

Returns:

-

        (Contract)

```

118
119
120
```

```
# File 'lib/dry/validation/contract/class_interface.rb', line 118

def build(options = EMPTY_HASH, &)
  Class.new(self, &).new(**options)
end

```

###
  
    #**config**  ⇒ Config 
  

  

  

  
    

Configuration

#### Examples

```
class MyContract < Dry::Validation::Contract
  config.messages.backend = :i18n
end

```

Returns:

-

        (Config)

```

32
33
34
```

```
# File 'lib/dry/validation/contract/class_interface.rb', line 32

def config
  @config ||= Validation::Config.new
end

```

###
  
    #**inherited**(klass)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

17
18
19
20
```

```
# File 'lib/dry/validation/contract/class_interface.rb', line 17

def inherited(klass)
  super
  klass.instance_variable_set("@config", config.dup)
end

```

###
  
    #**json**(*external_schemas)  ⇒ Dry::Schema::JSON, NilClass 
  

  

  

  
    

Define a JSON schema for your contract

This type of schema is suitable for JSON data

Returns:

-

        (Dry::Schema::JSON, NilClass)

See Also:
  
- https://dry-rb.org/gems/dry-schema/json/

```

65
66
67
```

```
# File 'lib/dry/validation/contract/class_interface.rb', line 65

def json(*external_schemas, &)
  define(:JSON, external_schemas, &)
end

```

###
  
    #**macros**  ⇒ Macros::Container 
  

  

  

  
    

Return macros registered for this class

Returns:

-

        (Macros::Container)

```

41
42
43
```

```
# File 'lib/dry/validation/contract/class_interface.rb', line 41

def macros
  config.macros
end

```

###
  
    #**messages**  ⇒ Dry::Schema::Messages 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Return messages configured for this class

Returns:

-

        (Dry::Schema::Messages)

```

143
144
145
```

```
# File 'lib/dry/validation/contract/class_interface.rb', line 143

def messages
  @messages ||= Schema::Messages.setup(config.messages)
end

```

###
  
    #**params**(*external_schemas)  ⇒ Dry::Schema::Params, NilClass 
  

  

  

  
    

Define a params schema for your contract

This type of schema is suitable for HTTP parameters

Returns:

-

        (Dry::Schema::Params, NilClass)

See Also:
  
- https://dry-rb.org/gems/dry-schema/params/

```

53
54
55
```

```
# File 'lib/dry/validation/contract/class_interface.rb', line 53

def params(*external_schemas, &)
  define(:Params, external_schemas, &)
end

```

###
  
    #**rule**(*keys, &block)  ⇒ Rule 
  

  

  

  
    

Define a rule for your contract

#### Examples

#####

using a symbol

```
rule(:age) do
  failure('must be at least 18') if values[:age] < 18
end

```

#####

using a path to a value and a custom predicate

```
rule('address.street') do
  failure('please provide a valid street address') if valid_street?(values[:street])
end

```

Returns:

-

        (Rule)

```

96
97
98
99
100
101
102
```

```
# File 'lib/dry/validation/contract/class_interface.rb', line 96

def rule(*keys, &block)
  ensure_valid_keys(*keys) if __schema__

  Rule.new(keys: keys, block: block).tap do |rule|
    rules << rule
  end
end

```

###
  
    #**rules**  ⇒ Array<Rule> 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Return rules defined in this class

Returns:

-

        (Array<Rule>)

```

132
133
134
135
136
```

```
# File 'lib/dry/validation/contract/class_interface.rb', line 132

def rules
  @rules ||= EMPTY_ARRAY
    .dup
    .concat(superclass.respond_to?(:rules) ? superclass.rules : EMPTY_ARRAY)
end

```

###
  
    #**schema**(*external_schemas)  ⇒ Dry::Schema::Processor, NilClass 
  

  

  

  
    

Define a plain schema for your contract

This type of schema does not offer coercion out of the box

Returns:

-

        (Dry::Schema::Processor, NilClass)

See Also:
  
- https://dry-rb.org/gems/dry-schema/

```

77
78
79
```

```
# File 'lib/dry/validation/contract/class_interface.rb', line 77

def schema(*external_schemas, &)
  define(:schema, external_schemas, &)
end

```
