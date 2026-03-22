# Class: Kramdown::Converter::Latex
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- Kramdown::Converter::Latex
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/kramdown/converter/latex.rb
  
  

## Overview

  
    

Converts an element tree to LaTeX.

This converter uses ideas from other Markdown-to-LaTeX converters like Pandoc and Maruku.

You can customize this converter by sub-classing it and overriding the `convert_NAME` methods. Each such method takes the following parameters:
`el`

The element of type `NAME` to be converted.
`opts`

A hash containing processing options that are passed down from parent elements. The key :parent is always set and contains the parent element as value.

The return value of such a method has to be a string containing the element `el` formatted correctly as LaTeX markup.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        TABLE_ALIGNMENT_CHAR =
          
  
    

:nodoc:

  

  

        
        

```
{default: 'l', left: 'l', center: 'c', right: 'r'}

```

      
        ENTITY_CONV_TABLE =
          
  
    

Inspired by Maruku: entity conversion table based on the one from htmltolatex (sourceforge.net/projects/htmltolatex/), with some small adjustments/additions

  

  

        
        

```
{
  913 => ['$A$'],
  914 => ['$B$'],
  915 => ['$\Gamma$'],
  916 => ['$\Delta$'],
  917 => ['$E$'],
  918 => ['$Z$'],
  919 => ['$H$'],
  920 => ['$\Theta$'],
  921 => ['$I$'],
  922 => ['$K$'],
  923 => ['$\Lambda$'],
  924 => ['$M$'],
  925 => ['$N$'],
  926 => ['$\Xi$'],
  927 => ['$O$'],
  928 => ['$\Pi$'],
  929 => ['$P$'],
  931 => ['$\Sigma$'],
  932 => ['$T$'],
  933 => ['$Y$'],
  934 => ['$\Phi$'],
  935 => ['$X$'],
  936 => ['$\Psi$'],
  937 => ['$\Omega$'],
  945 => ['$\alpha$'],
  946 => ['$\beta$'],
  947 => ['$\gamma$'],
  948 => ['$\delta$'],
  949 => ['$\epsilon$'],
  950 => ['$\zeta$'],
  951 => ['$\eta$'],
  952 => ['$\theta$'],
  953 => ['$\iota$'],
  954 => ['$\kappa$'],
  955 => ['$\lambda$'],
  956 => ['$\mu$'],
  957 => ['$\nu$'],
  958 => ['$\xi$'],
  959 => ['$o$'],
  960 => ['$\pi$'],
  961 => ['$\rho$'],
  963 => ['$\sigma$'],
  964 => ['$\tau$'],
  965 => ['$\upsilon$'],
  966 => ['$\phi$'],
  967 => ['$\cchi$'],
  968 => ['$\psi$'],
  969 => ['$\omega$'],
  962 => ['$\varsigma$'],
  977 => ['$\vartheta$'],
  982 => ['$\varpi$'],
  8230 => ['\ldots'],
  8242 => ['$\prime$'],
  8254 => ['-'],
  8260 => ['/'],
  8472 => ['$\wp$'],
  8465 => ['$\Im$'],
  8476 => ['$\Re$'],
  8501 => ['$\aleph$'],
  8226 => ['$\bullet$'],
  8482 => ['$^{\rm TM}$'],
  8592 => ['$\leftarrow$'],
  8594 => ['$\rightarrow$'],
  8593 => ['$\uparrow$'],
  8595 => ['$\downarrow$'],
  8596 => ['$\leftrightarrow$'],
  8629 => ['$\hookleftarrow$'],
  8657 => ['$\Uparrow$'],
  8659 => ['$\Downarrow$'],
  8656 => ['$\Leftarrow$'],
  8658 => ['$\Rightarrow$'],
  8660 => ['$\Leftrightarrow$'],
  8704 => ['$\forall$'],
  8706 => ['$\partial$'],
  8707 => ['$\exists$'],
  8709 => ['$\emptyset$'],
  8711 => ['$\nabla$'],
  8712 => ['$\in$'],
  8715 => ['$\ni$'],
  8713 => ['$\notin$'],
  8721 => ['$\sum$'],
  8719 => ['$\prod$'],
  8722 => ['$-$'],
  8727 => ['$\ast$'],
  8730 => ['$\surd$'],
  8733 => ['$\propto$'],
  8734 => ['$\infty$'],
  8736 => ['$\angle$'],
  8743 => ['$\wedge$'],
  8744 => ['$\vee$'],
  8745 => ['$\ccap$'],
  8746 => ['$\ccup$'],
  8747 => ['$\int$'],
  8756 => ['$\therefore$', 'amssymb'],
  8764 => ['$\sim$'],
  8776 => ['$\approx$'],
  8773 => ['$\ccong$'],
  8800 => ['$\neq$'],
  8801 => ['$\equiv$'],
  8804 => ['$\leq$'],
  8805 => ['$\geq$'],
  8834 => ['$\subset$'],
  8835 => ['$\supset$'],
  8838 => ['$\subseteq$'],
  8839 => ['$\supseteq$'],
  8836 => ['$\nsubset$', 'amssymb'],
  8853 => ['$\oplus$'],
  8855 => ['$\otimes$'],
  8869 => ['$\perp$'],
  8901 => ['$\ccdot$'],
  8968 => ['$\rceil$'],
  8969 => ['$\lceil$'],
  8970 => ['$\lfloor$'],
  8971 => ['$\rfloor$'],
  9001 => ['$\rangle$'],
  9002 => ['$\langle$'],
  9674 => ['$\lozenge$', 'amssymb'],
  9824 => ['$\spadesuit$'],
  9827 => ['$\cclubsuit$'],
  9829 => ['$\heartsuit$'],
  9830 => ['$\diamondsuit$'],
  38 => ['\&'],
  34 => ['"'],
  39 => ['\''],
  169 => ['\ccopyright'],
  60 => ['\textless'],
  62 => ['\textgreater'],
  338 => ['\OE'],
  339 => ['\oe'],
  352 => ['\v{S}'],
  353 => ['\v{s}'],
  376 => ['\"Y'],
  710 => ['\textasciicircum'],
  732 => ['\textasciitilde'],
  8211 => ['--'],
  8212 => ['---'],
  8216 => ['`'],
  8217 => ['\''],
  8220 => ['``'],
  8221 => ['\'\''],
  8224 => ['\dag'],
  8225 => ['\ddag'],
  8240 => ['\permil', 'wasysym'],
  8364 => ['\euro', 'eurosym'],
  8249 => ['\guilsinglleft'],
  8250 => ['\guilsinglright'],
  8218 => ['\quotesinglbase', 'mathcomp'],
  8222 => ['\quotedblbase', 'mathcomp'],
  402 => ['\textflorin', 'mathcomp'],
  381 => ['\v{Z}'],
  382 => ['\v{z}'],
  160 => ['~'],
  161 => ['\textexclamdown'],
  163 => ['\pounds'],
  164 => ['\ccurrency', 'wasysym'],
  165 => ['\textyen', 'textcomp'],
  166 => ['\brokenvert', 'wasysym'],
  167 => ['\S'],
  171 => ['\guillemotleft'],
  187 => ['\guillemotright'],
  174 => ['\textregistered'],
  170 => ['\textordfeminine'],
  172 => ['$\neg$'],
  173 => ['\-'],
  176 => ['$\degree$', 'mathabx'],
  177 => ['$\pm$'],
  180 => ['\''],
  181 => ['$\mu$'],
  182 => ['\P'],
  183 => ['$\ccdot$'],
  186 => ['\textordmasculine'],
  162 => ['\ccent', 'wasysym'],
  185 => ['$^1$'],
  178 => ['$^2$'],
  179 => ['$^3$'],
  189 => ['$\frac{1}{2}$'],
  188 => ['$\frac{1}{4}$'],
  190 => ['$\frac{3}{4}'],
  192 => ['\`A'],
  193 => ['\\\'A'],
  194 => ['\^A'],
  195 => ['\~A'],
  196 => ['\"A'],
  197 => ['\AA'],
  198 => ['\AE'],
  199 => ['\ccC'],
  200 => ['\`E'],
  201 => ['\\\'E'],
  202 => ['\^E'],
  203 => ['\"E'],
  204 => ['\`I'],
  205 => ['\\\'I'],
  206 => ['\^I'],
  207 => ['\"I'],
  208 => ['$\eth$', 'amssymb'],
  209 => ['\~N'],
  210 => ['\`O'],
  211 => ['\\\'O'],
  212 => ['\^O'],
  213 => ['\~O'],
  214 => ['\"O'],
  215 => ['$\times$'],
  216 => ['\O'],
  217 => ['\`U'],
  218 => ['\\\'U'],
  219 => ['\^U'],
  220 => ['\"U'],
  221 => ['\\\'Y'],
  222 => ['\Thorn', 'wasysym'],
  223 => ['\ss'],
  224 => ['\`a'],
  225 => ['\\\'a'],
  226 => ['\^a'],
  227 => ['\~a'],
  228 => ['\"a'],
  229 => ['\aa'],
  230 => ['\ae'],
  231 => ['\ccc'],
  232 => ['\`e'],
  233 => ['\\\'e'],
  234 => ['\^e'],
  235 => ['\"e'],
  236 => ['\`i'],
  237 => ['\\\'i'],
  238 => ['\^i'],
  239 => ['\"i'],
  240 => ['$\eth$'],
  241 => ['\~n'],
  242 => ['\`o'],
  243 => ['\\\'o'],
  244 => ['\^o'],
  245 => ['\~o'],
  246 => ['\"o'],
  247 => ['$\divide$'],
  248 => ['\o'],
  249 => ['\`u'],
  250 => ['\\\'u'],
  251 => ['\^u'],
  252 => ['\"u'],
  253 => ['\\\'y'],
  254 => ['\thorn', 'wasysym'],
  255 => ['\"y'],
  8201 => ['\thinspace'],
  8194 => ['\hskip .5em\relax'],
  8195 => ['\quad'],
}

