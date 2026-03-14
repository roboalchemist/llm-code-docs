# Class: Pod::Target::BuildSettings::AggregateTargetSettings
  
  
  

  
  
    Inherits:
    
      Pod::Target::BuildSettings
      
        

          
- Object
          
            
- Pod::Target::BuildSettings
          
            
- Pod::Target::BuildSettings::AggregateTargetSettings
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/target/build_settings.rb
  
  

## Overview

  
    

A subclass that generates build settings for a `PodTarget`

  

  

Since:

  
    
- 
      
      
      
      
        
        

1.5.0

      
    
  

  
## Constant Summary

  
  
### Constants inherited
     from Pod::Target::BuildSettings

  

CONFIGURATION_BUILD_DIR_VARIABLE, PLURAL_SETTINGS, XCFRAMEWORKS_BUILD_DIR_VARIABLE

  
## Public API collapse

  

    
      
- 
  
    
      #**configuration_name**  ⇒ Symbol 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The build configuration these settings will be used for.

  

    
  

  
  
  
### Attributes inherited from Pod::Target::BuildSettings

  

#target

  
    
## 
      Public API
      collapse
    

    

      
        
- 
  
    
      .**build_settings_names**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(target, configuration_name, configuration: nil)  ⇒ AggregateTargetSettings 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initializes a new instance.

  

      
        
- 
  
    
      #**xcconfig**  ⇒ Xcodeproj::Config 
    

    
  
  
  
  
  
  
  
  

  
    

The `xcconfig` build setting for the #target.

  

      
    

  
    
## 
      Paths
      collapse
    

    

      
        
- 
  
    
      #**pods_podfile_dir_path**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

The `pods_podfile_dir_path` build setting for the #target.

  

      
        
- 
  
    
      #**pods_root**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

The `pods_root` build setting for the #target.

  

      
    

  
    
## 
      Frameworks
      collapse
    

    

      
        
- 
  
    
      #**framework_search_paths**  ⇒ Array<String> 
    

    
  
  
  
  
  
  
  
  

  
    

The `framework_search_paths` build setting for the #target.

  

      
        
- 
  
    
      #**frameworks**  ⇒ Array<String> 
    

    
  
  
  
  
  
  
  
  

  
    

The `frameworks` build setting for the #target.

  

      
        
- 
  
    
      #**weak_frameworks**  ⇒ Array<String> 
    

    
  
  
  
  
  
  
  
  

  
    

The `weak_frameworks` build setting for the #target.

  

      
    

  
    
## 
      Libraries
      collapse
    

    

      
        
- 
  
    
      #**libraries**  ⇒ Array<String> 
    

    
  
  
  
  
  
  
  
  

  
    

The `libraries` build setting for the #target.

  

      
        
- 
  
    
      #**library_search_paths**  ⇒ Array<String> 
    

    
  
  
  
  
  
  
  
  

  
    

The `library_search_paths` build setting for the #target.

  

      
    

  
    
## 
      Clang
      collapse
    

    

      
        
- 
  
    
      #**header_search_paths**  ⇒ Array<String> 
    

    
  
  
  
  
  
  
  
  

  
    

The `header_search_paths` build setting for the #target.

  

      
        
- 
  
    
      #**module_map_files**  ⇒ Array<String> 
    

    
  
  
  
  
  
  
  
  

  
    

The `module_map_files` build setting for the #target.

  

      
        
- 
  
    
      #**other_cflags**  ⇒ Array<String> 
    

    
  
  
  
  
  
  
  
  

  
    

The `other_cflags` build setting for the #target.

  

      
        
- 
  
    
      #**other_module_verifier_flags**  ⇒ Array<String> 
    

    
  
  
  
  
  
  
  
  

  
    

The `other_module_verifier_flags` build setting for the #target.

  

      
    

  
    
## 
      Swift
      collapse
    

    

      
        
- 
  
    
      #**always_embed_swift_standard_libraries**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

The `always_embed_swift_standard_libraries` build setting for the #target.

  

      
        
- 
  
    
      #**embedded_content_contains_swift**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

The `embedded_content_contains_swift` build setting for the #target.

  

      
        
- 
  
    
      #**must_embed_swift?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

The `must_embed_swift?` build setting for the #target.

  

      
        
- 
  
    
      #**other_swift_flags_without_swift?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**swift_include_paths**  ⇒ Array<String> 
    

    
  
  
  
  
  
  
  
  

  
    

