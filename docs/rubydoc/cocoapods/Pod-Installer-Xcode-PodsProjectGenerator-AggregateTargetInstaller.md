# Class: Pod::Installer::Xcode::PodsProjectGenerator::AggregateTargetInstaller
  
    Inherits:
    
      TargetInstaller
      
        

          
- Object

- TargetInstaller

- Pod::Installer::Xcode::PodsProjectGenerator::AggregateTargetInstaller

        show all
      

    Defined in:
    lib/cocoapods/installer/xcode/pods_project_generator/aggregate_target_installer.rb
  
## Overview

Creates the targets which aggregate the Pods libraries in the Pods project and the relative support files.

## Instance Attribute Summary collapse

-
  
      #**target**  ⇒ AggregateTarget 

      readonly
    
    
  
  
  
  
  

  
    
  

    
  
### Attributes inherited from TargetInstaller

# project, #sandbox

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**install!**  ⇒ TargetInstallationResult 
    

    
  
  
  
  
  
  
  
  

  
    

Creates the target in the Pods project and the relative support files.

### Methods inherited from TargetInstaller

# initialize

### Methods included from TargetInstallerHelper

create_info_plist_file_with_sandbox, create_prefix_header, update_changed_file

## Constructor Details

This class inherits a constructor from Pod::Installer::Xcode::PodsProjectGenerator::TargetInstaller
  
## Instance Attribute Details

###
  
    #**target**  ⇒ AggregateTarget  (readonly)
  

  

  

  
    
      

```

11
12
13
```

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/aggregate_target_installer.rb', line 11

def target
  @target
end

```

## Instance Method Details

###
  
    #**install!**  ⇒ TargetInstallationResult 
  

  

  

  
    

Creates the target in the Pods project and the relative support files.

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
```

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/aggregate_target_installer.rb', line 17

def install!
  UI.message "- Installing target `#{target.name}` #{target.platform}" do
    native_target = add_target
    create_support_files_dir
    create_support_files_group
    create_xcconfig_file(native_target)
    if target.build_as_framework?
      create_info_plist_file(target.info_plist_path, native_target, target.version, target.platform)
      create_module_map(native_target)
      create_umbrella_header(native_target)
    elsif target.uses_swift?
      create_module_map(native_target)
      create_umbrella_header(native_target)
    end
    # Because embedded targets live in their host target, CocoaPods
    # copies all of the embedded target's pod_targets to its host
    # targets. Having this script for the embedded target would
    # cause an App Store rejection because frameworks cannot be
    # embedded in embedded targets.
    #
    create_embed_frameworks_script if embed_frameworks_script_required?
    create_bridge_support_file(native_target)
    create_copy_resources_script if target.includes_resources?
    create_acknowledgements
    create_dummy_source(native_target)
    clean_support_files_temp_dir
    TargetInstallationResult.new(target, native_target)
  end
end

```
