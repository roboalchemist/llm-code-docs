# Class: Jekyll::PageWithoutAFile
  
    Inherits:
    
      Page
      
        

          
- Object

- Page

- Jekyll::PageWithoutAFile

        show all
      

    Defined in:
    lib/jekyll/page_without_a_file.rb
  
## Overview

A Jekyll::Page subclass to handle processing files without reading it to determine the page-data and page-content based on Front Matter delimiters.

The class instance is basically just a bare-bones entity with just attributes “dir”, “name”, “path”, “url” defined on it.

## Constant Summary

### Constants inherited

     from Page

Jekyll::Page::ATTRIBUTES_FOR_LIQUID, Jekyll::Page::HTML_EXTENSIONS

## Instance Attribute Summary

### Attributes inherited from Page

# basename, #content, #data, #dir, #ext, #name, #output, #pager, #site

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**read_yaml**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods inherited from Page

# destination, #excerpt, #excerpt_separator, #generate_excerpt?, #html?, #index?, #initialize, #inspect, #path, #permalink, #process, #relative_path, #render, #template, #trigger_hooks, #url, #url_placeholders, #write?

### Methods included from Convertible

# [], #asset_file?, #coffeescript_file?, #converters, #do_layout, #hook_owner, #invalid_layout?, #output_ext, #place_in_layout?, #published?, #render_all_layouts, #render_liquid, #render_with_liquid?, #renderer, #sass_file?, #to_liquid, #to_s, #transform, #type, #validate_data!, #validate_permalink!, #write

## Constructor Details

This class inherits a constructor from Jekyll::Page
  
## Instance Method Details

###
  
    #**read_yaml**  ⇒ Object 
  

  

  

  
    
      

```

10
11
12
```

```
# File 'lib/jekyll/page_without_a_file.rb', line 10

def read_yaml(*)
  @data ||= {}
end
```
