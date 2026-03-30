# Source: https://learn.microsoft.com/en-us/power-apps/mobile/run-powerapps-on-mobile

Title: Install the Power Apps mobile app - Power Apps

URL Source: https://learn.microsoft.com/en-us/power-apps/mobile/run-powerapps-on-mobile

Markdown Content:
If you're not signed up for Power Apps, [sign up for free](https://make.powerapps.com/signup?redirect=marketing&email=). Then choose the download link or scan a QR code to download Power Apps mobile.

| iOS | Android | Windows |
| --- | --- | --- |
| [![Image 1: Download Power Apps from the Apple App Store.](https://learn.microsoft.com/en-us/power-apps/mobile/media/app-store-icon.png)](https://itunes.apple.com/app/powerapps/id1047318566?mt=8) | [![Image 2: Download Power Apps from Google Play.](https://learn.microsoft.com/en-us/power-apps/mobile/media/play-store-android-icon.png)](https://play.google.com/store/apps/details?id=com.microsoft.msapps) | [![Image 3: Download Power Apps from Windows Store.](https://learn.microsoft.com/en-us/power-apps/mobile/media/windows-store-icon.png)](https://www.microsoft.com/store/apps/9MVC8P1Q3B29) |
| ![Image 4: Download Power Apps from the Apple App Store using the QR code.](https://learn.microsoft.com/en-us/power-apps/mobile/media/qr-code-ios.png) | ![Image 5: Download Power Apps from Google Play using the QR code.](https://learn.microsoft.com/en-us/power-apps/mobile/media/qr-code-android.png) | ![Image 6: Download Power Apps from Windows Store using QR the code.](https://learn.microsoft.com/en-us/power-apps/mobile/media/qr-code-windows.png) |

Review the following privileges and supported devices to run Power Apps Mobile app:

*   [Required privileges](https://learn.microsoft.com/en-us/dynamics365/mobile-app/set-up-dynamics-365-for-phones-and-dynamics-365-for-tablets#required-privileges)
*   [Supported platforms for running apps using the Power Apps mobile app](https://learn.microsoft.com/en-us/power-apps/limits-and-config#supported-platforms-for-running-apps-by-using-the-power-apps-mobile-app).

Open Power Apps on your mobile device, and sign in by using your Azure Active Directory credentials.

If you have the Microsoft Authenticator app installed on your mobile device, enter your username when prompted, and then approve the notification sent to your device. If you run into issues signing in, see [Troubleshoot issues for Power Apps mobile app](https://learn.microsoft.com/en-us/power-apps/mobile/powerapps-mobile-troubleshoot).

![Image 7: Sign in to Power Apps.](https://learn.microsoft.com/en-us/power-apps/mobile/media/powerapps_mobile_app_signin_screen.png)

When you create an app, or someone shares an app with you—either a [canvas app](https://learn.microsoft.com/en-us/power-apps/maker/#canvas-apps) or [model-driven](https://learn.microsoft.com/en-us/power-apps/maker/#model-driven-apps) app—you can run that app on Power Apps mobile.

Note

To see a model-driven app in the list of apps on Power Apps mobile, you need to have a [predefined security role](https://learn.microsoft.com/en-us/power-platform/admin/database-security#predefined-security-roles) in the environment that the app is in. If a predefined security role is assigned to a user using a Dataverse team, you need to use an Azure Active Directory (AAD) group team. Users will not see model-driven apps if a predefined security role is assigned using a Dataverse owner team.

![Image 8: Power Apps mobile user interface with model-driven and canvas apps.](https://learn.microsoft.com/en-us/power-apps/mobile/media/powerappsmobile-1.png)

Legend:

1.   **Model-driven apps**
2.   **Canvas apps**

The apps that you used recently will show on the default screen when you sign in to Power Apps mobile.

The **Home** is the default screen when you sign in. It shows the apps that you used recently and the apps that have marked as favorites.

![Image 9: Default Home screen.](https://learn.microsoft.com/en-us/power-apps/mobile/media/default-home-screen.png)

If you don't have any apps, then when you sign in, you will land on the **All apps** screen. The list of apps is organized in alphabetical order. Type in an app name in the search bar to find an app.

![Image 10: Filter and find apps.](https://learn.microsoft.com/en-us/power-apps/mobile/media/app-list-2.png)

1.   **Settings**: Access app settings and sign out.
2.   **Search**: Use the search to search for apps. When you run a search, it will only search for apps that are on the screen you're on.
3.   **Favorites** (canvas apps only): Displays canvas apps that you have pinned to favorites.
4.   **Recent apps**: Displays both model-driven and canvas apps that you have recently used.
5.   **Home**: Displays favorite apps and recently accessed apps sorted by open date.
6.   **All apps**: Displays all canvas apps and model-driven apps to which you have access, including apps you created and apps that others shared with you.
7.   **More** (canvas apps only): Displays featured and sample apps.
8.   **Details**: View information about the app including run the app, add a shortcut for the app, and add the app to favorites.
9.   **Sort apps**: You can short by the app name or modified date. 

You can add canvas and model-driven apps to your list of favorite apps.

*   Swipe left and then select **Favorite**. A yellow star will appear next to app name when it's added to favorites. You can also select **Details**![Image 11: Details button.](https://learn.microsoft.com/en-us/power-apps/mobile/media/detailsbutton.png) and then add the app to favorites.

![Image 12: Add to list of favorites.](https://learn.microsoft.com/en-us/power-apps/mobile/media/add-to-favs-1-1.png)

*   To remove the app from the list, swipe left again and then select **Unfavorite**.

![Image 13: Remove the app from the list.](https://learn.microsoft.com/en-us/power-apps/mobile/media/add-to-favs-1-2.png)

You can sort both canvas apps and model-driven apps. You can sort apps alphabetically by name or by modified date. The sort option is available on **Home**, **All apps**, **Featured apps**, and **Sample apps** screen.

![Image 14: Sort menu.](https://learn.microsoft.com/en-us/power-apps/mobile/media/sort-apps-iphone.png)

If you know the name of the app that you want to run, then use search to quickly find the app. You can search for both canvas apps and model-driven apps.

To find an app, enter the app name in the search field. The app will only search for apps that are on the screen you're on.

![Image 15: Search for your app.](https://learn.microsoft.com/en-us/power-apps/mobile/media/search_apps-1.png)

On the **Home**, **All apps** or any other screen with a list of apps, swipe down to refresh the app list.

![Image 16: Refresh the app list.](https://learn.microsoft.com/en-us/power-apps/mobile/media/refesh-apps-iphone.png)

You can add a shortcut for both canvas apps and model-driven apps to the home screen of your device for quick access.

1.   On the app that you want to create a shortcut for, swipe to the right and select **Shortcut**.

![Image 17: Select shortcut.](https://learn.microsoft.com/en-us/power-apps/mobile/media/add-shortcut-iphone.png)

2.   Select ![Image 18: Pin an app on iPhone button.](https://learn.microsoft.com/en-us/power-apps/mobile/media/add-to-home-button.png).

![Image 19: Pin an app on iPhone.](https://learn.microsoft.com/en-us/power-apps/mobile/media/pin_to_home_1.png)

3.   Scroll down and select **Add to Home Screen**

![Image 20: Add to Home Screen.](https://learn.microsoft.com/en-us/power-apps/mobile/media/pin_to_home_2.png)

4.   Select **Add**.

![Image 21: Select Add to add to Home screen.](https://learn.microsoft.com/en-us/power-apps/mobile/media/pin_to_home_3.png)

Note

For iOS devices that have multiple browsers installed, use Safari when pinning an app to home.

The Power Apps mobile app is now integrated with Siri shortcuts, which gives you the ability to add a shortcut to the Home screen, launch apps with Siri, and create new workflows. For more information on how shortcuts work on iOS, see [Shortcuts User Guide](https://support.apple.com/guide/shortcuts/welcome/ios). This feature requires Power Apps mobile version 3.20092.x or later.

Users on iOS 14 or later can use Siri Shortcuts to pin an app to the home screen. The new experience works for both model-driven and canvas apps. When you add a Siri shortcut, the app is added to the iOS **Shortcuts** app and from there you can add the app to your home screen.

1.   On the app that you want add a shortcut for, swipe to the right and select **Shortcut**.

![Image 22: Select shortcut.](https://learn.microsoft.com/en-us/power-apps/mobile/media/add-shortcut-iphone.png)

2.   Add a custom phrase to open the app using voice commands and then select **Add to Siri**.

![Image 23: Select Add to Siri.](https://learn.microsoft.com/en-us/power-apps/mobile/media/add-shortcut-1.png)

3.   The app is added to the **Shortcuts** app on your mobile device. Open the **Shortcuts** app and select the ellipsis (...) above the app name.

![Image 24: Select the ellipsis to add a shortcut.](https://learn.microsoft.com/en-us/power-apps/mobile/media/add-short-2.png)

4.   Select **Add to Home Screen**.

![Image 25: Select Add to Home Screen.](https://learn.microsoft.com/en-us/power-apps/mobile/media/add-to-homescreen.png)

5.   On the upper right corner, select **Add** and then select **Done**.

![Image 26: Select Add.](https://learn.microsoft.com/en-us/power-apps/mobile/media/add-shortcut-3.png)

6.   Go to your home screen to find the pinned app.

![Image 27: App shortcut on home screen.](https://learn.microsoft.com/en-us/power-apps/mobile/media/add-shortcut-4.png)

You can customize the shortcut icon but it is limited to the customization options in iOS. For more information, go to [Modify shortcut icons](https://support.apple.com/guide/shortcuts/modify-shortcut-icons-apd5ad5a2128/ios).

Select the ellipsis (...) on the app tile, select **Pin to Home**, and then follow the instructions that appear.

![Image 28: Pin an app.](https://learn.microsoft.com/en-us/power-apps/mobile/media/pin_to_home.png)

By default, only production model-driven apps are shown in the list of apps.

To see model-driven apps from non-production environments, select the **Settings** menu ![Image 29: Settings button](https://learn.microsoft.com/en-us/power-apps/mobile/media/settings_icon-1.png), and then turn on **Show non-production apps**. Follow the instructions that appear.

![Image 30: Non-production apps toggle.](https://learn.microsoft.com/en-us/power-apps/mobile/media/non_prod_toggle.png)

To run an app on a mobile device, select the app tile from the **Home** or **All apps** screen in the Power Apps mobile app.

Considerations when opening apps:

*   If you created the app, you see the app in the **Home** page >**Recommended apps** section.
*   If you didn't create the app and the app is shared with you, use search box in the **Apps** screen to find the app the first time. After you open the app, it shows up on the **Home** screen the next time you access it.

If this is the first time you're running a canvas app by using Power Apps mobile, a screen shows the swipe gestures.

Use your finger to swipe from the left edge of the app to the right to close an app. On Android devices, you can also press the Back button and then confirm that you intended to close the app.

![Image 31: Close an app.](https://learn.microsoft.com/en-us/power-apps/mobile/media/swipe.gif)

![Image 32: Pinch to zoom.](https://learn.microsoft.com/en-us/power-apps/mobile/media/pinchtozoom.jpg)

If an app requires a connection to a data source or permission to use the device's capabilities (such as the camera or location services), you must give consent before you can use the app. Typically, you're prompted only the first time you run the app.

![Image 33: Give consent to a canvas app.](https://learn.microsoft.com/en-us/power-apps/mobile/media/give_consent_canvas.jpg)

The following image shows an example of a model-driven app screen after you've signed in. To learn how to use model-driven apps running on Power Apps mobile, go to [Use model-driven apps on Power Apps mobile](https://learn.microsoft.com/en-us/power-apps/mobile/use-custom-model-driven-app-on-mobile).

![Image 34: Model-driven app home page.](https://learn.microsoft.com/en-us/power-apps/mobile/media/model-driven-app-opened.png)

If an app requires a connection to a data source or permission to use the device's capabilities (such as the camera or location services), you must give consent before you can use the app. Typically, you're prompted only the first time you use the app.

![Image 35: Give consent.](https://learn.microsoft.com/en-us/power-apps/mobile/media/give_consent.png)

Select the site map ![Image 36: Site map icon.](https://learn.microsoft.com/en-us/power-apps/mobile/media/pa_mobile_sitemap_icon.png), and then select **Apps**.

![Image 37: Close a model-driven app.](https://learn.microsoft.com/en-us/power-apps/mobile/media/pa_mobile_close_app.png)

The table below outlines which other mobile apps you can use to run your app.

| **Mobile App** | **Apps you can run** |
| --- | --- |
| [Power Apps mobile](https://learn.microsoft.com/en-us/power-apps/mobile/run-powerapps-on-mobile) (covered in this topic) | * [Model-driven apps](https://learn.microsoft.com/en-us/power-apps/maker/#model-driven-apps) * [Canvas apps](https://learn.microsoft.com/en-us/power-apps/maker/#canvas-apps) * [Dynamics 365 Marketing](https://learn.microsoft.com/en-us/dynamics365/marketing/help-hub) * [Dynamics 365 Customer Service](https://learn.microsoft.com/en-us/dynamics365/customer-service/help-hub) |
| [Power Apps for Windows](https://learn.microsoft.com/en-us/power-apps/mobile/windows-app-install) | * [Model-driven apps](https://learn.microsoft.com/en-us/power-apps/maker/#model-driven-apps) * [Canvas apps](https://learn.microsoft.com/en-us/power-apps/maker/#canvas-apps) |
| [Dynamics 365 for phone and tablets](https://learn.microsoft.com/en-us/dynamics365/mobile-app/overview) | * [Microsoft Dynamics 365 Customer Engagement (on-premises)](https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/overview) **Note**: Dynamics 365 for Tablets is deprecated, and won't be supported in 2023. |
| [Dynamics 365 Sales Mobile](https://learn.microsoft.com/en-us/dynamics365/sales/sales-mobile/dynamics-365-sales-mobile-app) | * [Dynamics 365 Sales](https://learn.microsoft.com/en-us/dynamics365/sales/help-hub) |
| [Field Service Mobile](https://learn.microsoft.com/en-us/dynamics365/field-service/mobile-power-app-overview) | * [Field Service (Dynamics 365)](https://learn.microsoft.com/en-us/dynamics365/field-service/overview) |

Power Apps mobile app is available to users in Azure global cloud and also in the following regions:

*   [US Department of Defense (US DoD)](https://learn.microsoft.com/en-us/azure/azure-government/documentation-government-overview-dod)
*   [US Government Community Cloud (GCC) High](https://learn.microsoft.com/en-us/power-platform/admin/microsoft-dynamics-365-government#about-dynamics-365-us-government-environments-and-products)
*   [US Government Community Cloud (GCC)](https://learn.microsoft.com/en-us/power-platform/admin/microsoft-dynamics-365-government#about-dynamics-365-us-government-environments-and-products)
*   [China Sovereign Cloud](https://learn.microsoft.com/en-us/power-platform/admin/about-microsoft-cloud-china)

Mobile users have an option to select their region on Power Apps mobile app sign in screen.

![Image 38: Choose a region when signing in to Power Apps mobile app](https://learn.microsoft.com/en-us/power-apps/mobile/media/select_user_region_mobile_app.jpg)

More information:

*   [Azure Government documentation](https://learn.microsoft.com/en-us/azure/azure-government/)
*   [Dynamics 365 US Government](https://learn.microsoft.com/en-us/power-platform/admin/microsoft-dynamics-365-government#about-dynamics-365-us-government-environments-and-products)
*   [Power Platform and Dynamics 365 apps in China](https://learn.microsoft.com/en-us/power-platform/admin/about-microsoft-cloud-china)

Power Apps mobile app for Android registers for a system event that is broadcasted when the device is finished booting. Power Apps mobile app for Android registers for this event to support push notifications sent to the app.

Power Apps mobile app and [wrapped native mobile apps](https://learn.microsoft.com/en-us/power-apps/maker/common/wrap/overview) may use device sensors, such as the device accelerometer, to respond to user actions. For example, [wrapped native mobile apps](https://learn.microsoft.com/en-us/power-apps/maker/common/wrap/overview) would automatically show the app menu when the user shakes the device.

[Use model-driven apps on Power Apps mobile](https://learn.microsoft.com/en-us/power-apps/mobile/use-custom-model-driven-app-on-mobile)

[Troubleshoot issues for Power Apps mobile](https://learn.microsoft.com/en-us/powerapps/user/powerapps_mobile_troubleshoot)