```

      
        TYPOGRAPHIC_SYMS =
          
        
        

```
{
  mdash: '---', ndash: '--', hellip: '\ldots{}',
  laquo_space: '\guillemotleft{}~', raquo_space: '~\guillemotright{}',
  laquo: '\guillemotleft{}', raquo: '\guillemotright{}'
}

```

      
        ESCAPE_MAP =
          
        
        

```
{
  "^"  => "\\^{}",
  "\\" => "\\textbackslash{}",
  "~"  => "\\ensuremath{\\sim}",
  "|"  => "\\textbar{}",
  "<"  => "\\textless{}",
  ">"  => "\\textgreater{}",
  "["  => "{[}",
  "]"  => "{]}",
}.merge(Hash[*"{}$%&_#".each_char.map {|c| [c, "\\#{c}"] }.flatten])

```

      
        ESCAPE_RE =
          
  
    

:nodoc:

  

  

        
        

```
Regexp.union(*ESCAPE_MAP.collect {|k, _v| k })

```

      
    
  

  
  
  
### Constants inherited
     from Base

  

Base::SMART_QUOTE_INDICES

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#data, #options, #root, #warnings

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**attribute_list**(el)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return a LaTeX comment containing all attributes as ‘key=“value”’ pairs.

  

      
        
- 
  
    
      #**convert**(el, opts = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Dispatch the conversion of the element `el` to a `convert_TYPE` method using the `type` of the element.

  

      
        
- 
  
    
      #**convert_a**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_abbreviation**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_blank**(_el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_blockquote**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_br**(_el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_codeblock**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_codespan**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_comment**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_dd**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_dl**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_dt**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_em**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_entity**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_footnote**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_header**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_hr**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_html_element**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_img**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_li**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_math**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_p**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_raw**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_root**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_smart_quote**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_standalone_image**(el, _opts, img)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Helper method used by `convert_p` to convert a paragraph that only contains a single :img element.

  

      
        
- 
  
    
      #**convert_strong**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_table**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_tbody**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_td**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_text**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_tfoot**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_thead**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_tr**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_typographic_sym**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**convert_ul**(el, opts)  ⇒ Object 
    

    
      (also: #convert_ol)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_xml_comment**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_xml_pi**(_el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**entity_to_latex**(entity)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**escape**(str)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Escape the special LaTeX characters in the string `str`.

  

      
        
- 
  
    
      #**initialize**(root, options)  ⇒ Latex 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize the LaTeX converter with the `root` element and the conversion `options`.

  

      
        
- 
  
    
      #**inner**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return the converted content of the children of `el` as a string.

  

      
        
- 
  
    
      #**latex_environment**(type, el, text)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Wrap the `text` inside a LaTeX environment of type `type`.

  

      
        
- 
  
    
      #**latex_link_target**(el, add_label = false)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return a string containing a valid hypertarget command if the element has an ID defined, or `nil` otherwise.

  

      
        
- 
  
    
      #**normalize_abbreviation_key**(key)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Normalize the abbreviation key so that it only contains allowed ASCII character.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

apply_template, #apply_template_after?, #apply_template_before?, #basic_generate_id, convert, #extract_code_language, #extract_code_language!, #format_math, #generate_id, get_template, #highlight_code, #in_toc?, #output_header_level, #smart_quote_entity, #warning

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(root, options)  ⇒ Latex 
  

  

  

  
    

Initialize the LaTeX converter with the `root` element and the conversion `options`.

  

  

  
    
      

```

