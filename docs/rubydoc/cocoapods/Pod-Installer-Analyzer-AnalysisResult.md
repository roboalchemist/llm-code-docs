# Class: Pod::Installer::Analyzer::AnalysisResult
  
    Inherits:
    
      Object
      
        

          
- Object

- Pod::Installer::Analyzer::AnalysisResult

        show all
      

    Defined in:
    lib/cocoapods/installer/analyzer/analysis_result.rb
  
## Overview

A simple container produced after a analysis is completed by the Pod::Installer::Analyzer.

## Instance Attribute Summary collapse

-
  
      #**pod_targets**  ⇒ Array<PodTarget> 

      readonly
    
    
  
  
  
  
  

  
    

The pod targets created for all the aggregate targets.

-
  
      #**podfile_dependency_cache**  ⇒ PodfileDependencyCache 

      readonly
    
    
  
  
  
  
  

  
    

The cache of all dependencies in the podfile.

-
  
      #**podfile_state**  ⇒ SpecsState 

      readonly
    
    
  
  
  
  
  

  
    

The states of the Podfile specs.

-
  
      #**sandbox_state**  ⇒ SpecsState 

      readonly
    
    
  
  
  
  
  

  
    

The states of the Sandbox respect the resolved specifications.

-
  
      #**specifications**  ⇒ Array<Specification> 

      readonly
    
    
  
  
  
  
  

  
    

The specifications of the resolved version of Pods that should be installed.

-
  
      #**specs_by_source**  ⇒ Hash{Source => Array<Specification>} 

      readonly
    
    
  
  
  
  
  

  
    

The specifications grouped by spec repo source.

-
  
      #**specs_by_target**  ⇒ Hash{TargetDefinition => Array<Specification>} 

      readonly
    
    
  
  
  
  
  

  
    

The specifications grouped by target.

-
  
      #**targets**  ⇒ Array<AggregateTarget> 

      readonly
    
    
  
  
  
  
  

  
    

The aggregate targets created for each TargetDefinition from the Podfile.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**all_user_build_configurations**  ⇒ Hash{String=>Symbol} 
    

    
  
  
  
  
  
  
  
  

  
    

A hash representing all the user build configurations across all integration targets.

-
  
      #**initialize**(podfile_state, specs_by_target, specs_by_source, specifications, sandbox_state, targets, pod_targets, podfile_dependency_cache)  ⇒ AnalysisResult 

    constructor
  
  
  
  
  
  

  
    

A new instance of AnalysisResult.

-
  
      #**needs_install?**  ⇒ Boolean 

Whether an installation should be performed or this CocoaPods project is already up to date.

-
  
      #**podfile_needs_install?**  ⇒ Boolean 

Whether the podfile has changes respect to the lockfile.

-
  
      #**sandbox_needs_install?**  ⇒ Boolean 

Whether the sandbox is in synch with the lockfile.

## Constructor Details

###
  
    #**initialize**(podfile_state, specs_by_target, specs_by_source, specifications, sandbox_state, targets, pod_targets, podfile_dependency_cache)  ⇒ AnalysisResult 
  

  

  

  
    

Returns a new instance of AnalysisResult.

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
```

```
# File 'lib/cocoapods/installer/analyzer/analysis_result.rb', line 39

def initialize(podfile_state, specs_by_target, specs_by_source, specifications, sandbox_state, targets, pod_targets,
               podfile_dependency_cache)
  @podfile_state = podfile_state
  @specs_by_target = specs_by_target
  @specs_by_source = specs_by_source
  @specifications = specifications
  @sandbox_state = sandbox_state
  @targets = targets
  @pod_targets = pod_targets
  @podfile_dependency_cache = podfile_dependency_cache
end
```

## Instance Attribute Details

###
  
    #**pod_targets**  ⇒ Array<PodTarget>  (readonly)
  

  

  

  
    

Returns The pod targets created for all the aggregate targets.

Returns:

-

        (Array<PodTarget>)

        —
        

The pod targets created for all the aggregate targets.

```

33
34
35
```

```
# File 'lib/cocoapods/installer/analyzer/analysis_result.rb', line 33

def pod_targets
  @pod_targets
end
```

###
  
    #**podfile_dependency_cache**  ⇒ PodfileDependencyCache  (readonly)
  

  

  

  
    

Returns the cache of all dependencies in the podfile.

Returns:

-

        (PodfileDependencyCache)

        —
        

the cache of all dependencies in the podfile.

```

37
38
39
```

```
# File 'lib/cocoapods/installer/analyzer/analysis_result.rb', line 37

def podfile_dependency_cache
  @podfile_dependency_cache
end
```

###
  
    #**podfile_state**  ⇒ SpecsState  (readonly)
  

  

  

  
    

Returns the states of the Podfile specs.

Returns:

-

        (SpecsState)

        —
        

the states of the Podfile specs.

```

