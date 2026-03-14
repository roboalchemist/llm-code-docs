# Class: Pod::Installer::Xcode::PodsProjectGenerator::AppHostInstaller
  
    Inherits:
    
      Object
      
        

          
- Object

- Pod::Installer::Xcode::PodsProjectGenerator::AppHostInstaller

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      TargetInstallerHelper
  
    Defined in:
    lib/cocoapods/installer/xcode/pods_project_generator/app_host_installer.rb
  
## Overview

Installs an app host target to a given project.

## Instance Attribute Summary collapse

-
  
      #**add_launchscreen_storyboard**  ⇒ Boolean 

      readonly
    
    
  
  
  
  
  

  
    

Whether the app host installer should add a launch screen storyboard.

-
  
      #**add_main**  ⇒ Boolean 

      readonly
    
    
  
  
  
  
  

  
    

Whether the app host installer should add main.m.

-
  
      #**app_target_label**  ⇒ String 

      readonly
    
    
  
  
  
  
  

  
    

The name of the app target label that will be used.

-
  
      #**group_name**  ⇒ String 

      readonly
    
    
  
  
  
  
  

  
    

The name of the group the app host installer will be installing within.

-
  
      #**info_plist_entries**  ⇒ Hash 

      readonly
    
    
  
  
  
  
  

  
    

Info.plist entries for the app host.

-
  
      #**platform**  ⇒ Platform 

      readonly
    
    
  
  
  
  
  

  
    

The platform to use for this app host.

-
  
      #**product_basename**  ⇒ String 

      readonly
    
    
  
  
  
  
  

  
    

Product_basename The product basename to use for the target.

-
  
      #**project**  ⇒ Pod::Project 

      readonly
    
    
  
  
  
  
  

  
    

The project to install the app host into.

-
  
      #**sandbox**  ⇒ Sandbox 

      readonly
    
    
  
  
  
  
  

  
    

The sandbox used for this installation.

-
  
      #**subgroup_name**  ⇒ String 

      readonly
    
    
  
  
  
  
  

  
    

The name of the sub group.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(sandbox, project, platform, subgroup_name, group_name, app_target_label, add_main: true, add_launchscreen_storyboard: platform == :ios, info_plist_entries: {}, product_basename: nil)  ⇒ AppHostInstaller 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize a new instance.

-
  
      #**install!**  ⇒ PBXNativeTarget 

The app host native target that was installed.

### Methods included from TargetInstallerHelper

create_info_plist_file_with_sandbox, create_prefix_header, update_changed_file

## Constructor Details

###
  
    #**initialize**(sandbox, project, platform, subgroup_name, group_name, app_target_label, add_main: true, add_launchscreen_storyboard: platform == :ios, info_plist_entries: {}, product_basename: nil)  ⇒ AppHostInstaller 
  

  

  

  
    

Initialize a new instance

Parameters:

-

        sandbox

        (Sandbox)
      
      
      
        —
        

@see #sandbox

-

        project

        (Pod::Project)
      
      
      
        —
        

@see #project

-

        platform

        (Platform)
      
      
      
        —
        

@see #platform

-

        subgroup_name

        (String)
      
      
      
        —
        

@see #subgroup_name

-

        group_name

        (String)
      
      
      
        —
        

@see #group_name

-

        app_target_label

        (String)
      
      
      
        —
        

see #app_target_label

-

        add_main

        (Boolean)
      
      
        *(defaults to: true)*
      
      
        —
        

see #add_main

-

        info_plist_entries

        (Hash)
      
      
        *(defaults to: {})*
      
      
        —
        

see #info_plist_entries

-

        product_basename

        (String)
      
      
        *(defaults to: nil)*
      
      
        —
        

see #product_basename

```

65
66
67
68
69
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
```

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/app_host_installer.rb', line 65

def initialize(sandbox, project, platform, subgroup_name, group_name, app_target_label, add_main: true,
               add_launchscreen_storyboard: platform == :ios, info_plist_entries: {}, product_basename: nil)
  @sandbox = sandbox
  @project = project
  @platform = platform
  @subgroup_name = subgroup_name
  @group_name = group_name
  @app_target_label = app_target_label
  @add_main = add_main
  @add_launchscreen_storyboard = add_launchscreen_storyboard
  @info_plist_entries = info_plist_entries
  @product_basename = product_basename || app_target_label
  target_group = project.pod_group(group_name)
  @group = target_group[subgroup_name] || target_group.new_group(subgroup_name)
end

```

## Instance Attribute Details

###
  
    #**add_launchscreen_storyboard**  ⇒ Boolean  (readonly)
  

  

  

  
    

Returns whether the app host installer should add a launch screen storyboard.

Returns:

-

        (Boolean)

        —
        

whether the app host installer should add a launch screen storyboard

```

