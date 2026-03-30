# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/working-with-files/react-native-save-file.md

---
title: File Storage
slug: docs/react-native/parse-sdk/working-with-files/react-native-save-file
description: In this guide you'll learn save and read files in Back4App on your React Native App
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-19T17:15:39.852Z
updatedAt: 2025-01-17T14:12:40.568Z
---

# Save Files from a React Native App

## Introduction

In this guide, you will learn how to store and retrieve files in your React Native Application using Parse Javascript SDK to manage Back4app cloud storage.

In the Parse world, we use the typeParse.File to manage files. After creating the Parse.File, you will store it on the Back4App Cloud using the save() method. You should always associate the file with another data object so you can retrieve this file path when querying the object. If you do not associate, the file will be stored, but you will not find them on the Cloud.

Another important tip is to give a name to the file that has a file extension. This extension lets Parse figure out the file type and handle it accordingly. We should also mention that Each upload gets a unique identifier, so there’s no problem with uploading multiple files using the same name.

React Native App’s most common use case is storing images. In this guide, you will build a demo gallery app to store and display pictures.

The full sample code for the created App in this tutorial is [**here**](https://github.com/templates-back4app/react-native-demo-gallery-app). Feel free to follow along step by step or jump straight to the code.
playing images.

:::hint{type="danger"}
If you do not associate your file to a data object the file will become an orphan file and you wont be able to find it on Back4App Cloud.
:::

## Goal

To create a React Native gallery App that uploads and displays images using Parse Javascript and Back4app.

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- Complete the [**Install Parse SDK**](https://www.back4app.com/docs/parse-sdk/react-native-sdk) tutorial.
:::

## 1 - Installing dependencies

Working with files (i.e., uploading photos) on React Native apps is one of the most common features. In this tutorial, you will build a simple gallery App that uploads and displays images.

Once you have a [**React Native project successfully connected with Back4app**](https://www.back4app.com/docs/parse-sdk/react-native-sdk), go to its root directory and install the following dependency:

:::BlockQuote
cd startWithBack4app

\# To select images on devices
yarn add react-native-image-picker&#x20;
:::

For iOS, install pods:

:::BlockQuote
cd ios && npx pod-install
:::

Note that auto-linking is available for React native v0.60+, but for information on installing react-native-image-picker older versions, [**check the official documentation here**](https://github.com/react-native-image-picker/react-native-image-picker).

After installing, you will need to add the NSPhotoLibraryUsageDescription key to your info.plist for allowing the user to select image/video from photos on iOS.

:::BlockQuote
\<dict>
//other keys ...
\<key>NSPhotoLibraryUsageDescription\</key>
\<string>APP\_NAME\_HERE would like access to your photo\</string>&#x20;
\</dict>
:::

On android no permissions are required to select photos for gallery.

## 2 - Selecting an Image from Gallery

Next, you will build a component that wraps the UI and logic for selecting an image from the gallery and uploading it.

In your root directory, create a UploadingImage.js file with the following content:

```javascript
1	import  React, {useState} from  'react';
2	import {View, Button, Image, StyleSheet} from  'react-native';
3	
4	import {launchImageLibrary} from  'react-native-image-picker';
5	import Parse from 'parse/react-native.js';
6	
7	const  UploadImage = () => {
8	const [image, setImage] = useState(null);
9	
10	async function upload() {
11	        // TODO: implement this method
12	}
13	// This will open phone image library
14	function pickImage() {
15	  launchImageLibrary(
16	        {
17	          mediaType:  'photo',
18	          includeBase64:  true,
19	          maxHeight:  200,
20	          maxWidth:  200,
21	        },
22	        (response) => {
23	          // Add selected image to the state
24	          setImage(response);
25	        },
26	  );
27	}
28	
29	return (
30	  <View>
31	        <Button
32	          onPress={pickImage}
33	          title="Pick an image from gallery"
34	          color="#841584" />
35	          {image && <Image source={ {uri: image.uri} } style={styles.currentImage}/>}
36	
37	          {image && <Button title="Upload" color="green" onPress={upload}  />}
38	  </View>
39	);
40	
41	};
42	
43	const styles = StyleSheet.create({
44	  container: {
45	    height:  400,
46	    justifyContent:  'center',
47	    alignItems:  'center',
48	  },
49	  currentImage: {
50	        width:  250,
51	        height:  250,
52	        resizeMode:  'cover',
53	        alignSelf:  'center',
54	  },
55	});
56	
57	export  default  UploadImage;
```

The above component renders:

1. A button which opens the image library when a user clicks
2. The selected image along with an upload button

As you can see, the upload method does not do anything. Next, you will implement its behavior and see how to actually upload images to Back4app cloud.

## 3 - Uploading an Image

Back4app storage is built upon Parse.File and lets you store any files such as documents, images, videos, music, and any other binary data. Parse.File is a utility class that Parse Javascript SDK provides to abstract the file storage process and make it easy for you.

Therefore, to upload an image, you will only need to create a Parse.File instance and then call the save method. By doing this, Parse will automatically do the rest for you. You can read the [**full documentation about Parse Files here**](https://docs.parseplatform.org/js/guide/#files).

Let’s do that in our upload function:

```javascript
1	async function upload() {
2	  // 1. Create a file
3	  const {base64, fileName} = image;
4	  const  parseFile = new  Parse.File(fileName, {base64});
5	
6	  // 2. Save the file
7	  try {
8	        const responseFile = await  parseFile.save();
9	        const Gallery = Parse.Object.extend('Gallery');
10	        const gallery = new  Gallery();
11	        gallery.set('picture', responseFile);
12	
13	        await gallery.save();
14	        Alert.alert('The file has been saved to Back4app.');
15	  } catch (error) {
16	          console.log(
17	            'The file either could not be read, or could not be saved to Back4app.',
18	          );
19	        }
20	}
```

In short, the above snippet creates and saves the selected image, and after the save completes, we associate it with a Parse.Object called Gallery.

Now you need to import and use the UploadImage component in your App.js:

```javascript
1	import React from 'react';
2	import {SafeAreaView, StyleSheet} from 'react-native';
3	// In a React Native application
4	import Parse from 'parse/react-native.js';
5	import AsyncStorage from '@react-native-community/async-storage';
6	import keys from './constants/Keys';
7	//Before using the SDK...
8	Parse.setAsyncStorage(AsyncStorage);
9	Parse.initialize(keys.applicationId, keys.javascriptKey);
10	Parse.serverURL = keys.serverURL;
11	
12	import UploadImage from './UploadImage';
13	
14	const App = () => {
15	  return (
16	        <SafeAreaView style={styles.container}>
17	                <UploadImage/>
18	        </SafeAreaView>
19	  )
20	};
21	
22	const styles = StyleSheet.create({
23	  container: {
24	        backgroundColor: '#f5f5f5',
25	        flex: 1,
26	  },
27	  title: {
28	        fontSize: 18,
29	        textAlign: 'center',
30	        fontWeight: 'bold',
31	  },
32	});
33	
34	export default App;
```

Once you do that, you should be able to pick images from the gallery:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/wj-9xLb7nlPZOFo-Z3n_J_image.png" signedSrc size="50" width="380" height="796" position="center" caption}

And successfully upload images hitting the upload button:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/kosbv459hnKX83Q1F8Uo7_image.png" signedSrc size="50" width="377" height="797" position="center" caption}

## 4 - Displaying Images

We need to get the image’s URL to retrieve the image’s contents and display it to our users. Next, you will build a component for querying images from our Gallery Object and displaying them on a FlatList.

In your root directory, create a Gallery.js file with the following content:

```javascript
1	import React, {useState, useEffect} from  'react';
2	import {Text, Image, FlatList, StyleSheet} from 'react-native';
3	
4	import Parse from 'parse/react-native.js';
5	
6	const Gallery = () => {
7	const [images, setImages] = useState([]);
8	
9	useEffect(() => {
10	  const fetchImages = async () => {
11	        let query = new Parse.Query('Gallery');
12	        const results = await query.find();
13	        setImages(results);
14	  };
15	  
16	  fetchImages();
17	}, []);
18	
19	return (
20	  <FlatList
21	    style={styles.container}
22	        contentContainerStyle={styles.listContent}
23	        data={images}
24	        horizontal={false}
25	        numColumns={3}
26	        ListEmptyComponent={() =>  <Text>No images uploaded.</Text>}
27	        renderItem={({item}) => 
28	          <Image source={ {uri: item.get('picture').url()} } style={styles.imageItem}/>
29	        )}
30	        keyExtractor={(item) => item.id}
31	  />);
32	};
33	
34	const  styles = StyleSheet.create({
35	  container: {
36	        flex: 1,
37	        backgroundColor: '#f5f5f5',
38	  },
39	  listContent: {
40	        justifyContent: 'center',
41	        alignItems: 'center',
42	  },
43	  imageItem: {
44	        width: 100,
45	        height: 100,
46	        resizeMode: 'cover',
47	        marginHorizontal: 5,
48	        marginVertical: 5,
49	  },
50	});
51	
52	export default Gallery;
```

The above component uses the useEffect hook to query images uploaded to the Gallery Object once it finishes rendering. Next, you will need to add the component to your App.js:

```javascript
1	// ...other imports
2	import UploadImage from './UploadImage';
3	import Gallery from './Gallery';
4	
5	const App = () => {
6	  return (
7	        <SafeAreaView style={styles.container}>
8	          <UploadImage/>
9	          <Gallery/>
10	        </SafeAreaView>
11	        );
12	}
```

When you run your App, you should be able to see the list of uploaded images like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/qWi5YHa87nR0gLTJ4Rsdh_image.png" signedSrc size="50" width="377" height="799" position="center" caption}

## 5 - It’s Done!

At this point, you have uploaded your first image on Back4App and displayed it in a React Native application.
