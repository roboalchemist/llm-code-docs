# DirAccess

# DirAccess

Inherits:RefCounted<Object
Provides methods for managing directories and their content.

## Description

This class is used to manage directories and their content, even outside of the project folder.
DirAccesscan't be instantiated directly. Instead it is created with a static method that takes a path for which it will be opened.
Most of the methods have a static alternative that can be used without creating aDirAccess. Static methods only support absolute paths (includingres://anduser://).

```
# Standard
var dir = DirAccess.open("user://levels")
dir.make_dir("world1")
# Static
DirAccess.make_dir_absolute("user://levels/world1")
```

Note:Accessing project ("res://") directories once exported may behave unexpectedly as some files are converted to engine-specific formats and their original source files may not be present in the expected PCK package. Because of this, to access resources in an exported project, it is recommended to useResourceLoaderinstead ofFileAccess.
Here is an example on how to iterate through the files of a directory:

```
func dir_contents(path):
    var dir = DirAccess.open(path)
    if dir:
        dir.list_dir_begin()
        var file_name = dir.get_next()
        while file_name != "":
            if dir.current_is_dir():
                print("Found directory: " + file_name)
            else:
                print("Found file: " + file_name)
            file_name = dir.get_next()
    else:
        print("An error occurred when trying to access the path.")
```

```
public void DirContents(string path)
{
    using var dir = DirAccess.Open(path);
    if (dir != null)
    {
        dir.ListDirBegin();
        string fileName = dir.GetNext();
        while (fileName != "")
        {
            if (dir.CurrentIsDir())
            {
                GD.Print($"Found directory: {fileName}");
            }
            else
            {
                GD.Print($"Found file: {fileName}");
            }
            fileName = dir.GetNext();
        }
    }
    else
    {
        GD.Print("An error occurred when trying to access the path.");
    }
}
```

Keep in mind that file names may change or be remapped after export. If you want to see the actual resource file list as it appears in the editor, useResourceLoader.list_directory()instead.

## Tutorials

- File system
File system

## Properties

| bool | include_hidden |
|---|---|
| bool | include_navigational |

bool
include_hidden
bool
include_navigational

## Methods

| Error | change_dir(to_dir:String) |
|---|---|
| Error | copy(from:String, to:String, chmod_flags:int= -1) |
| Error | copy_absolute(from:String, to:String, chmod_flags:int= -1)static |
| Error | create_link(source:String, target:String) |
| DirAccess | create_temp(prefix:String= "", keep:bool= false)static |
| bool | current_is_dir()const |
| bool | dir_exists(path:String) |
| bool | dir_exists_absolute(path:String)static |
| bool | file_exists(path:String) |
| String | get_current_dir(include_drive:bool= true)const |
| int | get_current_drive() |
| PackedStringArray | get_directories() |
| PackedStringArray | get_directories_at(path:String)static |
| int | get_drive_count()static |
| String | get_drive_name(idx:int)static |
| PackedStringArray | get_files() |
| PackedStringArray | get_files_at(path:String)static |
| String | get_filesystem_type()const |
| String | get_next() |
| Error | get_open_error()static |
| int | get_space_left() |
| bool | is_bundle(path:String)const |
| bool | is_case_sensitive(path:String)const |
| bool | is_equivalent(path_a:String, path_b:String)const |
| bool | is_link(path:String) |
| Error | list_dir_begin() |
| void | list_dir_end() |
| Error | make_dir(path:String) |
| Error | make_dir_absolute(path:String)static |
| Error | make_dir_recursive(path:String) |
| Error | make_dir_recursive_absolute(path:String)static |
| DirAccess | open(path:String)static |
| String | read_link(path:String) |
| Error | remove(path:String) |
| Error | remove_absolute(path:String)static |
| Error | rename(from:String, to:String) |
| Error | rename_absolute(from:String, to:String)static |

Error
change_dir(to_dir:String)
Error
copy(from:String, to:String, chmod_flags:int= -1)
Error
copy_absolute(from:String, to:String, chmod_flags:int= -1)static
Error
create_link(source:String, target:String)
DirAccess
create_temp(prefix:String= "", keep:bool= false)static
bool
current_is_dir()const
bool
dir_exists(path:String)
bool
dir_exists_absolute(path:String)static
bool
file_exists(path:String)
String
get_current_dir(include_drive:bool= true)const
get_current_drive()
PackedStringArray
get_directories()
PackedStringArray
get_directories_at(path:String)static
get_drive_count()static
String
get_drive_name(idx:int)static
PackedStringArray
get_files()
PackedStringArray
get_files_at(path:String)static
String
get_filesystem_type()const
String
get_next()
Error
get_open_error()static
get_space_left()
bool
is_bundle(path:String)const
bool
is_case_sensitive(path:String)const
bool
is_equivalent(path_a:String, path_b:String)const
bool
is_link(path:String)
Error
list_dir_begin()
void
list_dir_end()
Error
make_dir(path:String)
Error
make_dir_absolute(path:String)static
Error
make_dir_recursive(path:String)
Error
make_dir_recursive_absolute(path:String)static
DirAccess
open(path:String)static
String
read_link(path:String)
Error
remove(path:String)
Error
remove_absolute(path:String)static
Error
rename(from:String, to:String)
Error
rename_absolute(from:String, to:String)static

## Property Descriptions

boolinclude_hidden🔗

- voidset_include_hidden(value:bool)
voidset_include_hidden(value:bool)
- boolget_include_hidden()
boolget_include_hidden()
Iftrue, hidden files are included when navigating the directory.
Affectslist_dir_begin(),get_directories()andget_files().
boolinclude_navigational🔗
- voidset_include_navigational(value:bool)
voidset_include_navigational(value:bool)
- boolget_include_navigational()
boolget_include_navigational()
Iftrue,.and..are included when navigating the directory.
Affectslist_dir_begin()andget_directories().

## Method Descriptions

Errorchange_dir(to_dir:String)🔗
Changes the currently opened directory to the one passed as an argument. The argument can be relative to the current directory (e.g.newdiror../newdir), or an absolute path (e.g./tmp/newdirorres://somedir/newdir).
Returns one of theErrorcode constants (@GlobalScope.OKon success).
Note:The new directory must be within the same scope, e.g. when you had opened a directory insideres://, you can't change it touser://directory. If you need to open a directory in another access scope, useopen()to create a new instance instead.
Errorcopy(from:String, to:String, chmod_flags:int= -1)🔗
Copies thefromfile to thetodestination. Both arguments should be paths to files, either relative or absolute. If the destination file exists and is not access-protected, it will be overwritten.
Ifchmod_flagsis different than-1, the Unix permissions for the destination path will be set to the provided value, if available on the current operating system.
Returns one of theErrorcode constants (@GlobalScope.OKon success).
Errorcopy_absolute(from:String, to:String, chmod_flags:int= -1)static🔗
Static version ofcopy(). Supports only absolute paths.
Errorcreate_link(source:String, target:String)🔗
Creates symbolic link between files or folders.
Note:On Windows, this method works only if the application is running with elevated privileges or Developer Mode is enabled.
Note:This method is implemented on macOS, Linux, and Windows.
DirAccesscreate_temp(prefix:String= "", keep:bool= false)static🔗
Creates a temporary directory. This directory will be freed when the returnedDirAccessis freed.
Ifprefixis not empty, it will be prefixed to the directory name, separated by a-.
Ifkeepistrue, the directory is not deleted when the returnedDirAccessis freed.
Returnsnullif opening the directory failed. You can useget_open_error()to check the error that occurred.
boolcurrent_is_dir()const🔗
Returns whether the current item processed with the lastget_next()call is a directory (.and..are considered directories).
booldir_exists(path:String)🔗
Returns whether the target directory exists. The argument can be relative to the current directory, or an absolute path.
Note:The returnedboolin the editor and after exporting when used on a path in theres://directory may be different. Some files are converted to engine-specific formats when exported, potentially changing the directory structure.
booldir_exists_absolute(path:String)static🔗
Static version ofdir_exists(). Supports only absolute paths.
Note:The returnedboolin the editor and after exporting when used on a path in theres://directory may be different. Some files are converted to engine-specific formats when exported, potentially changing the directory structure.
boolfile_exists(path:String)🔗
Returns whether the target file exists. The argument can be relative to the current directory, or an absolute path.
For a static equivalent, useFileAccess.file_exists().
Note:Many resources types are imported (e.g. textures or sound files), and their source asset will not be included in the exported game, as only the imported version is used. SeeResourceLoader.exists()for an alternative approach that takes resource remapping into account.
Stringget_current_dir(include_drive:bool= true)const🔗
Returns the absolute path to the currently opened directory (e.g.res://folderorC:\tmp\folder).
intget_current_drive()🔗
Returns the currently opened directory's drive index. Seeget_drive_name()to convert returned index to the name of the drive.
PackedStringArrayget_directories()🔗
Returns aPackedStringArraycontaining filenames of the directory contents, excluding files. The array is sorted alphabetically.
Affected byinclude_hiddenandinclude_navigational.
Note:The returned directories in the editor and after exporting in theres://directory may differ as some files are converted to engine-specific formats when exported.
PackedStringArrayget_directories_at(path:String)static🔗
Returns aPackedStringArraycontaining filenames of the directory contents, excluding files, at the givenpath. The array is sorted alphabetically.
Useget_directories()if you want more control of what gets included.
Note:The returned directories in the editor and after exporting in theres://directory may differ as some files are converted to engine-specific formats when exported.
intget_drive_count()static🔗
On Windows, returns the number of drives (partitions) mounted on the current filesystem.
On macOS and Android, returns the number of mounted volumes.
On Linux, returns the number of mounted volumes and GTK 3 bookmarks.
On other platforms, the method returns 0.
Stringget_drive_name(idx:int)static🔗
On Windows, returns the name of the drive (partition) passed as an argument (e.g.C:).
On macOS, returns the path to the mounted volume passed as an argument.
On Linux, returns the path to the mounted volume or GTK 3 bookmark passed as an argument.
On Android (API level 30+), returns the path to the mounted volume as an argument.
On other platforms, or if the requested drive does not exist, the method returns an empty String.
PackedStringArrayget_files()🔗
Returns aPackedStringArraycontaining filenames of the directory contents, excluding directories. The array is sorted alphabetically.
Affected byinclude_hidden.
Note:When used on ares://path in an exported project, only the files actually included in the PCK at the given folder level are returned. In practice, this means that since imported resources are stored in a top-level.godot/folder, only paths to*.gdand*.importfiles are returned (plus a few files such asproject.godotorproject.binaryand the project icon). In an exported project, the list of returned files will also vary depending on whetherProjectSettings.editor/export/convert_text_resources_to_binaryistrue.
PackedStringArrayget_files_at(path:String)static🔗
Returns aPackedStringArraycontaining filenames of the directory contents, excluding directories, at the givenpath. The array is sorted alphabetically.
Useget_files()if you want more control of what gets included.
Note:When used on ares://path in an exported project, only the files included in the PCK at the given folder level are returned. In practice, this means that since imported resources are stored in a top-level.godot/folder, only paths to.gdand.importfiles are returned (plus a few other files, such asproject.godotorproject.binaryand the project icon). In an exported project, the list of returned files will also vary depending onProjectSettings.editor/export/convert_text_resources_to_binary.
Stringget_filesystem_type()const🔗
Returns file system type name of the current directory's disk. Returned values are uppercase strings likeNTFS,FAT32,EXFAT,APFS,EXT4,BTRFS, and so on.
Note:This method is implemented on macOS, Linux, Windows and for PCK virtual file system.
Stringget_next()🔗
Returns the next element (file or directory) in the current directory.
The name of the file or directory is returned (and not its full path). Once the stream has been fully processed, the method returns an emptyStringand closes the stream automatically (i.e.list_dir_end()would not be mandatory in such a case).
Errorget_open_error()static🔗
Returns the result of the lastopen()call in the current thread.
intget_space_left()🔗
Returns the available space on the current directory's disk, in bytes. Returns0if the platform-specific method to query the available space fails.
boolis_bundle(path:String)const🔗
Returnstrueif the directory is a macOS bundle.
Note:This method is implemented on macOS.
boolis_case_sensitive(path:String)const🔗
Returnstrueif the file system or directory use case sensitive file names.
Note:This method is implemented on macOS, Linux (for EXT4 and F2FS filesystems only) and Windows. On other platforms, it always returnstrue.
boolis_equivalent(path_a:String, path_b:String)const🔗
Returnstrueif pathspath_aandpath_bresolve to the same file system object. Returnsfalseotherwise, even if the files are bit-for-bit identical (e.g., identical copies of the file that are not symbolic links).
boolis_link(path:String)🔗
Returnstrueif the file or directory is a symbolic link, directory junction, or other reparse point.
Note:This method is implemented on macOS, Linux, and Windows.
Errorlist_dir_begin()🔗
Initializes the stream used to list all files and directories using theget_next()function, closing the currently opened stream if needed. Once the stream has been processed, it should typically be closed withlist_dir_end().
Affected byinclude_hiddenandinclude_navigational.
Note:The order of files and directories returned by this method is not deterministic, and can vary between operating systems. If you want a list of all files or folders sorted alphabetically, useget_files()orget_directories().
voidlist_dir_end()🔗
Closes the current stream opened withlist_dir_begin()(whether it has been fully processed withget_next()does not matter).
Errormake_dir(path:String)🔗
Creates a directory. The argument can be relative to the current directory, or an absolute path. The target directory should be placed in an already existing directory (to create the full path recursively, seemake_dir_recursive()).
Returns one of theErrorcode constants (@GlobalScope.OKon success).
Errormake_dir_absolute(path:String)static🔗
Static version ofmake_dir(). Supports only absolute paths.
Errormake_dir_recursive(path:String)🔗
Creates a target directory and all necessary intermediate directories in its path, by callingmake_dir()recursively. The argument can be relative to the current directory, or an absolute path.
Returns one of theErrorcode constants (@GlobalScope.OKon success).
Errormake_dir_recursive_absolute(path:String)static🔗
Static version ofmake_dir_recursive(). Supports only absolute paths.
DirAccessopen(path:String)static🔗
Creates a newDirAccessobject and opens an existing directory of the filesystem. Thepathargument can be within the project tree (res://folder), the user directory (user://folder) or an absolute path of the user filesystem (e.g./tmp/folderorC:\tmp\folder).
Returnsnullif opening the directory failed. You can useget_open_error()to check the error that occurred.
Stringread_link(path:String)🔗
Returns target of the symbolic link.
Note:This method is implemented on macOS, Linux, and Windows.
Errorremove(path:String)🔗
Permanently deletes the target file or an empty directory. The argument can be relative to the current directory, or an absolute path. If the target directory is not empty, the operation will fail.
If you don't want to delete the file/directory permanently, useOS.move_to_trash()instead.
Returns one of theErrorcode constants (@GlobalScope.OKon success).
Errorremove_absolute(path:String)static🔗
Static version ofremove(). Supports only absolute paths.
Errorrename(from:String, to:String)🔗
Renames (move) thefromfile or directory to thetodestination. Both arguments should be paths to files or directories, either relative or absolute. If the destination file or directory exists and is not access-protected, it will be overwritten.
Returns one of theErrorcode constants (@GlobalScope.OKon success).
Errorrename_absolute(from:String, to:String)static🔗
Static version ofrename(). Supports only absolute paths.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