The `swift_include_paths` build setting for the #target.

  

      
    

  
    
## 
      Linking
      collapse
    

    

      
        
- 
  
    
      #**any_vendored_dynamic_artifacts?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

The `any_vendored_dynamic_artifacts?` build setting for the #target.

  

      
        
- 
  
    
      #**any_vendored_static_artifacts?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

The `any_vendored_static_artifacts?` build setting for the #target.

  

      
        
- 
  
    
      #**ld_runpath_search_paths**  ⇒ Array<String> 
    

    
  
  
  
  
  
  
  
  

  
    

The `ld_runpath_search_paths` build setting for the #target.

  

      
        
- 
  
    
      #**requires_fobjc_arc?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

The `requires_fobjc_arc?` build setting for the #target.

  

      
        
- 
  
    
      #**requires_objc_linker_flag?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

The `requires_objc_linker_flag?` build setting for the #target.

  

      
    

  
    
## 
      Target Properties
      collapse
    

    

      
        
- 
  
    
      #**merged_user_target_xcconfigs**  ⇒ Hash{String, String} 
    

    
  
  
  
  
  
  
  
  

  
    

Merges the `user_target_xcconfig` for all pod targets into a single hash and warns on conflicting definitions.

  

      
        
- 
  
    
      #**pod_targets**  ⇒ Array<PodTarget> 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the PodTargets which are active for the current configuration name.

  

      
        
- 
  
    
      #**pod_targets_to_link**  ⇒ Array<PodTarget> 
    

    
  
  
  
  
  
  
  
  

  
    

The `pod_targets_to_link` build setting for the #target.

  

      
        
- 
  
    
      #**search_paths_aggregate_target_pod_target_build_settings**  ⇒ Array<PodTarget> 
    

    
  
  
  
  
  
  
  
  

  
    

The `search_paths_aggregate_target_pod_target_build_settings` build setting for the #target.

  

      
        
- 
  
    
      #**target_swift_version**  ⇒ Version 
    

    
  
  
  
  
  
  
  
  

  
    

The `target_swift_version` build setting for the #target.

  

      
        
- 
  
    
      #**user_target_xcconfig_values_by_consumer_by_key**  ⇒ Hash{String,Hash{Target,String}] 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the `user_target_xcconfig` for all pod targets and their spec consumers grouped by keys.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Pod::Target::BuildSettings

  

#clang_warn_quoted_include_in_framework_header, #code_sign_identity, #framework_search_paths_to_import_developer_frameworks, #gcc_preprocessor_definitions, #initialize_copy, #other_ldflags, #other_swift_flags, #pods_build_dir, #pods_configuration_build_dir, #pods_xcframeworks_build_dir, #save_as, #use_recursive_script_inputs_in_script_phases, xcframework_intermediate_dir

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(target, configuration_name, configuration: nil)  ⇒ AggregateTargetSettings 
  

  

  

  
    

Initializes a new instance

  

  

Parameters:

  
    
- 
      
        target
      
      
        (AggregateTarget)
      
      
      
        —
        

see Pod::Target::BuildSettings#target

      
    
  
    
- 
      
        configuration_name
      
      
        (Symbol)
      
      
      
        —
        

see #configuration_name

      
    
  

Since:

  
    
- 
      
      
      
      
        
        

1.5.0

      
    
  

  
    
      

```

1130
1131
1132
1133
1134
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1130

def initialize(target, configuration_name, configuration: nil)
  super(target)
  @configuration_name = configuration_name
  (@configuration = configuration) || raise("No configuration for #{self}.")
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**configuration_name**  ⇒ Symbol  (readonly)
  

  

  

  
    

Returns The build configuration these settings will be used for.

  

  

Returns:

  
    
- 
      
      
        (Symbol)
      
      
      
        —
        

The build configuration these settings will be used for

      
    
  

Since:

  
    
- 
      
      
      
      
        
        

1.5.0

      
    
  

  
    
      

```

1120
1121
1122
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1120

def configuration_name
  @configuration_name
end

```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**build_settings_names**  ⇒ Object 
  

  

  

  
    

  

  

  

See Also:
  

    
      
- Pod::Target::BuildSettings.build_settings_names
    
  

Since:

  
    
- 
      
      
      
      
        
        

1.5.0

      
    
  

  
    
      

```

1114
1115
1116
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1114

def self.build_settings_names
  @build_settings_names | BuildSettings.build_settings_names
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**always_embed_swift_standard_libraries**  ⇒ String 
  

  

  

  
    

