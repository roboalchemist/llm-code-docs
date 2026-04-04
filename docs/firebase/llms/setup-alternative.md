# Source: https://firebase.google.com/docs/unity/setup-alternative.md.txt

<br />

Rather than downloading a large`.zip`file containing all`.unitypackage`files for both .NET 3.X and .NET 4.X, you can download individual packages from the[Google APIs for Unity site](https://developers.google.com/unity/packages).

The site provides:

- Individual .NET 4.X`.unitypackage`files to import as Asset packages.
- Individual`.tgz`archives to import using Unity Package Manager.

This is especially useful when your app uses a single Firebase product, since the individual`.unitypackage`files contain all needed dependencies, and the`.tgz`files are listed alongside related`.tgz`files on which they depend.

This page provides instructions involving Unity Package Manager, so it's a good idea to learn about the tool[from the Unity documentation](https://docs.unity3d.com/Manual/Packages.html).
| **Note:** If you still need to use .NET 3.x, download the entire Firebase SDK as described in[Add Firebase to your Unity project](https://firebase.google.com/docs/unity/setup#add-sdks).

## Import Firebase packages as Assets

When importing Firebase products from`.unitypackage`files downloaded from[Google APIs for Unity site](https://developers.google.com/unity/packages), keep the following in mind:

- If you are using multiple Firebase products in your project, you must download and upgrade all Firebase products to the same version.

- Do not mix import methods in one project. That is, do not import Firebase products with the Asset package flow and using the Unity Package Manager flow.

After downloading, to import:

1. In your open Unity project, navigate to**Assets** \>**Import Package** \>**Custom Package**.

2. In the*Import Unity Package* window, click**Import**.

## Import Firebase packages using Unity Package Manager

When importing Firebase products from`.tgz`files downloaded from the[Google APIs for Unity archive](https://developers.google.com/unity/archive), keep the following in mind:

- This method is only available in 2018.3+.

- If you are using multiple Firebase products in your project, you must download and upgrade all Firebase products to the same version.

- Do not mix import methods in one project. That is, do not import Firebase products with the Asset package flow and with the Unity Package Manager flow.

- Dependencies for each product`.tgz`file are linked alongside in their own`.tgz`files. You must download and import the product`.tgz`file and dependency`.tgz`files, in the correct order:

  1. External Dependency Manager (`com.google.external-dependency-manager`)
  2. Firebase Core (`com.google.firebase.app`)
  3. Firebase products used in your project. If you useRealtime DatabaseorCloud Storage, importAuthentication(`com.google.firebase.auth`) first.

After downloading, import`.tgz`files into your project using one of the following methods:  

### Package Manager UI

1. Open Unity's Package Manager window.
2. Click the`+`icon in the top-left corner of the Package Manager window and select`Add package from tarball`to open the file browser.
3. Select the desired tarball in the file browser.

Some older versions of Unity 2019 do not support adding tarballs directly. In this case, you will need to:

1. Unzip the`.tgz`file.
2. Click the`+`icon in the top-left corner of the Package Manager window and select`Add package from disk`to open the file browser.
3. Select the extracted folder in the file browser.

### manifest.json

1. Create a new folder next to your project's`Packages`folder and name it`GooglePackages`.
2. Place the`.tgz`files into that folder.
3. Use a text editor to open`Packages/manifest.json`under your Unity project folder.
4. Add an entry for each package you want to import, mapping the package name to the location on disk. Be sure to append`file:`to the`.tgz`file path. For example, if you were importing`com.google.firebase.storage`and its dependency's, your`manifest.json`would look like this:

       {
         "dependencies": {
           "com.google.external-dependency-manager": "file:../GooglePackages/com.google.external-dependency-manager-1.2.164.tgz",
           "com.google.firebase.app": "file:../GooglePackages/com.google.firebase.app-7.1.0.tgz",
           "com.google.firebase.auth": "file:../GooglePackages/com.google.firebase.auth-7.1.0.tgz",
           "com.google.firebase.storage": "file:../GooglePackages/com.google.firebase.storage-7.1.0.tgz",
           // com.unity package entries...
         }
       }

5. Save the`manifest.json`file.

6. When Unity regains focus it will reload the`manifest.json`and import the newly-added packages.

Some older versions of Unity do not support`.tgz`files in the`manifest.json`. In this case, you should:

1. Unzip the`.tgz`file.
2. Edit your`manifest.json`to use the path to the extracted folder, instead of the`.tgz`file, like so:

       {
         "dependencies": {
           "com.google.external-dependency-manager": "file:../GooglePackages/com.google.external-dependency-manager-1.2.164",
           "com.google.firebase.app": "file:../GooglePackages/com.google.firebase.app-7.1.0",
           "com.google.firebase.auth": "file:../GooglePackages/com.google.firebase.auth-7.1.0",
           "com.google.firebase.storage": "file:../GooglePackages/com.google.firebase.storage-7.1.0",
           // com.unity package entries...
         }
       }

## Migrate from Unity Package Manager to Asset packages

In some cases, you might want to switch from using Unity Package Manager to track Firebase products, to importing products under the`Assets`folder.

If you're not sure which import method you're using, in your Unity project folder, open the file`Packages/manifest.json`. If the file contains entries starting with`com.google.firebase`, your project used Unity Package Manager for import.

To migrate to Asset packages:

1. Note current Firebase package versions in your project and remove them.

   1. From the**Window** menu, select**Package Manager** . In the*Package Manager*window, make sure "Packages: In Project" is selected.
   2. Note the versions of imported Firebase packages.
   3. Click on each package name, then click**Remove** . Be sure to remove the External Dependency Manager package (`.com.google.external-dependency-manager`) as well as Firebase packages.
2. Download and import replacement`.unitypackage`files. You have two options:

   - If you can upgrade to the latest version of each package, download the Firebase Unity SDK zip file and import as described in[Add Firebase to your Unity project](https://firebase.google.com/docs/unity/setup#add-sdks).
   - If you need to preserve current`.unitypackage`versions, you can download and import individual packages as described[above](https://firebase.google.com/docs/unity/setup-alternative#alternative_individual_unitypackages)on this page.

## Migrate from Asset packages to Unity Package Manager

In some cases, you might want to switch from importing products under the`Assets`folder to importing and tracking products with Unity Package Manager.

If you're not sure which import method you're using, in your Unity project folder, open the file`Packages/manifest.json`. If the file contains entries starting with`com.google.firebase`your project is already using Unity Package Manager for import.

To migrate to Unity Package Manager:

1. Make sure all Firebase packages and the External Dependency Manager package are removed from the`Assets`folder, using either of the following methods.

   ### EDM4U UI

   <br />

   1. In your open Unity project, navigate to**Assets \> External Dependency Manager \> Version Handler \> Uninstall Managed Packages**.
   2. Select all Firebase packages and External Dependency Manager.
   3. Click**Uninstall Selected Package**.

   <br />

   ### Manual removal

   Using file system tools, manually delete the following folders:
   - `Assets/Editor Default Resources/Firebase`
   - `Assets/ExternalDependencyManager`
   - `Assets/Firebase`
   - `Assets/Parse`
   - `Assets/Plugins/iOS/Firebase`
2. Import packages using Unity Package Manager, as described[above](https://firebase.google.com/docs/unity/setup-alternative#alternative_unity_package_manager)on this page.