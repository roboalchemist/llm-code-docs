# Class: Pod::Target::BuildSettings
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Pod::Target::BuildSettings
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/target/build_settings.rb
  
  

## Overview

  
    

  

  

Since:

  
    
- 
      
      
      
      
        
        

1.5.0

      
    
  

  
## Direct Known Subclasses

  

AggregateTargetSettings, PodTargetSettings

## Defined Under Namespace

  
    
  
    
      **Classes:** AggregateTargetSettings, PodTargetSettings
    
  

  
    
## 
      Constants
      collapse
    

    
      
        PLURAL_SETTINGS =
          
  
    

Returns The build settings that should be treated as arrays, rather than strings.

  

  

Returns:

  
    
- 
      
      
        (Set<String>)
      
      
      
        —
        

The build settings that should be treated as arrays, rather than strings.

      
    
  

Since:

  
    
- 
      
      
      
      
        
        

1.5.0

      
    
  

        
        

```
%w(
  ALTERNATE_PERMISSIONS_FILES
  ARCHS
  BUILD_VARIANTS
  EXCLUDED_SOURCE_FILE_NAMES
  FRAMEWORK_SEARCH_PATHS
  GCC_PREPROCESSOR_DEFINITIONS
  GCC_PREPROCESSOR_DEFINITIONS_NOT_USED_IN_PRECOMPS
  HEADER_SEARCH_PATHS
  INCLUDED_SOURCE_FILE_NAMES
  INFOPLIST_PREPROCESSOR_DEFINITIONS
  LD_RUNPATH_SEARCH_PATHS
  LIBRARY_SEARCH_PATHS
  LOCALIZED_STRING_MACRO_NAMES
  OTHER_CFLAGS
  OTHER_CPLUSPLUSFLAGS
  OTHER_LDFLAGS
  OTHER_MODULE_VERIFIER_FLAGS
  OTHER_SWIFT_FLAGS
  REZ_SEARCH_PATHS
  SECTORDER_FLAGS
  SWIFT_ACTIVE_COMPILATION_CONDITIONS
  SWIFT_INCLUDE_PATHS
  SYSTEM_FRAMEWORK_SEARCH_PATHS
  SYSTEM_HEADER_SEARCH_PATHS
  USER_HEADER_SEARCH_PATHS
  WARNING_CFLAGS
  WARNING_LDFLAGS
).to_set.freeze

```

      
        CONFIGURATION_BUILD_DIR_VARIABLE =
          
  
    

Returns The variable for the configuration build directory used when building pod targets.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

The variable for the configuration build directory used when building pod targets.

      
    
  

Since:

  
    
- 
      
      
      
      
        
        

1.5.0

      
    
  

        
        

```
'${PODS_CONFIGURATION_BUILD_DIR}'

```

      
        XCFRAMEWORKS_BUILD_DIR_VARIABLE =
          
  
    

Returns The variable for the configuration intermediate frameworks directory used for building pod targets that contain vendored xcframeworks.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

The variable for the configuration intermediate frameworks directory used for building pod targets that contain vendored xcframeworks.

      
    
  

Since:

  
    
- 
      
      
      
      
        
        

1.5.0

      
    
  

        
        

```
'${PODS_XCFRAMEWORKS_BUILD_DIR}'

```

      
    
  

  
## Public API collapse

  

    
      
- 
  
    
      .**build_settings_names**  ⇒ Set<String> 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

be present in the #xcconfig.

  

    
      
- 
  
    
      #**target**  ⇒ Target 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The target this build settings object is generating build settings for.

  

    
  

  
    
## 
      DSL
      collapse
    

    

      
        
- 
  
    
      .**xcframework_intermediate_dir**(xcframework)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

The path to the directory containing the xcframework slice.

  

      
    

  
    
## 
      Public API
      collapse
    

    

      
        
- 
  
    
      #**initialize**(target)  ⇒ BuildSettings 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize a new instance.

  

      
        
- 
  
    
      #**initialize_copy**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**save_as**(path)  ⇒ Xcodeproj::Config 
    

    
  
  
  
  
  
  
  
  

  
    

