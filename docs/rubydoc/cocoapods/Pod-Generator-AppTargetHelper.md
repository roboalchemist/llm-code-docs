# Module: Pod::Generator::AppTargetHelper
  
    Defined in:
    lib/cocoapods/generator/app_target_helper.rb
  
## Overview

Stores the common logic for creating app targets within projects including generating standard import and main files for app hosts.

##

      Constant Summary
      collapse
    

    
      
        IOS_APP_HOST_MAIN_CONTENTS =
          
        
        

```
<<EOS.freeze
#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>

@interface CPTestAppHostAppDelegate : UIResponder <UIApplicationDelegate>

@property (nonatomic, strong) UIWindow *window;

@end

@implementation CPTestAppHostAppDelegate

- (BOOL)application:(UIApplication *)__unused application didFinishLaunchingWithOptions:(NSDictionary *)__unused launchOptions
{
    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    self.window.rootViewController = [UIViewController new];

    [self.window makeKeyAndVisible];

    return YES;
}

@end

int main(int argc, char *argv[])
{
    @autoreleasepool
    {
        return UIApplicationMain(argc, argv, nil, NSStringFromClass([CPTestAppHostAppDelegate class]));
    }
}
EOS
```

        MACOS_APP_HOST_MAIN_CONTENTS =
          
        
        

```
<<EOS.freeze
#import <Cocoa/Cocoa.h>

int main(int argc, const char * argv[]) {
    return NSApplicationMain(argc, argv);
}
EOS
```

        LAUNCHSCREEN_STORYBOARD_CONTENTS_IOS_8 =
          
        
        

```
<<-XML.strip_heredoc.freeze
        <?xml version="1.0" encoding="UTF-8" standalone="no"?>
        <document type="com.apple.InterfaceBuilder3.CocoaTouch.Storyboard.XIB" version="3.0" toolsVersion="13122.16" systemVersion="17A277" targetRuntime="iOS.CocoaTouch" propertyAccessControl="none" useAutolayout="YES" launchScreen="YES" useTraitCollections="YES" colorMatched="YES" initialViewController="01J-lp-oVM">
          <dependencies>
            <plugIn identifier="com.apple.InterfaceBuilder.IBCocoaTouchPlugin" version="13104.12"/>
            <capability name="documents saved in the Xcode 8 format" minToolsVersion="8.0"/>
          </dependencies>
          <scenes>
            <!--View Controller-->
            <scene sceneID="EHf-IW-A2E">
              <objects>
                <viewController id="01J-lp-oVM" sceneMemberID="viewController">
                  <layoutGuides>
                    <viewControllerLayoutGuide type="top" id="rUq-ht-380"/>
                    <viewControllerLayoutGuide type="bottom" id="a9l-8d-mfx"/>
                  </layoutGuides>
                  <view key="view" contentMode="scaleToFill" id="Ze5-6b-2t3">
                    <rect key="frame" x="0.0" y="0.0" width="375" height="667"/>
                    <autoresizingMask key="autoresizingMask" widthSizable="YES" heightSizable="YES"/>
                    <color key="backgroundColor" red="1" green="1" blue="1" alpha="1" colorSpace="custom" customColorSpace="sRGB"/>
                  </view>
                </viewController>
                <placeholder placeholderIdentifier="IBFirstResponder" id="iYj-Kq-Ea1" userLabel="First Responder" sceneMemberID="firstResponder"/>
              </objects>
              <point key="canvasLocation" x="53" y="375"/>
            </scene>
          </scenes>
        </document>
XML
```

        LAUNCHSCREEN_STORYBOARD_CONTENTS =
          
        
        

