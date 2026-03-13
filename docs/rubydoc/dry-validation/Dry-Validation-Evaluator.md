# Class: Dry::Validation::Evaluator
  
    Inherits:
    
      Object
      
        

          
- Object

- Dry::Validation::Evaluator

        show all
      
    
  
  

  
  
  
      Extended by:
      Initializer
  
    Defined in:
    lib/dry/validation/evaluator.rb
  
## Overview

Evaluator is the execution context for rules

Evaluators expose an API for setting failure messages and forward method calls to the contracts, so that you can use your contract methods within rule blocks

API:

-

public

## Instance Attribute Summary collapse

-
  
      #**_context**  ⇒ Concurrent::Map 

      readonly
    
    
  
  private

-
  
      #**_contract**  ⇒ Contract 

      readonly
    
    
  
  private

-
  
      #**_options**  ⇒ Hash 

      readonly
    
    
  
  
  
  
  

  
    
  

    
      
-
  
      #**block_options**  ⇒ Hash<Symbol=>Symbol> 
    

    
  
  
  
  
    
      readonly
    
    
  
  private

-
  
      #**keys**  ⇒ Array<String, Symbol, Hash> 

      readonly
    
    
  
  private

-
  
      #**macros**  ⇒ Array<Symbol> 

      readonly
    
    
  
  private

-
  
      #**path**  ⇒ Dry::Schema::Path 

      readonly
    
    
  
  private

-
  
      #**result**  ⇒ Result 

      readonly
    
    
  
  private

-
  
      #**values**  ⇒ Object 

      readonly
    
    
  
  private

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**base**  ⇒ Failures 
    

    
  
  
  
  
  
  
  
  

  
    

Get `Failures` object for base errors.

-
  
      #**base_rule_error?**  ⇒ Boolean 

Check if there are any base rule errors.

-
  
      #**failures**  ⇒ Array<Hash> 

  private

Return aggregated failures.

-
  
      #**initialize**(contract, **options, &block)  ⇒ Evaluator 

    constructor
  
  private

Initialize a new evaluator.

-
  
      #**key**(path = self.path)  ⇒ Failures 

Get `Failures` object for the default or provided path.

-
  
      #**key?**(name = key_name)  ⇒ Boolean 

Return if the value under the default key is available.

-
  
      #**key_name**  ⇒ Symbol 

Return default (first) key name.

-
  
      #**respond_to_missing?**(meth, include_private = false)  ⇒ Boolean 

  private

-
  
      #**rule_error?**(path = nil)  ⇒ Boolean 

Check if there are any errors on the current rule.

-
  
      #**schema_error?**(path)  ⇒ Boolean 

Check if there are any errors on the schema under the provided path.

-
  
      #**value**  ⇒ Object 

Return the value found under the first specified key.

-
  
      #**with**(new_opts)  ⇒ Object 

  private

## Constructor Details

###
  
    #**initialize**(contract, **options, &block)  ⇒ Evaluator 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Initialize a new evaluator

API:

-

private

```

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
80
81
```

```
# File 'lib/dry/validation/evaluator.rb', line 67

def initialize(contract, **options, &block)
  super(contract, **options)

  @_options = options

  if block
    exec_opts = block_options.transform_values { _options[_1] }
    instance_exec(**exec_opts, &block)
  end

  macros.each do |args|
    macro = macro(*args.flatten(1))
    instance_exec(**macro.extract_block_options(_options.merge(macro: macro)), &macro.block)
  end
end

```

## Dynamic Method Handling

    This class handles dynamic methods through the method_missing method
    
  
  
    
  
###
  
    #**method_missing**(meth)  ⇒ Object  (private)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Forward to the underlying contract

API:

-

private

```

219
220
221
222
223
224
225
226
```

```
# File 'lib/dry/validation/evaluator.rb', line 219

def method_missing(meth, ...)
  # yes, we do want to delegate to private methods too
  if _contract.respond_to?(meth, true)
    _contract.__send__(meth, ...)
  else
    super
  end
end

```

## Instance Attribute Details

###
  
    #**_context**  ⇒ Concurrent::Map  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

API:

-

private

```

44
```

```
# File 'lib/dry/validation/evaluator.rb', line 44

option :_context

```

###
  
    #**_contract**  ⇒ Contract  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

API:

-

private

```

24
```

```
# File 'lib/dry/validation/evaluator.rb', line 24

param :_contract

```

###
  
    #**_options**  ⇒ Hash  (readonly)
  

  

  

  
    

Returns:

-

API:

-

public

```

62
63
64
```

```
# File 'lib/dry/validation/evaluator.rb', line 62

def _options
  @_options
end

```

###
  
    #**block_options**  ⇒ Hash<Symbol=>Symbol>  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

API:

-

private

```

59
```

```
# File 'lib/dry/validation/evaluator.rb', line 59

option :block_options, default: proc { EMPTY_HASH }

```

###
  
    #**keys**  ⇒ Array<String, Symbol, Hash>  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

API:

-

private

```

34
```

```
# File 'lib/dry/validation/evaluator.rb', line 34

option :keys

```

###
  
    #**macros**  ⇒ Array<Symbol>  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

API:

-

private

```

39
```

