# Class: Pod::AggregateTarget
  
    Inherits:
    
      Target
      
        

          
- Object

- Target

- Pod::AggregateTarget

        show all
      

    Defined in:
    lib/cocoapods/target/aggregate_target.rb
  
## Overview

Stores the information relative to the target used to cluster the targets of the single Pods. The client targets will then depend on this one.

##

      Constant Summary
      collapse
    

    
      
        EMBED_FRAMEWORKS_IN_HOST_TARGET_TYPES =
          
  
    

Product types where the product’s frameworks must be embedded in a host target

```
[:app_extension, :framework, :static_library, :messages_extension,
:watch_extension, :xpc_service].freeze

```

### Constants inherited

     from Target

Target::DEFAULT_BUILD_CONFIGURATIONS, Target::DEFAULT_NAME, Target::DEFAULT_VERSION

## Instance Attribute Summary collapse

-
  
      #**client_root**  ⇒ Pathname 

      readonly
    
    
  
  
  
  
  

  
    

The folder where the client is stored used for computing the relative paths.

-
  
      #**pod_targets**  ⇒ Array<PodTarget> 

      readonly
    
    
  
  
  
  
  

  
    

The dependencies for this target.

-
  
      #**search_paths_aggregate_targets**  ⇒ Array<AggregateTarget> 

      readonly
    
    
  
  
  
  
  

  
    

The aggregate targets whose pods this target must be able to import, but will not directly link against.

-
  
      #**target_definition**  ⇒ TargetDefinition 

      readonly
    
    
  
  
  
  
  

  
    

The target definition of the Podfile that generated this target.

-
  
      #**user_project**  ⇒ Xcodeproj::Project 

      readonly
    
    
  
  
  
  
  

  
    

The user project that this target will integrate as identified by the analyzer.

-
  
      #**user_target_uuids**  ⇒ Array<String> 

      readonly
    
    
  
  
  
  
  

  
    

The list of the UUIDs of the user targets that will be integrated by this target as identified by the analyzer.

-
  
      #**xcconfigs**  ⇒ Hash<String, Xcodeproj::Config> 

      readonly
    
    
  
  
  
  
  

  
    

Map from configuration name to configuration file for the target.

### Attributes inherited from Target

# application_extension_api_only, #archs, #build_library_for_distribution, #platform, #sandbox, #user_build_configurations

##

      Support files
      collapse
    

    

      
        
-
  
      #**acknowledgements_basepath**  ⇒ Pathname 
    

    
  
  
  
  
  
  
  
  

  
    

The absolute path of acknowledgements file.

-
  
      #**check_manifest_lock_script_output_file_path**  ⇒ String 

The output file path fo the check manifest lock script.

-
  
      #**copy_resources_script_input_files_path**(configuration)  ⇒ Pathname 

The absolute path of the copy resources script input file list.

-
  
      #**copy_resources_script_input_files_relative_path**  ⇒ String 

The path of the copy resources script input file list relative to the root of the Pods project.

-
  
      #**copy_resources_script_output_files_path**(configuration)  ⇒ Pathname 

The absolute path of the copy resources script output file list.

-
  
      #**copy_resources_script_output_files_relative_path**  ⇒ String 

The path of the copy resources script output file list relative to the root of the Pods project.

-
  
      #**copy_resources_script_path**  ⇒ Pathname 

The absolute path of the copy resources script.

-
  
      #**copy_resources_script_relative_path**  ⇒ String 

The path of the copy resources script relative to the root of the Pods project.

-
  
      #**embed_frameworks_script_input_files_path**(configuration)  ⇒ Pathname 

The absolute path of the embed frameworks script input file list.

-
  
      #**embed_frameworks_script_input_files_relative_path**  ⇒ String 

The path of the embed frameworks script input file list relative to the root of the Pods project.

-
  
      #**embed_frameworks_script_output_files_path**(configuration)  ⇒ Pathname 

The absolute path of the embed frameworks script output file list.

-
  
      #**embed_frameworks_script_output_files_relative_path**  ⇒ String 

The path of the embed frameworks script output file list relative to the root of the Pods project.

-
  
      #**embed_frameworks_script_path**  ⇒ Pathname 

The absolute path of the embed frameworks script.

-
  
      #**embed_frameworks_script_relative_path**  ⇒ String 

The path of the embed frameworks relative to the root of the Pods project.

-
  
      #**podfile_dir_relative_path**  ⇒ String 

The path of the Podfile directory relative to the root of the user project.

-
  
      #**prepare_artifacts_script_input_files_path**(configuration)  ⇒ Pathname 

  deprecated
  
    **Deprecated.** 
  

      
        
-
  
      #**prepare_artifacts_script_input_files_relative_path**  ⇒ String 
    

    
  
  deprecated
  
    **Deprecated.** 
  

      
        
-
  
      #**prepare_artifacts_script_output_files_path**(configuration)  ⇒ Pathname 
    

    
  
  deprecated
  
    **Deprecated.** 
  

      
        
