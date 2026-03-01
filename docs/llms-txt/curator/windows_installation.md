# Source: https://docs.curator.interworks.com/setup/installation/windows_installation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Windows Installation

> Instructions for installing Curator on Windows.

## Installation Steps

<Steps>
  <Step title="Download the Installer">
    Log in to the server where you'd like to install Curator and [download the Curator installer for Windows](https://api.curator.interworks.com/CuratorSetup.exe).
  </Step>

  <Step title="Run the Installer">
    Locate your download and right-click the file, then select "Run as Administrator" to begin the installation process.

        <img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/run_as_admin.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=89aec2ac7651eb2221646df19ea3296b" alt="Run .exe as admin" data-og-width="669" width="669" data-og-height="401" height="401" data-path="assets/images/setup/installation/windows_installation/run_as_admin.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/run_as_admin.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=6e8c40c95996ef1c3f63d88793445e61 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/run_as_admin.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=e0496ea4714b60dd7af5b9eb9c17bfd9 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/run_as_admin.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=a974cbe0639e0a5997b6a66bee505fa3 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/run_as_admin.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=700e0dbfe7fc8c1b446795b04908969b 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/run_as_admin.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=6ba6dcb55947a0de1929c8c0e2772f3d 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/run_as_admin.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=1d37f1dcab4ba466da834a9e10d5d34d 2500w" />

    Click the "Install" button to run initial installation process:

        <img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/click_install.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=8b74b6a87c83b6dbb386e3861d17eaca" alt="Installer view" data-og-width="543" width="543" data-og-height="358" height="358" data-path="assets/images/setup/installation/windows_installation/click_install.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/click_install.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=fbdedadf835d778add09134de6973934 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/click_install.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=a4f6a51c9a2ac02969f173f28f16d87c 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/click_install.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=5e09fab8ce2d379448477a06777ff4d1 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/click_install.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=1b4e61923e30a50e957b5f25b97b40f8 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/click_install.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=897035de492cd25bab61804c0f9fdb11 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/click_install.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=4f76154bfd71577c62555829d4058051 2500w" />

    Click "Options" to change the installation directory.
  </Step>

  <Step title="Credentials">
    The installer will generate credentials for use during installation and will store them in a file in the installation
    directory (Default: `/var/www/curator_info.txt` or `C:\InterWorks\Curator\curator_info.txt` in Windows). You will need
    these credentials to complete the installation and to log in to the Curator backend after installation.
  </Step>

  <Step title="License Key">
    Enter your license key when prompted. If you do not have a license key, please contact InterWorks to obtain one.

        <img src="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/installation_enter_key.png?fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=f78214155c914ed84abf7a0cfbed9590" alt="License key prompt page" data-og-width="2880" width="2880" data-og-height="1800" height="1800" data-path="assets/images/snippets/installation_enter_key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/installation_enter_key.png?w=280&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=a038f0b5e19ba7f27f10f087bfc36617 280w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/installation_enter_key.png?w=560&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=a43cc98c58b2938445cecc7286314520 560w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/installation_enter_key.png?w=840&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=06a6e59aa1e66df53033cbd203ff53a7 840w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/installation_enter_key.png?w=1100&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=445020613ecc2bf6f2c0452e7ba404f5 1100w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/installation_enter_key.png?w=1650&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=59279cfeea99e4f57144c016e19a3a6d 1650w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/installation_enter_key.png?w=2500&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=0e63e628c90d7d9167cdb7999546efa4 2500w" />
  </Step>

  <Step title="Database Connection">
    You may be prompted to enter your database connection information if the installer is unable to automatically find the
    database for you.

        <img src="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/enter_database_credentials.png?fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=ac7b79590da93165c51793b36faffba2" alt="Database credentials prompt page" data-og-width="2880" width="2880" data-og-height="1800" height="1800" data-path="assets/images/snippets/enter_database_credentials.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/enter_database_credentials.png?w=280&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=e5e615ae58f9a8b398caade550f2249c 280w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/enter_database_credentials.png?w=560&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=2a0cdc565c6f768ba14caded166aaab5 560w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/enter_database_credentials.png?w=840&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=2b0363b31af1e9af44adb74cd2c316ff 840w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/enter_database_credentials.png?w=1100&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=8b3a7f03bf1e122221ccbe67dc8bae2b 1100w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/enter_database_credentials.png?w=1650&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=1b6a6c2ce5d6e8a520ae3ca999b75c0f 1650w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/enter_database_credentials.png?w=2500&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=be65e316d9c1d27dacd797afed0afaa8 2500w" />
  </Step>

  <Step title="Success">
    If the installation is successful, you will be redirected to your new Curator homepage

        <img src="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/post_install_homepage.png?fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=b4fac79de5100b4aa4b4e76c6c4c88fb" alt="Database credentials prompt page" data-og-width="2880" width="2880" data-og-height="1800" height="1800" data-path="assets/images/snippets/post_install_homepage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/post_install_homepage.png?w=280&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=71b2579f6586cd626ff09b7cb2ce875b 280w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/post_install_homepage.png?w=560&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=ccb029c3a1dc255d357e60aa50de2866 560w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/post_install_homepage.png?w=840&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=63065e8d1999fdbc16b8a32bc6db541d 840w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/post_install_homepage.png?w=1100&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=4b000d0905e26baabd2115e854d72891 1100w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/post_install_homepage.png?w=1650&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=52df8dad071b6be5a3f190316353310d 1650w, https://mintcdn.com/interworks/3RotvmSfKD9xBISI/assets/images/snippets/post_install_homepage.png?w=2500&fit=max&auto=format&n=3RotvmSfKD9xBISI&q=85&s=198c8d449d6b2b317581f4068a58ead1 2500w" />

    Using the same auto-generated credentials created in the install script above, you can log into the Curator backend which
    can be accessed from `http://curatorexample.com/backend`. If you're on the server you installed, you may also use localhost.
    Keep in mind this may be an IP address or computer name until your IT team sets up DNS.
  </Step>