```
<<-XML.strip_heredoc.freeze
        <?xml version="1.0" encoding="UTF-8" standalone="no"?>
        <document type="com.apple.InterfaceBuilder3.CocoaTouch.Storyboard.XIB" version="3.0" toolsVersion="13122.16" systemVersion="17A277" targetRuntime="iOS.CocoaTouch" propertyAccessControl="none" useAutolayout="YES" launchScreen="YES" useTraitCollections="YES" useSafeAreas="YES" colorMatched="YES" initialViewController="01J-lp-oVM">
          <dependencies>
            <plugIn identifier="com.apple.InterfaceBuilder.IBCocoaTouchPlugin" version="13104.12"/>
            <capability name="Safe area layout guides" minToolsVersion="9.0"/>
            <capability name="documents saved in the Xcode 8 format" minToolsVersion="8.0"/>
          </dependencies>
          <scenes>
            <!--View Controller-->
            <scene sceneID="EHf-IW-A2E">
              <objects>
                <viewController id="01J-lp-oVM" sceneMemberID="viewController">
                  <view key="view" contentMode="scaleToFill" id="Ze5-6b-2t3">
                    <rect key="frame" x="0.0" y="0.0" width="375" height="667"/>
                    <autoresizingMask key="autoresizingMask" widthSizable="YES" heightSizable="YES"/>
                    <color key="backgroundColor" red="1" green="1" blue="1" alpha="1" colorSpace="custom" customColorSpace="sRGB"/>
                    <viewLayoutGuide key="safeArea" id="6Tk-OE-BBY"/>
                  </view>
                </viewController>
                <placeholder placeholderIdentifier="IBFirstResponder" id="iYj-Kq-Ea1" userLabel="First Responder" sceneMemberID="firstResponder"/>
              </objects>
              <point key="canvasLocation" x="53" y="375"/>
            </scene>
          </scenes>
        </document>
XML
```

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**add_app_host_main_file**(project, target, platform, group, name = 'App')  ⇒ Array<PBXBuildFile> 
    

    
  
  
  
  
  
  
  
  

  
    

Creates and links a default app host ‘main.m’ file.

-
  
      .**add_app_project_import**(project, target, pod_target, platform, name = 'App')  ⇒ Array<PBXBuildFile> 

Creates and links an import file for the given pod target and into the given native target.

-
  
      .**add_app_target**(project, platform_name, deployment_target, name = 'App', product_basename = nil)  ⇒ PBXNativeTarget 

Adds a single app target to the given project with the provided name.

-
  
      .**add_empty_swift_file**(project, target, name = 'App')  ⇒ Array<PBXBuildFile> 

Creates and links an empty Swift file for the given target.

-
  
      .**add_launchscreen_storyboard**(project, target, group, deployment_target, name = 'App')  ⇒ PBXFileReference 

Creates a default launchscreen storyboard.

-
  
      .**add_swift_version**(target, swift_version)  ⇒ void 

Adds the provided swift version into the given target.

-
  
      .**add_xctest_search_paths**(target)  ⇒ void 

Adds the xctest framework search paths into the given target.

-
  
      .**create_app_host_main_file**(project, platform, name = 'App')  ⇒ Pathname 

Creates a default app host ‘main.m’ file.

-
  
      .**create_app_import_source_file**(project, pod_target, platform, name = 'App')  ⇒ Pathname 

Creates a default import file for the given pod target.

-
  
      .**create_launchscreen_storyboard_file**(project, deployment_target, name = 'App')  ⇒ Pathname 

Creates a default launchscreen storyboard file.

## Class Method Details

###
  
    .**add_app_host_main_file**(project, target, platform, group, name = 'App')  ⇒ Array<PBXBuildFile> 
  

  

  

  
    

Creates and links a default app host ‘main.m’ file.

Parameters:

-

        project

        (Project)
      
      
      
        —
        

the Xcodeproj to generate the main file into.

-

        target

        (PBXNativeTarget)
      
      
      
        —
        

the native target to link the generated main file into.

-

        platform

        (Symbol)
      
      
      
        —
        

the platform of the target. Can be `:ios` or `:osx`, etc.

-

        name

        (String)
      
      
        *(defaults to: 'App')*
      
      
        —
        

The name to use for the target, defaults to ‘App’.

