# Source: https://firebase.google.com/docs/analytics/unity/properties.md.txt

# Source: https://firebase.google.com/docs/analytics/cpp/properties.md.txt

# Source: https://firebase.google.com/docs/analytics/unity/properties.md.txt

# Source: https://firebase.google.com/docs/analytics/cpp/properties.md.txt

<br />

User properties are attributes you define to describe segments of your user base, such as language preference or geographic location.

Analyticsautomatically logs some[user properties](https://support.google.com/analytics/answer/9268042); you don't need to add any code to enable them. If your app needs to collect additional data, you can set up to 25 differentAnalyticsuser properties in your app.

## Before you begin

Make sure that you've set up your project and can accessAnalyticsas described in[Get Started withAnalyticsfor C++](https://firebase.google.com/docs/analytics/cpp/start#before_you_begin).

## Set user properties

You can setAnalyticsuser properties to describe the users of your app. You can analyze behaviors of various user segments by applying these properties as filters to your reports.

Set a user property as follows:

1. [Register](https://support.google.com/firebase/answer/6317519?hl=en&ref_topic=6317489#create-property)the property in the**Analytics** tab of the[Firebaseconsole](https://console.firebase.google.com/).

2. Add code to set anAnalyticsuser property with the[`SetUserProperty()`](https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#setuserproperty)method. You can use the name and value of your choosing for each property.

The following example shows adding a hypothetical favorite food property, which assigns the value in the string`mFavoriteFood`to the active user:  

```c++
SetUserProperty("favorite_food", mFavoriteFood);
```
| **Note:** Once the property is registered, it can take several hours for data collected with the property to be included in reports. When the new data is available, the user property can be used as a report filter.

You can access this data as follows:

1. In the[Firebaseconsole](https://console.firebase.google.com/), open your project.
2. Select**Analytics** from the menu to view theAnalyticsreporting dashboard.

The**User Properties** tab shows a list of user properties that you have defined for your app. You can use these properties as a filter on many of the reports available inGoogle Analytics. Read more about the[Analyticsreporting dashboard](https://support.google.com/analytics/answer/11014767)in the Firebase Help Center.
| **Note:** Data in theAnalyticsreporting dashboard refreshes periodically throughout the day.