</Steps>

## Log Locations

These paths are dependant on your installation location, but these are the default paths:

* Apache: `C:\InterWorks\Curator\httpd_errors.log`
* PHP: `C:\InterWorks\Curator\php_errors.log`
* Installation Log: `C:\InterWorks\Curator\install.log`

## Other Information

These paths are dependant on your installation location, but these are the default paths:

* Webroot: `C:\InterWorks\Curator\htdocs`
* HTTPD Config: `C:\InterWorks\Curator\web.conf`
* PHP.ini: `C:\InterWorks\Curator\php.ini`
* Start Process: `C:\InterWorks\Curator\start.bat` (Also desktop shortcut)
* Stop Process: `C:\InterWorks\Curator\stop.bat` (Also desktop shortcut)
* Apache Location: `C:\InterWorks\Curator\libs\Apache24`
* Database Location: `C:\InterWorks\Curator\libs\MariaDB`
* PHP Location: `C:\InterWorks\Curator\libs\PHP`

## Changing the Install Path

This is *not recommended* but may be necessary in rare circumstances. The installer will default to
`C:\InterWorks\Curator` if no changes are made to the install path. If you must change the install path, click the
"Options" button in the installer window

<img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/click_options.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=346d94183d86e33d14727705647586df" alt="Highlight options button" data-og-width="538" width="538" data-og-height="384" height="384" data-path="assets/images/setup/installation/windows_installation/click_options.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/click_options.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=060d7bf44c4623f5cca219ccdd86b666 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/click_options.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=10639fc48936395bc93c569f826a89e2 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/click_options.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=c5408334e50b206fd7bd6cbec51c4c9f 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/click_options.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=d27aa7ed2caadcd9ceaf78ecfe3290d7 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/click_options.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=f0494bced9b502ff545ae6fd74de0a9e 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/click_options.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=7db9c68d29c3e8a531c7fb7c53dd965c 2500w" />

then change the Install Location path:

<img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/change_path.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=8501dbecf6e39ef1d103714905a6f217" alt="Change install path" data-og-width="533" width="533" data-og-height="358" height="358" data-path="assets/images/setup/installation/windows_installation/change_path.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/change_path.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=d25c0f93335377e8f94fffb355e559c7 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/change_path.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=220e9b4c43d5999eb0c730114d790bd4 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/change_path.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=6031547024cd40ebd39fad058afb5f9c 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/change_path.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=86e752b3c41017c14ec84f46f77c8acf 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/change_path.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=c053e17f9b9de72b8b6746d0724753e4 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/installation/windows_installation/change_path.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=5c33b394a8f6c6c823078d719eb351d1 2500w" />

Please note that the paths above may no longer be valid if you change the install path.
