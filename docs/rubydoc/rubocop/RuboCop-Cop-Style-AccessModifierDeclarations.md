# Class: RuboCop::Cop::Style::AccessModifierDeclarations
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Style::AccessModifierDeclarations

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
  
  
  
  
      Includes:
      ConfigurableEnforcedStyle, RangeHelp
  
    Defined in:
    lib/rubocop/cop/style/access_modifier_declarations.rb
  
## Overview

Access modifiers should be declared to apply to a group of methods or inline before each method, depending on configuration. EnforcedStyle config covers only method definitions. Applications of visibility methods to symbols can be controlled using AllowModifiersOnSymbols config. Also, the visibility of `attr*` methods can be controlled using AllowModifiersOnAttrs config.

In Ruby 3.0, `attr*` methods now return an array of defined method names as symbols. So we can write the modifier and `attr*` in inline style. AllowModifiersOnAttrs config allows `attr*` methods to be written in inline style without modifying applications that have been maintained for a long time in group style. Furthermore, developers who are not very familiar with Ruby may know that the modifier applies to `def`, but they may not know that it also applies to `attr*` methods. It would be easier to understand if we could write `attr*` methods in inline style.

#### Examples

#####

EnforcedStyle: group (default)

```
# bad
class Foo

  private def bar; end
  private def baz; end

end

# good
class Foo

  private

  def bar; end
  def baz; end

end
```

#####

EnforcedStyle: inline

```
# bad
class Foo

  private

  def bar; end
  def baz; end

end

# good
class Foo

  private def bar; end
  private def baz; end

end
```

#####

AllowModifiersOnSymbols: true (default)

```
# good
class Foo

  private :bar, :baz
  private *%i[qux quux]
  private *METHOD_NAMES
  private *private_methods

end
```

#####

AllowModifiersOnSymbols: false

```
# bad
class Foo

  private :bar, :baz
  private *%i[qux quux]
  private *METHOD_NAMES
  private *private_methods

end
```

#####

AllowModifiersOnAttrs: true (default)

```
# good
class Foo

  public attr_reader :bar
  protected attr_writer :baz
  private attr_accessor :qux
  private attr :quux

  def public_method; end

  private

  def private_method; end

end
```

#####

AllowModifiersOnAttrs: false

```
# bad
class Foo

  public attr_reader :bar
  protected attr_writer :baz
  private attr_accessor :qux
  private attr :quux

end
```

#####

AllowModifiersOnAliasMethod: true (default)

```
# good
class Foo

  public alias_method :bar, :foo
  protected alias_method :baz, :foo
  private alias_method :qux, :foo

end
```

#####

AllowModifiersOnAliasMethod: false

```
# bad
class Foo

  public alias_method :bar, :foo
  protected alias_method :baz, :foo
  private alias_method :qux, :foo

end
```

##

      Constant Summary
      collapse
    

    
      
        GROUP_STYLE_MESSAGE =
          
        
        

```
[
  '`%<access_modifier>s` should not be',
  'inlined in method definitions.'
].join(' ')
```

        INLINE_STYLE_MESSAGE =
          
        
        

```
[
  '`%<access_modifier>s` should be',
  'inlined in method definitions.'
].join(' ')
```

        RESTRICT_ON_SEND =
          
        
        

```
%i[private protected public module_function].freeze
```

### Constants included

     from RangeHelp

RangeHelp::BYTE_ORDER_MARK, RangeHelp::NOT_GIVEN

## Instance Attribute Summary

### Attributes inherited from Base

# config, #processed_source

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**access_modifier_with_alias_method?**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**access_modifier_with_attr?**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**access_modifier_with_symbol?**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**on_send**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods included from AutoCorrector

support_autocorrect?

### Methods included from ConfigurableEnforcedStyle

# alternative_style, #alternative_styles, #ambiguous_style_detected, #correct_style_detected, #detected_style, #detected_style=, #no_acceptable_style!, #no_acceptable_style?, #opposite_style_detected, #style, #style_configured?, #style_detected, #style_parameter_name, #supported_styles, #unexpected_style_detected

### Methods inherited from Base

# active_support_extensions_enabled?, #add_global_offense, #add_offense, #always_autocorrect?, autocorrect_incompatible_with, badge, #begin_investigation, #callbacks_needed, callbacks_needed, #config_to_allow_offenses, #config_to_allow_offenses=, #contextual_autocorrect?, #cop_config, cop_name, #cop_name, department, documentation_url, exclude_from_registry, #excluded_file?, #external_dependency_checksum, inherited, #initialize, #inspect, joining_forces, lint?, match?, #offenses, #on_investigation_end, #on_new_investigation, #on_other_file, #parse, #parser_engine, #ready, #relevant_file?, requires_gem, #string_literals_frozen_by_default?, support_autocorrect?, support_multiple_source?, #target_gem_version, #target_rails_version, #target_ruby_version

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
  
## Instance Method Details

###
  
    #**access_modifier_with_alias_method?**  ⇒ Object 
  

  

  

  
    
      

```

167
168
169
170
```

```
# File 'lib/rubocop/cop/style/access_modifier_declarations.rb', line 167

def_node_matcher :access_modifier_with_alias_method?, <<~PATTERN
  (send nil? {:private :protected :public :module_function}
    (send nil? :alias_method _ _))
PATTERN
```

###
  
    #**access_modifier_with_attr?**(node)  ⇒ Object 
  

  

  

  
    
      

```

161
162
163
164
```

```
# File 'lib/rubocop/cop/style/access_modifier_declarations.rb', line 161

def_node_matcher :access_modifier_with_attr?, <<~PATTERN
  (send nil? {:private :protected :public :module_function}
    (send nil? {:attr :attr_reader :attr_writer :attr_accessor} _+))
PATTERN
```

###
  
    #**access_modifier_with_symbol?**(node)  ⇒ Object 
  

  

  

  
    
      

```

154
155
156
157
158
```

```
# File 'lib/rubocop/cop/style/access_modifier_declarations.rb', line 154

def_node_matcher :access_modifier_with_symbol?, <<~PATTERN
  (send nil? {:private :protected :public :module_function}
    {(sym _)+ (splat {#percent_symbol_array? const send})}
  )
PATTERN
```

###
  
    #**on_send**(node)  ⇒ Object 
  

  

  

  
    
      

```

172
173
174
175
176
177
178
179
180
181
182
183
```

```
# File 'lib/rubocop/cop/style/access_modifier_declarations.rb', line 172

def on_send(node)
  return if allowed?(node)

  if offense?(node)
    add_offense(node.loc.selector) do |corrector|
      autocorrect(corrector, node)
    end
    opposite_style_detected
  else
    correct_style_detected
  end
end
```