```
# File 'lib/dry/validation/evaluator.rb', line 39

option :macros, optional: true, default: proc { EMPTY_ARRAY.dup }

```

###
  
    #**path**  ⇒ Dry::Schema::Path  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

API:

-

private

```

49
```

```
# File 'lib/dry/validation/evaluator.rb', line 49

option :path, default: proc { Dry::Schema::Path[(key = keys.first) ? key : ROOT_PATH] }

```

###
  
    #**result**  ⇒ Result  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

API:

-

private

```

29
```

```
# File 'lib/dry/validation/evaluator.rb', line 29

option :result

```

###
  
    #**values**  ⇒ Object  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

API:

-

private

```

54
```

```
# File 'lib/dry/validation/evaluator.rb', line 54

option :values

```

## Instance Method Details

###
  
    #**base**  ⇒ Failures 
  

  

  

  
    

Get `Failures` object for base errors

Returns:

-

See Also:
  
- Failures#failure

API:

-

public

```

103
104
105
```

```
# File 'lib/dry/validation/evaluator.rb', line 103

def base
  @base ||= Failures.new
end

```

###
  
    #**base_rule_error?**  ⇒ Boolean 
  

  

  

  
    

Check if there are any base rule errors

Returns:

-

API:

-

public

```

205
206
207
```

```
# File 'lib/dry/validation/evaluator.rb', line 205

def base_rule_error?
  !base.empty? || result.base_rule_error?
end

```

###
  
    #**failures**  ⇒ Array<Hash> 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Return aggregated failures

Returns:

-

API:

-

private

```

112
113
114
115
116
117
```

```
# File 'lib/dry/validation/evaluator.rb', line 112

def failures
  @failures ||= []
  @failures += @base.opts if defined?(@base)
  @failures.concat(@key.values.flat_map(&:opts)) if defined?(@key)
  @failures
end

```

###
  
    #**key**(path = self.path)  ⇒ Failures 
  

  

  

  
    

Get `Failures` object for the default or provided path

Parameters:

-

        *(defaults to: self.path)*

Returns:

-

See Also:
  
- Failures#failure

API:

-

public

```

92
93
94
```

```
# File 'lib/dry/validation/evaluator.rb', line 92

def key(path = self.path)
  (@key ||= EMPTY_HASH.dup)[path] ||= Failures.new(path)
end

```

###
  
    #**key?**(name = key_name)  ⇒ Boolean 
  

  

  

  
    

Return if the value under the default key is available

This is useful when dealing with rules for optional keys

#### Examples

#####

use the default key name

```
rule(:age) do
  key.failure(:invalid) if key? && value < 18
end

```

#####

specify the key name

```
rule(:start_date, :end_date) do
  if key?(:start_date) && !key?(:end_date)
    key(:end_date).failure("must provide an end_date with start_date")
  end
end

```

Returns:

-

API:

-

public

```

170
171
172
```

```
# File 'lib/dry/validation/evaluator.rb', line 170

def key?(name = key_name)
  values.key?(name)
end

```

###
  
    #**key_name**  ⇒ Symbol 
  

  

  

  
    

Return default (first) key name

Returns:

-

API:

-

public

```

129
130
131
```

```
# File 'lib/dry/validation/evaluator.rb', line 129

def key_name
  @key_name ||= keys.first
end

```

###
  
    #**respond_to_missing?**(meth, include_private = false)  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

API:

-

private

```

210
211
212
```

```
# File 'lib/dry/validation/evaluator.rb', line 210

def respond_to_missing?(meth, include_private = false)
  super || _contract.respond_to?(meth, true)
end

```

###
  
    #**rule_error?**(path = nil)  ⇒ Boolean 
  

  

  

  
    

Check if there are any errors on the current rule

Parameters:

-

        *(defaults to: nil)*

A Path-compatible spec

Returns:

-

API:

-

public

```

192
193
194
195
196
197
198
```

```
# File 'lib/dry/validation/evaluator.rb', line 192

def rule_error?(path = nil)
  if path.nil?
    !key(self.path).empty?
  else
    result.rule_error?(path)
  end
end

```

###
  
    #**schema_error?**(path)  ⇒ Boolean 
  

  

  

  
    

Check if there are any errors on the schema under the provided path

Parameters:

-

A Path-compatible spec

Returns:

-

API:

-

public

```

181
182
183
```

```
# File 'lib/dry/validation/evaluator.rb', line 181

def schema_error?(path)
  result.schema_error?(path)
end

```

###
  
    #**value**  ⇒ Object 
  

  

  

  
    

Return the value found under the first specified key

This is a convenient method that can be used in all the common cases where a rule depends on just one key and you want a quick access to the value

#### Examples

```
rule(:age) do
  key.failure(:invalid) if value < 18
end

```

Returns:

-

API:

-

public

```

147
148
149
```

```
# File 'lib/dry/validation/evaluator.rb', line 147

def value
  values[key_name]
end

```

###
  
    #**with**(new_opts)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

API:

-

private

```

120
121
122
```

```
# File 'lib/dry/validation/evaluator.rb', line 120

def with(new_opts, &)
  self.class.new(_contract, **_options, **new_opts, &)
end

```