Returns:

-

        (Array<PBXBuildFile>)

        —
        

the created build file references.

```

95
96
97
98
99
```

```
# File 'lib/cocoapods/generator/app_target_helper.rb', line 95

def self.add_app_host_main_file(project, target, platform, group, name = 'App')
  source_file = AppTargetHelper.create_app_host_main_file(project, platform, name)
  source_file_ref = group.new_file(source_file)
  target.add_file_references([source_file_ref])
end
```

###
  
    .**add_app_project_import**(project, target, pod_target, platform, name = 'App')  ⇒ Array<PBXBuildFile> 
  

  

  

  
    

Creates and links an import file for the given pod target and into the given native target.

Parameters:

-

        project

        (Project)
      
      
      
        —
        

the Xcodeproj to generate the target into.

-

        target

        (PBXNativeTarget)
      
      
      
        —
        

the native target to link the generated import file into.

-

        pod_target

        (PodTarget)
      
      
      
        —
        

the pod target to use for when generating the contents of the import file.

-

        platform

        (Symbol)
      
      
      
        —
        

the platform of the target. Can be `:ios` or `:osx`, etc.

-

        name

        (String)
      
      
        *(defaults to: 'App')*
      
      
        —
        

The name to use for the target, defaults to ‘App’.

Returns:

-

        (Array<PBXBuildFile>)

        —
        

the created build file references.

```

50
51
52
53
54
55
```

```
# File 'lib/cocoapods/generator/app_target_helper.rb', line 50

def self.add_app_project_import(project, target, pod_target, platform, name = 'App')
  source_file = AppTargetHelper.create_app_import_source_file(project, pod_target, platform, name)
  group = project[name] || project.new_group(name, name)
  source_file_ref = group.new_file(source_file)
  target.add_file_references([source_file_ref])
end
```

###
  
    .**add_app_target**(project, platform_name, deployment_target, name = 'App', product_basename = nil)  ⇒ PBXNativeTarget 
  

  

  

  
    

Adds a single app target to the given project with the provided name.

Parameters:

-

        project

        (Project)
      
      
      
        —
        

the Xcodeproj to generate the target into.

-

        platform_name

        (Symbol)
      
      
      
        —
        

the platform of the target. Can be `:ios` or `:osx`, etc.

-

        deployment_target

        (String)
      
      
      
        —
        

the deployment target for the platform.

-

        name

        (String)
      
      
        *(defaults to: 'App')*
      
      
        —
        

The name to use for the target, defaults to ‘App’.

-

        product_basename

        (String)
      
      
        *(defaults to: nil)*
      
      
        —
        

The product basename to use for the target, defaults to `name`.

Returns:

-

        (PBXNativeTarget)

        —
        

the new target that was created.

```

26
27
28
29
```

```
# File 'lib/cocoapods/generator/app_target_helper.rb', line 26

def self.add_app_target(project, platform_name, deployment_target, name = 'App', product_basename = nil)
  project.new_target(:application, name, platform_name, deployment_target, nil,
                     nil, product_basename)
end
```

###
  
    .**add_empty_swift_file**(project, target, name = 'App')  ⇒ Array<PBXBuildFile> 
  

  

  

  
    

Creates and links an empty Swift file for the given target.

Parameters:

-

        project

        (Project)
      
      
      
        —
        

the Xcodeproj to generate the target into.

-

        target

        (PBXNativeTarget)
      
      
      
        —
        

the native target to link the generated import file into.

-

        name

        (String)
      
      
        *(defaults to: 'App')*
      
      
        —
        

The name to use for the target, defaults to ‘App’.

Returns:

-

        (Array<PBXBuildFile>)

        —
        

the created build file references.

```

70
71
72
73
74
75
76
77
```

```
# File 'lib/cocoapods/generator/app_target_helper.rb', line 70

def self.add_empty_swift_file(project, target, name = 'App')
  swift_file = project.path.dirname.+("#{name}/dummy.swift")
  swift_file.parent.mkpath
  File.write(swift_file, '')
  group = project[name] || project.new_group(name, name)
  swift_file_ref = group.new_file(swift_file)
  target.add_file_references([swift_file_ref])
end
```

