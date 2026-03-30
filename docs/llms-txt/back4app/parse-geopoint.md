# Source: https://docs-containers.back4app.com/docs/android/data-objects/parse-geopoint.md

---
title: Using GeoPoints
slug: docs/android/data-objects/parse-geopoint
description: In this tutorial you'll learn how to use Parse GeoPoints on your Android app to find out what user is closest to another user or which places are closest to a user
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-13T16:21:31.118Z
updatedAt: 2025-01-16T20:44:49.451Z
---

# Using Parse GeoPoints on your Android app

## Introduction

Parse allows you to associate real-world latitude and longitude coordinates with an object. Adding a **ParseGeoPoint** to a **ParseUser**, you will be able to easily find out which user is closest to another, show the locations of the users of your app and also store the user’s location information, among other possibilities.

You can also associate a **ParseGeoPoint** to any **ParseObject**. For example, if your app is associated with a store with physical affiliates, you will be able to create an activity to show the location of those stores or to show the user which store is closest to him. Another example of this association usage: if your app is a game in which you created ParseObjects to represent characters, adding ParseGeoPoints to these characters would allow them to be shown along the player’s path.

This tutorial explains how to use some features of ParseGeoPoint through Back4App.

After following this tutorial, you will be able to do this:



::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/vq11izFSiACJsleR19j_A_image.png" signedSrc size="50" width="414" height="827" position="center" caption}

:::hint{type="success"}
At any time, you can access the complete Android Project built with this tutorial at our [**GitHub repository**](https://github.com/back4app/android-geopoints-tutorial).
:::

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, we need:**

- [**Android Studio**](https://developer.android.com/studio/index.html)
- An User Registration - Login App created on Back4App.
  - **Note:&#x20;**&#x46;ollow the User Registration - login tutorial to learn how to create an User Registration - Login App on Back4App. .
- A real device running Android 4.0 (Ice Cream Sandwich) or newer.
  - **Note:** It is very likely that the app built with this tutorial won't run as expected in a virtual device and may even crush because it might not retrieve the current location of the virtual device. So we strongly recommend that you use a real device to run it.
:::

## 1 - Set up Google API Key

To show the location you stored in a ParseGeoPoint, you will need to display a Map. To do that, it’s interesting to use a Google Maps Activity. In order to create a Google Maps Activity in Android Studio, do the following:

1. Go to File > New > Google > Google Maps Activity. Then, automatically, it will create a java file, a layoutfile and a values file corresponding to the Google Maps Activity that you have created.
2. Go to the created values file (you can do this by accessing app > res > values > google\_maps\_api.xml), as shown in the image below. This file will give you some instructions on how to get a Google Maps API Key. Basically, you should open the link shown in the image.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/pQrS9WvLGBK-Xl2iOpMKp_image.png)

&#x20;    3\. After opening it, you should login in your Google Account, select the Create a project option and click on Continue. While creating the project, Google will enable your API.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/qw5OD2Yy4C5hDUQCkSx40_image.png)

&#x20;    4\. After your API is enabled, you will be able to get an API key, to do so click on

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/c1tRU2IbSSgv0CV2pn5lv_image.png)

&#x20;    5\. Then, your key will be created and you can copy it and paste it in the values file that lead you to this page, in the place where its written YOUR KEY HERE.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/vKHMI6Y2UQRegSW7S1z1B_image.png)

&#x20;    6\. It’s important to have the uses-permission below in your AndroidManifest.xml file. If you created the Google Maps Activity following the instructions above, then one of these permissions should already be in your manifest, anyway, you’ll need both of them for your app to work properly, so check if they are in your AndroidManifest.xml file, otherwise, insert them on it.

```xml
1   <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
2   <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
```

&#x20;    7\. At the beginning of your MapsActivity, import the following:

```java
1   // Android Dependencies
2   import android.Manifest;
3   import android.app.ProgressDialog;
4   import android.content.Context;
5   import android.content.DialogInterface;
6   import android.content.Intent;
7   import android.content.pm.PackageManager;
8   import android.location.Location;
9   import android.location.LocationManager;
10  import android.support.annotation.NonNull;
11  import android.support.v4.app.ActivityCompat;
12  import android.support.v4.app.FragmentActivity;
13  import android.os.Bundle;
14  import android.util.Log;
15  import android.view.View;
16  import android.widget.Button;
17  // Google Maps Dependencies
18  import com.google.android.gms.maps.CameraUpdateFactory;
19  import com.google.android.gms.maps.GoogleMap;
20  import com.google.android.gms.maps.OnMapReadyCallback;
21  import com.google.android.gms.maps.SupportMapFragment;
22  import com.google.android.gms.maps.model.BitmapDescriptorFactory;
23  import com.google.android.gms.maps.model.LatLng;
24  import com.google.android.gms.maps.model.MarkerOptions;
25  // Parse Dependencies
26  import com.parse.FindCallback;
27  import com.parse.ParseException;
28  import com.parse.ParseGeoPoint;
29  import com.parse.ParseQuery;
30  import com.parse.ParseUser;
31  // Java dependencies
32  import java.util.List;
```

