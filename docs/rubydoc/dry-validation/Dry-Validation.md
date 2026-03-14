# Module: Dry::Validation
  
      Extended by:
      Core::Extensions, Macros::Registrar
  
  
  
  
  
      Includes:
      Core::Constants
  
  
  

  

  
  
    Defined in:
    lib/dry/validation.rb,

  lib/dry/validation/rule.rb,
 lib/dry/validation/macro.rb,
 lib/dry/validation/config.rb,
 lib/dry/validation/macros.rb,
 lib/dry/validation/result.rb,
 lib/dry/validation/values.rb,
 lib/dry/validation/message.rb,
 lib/dry/validation/version.rb,
 lib/dry/validation/contract.rb,
 lib/dry/validation/failures.rb,
 lib/dry/validation/function.rb,
 lib/dry/validation/constants.rb,
 lib/dry/validation/evaluator.rb,
 lib/dry/validation/message_set.rb,
 lib/dry/validation/extensions/hints.rb,
 lib/dry/validation/extensions/monads.rb,
 lib/dry/validation/messages/resolver.rb,
 lib/dry/validation/contract/class_interface.rb,
 lib/dry/validation/extensions/predicates_as_macros.rb

## Overview

Main library namespace

## Defined Under Namespace

      **Modules:** Hints, Macros, Messages
    
  
    
      **Classes:** Config, Contract, Evaluator, Failures, Function, Macro, Message, MessageSet, PredicateRegistry, Result, Rule, Values
    
  

  
    
##

      Constant Summary
      collapse
    

    
      
        VERSION =
          
  
    

  

  

        
        

```
"1.11.1"
```

        DOT =
          
  
    

  

  

        
        

```
"."
```

        ROOT_PATH =
          
  
    

Root path is used for base errors in hash representation of error messages

```
[nil].freeze
```

        DEFAULT_ERRORS_NAMESPACE =
          
  
    

Path to the default errors locale file

```
"dry_validation"
```

        DEFAULT_ERRORS_PATH =
          
  
    

Path to the default errors locale file

```
Pathname(__FILE__).join("../../../../config/errors.yml").realpath.freeze
```

        BLOCK_OPTIONS_MAPPINGS =
          
  
    

Mapping for block kwarg options used by block_options

See Also:
  
- Function#block_options

```
::Hash.new { |_, key| key }.update(context: :_context).freeze
```

        InvalidKeysError =
          
  
    

Error raised when `rule` specifies one or more keys that the schema doesn’t specify

```
::Class.new(::StandardError)
```

        MissingMessageError =
          
  
    

Error raised when a localized message was not found

```
::Class.new(::StandardError)
```

        DuplicateSchemaError =
          
  
    

Error raised when trying to define a schema in a contract class that already has a schema

```
::Class.new(::StandardError)
```

        SchemaMissingError =
          
  
    

Error raised during initialization of a contract that has no schema defined

```
::Class.new(::StandardError) do
  # @api private
  def initialize(klass)
    super("#{klass} cannot be instantiated without a schema defined")
  end
end
```

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**Contract**(options = EMPTY_HASH)  ⇒ Contract 
    

    
  
  
  
  
  
  
  
  

  
    

Define a contract and build its instance.

-
  
      .**loader**  ⇒ Object 

-
  
      .**macros**  ⇒ Object 

  private

This is needed by Macros::Registrar.

### Methods included from Macros::Registrar

register_macro

## Class Method Details

###
  
    .**Contract**(options = EMPTY_HASH)  ⇒ Contract 
  

  

  

  
    

Define a contract and build its instance

#### Examples

```
my_contract = Dry::Validation.Contract do
  params do
    required(:name).filled(:string)
  end
end

my_contract.call(name: "Jane")
```

Parameters:

-

        options

        (Hash)
      
      
        *(defaults to: EMPTY_HASH)*
      
      
        —
        

Contract options

Returns:

-

        (Contract)

See Also:
  
- Contract

```

67
68
69
```

```
# File 'lib/dry/validation.rb', line 67

def self.Contract(options = EMPTY_HASH, &)
  Contract.build(options, &)
end
```

###
  
    .**loader**  ⇒ Object 
  

  

  

  
    

  

  

  
    
      

```

20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
```

```
# File 'lib/dry/validation.rb', line 20

def self.loader
  @loader ||= Zeitwerk::Loader.new.tap do |loader|
    root = File.expand_path("..", __dir__)
    loader.tag = "dry-validation"
    loader.inflector = Zeitwerk::GemInflector.new("#{root}/dry-validation.rb")
    loader.push_dir(root)
    loader.ignore(
      "#{root}/dry-validation.rb",
      "#{root}/dry/validation/schema_ext.rb",
      "#{root}/dry/validation/{constants,errors,version}.rb",
      "#{root}/dry/validation/extensions"
    )
    loader.inflector.inflect("dsl" => "DSL")
  end
end
```

###
  
    .**macros**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

This is needed by Macros::Registrar

```

74
75
76
```

```
# File 'lib/dry/validation.rb', line 74

def self.macros
  Macros
end
```
