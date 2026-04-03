:github_url: hide



# EditorExportPlatformWindows

**Inherits:** [EditorExportPlatformPC<class_EditorExportPlatformPC>] **<** [EditorExportPlatform<class_EditorExportPlatform>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Exporter for Windows.


## Description

The Windows exporter customizes how a Windows build is handled. In the editor's "Export" window, it is created when adding a new "Windows" preset.


## Tutorials

- [../tutorials/export/exporting_for_windows](Exporting for Windows .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`application/company_name<class_EditorExportPlatformWindows_property_application/company_name>`                               |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`application/console_wrapper_icon<class_EditorExportPlatformWindows_property_application/console_wrapper_icon>`               |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`application/copyright<class_EditorExportPlatformWindows_property_application/copyright>`                                     |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`application/d3d12_agility_sdk_multiarch<class_EditorExportPlatformWindows_property_application/d3d12_agility_sdk_multiarch>` |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                             | :ref:`application/export_angle<class_EditorExportPlatformWindows_property_application/export_angle>`                               |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                             | :ref:`application/export_d3d12<class_EditorExportPlatformWindows_property_application/export_d3d12>`                               |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`application/file_description<class_EditorExportPlatformWindows_property_application/file_description>`                       |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`application/file_version<class_EditorExportPlatformWindows_property_application/file_version>`                               |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`application/icon<class_EditorExportPlatformWindows_property_application/icon>`                                               |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                             | :ref:`application/icon_interpolation<class_EditorExportPlatformWindows_property_application/icon_interpolation>`                   |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`application/modify_resources<class_EditorExportPlatformWindows_property_application/modify_resources>`                       |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`application/product_name<class_EditorExportPlatformWindows_property_application/product_name>`                               |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`application/product_version<class_EditorExportPlatformWindows_property_application/product_version>`                         |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`application/trademarks<class_EditorExportPlatformWindows_property_application/trademarks>`                                   |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`binary_format/architecture<class_EditorExportPlatformWindows_property_binary_format/architecture>`                           |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`binary_format/embed_pck<class_EditorExportPlatformWindows_property_binary_format/embed_pck>`                                 |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>` | :ref:`codesign/custom_options<class_EditorExportPlatformWindows_property_codesign/custom_options>`                                 |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`codesign/description<class_EditorExportPlatformWindows_property_codesign/description>`                                       |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                             | :ref:`codesign/digest_algorithm<class_EditorExportPlatformWindows_property_codesign/digest_algorithm>`                             |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`codesign/enable<class_EditorExportPlatformWindows_property_codesign/enable>`                                                 |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`codesign/identity<class_EditorExportPlatformWindows_property_codesign/identity>`                                             |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                             | :ref:`codesign/identity_type<class_EditorExportPlatformWindows_property_codesign/identity_type>`                                   |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`codesign/password<class_EditorExportPlatformWindows_property_codesign/password>`                                             |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`codesign/timestamp<class_EditorExportPlatformWindows_property_codesign/timestamp>`                                           |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`codesign/timestamp_server_url<class_EditorExportPlatformWindows_property_codesign/timestamp_server_url>`                     |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`custom_template/debug<class_EditorExportPlatformWindows_property_custom_template/debug>`                                     |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`custom_template/release<class_EditorExportPlatformWindows_property_custom_template/release>`                                 |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                             | :ref:`debug/export_console_wrapper<class_EditorExportPlatformWindows_property_debug/export_console_wrapper>`                       |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`shader_baker/enabled<class_EditorExportPlatformWindows_property_shader_baker/enabled>`                                       |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`ssh_remote_deploy/cleanup_script<class_EditorExportPlatformWindows_property_ssh_remote_deploy/cleanup_script>`               |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`ssh_remote_deploy/enabled<class_EditorExportPlatformWindows_property_ssh_remote_deploy/enabled>`                             |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`ssh_remote_deploy/extra_args_scp<class_EditorExportPlatformWindows_property_ssh_remote_deploy/extra_args_scp>`               |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`ssh_remote_deploy/extra_args_ssh<class_EditorExportPlatformWindows_property_ssh_remote_deploy/extra_args_ssh>`               |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`ssh_remote_deploy/host<class_EditorExportPlatformWindows_property_ssh_remote_deploy/host>`                                   |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`ssh_remote_deploy/port<class_EditorExportPlatformWindows_property_ssh_remote_deploy/port>`                                   |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`ssh_remote_deploy/run_script<class_EditorExportPlatformWindows_property_ssh_remote_deploy/run_script>`                       |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`texture_format/etc2_astc<class_EditorExportPlatformWindows_property_texture_format/etc2_astc>`                               |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`texture_format/s3tc_bptc<class_EditorExportPlatformWindows_property_texture_format/s3tc_bptc>`                               |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[String<class_String>] **application/company_name** [🔗<class_EditorExportPlatformWindows_property_application/company_name>]

Company that produced the application. Required. See [StringFileInfo ](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block)_.


----



[String<class_String>] **application/console_wrapper_icon** [🔗<class_EditorExportPlatformWindows_property_application/console_wrapper_icon>]

Console wrapper icon file. If left empty, it will fallback to [application/icon<class_EditorExportPlatformWindows_property_application/icon>], then to [ProjectSettings.application/config/windows_native_icon<class_ProjectSettings_property_application/config/windows_native_icon>], and lastly, [ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>].


----



[String<class_String>] **application/copyright** [🔗<class_EditorExportPlatformWindows_property_application/copyright>]

Copyright notice for the bundle visible to the user. Optional. See [StringFileInfo ](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block)_.


----



[bool<class_bool>] **application/d3d12_agility_sdk_multiarch** [🔗<class_EditorExportPlatformWindows_property_application/d3d12_agility_sdk_multiarch>]

If `true`, and [application/export_d3d12<class_EditorExportPlatformWindows_property_application/export_d3d12>] is set, the Agility SDK DLLs will be stored in arch-specific subdirectories.


----



[int<class_int>] **application/export_angle** [🔗<class_EditorExportPlatformWindows_property_application/export_angle>]

If set to `1`, ANGLE libraries are exported with the exported application. If set to `0`, ANGLE libraries are exported only if [ProjectSettings.rendering/gl_compatibility/driver<class_ProjectSettings_property_rendering/gl_compatibility/driver>] is set to `"opengl3_angle"`.


----



[int<class_int>] **application/export_d3d12** [🔗<class_EditorExportPlatformWindows_property_application/export_d3d12>]

If set to `1`, the Direct3D 12 runtime libraries (Agility SDK, PIX) are exported with the exported application. If set to `0`, Direct3D 12 libraries are exported only if [ProjectSettings.rendering/rendering_device/driver<class_ProjectSettings_property_rendering/rendering_device/driver>] is set to `"d3d12"`.


----



[String<class_String>] **application/file_description** [🔗<class_EditorExportPlatformWindows_property_application/file_description>]

File description to be presented to users. Required. See [StringFileInfo ](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block)_.


----



[String<class_String>] **application/file_version** [🔗<class_EditorExportPlatformWindows_property_application/file_version>]

Version number of the file. Falls back to [ProjectSettings.application/config/version<class_ProjectSettings_property_application/config/version>] if left empty. See [StringFileInfo ](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block)_.


----



[String<class_String>] **application/icon** [🔗<class_EditorExportPlatformWindows_property_application/icon>]

Application icon file. If left empty, it will fallback to [ProjectSettings.application/config/windows_native_icon<class_ProjectSettings_property_application/config/windows_native_icon>], and then to [ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>].


----



[int<class_int>] **application/icon_interpolation** [🔗<class_EditorExportPlatformWindows_property_application/icon_interpolation>]

Interpolation method used to resize application icon.


----



[bool<class_bool>] **application/modify_resources** [🔗<class_EditorExportPlatformWindows_property_application/modify_resources>]

If enabled, icon and metadata of the exported executable is set according to the other `application/*` values.


----



[String<class_String>] **application/product_name** [🔗<class_EditorExportPlatformWindows_property_application/product_name>]

Name of the application. Required. See [StringFileInfo ](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block)_.


----



[String<class_String>] **application/product_version** [🔗<class_EditorExportPlatformWindows_property_application/product_version>]

Application version visible to the user. Falls back to [ProjectSettings.application/config/version<class_ProjectSettings_property_application/config/version>] if left empty. See [StringFileInfo ](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block)_.


----



[String<class_String>] **application/trademarks** [🔗<class_EditorExportPlatformWindows_property_application/trademarks>]

Trademarks and registered trademarks that apply to the file. Optional. See [StringFileInfo ](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block)_.


----



[String<class_String>] **binary_format/architecture** [🔗<class_EditorExportPlatformWindows_property_binary_format/architecture>]

Application executable architecture.

Supported architectures: `x86_32`, `x86_64`, and `arm64`.


----



[bool<class_bool>] **binary_format/embed_pck** [🔗<class_EditorExportPlatformWindows_property_binary_format/embed_pck>]

If `true`, project resources are embedded into the executable.


----



[PackedStringArray<class_PackedStringArray>] **codesign/custom_options** [🔗<class_EditorExportPlatformWindows_property_codesign/custom_options>]

Array of the additional command line arguments passed to the code signing tool. See [Sign Tool ](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe)_.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray<class_PackedStringArray>] for more details.


----



[String<class_String>] **codesign/description** [🔗<class_EditorExportPlatformWindows_property_codesign/description>]

Description of the signed content. See [Sign Tool ](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe)_.


----



[int<class_int>] **codesign/digest_algorithm** [🔗<class_EditorExportPlatformWindows_property_codesign/digest_algorithm>]

Digest algorithm to use for creating signature. See [Sign Tool ](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe)_.


----



[bool<class_bool>] **codesign/enable** [🔗<class_EditorExportPlatformWindows_property_codesign/enable>]

If `true`, executable signing is enabled.


----



[String<class_String>] **codesign/identity** [🔗<class_EditorExportPlatformWindows_property_codesign/identity>]

PKCS #12 certificate file used to sign executable or certificate SHA-1 hash (if [codesign/identity_type<class_EditorExportPlatformWindows_property_codesign/identity_type>] is set to "Use certificate store"). See [Sign Tool ](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe)_.

Can be overridden with the environment variable `GODOT_WINDOWS_CODESIGN_IDENTITY`.


----



[int<class_int>] **codesign/identity_type** [🔗<class_EditorExportPlatformWindows_property_codesign/identity_type>]

Type of identity to use. See [Sign Tool ](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe)_.

Can be overridden with the environment variable `GODOT_WINDOWS_CODESIGN_IDENTITY_TYPE`.


----



[String<class_String>] **codesign/password** [🔗<class_EditorExportPlatformWindows_property_codesign/password>]

Password for the certificate file used to sign executable. See [Sign Tool ](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe)_.

Can be overridden with the environment variable `GODOT_WINDOWS_CODESIGN_PASSWORD`.


----



[bool<class_bool>] **codesign/timestamp** [🔗<class_EditorExportPlatformWindows_property_codesign/timestamp>]

If `true`, time-stamp is added to the signature. See [Sign Tool ](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe)_.


----



[String<class_String>] **codesign/timestamp_server_url** [🔗<class_EditorExportPlatformWindows_property_codesign/timestamp_server_url>]

URL of the time stamp server. If left empty, the default server is used. See [Sign Tool ](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe)_.


----



[String<class_String>] **custom_template/debug** [🔗<class_EditorExportPlatformWindows_property_custom_template/debug>]

Path to the custom export template. If left empty, default template is used.


----



[String<class_String>] **custom_template/release** [🔗<class_EditorExportPlatformWindows_property_custom_template/release>]

Path to the custom export template. If left empty, default template is used.


----



[int<class_int>] **debug/export_console_wrapper** [🔗<class_EditorExportPlatformWindows_property_debug/export_console_wrapper>]

If `true`, a console wrapper executable is exported alongside the main executable, which allows running the project with enabled console output.


----



[bool<class_bool>] **shader_baker/enabled** [🔗<class_EditorExportPlatformWindows_property_shader_baker/enabled>]

If `true`, shaders will be compiled and embedded in the application. This option is only supported when using the Forward+ and Mobile renderers.

\ **Note:** When exporting as a dedicated server, the shader baker is always disabled since no rendering is performed.


----



[String<class_String>] **ssh_remote_deploy/cleanup_script** [🔗<class_EditorExportPlatformWindows_property_ssh_remote_deploy/cleanup_script>]

Script code to execute on the remote host when app is finished.

The following variables can be used in the script:

- `{temp_dir}` - Path of temporary folder on the remote, used to upload app and scripts to.

- `{archive_name}` - Name of the ZIP containing uploaded application.

- `{exe_name}` - Name of application executable.

- `{cmd_args}` - Array of the command line argument for the application.


----



[bool<class_bool>] **ssh_remote_deploy/enabled** [🔗<class_EditorExportPlatformWindows_property_ssh_remote_deploy/enabled>]

Enables remote deploy using SSH/SCP.


----



[String<class_String>] **ssh_remote_deploy/extra_args_scp** [🔗<class_EditorExportPlatformWindows_property_ssh_remote_deploy/extra_args_scp>]

Array of the additional command line arguments passed to the SCP.


----



[String<class_String>] **ssh_remote_deploy/extra_args_ssh** [🔗<class_EditorExportPlatformWindows_property_ssh_remote_deploy/extra_args_ssh>]

Array of the additional command line arguments passed to the SSH.


----



[String<class_String>] **ssh_remote_deploy/host** [🔗<class_EditorExportPlatformWindows_property_ssh_remote_deploy/host>]

Remote host SSH user name and address, in `user@address` format.


----



[String<class_String>] **ssh_remote_deploy/port** [🔗<class_EditorExportPlatformWindows_property_ssh_remote_deploy/port>]

Remote host SSH port number.


----



[String<class_String>] **ssh_remote_deploy/run_script** [🔗<class_EditorExportPlatformWindows_property_ssh_remote_deploy/run_script>]

Script code to execute on the remote host when running the app.

The following variables can be used in the script:

- `{temp_dir}` - Path of temporary folder on the remote, used to upload app and scripts to.

- `{archive_name}` - Name of the ZIP containing uploaded application.

- `{exe_name}` - Name of application executable.

- `{cmd_args}` - Array of the command line argument for the application.


----



[bool<class_bool>] **texture_format/etc2_astc** [🔗<class_EditorExportPlatformWindows_property_texture_format/etc2_astc>]

If `true`, project textures are exported in the ETC2/ASTC format.


----



[bool<class_bool>] **texture_format/s3tc_bptc** [🔗<class_EditorExportPlatformWindows_property_texture_format/s3tc_bptc>]

If `true`, project textures are exported in the S3TC/BPTC format.

