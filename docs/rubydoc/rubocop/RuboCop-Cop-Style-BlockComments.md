# Class: RuboCop::Cop::Style::BlockComments
  
    Inherits:
    
      Base
      
        

          
- Object

- Base

- RuboCop::Cop::Style::BlockComments

        show all
      
    
  
  

  
  
  
      Extended by:
      AutoCorrector
  
  
  
  
  
      Includes:
      RangeHelp
  
    Defined in:
    lib/rubocop/cop/style/block_comments.rb
  
## Overview

Looks for uses of block comments (=begin…=end).

#### Examples

```
# bad
=begin
Multiple lines
of comments...
=end

# good
# Multiple lines
# of comments...

```

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Do not use block comments.'

```

        BEGIN_LENGTH =
          
        
        

```
"=begin\n".length

```

        END_LENGTH =
          
        
        

```
"\n=end".length

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

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**on_new_investigation**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods included from AutoCorrector

support_autocorrect?

### Methods inherited from Base

# active_support_extensions_enabled?, #add_global_offense, #add_offense, #always_autocorrect?, autocorrect_incompatible_with, badge, #begin_investigation, #callbacks_needed, callbacks_needed, #config_to_allow_offenses, #config_to_allow_offenses=, #contextual_autocorrect?, #cop_config, cop_name, #cop_name, department, documentation_url, exclude_from_registry, #excluded_file?, #external_dependency_checksum, inherited, #initialize, #inspect, joining_forces, lint?, match?, #message, #offenses, #on_investigation_end, #on_other_file, #parse, #parser_engine, #ready, #relevant_file?, requires_gem, #string_literals_frozen_by_default?, support_autocorrect?, support_multiple_source?, #target_gem_version, #target_rails_version, #target_ruby_version

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
  
    #**on_new_investigation**  ⇒ Object 
  

  

  

  
    
      

```

27
28
29
30
31
32
33
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
```

```
# File 'lib/rubocop/cop/style/block_comments.rb', line 27

def on_new_investigation
  processed_source.comments.each do |comment|
    next unless comment.document?

    add_offense(comment) do |corrector|
      eq_begin, eq_end, contents = parts(comment)

      corrector.remove(eq_begin)
      unless contents.empty?
        corrector.replace(
          contents,
          contents.source.gsub(/\A/, '# ').gsub("\n\n", "\n#\n").gsub(/\n(?=[^#])/, "\n# ")
        )
      end
      corrector.remove(eq_end)
    end
  end
end

```