## 2 - Set up Back4App Dashboard to save user’s location

1. Go to [**Back4App website&#x20;**](https://www.back4app.com/)login, find your app and open its Dashboard.
2. Go to Core > Browser > User, as shown in the image below.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/EM9imOEAfCvIhzCYgKKEg_image.png)

&#x20;    3\. Now, create a new column to save the user’s location. To do so, click on the Edit button in the top right, as shown below.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/8ov3mPji-5pyg0Bn-8B0j_image.png)

&#x20;    4\. Then, click on Add a column.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/5l5kpmezZk2xlablyDI8-_image.png)

&#x20;    5\. In the field What type of data do you want to store?, choose the GeoPoint option.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/N7bLZpTRSeZTIf_yvB0Bs_image.png)

&#x20;    6\. In the field What should we call it?, type “**Location**”.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/yXvBMPYZGCduNr_181WsT_image.png)

&#x20;    7\. So, click on Add column, as shown in the image below.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/hJohTYLWB1BqOyMERptvr_image.png)

&#x20;    8\. Now, your app is able to store location data of users and your User Class in your Back4pp Dashboard should look like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/eNUxXQn3_1AzdMj7dcQlN_image.png)

## 3 - Save users current location in your Back4pp Dashboard

1. Open your MapsActivity and inside the public class MapsActivity define an int called REQUEST\_LOCATION with value 1 and a locationManager, as in the following code.

```java
1  private static final int REQUEST_LOCATION = 1;
2  LocationManager locationManager;
```

&#x20;    2\. In the onCreate method create the locationManager, as in the following code.

```java
1 locationManager = (LocationManager)getSystemService(Context.LOCATION_SERVICE);
```

&#x20;    3\. To save user’s location in your Back4pp Dashboard, simply implement the following method and call it in your onMapReady method.

```java
1    private void saveCurrentUserLocation() {
2     // requesting permission to get user's location
3     if(ActivityCompat.checkSelfPermission(UsersActivity.this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(UsersActivity.this, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED){
4         ActivityCompat.requestPermissions(UsersActivity.this, new String[]{android.Manifest.permission.ACCESS_FINE_LOCATION}, REQUEST_LOCATION);
5     }
6     else {
7         // getting last know user's location
8         Location location = locationManager.getLastKnownLocation(LocationManager.NETWORK_PROVIDER);
9
10        // checking if the location is null
11        if(location != null){
12            // if it isn't, save it to Back4App Dashboard
13            ParseGeoPoint currentUserLocation = new ParseGeoPoint(location.getLatitude(), location.getLongitude());
14
15            ParseUser currentUser = ParseUser.getCurrentUser();
16
17            if (currentUser != null) {
18                currentUser.put("Location", currentUserLocation);
19                currentUser.saveInBackground();
20            } else {
21                // do something like coming back to the login activity
22            }
23        }
24        else {
25            // if it is null, do something like displaying error and coming back to the menu activity
26        } 
27    }
28   }
```

&#x20;    4\. It’s really important to implement the following method in order to make saveCurrentUserLocation method works.

```java
1    @Override
2    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults){
3     super.onRequestPermissionsResult(requestCode, permissions, grantResults);
4
5     switch (requestCode){
6         case REQUEST_LOCATION:
7             saveCurrentUserLocation();
8             break;
9     }
10   } 
```

## 4 - Retrieve user’s location

To retrieve user’s location, you’ll need to find who is the current user, save its location and then return the location saved in your Back4App Dashboard.
In order to do that, implement the following method in your MapsActivity and call it when needed.

