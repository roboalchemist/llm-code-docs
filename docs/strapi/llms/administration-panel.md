# Administration panel

The admin panel is the back office of your Strapi application. From the admin panel, you will be able to manage content-types and write their actual content, but also manage users, both administrators and end users of your Strapi application.

### Modifying profile information (name, email, username)

1. Go to the *Profile* section of your profile.
2. Fill in the following options:

| Profile & Experience | Instructions                                      |
| -------------------- | ------------------------------------------------- |
| First name           | Write your first name in the textbox.             |
| Last name            | Write your last name in the textbox.              |
| Email                | Write your complete email address in the textbox. |
| Username             | (optional) Write a username in the textbox.       |

3. Click on the **Save** button.

### Changing account password

1. Go to the *Change password* section of your profile.
2. Fill in the following options:

| Password modification | Instructions                                |
| --------------------- | ------------------------------------------- |
| Current password      | Write your current password in the textbox. |
| Password              | Write the new password in the textbox.      |
| Password confirmation | Write the same new password in the textbox. |

3. Click on the **Save** button.

:::tip
You can click on the  icon for the passwords to be shown.
:::

### Choosing interface language

In the *Experience* section of your profile, select your preferred language using the *Interface language* dropdown.

:::note
Keep in mind that choosing an interface language only applies to your account on the admin panel. Other users of the same application's admin panel can use a different language.
:::

### Choosing interface mode (light, dark)

By default, the chosen interface mode is based on your browser's mode. You can however, in the *Experience* section of your profile, manually choose either the Light Mode or Dark Mode using the *Interface mode* dropdown.

:::note
Keep in mind that choosing an interface mode only applies to your account on the admin panel.
:::

### Resetting guided tour

In the *Guided tour* section of your profile, you can click the **Reset guided tour** button to reset the guided tour which is available in the homepage of the admin panel. It allows you to see again the guided tour of the admin panel if you closed it beforehand, and to follow again its various steps.

### Customizing the logo

**Path to configure the admin panel:**  *Settings > Global settings > Overview*

The default Strapi logos, displayed in the main navigation of a Strapi application and the authentication pages, can be modified.

1. Click on the upload area for *Menu logo* or *Auth logo*.
2. Upload your chosen logo, either by browsing files, drag & dropping the file in the right area, or by using a URL. The logo shouldn't be more than 750x750px. 
3. Click on the **Upload logo** button in the upload window.
4. Click on the **Save** button in the top right corner.

Once uploaded, the new logo can be replaced with another one , or reset  with the default Strapi logo or the logo set in the configuration files.

:::note
Both logos can also be customized programmatically via the Strapi application's configuration files (see [Admin panel customization](/cms/admin-panel-customization/logos)). However, the logos uploaded via the admin panel supersedes any logo set through the configuration files.
:::

## Usage

:::caution
In order to access the admin panel, your Strapi application must be launched, and you must be aware of the URL to its admin panel (e.g. `api.example.com/admin`).
:::

To access the admin panel:

1. Go to the URL of your Strapi application's admin panel.
2. Enter your credentials to log in.
3. Click on the **Login** button. You should be redirected to the homepage of the admin panel.

:::note
If you prefer or are required to log in via an SSO provider, please refer to the [Single Sign-On documentation](/cms/features/sso).
:::