:github_url: hide



# EditorVCSInterface

**Inherits:** [Object<class_Object>]

Version Control System (VCS) interface, which reads and writes to the local VCS in use.


## Description

Defines the API that the editor uses to extract information from the underlying VCS. The implementation of this API is included in VCS plugins, which are GDExtension plugins that inherit **EditorVCSInterface** and are attached (on demand) to the singleton instance of **EditorVCSInterface**. Instead of performing the task themselves, all the virtual functions listed below are calling the internally overridden functions in the VCS plugins to provide a plug-n-play experience. A custom VCS plugin is supposed to inherit from **EditorVCSInterface** and override each of these virtual functions.


## Tutorials

- [../tutorials/best_practices/version_control_systems](Version control systems .md)


## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`_checkout_branch<class_EditorVCSInterface_private_method__checkout_branch>`\ (\ branch_name\: :ref:`String<class_String>`\ ) |virtual| |required|                                                                                                                                                                                           |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_commit<class_EditorVCSInterface_private_method__commit>`\ (\ msg\: :ref:`String<class_String>`\ ) |virtual| |required|                                                                                                                                                                                                                     |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_create_branch<class_EditorVCSInterface_private_method__create_branch>`\ (\ branch_name\: :ref:`String<class_String>`\ ) |virtual| |required|                                                                                                                                                                                               |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_create_remote<class_EditorVCSInterface_private_method__create_remote>`\ (\ remote_name\: :ref:`String<class_String>`, remote_url\: :ref:`String<class_String>`\ ) |virtual| |required|                                                                                                                                                     |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_discard_file<class_EditorVCSInterface_private_method__discard_file>`\ (\ file_path\: :ref:`String<class_String>`\ ) |virtual| |required|                                                                                                                                                                                                   |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_fetch<class_EditorVCSInterface_private_method__fetch>`\ (\ remote\: :ref:`String<class_String>`\ ) |virtual| |required|                                                                                                                                                                                                                    |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`String<class_String>`\]         | :ref:`_get_branch_list<class_EditorVCSInterface_private_method__get_branch_list>`\ (\ ) |virtual| |required|                                                                                                                                                                                                                                      |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                      | :ref:`_get_current_branch_name<class_EditorVCSInterface_private_method__get_current_branch_name>`\ (\ ) |virtual| |required|                                                                                                                                                                                                                      |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\] | :ref:`_get_diff<class_EditorVCSInterface_private_method__get_diff>`\ (\ identifier\: :ref:`String<class_String>`, area\: :ref:`int<class_int>`\ ) |virtual| |required|                                                                                                                                                                            |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\] | :ref:`_get_line_diff<class_EditorVCSInterface_private_method__get_line_diff>`\ (\ file_path\: :ref:`String<class_String>`, text\: :ref:`String<class_String>`\ ) |virtual| |required|                                                                                                                                                             |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\] | :ref:`_get_modified_files_data<class_EditorVCSInterface_private_method__get_modified_files_data>`\ (\ ) |virtual| |required|                                                                                                                                                                                                                      |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\] | :ref:`_get_previous_commits<class_EditorVCSInterface_private_method__get_previous_commits>`\ (\ max_commits\: :ref:`int<class_int>`\ ) |virtual| |required|                                                                                                                                                                                       |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`String<class_String>`\]         | :ref:`_get_remotes<class_EditorVCSInterface_private_method__get_remotes>`\ (\ ) |virtual| |required|                                                                                                                                                                                                                                              |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                      | :ref:`_get_vcs_name<class_EditorVCSInterface_private_method__get_vcs_name>`\ (\ ) |virtual| |required|                                                                                                                                                                                                                                            |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`_initialize<class_EditorVCSInterface_private_method__initialize>`\ (\ project_path\: :ref:`String<class_String>`\ ) |virtual| |required|                                                                                                                                                                                                    |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_pull<class_EditorVCSInterface_private_method__pull>`\ (\ remote\: :ref:`String<class_String>`\ ) |virtual| |required|                                                                                                                                                                                                                      |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_push<class_EditorVCSInterface_private_method__push>`\ (\ remote\: :ref:`String<class_String>`, force\: :ref:`bool<class_bool>`\ ) |virtual| |required|                                                                                                                                                                                     |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_remove_branch<class_EditorVCSInterface_private_method__remove_branch>`\ (\ branch_name\: :ref:`String<class_String>`\ ) |virtual| |required|                                                                                                                                                                                               |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_remove_remote<class_EditorVCSInterface_private_method__remove_remote>`\ (\ remote_name\: :ref:`String<class_String>`\ ) |virtual| |required|                                                                                                                                                                                               |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_set_credentials<class_EditorVCSInterface_private_method__set_credentials>`\ (\ username\: :ref:`String<class_String>`, password\: :ref:`String<class_String>`, ssh_public_key_path\: :ref:`String<class_String>`, ssh_private_key_path\: :ref:`String<class_String>`, ssh_passphrase\: :ref:`String<class_String>`\ ) |virtual| |required| |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`_shut_down<class_EditorVCSInterface_private_method__shut_down>`\ (\ ) |virtual| |required|                                                                                                                                                                                                                                                  |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_stage_file<class_EditorVCSInterface_private_method__stage_file>`\ (\ file_path\: :ref:`String<class_String>`\ ) |virtual| |required|                                                                                                                                                                                                       |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_unstage_file<class_EditorVCSInterface_private_method__unstage_file>`\ (\ file_path\: :ref:`String<class_String>`\ ) |virtual| |required|                                                                                                                                                                                                   |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                              | :ref:`add_diff_hunks_into_diff_file<class_EditorVCSInterface_method_add_diff_hunks_into_diff_file>`\ (\ diff_file\: :ref:`Dictionary<class_Dictionary>`, diff_hunks\: :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\]\ )                                                                                                         |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                              | :ref:`add_line_diffs_into_diff_hunk<class_EditorVCSInterface_method_add_line_diffs_into_diff_hunk>`\ (\ diff_hunk\: :ref:`Dictionary<class_Dictionary>`, line_diffs\: :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\]\ )                                                                                                         |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                              | :ref:`create_commit<class_EditorVCSInterface_method_create_commit>`\ (\ msg\: :ref:`String<class_String>`, author\: :ref:`String<class_String>`, id\: :ref:`String<class_String>`, unix_timestamp\: :ref:`int<class_int>`, offset_minutes\: :ref:`int<class_int>`\ )                                                                              |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                              | :ref:`create_diff_file<class_EditorVCSInterface_method_create_diff_file>`\ (\ new_file\: :ref:`String<class_String>`, old_file\: :ref:`String<class_String>`\ )                                                                                                                                                                                   |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                              | :ref:`create_diff_hunk<class_EditorVCSInterface_method_create_diff_hunk>`\ (\ old_start\: :ref:`int<class_int>`, new_start\: :ref:`int<class_int>`, old_lines\: :ref:`int<class_int>`, new_lines\: :ref:`int<class_int>`\ )                                                                                                                       |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                              | :ref:`create_diff_line<class_EditorVCSInterface_method_create_diff_line>`\ (\ new_line_no\: :ref:`int<class_int>`, old_line_no\: :ref:`int<class_int>`, content\: :ref:`String<class_String>`, status\: :ref:`String<class_String>`\ )                                                                                                            |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                              | :ref:`create_status_file<class_EditorVCSInterface_method_create_status_file>`\ (\ file_path\: :ref:`String<class_String>`, change_type\: :ref:`ChangeType<enum_EditorVCSInterface_ChangeType>`, area\: :ref:`TreeArea<enum_EditorVCSInterface_TreeArea>`\ )                                                                                       |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`popup_error<class_EditorVCSInterface_method_popup_error>`\ (\ msg\: :ref:`String<class_String>`\ )                                                                                                                                                                                                                                          |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **ChangeType**: [🔗<enum_EditorVCSInterface_ChangeType>]