```java
1    /* saving the current user location, using the saveCurrentUserLocation method of Step 3, to avoid
2    null pointer exception and also to return the user's most current location */
3    saveCurrentUserLocation();
4    private ParseGeoPoint getCurrentUserLocation(){
5
6    // finding currentUser
7    ParseUser currentUser = ParseUser.getCurrentUser();
8
9    if (currentUser == null) {
10        // if it's not possible to find the user, do something like returning to login activity
11    }
12    // otherwise, return the current user location
13    return currentUser.getParseGeoPoint("Location");
14
15  }
```

## 5 - Showing current user’s location in map

To display user’s location in the map, you’ll need to retrieve user’s location and then create a marker in the map using the information retrieved.
In order to do that, implement the following method in your MapsActivity and call it in the onMapReady method.

```java
1   private void showCurrentUserInMap(final GoogleMap googleMap){
2
3       // calling retrieve user's location method of Step 4
4       ParseGeoPoint currentUserLocation = getCurrentUserLocation();
5
6       // creating a marker in the map showing the current user location
7       LatLng currentUser = new LatLng(currentUserLocation.getLatitude(), currentUserLocation.getLongitude());
8       googleMap.addMarker(new MarkerOptions().position(currentUser).title(ParseUser.getCurrentUser().getUsername()).icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_RED)));
9
10      // zoom the map to the currentUserLocation
11      googleMap.animateCamera(CameraUpdateFactory.newLatLngZoom(currentUser, 5));
12  }
```

## 6 - Finding the closest user to the current one

1. Now that you have a bunch of users with spatial coordinates associated, it would be good to find out which user is closest to another. This can be done by using a ParseQuery. First, you’ll need to create a ParseUser query and restrict it with whereNear, informing in which column of the User class on Back4App you are doing the query (in this case the “Location” column) and also inform the reference ParseGeoPoint for the query from which will be found the closest user (in this case the ParseGeoPoint associated to the current user location). The following code do that:

```java
1   ParseQuery<ParseUser> query = ParseUser.getQuery();
2   query.whereNear("Location", getCurrentUserLocation());
```

&#x20;    2\. You can limit the number of results of this query adding to it the restriction setLimit. By default, results are limited to 100. As the whereNear restriction will make the query retrieve an array of users ordered by distance (nearest to farthest) from currentUserLocation, setting the limit of close users to find to the number 2, the list of results of the query will only have two users: the current and the closest user from him. The following code set the limit of results to 2:

```java
1  query.setLimit(2);

```

&#x20;    3\. Now that you restricted your query, let’s retrieve its results. In order to do that, you will call a findInBackground method and pass as argument a List of users, in which it’ll be stored the results of the query and also a ParseException to handle errors. To avoid errors, don’t forget to clear cached results after the query run. The following code do that:

```java
1   query.findInBackground(new FindCallback<ParseUser>() {
2      @Override  public void done(List<ParseUser> nearUsers, ParseException e) {
3          if (e == null) {
4            // do something with the list of results of your query
5          } else {
6              // handle the error
7          }
8      }
9     });
10    ParseQuery.clearAllCachedResults();
11  }
```

&#x20;    4\. If no error occurs, you’ll have in the nearUsers list the two closest users to the current user (the actual current user and the closest user from him), now you’ll only have to find who isn’t the current user. To do that, inside the if (e == null) block use the following code:

```java
1   // avoiding null pointer
2   ParseUser closestUser = ParseUser.getCurrentUser();
3   // set the closestUser to the one that isn't the current user
4   for(int i = 0; i < nearUsers.size(); i++) {
5   if(!nearUsers.get(i).getObjectId().equals(ParseUser.getCurrentUser().getObjectId())) {
6       closestUser = nearUsers.get(i);
7   }
8  }
```

&#x20;    5\. Now that you know who is the closest user to the current one you can mesure the distance between them using the distanceInKilometersTo method. In order to do that, use the following code:

```java
1  // finding and displaying the distance between the current user and the closest user to him
2  double distance = getCurrentUserLocation().distanceInKilometersTo(closestUser.getParseGeoPoint("Location"));
3  alertDisplayer("We found the closest user from you!", "It's " + closestUser.getUsername() + ". \nYou are " + Math.round (distance * 100.0) / 100.0  + " km from this user.");

```

:::hint{type="info"}
The alertDisplayer method used above, is the following:
:::

```java
1   private void alertDisplayer(String title,String message){
2      android.app.AlertDialog.Builder builder = new android.app.AlertDialog.Builder(UsersActivity.this)
3              .setTitle(title)
4              .setMessage(message)
5              .setPositiveButton("OK", new DialogInterface.OnClickListener() {
6                  @Override
7                  public void onClick(DialogInterface dialog, int which) {
8                      dialog.cancel();
9                  }
10             });
11     android.app.AlertDialog ok = builder.create();
12     ok.show();
13  }
```

