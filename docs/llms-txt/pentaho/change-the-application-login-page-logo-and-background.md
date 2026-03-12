# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/customize-pentaho-products-cp/customize-the-pentaho-user-console/change-the-application-login-page-logo-and-background.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/customize-pentaho-products-cp/customize-the-pentaho-user-console/change-the-application-login-page-logo-and-background.md

# Change the application login page logo and background

You can edit the User Console login page to replace the default logo with your corporate logo or other image. You can also modify or replace the default background image and other page elements to better fit your organization or brand.

![User console logo and background elements](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-1dbc88974808622b5e5bd148220c982a93bd6fe7%2FPUC_login_screen_elements.png?alt=media)

**Note:** The User Console login page uses CSS properties that start with "`#login`" for easy identification. The method for changing the logo and background for other available themes, like Crystal and Sapphire, is the same. Each theme uses different style definitions, image types, names, and file paths.

Follow the steps below to change the default logo and background images for the User Console login page theme.

1. Back up and remove the default image file for the logo from the `/pentaho-server/pentaho-solutions/system/common-ui/resources/themes/<*theme-name*>/images` directory of the theme you want to change.

| **Ruby (default)** | `header_logo.svg`        |
| ------------------ | ------------------------ |
| **Crystal**        | `puc-login-logo.png`     |
| **Sapphire**       | `pentaho-logo-white.png` |

2\. Rename the new image file to match the name of the logo file that you are replacing, and then copy the new image file into the \`\pentaho-server\pentaho-solutions\system\common-ui\resources\themes\\<\*theme-name\*>\images\` directory.

3. Update the style definitions for your image. Navigate to the `\pentaho-server\pentaho-solutions\system\common-ui\resources\themes\<theme name>` directory for the theme you are changing and then open the `.css` file with a text editor.

| **Ruby (default)** | `globalRuby.css`     |
| ------------------ | -------------------- |
| **Crystal**        | `globalCrystal.css`  |
| **Sapphire**       | `globalSapphire.css` |

4\. Locate the \*\*\\#login-header-logo\*\* property, then adjust the dimensions and margin for the new image.

5. (Optional) You can back up and remove the background image file. If not replacing the background image, proceed to the next step.

   The background image file is located in the `\pentaho-server\pentaho-solutions\system\common-ui\resources\themes\<*theme-name*>\images` directory of the theme you want to change. Use the following table to locate your theme and image.&#x20;

   | **Ruby (default)** | `bg.svg`                |
   | ------------------ | ----------------------- |
   | **Crystal**        | `login-crystal-bg.jpeg` |
   | **Sapphire**       | `#0F2B5B`               |

   1. Rename the new background image file to match the name of the background file that you are replacing, and then copy the new image file into the \`\pentaho-server\pentaho-solutions\system\common-ui\resources\themes\\<\*theme-name\*>\images\` directory.
   2. Update the image dimensions for your background. Navigate to the `\server\pentaho-server\pentaho-solutions\system\common-ui\resources\themes\<*theme-name*>` directory and open the `.css` file with a text editor.
   3. Locate the **#login-background** property, then adjust the dimensions, position, and other properties for the background image.

6\. Save and close the file.

7. Clear the web browser cache and restart the server to see the new logo.

The default theme logo is removed, and your custom logo appears in its place. If you replaced the background image, the new background also appears. You can also use the same process to modify or replace the remaining elements on the login page.