-
  
      #**prepare_artifacts_script_output_files_relative_path**  ⇒ String 
    

    
  
  deprecated
  
    **Deprecated.** 
  

      
        
-
  
      #**prepare_artifacts_script_relative_path**  ⇒ String 
    

    
  
  deprecated
  
    **Deprecated.** 
  

      
        
-
  
      #**relative_pods_root**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

The xcconfig path of the root from the ‘$(SRCROOT)` variable of the user’s project.

-
  
      #**relative_pods_root_path**  ⇒ Pathname 

The relative path of the Pods directory from user project’s directory.

-
  
      #**xcconfig_relative_path**(config_name)  ⇒ String 

The path of the xcconfig file relative to the root of the user project.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**bridge_support_file**  ⇒ Pathname 
    

    
  
  
  
  
  
  
  
  

  
    

The path of the bridge support file relative to the sandbox or `nil` if bridge support is disabled.

-
  
      #**build_settings**(configuration_name = nil)  ⇒ Object 

-
  
      #**framework_paths_by_config**  ⇒ Hash{String => Array<FrameworkPaths>} 

The vendored dynamic artifacts and framework target input and output paths grouped by config.

-
  
      #**includes_frameworks?**  ⇒ Boolean 

Whether the target contains frameworks to be embedded into the user target.

-
  
      #**includes_on_demand_resources?**  ⇒ Boolean 

Whether the target contains any on demand resources.

-
  
      #**includes_resources?**  ⇒ Boolean 

Whether the target contains any resources.

-
  
      #**includes_xcframeworks?**  ⇒ Boolean 

Whether the target contains xcframeworks to be embedded into the user target.

-
  
      #**initialize**(sandbox, build_type, user_build_configurations, archs, platform, target_definition, client_root, user_project, user_target_uuids, pod_targets_for_build_configuration)  ⇒ AggregateTarget 

    constructor
  
  
  
  
  
  

  
    

Initialize a new instance.

-
  
      #**label**  ⇒ String 

The label for the target.

-
  
      #**library?**  ⇒ Boolean 

True if the user_target refers to a library (framework, static or dynamic lib).

-
  
      #**merge_embedded_pod_targets**(embedded_pod_targets_for_build_configuration)  ⇒ AggregateTarget 

Merges this aggregate target with additional pod targets that are part of embedded aggregate targets.

-
  
      #**on_demand_resources**  ⇒ Array<Pathname> 

the resources build phase.

-
  
      #**pod_targets_for_build_configuration**(build_configuration)  ⇒ Array<PodTarget> 

The pod targets for the given build configuration.

-
  
      #**podfile**  ⇒ Podfile 

The podfile which declares the dependency.

-
  
      #**requires_host_target?**  ⇒ Boolean 

True if the user_target’s pods are for an extension and must be embedded in a host, target, otherwise false.

-
  
      #**resource_paths_by_config**  ⇒ Hash{String => Array<String>} 

Uniqued Resources grouped by config.

-
  
      #**spec_consumers**  ⇒ Array<Specification::Consumer> 

The consumers of the Pod.

-
  
      #**specs**  ⇒ Array<Specification> 

The specifications used by this aggregate target.

-
  
      #**specs_by_build_configuration**  ⇒ Hash{Symbol => Array<Specification>} 

The pod targets for each build configuration.

-
  
      #**user_project_path**  ⇒ Pathname 

The path of the user project that this target will integrate as identified by the analyzer.

-
  
      #**user_targets**  ⇒ Array<PBXNativeTarget> 

List all user targets that will be integrated by this #target.

-
  
      #**uses_swift?**  ⇒ Boolean 

Whether the target uses Swift code.

-
  
      #**xcframeworks_by_config**  ⇒ Hash{String => Array<Xcode::XCFramework>} 

The vendored dynamic artifacts and framework target input and output paths grouped by config.

### Methods inherited from Target

# bridge_support_path, #build_as_dynamic?, #build_as_dynamic_framework?, #build_as_dynamic_library?, #build_as_framework?, #build_as_library?, #build_as_static?, #build_as_static_framework?, #build_as_static_library?, #dummy_source_path, #framework_name, #info_plist_entries, #info_plist_path, #inspect, #mark_application_extension_api_only, #mark_build_library_for_distribution, #module_map_path, #module_map_path_to_write, #name, output_extension_for_resource, #prepare_artifacts_script_path, #product_basename, #product_module_name, #product_name, #product_type, #requires_frameworks?, resource_extension_compilable?, #static_framework?, #static_library_name, #support_files_dir, #umbrella_header_path, #umbrella_header_path_to_write, #version, #xcconfig_path

## Constructor Details

###
  
    #**initialize**(sandbox, build_type, user_build_configurations, archs, platform, target_definition, client_root, user_project, user_target_uuids, pod_targets_for_build_configuration)  ⇒ AggregateTarget 
  

  

  

  
    

Initialize a new instance

Parameters:

-

        sandbox

        (Sandbox)
      
      
      
        —
        

@see Target#sandbox

-

        build_type

        (BuildType)
      
      
      
        —
        

@see Target#build_type

-

        user_build_configurations

        (Hash{String=>Symbol})
      
      
      
        —
        

@see Target#user_build_configurations

-

        archs

        (Array<String>)
      
      
      
        —
        

@see Target#archs

-

        platform

        (Platform)
      
      
      
        —
        

@see #Target#platform

-

        target_definition

        (TargetDefinition)
      
      
      
        —
        

@see #target_definition

-

        client_root

        (Pathname)
      
      
      
        —
        

@see #client_root

-

        user_project

        (Xcodeproj::Project)
      
      
      
        —
        

@see #user_project

-

        user_target_uuids

        (Array<String>)
      
      
      
        —
        

@see #user_target_uuids

-

        pod_targets_for_build_configuration

        (Hash{String=>Array<PodTarget>})
      
      
      
        —
        

@see #pod_targets_for_build_configuration

```

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
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 70