###
  
    .**add_launchscreen_storyboard**(project, target, group, deployment_target, name = 'App')  ⇒ PBXFileReference 
  

  

  

  
    

Creates a default launchscreen storyboard.

Parameters:

-

        project

        (Project)
      
      
      
        —
        

the Xcodeproj to generate the launchscreen storyboard into.

-

        target

        (PBXNativeTarget)
      
      
      
        —
        

the native target to link the generated launchscreen storyboard into.

-

        platform

        (Symbol)
      
      
      
        —
        

the platform of the target. Can be `:ios` or `:osx`, etc.

-

        deployment_target

        (String)
      
      
      
        —
        

the deployment target for the platform.

-

        name

        (String)
      
      
        *(defaults to: 'App')*
      
      
        —
        

The name to use for the target, defaults to ‘App’.

Returns:

-

        (PBXFileReference)

        —
        

the created file reference of the launchscreen storyboard.

```

120
121
122
123
124
```

```
# File 'lib/cocoapods/generator/app_target_helper.rb', line 120

def self.add_launchscreen_storyboard(project, target, group, deployment_target, name = 'App')
  launch_storyboard_file = AppTargetHelper.create_launchscreen_storyboard_file(project, deployment_target, name)
  launch_storyboard_ref = group.new_file(launch_storyboard_file)
  target.resources_build_phase.add_file_reference(launch_storyboard_ref)
end
```

###
  
    .**add_swift_version**(target, swift_version)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Adds the provided swift version into the given target.

Parameters:

-

        target

        (PBXNativeTarget)
      
      
      
        —
        

the native target to add the swift version into.

-

        swift_version

        (String)
      
      
      
        —
        

the swift version to set to.

```

158
159
160
161
162
163
```

```
# File 'lib/cocoapods/generator/app_target_helper.rb', line 158

def self.add_swift_version(target, swift_version)
  raise 'Cannot set empty Swift version to target.' if swift_version.blank?
  target.build_configurations.each do |configuration|
    configuration.build_settings['SWIFT_VERSION'] = swift_version
  end
end
```

###
  
    .**add_xctest_search_paths**(target)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Adds the xctest framework search paths into the given target.

Parameters:

-

        target

        (PBXNativeTarget)
      
      
      
        —
        

the native target to add XCTest into.

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
146
```

```
# File 'lib/cocoapods/generator/app_target_helper.rb', line 133

def self.add_xctest_search_paths(target)
  requires_libs = target.platform_name == :ios &&
    Version.new(target.deployment_target) < Version.new('12.2')

  target.build_configurations.each do |configuration|
    framework_search_paths = configuration.build_settings['FRAMEWORK_SEARCH_PATHS'] ||= '$(inherited)'
    framework_search_paths << ' "$(PLATFORM_DIR)/Developer/Library/Frameworks"'

    if requires_libs
      library_search_paths = configuration.build_settings['LIBRARY_SEARCH_PATHS'] ||= '$(inherited)'
      library_search_paths << ' "$(PLATFORM_DIR)/Developer/usr/lib"'
    end
  end
end
```

###
  
    .**create_app_host_main_file**(project, platform, name = 'App')  ⇒ Pathname 
  

  

  

  
    

Creates a default app host ‘main.m’ file.

Parameters:

-

        project

        (Project)
      
      
      
        —
        

the Xcodeproj to generate the target into.

-

        platform

        (Symbol)
      
      
      
        —
        

the platform of the target. Can be `:ios` or `:osx`.

-

        name

        (String)
      
      
        *(defaults to: 'App')*
      
      
        —
        

The name of the folder to use and save the generated main file.

Returns:

-

        (Pathname)

        —
        

the new source file that was generated.

```

