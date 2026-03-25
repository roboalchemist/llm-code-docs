# Class: Kramdown::Parser::Kramdown
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- Kramdown::Parser::Kramdown
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Kramdown, Html::Parser, Utils::Html
  
  
  

  

  
  
    Defined in:
    lib/kramdown/parser/kramdown.rb,

  lib/kramdown/parser/kramdown/eob.rb,
 lib/kramdown/parser/kramdown/html.rb,
 lib/kramdown/parser/kramdown/link.rb,
 lib/kramdown/parser/kramdown/list.rb,
 lib/kramdown/parser/kramdown/math.rb,
 lib/kramdown/parser/kramdown/table.rb,
 lib/kramdown/parser/kramdown/header.rb,
 lib/kramdown/parser/kramdown/autolink.rb,
 lib/kramdown/parser/kramdown/codespan.rb,
 lib/kramdown/parser/kramdown/emphasis.rb,
 lib/kramdown/parser/kramdown/footnote.rb,
 lib/kramdown/parser/kramdown/codeblock.rb,
 lib/kramdown/parser/kramdown/paragraph.rb,
 lib/kramdown/parser/kramdown/blank_line.rb,
 lib/kramdown/parser/kramdown/blockquote.rb,
 lib/kramdown/parser/kramdown/extensions.rb,
 lib/kramdown/parser/kramdown/line_break.rb,
 lib/kramdown/parser/kramdown/html_entity.rb,
 lib/kramdown/parser/kramdown/abbreviation.rb,
 lib/kramdown/parser/kramdown/smart_quotes.rb,
 lib/kramdown/parser/kramdown/escaped_chars.rb,
 lib/kramdown/parser/kramdown/block_boundary.rb,
 lib/kramdown/parser/kramdown/horizontal_rule.rb,
 lib/kramdown/parser/kramdown/typographic_symbol.rb

  
  

## Overview

  
    

Used for parsing a document in kramdown format.

If you want to extend the functionality of the parser, you need to do the following:

- 

Create a new subclass

- 

add the needed parser methods

- 

modify the @block_parsers and @span_parsers variables and add the names of your parser methods

Here is a small example for an extended parser class that parses ERB style tags as raw text if they are used as span-level elements (an equivalent block-level parser should probably also be made to handle the block case):

```
require 'kramdown/parser/kramdown'

class Kramdown::Parser::ERBKramdown < Kramdown::Parser::Kramdown

   def initialize(source, options)
     super
     @span_parsers.unshift(:erb_tags)
   end

   ERB_TAGS_START = /<%.*?%>/

   def parse_erb_tags
     @src.pos += @src.matched_size
     @tree.children << Element.new(:raw, @src.matched)
   end
   define_parser(:erb_tags, ERB_TAGS_START, '<%')

end

```

The new parser can be used like this:

```
require 'kramdown/document'
# require the file with the above parser class

Kramdown::Document.new(input_text, :input => 'ERBKramdown').to_html

```

  

  

  
## Direct Known Subclasses

  

Markdown

## Defined Under Namespace

  
    
  
    
      **Classes:** Data
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        EOB_MARKER =
          
        
        

```
/^\^\s*?\n/

```

      
        HTML_MARKDOWN_ATTR_MAP =
          
  
    

Mapping of markdown attribute value to content model. I.e. :raw when “0”, :default when “1” (use default content model for the HTML element), :span when “span”, :block when block and for everything else `nil` is returned.

  

  

        
        

```
{"0" => :raw, "1" => :default, "span" => :span, "block" => :block}

```

      
        TRAILING_WHITESPACE =
          
        
        

```
/[ \t]*\n/

```

      
        HTML_BLOCK_START =
          
        
        

```
/^#{OPT_SPACE}<(#{REXML::Parsers::BaseParser::UNAME_STR}|!--|\/)/

```

      
        HTML_SPAN_START =
          
        
        

```
/<(#{REXML::Parsers::BaseParser::UNAME_STR}|!--|\/|!\[CDATA\[)/

```

      
        LINK_DEFINITION_START =
          
        
        

```
/^#{OPT_SPACE}\[([^\n\]]+)\]:[ \t]*(?:<(.*?)>|([^\n]*?\S[^\n]*?))(?:(?:[ \t]*?\n|[ \t]+?)[ \t]*?(["'])(.+?)\4)?[ \t]*?\n/

```

      
        LINK_BRACKET_STOP_RE =
          
        
        

```
/(\])|!?\[/

```

      
        LINK_PAREN_STOP_RE =
          
        
        

```
/(\()|(\))|\s(?=['"])/

```

      
        LINK_INLINE_ID_RE =
          
        
        

```
/\s*?\[([^\]]+)?\]/

```

      
        LINK_INLINE_TITLE_RE =
          
        
        

```
/\s*?(["'])(.+?)\1\s*?\)/m

```

      
        LINK_START =
          
        
        

```
/!?\[(?=[^^])/

```

      
        LIST_ITEM_IAL =
          
        
        

```
/^\s*(?:\{:(?!(?:#{ALD_ID_NAME})?:|\/)(#{ALD_ANY_CHARS}+)\})\s*/

```

      
        LIST_ITEM_IAL_CHECK =
          
        
        

```
/^#{LIST_ITEM_IAL}?\s*\n/

```

      
        PARSE_FIRST_LIST_LINE_REGEXP_CACHE =
          
        
        

```
Hash.new do |h, indentation|
  indent_re = /^ {#{indentation}}/
  content_re = /^(?:(?:\t| {4}){#{indentation / 4}} {#{indentation % 4}}|(?:\t| {4}){#{indentation / 4 + 1}}).*\S.*\n/
  lazy_re = /(?!^ {0,#{[indentation, 3].min}}(?:#{IAL_BLOCK}|#{LAZY_END_HTML_STOP}|#{LAZY_END_HTML_START})).*\S.*\n/

  h[indentation] = [content_re, lazy_re, indent_re]
end

```

      
        PATTERN_TAIL =
          
        
        

```
/[\t| ].*?\n/

```

      
        LIST_START_UL =
          
        
        

```
/^(#{OPT_SPACE}[+*-])(#{PATTERN_TAIL})/

```

      
        LIST_START_OL =
          
        
        

```
/^(#{OPT_SPACE}\d+\.)(#{PATTERN_TAIL})/

```

      
        LIST_START =
          
        
        

```
/#{LIST_START_UL}|#{LIST_START_OL}/

```

      
        DEFINITION_LIST_START =
          
        
        

```
/^(#{OPT_SPACE}:)(#{PATTERN_TAIL})/

```

      
        BLOCK_MATH_START =
          
        
        

```
/^#{OPT_SPACE}(\\)?\$\$(.*?)\$\$(\s*?\n)?/m

```

      
        INLINE_MATH_START =
          
        
        

```
/\$\$(.*?)\$\$/m

```

      
        TABLE_SEP_LINE =
          
        
        

```
/^([+|: \t-]*?-[+|: \t-]*?)[ \t]*\n/

```

      
        TABLE_HSEP_ALIGN =
          
        
        

```
/[ \t]?(:?)-+(:?)[ \t]?/

```

      
        TABLE_FSEP_LINE =
          
        
        

```
/^[+|: \t=]*?=[+|: \t=]*?[ \t]*\n/

```

      
        TABLE_ROW_LINE =
          
        
        

```
/^(.*?)[ \t]*\n/

```

      
        TABLE_PIPE_CHECK =
          
        
        

```
/(?:\||.*?[^\\\n]\|)/

```

      
        TABLE_LINE =
          
        
        

```
/#{TABLE_PIPE_CHECK}.*?\n/

```

      
        TABLE_START =
          
        
        

```
/^#{OPT_SPACE}(?=\S)#{TABLE_LINE}/

```

      
        SETEXT_HEADER_START =
          
        
        

```
/^#{OPT_SPACE}(?<contents>[^ \t].*)\n(?<level>[-=])[-=]*[ \t\r\f\v]*\n/

```

      
        ATX_HEADER_START =
          
        
        

```
/^(?<level>\#{1,6})[\t ]*(?<contents>[^ \t].*)\n/

```

      
        ACHARS =
          
        
        

```
'[[:alnum:]]-_.'

```

      
        AUTOLINK_START_STR =
          
        
        

```
"<((mailto|https?|ftps?):.+?|[#{ACHARS}]+?@[#{ACHARS}]+?)>"

```

      
        AUTOLINK_START =
          
        
        

```
/#{AUTOLINK_START_STR}/u

```

      
        CODESPAN_DELIMITER =
          
        
        

```
/`+/

```

      
        EMPHASIS_START =
          
        
        

```
/(?:\*\*?|__?)/

```

      
        FOOTNOTE_DEFINITION_START =
          
        
        

```
/^#{OPT_SPACE}\[\^(#{ALD_ID_NAME})\]:\s*?(.*?\n#{CODEBLOCK_MATCH})/

