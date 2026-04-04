# Source: https://docs.syncfusion.com/common/essential-studio/applying-patches/applying-patches.md

# Source: https://docs.syncfusion.com/uwp/applying-patches/applying-patches.md

# Source: https://docs.syncfusion.com/winui/applying-patches/applying-patches.md

# Source: https://docs.syncfusion.com/windowsforms/applying-patches/applying-patches.md

# Source: https://docs.syncfusion.com/wpf/applying-patches/applying-patches.md

# Applying the Patches

Syncfusion provides patch installer for major version or service pack version, either to add new features or to fix issues. You have to install the patches in the order you have received.


## Installing the Patch installer

The steps below show how to install a patch.


I> Before installing the patch, ensure that corresponding Essential Studio version platform has been installed in your machine.



1. Double-click theÂ Syncfusion Essential Studio patch installer. TheÂ Syncfusion Essential Studio Service PackÂ opens.
   
   ![Welcome Wizard](Patches_images/Installing-a-Patch-Setup_img2.png)




2. ClickÂ Next. TheÂ Assembly ManagerÂ screen opens.
   
   ![Assembly Manager](Patches_images/Installing-a-Patch-Setup_img3.png)




3. Select theÂ Run Assembly ManagerÂ check box to install the assemblies in GAC.

4. ClickÂ Next.Â The Ready To InstallÂ screen opens.
   
   ![Ready To Install](Patches_images/Installing-a-Patch-Setup_img4.png)




5. ClickÂ InstallÂ to continue installing.
   
   ![Installation Progress](Patches_images/Installing-a-Patch-Setup_img5.png)

   N> The patch is installed on your computer, and a dialog box appears when the installation is complete.



    ![Finish Wizard](Patches_images/Installing-a-Patch-Setup_img7.png)


6. ClickÂ Finish. The new assemblies are placed in theÂ Pre-Compiled AssembliesÂ folder. These new assemblies can be referenced in your project.


## Patch Assembly Version Format
   
In the patch assembly, the **File Version** and **Product Version** will be different. Product Version will be the release version and File Version will be the increment of the release version's **revision** number. For each patch, the File Version will be a different one. You can differentiate between the build and patch assemblies by File Version. 
   
**File Version of the assembly shipped in build:**
   
![Patch Assembly](Patches_images/Installing-a-Patch-Setup_img8.png)
   
**Product Version of the assembly shipped in patch:**
   
![Patch Assembly](Patches_images/Installing-a-Patch-Setup_img9.png)