34
35
36
37
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 34

def initialize(root, options)
  super
  @data[:packages] = Set.new
end

```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**attribute_list**(el)  ⇒ Object 
  

  

  

  
    

Return a LaTeX comment containing all attributes as ‘key=“value”’ pairs.

  

  

  
    
      

```

600
601
602
603
604
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 600

def attribute_list(el)
  attrs = el.attr.map {|k, v| v.nil? ? '' : " #{k}=\"#{v}\"" }.compact.sort.join
  attrs = "   % #{attrs}" unless attrs.empty?
  attrs
end

```

    
  

    
      
  
### 
  
    #**convert**(el, opts = {})  ⇒ Object 
  

  

  

  
    

Dispatch the conversion of the element `el` to a `convert_TYPE` method using the `type` of the element.

  

  

  
    
      

```

41
42
43
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 41

def convert(el, opts = {})
  send("convert_#{el.type}", el, opts)
end

```

    
  

    
      
  
### 
  
    #**convert_a**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

217
218
219
220
221
222
223
224
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 217

def convert_a(el, opts)
  url = el.attr['href']
  if url.start_with?('#')
    "\\hyperlink{#{url[1..-1].gsub('%', '\\%')}}{#{inner(el, opts)}}"
  else
    "\\href{#{url.gsub('%', '\\%')}}{#{inner(el, opts)}}"
  end
end

```

    
  

    
      
  
### 
  
    #**convert_abbreviation**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

