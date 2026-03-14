# Class: Pod::Installer::Xcode::AggregateTargetDependencyInstaller
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Pod::Installer::Xcode::AggregateTargetDependencyInstaller
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/installer/xcode/pods_project_generator/aggregate_target_dependency_installer.rb
  
  

## Overview

  
    

Wires up the dependencies for aggregate targets from the target installation results

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**aggregate_target_installation_results**  ⇒ Hash{String => TargetInstallationResult} 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The target installation results for aggregate targets.

  

    
      
- 
  
    
      #**metadata_cache**  ⇒ ProjectMetadataCache 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The project metadata cache.

  

    
      
- 
  
    
      #**pod_target_installation_results**  ⇒ Hash{String => TargetInstallationResult} 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The target installation results for pod targets.

  

    
      
- 
  
    
      #**sandbox**  ⇒ Sandbox 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The sandbox used for this installation.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(sandbox, aggregate_target_installation_results, pod_target_installation_results, metadata_cache)  ⇒ AggregateTargetDependencyInstaller 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize a new instance.

  

      
        
- 
  
    
      #**install!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(sandbox, aggregate_target_installation_results, pod_target_installation_results, metadata_cache)  ⇒ AggregateTargetDependencyInstaller 
  

  

  

  
    

Initialize a new instance.

  

  

Parameters:

  
    
- 
      
        sandbox
      
      
        (Sandbox)
      
      
      
        —
        

@see #sandbox

      
    
  
    
- 
      
        aggregate_target_installation_results
      
      
        (Hash{String => TargetInstallationResult})
      
      
      
        —
        

@see #aggregate_target_installation_results

      
    
  
    
- 
      
        pod_target_installation_results
      
      
        (Hash{String => TargetInstallationResult})
      
      
      
        —
        

@see #pod_target_installation_results

      
    
  
    
- 
      
        metadata_cache
      
      
        (ProjectMetadataCache)
      
      
      
        —
        

@see #metadata_cache

      
    
  

  
    
      

```

32
33
34
35
36
37
```

    
    
      

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/aggregate_target_dependency_installer.rb', line 32

def initialize(sandbox, aggregate_target_installation_results, pod_target_installation_results, metadata_cache)
  @sandbox = sandbox
  @aggregate_target_installation_results = aggregate_target_installation_results
  @pod_target_installation_results = pod_target_installation_results
  @metadata_cache = metadata_cache
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**aggregate_target_installation_results**  ⇒ Hash{String => TargetInstallationResult}  (readonly)
  

  

  

  
    

Returns The target installation results for aggregate targets.

  

  

Returns:

  
    
- 
      
      
        (Hash{String => TargetInstallationResult})
      
      
      
        —
        

The target installation results for aggregate targets.

      
    
  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/aggregate_target_dependency_installer.rb', line 15

def aggregate_target_installation_results
  @aggregate_target_installation_results
end
```

    
  

    
      
      
      
  
### 
  
    #**metadata_cache**  ⇒ ProjectMetadataCache  (readonly)
  

  

  

  
    

Returns The project metadata cache.

  

  

Returns:

  
    
- 
      
      
        (ProjectMetadataCache)
      
      
      
        —
        

The project metadata cache.

      
    
  

  
    
      

```

19
20
21
```

    
    
      

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/aggregate_target_dependency_installer.rb', line 19

def metadata_cache
  @metadata_cache
end
```

    
  

    
      
      
      
  
### 
  
    #**pod_target_installation_results**  ⇒ Hash{String => TargetInstallationResult}  (readonly)
  

  

  

  
    

Returns The target installation results for pod targets.

  

  

Returns:

  
    
- 
      
      
        (Hash{String => TargetInstallationResult})
      
      
      
        —
        

The target installation results for pod targets.

      
    
  

  
    
      

```

11
12
13
```

    
    
      

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/aggregate_target_dependency_installer.rb', line 11

def pod_target_installation_results
  @pod_target_installation_results
end
```

    
  

    
      
      
      
  
### 
  
    #**sandbox**  ⇒ Sandbox  (readonly)
  

  

  

  
    

Returns The sandbox used for this installation.

  

  

Returns:

  
    
- 
      
      
        (Sandbox)
      
      
      
        —
        

The sandbox used for this installation.

      
    
  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/aggregate_target_dependency_installer.rb', line 23

def sandbox
  @sandbox
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**install!**  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/aggregate_target_dependency_installer.rb', line 39

def install!
  aggregate_target_installation_results.values.each do |aggregate_target_installation_result|
    aggregate_target = aggregate_target_installation_result.target
    aggregate_native_target = aggregate_target_installation_result.native_target
    project = aggregate_native_target.project
    # Wire up dependencies that are part of inherit search paths for this aggregate target.
    aggregate_target.search_paths_aggregate_targets.each do |search_paths_target|
      aggregate_native_target.add_dependency(aggregate_target_installation_results[search_paths_target.name].native_target)
    end
    # Wire up all pod target dependencies to aggregate target.
    aggregate_target.pod_targets.each do |pod_target|
      if pod_target_installation_result = pod_target_installation_results[pod_target.name]
        pod_target_native_target = pod_target_installation_result.native_target
        aggregate_native_target.add_dependency(pod_target_native_target)
      else
        # Hit the cache
        is_local = sandbox.local?(pod_target.pod_name)
        cached_dependency = metadata_cache.target_label_by_metadata[pod_target.label]
        project.add_cached_pod_subproject(sandbox, cached_dependency, is_local)
        Project.add_cached_dependency(sandbox, aggregate_native_target, cached_dependency)
      end
    end
  end
end
```