```

      
        FOOTNOTE_MARKER_START =
          
        
        

```
/\[\^(#{ALD_ID_NAME})\]/

```

      
        CODEBLOCK_START =
          
        
        

```
INDENT

```

      
        CODEBLOCK_MATCH =
          
        
        

```
/(?:#{BLANK_LINE}?(?:#{INDENT}[ \t]*\S.*\n)+(?:(?!#{IAL_BLOCK_START}|#{EOB_MARKER}|^#{OPT_SPACE}#{LAZY_END_HTML_STOP}|^#{OPT_SPACE}#{LAZY_END_HTML_START})^[ \t]*\S.*\n)*)*/

```

      
        FENCED_CODEBLOCK_START =
          
        
        

```
/^~{3,}/

```

      
        FENCED_CODEBLOCK_MATCH =
          
        
        

```
/^((~){3,})\s*?((\S+?)(?:\?\S*)?)?\s*?\n(.*?)^\1\2*\s*?\n/m

```

      
        LAZY_END_HTML_SPAN_ELEMENTS =
          
        
        

```
HTML_SPAN_ELEMENTS + %w[script]

```

      
        LAZY_END_HTML_START =
          
        
        

```
/<(?>(?!(?:#{LAZY_END_HTML_SPAN_ELEMENTS.join('|')})\b)#{REXML::Parsers::BaseParser::UNAME_STR})/

```

      
        LAZY_END_HTML_STOP =
          
        
        

```
/<\/(?!(?:#{LAZY_END_HTML_SPAN_ELEMENTS.join('|')})\b)#{REXML::Parsers::BaseParser::UNAME_STR}\s*>/m

```

      
        LAZY_END =
          
        
        

```
/#{BLANK_LINE}|#{IAL_BLOCK_START}|#{EOB_MARKER}|^#{OPT_SPACE}#{LAZY_END_HTML_STOP}|^#{OPT_SPACE}#{LAZY_END_HTML_START}|\Z/

```

      
        PARAGRAPH_START =
          
        
        

```
/^#{OPT_SPACE}[^ \t].*?\n/

```

      
        PARAGRAPH_MATCH =
          
        
        

```
/^.*?\n/

```

      
        PARAGRAPH_END =
          
        
        

```
/#{LAZY_END}|#{DEFINITION_LIST_START}/

```

      
        BLANK_LINE =
          
        
        

```
/(?>^\s*\n)+/

```

      
        BLOCKQUOTE_START =
          
        
        

```
/^#{OPT_SPACE}> ?/

```

      
        IAL_CLASS_ATTR =
          
        
        

```
'class'

```

      
        ALD_ID_CHARS =
          
        
        

```
/[\w-]/

```

      
        ALD_ANY_CHARS =
          
        
        

```
/\\\}|[^}]/

```

      
        ALD_ID_NAME =
          
        
        

```
/\w#{ALD_ID_CHARS}*/

```

      
        ALD_CLASS_NAME =
          
        
        

```
/[^\s.#]+/

```

      
        ALD_TYPE_KEY_VALUE_PAIR =
          
        
        

```
/(#{ALD_ID_NAME})=("|')((?:\\\}|\\\2|[^}\2])*?)\2/

```

      
        ALD_TYPE_CLASS_NAME =
          
        
        

```
/\.(#{ALD_CLASS_NAME})/

```

      
        ALD_TYPE_ID_NAME =
          
        
        

```
/#([A-Za-z][\w:-]*)/

```

      
        ALD_TYPE_ID_OR_CLASS =
          
        
        

```
/#{ALD_TYPE_ID_NAME}|#{ALD_TYPE_CLASS_NAME}/

```

      
        ALD_TYPE_ID_OR_CLASS_MULTI =
          
        
        

```
/((?:#{ALD_TYPE_ID_NAME}|#{ALD_TYPE_CLASS_NAME})+)/

```

      
        ALD_TYPE_REF =
          
        
        

```
/(#{ALD_ID_NAME})/

```

      
        ALD_TYPE_ANY =
          
        
        

```
/(?:\A|\s)(?:#{ALD_TYPE_KEY_VALUE_PAIR}|#{ALD_TYPE_REF}|#{ALD_TYPE_ID_OR_CLASS_MULTI})(?=\s|\Z)/

```

      
        ALD_START =
          
        
        

```
/^#{OPT_SPACE}\{:(#{ALD_ID_NAME}):(#{ALD_ANY_CHARS}+)\}\s*?\n/

```

      
        EXT_STOP_STR =
          
        
        

```
"\\{:/(%s)?\\}"

```

      
        EXT_START_STR =
          
        
        

```
"\\{::(\\w+)(?:\\s(#{ALD_ANY_CHARS}*?)|)(\\/)?\\}"

```

      
        EXT_BLOCK_START =
          
        
        

```
/^#{OPT_SPACE}(?:#{EXT_START_STR}|#{EXT_STOP_STR % ALD_ID_NAME})\s*?\n/

```

      
        EXT_BLOCK_STOP_STR =
          
        
        

```
"^#{OPT_SPACE}#{EXT_STOP_STR}\s*?\n"

```

      
        IAL_BLOCK =
          
        
        

```
/\{:(?!:|\/)(#{ALD_ANY_CHARS}+)\}\s*?\n/

```

      
        IAL_BLOCK_START =
          
        
        

```
/^#{OPT_SPACE}#{IAL_BLOCK}/

```

      
        BLOCK_EXTENSIONS_START =
          
        
        

```
/^#{OPT_SPACE}\{:/

```

      
        EXT_SPAN_START =
          
        
        

```
/#{EXT_START_STR}|#{EXT_STOP_STR % ALD_ID_NAME}/

```

      
        IAL_SPAN_START =
          
        
        

```
/\{:(#{ALD_ANY_CHARS}+)\}/

```

      
        SPAN_EXTENSIONS_START =
          
        
        

```
/\{:/

```

      
        LINE_BREAK =
          
        
        

```
/(  |\\\\)(?=\n)/

```

      
        ABBREV_DEFINITION_START =
          
        
        

```
/^#{OPT_SPACE}\*\[(.+?)\]:(.*?)\n/

```

      
        SQ_PUNCT =
          
        
        

```
'[!"#\$\%\'()*+,\-.\/:;<=>?\@\[\\\\\]\^_`{|}~]'

```

      
        SQ_CLOSE =
          
        
        

```
%![^ \\\\\t\r\n\\[{(-]!

```

      
        SQ_RULES =
          
        
        

```
[
  [/("|')(?=[_*]{1,2}\S)/, [:lquote1]],
  [/("|')(?=#{SQ_PUNCT}(?!\.\.)\B)/, [:rquote1]],
  # Special case for double sets of quotes, e.g.:
  #   <p>He said, "'Quoted' words in a larger quote."</p>
  [/(\s?)"'(?=\w)/, [1, :ldquo, :lsquo]],
  [/(\s?)'"(?=\w)/, [1, :lsquo, :ldquo]],
  # Special case for decade abbreviations (the '80s):
  [/(\s?)'(?=\d\ds)/, [1, :rsquo]],

  # Get most opening single/double quotes:
  [/(\s)('|")(?=\w)/, [1, :lquote2]],
  # Single/double closing quotes:
  [/(#{SQ_CLOSE})('|")/, [1, :rquote2]],
  # Special case for e.g. "<i>Custer</i>'s Last Stand."
  [/("|')(?=\s|s\b|$)/, [:rquote1]],
  # Any remaining single quotes should be opening ones:
  [/(.?)'/m, [1, :lsquo]],
  [/(.?)"/m, [1, :ldquo]],
]

```

      
        SQ_SUBSTS =
          
  
    

‘“

  

  

        
        

```
{
  [:rquote1, '"'] => :rdquo,
  [:rquote1, "'"] => :rsquo,
  [:rquote2, '"'] => :rdquo,
  [:rquote2, "'"] => :rsquo,
  [:lquote1, '"'] => :ldquo,
  [:lquote1, "'"] => :lsquo,
  [:lquote2, '"'] => :ldquo,
  [:lquote2, "'"] => :lsquo,
}

```

      
        SMART_QUOTES_RE =
          
        
        

```
/[^\\]?["']/

```

      
        ESCAPED_CHARS =
          
        
        

```
/\\([\\.*_+`<>()\[\]{}#!:|"'$=-])/

```

      
        BLOCK_BOUNDARY =
          
        
        

```
/#{BLANK_LINE}|#{EOB_MARKER}|#{IAL_BLOCK_START}|\Z/

```

      
        HR_START =
          
        
        

```
/^#{OPT_SPACE}(\*|-|_)[ \t]*\1[ \t]*\1(\1|[ \t])*\n/

```

      
        TYPOGRAPHIC_SYMS =
          
        
        

```
[['---', :mdash], ['--', :ndash], ['...', :hellip],
['\\<<', '<<'], ['\\>>', '>>'],
['<< ', :laquo_space], [' >>', :raquo_space],
['<<', :laquo], ['>>', :raquo]]

```

      
        TYPOGRAPHIC_SYMS_SUBST =
          
        
        

```

```

      
        TYPOGRAPHIC_SYMS_RE =
          
        
        

```
/#{TYPOGRAPHIC_SYMS.map {|k, _v| Regexp.escape(k) }.join('|')}/

```

      
    
  

  
  
  
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
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**define_parser**(name, start_re, span_start = nil, meth_name = "parse_#{name}")  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Add a parser method.

  

      
        
- 
  
    
      .**has_parser?**(name)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Return `true` if there is a parser called `name`.

  

      
        
- 
  
    
      .**parser**(name = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return the Data structure for the parser `name`.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**add_link**(el, href, title, alt_text = nil, ial = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

This helper methods adds the approriate attributes to the element `el` of type `a` or `img` and the element itself to the @tree.

  

      
        
- 
  
    
      #**after_block_boundary?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Return `true` if we are after a block boundary.

  

      
        
- 
  
    
      #**before_block_boundary?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Return `true` if we are before a block boundary.

  

      
        
- 
  
    
      #**correct_abbreviations_attributes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Correct abbreviation attributes.

  

      
        
- 
  
    
      #**handle_extension**(name, opts, body, type, line_no = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**handle_kramdown_html_tag**(el, closed, handle_body)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(source, options)  ⇒ Kramdown 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Create a new Kramdown parser object with the given `options`.

  

      
        
- 
  
    
      #**normalize_link_id**(id)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Normalize the link identifier.

  

      
        
- 
  
    
      #**paragraph_end**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**parse**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The source string provided on initialization is parsed into the @root element.

  

      
        
- 
  
    
      #**parse_abbrev_definition**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the link definition at the current location.

  

      
        
- 
  
    
      #**parse_attribute_list**(str, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the string `str` and extract all attributes and add all found attributes to the hash `opts`.

  

      
        
- 
  
    
      #**parse_atx_header**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the Atx header at the current location.

  

      
        
- 
  
    
      #**parse_autolink**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the autolink at the current location.

  

      
        
- 
  
    
      #**parse_blank_line**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the blank line at the current postition.

  

      
        
- 
  
    
      #**parse_block_extensions**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse one of the block extensions (ALD, block IAL or generic extension) at the current location.

  

      
        
- 
  
    
      #**parse_block_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the HTML at the current position as block-level HTML.

  

      
        
- 
  
    
      #**parse_block_math**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the math block at the current location.

  

      
        
- 
  
    
      #**parse_blockquote**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the blockquote at the current location.

  

      
        
- 
  
    
      #**parse_codeblock**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the indented codeblock at the current location.

  

      
        
- 
  
    
      #**parse_codeblock_fenced**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the fenced codeblock at the current location.

  

      
        
- 
  
    
      #**parse_codespan**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the codespan at the current scanner location.

  

      
        
- 
  
    
      #**parse_definition_list**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the ordered or unordered list at the current location.

  

      
        
- 
  
    
      #**parse_emphasis**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the emphasis at the current location.

  

      
        
- 
  
    
      #**parse_eob_marker**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the EOB marker at the current location.

  

      
        
- 
  
    
      #**parse_escaped_chars**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the backslash-escaped character at the current location.

  

      
        
- 
  
    
      #**parse_extension_start_tag**(type)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the generic extension at the current point.

  

      
        
- 
  
    
      #**parse_first_list_line**(indentation, content)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Used for parsing the first line of a list item or a definition, i.e.

  

      
        
- 
  
    
      #**parse_footnote_definition**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the foot note definition at the current location.

  

      
        
- 
  
    
      #**parse_footnote_marker**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the footnote marker at the current location.

  

      
        
- 
  
    
      #**parse_horizontal_rule**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the horizontal rule at the current location.

  

      
        
- 
  
    
      #**parse_html_entity**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the HTML entity at the current location.

  

      
        
- 
  
    
      #**parse_inline_math**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the inline math at the current location.

  

      
        
- 
  
    
      #**parse_line_break**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the line break at the current location.

  

      
        
- 
  
    
      #**parse_link**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the link at the current scanner position.

  

      
        
- 
  
    
      #**parse_link_definition**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the link definition at the current location.

  

      
        
- 
  
    
      #**parse_list**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the ordered or unordered list at the current location.

  

      
        
- 
  
    
      #**parse_paragraph**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the paragraph at the current location.

  

      
        
- 
  
    
      #**parse_setext_header**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the Setext header at the current location.

  

      
        
- 
  
    
      #**parse_smart_quotes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the smart quotes at current location.

  

      
        
- 
  
    
      #**parse_span_extensions**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the extension span at the current location.

  

      
        
- 
  
    
      #**parse_span_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the HTML at the current position as span-level HTML.

  

      
        
- 
  
    
      #**parse_table**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the table at the current location.

  

      
        
- 
  
    
      #**parse_typographic_syms**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the typographic symbols at the current location.

  

      
        
- 
  
    
      #**replace_abbreviations**(el, regexps = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Replace the abbreviation text with elements.

  

      
        
- 
  
    
      #**update_ial_with_ial**(ial, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Update the `ial` with the information from the inline attribute list `opts`.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Utils::Html

  

#entity_to_str, #escape_html, #fix_cjk_line_break, #html_attributes

  
  
  
  
  
  
  
  
  
### Methods included from Html::Parser

  

#handle_html_start_tag, #handle_raw_html_tag, #parse_html_attributes, #parse_raw_html

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from Kramdown

  

data_dir

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#adapt_source, #add_text, #extract_string, parse, #warning

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(source, options)  ⇒ Kramdown 
  

  

  

  
    

Create a new Kramdown parser object with the given `options`.

  

  

  
    
      

```

65
66
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
82
83
84
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown.rb', line 65

def initialize(source, options)
  super

  reset_env

  @alds = {}
  @footnotes = {}
  @link_defs = {}
  update_link_definitions(@options[:link_defs])

  @block_parsers = [:blank_line, :codeblock, :codeblock_fenced, :blockquote, :atx_header,
                    :horizontal_rule, :list, :definition_list, :block_html, :setext_header,
                    :block_math, :table, :footnote_definition, :link_definition,
                    :abbrev_definition, :block_extensions, :eob_marker, :paragraph]
  @span_parsers =  [:emphasis, :codespan, :autolink, :span_html, :footnote_marker, :link,
                    :smart_quotes, :inline_math, :span_extensions, :html_entity,
                    :typographic_syms, :line_break, :escaped_chars]

  @span_pattern_cache ||= Hash.new {|h, k| h[k] = {} }
end

```

    
  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**define_parser**(name, start_re, span_start = nil, meth_name = "parse_#{name}")  ⇒ Object 
  

  

  

  
    

Add a parser method

- 

with the given `name`,

- 

using `start_re` as start regexp

- 

and, for span parsers, `span_start` as a String that can be used in a regexp and which identifies the starting character(s)

to the registry. The method name is automatically derived from the `name` or can explicitly be set by using the `meth_name` parameter.

  

  

  
    
      

```

329
330
331
332
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown.rb', line 329

def self.define_parser(name, start_re, span_start = nil, meth_name = "parse_#{name}")
  raise "A parser with the name #{name} already exists!" if @@parsers.key?(name)
  @@parsers[name] = Data.new(name, start_re, span_start, meth_name)
end

```

    
  

    
      
  
### 
  
    .**has_parser?**(name)  ⇒ Boolean 
  

  

  

  
    

Return `true` if there is a parser called `name`.

  

  

  
    
      

```

340
341
342
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown.rb', line 340

def self.has_parser?(name)
  @@parsers.key?(name)
end

```

    
  

    
      
  
### 
  
    .**parser**(name = nil)  ⇒ Object 
  

  

  

  
    

Return the Data structure for the parser `name`.

  

  

  
    
      

```

335
336
337
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown.rb', line 335

def self.parser(name = nil)
  @@parsers[name]
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**add_link**(el, href, title, alt_text = nil, ial = nil)  ⇒ Object 
  

  

  

  
    

This helper methods adds the approriate attributes to the element `el` of type `a` or `img` and the element itself to the @tree.

  

  

  
    
      

```

39
40
41
42
43
44
45
46
47
48
49
50
51
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/link.rb', line 39

def add_link(el, href, title, alt_text = nil, ial = nil)
  el.options[:ial] = ial
  update_attr_with_ial(el.attr, ial) if ial
  if el.type == :a
    el.attr['href'] = href
  else
    el.attr['src'] = href
    el.attr['alt'] = alt_text
    el.children.clear
  end
  el.attr['title'] = title if title
  @tree.children << el
end

```

    
  

    
      
  
### 
  
    #**after_block_boundary?**  ⇒ Boolean 
  

  

  

  
    

Return `true` if we are after a block boundary.

  

  

  
    
      

```

21
22
23
24
25
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/block_boundary.rb', line 21

def after_block_boundary?
  last_child = @tree.children.last
  !last_child || last_child.type == :blank ||
    (last_child.type == :eob && last_child.value.nil?) || @block_ial
end

```

    
  

    
      
  
### 
  
    #**before_block_boundary?**  ⇒ Boolean 
  

  

  

  
    

Return `true` if we are before a block boundary.

  

  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/block_boundary.rb', line 28

def before_block_boundary?
  @src.check(self.class::BLOCK_BOUNDARY)
end

```

    
  

    
      
  
### 
  
    #**correct_abbreviations_attributes**  ⇒ Object 
  

  

  

  
    

Correct abbreviation attributes.

  

  

  
    
      

```

34
35
36
37
38
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/abbreviation.rb', line 34

def correct_abbreviations_attributes
  @root.options[:abbrev_attr].keys.each do |k|
    @root.options[:abbrev_attr][k] = @root.options[:abbrev_attr][k].attr
  end
end

```

    
  

    
      
  
### 
  
    #**handle_extension**(name, opts, body, type, line_no = nil)  ⇒ Object 
  

  

  

  
    
      

```

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
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/extensions.rb', line 96

def handle_extension(name, opts, body, type, line_no = nil)
  case name
  when 'comment'
    if body.kind_of?(String)
      @tree.children << Element.new(:comment, body, nil, category: type, location: line_no)
    end
    true
  when 'nomarkdown'
    if body.kind_of?(String)
      @tree.children << Element.new(:raw, body, nil, category: type,
                                    location: line_no, type: opts['type'].to_s.split(/\s+/))
    end
    true
  when 'options'
    opts.select do |k, v|
      k = k.to_sym
      if Kramdown::Options.defined?(k)
        if @options[:forbidden_inline_options].include?(k) ||
            k == :forbidden_inline_options
          warning("Option #{k} may not be set inline")
          next false
        end

        begin
          val = Kramdown::Options.parse(k, v)
          @options[k] = val
          (@root.options[:options] ||= {})[k] = val
        rescue StandardError
        end
        false
      else
        true
      end
    end.each do |k, _v|
      warning("Unknown kramdown option '#{k}'")
    end
    @tree.children << new_block_el(:eob, :extension) if type == :block
    true
  else
    false
  end
end

```

    
  

    
      
  
### 
  
    #**handle_kramdown_html_tag**(el, closed, handle_body)  ⇒ Object 
  

  

  

  
    
      

```

26
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
45
46
47
48
49
50
51
52
53
54
55
56
57
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
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/html.rb', line 26

def handle_kramdown_html_tag(el, closed, handle_body)
  if @block_ial
    el.options[:ial] = @block_ial
    @block_ial = nil
  end

  content_model = if @tree.type != :html_element || @tree.options[:content_model] != :raw
                    (@options[:parse_block_html] ? HTML_CONTENT_MODEL[el.value] : :raw)
                  else
                    :raw
                  end
  if (val = HTML_MARKDOWN_ATTR_MAP[el.attr.delete('markdown')])
    content_model = (val == :default ? HTML_CONTENT_MODEL[el.value] : val)
  end

  @src.scan(TRAILING_WHITESPACE) if content_model == :block
  el.options[:content_model] = content_model
  el.options[:is_closed] = closed

  if !closed && handle_body
    case content_model
    when :block
      unless parse_blocks(el)
        warning("Found no end tag for '#{el.value}' (line #{el.options[:location]}) - auto-closing it")
      end
    when :span
      curpos = @src.pos
      if @src.scan_until(/(?=<\/#{el.value}\s*>)/mi)
        add_text(extract_string(curpos...@src.pos, @src), el)
        @src.scan(HTML_TAG_CLOSE_RE)
      else
        add_text(@src.rest, el)
        @src.terminate
        warning("Found no end tag for '#{el.value}' (line #{el.options[:location]}) - auto-closing it")
      end
    else
      parse_raw_html(el) {|iel, ic, ih| handle_kramdown_html_tag(iel, ic, ih) }
    end
    unless @tree.type == :html_element && @tree.options[:content_model] == :raw
      @src.scan(TRAILING_WHITESPACE)
    end
  end
end

```

    
  

    
      
  
### 
  
    #**normalize_link_id**(id)  ⇒ Object 
  

  

  

  
    

Normalize the link identifier.

  

  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/link.rb', line 17

def normalize_link_id(id)
  id.gsub(/\s+/, ' ').downcase
end

```

    
  

    
      
  
### 
  
    #**paragraph_end**  ⇒ Object 
  

  

  

  
    
      

```

56
57
58
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/paragraph.rb', line 56

def paragraph_end
  self.class::PARAGRAPH_END
end

```

    
  

    
      
  
### 
  
    #**parse**  ⇒ Object 
  

  

  

  
    

The source string provided on initialization is parsed into the @root element.

  

  

  
    
      

```

88
89
90
91
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
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown.rb', line 88

def parse
  configure_parser
  parse_blocks(@root, adapt_source(source))
  update_tree(@root)
  correct_abbreviations_attributes
  replace_abbreviations(@root)
  @footnotes.each do |_name, data|
    update_tree(data[:content])
    replace_abbreviations(data[:content])
  end
  footnote_count = 0
  @footnotes.each do |name, data|
    (footnote_count += 1; next) if data.key?(:marker)
    line = data[:content].options[:location]
    warning("Footnote definition for '#{name}' on line #{line} is unreferenced - ignoring")
  end
  @root.options[:footnote_count] = footnote_count
end

```

    
  

    
      
  
### 
  
    #**parse_abbrev_definition**  ⇒ Object 
  

  

  

  
    

Parse the link definition at the current location.

  

  

  
    
      

```

17
18
19
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
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/abbreviation.rb', line 17

def parse_abbrev_definition
  start_line_number = @src.current_line_number
  @src.pos += @src.matched_size
  abbrev_id, abbrev_text = @src[1], @src[2]
  abbrev_text.strip!
  if @root.options[:abbrev_defs][abbrev_id]
    warning("Duplicate abbreviation ID '#{abbrev_id}' on line #{start_line_number} " \
            "- overwriting")
  end
  @tree.children << new_block_el(:eob, :abbrev_def)
  @root.options[:abbrev_defs][abbrev_id] = abbrev_text
  @root.options[:abbrev_attr][abbrev_id] = @tree.children.last
  true
end

```

    
  

    
      
  
### 
  
    #**parse_attribute_list**(str, opts)  ⇒ Object 
  

  

  

  
    

Parse the string `str` and extract all attributes and add all found attributes to the hash `opts`.

  

  

  
    
      

```

18
19
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
35
36
37
38
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/extensions.rb', line 18

def parse_attribute_list(str, opts)
  return if str.strip.empty? || str.strip == ':'
  attrs = str.scan(ALD_TYPE_ANY)
  attrs.each do |key, sep, val, ref, id_and_or_class, _, _|
    if ref
      (opts[:refs] ||= []) << ref
    elsif id_and_or_class
      id_and_or_class.scan(ALD_TYPE_ID_OR_CLASS).each do |id_attr, class_attr|
        if class_attr
          opts[IAL_CLASS_ATTR] = "#{opts[IAL_CLASS_ATTR]} #{class_attr}".lstrip
        else
          opts['id'] = id_attr
        end
      end
    else
      val.gsub!(/\\(\}|#{sep})/, "\\1")
      opts[key] = val
    end
  end
  warning("No or invalid attributes found in IAL/ALD content: #{str}") if attrs.empty?
end

```

    
  

    
      
  
### 
  
    #**parse_atx_header**  ⇒ Object 
  

  

  

  
    

Parse the Atx header at the current location.

  

  

  
    
      

```

32
33
34
35
36
37
38
39
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/header.rb', line 32

def parse_atx_header
  return false unless after_block_boundary?
  text, id = parse_header_contents
  text.sub!(/(?<!\\)#+\z/, '') && text.rstrip!
  return false if text.empty?
  add_header(@src["level"].length, text, id)
  true
end

```

    
  

    
      
  
### 
  
    #**parse_autolink**  ⇒ Object 
  

  

  

  
    

Parse the autolink at the current location.

  

  

  
    
      

```

19
20
21
22
23
24
25
26
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/autolink.rb', line 19

def parse_autolink
  start_line_number = @src.current_line_number
  @src.pos += @src.matched_size
  href = (@src[2].nil? ? "mailto:#{@src[1]}" : @src[1])
  el = Element.new(:a, nil, {'href' => href}, location: start_line_number)
  add_text(@src[1].sub(/^mailto:/, ''), el)
  @tree.children << el
end

```

    
  

    
      
  
### 
  
    #**parse_blank_line**  ⇒ Object 
  

  

  

  
    

Parse the blank line at the current postition.

  

  

  
    
      

```

17
18
19
20
21
22
23
24
25
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/blank_line.rb', line 17

def parse_blank_line
  @src.pos += @src.matched_size
  if (last_child = @tree.children.last) && last_child.type == :blank
    last_child.value << @src.matched
  else
    @tree.children << new_block_el(:blank, @src.matched)
  end
  true
end

```

    
  

    
      
  
### 
  
    #**parse_block_extensions**  ⇒ Object 
  

  

  

  
    

Parse one of the block extensions (ALD, block IAL or generic extension) at the current location.

  

  

  
    
      

```

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
178
179
180
181
182
183
184
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/extensions.rb', line 164

def parse_block_extensions
  if @src.scan(ALD_START)
    parse_attribute_list(@src[2], @alds[@src[1]] ||= {})
    @tree.children << new_block_el(:eob, :ald)
    true
  elsif @src.check(EXT_BLOCK_START)
    parse_extension_start_tag(:block)
  elsif @src.scan(IAL_BLOCK_START)
    if (last_child = @tree.children.last) && last_child.type != :blank &&
        (last_child.type != :eob ||
         [:link_def, :abbrev_def, :footnote_def].include?(last_child.value))
      parse_attribute_list(@src[1], last_child.options[:ial] ||= {})
      @tree.children << new_block_el(:eob, :ial) unless @src.check(IAL_BLOCK_START)
    else
      parse_attribute_list(@src[1], @block_ial ||= {})
    end
    true
  else
    false
  end
end

```

    
  

    
      
  
### 
  
    #**parse_block_html**  ⇒ Object 
  

  

  

  
    

Parse the HTML at the current position as block-level HTML.

  

  

  
    
      

```

73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/html.rb', line 73

def parse_block_html
  line = @src.current_line_number
  if (result = @src.scan(HTML_COMMENT_RE))
    @tree.children << Element.new(:xml_comment, result, nil, category: :block, location: line)
    @src.scan(TRAILING_WHITESPACE)
    true
  elsif @src.check(/^#{OPT_SPACE}#{HTML_TAG_RE}/o) && !HTML_SPAN_ELEMENTS.include?(@src[1].downcase)
    @src.pos += @src.matched_size
    handle_html_start_tag(line) {|iel, ic, ih| handle_kramdown_html_tag(iel, ic, ih) }
    Kramdown::Parser::Html::ElementConverter.convert(@root, @tree.children.last) if @options[:html_to_native]
    true
  elsif @src.check(/^#{OPT_SPACE}#{HTML_TAG_CLOSE_RE}/o) && !HTML_SPAN_ELEMENTS.include?(@src[1].downcase)
    name = @src[1].downcase

    if @tree.type == :html_element && @tree.value == name
      @src.pos += @src.matched_size
      throw :stop_block_parsing, :found
    else
      false
    end
  else
    false
  end
end

```

    
  

    
      
  
### 
  
    #**parse_block_math**  ⇒ Object 
  

  

  

  
    

Parse the math block at the current location.

  

  

  
    
      

```

19
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
35
36
37
38
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/math.rb', line 19

def parse_block_math
  start_line_number = @src.current_line_number
  if !after_block_boundary?
    return false
  elsif @src[1]
    @src.scan(/^#{OPT_SPACE}\\/o) if @src[3]
    return false
  end

  saved_pos = @src.save_pos
  @src.pos += @src.matched_size
  data = @src[2].strip
  if before_block_boundary?
    @tree.children << new_block_el(:math, data, nil, category: :block, location: start_line_number)
    true
  else
    @src.revert_pos(saved_pos)
    false
  end
end

```

    
  

    
      
  
### 
  
    #**parse_blockquote**  ⇒ Object 
  

  

  

  
    

Parse the blockquote at the current location.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/blockquote.rb', line 21

def parse_blockquote
  start_line_number = @src.current_line_number
  result = @src.scan(PARAGRAPH_MATCH)
  until @src.match?(self.class::LAZY_END)
    result << @src.scan(PARAGRAPH_MATCH)
  end
  result.gsub!(BLOCKQUOTE_START, '')

  el = new_block_el(:blockquote, nil, nil, location: start_line_number)
  @tree.children << el
  parse_blocks(el, result)
  true
end

```

    
  

    
      
  
### 
  
    #**parse_codeblock**  ⇒ Object 
  

  

  

  
    

Parse the indented codeblock at the current location.

  

  

  
    
      

```

23
24
25
26
27
28
29
30
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/codeblock.rb', line 23

def parse_codeblock
  start_line_number = @src.current_line_number
  data = @src.scan(self.class::CODEBLOCK_MATCH)
  data.gsub!(/\n( {0,3}\S)/, ' \\1')
  data.gsub!(INDENT, '')
  @tree.children << new_block_el(:codeblock, data, nil, location: start_line_number)
  true
end

```

    
  

    
      
  
### 
  
    #**parse_codeblock_fenced**  ⇒ Object 
  

  

  

  
    

Parse the fenced codeblock at the current location.

  

  

  
    
      

```

37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/codeblock.rb', line 37

def parse_codeblock_fenced
  if @src.check(self.class::FENCED_CODEBLOCK_MATCH)
    start_line_number = @src.current_line_number
    @src.pos += @src.matched_size
    el = new_block_el(:codeblock, @src[5], nil, location: start_line_number, fenced: true)
    lang = @src[3].to_s.strip
    unless lang.empty?
      el.options[:lang] = lang
      el.attr['class'] = "language-#{@src[4]}"
    end
    @tree.children << el
    true
  else
    false
  end
end

```

    
  

    
      
  
### 
  
    #**parse_codespan**  ⇒ Object 
  

  

  

  
    

Parse the codespan at the current scanner location.

  

  

  
    
      

```

17
18
19
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
45
46
47
48
49
50
51
52
53
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/codespan.rb', line 17

def parse_codespan
  start_line_number = @src.current_line_number
  result = @src.scan(CODESPAN_DELIMITER)
  simple = (result.length == 1)
  saved_pos = @src.save_pos

  if simple && @src.pre_match =~ /\s\Z|\A\Z/ && @src.match?(/\s/)
    add_text(result)
    return
  end

  # assign static regex to avoid allocating the same on every instance
  # where +result+ equals a single-backtick. Interpolate otherwise.
  if result == '`'
    scan_pattern = /`/
    str_sub_pattern = /`\Z/
  else
    scan_pattern = /#{result}/
    str_sub_pattern = /#{result}\Z/
  end

  if (text = @src.scan_until(scan_pattern))
    text.sub!(str_sub_pattern, '')
    unless simple
      text = text[1..-1] if text[0..0] == ' '
      text = text[0..-2] if text[-1..-1] == ' '
    end
    @tree.children << Element.new(:codespan, text, nil, {
                                    codespan_delimiter: result,
                                    location: start_line_number,
                                  })

  else
    @src.revert_pos(saved_pos)
    add_text(result)
  end
end

```

    
  

    
      
  
### 
  
    #**parse_definition_list**  ⇒ Object 
  

  

  

  
    

Parse the ordered or unordered list at the current location.

  

  

  
    
      

```

153
154
155
156
157
158
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
178
179
180
181
182
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
198
199
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
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/list.rb', line 153

def parse_definition_list
  children = @tree.children
  if !children.last || (children.length == 1 && children.last.type != :p) ||
      (children.length >= 2 && children[-1].type != :p &&
       (children[-1].type != :blank || children[-1].value != "\n" || children[-2].type != :p))
    return false
  end

  first_as_para = false
  deflist = new_block_el(:dl)
  para = @tree.children.pop
  if para.type == :blank
    para = @tree.children.pop
    first_as_para = true
  end
  # take location from preceding para which is the first definition term
  deflist.options[:location] = para.options[:location]
  para.children.first.value.split("\n").each do |term|
    el = Element.new(:dt, nil, nil, location: @src.current_line_number)
    term.sub!(self.class::LIST_ITEM_IAL) do
      parse_attribute_list($1, el.options[:ial] ||= {})
      ''
    end
    el.options[:raw_text] = term
    el.children << Element.new(:raw_text, term)
    deflist.children << el
  end
  deflist.options[:ial] = para.options[:ial]

  item = nil
  content_re, lazy_re, indent_re = nil
  def_start_re = DEFINITION_LIST_START
  last_is_blank = false
  until @src.eos?
    start_line_number = @src.current_line_number
    if @src.scan(def_start_re)
      item = Element.new(:dd, nil, nil, location: start_line_number)
      item.options[:first_as_para] = first_as_para
      item.value, indentation, content_re, lazy_re, indent_re =
        parse_first_list_line(@src[1].length, @src[2])
      deflist.children << item

      item.value.sub!(self.class::LIST_ITEM_IAL) do |_match|
        parse_attribute_list($1, item.options[:ial] ||= {})
        ''
      end

      def_start_re = fetch_pattern(:dl, indentation)
      first_as_para = false
      last_is_blank = false
    elsif @src.check(EOB_MARKER)
      break
    elsif (result = @src.scan(content_re)) || (!last_is_blank && (result = @src.scan(lazy_re)))
      result.sub!(/^(\t+)/) { " " * ($1 ? 4 * $1.length : 0) }
      result.sub!(indent_re, '')
      item.value << result
      first_as_para = false
      last_is_blank = false
    elsif (result = @src.scan(BLANK_LINE))
      first_as_para = true
      item.value << result
      last_is_blank = true
    else
      break
    end
  end

  last = nil
  deflist.children.each do |it|
    next if it.type == :dt

    parse_blocks(it, it.value)
    it.value = nil
    it_children = it.children
    next if it_children.empty?

    last = (it_children.last.type == :blank ? it_children.pop : nil)

    if it_children.first && it_children.first.type == :p && !it.options.delete(:first_as_para)
      it_children.first.children.first.value << "\n" if it_children.size > 1
      it_children.first.options[:transparent] = true
    end
  end

  children = @tree.children
  if children.length >= 1 && children.last.type == :dl
    children[-1].children.concat(deflist.children)
  elsif children.length >= 2 && children[-1].type == :blank &&
      children[-2].type == :dl
    children.pop
    children[-1].children.concat(deflist.children)
  else
    children << deflist
  end

  children << last if last

  true
end

```

    
  

    
      
  
### 
  
    #**parse_emphasis**  ⇒ Object 
  

  

  

  
    

Parse the emphasis at the current location.

  

  

  
    
      

```

17
18
19
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
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/emphasis.rb', line 17

def parse_emphasis
  start_line_number = @src.current_line_number
  saved_pos = @src.save_pos

  result = @src.scan(EMPHASIS_START)
  element = (result.length == 2 ? :strong : :em)
  type = result[0..0]

  if (type == '_' && @src.pre_match =~ /[[:alpha:]]-?[[:alpha:]]*_*\z/) || @src.check(/\s/) ||
      @tree.type == element || @stack.any? {|el, _| el.type == element }
    add_text(result)
    return
  end

  warnings_pos = @warnings.size
  sub_parse = lambda do |delim, elem|
    el = Element.new(elem, nil, nil, location: start_line_number)
    stop_re = /#{Regexp.escape(delim)}/
    found = parse_spans(el, stop_re) do
      (@src.pre_match[-1, 1] !~ /\s/) &&
        (elem != :em || !@src.match?(/#{Regexp.escape(delim * 2)}(?!#{Regexp.escape(delim)})/)) &&
        (type != '_' || !@src.match?(/#{Regexp.escape(delim)}[[:alnum:]]/)) && !el.children.empty?
    end
    [found, el, stop_re]
  end

  found, el, stop_re = sub_parse.call(result, element)
  if !found && element == :strong && @tree.type != :em
    @src.revert_pos(saved_pos)
    @src.pos += 1
    found, el, stop_re = sub_parse.call(type, :em)
  end
  if found
    # Useful for implementing underlines.
    el.options[:char] = type

    @src.scan(stop_re)
    @tree.children << el
  else
    @warnings.slice!(0...warnings_pos)
    @src.revert_pos(saved_pos)
    @src.pos += result.length
    add_text(result)
  end
end

```

    
  

    
      
  
### 
  
    #**parse_eob_marker**  ⇒ Object 
  

  

  

  
    

Parse the EOB marker at the current location.

  

  

  
    
      

```

17
18
19
20
21
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/eob.rb', line 17

def parse_eob_marker
  @src.pos += @src.matched_size
  @tree.children << new_block_el(:eob)
  true
end

```

    
  

    
      
  
### 
  
    #**parse_escaped_chars**  ⇒ Object 
  

  

  

  
    

Parse the backslash-escaped character at the current location.

  

  

  
    
      

```

17
18
19
20
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/escaped_chars.rb', line 17

def parse_escaped_chars
  @src.pos += @src.matched_size
  add_text(@src[1])
end

```

    
  

    
      
  
### 
  
    #**parse_extension_start_tag**(type)  ⇒ Object 
  

  

  

  
    

Parse the generic extension at the current point. The parameter `type` can either be :block or :span depending whether we parse a block or span extension tag.

  

  

  
    
      

```

54
55
56
57
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
82
83
84
85
86
87
88
89
90
91
92
93
94
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/extensions.rb', line 54

def parse_extension_start_tag(type)
  saved_pos = @src.save_pos
  start_line_number = @src.current_line_number
  @src.pos += @src.matched_size

  error_block = lambda do |msg|
    warning(msg)
    @src.revert_pos(saved_pos)
    add_text(@src.getch) if type == :span
    false
  end

  if @src[4] || @src.matched == '{:/}'
    name = (@src[4] ? "for '#{@src[4]}' " : '')
    return error_block.call("Invalid extension stop tag #{name} found on line " \
                            "#{start_line_number} - ignoring it")
  end

  ext = @src[1]
  opts = {}
  body = nil
  parse_attribute_list(@src[2] || '', opts)

  unless @src[3]
    stop_re = (type == :block ? /#{EXT_BLOCK_STOP_STR % ext}/ : /#{EXT_STOP_STR % ext}/)
    if (result = @src.scan_until(stop_re))
      body = result.sub!(stop_re, '')
      body.chomp! if type == :block
    else
      return error_block.call("No stop tag for extension '#{ext}' found on line " \
                              "#{start_line_number} - ignoring it")
    end
  end

  if handle_extension(ext, opts, body, type, start_line_number)
    true
  else
    error_block.call("Invalid extension with name '#{ext}' specified on line " \
                     "#{start_line_number} - ignoring it")
  end
end

```

    
  

    
      
  
### 
  
    #**parse_first_list_line**(indentation, content)  ⇒ Object 
  

  

  

  
    

Used for parsing the first line of a list item or a definition, i.e. the line with list item marker or the definition marker.

  

  

  
    
      

```

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
45
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/list.rb', line 32

def parse_first_list_line(indentation, content)
  if content.match?(self.class::LIST_ITEM_IAL_CHECK)
    indentation = 4
  else
    while content.match?(/^ *\t/)
      temp = content.scan(/^ */).first.length + indentation
      content.sub!(/^( *)(\t+)/) { $1 << " " * (4 - (temp % 4) + ($2.length - 1) * 4) }
    end
    indentation += content[/^ */].length
  end
  content.sub!(/^\s*/, '')

  [content, indentation, *PARSE_FIRST_LIST_LINE_REGEXP_CACHE[indentation]]
end

```

    
  

    
      
  
### 
  
    #**parse_footnote_definition**  ⇒ Object 
  

  

  

  
    

Parse the foot note definition at the current location.

  

  

  
    
      

```

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
# File 'lib/kramdown/parser/kramdown/footnote.rb', line 21

def parse_footnote_definition
  start_line_number = @src.current_line_number
  @src.pos += @src.matched_size

  el = Element.new(:footnote_def, nil, nil, location: start_line_number)
  parse_blocks(el, @src[2].gsub(INDENT, ''))
  if @footnotes[@src[1]]
    warning("Duplicate footnote name '#{@src[1]}' on line #{start_line_number} - overwriting")
  end
  @tree.children << new_block_el(:eob, :footnote_def)
  (@footnotes[@src[1]] = {})[:content] = el
  @footnotes[@src[1]][:eob] = @tree.children.last
  true
end

```

    
  

    
      
  
### 
  
    #**parse_footnote_marker**  ⇒ Object 
  

  

  

  
    

Parse the footnote marker at the current location.

  

  

  
    
      

```

40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/footnote.rb', line 40

def parse_footnote_marker
  start_line_number = @src.current_line_number
  @src.pos += @src.matched_size
  fn_def = @footnotes[@src[1]]
  if fn_def
    if fn_def[:eob]
      update_attr_with_ial(fn_def[:eob].attr, fn_def[:eob].options[:ial] || {})
      fn_def[:attr] = fn_def[:eob].attr
      fn_def[:options] = fn_def[:eob].options
      fn_def.delete(:eob)
    end
    fn_def[:marker] ||= []
    fn_def[:marker].push(Element.new(:footnote, fn_def[:content], fn_def[:attr],
                                     fn_def[:options].merge(name: @src[1], location: start_line_number)))
    @tree.children << fn_def[:marker].last
  else
    warning("Footnote definition for '#{@src[1]}' not found on line #{start_line_number}")
    add_text(@src.matched)
  end
end

```

    
  

    
      
  
### 
  
    #**parse_horizontal_rule**  ⇒ Object 
  

  

  

  
    

Parse the horizontal rule at the current location.

  

  

  
    
      

```

17
18
19
20
21
22
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/horizontal_rule.rb', line 17

def parse_horizontal_rule
  start_line_number = @src.current_line_number
  @src.pos += @src.matched_size
  @tree.children << new_block_el(:hr, nil, nil, location: start_line_number)
  true
end

```

    
  

    
      
  
### 
  
    #**parse_html_entity**  ⇒ Object 
  

  

  

  
    

Parse the HTML entity at the current location.

  

  

  
    
      

```

17
18
19
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
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/html_entity.rb', line 17

def parse_html_entity
  start_line_number = @src.current_line_number
  @src.pos += @src.matched_size
  begin
    value = ::Kramdown::Utils::Entities.entity(@src[1] || @src[2]&.to_i || @src[3].hex)
    @tree.children << Element.new(:entity, value,
                                  nil, original: @src.matched, location: start_line_number)
  rescue ::Kramdown::Error
    @tree.children << Element.new(:entity, ::Kramdown::Utils::Entities.entity('amp'),
                                  nil, location: start_line_number)
    add_text(@src.matched[1..-1])
  end
end

```

    
  

    
      
  
### 
  
    #**parse_inline_math**  ⇒ Object 
  

  

  

  
    

Parse the inline math at the current location.

  

  

  
    
      

```

44
45
46
47
48
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/math.rb', line 44

def parse_inline_math
  start_line_number = @src.current_line_number
  @src.pos += @src.matched_size
  @tree.children << Element.new(:math, @src[1].strip, nil, category: :span, location: start_line_number)
end

```

    
  

    
      
  
### 
  
    #**parse_line_break**  ⇒ Object 
  

  

  

  
    

Parse the line break at the current location.

  

  

  
    
      

```

17
18
19
20
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/line_break.rb', line 17

def parse_line_break
  @tree.children << Element.new(:br, nil, nil, location: @src.current_line_number)
  @src.pos += @src.matched_size
end

```

    
  

    
      
  
### 
  
    #**parse_link**  ⇒ Object 
  

  

  

  
    

Parse the link at the current scanner position. This method is used to parse normal links as well as image links.

  

  

  
    
      

```

61
62
63
64
65
66
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
82
83
84
85
86
87
88
89
90
91
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
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
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
142
143
144
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/link.rb', line 61

def parse_link
  start_line_number = @src.current_line_number
  result = @src.scan(LINK_START)
  cur_pos = @src.pos
  saved_pos = @src.save_pos

  link_type = (result.match?(/^!/) ? :img : :a)

  # no nested links allowed
  if link_type == :a && (@tree.type == :img || @tree.type == :a ||
                         @stack.any? {|t, _| t && (t.type == :img || t.type == :a) })
    add_text(result)
    return
  end
  el = Element.new(link_type, nil, nil, location: start_line_number)

  count = 1
  found = parse_spans(el, LINK_BRACKET_STOP_RE) do
    count += (@src[1] ? -1 : 1)
    count - el.children.count {|c| c.type == :img } == 0
  end
  unless found
    @src.revert_pos(saved_pos)
    add_text(result)
    return
  end
  alt_text = extract_string(cur_pos...@src.pos, @src).gsub(ESCAPED_CHARS, '\1')
  @src.scan(LINK_BRACKET_STOP_RE)

  # reference style link or no link url
  if @src.scan(LINK_INLINE_ID_RE) || !@src.check(/\(/)
    emit_warning = !@src[1]
    link_id = normalize_link_id(@src[1] || alt_text)
    if @link_defs.key?(link_id)
      link_def = @link_defs[link_id]
      add_link(el, link_def[0], link_def[1], alt_text,
               link_def[2] && link_def[2].options[:ial])
    else
      if emit_warning
        warning("No link definition for link ID '#{link_id}' found on line #{start_line_number}")
      end
      @src.revert_pos(saved_pos)
      add_text(result)
    end
    return
  end

  # link url in parentheses
  if @src.scan(/\(<(.*?)>/)
    link_url = @src[1]
    if @src.scan(/\)/)
      add_link(el, link_url, nil, alt_text)
      return
    end
  else
    link_url = +''
    nr_of_brackets = 0
    while (temp = @src.scan_until(LINK_PAREN_STOP_RE))
      link_url << temp
      if @src[2]
        nr_of_brackets -= 1
        break if nr_of_brackets == 0
      elsif @src[1]
        nr_of_brackets += 1
      else
        break
      end
    end
    link_url = link_url[1..-2]
    link_url.strip!

    if nr_of_brackets == 0
      add_link(el, link_url, nil, alt_text)
      return
    end
  end

  if @src.scan(LINK_INLINE_TITLE_RE)
    add_link(el, link_url, @src[2], alt_text)
  else
    @src.revert_pos(saved_pos)
    add_text(result)
  end
end

```

    
  

    
      
  
### 
  
    #**parse_link_definition**  ⇒ Object 
  

  

  

  
    

Parse the link definition at the current location.

  

  

  
    
      

```

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
# File 'lib/kramdown/parser/kramdown/link.rb', line 24

def parse_link_definition
  return false if @src[3].to_s.match?(/[ \t]+["']/)
  @src.pos += @src.matched_size
  link_id, link_url, link_title = normalize_link_id(@src[1]), @src[2] || @src[3], @src[5]
  if @link_defs[link_id]
    warning("Duplicate link ID '#{link_id}' on line #{@src.current_line_number} - overwriting")
  end
  @tree.children << new_block_el(:eob, :link_def)
  @link_defs[link_id] = [link_url, link_title, @tree.children.last]
  true
end

```

    
  

    
      
  
### 
  
    #**parse_list**  ⇒ Object 
  

  

  

  
    

Parse the ordered or unordered list at the current location.

  

  

  
    
      

```

54
55
56
57
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
82
83
84
85
86
87
88
89
90
91
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
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
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
142
143
144
145
146
147
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/list.rb', line 54

def parse_list
  start_line_number = @src.current_line_number
  type, list_start_re = (@src.check(LIST_START_UL) ? [:ul, LIST_START_UL] : [:ol, LIST_START_OL])
  list = new_block_el(type, nil, nil, location: start_line_number)

  item = nil
  content_re, lazy_re, indent_re = nil
  eob_found = false
  nested_list_found = false
  last_is_blank = false
  until @src.eos?
    start_line_number = @src.current_line_number
    if last_is_blank && @src.check(HR_START)
      break
    elsif @src.scan(EOB_MARKER)
      eob_found = true
      break
    elsif @src.scan(list_start_re)
      list.options[:first_list_marker] ||= @src[1].strip
      item = Element.new(:li, nil, nil, location: start_line_number)
      item.value, indentation, content_re, lazy_re, indent_re =
        parse_first_list_line(@src[1].length, @src[2])
      list.children << item

      item.value.sub!(self.class::LIST_ITEM_IAL) do
        parse_attribute_list($1, item.options[:ial] ||= {})
        ''
      end

      list_start_re = fetch_pattern(type, indentation)
      nested_list_found = (item.value =~ LIST_START)
      last_is_blank = false
      item.value = [item.value]
    elsif (result = @src.scan(content_re)) || (!last_is_blank && (result = @src.scan(lazy_re)))
      result.sub!(/^(\t+)/) { " " * 4 * $1.length }
      indentation_found = result.sub!(indent_re, '')
      if !nested_list_found && indentation_found && result =~ LIST_START
        item.value << +''
        nested_list_found = true
      elsif nested_list_found && !indentation_found && result =~ LIST_START
        result = " " * (indentation + 4) << result
      end
      item.value.last << result
      last_is_blank = false
    elsif (result = @src.scan(BLANK_LINE))
      nested_list_found = true
      last_is_blank = true
      item.value.last << result
    else
      break
    end
  end

  @tree.children << list

  last = nil
  list.children.each do |it|
    temp = Element.new(:temp, nil, nil, location: it.options[:location])

    env = save_env
    location = it.options[:location]
    it.value.each do |val|
      @src = ::Kramdown::Utils::StringScanner.new(val, location)
      parse_blocks(temp)
      location = @src.current_line_number
    end
    restore_env(env)

    it.children = temp.children
    it.value = nil

    it_children = it.children
    next if it_children.empty?

    # Handle the case where an EOB marker is inserted by a block IAL for the first paragraph
    it_children.delete_at(1) if it_children.first.type == :p &&
      it_children.length >= 2 && it_children[1].type == :eob && it_children.first.options[:ial]

    if it_children.first.type == :p &&
        (it_children.length < 2 || it_children[1].type != :blank ||
        (it == list.children.last && it_children.length == 2 && !eob_found)) &&
        (list.children.last != it || list.children.size == 1 ||
        list.children[0..-2].any? {|cit| !cit.children.first || cit.children.first.type != :p || cit.children.first.options[:transparent] })
      it_children.first.children.first.value << "\n" if it_children.size > 1 && it_children[1].type != :blank
      it_children.first.options[:transparent] = true
    end

    last = (it_children.last.type == :blank ? it_children.pop : nil)
  end

  @tree.children << last if !last.nil? && !eob_found

  true
end

```

    
  

    
      
  
### 
  
    #**parse_paragraph**  ⇒ Object 
  

  

  

  
    

Parse the paragraph at the current location.

  

  

  
    
      

```

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
45
46
47
48
49
50
51
52
53
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/paragraph.rb', line 31

def parse_paragraph
  pos = @src.pos
  start_line_number = @src.current_line_number
  result = @src.scan(PARAGRAPH_MATCH)
  until @src.match?(paragraph_end)
    result << @src.scan(PARAGRAPH_MATCH)
  end
  result.rstrip!
  if (last_child = @tree.children.last) && last_child.type == :p
    last_item_in_para = last_child.children.last
    if last_item_in_para && last_item_in_para.type == @text_type
      joiner = (extract_string((pos - 3)...pos, @src) == "  \n" ? "  \n" : "\n")
      last_item_in_para.value << joiner << result
    else
      add_text(result, last_child)
    end
  else
    @tree.children << new_block_el(:p, nil, nil, location: start_line_number)
    result.lstrip!
    add_text(result, @tree.children.last)
  end
  true
end

```

    
  

    
      
  
### 
  
    #**parse_setext_header**  ⇒ Object 
  

  

  

  
    

Parse the Setext header at the current location.

  

  

  
    
      

```

20
21
22
23
24
25
26
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/header.rb', line 20

def parse_setext_header
  return false unless after_block_boundary?
  text, id = parse_header_contents
  return false if text.empty?
  add_header(@src["level"] == '-' ? 2 : 1, text, id)
  true
end

```

    
  

    
      
  
### 
  
    #**parse_smart_quotes**  ⇒ Object 
  

  

  

  
    

Parse the smart quotes at current location.

  

  

  
    
      

```

158
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
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/smart_quotes.rb', line 158

def parse_smart_quotes
  start_line_number = @src.current_line_number
  substs = SQ_RULES.find {|reg, _subst| @src.scan(reg) }[1]
  substs.each do |subst|
    if subst.kind_of?(Integer)
      add_text(@src[subst])
    else
      val = SQ_SUBSTS[[subst, @src[subst.to_s[-1, 1].to_i]]] || subst
      @tree.children << Element.new(:smart_quote, val, nil, location: start_line_number)
    end
  end
end

```

    
  

    
      
  
### 
  
    #**parse_span_extensions**  ⇒ Object 
  

  

  

  
    

Parse the extension span at the current location.

  

  

  
    
      

```

192
193
194
195
196
197
198
199
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
# File 'lib/kramdown/parser/kramdown/extensions.rb', line 192

def parse_span_extensions
  if @src.check(EXT_SPAN_START)
    parse_extension_start_tag(:span)
  elsif @src.check(IAL_SPAN_START)
    if (last_child = @tree.children.last) && last_child.type != :text
      @src.pos += @src.matched_size
      attr = {}
      parse_attribute_list(@src[1], attr)
      update_ial_with_ial(last_child.options[:ial] ||= {}, attr)
      update_attr_with_ial(last_child.attr, attr)
    else
      warning("Found span IAL after text - ignoring it")
      add_text(@src.getch)
    end
  else
    add_text(@src.getch)
  end
end

```

    
  

    
      
  
### 
  
    #**parse_span_html**  ⇒ Object 
  

  

  

  
    

Parse the HTML at the current position as span-level HTML.

  

  

  
    
      

```

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
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
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
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/html.rb', line 102

def parse_span_html
  line = @src.current_line_number
  if (result = @src.scan(HTML_COMMENT_RE))
    @tree.children << Element.new(:xml_comment, result, nil, category: :span, location: line)
  elsif @src.scan(HTML_CDATA_RE)
    add_text(escape_html(@src[1]))
  elsif (result = @src.scan(HTML_TAG_CLOSE_RE))
    warning("Found invalidly used HTML closing tag for '#{@src[1]}' on line #{line}")
    add_text(result)
  elsif (result = @src.scan(HTML_TAG_RE))
    tag_name = @src[1]
    tag_name.downcase! if HTML_ELEMENT[tag_name.downcase]
    if HTML_BLOCK_ELEMENTS.include?(tag_name)
      warning("Found block HTML tag '#{tag_name}' in span-level text on line #{line}")
      add_text(result)
      return
    end

    attrs = parse_html_attributes(@src[2], line, HTML_ELEMENT[tag_name])
    attrs.each_value {|value| value.gsub!(/\n+/, ' ') unless value.empty? }

    do_parsing = if HTML_CONTENT_MODEL[tag_name] == :raw || @tree.options[:content_model] == :raw
                   false
                 else
                   @options[:parse_span_html]
                 end
    if (val = HTML_MARKDOWN_ATTR_MAP[attrs.delete('markdown')])
      case val
      when :block
        warning("Cannot use block-level parsing in span-level HTML tag (line #{line}) " \
                "- using default mode")
      when :span
        do_parsing = true
      when :default
        do_parsing = HTML_CONTENT_MODEL[tag_name] != :raw
      when :raw
        do_parsing = false
      end
    end

    el = Element.new(:html_element, tag_name, attrs, category: :span, location: line,
                     content_model: (do_parsing ? :span : :raw), is_closed: !@src[4].nil?)
    @tree.children << el
    stop_re = /<\/#{Regexp.escape(tag_name)}\s*>/
    stop_re = Regexp.new(stop_re.source, Regexp::IGNORECASE) if HTML_ELEMENT[tag_name]
    if !@src[4] && !HTML_ELEMENTS_WITHOUT_BODY.include?(el.value)
      if parse_spans(el, stop_re, (do_parsing ? nil : [:span_html]))
        @src.scan(stop_re)
      else
        warning("Found no end tag for '#{el.value}' (line #{line}) - auto-closing it")
        add_text(@src.rest, el)
        @src.terminate
      end
    end
    Kramdown::Parser::Html::ElementConverter.convert(@root, el) if @options[:html_to_native]
  else
    add_text(@src.getch)
  end
end

```

    
  

    
      
  
### 
  
    #**parse_table**  ⇒ Object 
  

  

  

  
    

Parse the table at the current location.

  

  

  
    
      

```

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
45
46
47
48
49
50
51
52
53
54
55
56
57
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
82
83
84
85
86
87
88
89
90
91
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
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
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
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/table.rb', line 25

def parse_table
  return false unless after_block_boundary?

  saved_pos = @src.save_pos
  orig_pos = @src.pos
  table = new_block_el(:table, nil, nil, alignment: [], location: @src.current_line_number)
  leading_pipe = (@src.check(TABLE_LINE) =~ /^\s*\|/)
  @src.scan(TABLE_SEP_LINE)

  rows = []
  has_footer = false
  columns = 0

  add_container = lambda do |type, force|
    if !has_footer || type != :tbody || force
      cont = Element.new(type)
      cont.children, rows = rows, []
      table.children << cont
    end
  end

  until @src.eos?
    break unless @src.check(TABLE_LINE)
    if @src.scan(TABLE_SEP_LINE)
      if rows.empty?
        # nothing to do, ignoring multiple consecutive separator lines
      elsif table.options[:alignment].empty? && !has_footer
        add_container.call(:thead, false)
        table.options[:alignment] = @src[1].scan(TABLE_HSEP_ALIGN).map do |left, right|
          (left.empty? && right.empty? && :default) || (right.empty? && :left) ||
            (left.empty? && :right) || :center
        end
      else # treat as normal separator line
        add_container.call(:tbody, false)
      end
    elsif @src.scan(TABLE_FSEP_LINE)
      add_container.call(:tbody, true) unless rows.empty?
      has_footer = true
    elsif @src.scan(TABLE_ROW_LINE)
      trow = Element.new(:tr)

      # parse possible code spans on the line and correctly split the line into cells
      env = save_env
      cells = []
      @src[1].split(/(<code.*?>.*?<\/code>)/).each_with_index do |str, i|
        if i.odd?
          (cells.empty? ? cells : cells.last) << str
        else
          reset_env(src: Kramdown::Utils::StringScanner.new(str, @src.current_line_number))
          root = Element.new(:root)
          parse_spans(root, nil, [:codespan])

          root.children.each do |c|
            if c.type == :raw_text
              f, *l = c.value.split(/(?<!\\)\|/, -1).map {|t| t.gsub(/\\\|/, '|') }
              (cells.empty? ? cells : cells.last) << f
              cells.concat(l)
            else
              delim = (c.value.scan(/`+/).max || '') + '`'
              tmp = +"#{delim}#{' ' if delim.size > 1}#{c.value}#{' ' if delim.size > 1}#{delim}"
              (cells.empty? ? cells : cells.last) << tmp
            end
          end
        end
      end
      restore_env(env)

      cells.shift if leading_pipe && cells.first.strip.empty?
      cells.pop if cells.last.strip.empty?
      cells.each do |cell_text|
        tcell = Element.new(:td)
        tcell.children << Element.new(:raw_text, cell_text.strip)
        trow.children << tcell
      end
      columns = [columns, cells.length].max
      rows << trow
    else
      break
    end
  end

  unless before_block_boundary?
    @src.revert_pos(saved_pos)
    return false
  end

  # Parse all lines of the table with the code span parser
  env = save_env
  l_src = ::Kramdown::Utils::StringScanner.new(extract_string(orig_pos...(@src.pos - 1), @src),
                                               @src.current_line_number)
  reset_env(src: l_src)
  root = Element.new(:root)
  parse_spans(root, nil, [:codespan, :span_html])
  restore_env(env)

  # Check if each line has at least one unescaped pipe that is not inside a code span/code
  # HTML element
  # Note: It doesn't matter that we parse *all* span HTML elements because the row splitting
  # algorithm above only takes <code> elements into account!
  pipe_on_line = false
  while (c = root.children.shift)
    next unless (lines = c.value)
    lines = lines.split("\n")
    if c.type == :codespan
      if lines.size > 2 || (lines.size == 2 && !pipe_on_line)
        break
      elsif lines.size == 2 && pipe_on_line
        pipe_on_line = false
      end
    else
      break if lines.size > 1 && !pipe_on_line && lines.first !~ /^#{TABLE_PIPE_CHECK}/o
      pipe_on_line = (lines.size > 1 ? false : pipe_on_line) || (lines.last =~ /^#{TABLE_PIPE_CHECK}/o)
    end
  end
  @src.revert_pos(saved_pos) and return false unless pipe_on_line

  add_container.call(has_footer ? :tfoot : :tbody, false) unless rows.empty?

  if table.children.none? {|el| el.type == :tbody }
    warning("Found table without body on line #{table.options[:location]} - ignoring it")
    @src.revert_pos(saved_pos)
    return false
  end

  # adjust all table rows to have equal number of columns, same for alignment defs
  table.children.each do |kind|
    kind.children.each do |row|
      (columns - row.children.length).times do
        row.children << Element.new(:td)
      end
    end
  end
  if table.options[:alignment].length > columns
    table.options[:alignment] = table.options[:alignment][0...columns]
  else
    table.options[:alignment] += [:default] * (columns - table.options[:alignment].length)
  end

  @tree.children << table

  true
end

```

    
  

    
      
  
### 
  
    #**parse_typographic_syms**  ⇒ Object 
  

  

  

  
    

Parse the typographic symbols at the current location.

  

  

  
    
      

```

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
35
36
37
38
39
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/typographic_symbol.rb', line 22

def parse_typographic_syms
  start_line_number = @src.current_line_number
  @src.pos += @src.matched_size
  val = TYPOGRAPHIC_SYMS_SUBST[@src.matched]
  if val.kind_of?(Symbol)
    @tree.children << Element.new(:typographic_sym, val, nil, location: start_line_number)
  elsif @src.matched == '\\<<'
    @tree.children << Element.new(:entity, ::Kramdown::Utils::Entities.entity('lt'),
                                  nil, location: start_line_number)
    @tree.children << Element.new(:entity, ::Kramdown::Utils::Entities.entity('lt'),
                                  nil, location: start_line_number)
  else
    @tree.children << Element.new(:entity, ::Kramdown::Utils::Entities.entity('gt'),
                                  nil, location: start_line_number)
    @tree.children << Element.new(:entity, ::Kramdown::Utils::Entities.entity('gt'),
                                  nil, location: start_line_number)
  end
end

```

    
  

    
      
  
### 
  
    #**replace_abbreviations**(el, regexps = nil)  ⇒ Object 
  

  

  

  
    

Replace the abbreviation text with elements.

  

  

  
    
      

```

41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
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
70
71
72
73
74
75
76
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/abbreviation.rb', line 41

def replace_abbreviations(el, regexps = nil)
  return if @root.options[:abbrev_defs].empty?
  unless regexps
    sorted_abbrevs = @root.options[:abbrev_defs].keys.sort {|a, b| b.length <=> a.length }
    regexps = [Regexp.union(*sorted_abbrevs.map do |k|
      /#{Regexp.escape(k).gsub(/\\\s/, "[\\s\\p{Z}]+").force_encoding(Encoding::UTF_8)}/
    end)]
    regexps << /(?=(?:\W|^)#{regexps.first}(?!\w))/ # regexp should only match on word boundaries
  end
  el.children.map! do |child|
    if child.type == :text && el.options[:content_model] != :raw
      if child.value.match?(regexps.first)
        result = []
        strscan = Kramdown::Utils::StringScanner.new(child.value, child.options[:location])
        text_lineno = strscan.current_line_number
        while (temp = strscan.scan_until(regexps.last))
          abbr_lineno = strscan.current_line_number
          abbr = strscan.scan(regexps.first) # begin of line case of abbr with \W char as first one
          if abbr.nil?
            temp << strscan.scan(/\W|^/)
            abbr = strscan.scan(regexps.first)
          end
          result << Element.new(:text, temp, nil, location: text_lineno)
          result << Element.new(:abbreviation, abbr, nil, location: abbr_lineno)
          text_lineno = strscan.current_line_number
        end
        result << Element.new(:text, strscan.rest, nil, location: text_lineno)
      else
        child
      end
    else
      replace_abbreviations(child, regexps)
      child
    end
  end.flatten!
end

```

    
  

    
      
  
### 
  
    #**update_ial_with_ial**(ial, opts)  ⇒ Object 
  

  

  

  
    

Update the `ial` with the information from the inline attribute list `opts`.

  

  

  
    
      

```

41
42
43
44
45
46
47
48
49
50
```

    
    
      

```
# File 'lib/kramdown/parser/kramdown/extensions.rb', line 41

def update_ial_with_ial(ial, opts)
  (ial[:refs] ||= []).concat(opts[:refs]) if opts.key?(:refs)
  opts.each do |k, v|
    if k == IAL_CLASS_ATTR
      ial[k] = "#{ial[k]} #{v}".lstrip
    elsif k.kind_of?(String)
      ial[k] = v
    end
  end
end

```