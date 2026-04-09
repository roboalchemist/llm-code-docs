# Class: Kramdown::Parser::Markdown
  
  
  

  
  
    Inherits:
    
      Kramdown
      
        

          
- Object
          
            
- Base
          
            
- Kramdown
          
            
- Kramdown::Parser::Markdown
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/kramdown/parser/markdown.rb
  
  

## Overview

  
    

Used for parsing a document in Markdown format.

This parser is based on the kramdown parser and removes the parser methods for the additional non-Markdown features. However, since some things are handled differently by the kramdown parser methods (like deciding when a list item contains just text), this parser differs from real Markdown parsers in some respects.

Note, though, that the parser basically fails just one of the Markdown test cases (some others also fail but those failures are negligible).

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        EXTENDED =
          
  
    

Array with all the parsing methods that should be removed from the standard kramdown parser.

  

  

        
        

```
[:codeblock_fenced, :table, :definition_list, :footnote_definition,
:abbrev_definition, :block_math, :block_extensions,
:footnote_marker, :smart_quotes, :inline_math, :span_extensions, :typographic_syms]

```

      
        BLOCK_BOUNDARY =
          
  
    

:stopdoc:

  

  

        
        

```
/#{BLANK_LINE}|#{EOB_MARKER}|\Z/

```

      
        LAZY_END =
          
        
        

```
/#{BLANK_LINE}|#{EOB_MARKER}|^#{OPT_SPACE}#{LAZY_END_HTML_STOP}|
^#{OPT_SPACE}#{LAZY_END_HTML_START}|\Z/x

```

      
        CODEBLOCK_MATCH =
          
        
        

```
/(?:#{BLANK_LINE}?(?:#{INDENT}[ \t]*\S.*\n)+)*/

```

      
        PARAGRAPH_END =
          
        
        

```
LAZY_END

```

      
        IAL_RAND_CHARS =
          
        
        

```
(('a'..'z').to_a + ('0'..'9').to_a)

```

      
        IAL_RAND_STRING =
          
        
        

```
(1..20).collect { IAL_RAND_CHARS[rand(IAL_RAND_CHARS.size)] }.join

```

      
        LIST_ITEM_IAL =
          
        
        

```
/^\s*(#{IAL_RAND_STRING})?\s*\n/

```

      
        IAL_SPAN_START =
          
        
        

```
LIST_ITEM_IAL

```

      
    
  

  
  
  
### Constants inherited
     from Kramdown

  

Kramdown::ABBREV_DEFINITION_START, Kramdown::ACHARS, Kramdown::ALD_ANY_CHARS, Kramdown::ALD_CLASS_NAME, Kramdown::ALD_ID_CHARS, Kramdown::ALD_ID_NAME, Kramdown::ALD_START, Kramdown::ALD_TYPE_ANY, Kramdown::ALD_TYPE_CLASS_NAME, Kramdown::ALD_TYPE_ID_NAME, Kramdown::ALD_TYPE_ID_OR_CLASS, Kramdown::ALD_TYPE_ID_OR_CLASS_MULTI, Kramdown::ALD_TYPE_KEY_VALUE_PAIR, Kramdown::ALD_TYPE_REF, Kramdown::ATX_HEADER_START, Kramdown::AUTOLINK_START, Kramdown::AUTOLINK_START_STR, Kramdown::BLANK_LINE, Kramdown::BLOCKQUOTE_START, Kramdown::BLOCK_EXTENSIONS_START, Kramdown::BLOCK_MATH_START, Kramdown::CODEBLOCK_START, Kramdown::CODESPAN_DELIMITER, Kramdown::DEFINITION_LIST_START, Kramdown::EMPHASIS_START, Kramdown::EOB_MARKER, Kramdown::ESCAPED_CHARS, Kramdown::EXT_BLOCK_START, Kramdown::EXT_BLOCK_STOP_STR, Kramdown::EXT_SPAN_START, Kramdown::EXT_START_STR, Kramdown::EXT_STOP_STR, Kramdown::FENCED_CODEBLOCK_MATCH, Kramdown::FENCED_CODEBLOCK_START, Kramdown::FOOTNOTE_DEFINITION_START, Kramdown::FOOTNOTE_MARKER_START, Kramdown::HR_START, Kramdown::HTML_BLOCK_START, Kramdown::HTML_MARKDOWN_ATTR_MAP, Kramdown::HTML_SPAN_START, Kramdown::IAL_BLOCK, Kramdown::IAL_BLOCK_START, Kramdown::IAL_CLASS_ATTR, Kramdown::INLINE_MATH_START, Kramdown::LAZY_END_HTML_SPAN_ELEMENTS, Kramdown::LAZY_END_HTML_START, Kramdown::LAZY_END_HTML_STOP, Kramdown::LINE_BREAK, Kramdown::LINK_BRACKET_STOP_RE, Kramdown::LINK_DEFINITION_START, Kramdown::LINK_INLINE_ID_RE, Kramdown::LINK_INLINE_TITLE_RE, Kramdown::LINK_PAREN_STOP_RE, Kramdown::LINK_START, Kramdown::LIST_ITEM_IAL_CHECK, Kramdown::LIST_START, Kramdown::LIST_START_OL, Kramdown::LIST_START_UL, Kramdown::PARAGRAPH_MATCH, Kramdown::PARAGRAPH_START, Kramdown::PARSE_FIRST_LIST_LINE_REGEXP_CACHE, Kramdown::PATTERN_TAIL, Kramdown::SETEXT_HEADER_START, Kramdown::SMART_QUOTES_RE, Kramdown::SPAN_EXTENSIONS_START, Kramdown::SQ_CLOSE, Kramdown::SQ_PUNCT, Kramdown::SQ_RULES, Kramdown::SQ_SUBSTS, Kramdown::TABLE_FSEP_LINE, Kramdown::TABLE_HSEP_ALIGN, Kramdown::TABLE_LINE, Kramdown::TABLE_PIPE_CHECK, Kramdown::TABLE_ROW_LINE, Kramdown::TABLE_SEP_LINE, Kramdown::TABLE_START, Kramdown::TRAILING_WHITESPACE, Kramdown::TYPOGRAPHIC_SYMS, Kramdown::TYPOGRAPHIC_SYMS_RE, Kramdown::TYPOGRAPHIC_SYMS_SUBST

  
  
  
### Constants included
     from Utils::Html

  

