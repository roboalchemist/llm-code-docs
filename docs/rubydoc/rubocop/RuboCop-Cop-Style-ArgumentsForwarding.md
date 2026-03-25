# Class: RuboCop::Cop::Style::ArgumentsForwarding
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Style::ArgumentsForwarding

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector, TargetRubyVersion
  
  
  
  
  
      Includes:
      RangeHelp
  
    Defined in:
    lib/rubocop/cop/style/arguments_forwarding.rb
  
## Overview

In Ruby 2.7, arguments forwarding has been added.

This cop identifies places where ‘do_something(*args, &block)` can be replaced by `do_something(…)`.

In Ruby 3.1, anonymous block forwarding has been added.

This cop identifies places where ‘do_something(&block)` can be replaced by `do_something(&)`; if desired, this functionality can be disabled by setting`UseAnonymousForwarding: false`.

In Ruby 3.2, anonymous args/kwargs forwarding has been added.

This cop also identifies places where ‘+use_args(*args)+`/`use_kwargs(**kwargs)` can be replaced by `+use_args(*)+`/`use_kwargs(**)`; if desired, this functionality can be disabled by setting`UseAnonymousForwarding: false`.

And this cop has `RedundantRestArgumentNames`, `RedundantKeywordRestArgumentNames`, and `RedundantBlockArgumentNames` options. This configuration is a list of redundant names that are sufficient for anonymizing meaningless naming.

Meaningless names that are commonly used can be anonymized by default: e.g., ‘+*args+`,`+**options+`,`&block`, and so on.

Names not on this list are likely to be meaningful and are allowed by default.

This cop handles not only method forwarding but also forwarding to `super`.
NOTE

####

Because of a bug in Ruby 3.3.0, when a block is referenced inside of another block, no offense will be registered until Ruby 3.4:
source,ruby

---

def foo(&block)

```
# Using an anonymous block would be a syntax error on Ruby 3.3.0
block_method { bar(&block) }

```

end

---

####

#### Examples

```
# bad
def foo(*args, &block)
  bar(*args, &block)
end

# bad
def foo(*args, **kwargs, &block)
  bar(*args, **kwargs, &block)
end

# good
def foo(...)
  bar(...)
end
```

#####

UseAnonymousForwarding: true (default, only relevant for Ruby >= 3.2)

```
# bad
def foo(*args, **kwargs, &block)
  args_only(*args)
  kwargs_only(**kwargs)
  block_only(&block)
end

# good
def foo(*, **, &)
  args_only(*)
  kwargs_only(**)
  block_only(&)
end
```

#####

UseAnonymousForwarding: false (only relevant for Ruby >= 3.2)

```
# good
def foo(*args, **kwargs, &block)
  args_only(*args)
  kwargs_only(**kwargs)
  block_only(&block)
end
```

#####

AllowOnlyRestArgument: true (default, only relevant for Ruby < 3.2)

```
# good
def foo(*args)
  bar(*args)
end

def foo(**kwargs)
  bar(**kwargs)
end
```

#####

AllowOnlyRestArgument: false (only relevant for Ruby < 3.2)

```
# bad
# The following code can replace the arguments with `...`,
# but it will change the behavior. Because `...` forwards block also.
def foo(*args)
  bar(*args)
end

def foo(**kwargs)
  bar(**kwargs)
end
```

#####

RedundantRestArgumentNames: [‘args’, ‘arguments’] (default)

```
# bad
def foo(*args)
  bar(*args)
end

# good
def foo(*)
  bar(*)
end
```

#####

RedundantKeywordRestArgumentNames: [‘kwargs’, ‘options’, ‘opts’] (default)

```
# bad
def foo(**kwargs)
  bar(**kwargs)
end

# good
def foo(**)
  bar(**)
end
```

#####

RedundantBlockArgumentNames: [‘blk’, ‘block’, ‘proc’] (default)

```
# bad - But it is good with `EnforcedStyle: explicit` set for `Naming/BlockForwarding`.
def foo(&block)
  bar(&block)
end

# good
def foo(&)
  bar(&)
end
```

## Defined Under Namespace

      **Classes:** SendNodeClassifier
    
  

  
    
##

      Constant Summary
      collapse
    

    
      
        FORWARDING_LVAR_TYPES =
          
        
        

```
%i[splat kwsplat block_pass].freeze
```

        FORWARDING_MSG =
          
        
        

```
'Use shorthand syntax `...` for arguments forwarding.'
```

        ARGS_MSG =
          
        
        

```
'Use anonymous positional arguments forwarding (`*`).'
```

        KWARGS_MSG =
          
        
        

```
'Use anonymous keyword arguments forwarding (`**`).'
```

        BLOCK_MSG =
          
        
        

```
'Use anonymous block arguments forwarding (`&`).'
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
  
      #**on_def**(node)  ⇒ Object 
    

    
      (also: #on_defs)
    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods included from AutoCorrector

support_autocorrect?

### Methods included from TargetRubyVersion

maximum_target_ruby_version, minimum_target_ruby_version, required_maximum_ruby_version, required_minimum_ruby_version, support_target_ruby_version?

### Methods inherited from Base

# active_support_extensions_enabled?, #add_global_offense, #add_offense, #always_autocorrect?, badge, #begin_investigation, #callbacks_needed, callbacks_needed, #config_to_allow_offenses, #config_to_allow_offenses=, #contextual_autocorrect?, #cop_config, cop_name, #cop_name, department, documentation_url, exclude_from_registry, #excluded_file?, #external_dependency_checksum, inherited, #initialize, #inspect, joining_forces, lint?, match?, #message, #offenses, #on_investigation_end, #on_new_investigation, #on_other_file, #parse, #parser_engine, #ready, #relevant_file?, requires_gem, #string_literals_frozen_by_default?, support_autocorrect?, support_multiple_source?, #target_gem_version, #target_rails_version, #target_ruby_version

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

155
156
157
```

```
# File 'lib/rubocop/cop/style/arguments_forwarding.rb', line 155

def self.autocorrect_incompatible_with
  [Naming::BlockForwarding]
end
```

## Instance Method Details

###
  
    #**on_def**(node)  ⇒ Object 
  

  
    Also known as:
    on_defs
    
  

  

  
    
      

```

159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
```

```
# File 'lib/rubocop/cop/style/arguments_forwarding.rb', line 159

def on_def(node)
  return unless node.body

  restarg, kwrestarg, blockarg = extract_forwardable_args(node.arguments)
  forwardable_args = redundant_forwardable_named_args(restarg, kwrestarg, blockarg)
  send_nodes = node.each_descendant(:call, :super, :yield).to_a

  send_classifications = classify_send_nodes(
    node, send_nodes, non_splat_or_block_pass_lvar_references(node.body), forwardable_args
  )

  return if send_classifications.empty?

  if only_forwards_all?(send_classifications)
    add_forward_all_offenses(node, send_classifications, forwardable_args)
  elsif target_ruby_version >= 3.2
    add_post_ruby_32_offenses(node, send_classifications, forwardable_args)
  end
end
```
