# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/working-with-files/react-native-delete-files.md

---
title: Deleting Files
slug: docs/react-native/parse-sdk/working-with-files/react-native-delete-files
description: In this guide you'll learn how to delete files in Back4App on your React Native App
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T17:24:23.366Z
updatedAt: 2025-01-17T14:12:44.198Z
---

# Delete Files from a React Native App

## Introduction

In this guide, you will learn the best way to delete files from back4app cloud in React Native Apps.

For managing application files in Back4app, we use the Parse.File utility class. You can perform storing, retrieving, and deleting operations using this class. In the previous section, [**File Storage**](https://www.back4app.com/docs/js-framework/react-native-files), we covered storing and retrieving files by creating a demo gallery App.

At this point, you should be aware that after creating and saving a Parse.File, the best practice is to always associate it with another data object. It will prevent the creation of orphan files in your project and make it possible for you to find and delete them on Back4app cloud.

Parse.File provides a way of deleting files, but it is a security sensitive operation that you should not perform on client-side. In this tutorial, you will learn the best practice for removing your application files.

## Goal

Add delete image action to a React Native gallery demo App

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- Complete the [**File Storage**](https://app.archbee.com/docs/_roxIyUMXoBue9I7uv49e/niJIQGQOc93TzrlyDmcBi) tutorial
- Parse >= 4.2.0
:::

## 1 - Application setup

In the previous section, [**File Storage**](https://www.back4app.com/docs/js-framework/react-native-files), we built a demo gallery App to upload and display user pictures.
For this tutorial, You will increment this App by adding a delete button to each image item in the Gallery.js component and performing our delete operation.

If you already finished coding the demo gallery App then you can jump to the next step.

Alternatively, you can clone the code base for the App to follow this tutorial along.

To clone the project run:

git clone https\://github.com/templates-back4app/react-native-demo-gallery-app

Then, install project dependencies:

:::BlockQuote
1   cd reac&#x74;**-**&#x6E;ativ&#x65;**-**&#x64;em&#x6F;**-**&#x67;aller&#x79;**-**&#x61;pp
2
3   # using yarn
4   yarn install
5
6   # using npm
7   npm install
:::

Before running, remember to setup your Back4app credentials, App Id and JavascriptKey, on the initialize method. For information on App credentials setup see [**Install Parse SDK**](https://www.back4app.com/docs/js-framework/react-native-cli).

Finally, run the React Native Application:

:::BlockQuote
1   # For Android
2   npx reac&#x74;**-**&#x6E;ative ru&#x6E;**-**&#x61;ndroid
3
4   # For iOS
5   npx reac&#x74;**-**&#x6E;ative ru&#x6E;**-**&#x69;os
:::

## 2 - Creating a delete button

On the gallery App, the Gallery.js component renders the list of images from your Back4app cloud project. Next, you will create and add a button to every image item in the current list.

Open the Gallery.js file add the following content:

```javascript
1	import React, {useState, useEffect} from  'react';
2	import {Text, View, Image, FlatList, StyleSheet, Button, Alert} from  'react-native';
3	import Parse from  'parse/react-native.js';
4	
5	const Gallery = () => {
6	const [images, setImages] = useState([]);
7	
8	useEffect(() => {
9	  const fetchImages = async () => {
10	  let query = new Parse.Query('Gallery');
11	  const results = await  query.find();
12	  setImages(results);
13	  };
14	
15	  fetchImages();
16	}, []);
17	
18	async function onDeleteImage(image_id) {
19	  // TODO: implement this function
20	}
21	
22	return (
23	<FlatList
24	  style={styles.container}
25	  contentContainerStyle={styles.listContent}
26	  data={images}
27	  horizontal={false}
28	  numColumns={3}
29	  ListEmptyComponent={() =>  <Text>No images uploaded.</Text>}
30	  renderItem={({item}) => (
31	    <View>
32	      <Image
33	        source={ {uri: item.get('picture').url()} }
34	        style={styles.imageItem}
35	      />
36	     <Button
37	        title="Delete"
38	        color="red"
39	        onPress={() => onDeleteImage(item.id)}
40	      />
41	    </View>
42	  )}
43	  keyExtractor={(item) =>  item.id}
44	/>);
45	
46	};
47	
48	const styles = StyleSheet.create({
49	container: {
50	  flex: 1,
51	  backgroundColor: '#f5f5f5',
52	},
53	listContent: {
54	  justifyContent: 'center',
55	  alignItems: 'center',
56	},
57	imageItem: {
58	  width: 100,
59	  height: 100,
60	  resizeMode: 'cover',
61	  marginHorizontal: 5,
62	  marginVertical: 5,
63	},
64	});
65	export default Gallery;
```

We have refactored the renderItem function, including a delete button to all rendered images. However, the button click event still has no functionality implemented. You will do it on the next step.

## 3 - Creating a delete picture cloud function

You’ve learned that a file should always be associated with a data object on the [**File Storage**](https://www.back4app.com/docs/js-framework/react-native-files). Not associating files to data objects will result in orphan files. Those files are unreachable inside your App. Once you can’t find them, you also can’t delete them from your App. You can only erase them using the Purge Files option on Back4App Dashboard.

The deleting process consists of finding and then deleting it. In Parse, the destroy method is used to delete referenced files. However, using it on client side is not safe as it requires the masterKey.

When you build a React Native app, all your keys are bundled together, therefore, anyone could reverse engineer, decompile your app or proxy your network traffic from their device to find your masterKey. Using the master key allows you to bypass all of your app’s security mechanisms, such as [**class-level permissions**](https://docs.parseplatform.org/js/guide/#class-level-permissions) and [**ACLs**](https://docs.parseplatform.org/js/guide/#object-level-access-control). You can find more details about Parse security best practices [**here**](https://blog.back4app.com/parse-server-security/).

The best way to delete files is to do it on the server side using a [**Cloud Code function**](https://www.back4app.com/docs/get-started/cloud-functions). In our gallery app, we will create a cloud code function for that.

Let’s create a main.js file with the following cloud function:

```javascript
1	Parse.Cloud.define('deleteGalleryPicture', async (request) => {
2	        const {image_id} = request.params;
3	        const Gallery = Parse.Object.extend('Gallery');
4	        const query = new Parse.Query(Gallery);
5	        try {
6	                const Image = await query.get(image_id);
7	                const picture = Image.get('picture');
8	
9	                await picture.destroy({useMasterKey:  true});
10	                await Image.destroy();
11	                return 'Image removed.';
12	        } catch (error) {
13	                console.log(error);
14	                throw new Error('Error deleting image');
15	        }
16	});
```

For simplicity, we will use the Dashboard to upload cloud functions directly:

1. Open your App Dashboard at [**Back4App Website&#x20;**](https://www.back4app.com/)and click onCore, then Cloud Code Functions.
2. Uploadmain.jsfile on the root of the cloud/folder
3. Deploy the function to Back4app server

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/txkkWMnIXE9i1Zlm3ReEC_image.png)

After a few seconds your cloud code function will be available to be called via REST or Parse SDK.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/lwkNJD3OmKDdBOJT8_fDO_image.png)

## 4 - Calling delete cloud function from your App

Once you have successfully deployed your Back4app Cloud Code function, go ahead and implement the action for when the users presses delete button in our gallery app:

```javascript
1	// Triggers on hitting delete
2	async function onDeleteImage(image_id) {
3	  try {
4	    const params = {image_id};
5	    const result = await Parse.Cloud.run('deleteGalleryPicture', params);
6	    Alert.alert(result);
7	  } catch (error) {
8	    console.log('Delete Error: ', error);
9	  }
10	}
11
```

Now when you click on delete, your app will trigger deleteGalleryPicture cloud function that will successfully delete an image:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/mMm9rAr2IiwvMWj6WhCiF_image.png" signedSrc size="50" width="279" height="593" position="center" caption}

## 5 - Purging Files

In some situations, when you lost track of your application files you need to delete files from your Dashboard. This usually occurs when you create the orphan files mentioned in this article.

For information on how to clean up your application files:

1. Try [**Back4app Files common questions**](https://help.back4app.com/hc/en-us/articles/360002327652-How-to-delete-files-completely-)
2. Or See [**App Settings documentation**](https://www.back4app.com/docs/parse-dashboard/app-settings)

## Done!

At this point, you have succefully deployed a cloud code function and learned how to delete an image in a React Native application.