249
250
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
```

```
# File 'lib/cocoapods/generator/app_target_helper.rb', line 249

def self.create_app_host_main_file(project, platform, name = 'App')
  source_file = project.path.dirname.+("#{name}/main.m")
  source_file.parent.mkpath
  source_file.open('w') do |f|
    case platform
    when :ios, :tvos
      f << IOS_APP_HOST_MAIN_CONTENTS
    when :osx
      f << MACOS_APP_HOST_MAIN_CONTENTS
    end
  end
  source_file
end
```

###
  
    .**create_app_import_source_file**(project, pod_target, platform, name = 'App')  ⇒ Pathname 
  

  

  

  
    

Creates a default import file for the given pod target.

Parameters:

-

        project

        (Project)
      
      
      
        —
        

the Xcodeproj to generate the target into.

-

        pod_target

        (PodTarget)
      
      
      
        —
        

the pod target to use for when generating the contents of the import file.

-

        platform

        (Symbol)
      
      
      
        —
        

the platform of the target. Can be `:ios` or `:osx`, etc.

-

        name

        (String)
      
      
        *(defaults to: 'App')*
      
      
        —
        

The name of the folder to use and save the generated main file.

Returns:

-

        (Pathname)

        —
        

the new source file that was generated.

```

181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
```

```
# File 'lib/cocoapods/generator/app_target_helper.rb', line 181

def self.create_app_import_source_file(project, pod_target, platform, name = 'App')
  language = pod_target.uses_swift? ? :swift : :objc

  if language == :swift
    source_file = project.path.dirname.+("#{name}/main.swift")
    source_file.parent.mkpath
    import_statement = pod_target.should_build? && pod_target.defines_module? ? "import #{pod_target.product_module_name}\n" : ''
    source_file.open('w') { |f| f << import_statement }
  else
    source_file = project.path.dirname.+("#{name}/main.m")
    source_file.parent.mkpath
    import_statement = if pod_target.should_build? && pod_target.defines_module?
                         "@import #{pod_target.product_module_name};\n"
                       else
                         header_name = "#{pod_target.product_module_name}/#{pod_target.product_module_name}.h"
                         if pod_target.sandbox.public_headers.root.+(header_name).file?
                           "#import <#{header_name}>\n"
                         else
                           ''
                         end
                       end
    source_file.open('w') do |f|
      f << "@import Foundation;\n"
      f << "@import UIKit;\n" if platform == :ios || platform == :tvos
      f << "@import Cocoa;\n" if platform == :osx
      f << "#{import_statement}int main(void) {}\n"
    end
  end
  source_file
end
```

###
  
    .**create_launchscreen_storyboard_file**(project, deployment_target, name = 'App')  ⇒ Pathname 
  

  

  

  
    

Creates a default launchscreen storyboard file.

Parameters:

-

        project

        (Project)
      
      
      
        —
        

the Xcodeproj to generate the launchscreen storyboard into.

-

        deployment_target

        (String)
      
      
      
        —
        

the deployment target for the platform.

-

        name

        (String)
      
      
        *(defaults to: 'App')*
      
      
        —
        

The name of the folder to use and save the generated launchscreen storyboard file.

Returns:

-

        (Pathname)

        —
        

the new launchscreen storyboard file that was generated.

```

225
226
227
228
229
230
231
232
233
234
```

```
# File 'lib/cocoapods/generator/app_target_helper.rb', line 225

def self.create_launchscreen_storyboard_file(project, deployment_target, name = 'App')
  launch_storyboard_file = project.path.dirname.+("#{name}/LaunchScreen.storyboard")
  launch_storyboard_file.parent.mkpath
  if Version.new(deployment_target) >= Version.new('9.0')
    File.write(launch_storyboard_file, LAUNCHSCREEN_STORYBOARD_CONTENTS)
  else
    File.write(launch_storyboard_file, LAUNCHSCREEN_STORYBOARD_CONTENTS_IOS_8)
  end
  launch_storyboard_file
end
```
