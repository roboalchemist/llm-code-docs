# Source: https://firebase.google.com/docs/crashlytics/get-deobfuscated-reports.md.txt

<br />

iOS+AndroidFlutterUnity  

<br />

By default,Firebase Crashlyticsautomatically processes your debug symbol (dSYM) files to give you deobfuscated and human-readable crash reports. You usually configure this behavior during the initial setup ofCrashlyticsin your app, specifically by[adding a run script](https://firebase.google.com/docs/crashlytics/get-started?platform=ios#set-up-dsym-uploading)that automatically uploads dSYM files during your app's build phase.

Unfortunately, there are a few cases that could cause your automatic dSYM files upload to fail. This guide provides some ways to troubleshoot whenCrashlyticscan't locate your app's dSYM files.

## Make sure Xcode can automatically process dSYMs and upload the files

When setting upCrashlyticsin your app, you[configured a run script](https://firebase.google.com/docs/crashlytics/get-started?platform=ios#set-up-dsym-uploading)to automatically process dSYMs and upload the files.

Make sure that your configuration for theCrashlyticsrun script is up-to-date with the new requirements which started with Xcode 15. If your configuration isn't up-to-date, you might be getting the following error:  
`error: Info.plist Error Unable to process Info.plist at path ...`.

Specifically, Xcode 15 and later requires that you provide a more complete set of file locations. For yourCrashlyticsrun script (`firebase-ios-sdk/Crashlytics/run`), make sure that you have the following setup:

1. Click the**Build Phases** tab, and then expand the*Run Script*section.

2. In the*Input Files*section, make sure you have the paths for the locations of the following files:

   ```
   ${DWARF_DSYM_FOLDER_PATH}/${DWARF_DSYM_FILE_NAME}
   ```  

   ```
   ${DWARF_DSYM_FOLDER_PATH}/${DWARF_DSYM_FILE_NAME}/Contents/Resources/DWARF/${PRODUCT_NAME}
   ```  

   ```
   ${DWARF_DSYM_FOLDER_PATH}/${DWARF_DSYM_FILE_NAME}/Contents/Info.plist
   ```  

   ```
   $(TARGET_BUILD_DIR)/$(UNLOCALIZED_RESOURCES_FOLDER_PATH)/GoogleService-Info.plist
   ```  

   ```
   $(TARGET_BUILD_DIR)/$(EXECUTABLE_PATH)
   ```
   If you have`ENABLE_USER_SCRIPT_SANDBOXING=YES`and`ENABLE_DEBUG_DYLIB=YES`in your project build settings, then include the following:  

   ```
   ${DWARF_DSYM_FOLDER_PATH}/${DWARF_DSYM_FILE_NAME}/Contents/Resources/DWARF/${PRODUCT_NAME}.debug.dylib
   ```
   **Understand why the locations of these files are needed**

   Xcode looks in the specified locations for these input files to ensure that the build files are available for the run script. Also, if*User Script Sandboxing* is enabled, Xcode only allows the run script to access files specified in the*Input Files*.
   - Providing the location of your project's dSYM files enablesCrashlyticsto process dSYMs.
   - Providing the location of your app's built`GoogleService-Info.plist`file enablesCrashlyticsto associate the dSYMs with your Firebase app.
   - Providing the location of your app's executable allows the run script to prevent duplicate uploads of the same dSYM. Note that app binaries are*not uploaded*.

## Check if Xcode is producing dSYMs

More often than not, dSYM files go missing because Xcode just isn't producing them. When an upload fails,Crashlyticsdisplays a "Missing dSYM" alert in theFirebaseconsole. If you get this alert, first check that Xcode is producing the correct dSYM for every build:

1. Open your project in Xcode, and then select the project file in the Xcode Navigator.

2. Select your main build target.

3. Open the target's**Build Settings** tab, and then click**All**.

4. Search for`debug information format`.

5. Set**Debug Information Format** to**DWARF with dSYM File**for all your build types.

6. Rebuild your app.

Your crash reports should now appear in the[Crashlyticsdashboard](https://console.firebase.google.com/project/_/crashlytics). If the problem persists or you encounter other errors, try[locating your dSYMs](https://firebase.google.com/docs/crashlytics/get-deobfuscated-reports#locate)and[uploading them toCrashlyticsmanually](https://firebase.google.com/docs/crashlytics/get-deobfuscated-reports#upload-dsyms).

## Locate your dSYMs on a local machine

Run the following command to display all your dSYMs' UUIDs on your machine and search for the missing dSYM:  

```text
mdfind -name .dSYM | while read -r line; do dwarfdump -u "$line"; done
```

Once you find the dSYM,[manually upload it toCrashlytics](https://firebase.google.com/docs/crashlytics/get-deobfuscated-reports#upload-dsyms). If the`mdfind`command doesn't return any results, you can look in the`Products`directory where your`.app`lives (by default, the`Products`directory is located in`Derived Data`). If your app is released to production, you can also look for its dSYM in the`.xcarchive`directory on disk:

1. In Xcode, open the**Organizer**window, and then select your app from the list. Xcode displays a list of archives for your project.

2. Control-click an archive to view it in Finder. Control-click it again, and then click**Show Package Contents**.

3. Within`.xcarchive`is a dSYMs directory that contains dSYMs generated as part of Xcode's archiving process.

## Upload your dSYMs

Crashlyticssupports multiple ways to upload your dSYMs files, either[automatically](https://firebase.google.com/docs/crashlytics/get-deobfuscated-reports#auto-upload-dsyms)or[manually](https://firebase.google.com/docs/crashlytics/get-deobfuscated-reports#manually-upload-dsyms).

### *(Recommended)*Automatically process your dSYMs and upload the files

When you initially set upCrashlytics, you most likely configured this automatic upload behavior for your app. However, if automatic uploads are failing,[check that your configuration is correct](https://firebase.google.com/docs/crashlytics/get-deobfuscated-reports#check-input-files-setup).

### Manually upload your dSYM files

If automatic uploads are failing, you can manually upload your dSYM files using either of the following options.

- **Option 1** : Use the console-based "Drag and Drop" option to upload a zip file containing your dSYM files (go to theFirebaseconsole \>[Crashlytics](https://console.firebase.google.com/project/_/crashlytics)\>*dSYMs*tab).

- **Option 2** : Use the`upload-symbols`script that you can call from anywhere in your build process to manually upload your dSYM files. To run the`upload-symbols`script, use either of the following options:

  - **Option A**: Include the following line in your build process:

    ```gdscript
    find dSYM_DIRECTORY -name "*.dSYM" | xargs -I \{\} $PODS_ROOT/FirebaseCrashlytics/upload-symbols -gsp /PATH/TO/GoogleService-Info.plist -p PLATFORM \{\}
    ```
  - **Option B**: Run the script directly from your terminal:

    ```
    /PATH/TO/PODS/DIRECTORY/FirebaseCrashlytics/upload-symbols -gsp /PATH/TO/GoogleService-Info.plist -p ios /PATH/TO/dSYMs
    ```

  For usage notes and additional instructions about this script, run`upload-symbols`with the`--help`parameter.