&#x20;    6\. You can also show both users in the map, using the following code:

```java
1  // showing current user in map, using the method implemented in Step 5
2  showCurrentUserInMap(mMap);
3  // creating a marker in the map showing the closest user to the current user location, using method implemented in Step 4
4  LatLng closestUserLocation = new LatLng(closestUser.getParseGeoPoint("Location").getLatitude(), closestUser.getParseGeoPoint("Location").getLongitude());
5  googleMap.addMarker(new MarkerOptions().position(closestUserLocation).title(closestUser.getUsername()).icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_GREEN)));
6  // zoom the map to the currentUserLocation
7  googleMap.animateCamera(CameraUpdateFactory.newLatLngZoom(closestUserLocation, 3));
```

The complete method that executes all 6 steps above is the following:

```java
1   private void showClosestUser(final GoogleMap googleMap){
2       ParseQuery<ParseUser> query = ParseUser.getQuery();
3       query.whereNear("Location", getCurrentUserLocation());
4       // setting the limit of near users to find to 2, you'll have in the nearUsers list only two users: the current user and the closest user from the current
5       query.setLimit(2);
6       query.findInBackground(new FindCallback<ParseUser>() {
7           @Override  public void done(List<ParseUser> nearUsers, ParseException e) {
8               if (e == null) {
9                   // avoiding null pointer
10                  ParseUser closestUser = ParseUser.getCurrentUser();
11                  // set the closestUser to the one that isn't the current user
12                  for(int i = 0; i < nearUsers.size(); i++) {
13                      if(!nearUsers.get(i).getObjectId().equals(ParseUser.getCurrentUser().getObjectId())) {
14                          closestUser = nearUsers.get(i);
15                      }
16                  }
17                  // finding and displaying the distance between the current user and the closest user to him, using method implemented in Step 4
18                  double distance = getCurrentUserLocation().distanceInKilometersTo(closestUser.getParseGeoPoint("Location"));
19                  alertDisplayer("We found the closest user from you!", "It's " + closestUser.getUsername() + ". \n You are " + Math.round (distance * 100.0) / 100.0  + " km from this user.");
20                  // showing current user in map, using the method implemented in Step 5
21                  showCurrentUserInMap(mMap);
22                  // creating a marker in the map showing the closest user to the current user location
23                  LatLng closestUserLocation = new LatLng(closestUser.getParseGeoPoint("Location").getLatitude(), closestUser.getParseGeoPoint("Location").getLongitude());
24                  googleMap.addMarker(new MarkerOptions().position(closestUserLocation).title(closestUser.getUsername()).icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_GREEN)));
25                  // zoom the map to the currentUserLocation
26                  googleMap.animateCamera(CameraUpdateFactory.newLatLngZoom(closestUserLocation, 3));
27              } else {
28                  Log.d("store", "Error: " + e.getMessage());
29              }
30          }
31      });
32      ParseQuery.clearAllCachedResults();
33  }
```

## 7 - Set up Back4App to associate ParseGeoPoint to ParseObjects

Supose that the example app you are builiding is associated with a group of stores with physical affiliates. It would be interesting to show all the physical affiliates of this store in the map. In order to do so create a Stores class on Back4pp Dashboard, save the existing stores as ParseObjects, their locations and after that the app will be able to query the physical affiliates and display their possitions on the map. The following steps will help you with that.

&#x20;    1 . Go to [**Back4App website**](https://www.back4app.com/), login, find your app and open its Dashboard.
&#x20;    2\. Go to Core > Browser > Create a class, as shown in the image below.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/MhVphU5R_RReJsrBy3228_image.png)

&#x20;    3\. In the field What type of class do you need?, choose the Custom option.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/GrPKqZY1CNezwx16-9KgY_image.png)

&#x20;    4\. In the field What should we call it?, type “Stores” and then click on Create classbutton.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ZWRMkTxTiXy99xR1Gt7NJ_image.png)

&#x20;    5\. Then a new class called “Stores” will be shown and you should insert 2 columns on it: a collumn with data type String called Name, as well as another column with data type GeoPoint called Location. If you don’t remember how to create a column, go back to Step 2, there it’s explained how to create a column at Back4App Dashboard. Your class should end up like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/M6bFQfcB0jl9b0aBBRFT3_image.png)