Utils::Html::ESCAPE_ALL_RE, Utils::Html::ESCAPE_ATTRIBUTE_RE, Utils::Html::ESCAPE_MAP, Utils::Html::ESCAPE_RE_FROM_TYPE, Utils::Html::ESCAPE_TEXT_RE, Utils::Html::REDUNDANT_LINE_BREAK_REGEX

  
  
  
### Constants included
     from Html::Parser

  

Html::Parser::HTML_RAW_START

  
  
  
### Constants included
     from Html::Constants

  

Html::Constants::HTML_ATTRIBUTE_RE, Html::Constants::HTML_BLOCK_ELEMENTS, Html::Constants::HTML_CDATA_RE, Html::Constants::HTML_COMMENT_RE, Html::Constants::HTML_CONTENT_MODEL, Html::Constants::HTML_CONTENT_MODEL_BLOCK, Html::Constants::HTML_CONTENT_MODEL_RAW, Html::Constants::HTML_CONTENT_MODEL_SPAN, Html::Constants::HTML_DOCTYPE_RE, Html::Constants::HTML_ELEMENT, Html::Constants::HTML_ELEMENTS_WITHOUT_BODY, Html::Constants::HTML_ENTITY_RE, Html::Constants::HTML_INSTRUCTION_RE, Html::Constants::HTML_SPAN_ELEMENTS, Html::Constants::HTML_TAG_CLOSE_RE, Html::Constants::HTML_TAG_RE

  
  
  
### Constants included
     from Kramdown

  

VERSION

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#options, #root, #source, #warnings

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(source, options)  ⇒ Markdown 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

:nodoc:.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Kramdown

  

#add_link, #after_block_boundary?, #before_block_boundary?, #correct_abbreviations_attributes, define_parser, #handle_extension, #handle_kramdown_html_tag, has_parser?, #normalize_link_id, #paragraph_end, #parse, #parse_abbrev_definition, #parse_attribute_list, #parse_atx_header, #parse_autolink, #parse_blank_line, #parse_block_extensions, #parse_block_html, #parse_block_math, #parse_blockquote, #parse_codeblock, #parse_codeblock_fenced, #parse_codespan, #parse_definition_list, #parse_emphasis, #parse_eob_marker, #parse_escaped_chars, #parse_extension_start_tag, #parse_first_list_line, #parse_footnote_definition, #parse_footnote_marker, #parse_horizontal_rule, #parse_html_entity, #parse_inline_math, #parse_line_break, #parse_link, #parse_link_definition, #parse_list, #parse_paragraph, #parse_setext_header, #parse_smart_quotes, #parse_span_extensions, #parse_span_html, #parse_table, #parse_typographic_syms, parser, #replace_abbreviations, #update_ial_with_ial

  
  
  
  
  
  
  
  
  
### Methods included from Utils::Html

  

#entity_to_str, #escape_html, #fix_cjk_line_break, #html_attributes

  
  
  
  
  
  
  
  
  
### Methods included from Html::Parser

  

#handle_html_start_tag, #handle_raw_html_tag, #parse_html_attributes, #parse_raw_html

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from Kramdown

  

data_dir

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#adapt_source, #add_text, #extract_string, #parse, parse, #warning

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(source, options)  ⇒ Markdown 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

32
33
34
35
36
```

    
    
      

```
# File 'lib/kramdown/parser/markdown.rb', line 32

def initialize(source, options) # :nodoc:
  super
  @block_parsers.delete_if {|i| EXTENDED.include?(i) }
  @span_parsers.delete_if {|i| EXTENDED.include?(i) }
end

```