# Class: RuboCop::Cop::Style::BlockDelimiters
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Style::BlockDelimiters

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
  
  
  
  
      Includes:
      AllowedMethods, AllowedPattern, ConfigurableEnforcedStyle, RangeHelp
  
    Defined in:
    lib/rubocop/cop/style/block_delimiters.rb
  
## Overview

Checks for uses of braces or do/end around single line or multi-line blocks.

Methods that can be either procedural or functional and cannot be categorised from their usage alone is ignored. `lambda`, `proc`, and `it` are their defaults. Additional methods can be added to the `AllowedMethods`.

#### Examples

#####

EnforcedStyle: line_count_based (default)

```
# bad - single line block
items.each do |item| item / 5 end

# good - single line block
items.each { |item| item / 5 }

# bad - multi-line block
things.map { |thing|
  something = thing.some_method
  process(something)
}

# good - multi-line block
things.map do |thing|
  something = thing.some_method
  process(something)
end

```

#####

EnforcedStyle: semantic

```
# Prefer `do...end` over `{...}` for procedural blocks.

# return value is used/assigned
# bad
foo = map do |x|
  x
end
puts (map do |x|
  x
end)

# return value is not used out of scope
# good
map do |x|
  x
end

# Prefer `{...}` over `do...end` for functional blocks.

# return value is not used out of scope
# bad
each { |x|
  x
}

# return value is used/assigned
# good
foo = map { |x|
  x
}
map { |x|
  x
}.inspect

# The AllowBracesOnProceduralOneLiners option is allowed unless the
# EnforcedStyle is set to `semantic`. If so:

# If the AllowBracesOnProceduralOneLiners option is unspecified, or
# set to `false` or any other falsey value, then semantic purity is
# maintained, so one-line procedural blocks must use do-end, not
# braces.

# bad
collection.each { |element| puts element }

# good
collection.each do |element| puts element end

# If the AllowBracesOnProceduralOneLiners option is set to `true`, or
# any other truthy value, then one-line procedural blocks may use
# either style. (There is no setting for requiring braces on them.)

# good
collection.each { |element| puts element }

# also good
collection.each do |element| puts element end

```

#####

EnforcedStyle: braces_for_chaining

```
# bad
words.each do |word|
  word.flip.flop
end.join("-")

# good
words.each { |word|
  word.flip.flop
}.join("-")

```

#####

EnforcedStyle: always_braces

```
# bad
words.each do |word|
  word.flip.flop
end

# good
words.each { |word|
  word.flip.flop
}

```

#####

BracesRequiredMethods: [‘sig’]

```

# Methods listed in the BracesRequiredMethods list, such as 'sig'
# in this example, will require `{...}` braces. This option takes
# precedence over all other configurations except AllowedMethods.

# bad
sig do
  params(
    foo: string,
  ).void
end
def bar(foo)
  puts foo
end

# good
sig {
  params(
    foo: string,
  ).void
}
def bar(foo)
  puts foo
end

```

#####

AllowedMethods: [‘lambda’, ‘proc’, ‘it’ ] (default)

```

# good
foo = lambda do |x|
  puts "Hello, #{x}"
end

foo = lambda do |x|
  x * 100
end

```

#####

AllowedPatterns: [] (default)

```

# bad
things.map { |thing|
  something = thing.some_method
  process(something)
}

```

#####

AllowedPatterns: [‘map’]

```

# good
things.map { |thing|
  something = thing.some_method
  process(something)
}

```

##

      Constant Summary
      collapse
    

    
      
        ALWAYS_BRACES_MESSAGE =
          
        
        

```
'Prefer `{...}` over `do...end` for blocks.'

```

        BRACES_REQUIRED_MESSAGE =
          
        
        

```
"Brace delimiters `{...}` required for '%<method_name>s' method."

```

### Constants included

     from RangeHelp

RangeHelp::BYTE_ORDER_MARK, RangeHelp::NOT_GIVEN

### Constants inherited

     from Base

Base::RESTRICT_ON_SEND

## Instance Attribute Summary

### Attributes inherited from Base

# config, #processed_source

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**autocorrect_incompatible_with**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**on_block**(node)  ⇒ Object 
    

    
      (also: #on_numblock, #on_itblock)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**on_send**(node)  ⇒ Object 
    

    
      (also: #on_csend)
    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods included from AutoCorrector

support_autocorrect?

### Methods included from ConfigurableEnforcedStyle

# alternative_style, #alternative_styles, #ambiguous_style_detected, #correct_style_detected, #detected_style, #detected_style=, #no_acceptable_style!, #no_acceptable_style?, #opposite_style_detected, #style, #style_configured?, #style_detected, #style_parameter_name, #supported_styles, #unexpected_style_detected

### Methods inherited from Base

# active_support_extensions_enabled?, #add_global_offense, #add_offense, #always_autocorrect?, badge, #begin_investigation, callbacks_needed, #callbacks_needed, #config_to_allow_offenses, #config_to_allow_offenses=, #contextual_autocorrect?, #cop_config, cop_name, #cop_name, department, documentation_url, exclude_from_registry, #excluded_file?, #external_dependency_checksum, inherited, #initialize, #inspect, joining_forces, lint?, match?, #offenses, #on_investigation_end, #on_new_investigation, #on_other_file, #parse, #parser_engine, #ready, #relevant_file?, requires_gem, #string_literals_frozen_by_default?, support_autocorrect?, support_multiple_source?, #target_gem_version, #target_rails_version, #target_ruby_version

### Methods included from ExcludeLimit

# exclude_limit

### Methods included from AutocorrectLogic

# autocorrect?, #autocorrect_enabled?, #autocorrect_requested?, #autocorrect_with_disable_uncorrectable?, #correctable?, #disable_uncorrectable?, #safe_autocorrect?

### Methods included from IgnoredNode

# ignore_node, #ignored_node?, #part_of_ignored_node?

### Methods included from Util

silence_warnings

## Constructor Details

This class inherits a constructor from RuboCop::Cop::Base
  
## Class Method Details

###
  
    .**autocorrect_incompatible_with**  ⇒ Object 
  

  

  

  
    
      

```

179
180
181
```

```
# File 'lib/rubocop/cop/style/block_delimiters.rb', line 179

def self.autocorrect_incompatible_with
  [Style::RedundantBegin]
end

```

## Instance Method Details

###
  
    #**on_block**(node)  ⇒ Object 
  

  
    Also known as:
    on_numblock, on_itblock
    
  

  

  
    
      

```

200
201
202
203
204
205
206
207
208
209
```

```
# File 'lib/rubocop/cop/style/block_delimiters.rb', line 200

def on_block(node)
  return if part_of_ignored_node?(node)
  return if proper_block_style?(node)

  message = message(node)
  add_offense(node.loc.begin, message: message) do |corrector|
    autocorrect(corrector, node)
    ignore_node(node)
  end
end

```

###
  
    #**on_send**(node)  ⇒ Object 
  

  
    Also known as:
    on_csend
    
  

  

  
    
      

```

183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
```

```
# File 'lib/rubocop/cop/style/block_delimiters.rb', line 183

def on_send(node)
  return unless node.arguments?
  return if node.parenthesized?
  return if node.assignment_method?
  return if single_argument_operator_method?(node)

  node.arguments.each do |arg|
    get_blocks(arg) do |block|
      # If there are no parentheses around the arguments, then braces
      # and do-end have different meaning due to how they bind, so we
      # allow either.
      ignore_node(block)
    end
  end
end

```
