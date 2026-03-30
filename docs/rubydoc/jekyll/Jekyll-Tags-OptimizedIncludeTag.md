# Class: Jekyll::Tags::OptimizedIncludeTag
  
    Inherits:
    
      IncludeTag
      
        

          
- Object

- Liquid::Tag

- IncludeTag

- Jekyll::Tags::OptimizedIncludeTag

        show all
      

    Defined in:
    lib/jekyll/tags/include.rb
  
## Overview

Do not inherit from this class. TODO: Merge into the `Jekyll::Tags::IncludeTag` in v5.0

## Constant Summary

### Constants inherited

     from IncludeTag

IncludeTag::FULL_VALID_SYNTAX, IncludeTag::INVALID_SEQUENCES, IncludeTag::VALID_FILENAME_CHARS, IncludeTag::VALID_SYNTAX, IncludeTag::VARIABLE_SYNTAX

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**render**(context)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods inherited from IncludeTag

# file_read_opts, #initialize, #load_cached_partial, #outside_site_source?, #parse_params, #read_file, #render_variable, #syntax_example, #tag_includes_dirs, #validate_file_name, #validate_params

## Constructor Details

This class inherits a constructor from Jekyll::Tags::IncludeTag
  
## Instance Method Details

###
  
    #**render**(context)  ⇒ Object 
  

  

  

  
    
      

```

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
```

```
# File 'lib/jekyll/tags/include.rb', line 195

def render(context)
  @site ||= context.registers[:site]

  file = render_variable(context) || @file
  validate_file_name(file)

  @site.inclusions[file] ||= locate_include_file(file)
  inclusion = @site.inclusions[file]

  add_include_to_dependency(inclusion, context) if @site.config["incremental"]

  context.stack do
    context["include"] = parse_params(context) if @params
    inclusion.render(context)
  end
end
```