9
10
11
```

```
# File 'lib/cocoapods/installer/analyzer/analysis_result.rb', line 9

def podfile_state
  @podfile_state
end
```

###
  
    #**sandbox_state**  ⇒ SpecsState  (readonly)
  

  

  

  
    

Returns the states of the Sandbox respect the resolved specifications.

Returns:

-

        (SpecsState)

        —
        

the states of the Sandbox respect the resolved specifications.

```

25
26
27
```

```
# File 'lib/cocoapods/installer/analyzer/analysis_result.rb', line 25

def sandbox_state
  @sandbox_state
end
```

###
  
    #**specifications**  ⇒ Array<Specification>  (readonly)
  

  

  

  
    

Returns the specifications of the resolved version of Pods that should be installed.

Returns:

-

        (Array<Specification>)

        —
        

the specifications of the resolved version of Pods that should be installed.

```

21
22
23
```

```
# File 'lib/cocoapods/installer/analyzer/analysis_result.rb', line 21

def specifications
  @specifications
end
```

###
  
    #**specs_by_source**  ⇒ Hash{Source => Array<Specification>}  (readonly)
  

  

  

  
    

Returns the specifications grouped by spec repo source.

Returns:

-

        (Hash{Source => Array<Specification>})

        —
        

the specifications grouped by spec repo source.

```

17
18
19
```

```
# File 'lib/cocoapods/installer/analyzer/analysis_result.rb', line 17

def specs_by_source
  @specs_by_source
end
```

###
  
    #**specs_by_target**  ⇒ Hash{TargetDefinition => Array<Specification>}  (readonly)
  

  

  

  
    

Returns the specifications grouped by target.

Returns:

-

        (Hash{TargetDefinition => Array<Specification>})

        —
        

the specifications grouped by target.

```

13
14
15
```

```
# File 'lib/cocoapods/installer/analyzer/analysis_result.rb', line 13

def specs_by_target
  @specs_by_target
end
```

###
  
    #**targets**  ⇒ Array<AggregateTarget>  (readonly)
  

  

  

  
    

Returns The aggregate targets created for each TargetDefinition from the Podfile.

Returns:

-

        (Array<AggregateTarget>)

        —
        

The aggregate targets created for each TargetDefinition from the Podfile.

```

29
30
31
```

```
# File 'lib/cocoapods/installer/analyzer/analysis_result.rb', line 29

def targets
  @targets
end
```

## Instance Method Details

###
  
    #**all_user_build_configurations**  ⇒ Hash{String=>Symbol} 
  

  

  

  
    

Returns A hash representing all the user build configurations across all integration targets. Each key corresponds to the name of a configuration and its value to its type (`:debug` or `:release`).

Returns:

-

        (Hash{String=>Symbol})

        —
        

A hash representing all the user build configurations across all integration targets. Each key corresponds to the name of a configuration and its value to its type (`:debug` or `:release`).

```

56
57
58
59
60
```

```
# File 'lib/cocoapods/installer/analyzer/analysis_result.rb', line 56

def all_user_build_configurations
  targets.reduce({}) do |result, target|
    result.merge(target.user_build_configurations)
  end
end
```

###
  
    #**needs_install?**  ⇒ Boolean 
  

  

  

  
    

Returns Whether an installation should be performed or this CocoaPods project is already up to date.

Returns:

-

        (Boolean)

        —
        

Whether an installation should be performed or this CocoaPods project is already up to date.

```

65
66
67
```

```
# File 'lib/cocoapods/installer/analyzer/analysis_result.rb', line 65

def needs_install?
  podfile_needs_install? || sandbox_needs_install?
end
```

###
  
    #**podfile_needs_install?**  ⇒ Boolean 
  

  

  

  
    

Returns Whether the podfile has changes respect to the lockfile.

Returns:

-

        (Boolean)

        —
        

Whether the podfile has changes respect to the lockfile.

```

71
72
73
74
75
```

```
# File 'lib/cocoapods/installer/analyzer/analysis_result.rb', line 71

def podfile_needs_install?
  state = podfile_state
  needing_install = state.added.length + state.changed.length + state.deleted.length
  needing_install > 0
end
```

###
  
    #**sandbox_needs_install?**  ⇒ Boolean 
  

  

  

  
    

Returns Whether the sandbox is in synch with the lockfile.

Returns:

-

        (Boolean)

        —
        

Whether the sandbox is in synch with the lockfile.

```

79
80
81
82
83
```

```
# File 'lib/cocoapods/installer/analyzer/analysis_result.rb', line 79

def sandbox_needs_install?
  state = sandbox_state
  needing_install = state.added.length + state.changed.length + state.deleted.length
  needing_install > 0
end
```