def initialize(sandbox, build_type, user_build_configurations, archs, platform, target_definition, client_root,
               user_project, user_target_uuids, pod_targets_for_build_configuration)
  super(sandbox, build_type, user_build_configurations, archs, platform)
  raise "Can't initialize an AggregateTarget without a TargetDefinition!" if target_definition.nil?
  raise "Can't initialize an AggregateTarget with an abstract TargetDefinition!" if target_definition.abstract?
  @target_definition = target_definition
  @client_root = client_root
  @user_project = user_project
  @user_target_uuids = user_target_uuids
  @pod_targets_for_build_configuration = pod_targets_for_build_configuration
  @pod_targets = pod_targets_for_build_configuration.values.flatten.uniq
  @search_paths_aggregate_targets = []
  @xcconfigs = {}
end

```

## Instance Attribute Details

###
  
    #**client_root**  ⇒ Pathname  (readonly)
  

  

  

  
    

Returns the folder where the client is stored used for computing the relative paths. If integrating it should be the folder where the user project is stored, otherwise it should be the installation root.

Returns:

-

        (Pathname)

        —
        

the folder where the client is stored used for computing the relative paths. If integrating it should be the folder where the user project is stored, otherwise it should be the installation root.

```

24
25
26
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 24

def client_root
  @client_root
end

```

###
  
    #**pod_targets**  ⇒ Array<PodTarget>  (readonly)
  

  

  

  
    

Returns The dependencies for this target.

Returns:

-

        (Array<PodTarget>)

        —
        

The dependencies for this target.

```

50
51
52
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 50

def pod_targets
  @pod_targets
end

```

###
  
    #**search_paths_aggregate_targets**  ⇒ Array<AggregateTarget>  (readonly)
  

  

  

  
    

Returns The aggregate targets whose pods this target must be able to import, but will not directly link against.

Returns:

-

        (Array<AggregateTarget>)

        —
        

The aggregate targets whose pods this target must be able to import, but will not directly link against.

```

55
56
57
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 55

def search_paths_aggregate_targets
  @search_paths_aggregate_targets
end

```

###
  
    #**target_definition**  ⇒ TargetDefinition  (readonly)
  

  

  

  
    

Returns the target definition of the Podfile that generated this target.

Returns:

-

        (TargetDefinition)

        —
        

the target definition of the Podfile that generated this target.

```

17
18
19
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 17

def target_definition
  @target_definition
end

```

###
  
    #**user_project**  ⇒ Xcodeproj::Project  (readonly)
  

  

  

  
    

Returns the user project that this target will integrate as identified by the analyzer.

Returns:

-

        (Xcodeproj::Project)

        —
        

the user project that this target will integrate as identified by the analyzer.

```

29
30
31
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 29

def user_project
  @user_project
end

```

###
  
    #**user_target_uuids**  ⇒ Array<String>  (readonly)
  

  

  

  
    
  
    **Note:**
    

The target instances are not stored to prevent editing different instances.

Returns the list of the UUIDs of the user targets that will be integrated by this target as identified by the analyzer.

Returns:

-

        (Array<String>)

        —
        

the list of the UUIDs of the user targets that will be integrated by this target as identified by the analyzer.

```

37
38
39
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 37

def user_target_uuids
  @user_target_uuids
end

```

###
  
    #**xcconfigs**  ⇒ Hash<String, Xcodeproj::Config>  (readonly)
  

  

  

  
    
  
    **Note:**
    

The configurations are generated by the TargetInstaller and used by UserProjectIntegrator to check for any overridden values.

Returns Map from configuration name to configuration file for the target.

Returns:

-

        (Hash<String, Xcodeproj::Config>)

        —
        

Map from configuration name to configuration file for the target

```

46
47
48
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 46

def xcconfigs
  @xcconfigs
end

```

## Instance Method Details

###
  
    #**acknowledgements_basepath**  ⇒ Pathname 
  

  

  

  
    
  
    **Note:**
    

The acknowledgements generators add the extension according to the file type.

Returns The absolute path of acknowledgements file.

Returns:

-

        (Pathname)

        —
        

The absolute path of acknowledgements file.

```