[ChangeType<enum_EditorVCSInterface_ChangeType>] **CHANGE_TYPE_NEW** = `0`

A new file has been added.



[ChangeType<enum_EditorVCSInterface_ChangeType>] **CHANGE_TYPE_MODIFIED** = `1`

An earlier added file has been modified.



[ChangeType<enum_EditorVCSInterface_ChangeType>] **CHANGE_TYPE_RENAMED** = `2`

An earlier added file has been renamed.



[ChangeType<enum_EditorVCSInterface_ChangeType>] **CHANGE_TYPE_DELETED** = `3`

An earlier added file has been deleted.



[ChangeType<enum_EditorVCSInterface_ChangeType>] **CHANGE_TYPE_TYPECHANGE** = `4`

An earlier added file has been typechanged.



[ChangeType<enum_EditorVCSInterface_ChangeType>] **CHANGE_TYPE_UNMERGED** = `5`

A file is left unmerged.


----



enum **TreeArea**: [🔗<enum_EditorVCSInterface_TreeArea>]



[TreeArea<enum_EditorVCSInterface_TreeArea>] **TREE_AREA_COMMIT** = `0`

A commit is encountered from the commit area.



[TreeArea<enum_EditorVCSInterface_TreeArea>] **TREE_AREA_STAGED** = `1`

A file is encountered from the staged area.



[TreeArea<enum_EditorVCSInterface_TreeArea>] **TREE_AREA_UNSTAGED** = `2`

A file is encountered from the unstaged area.


----


## Method Descriptions



[bool<class_bool>] **_checkout_branch**\ (\ branch_name\: [String<class_String>]\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__checkout_branch>]

