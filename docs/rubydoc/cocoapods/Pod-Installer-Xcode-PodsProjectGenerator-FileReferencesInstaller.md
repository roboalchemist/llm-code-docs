# Class: Pod::Installer::Xcode::PodsProjectGenerator::FileReferencesInstaller
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Pod::Installer::Xcode::PodsProjectGenerator::FileReferencesInstaller
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/installer/xcode/pods_project_generator/file_references_installer.rb
  
  

## Overview

  
    

Controller class responsible of installing the file references of the specifications in the Pods project.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        LOCALIZATION_REGION_FILEPATTERN_REGEX =
          
  
    

Regex for extracting the region portion of a localized file path. Ex. `Resources/en.lproj` –> `en`

  

  

        
        

```
/(\/|^)(?<region>[^\/]*?)\.lproj(\/|$)/

```

      
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**pod_targets**  ⇒ Array<PodTarget> 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The pod targets of the installation.

  

    
      
- 
  
    
      #**pods_project**  ⇒ Project 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The project to install the file references into.

  

    
      
- 
  
    
      #**preserve_pod_file_structure**  ⇒ Boolean 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Add support for preserving the file structure of externally sourced pods, in addition to local pods.

  

    
      
- 
  
    
      #**sandbox**  ⇒ Sandbox 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The sandbox of the installation.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(sandbox, pod_targets, pods_project, preserve_pod_file_structure = false)  ⇒ FileReferencesInstaller 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize a new instance.

  

      
        
- 
  
    
      #**install!**  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Installs the file references.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(sandbox, pod_targets, pods_project, preserve_pod_file_structure = false)  ⇒ FileReferencesInstaller 
  

  

  

  
    

Initialize a new instance

  

  

Parameters:

  
    
- 
      
        sandbox
      
      
        (Sandbox)
      
      
      
        —
        

@see #sandbox

      
    
  
    
- 
      
        pod_targets
      
      
        (Array<PodTarget>)
      
      
      
        —
        

@see #pod_targets

      
    
  
    
- 
      
        pods_project
      
      
        (Project)
      
      
      
        —
        

@see #pods_project

      
    
  
    
- 
      
        preserve_pod_file_structure
      
      
        (Boolean)
      
      
        *(defaults to: false)*
      
      
        —
        

@see #preserve_pod_file_structure

      
    
  

  
    
      

```

35
36
37
38
39
40
```

    
    
      

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/file_references_installer.rb', line 35

def initialize(sandbox, pod_targets, pods_project, preserve_pod_file_structure = false)
  @sandbox = sandbox
  @pod_targets = pod_targets
  @pods_project = pods_project
  @preserve_pod_file_structure = preserve_pod_file_structure
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**pod_targets**  ⇒ Array<PodTarget>  (readonly)
  

  

  

  
    

Returns The pod targets of the installation.

  

  

Returns:

  
    
- 
      
      
        (Array<PodTarget>)
      
      
      
        —
        

The pod targets of the installation.

      
    
  

  
    
      

```

18
19
20
```

    
    
      

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/file_references_installer.rb', line 18

def pod_targets
  @pod_targets
end

```

    
  

    
      
      
      
  
### 
  
    #**pods_project**  ⇒ Project  (readonly)
  

  

  

  
    

Returns The project to install the file references into.

  

  

Returns:

  
    
- 
      
      
        (Project)
      
      
      
        —
        

The project to install the file references into.

      
    
  

  
    
      

```

22
23
24
```

    
    
      

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/file_references_installer.rb', line 22

def pods_project
  @pods_project
end

```

    
  

    
      
      
      
  
### 
  
    #**preserve_pod_file_structure**  ⇒ Boolean  (readonly)
  

  

  

  
    

Returns add support for preserving the file structure of externally sourced pods, in addition to local pods.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

add support for preserving the file structure of externally sourced pods, in addition to local pods.

      
    
  

  
    
      

```

26
27
28
```

    
    
      

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/file_references_installer.rb', line 26

def preserve_pod_file_structure
  @preserve_pod_file_structure
end

```

    
  

    
      
      
      
  
### 
  
    #**sandbox**  ⇒ Sandbox  (readonly)
  

  

  

  
    

Returns The sandbox of the installation.

  

  

Returns:

  
    
- 
      
      
        (Sandbox)
      
      
      
        —
        

The sandbox of the installation.

      
    
  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/file_references_installer.rb', line 14

def sandbox
  @sandbox
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**install!**  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Installs the file references.

  

  

  
    
      

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
# File 'lib/cocoapods/installer/xcode/pods_project_generator/file_references_installer.rb', line 46

def install!
  refresh_file_accessors
  prepare_pod_groups
  add_source_files_references
  add_frameworks_bundles
  add_vendored_libraries
  add_resources
  add_developer_files unless sandbox.development_pods.empty?
  link_headers
end

```