347
348
349
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 347

def acknowledgements_basepath
  support_files_dir + "#{label}-acknowledgements"
end

```

###
  
    #**bridge_support_file**  ⇒ Pathname 
  

  

  

  
    

Returns the path of the bridge support file relative to the sandbox or `nil` if bridge support is disabled.

Returns:

-

        (Pathname)

        —
        

the path of the bridge support file relative to the sandbox or `nil` if bridge support is disabled.

```

334
335
336
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 334

def bridge_support_file
  bridge_support_path.relative_path_from(sandbox.root) if podfile.generate_bridge_support?
end

```

###
  
    #**build_settings**(configuration_name = nil)  ⇒ Object 
  

  

  

  
    
      

```

105
106
107
108
109
110
111
112
113
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 105

def build_settings(configuration_name = nil)
  if configuration_name
    @build_settings[configuration_name] ||
      raise(ArgumentError, "#{self} does not contain a build setting for the #{configuration_name.inspect} configuration, only #{@build_settings.keys.inspect}")
  else
    @build_settings.each_value.first ||
      raise(ArgumentError, "#{self} does not contain any build settings")
  end
end

```

###
  
    #**check_manifest_lock_script_output_file_path**  ⇒ String 
  

  

  

  
    

Returns The output file path fo the check manifest lock script.

Returns:

-

        (String)

        —
        

The output file path fo the check manifest lock script.

```

421
422
423
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 421

def check_manifest_lock_script_output_file_path
  "$(DERIVED_FILE_DIR)/#{label}-checkManifestLockResult.txt"
end

```

###
  
    #**copy_resources_script_input_files_path**(configuration)  ⇒ Pathname 
  

  

  

  
    

Returns The absolute path of the copy resources script input file list.

Parameters:

-

        configuration

        (String)
      
      
      
        —
        

the configuration this path is for.

Returns:

-

        (Pathname)

        —
        

The absolute path of the copy resources script input file list.

```

367
368
369
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 367

def copy_resources_script_input_files_path(configuration)
  support_files_dir + "#{label}-resources-#{configuration}-input-files.xcfilelist"
end

```

###
  
    #**copy_resources_script_input_files_relative_path**  ⇒ String 
  

  

  

  
    

Returns The path of the copy resources script input file list relative to the root of the Pods project.

Returns:

-

        (String)

        —
        

The path of the copy resources script input file list relative to the root of the Pods project.

```

466
467
468
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 466

def copy_resources_script_input_files_relative_path
  "${PODS_ROOT}/#{relative_to_pods_root(copy_resources_script_input_files_path('${CONFIGURATION}'))}"
end

```

###
  
    #**copy_resources_script_output_files_path**(configuration)  ⇒ Pathname 
  

  

  

  
    

Returns The absolute path of the copy resources script output file list.

Parameters:

-

        configuration

        (String)
      
      
      
        —
        

the configuration this path is for.

Returns:

-

        (Pathname)

        —
        

The absolute path of the copy resources script output file list.

```

375
376
377
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 375

def copy_resources_script_output_files_path(configuration)
  support_files_dir + "#{label}-resources-#{configuration}-output-files.xcfilelist"
end

```

###
  
    #**copy_resources_script_output_files_relative_path**  ⇒ String 
  

  

  

  
    

Returns The path of the copy resources script output file list relative to the root of the Pods project.

Returns:

-

        (String)

        —
        

The path of the copy resources script output file list relative to the root of the Pods project.

```

473
474
475
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 473

def copy_resources_script_output_files_relative_path
  "${PODS_ROOT}/#{relative_to_pods_root(copy_resources_script_output_files_path('${CONFIGURATION}'))}"
end

```

###
  
    #**copy_resources_script_path**  ⇒ Pathname 
  

  

  

  
    

Returns The absolute path of the copy resources script.

Returns:

-

        (Pathname)

        —
        

The absolute path of the copy resources script.

```

353
354
355
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 353

def copy_resources_script_path
  support_files_dir + "#{label}-resources.sh"
end

```

###
  
    #**copy_resources_script_relative_path**  ⇒ String 
  

  

  

  
    

Returns The path of the copy resources script relative to the root of the Pods project.

Returns:

-

        (String)

        —
        

The path of the copy resources script relative to the root of the Pods project.

```

459
460
461
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 459

def copy_resources_script_relative_path
  "${PODS_ROOT}/#{relative_to_pods_root(copy_resources_script_path)}"
end

```

###
  
    #**embed_frameworks_script_input_files_path**(configuration)  ⇒ Pathname 
  

  

  

  
    

Returns The absolute path of the embed frameworks script input file list.

Parameters:

-

        configuration

        (String)
      
      
      
        —
        

the configuration this path is for.

Returns:

-

        (Pathname)

        —
        

The absolute path of the embed frameworks script input file list.

```

383
384
385
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 383