&#x20;    6\. Now, fill this class with information. To do so, click on Add a row button in the menu on the top right or in the middle of the page, as shown in the image below.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/0bql9F58RsmBcS1il3vRg_image.png)

&#x20;    7\. Then fill the row with the informations required: the name of the store and its latitude and longitude. After inserting some data, your Stores class should look like the image below. If you want to insert more data, you can click on the Add a row button on the top, or in the + button bellow the last row of data.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/dUBM-pQN-2Jye_YyQJ6uA_image.png)

Now you are ready to use the location information of the stores in your app.

## 8 - Display all the stores location on Map

&#x20;    1\. You can show all the stores you added to your class on the MapsActivity by using a ParseQuery. First, you’ll need to create a ParseObject query, informing the name of the Back4pp Dashboard class you want to query (in this case the “Stores” class), and restrict it with whereExists, informing the column of the Store class on Back4App you are doing the query (in this case the “Location” column). The following code do that:

1.

```java
1  ParseQuery<ParseObject> query = ParseQuery.getQuery("Stores");
2  query.whereExists("Location");
```

&#x20;    2\. Now that you restricted your query, let’s retrieve its results. In order to do that, you will call a findInBackground method and pass as argument a List of stores, in which it’ll be stored the results of the query and also a ParseException to handle errors. The whereExists restriction will make only the ParseObjects of the class that have a ParseGeoPoint associated to them indicating their location be stored in the list of stores. To avoid errors, don’t forget to clear cached results after the query run. The following code do that:

```java
1   query.findInBackground(new FindCallback<ParseObject>() {
2      @Override  public void done(List<ParseObject> stores, ParseException e) {
3          if (e == null) {
4            // do something with the list of results of your query
5          } else {
6              // handle the error
7          }
8      }
9     });
10    ParseQuery.clearAllCachedResults();
11  }
```

&#x20;    3\. If no error occurs, you’ll have in the stores list all the stores with location associated, now you’ll only have to make a loop to display them on the map. To do so, inside the if (e == null) block use the following code.

```java
1   for(int i = 0; i < stores.size(); i++) {
2   LatLng storeLocation = new LatLng(stores.get(i).getParseGeoPoint("Location").getLatitude(), stores.get(i).getParseGeoPoint("Location").getLongitude());
3   googleMap.addMarker(new MarkerOptions().position(storeLocation).title(stores.get(i).getString("Name")).icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_AZURE)));
4   }
```

The complete method that executes all 3 steps above is below. Call it on the onMapReady method for it to work.

```java
1   private void showStoresInMap(final GoogleMap googleMap){
2
3       ParseQuery<ParseObject> query = ParseQuery.getQuery("Stores");
4       query.whereExists("Location");
5       query.findInBackground(new FindCallback<ParseObject>() {
6           @Override  public void done(List<ParseObject> stores, ParseException e) {
7               if (e == null) {
8                   for(int i = 0; i < stores.size(); i++) {
9                       LatLng storeLocation = new LatLng(stores.get(i).getParseGeoPoint("Location").getLatitude(), stores.get(i).getParseGeoPoint("Location").getLongitude());
10                      googleMap.addMarker(new MarkerOptions().position(storeLocation).title(stores.get(i).getString("Name")).icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_AZURE)));
11                  }
12              } else {
13                  // handle the error
14                  Log.d("store", "Error: " + e.getMessage());
15              }
16          }
17      });
18      ParseQuery.clearAllCachedResults();
19  }
```

## 9 - Show closest user to a store

&#x20;    1\. Now that you have a bunch of stores with spatial coordinates associated, it would be good to find out which store is closest to a user. This can be done by using a ParseQuery. First, you’ll need to create a ParseObject query, informing the name of the Back4pp Dashboard class you want to query (in this case the “Stores” class), and restrict it with whereNear, informing the column of the Store class on Back4App you are doing the query (in this case the “Location” column). The following code do that:

```java
1   ParseQuery<ParseObject> query = ParseQuery.getQuery("Stores");
2   query.whereNear("Location", getCurrentUserLocation());
```

&#x20;    2\. You can limit the number of results of this query adding to it the restriction setLimit. By default, results are limited to 100. As the whereNear restriction will make the query retrieve an array of users ordered by distance (nearest to farthest) from currentUserLocation, setting the limit of close users to find to the number 1, the list of results of the query will only have one store: the closest to the current user. The following code set the limit of results to 1:

```java
1   query.setLimit(1);
```