42
43
44
```

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/app_host_installer.rb', line 42

def add_launchscreen_storyboard
  @add_launchscreen_storyboard
end

```

###
  
    #**add_main**  ⇒ Boolean  (readonly)
  

  

  

  
    

Returns whether the app host installer should add main.m.

Returns:

-

        (Boolean)

        —
        

whether the app host installer should add main.m

```

38
39
40
```

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/app_host_installer.rb', line 38

def add_main
  @add_main
end

```

###
  
    #**app_target_label**  ⇒ String  (readonly)
  

  

  

  
    

Returns the name of the app target label that will be used.

Returns:

-

        (String)

        —
        

the name of the app target label that will be used.

```

34
35
36
```

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/app_host_installer.rb', line 34

def app_target_label
  @app_target_label
end

```

###
  
    #**group_name**  ⇒ String  (readonly)
  

  

  

  
    

Returns the name of the group the app host installer will be installing within.

Returns:

-

        (String)

        —
        

the name of the group the app host installer will be installing within.

```

30
31
32
```

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/app_host_installer.rb', line 30

def group_name
  @group_name
end

```

###
  
    #**info_plist_entries**  ⇒ Hash  (readonly)
  

  

  

  
    

Returns Info.plist entries for the app host.

Returns:

-

        (Hash)

        —
        

Info.plist entries for the app host

```

46
47
48
```

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/app_host_installer.rb', line 46

def info_plist_entries
  @info_plist_entries
end

```

###
  
    #**platform**  ⇒ Platform  (readonly)
  

  

  

  
    

Returns the platform to use for this app host.

Returns:

-

        (Platform)

        —
        

the platform to use for this app host.

```

22
23
24
```

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/app_host_installer.rb', line 22

def platform
  @platform
end

```

###
  
    #**product_basename**  ⇒ String  (readonly)
  

  

  

  
    

Returns product_basename The product basename to use for the target.

Returns:

-

        (String)

        —
        

product_basename The product basename to use for the target.

```

51
52
53
```

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/app_host_installer.rb', line 51

def product_basename
  @product_basename
end

```

###
  
    #**project**  ⇒ Pod::Project  (readonly)
  

  

  

  
    

Returns The project to install the app host into.

Returns:

-

        (Pod::Project)

        —
        

The project to install the app host into.

```

18
19
20
```

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/app_host_installer.rb', line 18

def project
  @project
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

13
14
15
```

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/app_host_installer.rb', line 13

def sandbox
  @sandbox
end

```

###
  
    #**subgroup_name**  ⇒ String  (readonly)
  

  

  

  
    

Returns the name of the sub group.

Returns:

-

        (String)

        —
        

the name of the sub group.

```

26
27
28
```

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/app_host_installer.rb', line 26

def subgroup_name
  @subgroup_name
end

```

## Instance Method Details

###
  
    #**install!**  ⇒ PBXNativeTarget 
  

  

  

  
    

Returns the app host native target that was installed.

Returns:

-

        (PBXNativeTarget)

        —
        

the app host native target that was installed.

```

83
84
85
86
87
88
89
90
91
92
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
104
```

```
# File 'lib/cocoapods/installer/xcode/pods_project_generator/app_host_installer.rb', line 83

def install!
  platform_name = platform.name
  app_host_target = Pod::Generator::AppTargetHelper.add_app_target(project, platform_name, deployment_target,
                                                                   app_target_label, product_basename)
  app_host_target.build_configurations.each do |configuration|
    configuration.build_settings['PRODUCT_NAME'] = product_basename
    configuration.build_settings['PRODUCT_BUNDLE_IDENTIFIER'] = 'org.cocoapods.${PRODUCT_NAME:rfc1034identifier}'
    if platform == :osx
      configuration.build_settings['CODE_SIGN_IDENTITY'] = ''
    elsif platform == :ios
      configuration.build_settings['CODE_SIGN_IDENTITY'] = 'iPhone Developer'
    end
    configuration.build_settings['CURRENT_PROJECT_VERSION'] = '1'
  end

  Pod::Generator::AppTargetHelper.add_app_host_main_file(project, app_host_target, platform_name, @group, app_target_label) if add_main
  Pod::Generator::AppTargetHelper.add_launchscreen_storyboard(project, app_host_target, @group, deployment_target, app_target_label) if add_launchscreen_storyboard
  create_info_plist_file_with_sandbox(sandbox, app_host_info_plist_path, app_host_target, '1.0.0', platform,
                                      :appl, :additional_entries => additional_info_plist_entries)
  @group.new_file(app_host_info_plist_path)
  app_host_target
end

```