def embed_frameworks_script_input_files_path(configuration)
  support_files_dir + "#{label}-frameworks-#{configuration}-input-files.xcfilelist"
end

```

###
  
    #**embed_frameworks_script_input_files_relative_path**  ⇒ String 
  

  

  

  
    

Returns The path of the embed frameworks script input file list relative to the root of the Pods project.

Returns:

-

        (String)

        —
        

The path of the embed frameworks script input file list relative to the root of the Pods project.

```

487
488
489
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 487

def embed_frameworks_script_input_files_relative_path
  "${PODS_ROOT}/#{relative_to_pods_root(embed_frameworks_script_input_files_path('${CONFIGURATION}'))}"
end

```

###
  
    #**embed_frameworks_script_output_files_path**(configuration)  ⇒ Pathname 
  

  

  

  
    

Returns The absolute path of the embed frameworks script output file list.

Parameters:

-

        configuration

        (String)
      
      
      
        —
        

the configuration this path is for.

Returns:

-

        (Pathname)

        —
        

The absolute path of the embed frameworks script output file list.

```

391
392
393
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 391

def embed_frameworks_script_output_files_path(configuration)
  support_files_dir + "#{label}-frameworks-#{configuration}-output-files.xcfilelist"
end

```

###
  
    #**embed_frameworks_script_output_files_relative_path**  ⇒ String 
  

  

  

  
    

Returns The path of the embed frameworks script output file list relative to the root of the Pods project.

Returns:

-

        (String)

        —
        

The path of the embed frameworks script output file list relative to the root of the Pods project.

```

494
495
496
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 494

def embed_frameworks_script_output_files_relative_path
  "${PODS_ROOT}/#{relative_to_pods_root(embed_frameworks_script_output_files_path('${CONFIGURATION}'))}"
end

```

###
  
    #**embed_frameworks_script_path**  ⇒ Pathname 
  

  

  

  
    

Returns The absolute path of the embed frameworks script.

Returns:

-

        (Pathname)

        —
        

The absolute path of the embed frameworks script.

```

359
360
361
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 359

def embed_frameworks_script_path
  support_files_dir + "#{label}-frameworks.sh"
end

```

###
  
    #**embed_frameworks_script_relative_path**  ⇒ String 
  

  

  

  
    

Returns The path of the embed frameworks relative to the root of the Pods project.

Returns:

-

        (String)

        —
        

The path of the embed frameworks relative to the root of the Pods project.

```

480
481
482
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 480

def embed_frameworks_script_relative_path
  "${PODS_ROOT}/#{relative_to_pods_root(embed_frameworks_script_path)}"
end

```

###
  
    #**framework_paths_by_config**  ⇒ Hash{String => Array<FrameworkPaths>} 
  

  

  

  
    

Returns The vendored dynamic artifacts and framework target input and output paths grouped by config.

Returns:

-

        (Hash{String => Array<FrameworkPaths>})

        —
        

The vendored dynamic artifacts and framework target input and output paths grouped by config

```

251
252
253
254
255
256
257
258
259
260
261
262
263
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 251

def framework_paths_by_config
  @framework_paths_by_config ||= begin
    framework_paths_by_config = {}
    user_build_configurations.each_key do |config|
      relevant_pod_targets = pod_targets_for_build_configuration(config)
      framework_paths_by_config[config] = relevant_pod_targets.flat_map do |pod_target|
        library_specs = pod_target.library_specs.map(&:name)
        pod_target.framework_paths.values_at(*library_specs).flatten.compact.uniq
      end
    end
    framework_paths_by_config
  end
end

```

###
  
    #**includes_frameworks?**  ⇒ Boolean 
  

  

  

  
    

Returns Whether the target contains frameworks to be embedded into the user target.

Returns:

-

        (Boolean)

        —
        

Whether the target contains frameworks to be embedded into the user target

```

237
238
239
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 237

def includes_frameworks?
  !framework_paths_by_config.each_value.all?(&:empty?)
end

```

###
  
    #**includes_on_demand_resources?**  ⇒ Boolean 
  

  

  

  
    

Returns Whether the target contains any on demand resources.

Returns:

-

        (Boolean)

        —
        

Whether the target contains any on demand resources

```

230
231
232
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 230

def includes_on_demand_resources?
  !on_demand_resources.empty?
end

```

###
  
    #**includes_resources?**  ⇒ Boolean 
  

  

  

  
    

Returns Whether the target contains any resources.

Returns:

-

        (Boolean)

        —
        

Whether the target contains any resources

```

224
225
226
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 224

def includes_resources?
  !resource_paths_by_config.each_value.all?(&:empty?)
end

```

###
  
    #**includes_xcframeworks?**  ⇒ Boolean 
  

  

  

  
    

Returns Whether the target contains xcframeworks to be embedded into the user target.

Returns:

-

        (Boolean)

        —
        

Whether the target contains xcframeworks to be embedded into the user target

```

244
245
246
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 244

