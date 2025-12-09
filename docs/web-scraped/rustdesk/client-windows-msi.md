# Source: https://rustdesk.com/docs/en/client/windows/msi/

# MSI

The MSI package supports command line parameters for silent installation.

## Parameters

## INSTALLFOLDER

The installation folder.

**Default**: `[ProgramFiles6432Folder]\[app name]`, usually `C:\Program Files\[app name]`.

## CREATESTARTMENUSHORTCUTS

Whether to create a start menu shortcut.

**Default**:

- Install. Defaults to `1`.
- Upgrade. Defaults to the last installed options.

NoValueDesc1`1`Yes2`0`No3`Y`Yes, same as `1`4`N`No, same as `0`
## CREATEDESKTOPSHORTCUTS

Whether to create a desktop shortcut.

**Default**:

- Install. Defaults to `1`.
- Upgrade. Defaults to the last installed options.

NoValueDesc1`1`Yes2`0`No3`Y`Yes, same as `1`4`N`No, same as `0`
## INSTALLPRINTER

Whether to install a printer. The printer is used to execute the print jobs of the controlled side locally.

Since version `1.3.9`.

**Default**:

- Install. Defaults to `1`.
- Upgrade. Defaults to the last installed options.

NoValueDesc1`1`Yes2`0`No3`Y`Yes, same as `1`4`N`No, same as `0`
# Examples

**Caution**: For versions prior to `2024-08-05`, there are issues with silent installation and silent repair. Please uninstall first, then install.

## Install with installation parameters

Silent installation, set the installation path, do not create a desktop shortcut, create a start menu shortcut.

```
msiexec /i RustDesk-1.msi /qn INSTALLFOLDER=&#34;D:\Program Files\RustDesk&#34; CREATESTARTMENUSHORTCUTS=&#34;Y&#34; CREATEDESKTOPSHORTCUTS=&#34;N&#34; INSTALLPRINTER=&#34;N&#34; /l*v install.log
```

**Note**: `/l*v install.log` means printing the execution log to `install.log`.

## Upgrade, without parameters

Upgrade with the previous installation path and installation options.

```
msiexec /i RustDesk-2.msi /qn /l*v install.log
```

## Upgrade, modify installation options

```
msiexec /i RustDesk-1.msi /qn INSTALLFOLDER=&#34;C:\Program Files\RustDesk&#34; CREATESTARTMENUSHORTCUTS=&#34;N&#34; CREATEDESKTOPSHORTCUTS=&#34;N&#34; INSTALLPRINTER=&#34;N&#34; /l*v install.log
```