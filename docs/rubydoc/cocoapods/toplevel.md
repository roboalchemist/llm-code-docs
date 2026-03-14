# Top Level Namespace
  
  
  

  

  
  
  
  
  

  

  

## Defined Under Namespace

  
    
      **Modules:** Molinillo, OpenURI, Pod, Xcodeproj
    
  
    
  

  
    
## 
      Private Helpers
      collapse
    

    

      
        
- 
  
    
      #**merge_to_docc_folder**(paths)  ⇒ Array<Pathname> 
    

    
  
  
  
  
  
  
  
  

  
    

If we have an non-empty .docc folder, remove all paths under the folder but keep the folder itself.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**merge_to_docc_folder**(paths)  ⇒ Array<Pathname> 
  

  

  

  
    

If we have an non-empty .docc folder, remove all paths under the folder but keep the folder itself

  

  

Parameters:

  
    
- 
      
        paths
      
      
        (Array<Pathname>)
      
      
      
        —
        

the paths to inspect

      
    
  

Returns:

  
    
- 
      
      
        (Array<Pathname>)
      
      
      
        —
        

The resulted list of paths.

      
    
  

  
    
      

```

342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
```

    
    
      

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/file_references_installer.rb', line 342

def merge_to_docc_folder(paths)
  docc_paths_with_files = Set.new
  allowable_paths = paths.select do |path|
    path_str = path.to_s

    if path_str =~ /\.docc(\/|$)/i

      # we want folder with files
      next if path.directory?

      # remove everything after ".docc", but keep ".docc"
      folder_path = path_str.split("\.docc")[0] + "\.docc"

      docc_paths_with_files << Pathname(folder_path)
      next

    end
    true
  end

  allowable_paths + docc_paths_with_files.to_a
end
```