The `always_embed_swift_standard_libraries` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘always_embed_swift_standard_libraries, build_setting, memoized`.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

1269
1270
1271
1272
1273
1274
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1269

define_build_settings_method :always_embed_swift_standard_libraries, :build_setting => true, :memoized => true do
  return unless must_embed_swift?
  return if target_swift_version < EMBED_STANDARD_LIBRARIES_MINIMUM_VERSION

  'YES'
end

```

    
  

    
      
  
### 
  
    #**any_vendored_dynamic_artifacts?**  ⇒ Boolean 
  

  

  

  
    

The `any_vendored_dynamic_artifacts?` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘any_vendored_dynamic_artifacts?, memoized`.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1303
1304
1305
1306
1307
1308
1309
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1303

define_build_settings_method :any_vendored_dynamic_artifacts?, :memoized => true do
  pod_targets.any? do |pt|
    pt.file_accessors.any? do |fa|
      !fa.vendored_dynamic_artifacts.empty? || !fa.vendored_dynamic_xcframeworks.empty?
    end
  end
end

```

    
  

    
      
  
### 
  
    #**any_vendored_static_artifacts?**  ⇒ Boolean 
  

  

  

  
    

The `any_vendored_static_artifacts?` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘any_vendored_static_artifacts?, memoized`.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1312
1313
1314
1315
1316
1317
1318
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1312

define_build_settings_method :any_vendored_static_artifacts?, :memoized => true do
  pod_targets.any? do |pt|
    pt.file_accessors.any? do |fa|
      !fa.vendored_static_artifacts.empty?
    end
  end
end

```

    
  

    
      
  
### 
  
    #**embedded_content_contains_swift**  ⇒ String 
  

  

  

  
    

The `embedded_content_contains_swift` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘embedded_content_contains_swift, build_setting, memoized`.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

1277
1278
1279
1280
1281
1282
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1277

define_build_settings_method :embedded_content_contains_swift, :build_setting => true, :memoized => true do
  return unless must_embed_swift?
  return if target_swift_version >= EMBED_STANDARD_LIBRARIES_MINIMUM_VERSION

  'YES'
end

```

    
  

    
      
  
### 
  
    #**framework_search_paths**  ⇒ Array<String> 
  

  

  

  
    

The `framework_search_paths` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘framework_search_paths, build_setting, memoized, sorted, uniqued, from_pod_targets_to_link, from_search_paths_aggregate_targets`.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

1171
1172
1173
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1171

define_build_settings_method :framework_search_paths, :build_setting => true, :memoized => true, :sorted => true, :uniqued => true, :from_pod_targets_to_link => true, :from_search_paths_aggregate_targets => :framework_search_paths_to_import do
  []
end

```

    
  

    
      
  
### 
  
    #**frameworks**  ⇒ Array<String> 
  

  

  

  
    

The `frameworks` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘frameworks, memoized, sorted, uniqued, from_pod_targets_to_link, from_search_paths_aggregate_targets`.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

1161
1162
1163
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1161

define_build_settings_method :frameworks, :memoized => true, :sorted => true, :uniqued => true, :from_pod_targets_to_link => true, :from_search_paths_aggregate_targets => :dynamic_frameworks_to_import do
  []
end

```

    
  

    
      
  
### 
  
    #**header_search_paths**  ⇒ Array<String> 
  

  

  

  
    

The `header_search_paths` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘header_search_paths, build_setting, memoized, sorted, uniqued`.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

1194
1195
1196
1197
1198
1199
1200
1201
1202
1203
1204
1205
1206
1207
1208
1209
1210
1211
1212
1213
1214
1215
1216
1217
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1194

define_build_settings_method :header_search_paths, :build_setting => true, :memoized => true, :sorted => true, :uniqued => true do
  paths = []

  if !target.build_as_framework? || !pod_targets.all?(&:should_build?)
    paths.concat target.sandbox.public_headers.search_paths(target.platform)
  end

  # Make frameworks headers discoverable with any syntax (quotes,
  # brackets, @import, etc.)
  paths.concat pod_targets.
    select { |pt| pt.build_as_framework? && pt.should_build? }.
    map { |pt| pt.build_settings[@configuration].framework_header_search_path }

  xcframework_library_headers = pod_targets.flat_map { |pt| pt.build_settings[@configuration].vendored_xcframeworks }.
                                select { |xcf| xcf.build_type.static_library? }.
                                map { |xcf| "#{BuildSettings.xcframework_intermediate_dir(xcf)}/Headers" }.
                                compact

  paths.concat xcframework_library_headers

  paths.concat target.search_paths_aggregate_targets.flat_map { |at| at.build_settings(configuration_name).header_search_paths }

  paths
end

```

    
  

    
      
  
### 
  
    #**ld_runpath_search_paths**  ⇒ Array<String> 
  

  

  

  
    