def includes_xcframeworks?
  !xcframeworks_by_config.each_value.all?(&:empty?)
end

```

###
  
    #**label**  ⇒ String 
  

  

  

  
    

Returns the label for the target.

Returns:

-

        (String)

        —
        

the label for the target.

```

149
150
151
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 149

def label
  target_definition.label.to_s
end

```

###
  
    #**library?**  ⇒ Boolean 
  

  

  

  
    

Returns True if the user_target refers to a library (framework, static or dynamic lib).

Returns:

-

        (Boolean)

        —
        

True if the user_target refers to a library (framework, static or dynamic lib).

```

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
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 118

def library?
  # Without a user_project, we can't say for sure
  # that this is a library
  return false if user_project.nil?
  symbol_types = user_targets.map(&:symbol_type).uniq
  unless symbol_types.count == 1
    raise ArgumentError, "Expected single kind of user_target for #{name}. Found #{symbol_types.join(', ')}."
  end
  [:framework, :dynamic_library, :static_library].include? symbol_types.first
end

```

###
  
    #**merge_embedded_pod_targets**(embedded_pod_targets_for_build_configuration)  ⇒ AggregateTarget 
  

  

  

  
    

Merges this aggregate target with additional pod targets that are part of embedded aggregate targets.

Parameters:

-

        embedded_pod_targets_for_build_configuration

        (Hash{String=>Array<PodTarget>})
      
      
      
        —
        

The pod targets to merge with.

Returns:

-

        (AggregateTarget)

        —
        

a new instance of this aggregate target with additional pod targets to be used from pod targets of embedded aggregate targets.

```

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
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 93

def merge_embedded_pod_targets(embedded_pod_targets_for_build_configuration)
  merged = @pod_targets_for_build_configuration.merge(embedded_pod_targets_for_build_configuration) do |_, before, after|
    (before + after).uniq
  end
  AggregateTarget.new(sandbox, build_type, user_build_configurations, archs, platform,
                      target_definition, client_root, user_project, user_target_uuids, merged).tap do |aggregate_target|
    aggregate_target.search_paths_aggregate_targets.concat(search_paths_aggregate_targets).freeze
    aggregate_target.mark_application_extension_api_only if application_extension_api_only
    aggregate_target.mark_build_library_for_distribution if build_library_for_distribution
  end
end

```

###
  
    #**on_demand_resources**  ⇒ Array<Pathname> 
  

  

  

  
    
  
    **Note:**
    

On Demand Resources are not separated by config as they are integrated directly into the users target via

the resources build phase.

Returns:

-

        (Array<Pathname>)

        —
        

Uniqued On Demand Resources for this target.

```

287
288
289
290
291
292
293
294
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 287

def on_demand_resources
  @on_demand_resources ||= begin
    pod_targets.flat_map do |pod_target|
      library_file_accessors = pod_target.file_accessors.select { |fa| fa.spec.library_specification? }
      library_file_accessors.flat_map(&:on_demand_resources_files)
    end.uniq
  end
end

```

###
  
    #**pod_targets_for_build_configuration**(build_configuration)  ⇒ Array<PodTarget> 
  

  

  

  
    

Returns the pod targets for the given build configuration.

Parameters:

-

        build_configuration

        (String)
      
      
      
        —
        

The build configuration for which the the pod targets should be returned.

Returns:

-

        (Array<PodTarget>)

        —
        

the pod targets for the given build configuration.

```

188
189
190
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 188

def pod_targets_for_build_configuration(build_configuration)
  @pod_targets_for_build_configuration[build_configuration] || []
end

```

###
  
    #**podfile**  ⇒ Podfile 
  

  

  

  
    

Returns The podfile which declares the dependency.

Returns:

-

        (Podfile)

        —
        

The podfile which declares the dependency

```

155
156
157
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 155

def podfile
  target_definition.podfile
end

```

###
  
    #**podfile_dir_relative_path**  ⇒ String 
  

  

  

  
    

Returns The path of the Podfile directory relative to the root of the user project.

Returns:

-

        (String)

        —
        

The path of the Podfile directory relative to the root of the user project.

```

441
442
443
444
445
446
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 441

def podfile_dir_relative_path
  podfile_path = target_definition.podfile.defined_in_file
  return "${SRCROOT}/#{podfile_path.relative_path_from(client_root).dirname}" unless podfile_path.nil?
  # Fallback to the standard path if the Podfile is not represented by a file.
  '${PODS_ROOT}/..'
end

```

###
  
    #**prepare_artifacts_script_input_files_path**(configuration)  ⇒ Pathname 
  

  

  

  
    **Deprecated.** 

  
    **TODO:**
    

Remove in 2.0

Returns The absolute path of the prepare artifacts script input file list.

Parameters:

-

        configuration

        (String)
      
      
      
        —
        

the configuration this path is for.

Returns:

-

        (Pathname)

        —
        

The absolute path of the prepare artifacts script input file list.

```

403
404
405
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 403

