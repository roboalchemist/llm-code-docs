# Source: https://docs-containers.back4app.com/docs/js-framework/ionic/ionic-framework-tutorial.md

---
title: Using Geopoints
slug: docs/js-framework/ionic/ionic-framework-tutorial
description: In this tutorial you’ll learn how to use geo points on your Ionic app to find out what user is closest to another user or which places are closest to a user.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-08T14:13:55.114Z
updatedAt: 2025-01-17T19:12:06.146Z
---

# Using geo points with Ionic framework

## Introduction

Parse allows you to associate real-world latitude and longitude coordinates with an object. Adding a **ParseGeoPoint** to a **ParseUser**, you will be able to easily find out which user is closest to another, show the locations of the users of your app and also store the user’s location information, among other possibilities.

You can also associate a **ParseGeoPoint** to any **ParseObject**. For example, if your app is associated with a store with physical affiliates, you will be able to create a page to show the location of those stores or to show the user which store is closest to him. Another example of this association usage: if your app is a game in which you created ParseObjects to represent characters, adding ParseGeoPoints to these characters would allow them to be shown along the player’s path.

This tutorial explains how to use some features of ParseGeoPoint through Back4App.

After following this tutorial, you will be able to do this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/lC9NUmr8W2RwRGh9nPGSM_image.png" signedSrc size="40" width="359" height="639" position="center" caption}

## Prerequisites

## 1 - Set up Google API Key

Install [**Angular Google Maps - AGM**](https://angular-maps.com/api-docs/agm-core/).

:::BlockQuote
$ npm install @agm/core
:::

Import the SDK adding the generated key to ./src/app/app.module.ts.

## 2 - Retrieve user’s location

To retrieve user’s location, we’ll need to install [**Ionic Geolocation**](https://ionicframework.com/docs/native/geolocation/) plugin.

:::BlockQuote
$ ionic cordova plugin add cordova-plugin-geolocation --variable GEOLOCATION\_USAGE\_DESCRIPTION="To locate you"
$ npm install --save @ionic-native/geolocation
:::

Now that we installed and imported Geolocation to providers at ./src/app/app.module.ts, let’s implement the get location method and store the results to a class attribute.

## 3 - Create a page to display the map

Now that we have the user location, let’s create a page to display the map, using the already mentioned \[Angular Google Maps].

First, run the helper:

:::BlockQuote
$ ionic generate page Maps
:::

Let’s now make it receive a Marker that holds the **current** position the map is displaying and an array of Markers that will be the pin points around the map.

Let’s pull up the maps.html now and make it display the data.

## 4 - Showing current user’s location in map

Now we have a page to display the Map locations.

1. Let’s head back to home.ts and implement a method to display the user’s location on the map
2. Let’s make use of Parse easiness now and look for the peers closest to the user location

You can see how simple it is. Basically all we had to do is instantiate a query object for the User collection and make it look for the closest geo location by calling near().

## 5 - Set up Back4App to associate ParseGeoPoint to ParseObjects

Suppose that the example app you are building is associated with a group of stores with physical affiliates. It would be interesting to show all the physical affiliates of this store in the map. In order to do so create a Stores class on Back4pp Dashboard, save the existing stores as ParseObjects, their locations and after that the app will be able to query the physical affiliates and display their possitions on the map. The following steps will help you with that.

Go to [**Back4App website&#x20;**](https://www.back4app.com/)login, find your app and open its Dashboard.



Go to Core > Browser > Create a class, as shown in the image below.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/T9gMl256s_tvoPbKNEYt8_image.png)

In the field What type of class do you need?, choose the Custom option

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/XrAghJP5HgDEEJYbZ6HGq_image.png)

In the field What should we call it?, type “**Stores**” and then click on Create class button.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/5AoEZ5Geao4gHETUuWh-N_image.png)

Then a new class called “**Stores**” will be shown and you should insert 2 columns on it: a collumn with data type String called Name, as well as another column with data type GeoPoint called Location. Your class should end up like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Ze2MXhV5cInRg6nDKzxcp_image.png)

Now, fill this class with information. To do so, click on Add a row button in the menu on the top right or in the middle of the page, as shown in the image below.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/rF9YhyrN4W_s3DOobD5tn_image.png)

Then fill the row with the informations required: the name of the store and its latitude and longitude. After inserting some data, your Stores class should look like the image below. If you want to insert more data, you can click on the Add a row button on the top, or in the + button bellow the last row of data.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/HIHbksg6Y7-XCkykTqGoP_image.png)

Now you are ready to use the location information of the stores in your app.

## 6 - Display all the stores location on Map

Now that we have the stores location stored, let’s code a method to get the objects and display them.

Easy, right? Now, let’s get the CLOSEST one.

You can see how it’s just like getting the closest User as we have done earlier.

## 7 - Add buttons to Home Page

You probably noticed we have no way of calling those methods, let’s add the buttons to the home.ts then and make it happen!

## 8 - Test your app

1. Login at [**Back4App Website**](https://www.back4app.com/).
2. Find your app and click on Dashboard > Core > Browser > User and create some users with location associated to them to allow the method getClosestUser to work.
3. Run your app in a real device or in the browser to sign up and log in. Try every feature!

## It’s done!

At this stage, you can use some features of ParseGeoPoint through Back4App!
