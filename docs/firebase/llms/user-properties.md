# Source: https://firebase.google.com/docs/analytics/user-properties.md.txt

iOS+AndroidWebFlutter  

<br />

User properties are attributes you define to describe segments of your user base, such as language preference or geographic location. These can be used to define[audiences](https://support.google.com/firebase/answer/6317509)for your app. This guide shows you how to set user properties in your app.

Analyticsautomatically logs some[user properties](https://support.google.com/analytics/answer/9268042); you don't need to add any code to enable them. If you need to collect additional data, you can set up to 25 different user properties per project. Note that user property names are case-sensitive and that setting two user properties whose names differ only in case results in two distinct user properties being logged.

You can't use a small set of user property names reserved by Google:

- **Age**
- **Gender**
- **Interest**

## Before you begin

Make sure that you've set up your project and can accessAnalyticsas described in[Get Started withAnalytics](https://firebase.google.com/docs/analytics/get-started?platform=web).

## Set user properties

You can setAnalyticsuser properties to describe the users of your app. You can make use of user properties by creating custom definitions, then using them to apply comparisons in your reports or as audience evaluation criteria.

To set a user property, follow these steps:

1. Create a custom definition for the user property in the[**Custom Definitions**page](https://console.firebase.google.com/project/_/analytics/userproperty)of*Analytics* in theFirebaseconsole. For more information, see[Custom dimensions and metrics](https://support.google.com/analytics/answer/10075209).
2. Set a user property in your app with the[`setUserProperty()`](https://firebase.google.com/docs/reference/js/analytics#setuserproperties)method.

The following example shows how to add a hypothetical "favorite food" property, which assigns the value in the string`food`to the active user:  

### Web

```javascript
import { getAnalytics, setUserProperties } from "firebase/analytics";

const analytics = getAnalytics();
setUserProperties(analytics, { favorite_food: 'apples' });https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/analytics-next/index/analytics_set_user_properties.js#L8-L11
```

### Web

```javascript
firebase.analytics().setUserProperties({favorite_food: 'apples'});https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/analytics/index.js#L38-L38
```
| **Note:** After the property is registered, it can take several hours for data collected with the property to be included in reports. When the new data is available, the user property can be used as a report filter or audience definition.

You can access this data from the[**Custom Definitions**page](https://console.firebase.google.com/project/_/analytics/userproperty)of*Analytics* in theFirebaseconsole. The page shows a list of user properties that you have defined for your app. You can use these properties in comparisons on many of the reports available inGoogle Analytics. Read more about the[dashboard](https://support.google.com/analytics/answer/11014767).
| **Note:** Data in theAnalyticsreporting dashboard refreshes periodically throughout the day.