def prepare_artifacts_script_input_files_path(configuration)
  support_files_dir + "#{label}-artifacts-#{configuration}-input-files.xcfilelist"
end

```

###
  
    #**prepare_artifacts_script_input_files_relative_path**  ⇒ String 
  

  

  

  
    **Deprecated.** 

  
    **TODO:**
    

Remove in 2.0

Returns The path of the prepare artifacts script input file list relative to the root of the Pods project.

Returns:

-

        (String)

        —
        

The path of the prepare artifacts script input file list relative to the root of the Pods project.

```

516
517
518
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 516

def prepare_artifacts_script_input_files_relative_path
  "${PODS_ROOT}/#{relative_to_pods_root(prepare_artifacts_script_input_files_path('${CONFIGURATION}'))}"
end

```

###
  
    #**prepare_artifacts_script_output_files_path**(configuration)  ⇒ Pathname 
  

  

  

  
    **Deprecated.** 

  
    **TODO:**
    

Remove in 2.0

Returns The absolute path of the prepare artifacts script output file list.

Parameters:

-

        configuration

        (String)
      
      
      
        —
        

the configuration this path is for.

Returns:

-

        (Pathname)

        —
        

The absolute path of the prepare artifacts script output file list.

```

415
416
417
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 415

def prepare_artifacts_script_output_files_path(configuration)
  support_files_dir + "#{label}-artifacts-#{configuration}-output-files.xcfilelist"
end

```

###
  
    #**prepare_artifacts_script_output_files_relative_path**  ⇒ String 
  

  

  

  
    **Deprecated.** 

  
    **TODO:**
    

Remove in 2.0

Returns The path of the prepare artifacts script output file list relative to the root of the Pods project.

Returns:

-

        (String)

        —
        

The path of the prepare artifacts script output file list relative to the root of the Pods project.

```

527
528
529
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 527

def prepare_artifacts_script_output_files_relative_path
  "${PODS_ROOT}/#{relative_to_pods_root(prepare_artifacts_script_output_files_path('${CONFIGURATION}'))}"
end

```

###
  
    #**prepare_artifacts_script_relative_path**  ⇒ String 
  

  

  

  
    **Deprecated.** 

  
    **TODO:**
    

Remove in 2.0

Returns The path of the prepare artifacts script relative to the root of the Pods project.

Returns:

-

        (String)

        —
        

The path of the prepare artifacts script relative to the root of the Pods project.

```

505
506
507
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 505

def prepare_artifacts_script_relative_path
  "${PODS_ROOT}/#{relative_to_pods_root(prepare_artifacts_script_path)}"
end

```

###
  
    #**relative_pods_root**  ⇒ String 
  

  

  

  
    

Returns The xcconfig path of the root from the ‘$(SRCROOT)` variable of the user’s project.

Returns:

-

        (String)

        —
        

The xcconfig path of the root from the ‘$(SRCROOT)` variable of the user’s project.

```

434
435
436
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 434

def relative_pods_root
  "${SRCROOT}/#{relative_pods_root_path}"
end

```

###
  
    #**relative_pods_root_path**  ⇒ Pathname 
  

  

  

  
    

Returns The relative path of the Pods directory from user project’s directory.

Returns:

-

        (Pathname)

        —
        

The relative path of the Pods directory from user project’s directory.

```

427
428
429
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 427

def relative_pods_root_path
  sandbox.root.relative_path_from(client_root)
end

```

###
  
    #**requires_host_target?**  ⇒ Boolean 
  

  

  

  
    

Returns True if the user_target’s pods are for an extension and must be embedded in a host, target, otherwise false.

Returns:

-

        (Boolean)

        —
        

True if the user_target’s pods are for an extension and must be embedded in a host, target, otherwise false.

```

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
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 133

def requires_host_target?
  # If we don't have a user_project, then we can't
  # glean any info about how this target is going to
  # be integrated, so return false since we can't know
  # for sure that this target refers to an extension
  # target that would require a host target
  return false if user_project.nil?
  symbol_types = user_targets.map(&:symbol_type).uniq
  unless symbol_types.count == 1
    raise ArgumentError, "Expected single kind of user_target for #{name}. Found #{symbol_types.join(', ')}."
  end
  EMBED_FRAMEWORKS_IN_HOST_TARGET_TYPES.include?(symbol_types[0])
end

```

###
  
    #**resource_paths_by_config**  ⇒ Hash{String => Array<String>} 
  

  

  

  
    

Returns Uniqued Resources grouped by config.

Returns:

-

        (Hash{String => Array<String>})

        —
        

Uniqued Resources grouped by config

```

298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 298

