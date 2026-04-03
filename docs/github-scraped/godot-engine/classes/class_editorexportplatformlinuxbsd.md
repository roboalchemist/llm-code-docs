:github_url: hide



# EditorExportPlatformLinuxBSD

**Inherits:** [EditorExportPlatformPC<class_EditorExportPlatformPC>] **<** [EditorExportPlatform<class_EditorExportPlatform>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Exporter for Linux/BSD.


## Tutorials

- [../tutorials/export/exporting_for_linux](Exporting for Linux .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`binary_format/architecture<class_EditorExportPlatformLinuxBSD_property_binary_format/architecture>`             |
> +-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`binary_format/embed_pck<class_EditorExportPlatformLinuxBSD_property_binary_format/embed_pck>`                   |
> +-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`custom_template/debug<class_EditorExportPlatformLinuxBSD_property_custom_template/debug>`                       |
> +-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`custom_template/release<class_EditorExportPlatformLinuxBSD_property_custom_template/release>`                   |
> +-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`debug/export_console_wrapper<class_EditorExportPlatformLinuxBSD_property_debug/export_console_wrapper>`         |
> +-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`shader_baker/enabled<class_EditorExportPlatformLinuxBSD_property_shader_baker/enabled>`                         |
> +-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`ssh_remote_deploy/cleanup_script<class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/cleanup_script>` |
> +-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`ssh_remote_deploy/enabled<class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/enabled>`               |
> +-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`ssh_remote_deploy/extra_args_scp<class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/extra_args_scp>` |
> +-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`ssh_remote_deploy/extra_args_ssh<class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/extra_args_ssh>` |
> +-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`ssh_remote_deploy/host<class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/host>`                     |
> +-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`ssh_remote_deploy/port<class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/port>`                     |
> +-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`ssh_remote_deploy/run_script<class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/run_script>`         |
> +-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`texture_format/etc2_astc<class_EditorExportPlatformLinuxBSD_property_texture_format/etc2_astc>`                 |
> +-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`texture_format/s3tc_bptc<class_EditorExportPlatformLinuxBSD_property_texture_format/s3tc_bptc>`                 |
> +-----------------------------+-----------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[String<class_String>] **binary_format/architecture** [🔗<class_EditorExportPlatformLinuxBSD_property_binary_format/architecture>]

Application executable architecture.

Supported architectures: `x86_32`, `x86_64`, `arm64`, `arm32`, `rv64`, `ppc64`, and `loongarch64`.

Official export templates include `x86_32`, `x86_64`, `arm32`, and `arm64` binaries only.


----



[bool<class_bool>] **binary_format/embed_pck** [🔗<class_EditorExportPlatformLinuxBSD_property_binary_format/embed_pck>]

If `true`, project resources are embedded into the executable.


----



[String<class_String>] **custom_template/debug** [🔗<class_EditorExportPlatformLinuxBSD_property_custom_template/debug>]

Path to the custom export template. If left empty, default template is used.


----



[String<class_String>] **custom_template/release** [🔗<class_EditorExportPlatformLinuxBSD_property_custom_template/release>]

Path to the custom export template. If left empty, default template is used.


----



[int<class_int>] **debug/export_console_wrapper** [🔗<class_EditorExportPlatformLinuxBSD_property_debug/export_console_wrapper>]

If `true`, a console wrapper is exported alongside the main executable, which allows running the project with enabled console output.


----



[bool<class_bool>] **shader_baker/enabled** [🔗<class_EditorExportPlatformLinuxBSD_property_shader_baker/enabled>]

If `true`, shaders will be compiled and embedded in the application. This option is only supported when using the Forward+ or Mobile renderers.

\ **Note:** When exporting as a dedicated server, the shader baker is always disabled since no rendering is performed.


----



[String<class_String>] **ssh_remote_deploy/cleanup_script** [🔗<class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/cleanup_script>]

Script code to execute on the remote host when app is finished.

The following variables can be used in the script:

- `{temp_dir}` - Path of temporary folder on the remote, used to upload app and scripts to.

- `{archive_name}` - Name of the ZIP containing uploaded application.

- `{exe_name}` - Name of application executable.

- `{cmd_args}` - Array of the command line argument for the application.


----



[bool<class_bool>] **ssh_remote_deploy/enabled** [🔗<class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/enabled>]

Enables remote deploy using SSH/SCP.


----



[String<class_String>] **ssh_remote_deploy/extra_args_scp** [🔗<class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/extra_args_scp>]

Array of the additional command line arguments passed to the SCP.


----



[String<class_String>] **ssh_remote_deploy/extra_args_ssh** [🔗<class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/extra_args_ssh>]

Array of the additional command line arguments passed to the SSH.


----



[String<class_String>] **ssh_remote_deploy/host** [🔗<class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/host>]

Remote host SSH user name and address, in `user@address` format.


----



[String<class_String>] **ssh_remote_deploy/port** [🔗<class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/port>]

Remote host SSH port number.


----



[String<class_String>] **ssh_remote_deploy/run_script** [🔗<class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/run_script>]

Script code to execute on the remote host when running the app.

The following variables can be used in the script:

- `{temp_dir}` - Path of temporary folder on the remote, used to upload app and scripts to.

- `{archive_name}` - Name of the ZIP containing uploaded application.

- `{exe_name}` - Name of application executable.

- `{cmd_args}` - Array of the command line argument for the application.


----



[bool<class_bool>] **texture_format/etc2_astc** [🔗<class_EditorExportPlatformLinuxBSD_property_texture_format/etc2_astc>]

If `true`, project textures are exported in the ETC2/ASTC format.


----



[bool<class_bool>] **texture_format/s3tc_bptc** [🔗<class_EditorExportPlatformLinuxBSD_property_texture_format/s3tc_bptc>]

If `true`, project textures are exported in the S3TC/BPTC format.