The `ld_runpath_search_paths` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘ld_runpath_search_paths, build_setting, memoized, uniqued`.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

1294
1295
1296
1297
1298
1299
1300
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1294

define_build_settings_method :ld_runpath_search_paths, :build_setting => true, :memoized => true, :uniqued => true do
  return unless pod_targets.any?(&:build_as_dynamic?) || any_vendored_dynamic_artifacts?
  symbol_type = target.user_targets.map(&:symbol_type).uniq.first
  test_bundle = symbol_type == :octest_bundle || symbol_type == :unit_test_bundle || symbol_type == :ui_test_bundle
  _ld_runpath_search_paths(:requires_host_target => target.requires_host_target?, :test_bundle => test_bundle,
                           :uses_swift => pod_targets.any?(&:uses_swift?))
end

```

    
  

    
      
  
### 
  
    #**libraries**  ⇒ Array<String> 
  

  

  

  
    

The `libraries` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘libraries, memoized, sorted, uniqued, from_pod_targets_to_link, from_search_paths_aggregate_targets`.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

1180
1181
1182
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1180

define_build_settings_method :libraries, :memoized => true, :sorted => true, :uniqued => true, :from_pod_targets_to_link => true, :from_search_paths_aggregate_targets => :dynamic_libraries_to_import do
  []
end

```

    
  

    
      
  
### 
  
    #**library_search_paths**  ⇒ Array<String> 
  

  

  

  
    

The `library_search_paths` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘library_search_paths, build_setting, memoized, sorted, uniqued, from_pod_targets_to_link, from_search_paths_aggregate_targets`.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

1185
1186
1187
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1185

define_build_settings_method :library_search_paths, :build_setting => true, :memoized => true, :sorted => true, :uniqued => true, :from_pod_targets_to_link => true, :from_search_paths_aggregate_targets => :vendored_dynamic_library_search_paths do
  []
end

```

    
  

    
      
  
### 
  
    #**merged_user_target_xcconfigs**  ⇒ Hash{String, String} 
  

  

  

  
    

Merges the `user_target_xcconfig` for all pod targets into a single hash and warns on conflicting definitions.

The `merged_user_target_xcconfigs` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘merged_user_target_xcconfigs, memoized`.

  

  

Returns:

  
    
- 
      
      
        (Hash{String, String})
      
      
      
    
  

  
    
      

```

1395
1396
1397
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1395

define_build_settings_method :merged_user_target_xcconfigs, :memoized => true do
  merged_xcconfigs(user_target_xcconfig_values_by_consumer_by_key, :user_target_xcconfig)
end

```

    
  

    
      
  
### 
  
    #**module_map_files**  ⇒ Array<String> 
  

  

  

  
    

The `module_map_files` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘module_map_files, memoized, sorted, uniqued, compacted, from_search_paths_aggregate_targets`.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

1250
1251
1252
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1250

define_build_settings_method :module_map_files, :memoized => true, :sorted => true, :uniqued => true, :compacted => true, :from_search_paths_aggregate_targets => :module_map_file_to_import do
  pod_targets.map { |pt| pt.build_settings[@configuration].module_map_file_to_import }
end

```

    
  

    
      
  
### 
  
    #**must_embed_swift?**  ⇒ Boolean 
  

  

  

  
    

The `must_embed_swift?` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘must_embed_swift?, memoized`.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1285
1286
1287
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1285

define_build_settings_method :must_embed_swift?, :memoized => true do
  !target.requires_host_target? && pod_targets.any?(&:uses_swift?)
end

```

    
  

    
      
  
### 
  
    #**other_cflags**  ⇒ Array<String> 
  

  

  

  
    

The `other_cflags` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘other_cflags, build_setting, memoized`.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

1220
1221
1222
1223
1224
1225
1226
1227
1228
1229
1230
1231
1232
1233
1234
1235
1236
1237
1238
1239
1240
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1220

