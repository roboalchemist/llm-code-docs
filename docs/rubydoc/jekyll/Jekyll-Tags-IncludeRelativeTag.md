# Class: Jekyll::Tags::IncludeRelativeTag
  
    Inherits:
    
      IncludeTag
      
        

          
- Object

- Liquid::Tag

- IncludeTag

- Jekyll::Tags::IncludeRelativeTag

        show all
      

    Defined in:
    lib/jekyll/tags/include.rb
  
## Constant Summary

### Constants inherited

     from IncludeTag

Jekyll::Tags::IncludeTag::FULL_VALID_SYNTAX, Jekyll::Tags::IncludeTag::INVALID_SEQUENCES, Jekyll::Tags::IncludeTag::VALID_FILENAME_CHARS, Jekyll::Tags::IncludeTag::VALID_SYNTAX, Jekyll::Tags::IncludeTag::VARIABLE_SYNTAX

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**page_path**(context)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**tag_includes_dirs**(context)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods inherited from IncludeTag

# add_include_to_dependency, #file_read_opts, #initialize, #load_cached_partial, #locate_include_file, #outside_site_source?, #parse_params, #read_file, #realpath_prefixed_with?, #render, #render_variable, #syntax_example, #valid_include_file?, #validate_file_name, #validate_params

## Constructor Details

This class inherits a constructor from Jekyll::Tags::IncludeTag
  
## Instance Method Details

###
  
    #**page_path**(context)  ⇒ Object 
  

  

  

  
    
      

```

256
257
258
259
260
261
```

```
# File 'lib/jekyll/tags/include.rb', line 256

def page_path(context)
  page, site = context.registers.values_at(:page, :site)
  return site.source unless page

  site.in_source_dir File.dirname(resource_path(page, site))
end

```

###
  
    #**tag_includes_dirs**(context)  ⇒ Object 
  

  

  

  
    
      

```

252
253
254
```

```
# File 'lib/jekyll/tags/include.rb', line 252

def tag_includes_dirs(context)
  Array(page_path(context)).freeze
end

```