570
571
572
573
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 570

def convert_abbreviation(el, _opts)
  @data[:packages] += %w[acronym]
  "\\ac{#{normalize_abbreviation_key(el.value)}}"
end

```

    
  

    
      
  
### 
  
    #**convert_blank**(_el, opts)  ⇒ Object 
  

  

  

  
    
      

```

61
62
63
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 61

def convert_blank(_el, opts)
  opts[:result].match?(/\n\n\Z|\A\Z/) ? "" : "\n"
end

```

    
  

    
      
  
### 
  
    #**convert_blockquote**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

110
111
112
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 110

def convert_blockquote(el, opts)
  latex_environment(el.children.size > 1 ? 'quotation' : 'quote', el, inner(el, opts))
end

```

    
  

    
      
  
### 
  
    #**convert_br**(_el, opts)  ⇒ Object 
  

  

  

  
    
      

```

210
211
212
213
214
215
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 210

def convert_br(_el, opts)
  res = +"\\newline"
  res << "\n" if (c = opts[:parent].children[opts[:index] + 1]) &&
    (c.type != :text || c.value !~ /^\s*\n/)
  res
end

```

    
  

    
      
  
### 
  
    #**convert_codeblock**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 87

def convert_codeblock(el, _opts)
  show_whitespace = el.attr['class'].to_s =~ /\bshow-whitespaces\b/
  lang = extract_code_language(el.attr)

  if @options[:syntax_highlighter] == :minted &&
      (highlighted_code = highlight_code(el.value, lang, :block))
    @data[:packages] << 'minted'
    "#{latex_link_target(el)}#{highlighted_code}\n"
  elsif show_whitespace || lang
    options = []
    options << (show_whitespace ? "showspaces=true,showtabs=true" : "showspaces=false,showtabs=false")
    options << "language=#{lang}" if lang
    options << "basicstyle=\\ttfamily\\footnotesize,columns=fixed,frame=tlbr"
    id = el.attr['id']
    options << "label=#{id}" if id
    attrs = attribute_list(el)
    "#{latex_link_target(el)}\\begin{lstlisting}[#{options.join(',')}]\n" \
      "#{el.value}\n\\end{lstlisting}#{attrs}\n"
  else
    "#{latex_link_target(el)}\\begin{verbatim}#{el.value}\\end{verbatim}\n"
  end