define_build_settings_method :other_cflags, :build_setting => true, :memoized => true do
  flags = super()

  pod_targets_inhibiting_warnings = pod_targets.select(&:inhibit_warnings?)

  silenced_headers = []
  silenced_frameworks = []
  pod_targets_inhibiting_warnings.each do |pt|
    if pt.build_as_framework? && pt.should_build?
      silenced_headers.append pt.build_settings[@configuration].framework_header_search_path
    else
      silenced_headers.concat pt.build_settings[@configuration].public_header_search_paths
    end
    silenced_frameworks.concat pt.build_settings[@configuration].framework_search_paths_to_import
  end

  flags += silenced_headers.uniq.flat_map { |p| ['-isystem', p] }
  flags += silenced_frameworks.uniq.flat_map { |p| ['-iframework', p] }

  flags
end

```

    
  

    
      
  
### 
  
    #**other_module_verifier_flags**  ⇒ Array<String> 
  

  

  

  
    

The `other_module_verifier_flags` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘other_module_verifier_flags, memoized`.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

1243
1244
1245
1246
1247
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1243

define_build_settings_method :other_module_verifier_flags, :memoized => true do
  flags = super()
  flags += pod_targets.map { |pt| '-F' + pt.build_settings[@configuration].configuration_build_dir }
  flags
end

```

    
  

    
      
  
### 
  
    #**other_swift_flags_without_swift?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  

See Also:
  

    
      
- Pod::Target::BuildSettings#other_swift_flags_without_swift?
    
  

Since:

  
    
- 
      
      
      
      
        
        

1.5.0

      
    
  

  
    
      

```

1259
1260
1261
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1259

def other_swift_flags_without_swift?
  module_map_files.any?
end

```

    
  

    
      
  
### 
  
    #**pod_targets**  ⇒ Array<PodTarget> 
  

  

  

  
    

Returns the PodTargets which are active for the current configuration name.

The `pod_targets` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘pod_targets, memoized`.

  

  

Returns:

  
    
- 
      
      
        (Array<PodTarget>)
      
      
      
    
  

  
    
      

```

1352
1353
1354
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1352

define_build_settings_method :pod_targets, :memoized => true do
  target.pod_targets_for_build_configuration(configuration_name)
end

```

    
  

    
      
  
### 
  
    #**pod_targets_to_link**  ⇒ Array<PodTarget> 
  

  

  

  
    

The `pod_targets_to_link` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘pod_targets_to_link, memoized`.

  

  

Returns:

  
    
- 
      
      
        (Array<PodTarget>)
      
      
      
    
  

  
    
      

```

1357
1358
1359
1360
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1357

define_build_settings_method :pod_targets_to_link, :memoized => true do
  pod_targets -
    target.search_paths_aggregate_targets.flat_map { |at| at.build_settings(configuration_name).pod_targets_to_link }
end

```

    
  

    
      
  
### 
  
    #**pods_podfile_dir_path**  ⇒ String 
  

  

  

  
    

The `pods_podfile_dir_path` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘pods_podfile_dir_path, build_setting, memoized`.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

1147
1148
1149
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1147

define_build_settings_method :pods_podfile_dir_path, :build_setting => true, :memoized => true do
  target.podfile_dir_relative_path
end

```

    
  

    
      
  
### 
  
    #**pods_root**  ⇒ String 
  

  

  

  
    

The `pods_root` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘pods_root, build_setting, memoized`.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

1152
1153
1154
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1152

define_build_settings_method :pods_root, :build_setting => true, :memoized => true do
  target.relative_pods_root
end

```

    
  

    
      
  
### 
  
    #**requires_fobjc_arc?**  ⇒ Boolean 
  

  

  

  
    

The `requires_fobjc_arc?` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘requires_fobjc_arc?, memoized`.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1327
1328
1329
1330
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1327

define_build_settings_method :requires_fobjc_arc?, :memoized => true do
  target.podfile.set_arc_compatibility_flag? &&
  target.spec_consumers.any?(&:requires_arc?)
end

```

    
  

    
      
  
### 
  
    #**requires_objc_linker_flag?**  ⇒ Boolean 
  

  

  

  
    

The `requires_objc_linker_flag?` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘requires_objc_linker_flag?, memoized`.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1321
1322
1323
1324
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1321

define_build_settings_method :requires_objc_linker_flag?, :memoized => true do
  pod_targets.any?(&:build_as_static?) ||
    any_vendored_static_artifacts?
end

