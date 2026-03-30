# Source: https://www.elastic.co/docs/cloud-account/dark-mode

﻿---
title: Use dark mode in Kibana
description: The dark mode changes Kibana's default light appearance to a darker color theme. From the application header, you can turn on dark mode or synchronize...
url: https://www.elastic.co/docs/cloud-account/dark-mode
products:
  - Elastic Cloud Serverless
  - Kibana
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Stack: Generally available
---

# Use dark mode in Kibana
The dark mode changes Kibana's default light appearance to a darker color theme. From the application header, you can turn on dark mode or synchronize the color mode with your operating system settings.
<tip>
  If you're using Elastic Cloud, this setting only applies to the Kibana UI of your serverless projects and hosted deployments. If you'd like to change the Elastic Cloud Console color theme too, you must do so separately from its respective interface.
</tip>


## Change your color mode preferences

1. Open the user menu from the header.
2. Select **Appearance**.
   <note>
   On self-managed deployments of Kibana, this option is located on your profile page. To access it, select **Edit profile** from the header's user menu.
   </note>
3. Choose a color mode:
   - **Light**: The default color mode of Kibana
- **Dark**: The dark color mode of Kibana
- **System**: Synchronizes Kibana's color mode with your system settings
- **Space default**: Sets the color mode to the value defined in the [Space settings](https://www.elastic.co/docs/reference/kibana/advanced-settings#kibana-general-settings)
  <admonition title="Deprecated">
  The **Space default** option will be removed in a future version and automatically replaced with the System color mode.
  </admonition>
4. Select **Save changes**.
5. Refresh the page to apply the selected color mode.