Checks out a `branch_name` in the VCS.


----



|void| **_commit**\ (\ msg\: [String<class_String>]\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__commit>]

Commits the currently staged changes and applies the commit `msg` to the resulting commit.


----



|void| **_create_branch**\ (\ branch_name\: [String<class_String>]\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__create_branch>]

Creates a new branch named `branch_name` in the VCS.


----



|void| **_create_remote**\ (\ remote_name\: [String<class_String>], remote_url\: [String<class_String>]\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__create_remote>]

Creates a new remote destination with name `remote_name` and points it to `remote_url`. This can be an HTTPS remote or an SSH remote.


----



|void| **_discard_file**\ (\ file_path\: [String<class_String>]\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__discard_file>]

Discards the changes made in a file present at `file_path`.


----



|void| **_fetch**\ (\ remote\: [String<class_String>]\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__fetch>]

Fetches new changes from the `remote`, but doesn't write changes to the current working directory. Equivalent to `git fetch`.


----



[Array<class_Array>]\[[String<class_String>]\] **_get_branch_list**\ (\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__get_branch_list>]

Gets an instance of an [Array<class_Array>] of [String<class_String>]\ s containing available branch names in the VCS.


----



[String<class_String>] **_get_current_branch_name**\ (\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__get_current_branch_name>]

Gets the current branch name defined in the VCS.


----



[Array<class_Array>]\[[Dictionary<class_Dictionary>]\] **_get_diff**\ (\ identifier\: [String<class_String>], area\: [int<class_int>]\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__get_diff>]

Returns an array of [Dictionary<class_Dictionary>] items (see [create_diff_file()<class_EditorVCSInterface_method_create_diff_file>], [create_diff_hunk()<class_EditorVCSInterface_method_create_diff_hunk>], [create_diff_line()<class_EditorVCSInterface_method_create_diff_line>], [add_line_diffs_into_diff_hunk()<class_EditorVCSInterface_method_add_line_diffs_into_diff_hunk>] and [add_diff_hunks_into_diff_file()<class_EditorVCSInterface_method_add_diff_hunks_into_diff_file>]), each containing information about a diff. If `identifier` is a file path, returns a file diff, and if it is a commit identifier, then returns a commit diff.


----



[Array<class_Array>]\[[Dictionary<class_Dictionary>]\] **_get_line_diff**\ (\ file_path\: [String<class_String>], text\: [String<class_String>]\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__get_line_diff>]

Returns an [Array<class_Array>] of [Dictionary<class_Dictionary>] items (see [create_diff_hunk()<class_EditorVCSInterface_method_create_diff_hunk>]), each containing a line diff between a file at `file_path` and the `text` which is passed in.


----



[Array<class_Array>]\[[Dictionary<class_Dictionary>]\] **_get_modified_files_data**\ (\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__get_modified_files_data>]

Returns an [Array<class_Array>] of [Dictionary<class_Dictionary>] items (see [create_status_file()<class_EditorVCSInterface_method_create_status_file>]), each containing the status data of every modified file in the project folder.


----



[Array<class_Array>]\[[Dictionary<class_Dictionary>]\] **_get_previous_commits**\ (\ max_commits\: [int<class_int>]\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__get_previous_commits>]

Returns an [Array<class_Array>] of [Dictionary<class_Dictionary>] items (see [create_commit()<class_EditorVCSInterface_method_create_commit>]), each containing the data for a past commit.


----



[Array<class_Array>]\[[String<class_String>]\] **_get_remotes**\ (\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__get_remotes>]

Returns an [Array<class_Array>] of [String<class_String>]\ s, each containing the name of a remote configured in the VCS.


----



[String<class_String>] **_get_vcs_name**\ (\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__get_vcs_name>]

Returns the name of the underlying VCS provider.


----



[bool<class_bool>] **_initialize**\ (\ project_path\: [String<class_String>]\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__initialize>]

Initializes the VCS plugin when called from the editor. Returns whether or not the plugin was successfully initialized. A VCS project is initialized at `project_path`.


----



|void| **_pull**\ (\ remote\: [String<class_String>]\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__pull>]

Pulls changes from the remote. This can give rise to merge conflicts.


----



|void| **_push**\ (\ remote\: [String<class_String>], force\: [bool<class_bool>]\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__push>]

Pushes changes to the `remote`. If `force` is `true`, a force push will override the change history already present on the remote.


----



|void| **_remove_branch**\ (\ branch_name\: [String<class_String>]\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__remove_branch>]

Remove a branch from the local VCS.


----



|void| **_remove_remote**\ (\ remote_name\: [String<class_String>]\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__remove_remote>]

Remove a remote from the local VCS.


----