end

```

    
  

    
      
  
### 
  
    #**convert_codespan**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 240

def convert_codespan(el, _opts)
  lang = extract_code_language(el.attr)
  if @options[:syntax_highlighter] == :minted &&
      (highlighted_code = highlight_code(el.value, lang, :span))
    @data[:packages] << 'minted'
    "#{latex_link_target(el)}#{highlighted_code}"
  else
    "\\texttt{#{latex_link_target(el)}#{escape(el.value)}}"
  end
end

```

    
  

    
      
  
### 
  
    #**convert_comment**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

206
207
208
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 206

def convert_comment(el, _opts)
  el.value.split("\n").map {|l| "% #{l}" }.join("\n") << "\n"
end

```

    
  

    
      
  
### 
  
    #**convert_dd**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

151
152
153
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 151

def convert_dd(el, opts)
  "#{latex_link_target(el)}#{inner(el, opts)}\n\n"
end

```

    
  

    
      
  
### 
  
    #**convert_dl**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

139
140
141
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 139

def convert_dl(el, opts)
  latex_environment('description', el, inner(el, opts))
end

```

    
  

    
      
  
### 
  
    #**convert_dt**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

147
148
149
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 147

def convert_dt(el, opts)
  "\\item[#{inner(el, opts)}] "
end

```

    
  

    
      
  
### 
  
    #**convert_em**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

264
265
266
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 264

def convert_em(el, opts)
  "\\emph{#{latex_link_target(el)}#{inner(el, opts)}}"
end

```

    
  

    
      
  
### 
  
    #**convert_entity**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

534
535
536
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 534

def convert_entity(el, _opts)
  entity_to_latex(el.value)
end

```

    
  

    
      
  
### 
  
    #**convert_footnote**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

251
252
253
254
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 251

def convert_footnote(el, opts)
  @data[:packages] << 'fancyvrb'
  "\\footnote{#{inner(el.value, opts).rstrip}}"
end

```

    
  

    
      
  
### 
  
    #**convert_header**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

114
115
116
117
118
119
120
121
122
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 114

def convert_header(el, opts)
  type = @options[:latex_headers][output_header_level(el.options[:level]) - 1]
  if ((id = el.attr['id']) ||
      (@options[:auto_ids] && (id = generate_id(el.options[:raw_text])))) && in_toc?(el)
    "\\#{type}{#{inner(el, opts)}}\\hypertarget{#{id}}{}\\label{#{id}}\n\n"
  else
    "\\#{type}*{#{inner(el, opts)}}\n\n"
  end
end

```

    
  

    
      
  
### 
  
    #**convert_hr**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

124
125
126
127
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 124

def convert_hr(el, _opts)
  attrs = attribute_list(el)
  "#{latex_link_target(el)}\\begin{center}#{attrs}\n\\rule{3in}{0.4pt}\n\\end{center}#{attrs}\n"
end

```

    
  

    
      
  
### 
  
    #**convert_html_element**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 155

def convert_html_element(el, opts)
  case el.value
  when 'i', 'em'
    "\\emph{#{inner(el, opts)}}"
  when 'b', 'strong'
    "\\textbf{#{inner(el, opts)}}"
  else
    warning("Can't convert HTML element")
    ''
  end
end

```

    
  

    
      
  
### 
  
    #**convert_img**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 226