def resource_paths_by_config
  @resource_paths_by_config ||= begin
    relevant_pod_targets = pod_targets.reject do |pod_target|
      pod_target.should_build? && pod_target.build_as_dynamic_framework?
    end
    user_build_configurations.each_key.each_with_object({}) do |config, resources_by_config|
      targets = relevant_pod_targets & pod_targets_for_build_configuration(config)
      resources_by_config[config] = targets.flat_map do |pod_target|
        library_specs = pod_target.library_specs.map(&:name)
        resource_paths = pod_target.resource_paths.values_at(*library_specs).flatten

        if pod_target.build_as_static_framework?
          built_product_dir = Pathname.new(pod_target.build_product_path('${BUILT_PRODUCTS_DIR}'))
          resource_paths = resource_paths.map do |resource_path|
            extname = File.extname(resource_path)
            if self.class.resource_extension_compilable?(extname)
              output_extname = self.class.output_extension_for_resource(extname)
              output_path_components = Pathname(resource_path).each_filename.select { |component| File.extname(component) == '.lproj' }
              output_path_components << File.basename(resource_path)
              built_product_dir.join(*output_path_components).sub_ext(output_extname).to_s
            else
              resource_path
            end
          end
        end

        resource_paths << bridge_support_file
        resource_paths.compact.uniq
      end
    end
  end
end

```

###
  
    #**spec_consumers**  ⇒ Array<Specification::Consumer> 
  

  

  

  
    

Returns The consumers of the Pod.

Returns:

-

        (Array<Specification::Consumer>)

        —
        

The consumers of the Pod.

```

212
213
214
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 212

def spec_consumers
  specs.map { |spec| spec.consumer(platform) }
end

```

###
  
    #**specs**  ⇒ Array<Specification> 
  

  

  

  
    

Returns The specifications used by this aggregate target.

Returns:

-

        (Array<Specification>)

        —
        

The specifications used by this aggregate target.

```

194
195
196
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 194

def specs
  pod_targets.flat_map(&:specs)
end

```

###
  
    #**specs_by_build_configuration**  ⇒ Hash{Symbol => Array<Specification>} 
  

  

  

  
    

Returns The pod targets for each build configuration.

Returns:

-

        (Hash{Symbol => Array<Specification>})

        —
        

The pod targets for each build configuration.

```

201
202
203
204
205
206
207
208
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 201

def specs_by_build_configuration
  result = {}
  user_build_configurations.each_key do |build_configuration|
    result[build_configuration] = pod_targets_for_build_configuration(build_configuration).
      flat_map(&:specs)
  end
  result
end

```

###
  
    #**user_project_path**  ⇒ Pathname 
  

  

  

  
    

Returns the path of the user project that this target will integrate as identified by the analyzer.

Returns:

-

        (Pathname)

        —
        

the path of the user project that this target will integrate as identified by the analyzer.

```

162
163
164
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 162

def user_project_path
  user_project.path if user_project
end

```

###
  
    #**user_targets**  ⇒ Array<PBXNativeTarget> 
  

  

  

  
    

List all user targets that will be integrated by this #target.

Returns:

-

        (Array<PBXNativeTarget>)

```

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
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 170

def user_targets
  return [] unless user_project
  user_target_uuids.map do |uuid|
    native_target = user_project.objects_by_uuid[uuid]
    unless native_target
      raise Informative, '[Bug] Unable to find the target with ' \
        "the `#{uuid}` UUID for the `#{self}` integration library"
    end
    native_target
  end
end

```

###
  
    #**uses_swift?**  ⇒ Boolean 
  

  

  

  
    

Returns Whether the target uses Swift code.

Returns:

-

        (Boolean)

        —
        

Whether the target uses Swift code

```

218
219
220
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 218

def uses_swift?
  pod_targets.any?(&:uses_swift?)
end

```

###
  
    #**xcconfig_relative_path**(config_name)  ⇒ String 
  

  

  

  
    

Returns The path of the xcconfig file relative to the root of the user project.

Parameters:

-

        config_name

        (String)
      
      
      
        —
        

The build configuration name to get the xcconfig for

Returns:

-

        (String)

        —
        

The path of the xcconfig file relative to the root of the user project.

```

452
453
454
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 452

def xcconfig_relative_path(config_name)
  xcconfig_path(config_name).relative_path_from(client_root).to_s
end

```

###
  
    #**xcframeworks_by_config**  ⇒ Hash{String => Array<Xcode::XCFramework>} 
  

  

  

  
    

Returns The vendored dynamic artifacts and framework target input and output paths grouped by config.

Returns:

-

        (Hash{String => Array<Xcode::XCFramework>})

        —
        

The vendored dynamic artifacts and framework target input and output paths grouped by config

```

268
269
270
271
272
273
274
275
276
277
278
279
280
```

```
# File 'lib/cocoapods/target/aggregate_target.rb', line 268

def xcframeworks_by_config
  @xcframeworks_by_config ||= begin
    xcframeworks_by_config = {}
    user_build_configurations.each_key do |config|
      relevant_pod_targets = pod_targets_for_build_configuration(config)
      xcframeworks_by_config[config] = relevant_pod_targets.flat_map do |pod_target|
        library_specs = pod_target.library_specs.map(&:name)
        pod_target.xcframeworks.values_at(*library_specs).flatten.compact.uniq
      end
    end
    xcframeworks_by_config
  end
end

```