|void| **_set_credentials**\ (\ username\: [String<class_String>], password\: [String<class_String>], ssh_public_key_path\: [String<class_String>], ssh_private_key_path\: [String<class_String>], ssh_passphrase\: [String<class_String>]\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__set_credentials>]

Set user credentials in the underlying VCS. `username` and `password` are used only during HTTPS authentication unless not already mentioned in the remote URL. `ssh_public_key_path`, `ssh_private_key_path`, and `ssh_passphrase` are only used during SSH authentication.


----



[bool<class_bool>] **_shut_down**\ (\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__shut_down>]

Shuts down VCS plugin instance. Called when the user either closes the editor or shuts down the VCS plugin through the editor UI.


----



|void| **_stage_file**\ (\ file_path\: [String<class_String>]\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__stage_file>]

Stages the file present at `file_path` to the staged area.


----



|void| **_unstage_file**\ (\ file_path\: [String<class_String>]\ ) |virtual| |required| [🔗<class_EditorVCSInterface_private_method__unstage_file>]

Unstages the file present at `file_path` from the staged area to the unstaged area.


----



[Dictionary<class_Dictionary>] **add_diff_hunks_into_diff_file**\ (\ diff_file\: [Dictionary<class_Dictionary>], diff_hunks\: [Array<class_Array>]\[[Dictionary<class_Dictionary>]\]\ ) [🔗<class_EditorVCSInterface_method_add_diff_hunks_into_diff_file>]

Helper function to add an array of `diff_hunks` into a `diff_file`.


----



[Dictionary<class_Dictionary>] **add_line_diffs_into_diff_hunk**\ (\ diff_hunk\: [Dictionary<class_Dictionary>], line_diffs\: [Array<class_Array>]\[[Dictionary<class_Dictionary>]\]\ ) [🔗<class_EditorVCSInterface_method_add_line_diffs_into_diff_hunk>]

Helper function to add an array of `line_diffs` into a `diff_hunk`.


----



[Dictionary<class_Dictionary>] **create_commit**\ (\ msg\: [String<class_String>], author\: [String<class_String>], id\: [String<class_String>], unix_timestamp\: [int<class_int>], offset_minutes\: [int<class_int>]\ ) [🔗<class_EditorVCSInterface_method_create_commit>]

Helper function to create a commit [Dictionary<class_Dictionary>] item. `msg` is the commit message of the commit. `author` is a single human-readable string containing all the author's details, e.g. the email and name configured in the VCS. `id` is the identifier of the commit, in whichever format your VCS may provide an identifier to commits. `unix_timestamp` is the UTC Unix timestamp of when the commit was created. `offset_minutes` is the timezone offset in minutes, recorded from the system timezone where the commit was created.


----



[Dictionary<class_Dictionary>] **create_diff_file**\ (\ new_file\: [String<class_String>], old_file\: [String<class_String>]\ ) [🔗<class_EditorVCSInterface_method_create_diff_file>]

Helper function to create a [Dictionary<class_Dictionary>] for storing old and new diff file paths.


----



[Dictionary<class_Dictionary>] **create_diff_hunk**\ (\ old_start\: [int<class_int>], new_start\: [int<class_int>], old_lines\: [int<class_int>], new_lines\: [int<class_int>]\ ) [🔗<class_EditorVCSInterface_method_create_diff_hunk>]

Helper function to create a [Dictionary<class_Dictionary>] for storing diff hunk data. `old_start` is the starting line number in old file. `new_start` is the starting line number in new file. `old_lines` is the number of lines in the old file. `new_lines` is the number of lines in the new file.


----



[Dictionary<class_Dictionary>] **create_diff_line**\ (\ new_line_no\: [int<class_int>], old_line_no\: [int<class_int>], content\: [String<class_String>], status\: [String<class_String>]\ ) [🔗<class_EditorVCSInterface_method_create_diff_line>]

Helper function to create a [Dictionary<class_Dictionary>] for storing a line diff. `new_line_no` is the line number in the new file (can be `-1` if the line is deleted). `old_line_no` is the line number in the old file (can be `-1` if the line is added). `content` is the diff text. `status` is a single character string which stores the line origin.


----



[Dictionary<class_Dictionary>] **create_status_file**\ (\ file_path\: [String<class_String>], change_type\: [ChangeType<enum_EditorVCSInterface_ChangeType>], area\: [TreeArea<enum_EditorVCSInterface_TreeArea>]\ ) [🔗<class_EditorVCSInterface_method_create_status_file>]

Helper function to create a [Dictionary<class_Dictionary>] used by editor to read the status of a file.


----



|void| **popup_error**\ (\ msg\: [String<class_String>]\ ) [🔗<class_EditorVCSInterface_method_popup_error>]

Pops up an error message in the editor which is shown as coming from the underlying VCS. Use this to show VCS specific error messages.