Saves the generated xcconfig to the given path.

  

      
        
- 
  
    
      #**xcconfig**  ⇒ Xcodeproj::Config 
    

    
      (also: #generate)
    
  
  
  
  
  
  
  
  

  
    

The `xcconfig` build setting for the #target.

  

      
    

  
    
## 
      Build System
      collapse
    

    

      
        
- 
  
    
      #**pods_build_dir**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

The `pods_build_dir` build setting for the #target.

  

      
        
- 
  
    
      #**pods_configuration_build_dir**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

The `pods_configuration_build_dir` build setting for the #target.

  

      
        
- 
  
    
      #**pods_xcframeworks_build_dir**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The `pods_xcframeworks_build_dir` build setting for the #target.

  

      
        
- 
  
    
      #**use_recursive_script_inputs_in_script_phases**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

The `use_recursive_script_inputs_in_script_phases` build setting for the #target.

  

      
    

  
    
## 
      Code Signing
      collapse
    

    

      
        
- 
  
    
      #**code_sign_identity**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

The `code_sign_identity` build setting for the #target.

  

      
    

  
    
## 
      Frameworks
      collapse
    

    

      
        
- 
  
    
      #**framework_search_paths**  ⇒ Array<String> 
    

    
  
  
  
  
  
  
  
  

  
    

The `framework_search_paths` build setting for the #target.

  

      
        
- 
  
    
      #**framework_search_paths_to_import_developer_frameworks**(frameworks)  ⇒ Array<String> 
    

    
  
  
  
  
  
  
  
  

  
    

The `FRAMEWORK_SEARCH_PATHS` needed to import developer frameworks.

  

      
        
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

  

      
    

  
    
## 
      Clang
      collapse
    

    

      
        
- 
  
    
      #**gcc_preprocessor_definitions**  ⇒ Array<String> 
    

    
  
  
  
  
  
  
  
  

  
    

The `gcc_preprocessor_definitions` build setting for the #target.

  

      
        
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
  
    
      #**other_swift_flags**  ⇒ Array<String> 
    

    
  
  
  
  
  
  
  
  

  
    

The `other_swift_flags` build setting for the #target.

  

      
        
- 
  
    
      #**other_swift_flags_without_swift?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether `OTHER_SWIFT_FLAGS` should be generated when the target does not use swift.

  

      
    

  
    
## 
      Linking
      collapse
    

    

      
        
- 
  
    
      #**clang_warn_quoted_include_in_framework_header**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Xcode 12 turns on this warning by default which is problematic for CocoaPods-generated imports which use double-quoted paths.

  

      
        
- 
  
    
      #**other_ldflags**  ⇒ Array<String> 
    

    
  
  
  
  
  
  
  
  

  
    

The `other_ldflags` build setting for the #target.

  

      
        
- 
  
    
      #**requires_fobjc_arc?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

The `requires_fobjc_arc?` build setting for the #target.

  

      
        
- 
  
    
      #**requires_objc_linker_flag?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

The `requires_objc_linker_flag?` build setting for the #target.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(target)  ⇒ BuildSettings 
  

  

  

  
    

Initialize a new instance

  

  

Parameters:

  
    
- 
      
        target
      
      
        (Target)
      
      
      
        —
        

see #target

      
    
  

Since:

  
    
- 
      
      
      
      
        
        

1.5.0

      
    
  

  
    
      

```

177
178
179
180
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 177

def initialize(target)
  @target = target
  @__memoized = {}
end

```

    
  

  

  
    
## Class Attribute Details

    
      
      
      
  
### 
  
    .**build_settings_names**  ⇒ Set<String>  (readonly)
  

  

  

  
    

be present in the #xcconfig

  

  

Returns:

  
    
- 
      
      
        (Set<String>)
      
      
      
        —
        

a set of all the build settings names that will

      
    
  

Since:

  
    
- 
      
      
      
      
        
        

1.5.0

      
    
  

  
    
      

```

160
161
162
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 160

def build_settings_names
  @build_settings_names
end

```

    
  

    
  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**target**  ⇒ Target  (readonly)
  

  

  

  
    

Returns The target this build settings object is generating build settings for.

  

  

Returns:

  
    
- 
      
      
        (Target)
      
      
      
        —
        

The target this build settings object is generating build settings for

      
    
  

Since:

  
    
- 
      
      
      
      
        
        

1.5.0

      
    
  

  
    
      

```

170
171
172
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 170

def target
  @target
end

```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**xcframework_intermediate_dir**(xcframework)  ⇒ String 
  

  

  

  
    

Returns the path to the directory containing the xcframework slice.

  

  

Parameters:

  
    
- 
      
        xcframework
      
      
        (XCFramework)
      
      
      
        —
        

the xcframework slice that will be copied to the intermediates dir

      
    
  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

the path to the directory containing the xcframework slice

      
    
  

Since:

  
    
- 
      
      
      
      
        
        

1.5.0

      
    
  

  
    
      

```

148
149
150
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 148

def self.xcframework_intermediate_dir(xcframework)
  "#{XCFRAMEWORKS_BUILD_DIR_VARIABLE}/#{xcframework.target_name}"
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**clang_warn_quoted_include_in_framework_header**  ⇒ Boolean 
  

  

  

  
    

Xcode 12 turns on this warning by default which is problematic for CocoaPods-generated imports which use double-quoted paths. The `clang_warn_quoted_include_in_framework_header` build setting for the #target.

The return value from this method will be: ‘clang_warn_quoted_include_in_framework_header, build_setting`.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

344
345
346
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 344

define_build_settings_method :clang_warn_quoted_include_in_framework_header, :build_setting => true do
  'NO'
end

```

    
  

    
      
  
### 
  
    #**code_sign_identity**  ⇒ String 
  

  

  

  
    

The `code_sign_identity` build setting for the #target.

The return value from this method will be: ‘code_sign_identity, build_setting`.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

236
237
238
239
240
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 236

define_build_settings_method :code_sign_identity, :build_setting => true do
  return unless target.build_as_dynamic?
  return unless target.platform.to_sym == :osx
  ''
end

```

    
  

    
      
  
### 
  
    #**framework_search_paths**  ⇒ Array<String> 
  

  

  

  
    

The `framework_search_paths` build setting for the #target.

The return value from this method will be: ‘framework_search_paths, build_setting, memoized`.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

257
258
259
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 257

define_build_settings_method :framework_search_paths, :build_setting => true, :memoized => true do
  framework_search_paths_to_import_developer_frameworks(frameworks + weak_frameworks)
end

```

    
  

    
      
  
### 
  
    #**framework_search_paths_to_import_developer_frameworks**(frameworks)  ⇒ Array<String> 
  

  

  

  
    

Returns the `FRAMEWORK_SEARCH_PATHS` needed to import developer frameworks.

  

  

Parameters:

  
    
- 
      
        frameworks
      
      
        (Array<String>)
      
      
      
        —
        

The list of framework names

      
    
  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
        —
        

the `FRAMEWORK_SEARCH_PATHS` needed to import developer frameworks

      
    
  

Since:

  
    
- 
      
      
      
      
        
        

1.5.0

      
    
  

  
    
      

```

266
267
268
269
270
271
272
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 266

def framework_search_paths_to_import_developer_frameworks(frameworks)
  if frameworks.include?('XCTest') || frameworks.include?('SenTestingKit')
    %w[ $(PLATFORM_DIR)/Developer/Library/Frameworks ]
  else
    []
  end
end

```

    
  

    
      
  
### 
  
    #**frameworks**  ⇒ Array<String> 
  

  

  

  
    

The `frameworks` build setting for the #target.

The return value from this method will be: `frameworks`.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

247
248
249
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 247

define_build_settings_method :frameworks do
  []
end

```

    
  

    
      
  
### 
  
    #**gcc_preprocessor_definitions**  ⇒ Array<String> 
  

  

  

  
    

The `gcc_preprocessor_definitions` build setting for the #target.

The return value from this method will be: ‘gcc_preprocessor_definitions, build_setting`.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

288
289
290
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 288

define_build_settings_method :gcc_preprocessor_definitions, :build_setting => true do
  %w( COCOAPODS=1 )
end

```

    
  

    
      
  
### 
  
    #**initialize_copy**(other)  ⇒ Object 
  

  

  

  
    

  

  

Since:

  
    
- 
      
      
      
      
        
        

1.5.0

      
    
  

  
    
      

```

182
183
184
185
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 182

def initialize_copy(other)
  super
  @__memoized = {}
end

```

    
  

    
      
  
### 
  
    #**libraries**  ⇒ Array<String> 
  

  

  

  
    

The `libraries` build setting for the #target.

The return value from this method will be: `libraries`.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

279
280
281
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 279

define_build_settings_method :libraries do
  []
end

```

    
  

    
      
  
### 
  
    #**module_map_files**  ⇒ Array<String> 
  

  

  

  
    

The `module_map_files` build setting for the #target.

The return value from this method will be: `module_map_files`.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

303
304
305
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 303

define_build_settings_method :module_map_files do
  []
end

```

    
  

    
      
  
### 
  
    #**other_cflags**  ⇒ Array<String> 
  

  

  

  
    

The `other_cflags` build setting for the #target.

The return value from this method will be: ‘other_cflags, build_setting, memoized`.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

293
294
295
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 293

define_build_settings_method :other_cflags, :build_setting => true, :memoized => true do
  module_map_files.map { |f| "-fmodule-map-file=#{f}" }
end

```

    
  

    
      
  
### 
  
    #**other_ldflags**  ⇒ Array<String> 
  

  

  

  
    

The `other_ldflags` build setting for the #target.

The return value from this method will be: ‘other_ldflags, build_setting, memoized`.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

379
380
381
382
383
384
385
386
387
388
389
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 379

define_build_settings_method :other_ldflags, :build_setting => true, :memoized => true do
  ld_flags = []
  ld_flags << '-ObjC' if requires_objc_linker_flag?
  if requires_fobjc_arc?
    ld_flags << '-fobjc-arc'
  end
  libraries.each { |l| ld_flags << %(-l"#{l}") }
  frameworks.each { |f| ld_flags << '-framework' << %("#{f}") }
  weak_frameworks.each { |f| ld_flags << '-weak_framework' << %("#{f}") }
  ld_flags
end

```

    
  

    
      
  
### 
  
    #**other_module_verifier_flags**  ⇒ Array<String> 
  

  

  

  
    

The `other_module_verifier_flags` build setting for the #target.

The return value from this method will be: ‘other_module_verifier_flags, build_setting, memoized`.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

298
299
300
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 298

define_build_settings_method :other_module_verifier_flags, :build_setting => true, :memoized => true do
  []
end

```

    
  

    
      
  
### 
  
    #**other_swift_flags**  ⇒ Array<String> 
  

  

  

  
    

The `other_swift_flags` build setting for the #target.

The return value from this method will be: ‘other_swift_flags, build_setting, memoized`.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

320
321
322
323
324
325
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 320

define_build_settings_method :other_swift_flags, :build_setting => true, :memoized => true do
  return unless target.uses_swift? || other_swift_flags_without_swift?
  flags = %w(-D COCOAPODS)
  flags.concat module_map_files.flat_map { |f| ['-Xcc', "-fmodule-map-file=#{f}"] }
  flags
end

```

    
  

    
      
  
### 
  
    #**other_swift_flags_without_swift?**  ⇒ Boolean 
  

  

  

  
    

Returns Whether `OTHER_SWIFT_FLAGS` should be generated when the target does not use swift.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

Whether `OTHER_SWIFT_FLAGS` should be generated when the target does not use swift.

      
    
  

Since:

  
    
- 
      
      
      
      
        
        

1.5.0

      
    
  

  
    
      

```

315
316
317
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 315

def other_swift_flags_without_swift?
  false
end

```

    
  

    
      
  
### 
  
    #**pods_build_dir**  ⇒ String 
  

  

  

  
    

The `pods_build_dir` build setting for the #target.

The return value from this method will be: ‘pods_build_dir, build_setting`.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

213
214
215
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 213

define_build_settings_method :pods_build_dir, :build_setting => true do
  '${BUILD_DIR}'
end

```

    
  

    
      
  
### 
  
    #**pods_configuration_build_dir**  ⇒ String 
  

  

  

  
    

The `pods_configuration_build_dir` build setting for the #target.

The return value from this method will be: ‘pods_configuration_build_dir, build_setting`.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

218
219
220
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 218

define_build_settings_method :pods_configuration_build_dir, :build_setting => true do
  '${PODS_BUILD_DIR}/$(CONFIGURATION)$(EFFECTIVE_PLATFORM_NAME)'
end

```

    
  

    
      
  
### 
  
    #**pods_xcframeworks_build_dir**  ⇒ Object 
  

  

  

  
    

The `pods_xcframeworks_build_dir` build setting for the #target.

The return value from this method will be: ‘pods_xcframeworks_build_dir, build_setting`.

  

  

  
    
      

```

222
223
224
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 222

define_build_settings_method :pods_xcframeworks_build_dir, :build_setting => true do
  '$(PODS_CONFIGURATION_BUILD_DIR)/XCFrameworkIntermediates'
end

```

    
  

    
      
  
### 
  
    #**requires_fobjc_arc?**  ⇒ Boolean 
  

  

  

  
    

The `requires_fobjc_arc?` build setting for the #target.

The return value from this method will be: `requires_fobjc_arc?`.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

337
338
339
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 337

define_build_settings_method :requires_fobjc_arc? do
  false
end

```

    
  

    
      
  
### 
  
    #**requires_objc_linker_flag?**  ⇒ Boolean 
  

  

  

  
    

The `requires_objc_linker_flag?` build setting for the #target.

The return value from this method will be: `requires_objc_linker_flag?`.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

332
333
334
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 332

define_build_settings_method :requires_objc_linker_flag? do
  false
end

```

    
  

    
      
  
### 
  
    #**save_as**(path)  ⇒ Xcodeproj::Config 
  

  

  

  
    

Saves the generated xcconfig to the given path

  

  

Parameters:

  
    
- 
      
        path
      
      
        (String, Pathname)
      
      
      
        —
        

The path the xcconfig will be saved to

      
    
  

Returns:

  
    
- 
      
      
        (Xcodeproj::Config)
      
      
      
    
  

  

See Also:
  

    
      
- #xcconfig
    
  

Since:

  
    
- 
      
      
      
      
        
        

1.5.0

      
    
  

  
    
      

```

204
205
206
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 204

def save_as(path)
  xcconfig.save_as(path)
end

```

    
  

    
      
  
### 
  
    #**use_recursive_script_inputs_in_script_phases**  ⇒ String 
  

  

  

  
    

The `use_recursive_script_inputs_in_script_phases` build setting for the #target.

The return value from this method will be: ‘use_recursive_script_inputs_in_script_phases, build_setting`.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

227
228
229
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 227

define_build_settings_method :use_recursive_script_inputs_in_script_phases, :build_setting => true do
  'YES'
end

```

    
  

    
      
  
### 
  
    #**weak_frameworks**  ⇒ Array<String> 
  

  

  

  
    

The `weak_frameworks` build setting for the #target.

The return value from this method will be: `weak_frameworks`.

  

  

Returns:

  
    
- 
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

252
253
254
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 252

define_build_settings_method :weak_frameworks do
  []
end

```

    
  

    
      
  
### 
  
    #**xcconfig**  ⇒ Xcodeproj::Config 
  

  
    Also known as:
    generate
    
  

  

  
    

The `xcconfig` build setting for the #target.

The return value from this method will be: ‘xcconfig, memoized`.

  

  

Returns:

  
    
- 
      
      
        (Xcodeproj::Config)
      
      
      
    
  

  
    
      

```

188
189
190
191
```

    
    
      

```
# File 'lib/cocoapods/target/build_settings.rb', line 188

define_build_settings_method :xcconfig, :memoized => true do
  settings = add_inherited_to_plural(to_h)
  Xcodeproj::Config.new(settings)
end

```