def convert_img(el, _opts)
  line = el.options[:location]
  if el.attr['src'].match?(/^(https?|ftps?):\/\//)
    warning("Cannot include non-local image#{line ? " (line #{line})" : ''}")
    ''
  elsif !el.attr['src'].empty?
    @data[:packages] << 'graphicx'
    "#{latex_link_target(el)}\\includegraphics{#{el.attr['src']}}"
  else
    warning("Cannot include image with empty path#{line ? " (line #{line})" : ''}")
    ''
  end
end

```

    
  

    
      
  
### 
  
    #**convert_li**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

143
144
145
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 143

def convert_li(el, opts)
  "\\item{} #{latex_link_target(el, true)}#{inner(el, opts).sub(/\n+\Z/, '')}\n"
end

```

    
  

    
      
  
### 
  
    #**convert_math**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

557
558
559
560
561
562
563
564
565
566
567
568
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 557

def convert_math(el, _opts)
  @data[:packages] += %w[amssymb amsmath amsthm amsfonts]
  if el.options[:category] == :block
    if el.value.match?(/\A\s*\\begin\{/)
      el.value
    else
      latex_environment('displaymath', el, el.value)
    end
  else
    "$#{el.value}$"
  end
end

```

    
  

    
      
  
### 
  
    #**convert_p**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/kramdown/converter/latex.rb', line 69

def convert_p(el, opts)
  if el.children.size == 1 && el.children.first.type == :img &&
      !(img = convert_img(el.children.first, opts)).empty?
    convert_standalone_image(el, opts, img)
  else
    "#{latex_link_target(el)}#{inner(el, opts)}\n\n"
  end
end

```

    
  

    
      
  
### 
  
    #**convert_raw**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

256
257
258
259
260
261
262
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 256

def convert_raw(el, _opts)
  if !el.options[:type] || el.options[:type].empty? || el.options[:type].include?('latex')
    el.value + (el.options[:category] == :block ? "\n" : '')
  else
    ''
  end
end

```

    
  

    
      
  
### 
  
    #**convert_root**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

57
58
59
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 57

def convert_root(el, opts)
  inner(el, opts)
end

```

    
  

    
      
  
### 
  
    #**convert_smart_quote**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

551
552
553
554
555
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 551

def convert_smart_quote(el, opts)
  res = entity_to_latex(smart_quote_entity(el)).chomp('{}')
  res << "{}" if ((nel = opts[:parent].children[opts[:index] + 1]) && nel.type == :smart_quote) || res =~ /\w$/
  res
end

```

    
  

    
      
  
### 
  
    #**convert_standalone_image**(el, _opts, img)  ⇒ Object 
  

  

  

  
    

Helper method used by `convert_p` to convert a paragraph that only contains a single :img element.

  

  

  
    
      

```

80
81
82
83
84
85
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 80

def convert_standalone_image(el, _opts, img)
  attrs = attribute_list(el)
  "\\begin{figure}#{attrs}\n\\begin{center}\n#{img}\n\\end{center}\n" \
    "\\caption{#{escape(el.children.first.attr['alt'])}}\n" \
    "#{latex_link_target(el, true)}\n\\end{figure}#{attrs}\n"
end

```

    
  

    
      
  
### 
  
    #**convert_strong**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

268
269
270
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 268

def convert_strong(el, opts)
  "\\textbf{#{latex_link_target(el)}#{inner(el, opts)}}"
end

```

    
  

    
      
  
### 
  
    #**convert_table**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

178
179
180
181
182
183
184
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 178

def convert_table(el, opts)
  @data[:packages] << 'longtable'
  align = el.options[:alignment].map {|a| TABLE_ALIGNMENT_CHAR[a] }.join('|')
  attrs = attribute_list(el)
  "#{latex_link_target(el)}\\begin{longtable}{|#{align}|}#{attrs}\n" \
    "\\hline\n#{inner(el, opts)}\\hline\n\\end{longtable}#{attrs}\n\n"
end

```

    
  

    
      
  
### 
  
    #**convert_tbody**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

190
191
192
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 190

def convert_tbody(el, opts)
  inner(el, opts)
end

```

    
  

    
      
  
### 
  
    #**convert_td**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

202
203
204
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 202

def convert_td(el, opts)
  inner(el, opts)
end

```

    
  

    
      
  
### 
  
    #**convert_text**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

65
66
67
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 65

def convert_text(el, _opts)
  escape(el.value)
end

```

    
  

    
      
  
### 
  
    #**convert_tfoot**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

194
195
196
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 194

def convert_tfoot(el, opts)
  "\\hline \\hline \n#{inner(el, opts)}"
end

```

    
  

    
      
  
### 
  
    #**convert_thead**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

186
187
188
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 186

def convert_thead(el, opts)
  "#{inner(el, opts)}\\hline\n"
end

```

    
  

    
      
  
### 
  
    #**convert_tr**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

198
199
200
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 198

def convert_tr(el, opts)
  el.children.map {|c| send("convert_#{c.type}", c, opts) }.join(' & ') << "\\\\\n"
end

```

    
  

    
      
  
### 
  
    #**convert_typographic_sym**(el, _opts)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

543
544
545
546
547
548
549
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 543

def convert_typographic_sym(el, _opts)
  if (result = @options[:typographic_symbols][el.value])
    escape(result)
  else
    TYPOGRAPHIC_SYMS[el.value]
  end
end

```

    
  

    
      
  
### 
  
    #**convert_ul**(el, opts)  ⇒ Object 
  

  
    Also known as:
    convert_ol
    
  

  

  
    
      

```

129
130
131
132
133
134
135
136
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 129

def convert_ul(el, opts)
  if !@data[:has_toc] && el.options.dig(:ial, :refs)&.include?('toc')
    @data[:has_toc] = true
    '\tableofcontents'
  else
    latex_environment(el.type == :ul ? 'itemize' : 'enumerate', el, inner(el, opts))
  end
end

```

    
  

    
      
  
### 
  
    #**convert_xml_comment**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

167
168
169
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 167

def convert_xml_comment(el, _opts)
  el.value.split("\n").map {|l| "% #{l}" }.join("\n") + "\n"
end

```

    
  

    
      
  
### 
  
    #**convert_xml_pi**(_el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

171
172
173
174
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 171

def convert_xml_pi(_el, _opts)
  warning("Can't convert XML PI")
  ''
end

```

    
  

    
      
  
### 
  
    #**entity_to_latex**(entity)  ⇒ Object 
  

  

  

  
    
      

```

523
524
525
526
527
528
529
530
531
532
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 523

def entity_to_latex(entity)
  text, package = ENTITY_CONV_TABLE[entity.code_point]
  if text
    @data[:packages] << package if package
    text
  else
    warning("Couldn't find entity with code #{entity.code_point} in substitution table!")
    ''
  end
end

```

    
  

    
      
  
### 
  
    #**escape**(str)  ⇒ Object 
  

  

  

  
    

Escape the special LaTeX characters in the string `str`.

  

  

  
    
      

```

619
620
621
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 619

def escape(str)
  str.gsub(ESCAPE_RE) {|m| ESCAPE_MAP[m] }
end

```

    
  

    
      
  
### 
  
    #**inner**(el, opts)  ⇒ Object 
  

  

  

  
    

Return the converted content of the children of `el` as a string.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 46

def inner(el, opts)
  result = +''
  options = opts.dup.merge(parent: el)
  el.children.each_with_index do |inner_el, index|
    options[:index] = index
    options[:result] = result
    result << send("convert_#{inner_el.type}", inner_el, options)
  end
  result
end

```

    
  

    
      
  
### 
  
    #**latex_environment**(type, el, text)  ⇒ Object 
  

  

  

  
    

Wrap the `text` inside a LaTeX environment of type `type`. The element `el` is passed on to the method #attribute_list – the resulting string is appended to both the \begin and the \end lines of the LaTeX environment for easier post-processing of LaTeX environments.

  

  

  
    
      

```

583
584
585
586
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 583

def latex_environment(type, el, text)
  attrs = attribute_list(el)
  "\\begin{#{type}}#{latex_link_target(el)}#{attrs}\n#{text.rstrip}\n\\end{#{type}}#{attrs}\n"
end

```

    
  

    
      
  
### 
  
    #**latex_link_target**(el, add_label = false)  ⇒ Object 
  

  

  

  
    

Return a string containing a valid hypertarget command if the element has an ID defined, or `nil` otherwise. If the parameter `add_label` is `true`, a label command will also be used additionally to the hypertarget command.

  

  

  
    
      

```

591
592
593
594
595
596
597
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 591

def latex_link_target(el, add_label = false)
  if (id = el.attr['id'])
    "\\hypertarget{#{id}}{}#{add_label ? "\\label{#{id}}" : ''}"
  else
    nil
  end
end

```

    
  

    
      
  
### 
  
    #**normalize_abbreviation_key**(key)  ⇒ Object 
  

  

  

  
    

Normalize the abbreviation key so that it only contains allowed ASCII character

  

  

  
    
      

```

576
577
578
```

    
    
      

```
# File 'lib/kramdown/converter/latex.rb', line 576

def normalize_abbreviation_key(key)
  key.gsub(/\W/) {|m| m.unpack1('H*') }
end

```