&#x20;    3\. Now that you restricted your query, let’s retrieve its results. In order to do that, you will call a findInBackground method and pass as argument a List of store obejcts, in which it’ll be stored the results of the query and also a ParseException to handle errors. To avoid errors, don’t forget to clear cached results after the query found any result. The following code do that:

```java
1   query.findInBackground(new FindCallback<ParseObject>() {
2      @Override  public void done(List<ParseObject> nearStores, ParseException e) {
3          if (e == null) {
4            // do something with the list of results of your query
5          } else {
6              // handle the error
7          }
8      }
9     });
10    ParseQuery.clearAllCachedResults();
11  }
```

&#x20;    4\. If no error occurs, you’ll have in the nearStores list the closest store to the current user, now you’ll only have to display it on the MapsActivity. To do that, inside the if (e == null) block use the following code:

```java
1   ParseObject closestStore = nearStores.get(0);
2   // showing current user location, using the method implemented in Step 5
3   showCurrentUserInMap(mMap);
4   // finding and displaying the distance between the current user and the closest store to him, using method implemented in Step 4
5   double distance = getCurrentUserLocation().distanceInKilometersTo(closestStore.getParseGeoPoint("Location"));
6   alertDisplayer("We found the closest store from you!", "It's " + closestStore.getString("Name") + ". \n You are " + Math.round (distance * 100.0) / 100.0  + " km from this store.");
7   // creating a marker in the map showing the closest store to the current user
8   LatLng closestStoreLocation = new LatLng(closestStore.getParseGeoPoint("Location").getLatitude(), closestStore.getParseGeoPoint("Location").getLongitude());
9   googleMap.addMarker(new MarkerOptions().position(closestStoreLocation).title(closestStore.getString("Name")).icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_GREEN)));
10  // zoom the map to the closestStoreLocation
11  googleMap.animateCamera(CameraUpdateFactory.newLatLngZoom(closestStoreLocation, 3));
```

:::hint{type="info"}
The alertDisplayer method used above, is the same of the Step 6 (Finding the closest user to the current one).

:::

The complete method that executes all 4 steps above is the following:

```java
1   private void showClosestStore(final GoogleMap googleMap){
2       ParseQuery<ParseObject> query = ParseQuery.getQuery("Stores");
3       query.whereNear("Location", getCurrentUserLocation());
4       // setting the limit of near stores to 1, you'll have in the nearStores list only one object: the closest store from the current user
5       query.setLimit(1);
6       query.findInBackground(new FindCallback<ParseObject>() {
7           @Override  public void done(List<ParseObject> nearStores, ParseException e) {
8               if (e == null) {
9                   ParseObject closestStore = nearStores.get(0);
10                  // showing current user location, using the method implemented in Step 5
11                  showCurrentUserInMap(mMap);
12                  // finding and displaying the distance between the current user and the closest store to him, using method implemented in Step 4
13                  double distance = getCurrentUserLocation().distanceInKilometersTo(closestStore.getParseGeoPoint("Location"));
14                  alertDisplayer("We found the closest store from you!", "It's " + closestStore.getString("Name") + ". \nYou are " + Math.round (distance * 100.0) / 100.0  + " km from this store.");
15                  // creating a marker in the map showing the closest store to the current user
16                  LatLng closestStoreLocation = new LatLng(closestStore.getParseGeoPoint("Location").getLatitude(), closestStore.getParseGeoPoint("Location").getLongitude());
17                  googleMap.addMarker(new MarkerOptions().position(closestStoreLocation).title(closestStore.getString("Name")).icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_GREEN)));
18                  // zoom the map to the closestStoreLocation
19                  googleMap.animateCamera(CameraUpdateFactory.newLatLngZoom(closestStoreLocation, 3));
20              } else {
21                  Log.d("store", "Error: " + e.getMessage());
22              }
23          }
24      });
25
26      ParseQuery.clearAllCachedResults();
27
28  }
```

## 10 - Test your app

&#x20;    1\. Login at [**Back4App Website**](https://www.back4app.com/)

&#x20;    2\. Find your app and click on Dashboard > Core > Browser > User and create some users with location associated to them to allow the method showClosestUser to work.&#x20;

&#x20;    3\. Run your app in a real device and sign up an account. Try every feature!

&#x20;    4\. Go back to Back4pp Dashboard and verify if your location is stored in your user row.

## It’s done!

At this stage, you can use some features of ParseGeoPoint through Back4App!