```

    
  

    
      
  
### 
  
    #**search_paths_aggregate_target_pod_target_build_settings**  ⇒ Array<PodTarget> 
  

  

  

  
    

The `search_paths_aggregate_target_pod_target_build_settings` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘search_paths_aggregate_target_pod_target_build_settings, memoized, uniqued`.

  

  

Returns:

  
    
- 
      
      
        (Array<PodTarget>)
      
      
      
    
  

  
    
      

```

1363
1364
1365
1366
1367
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1363

define_build_settings_method :search_paths_aggregate_target_pod_target_build_settings, :memoized => true, :uniqued => true do
  pod_targets = target.search_paths_aggregate_targets.flat_map { |at| at.build_settings(configuration_name).pod_targets }
  pod_targets = select_maximal_pod_targets(pod_targets)
  pod_targets.map { |pt| pt.build_settings[@configuration] }
end

```

    
  

    
      
  
### 
  
    #**swift_include_paths**  ⇒ Array<String> 
  

  

  

  
    

The `swift_include_paths` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘swift_include_paths, build_setting, memoized, sorted, uniqued, from_pod_targets_to_link, from_search_paths_aggregate_targets`.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

1264
1265
1266
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1264

define_build_settings_method :swift_include_paths, :build_setting => true, :memoized => true, :sorted => true, :uniqued => true, :from_pod_targets_to_link => true, :from_search_paths_aggregate_targets => :swift_include_paths_to_import do
  []
end

```

    
  

    
      
  
### 
  
    #**target_swift_version**  ⇒ Version 
  

  

  

  
    

The `target_swift_version` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘target_swift_version, memoized, frozen`.

  

  

Returns:

  
    
- 
      
      
        (Version)
      
      
      
        —
        

the SWIFT_VERSION of the target being integrated

      
    
  

  
    
      

```

1338
1339
1340
1341
1342
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1338

define_build_settings_method :target_swift_version, :memoized => true, :frozen => false do
  swift_version = target.target_definition.swift_version
  swift_version = nil if swift_version.blank?
  Version.new(swift_version)
end

```

    
  

    
      
  
### 
  
    #**user_target_xcconfig_values_by_consumer_by_key**  ⇒ Hash{String,Hash{Target,String}] 
  

  

  

  
    

Returns the `user_target_xcconfig` for all pod targets and their spec consumers grouped by keys

  

  

Returns:

  
    
- 
      
      
        (Hash{String,Hash{Target,String}])
      
      
      
        —
        

HashString,Hash{Target,String]

      
    
  

Since:

  
    
- 
      
      
      
      
        
        

1.5.0

      
    
  

  
    
      

```

1374
1375
1376
1377
1378
1379
1380
1381
1382
1383
1384
1385
1386
1387
1388
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1374

def user_target_xcconfig_values_by_consumer_by_key
  targets = (pod_targets + target.search_paths_aggregate_targets.flat_map(&:pod_targets)).uniq
  targets.each_with_object({}) do |target, hash|
    target.spec_consumers.each do |spec_consumer|
      spec_consumer.user_target_xcconfig.each do |k, v|
        # TODO: Need to decide how we are going to ensure settings like these
        # are always excluded from the user's project.
        #
        # See https://github.com/CocoaPods/CocoaPods/issues/1216
        next if k == 'USE_HEADERMAP'
        (hash[k] ||= {})[spec_consumer] = v
      end
    end
  end
end

```

    
  

    
      
  
### 
  
    #**weak_frameworks**  ⇒ Array<String> 
  

  

  

  
    

The `weak_frameworks` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘weak_frameworks, memoized, sorted, uniqued, from_pod_targets_to_link, from_search_paths_aggregate_targets`.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

1166
1167
1168
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1166

define_build_settings_method :weak_frameworks, :memoized => true, :sorted => true, :uniqued => true, :from_pod_targets_to_link => true, :from_search_paths_aggregate_targets => :weak_frameworks do
  []
end

```

    
  

    
      
  
### 
  
    #**xcconfig**  ⇒ Xcodeproj::Config 
  

  

  

  
    

The `xcconfig` build setting for the Pod::Target::BuildSettings#target.

The return value from this method will be: ‘xcconfig, memoized`.

  

  

Returns:

  
    
- 
      
      
        (Xcodeproj::Config)
      
      
      
        —
        

xcconfig

      
    
  

  
    
      

```

1137
1138
1139
1140
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 1137

define_build_settings_method :xcconfig, :memoized => true do
  xcconfig = super()
  merge_spec_xcconfig_into_xcconfig(merged_user_target_xcconfigs, xcconfig)
end

```