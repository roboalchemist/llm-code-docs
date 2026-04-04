# Source: https://docs-containers.back4app.com/docs/react-native/parse-sdk/data-objects/react-native-data-types.md

---
title: Data types
slug: docs/react-native/parse-sdk/data-objects/react-native-data-types
description: In this guide you'll learn which data types are supported in Parse on React Native
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-18T21:19:00.900Z
updatedAt: 2025-01-28T13:50:21.083Z
---

# Parse Data Types in a React Native component

## Introduction

In the heart of Parse Core feature is the data objects management. Parse allows you to store and query its data straightforwardly using its SDKs or APIs(REST or GraphQL). All the data object features are built using the Parse.Object class, which fields may contain key-value pairs of several JSON-compatible data types. The primary data types that can be assigned to the object fields are the following:

- Number: integer (42) or floating-point (42.5) numbers, as long as ‘.’ is the decimal separator;
- boolean: true or false values;
- string: a string that can be as long as 2147483647 characters. Be aware that values this huge will slow down data operations;
- DateTime\:DateTimeobjects stored in UTC format as default. If you need to use another timezone, conversion should be done manually;
- array: an array containing data in any Parse compatible data.
- object\:a JSON object also containing any Parse data. When available in SDK, aninclude()call will bring details from the Object property.

:::hint{type="success"}
When you choose to use the Array type, we recommend keeping array objects small as this can affect your data operations’ overall performance. Our recommendation is to use the Array type if it does not exceed 20 elements and does not grow over time. Instead of the Array type, you can use the Pointer and Relations types as an alternative.
:::

In this guide, you will learn how to store data in each of the basic data types listed above. You will build a React Native product registration component, which will show you how to format, convert and save data to your Parse Server in React Native.

Parse also offers the datatypes GeoPoint to use the power of geolocation resources, and the Parse-specific relational data using the types Pointer or Relation. You will see both covered in the next following guides.

::embed[]{url="https://www.youtube.com/embed/gEr9KcjTpOA"}

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- A React Native App created and connected to [**Back4App**](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk).
- If you want to test/use the screen layout provided by this guide, you should set up thereact-native-paper[**library**](https://github.com/callstack/react-native-paper).
:::

## Goal

To understand the Parse-compatible basic data types, and to store each data type on Parse froma React Native component.

## 1 - The Product Creation Component

Let’s first create the component structure. Let’s make it simple and create a form screen with one text inputs to each data type, one switch toggle, and a submit button to save the object. These inputs will collect your Product field values: name(string), quantity(number), price(number), available(boolean), expiration date(DateTime), and categories(array). Also, you will save an additional object type field in your saving method as well, but this one won’t need an input field.

Create a separate component in a file called ProductCreation.js/ProductCreation.tsx including the following code, or add it to your main application file (App.js/App.tsx or index.js). You can use this layout with complete stylings using react-native-paper or set up your custom form.

:::CodeblockTabs
ProductCreation.js

```javascript
1	import React, {useState} from 'react';
2	import {
3	  Alert,
4	  Image,
5	  SafeAreaView,
6	  StatusBar,
7	  StyleSheet,
8	  View,
9	} from 'react-native';
10	import Parse from 'parse/react-native';
11	import {
12	  Button as PaperButton,
13	  Switch as PaperSwitch,
14	  Text as PaperText,
15	  TextInput as PaperTextInput,
16	} from 'react-native-paper';
17	
18	export const ProductCreation = () => {
19	  // State variables
20	  const [productName, setProductName] = useState('');
21	  const [productQuantity, setProductQuantity] = useState('');
22	  const [productPrice, setProductPrice] = useState('');
23	  const [productAvailable, setProductAvailable] = useState(false);
24	  const [productExpirationDate, setProductExpirationDate] = useState('');
25	  const [productCategories, setProductCategories] = useState('');
26	
27	  const toggleProductAvailable = () => setProductAvailable(!productAvailable);
28	
29	  return (
30	    <>
31	      <StatusBar backgroundColor="#208AEC" />
32	      <SafeAreaView style={Styles.container}>
33	        <View style={Styles.header}>
34	          <Image
35	            style={Styles.header_logo}
36	            source={ { uri: 'https://blog.back4app.com/wp-content/uploads/2019/05/back4app-white-logo-500px.png', } }
37	          />
38	          <PaperText style={Styles.header_text_bold}>
39	            {'React Native on Back4App'}
40	          </PaperText>
41	          <PaperText style={Styles.header_text}>{'Product Creation'}</PaperText>
42	        </View>
43	        <View style={Styles.wrapper}>
44	          {/* Boolean type input  */}
45	          <View style={Styles.switch_container}>
46	            <PaperText>{'Available?'}</PaperText>
47	            <PaperSwitch
48	              value={productAvailable}
49	              onValueChange={toggleProductAvailable}
50	            />
51	          </View>
52	          {/* String type input */}
53	          <PaperTextInput
54	            value={productName}
55	            onChangeText={(text) => setProductName(text)}
56	            label="Name"
57	            mode="outlined"
58	            style={Styles.form_input}
59	          />
60	          {/* Number type input (integer) */}
61	          <PaperTextInput
62	            value={productQuantity}
63	            onChangeText={(text) => setProductQuantity(text)}
64	            label="Quantity"
65	            mode="outlined"
66	            keyboardType={'number-pad'}
67	            style={Styles.form_input}
68	          />
69	          {/* Number type input (float) */}
70	          <PaperTextInput
71	            value={productPrice}
72	            onChangeText={(text) => setProductPrice(text)}
73	            label="Price"
74	            mode="outlined"
75	            keyboardType={'numeric'}
76	            style={Styles.form_input}
77	          />
78	          {/* Date type input  */}
79	          <PaperTextInput
80	            value={productExpirationDate}
81	            onChangeText={(text) => setProductExpirationDate(text)}
82	            label="Expiration Date (mm/dd/yyyy)"
83	            mode="outlined"
84	            keyboardType={'numbers-and-punctuation'}
85	            style={Styles.form_input}
86	          />
87	          {/* Array type input  */}
88	          <PaperTextInput
89	            value={productCategories}
90	            onChangeText={(text) => setProductCategories(text)}
91	            label="Categories (separated by commas)"
92	            mode="outlined"
93	            style={Styles.form_input}
94	          />
95	          {/* Product create button */}
96	          <PaperButton
97	            onPress={() => createProduct()}
98	            mode="contained"
99	            icon="plus"
100	            style={Styles.submit_button}>
101	            {'Create Product'}
102	          </PaperButton>
103	        </View>
104	      </SafeAreaView>
105	    </>
106	  );
107	};
108	
109	// These define the screen component styles
110	const Styles = StyleSheet.create({
111	  container: {
112	    flex: 1,
113	    backgroundColor: '#FFF',
114	  },
115	  wrapper: {
116	    width: '90%',
117	    alignSelf: 'center',
118	  },
119	  header: {
120	    alignItems: 'center',
121	    paddingTop: 10,
122	    paddingBottom: 20,
123	    backgroundColor: '#208AEC',
124	  },
125	  header_logo: {
126	    width: 170,
127	    height: 40,
128	    marginBottom: 10,
129	    resizeMode: 'contain',
130	  },
131	  header_text_bold: {
132	    color: '#fff',
133	    fontSize: 14,
134	    fontWeight: 'bold',
135	  },
136	  header_text: {
137	    marginTop: 3,
138	    color: '#fff',
139	    fontSize: 14,
140	  },
141	  form_input: {
142	    height: 44,
143	    marginBottom: 16,
144	    backgroundColor: '#FFF',
145	    fontSize: 14,
146	  },
147	  switch_container: {
148	    flexDirection: 'row',
149	    alignItems: 'center',
150	    justifyContent: 'space-between',
151	    paddingVertical: 12,
152	    marginBottom: 16,
153	    borderBottomWidth: 1,
154	    borderBottomColor: 'rgba(0, 0, 0, 0.3)',
155	  },
156	  submit_button: {
157	    width: '100%',
158	    maxHeight: 50,
159	    alignSelf: 'center',
160	    backgroundColor: '#208AEC',
161	  },
162	});
```

ProductCreation.tsx

```typescript
1	import React, {FC, ReactElement, useState} from 'react';
2	import {
3	  Alert,
4	  Image,
5	  SafeAreaView,
6	  StatusBar,
7	  StyleSheet,
8	  View,
9	} from 'react-native';
10	import Parse from 'parse/react-native';
11	import {
12	  Button as PaperButton,
13	  Switch as PaperSwitch,
14	  Text as PaperText,
15	  TextInput as PaperTextInput,
16	} from 'react-native-paper';
17	
18	export const ProductCreation: FC<{}> = ({}): ReactElement => {
19	  // State variables
20	  const [productName, setProductName] = useState('');
21	  const [productQuantity, setProductQuantity] = useState('');
22	  const [productPrice, setProductPrice] = useState('');
23	  const [productAvailable, setProductAvailable] = useState(false);
24	  const [productExpirationDate, setProductExpirationDate] = useState('');
25	  const [productCategories, setProductCategories] = useState('');
26	
27	  const toggleProductAvailable = () => setProductAvailable(!productAvailable);
28	
29	  return (
30	    <>
31	      <StatusBar backgroundColor="#208AEC" />
32	      <SafeAreaView style={Styles.container}>
33	        <View style={Styles.header}>
34	          <Image
35	            style={Styles.header_logo}
36	            source={ { uri: 'https://blog.back4app.com/wp-content/uploads/2019/05/back4app-white-logo-500px.png', } }
37	          />
38	          <PaperText style={Styles.header_text_bold}>
39	            {'React Native on Back4App'}
40	          </PaperText>
41	          <PaperText style={Styles.header_text}>{'Product Creation'}</PaperText>
42	        </View>
43	        <View style={Styles.wrapper}>
44	          {/* Boolean type input  */}
45	          <View style={Styles.switch_container}>
46	            <PaperText>{'Available?'}</PaperText>
47	            <PaperSwitch
48	              value={productAvailable}
49	              onValueChange={toggleProductAvailable}
50	            />
51	          </View>
52	          {/* String type input */}
53	          <PaperTextInput
54	            value={productName}
55	            onChangeText={(text) => setProductName(text)}
56	            label="Name"
57	            mode="outlined"
58	            style={Styles.form_input}
59	          />
60	          {/* Number type input (integer) */}
61	          <PaperTextInput
62	            value={productQuantity}
63	            onChangeText={(text) => setProductQuantity(text)}
64	            label="Quantity"
65	            mode="outlined"
66	            keyboardType={'number-pad'}
67	            style={Styles.form_input}
68	          />
69	          {/* Number type input (float) */}
70	          <PaperTextInput
71	            value={productPrice}
72	            onChangeText={(text) => setProductPrice(text)}
73	            label="Price"
74	            mode="outlined"
75	            keyboardType={'numeric'}
76	            style={Styles.form_input}
77	          />
78	          {/* Date type input  */}
79	          <PaperTextInput
80	            value={productExpirationDate}
81	            onChangeText={(text) => setProductExpirationDate(text)}
82	            label="Expiration Date (mm/dd/yyyy)"
83	            mode="outlined"
84	            keyboardType={'numbers-and-punctuation'}
85	            style={Styles.form_input}
86	          />
87	          {/* Array type input  */}
88	          <PaperTextInput
89	            value={productCategories}
90	            onChangeText={(text) => setProductCategories(text)}
91	            label="Categories (separated by commas)"
92	            mode="outlined"
93	            style={Styles.form_input}
94	          />
95	          {/* Product create button */}
96	          <PaperButton
97	            onPress={() => createProduct()}
98	            mode="contained"
99	            icon="plus"
100	            style={Styles.submit_button}>
101	            {'Create Product'}
102	          </PaperButton>
103	        </View>
104	      </SafeAreaView>
105	    </>
106	  );
107	};
108	
109	// These define the screen component styles
110	const Styles = StyleSheet.create({
111	  container: {
112	    flex: 1,
113	    backgroundColor: '#FFF',
114	  },
115	  wrapper: {
116	    width: '90%',
117	    alignSelf: 'center',
118	  },
119	  header: {
120	    alignItems: 'center',
121	    paddingTop: 10,
122	    paddingBottom: 20,
123	    backgroundColor: '#208AEC',
124	  },
125	  header_logo: {
126	    width: 170,
127	    height: 40,
128	    marginBottom: 10,
129	    resizeMode: 'contain',
130	  },
131	  header_text_bold: {
132	    color: '#fff',
133	    fontSize: 14,
134	    fontWeight: 'bold',
135	  },
136	  header_text: {
137	    marginTop: 3,
138	    color: '#fff',
139	    fontSize: 14,
140	  },
141	  form_input: {
142	    height: 44,
143	    marginBottom: 16,
144	    backgroundColor: '#FFF',
145	    fontSize: 14,
146	  },
147	  switch_container: {
148	    flexDirection: 'row',
149	    alignItems: 'center',
150	    justifyContent: 'space-between',
151	    paddingVertical: 12,
152	    marginBottom: 16,
153	    borderBottomWidth: 1,
154	    borderBottomColor: 'rgba(0, 0, 0, 0.3)',
155	  },
156	  submit_button: {
157	    width: '100%',
158	    maxHeight: 50,
159	    alignSelf: 'center',
160	    backgroundColor: '#208AEC',
161	  },
162	});
```
:::

After setting up this screen, your application should look like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/38EB6MiBYSc08XDNHaqfa_image.png" signedSrc size="50" width="345" height="736" position="center" caption}

Note that each Product attribute has its text input field, except for the boolean switch input, meaning that the data in them needs conversion to the corresponding data type before saving.

## 2 - Converting input data

Before saving your data to the Parse.object, you need to correctly format the number, DateTime, and array inputs. Let’s now create a saving function, which will retrieve data from your state variables and apply the suitable data conversion:

:::CodeblockTabs
ProductCreation.js

```javascript
1	const createProduct = async function () {
2	  try {
3	    // These values come from state variables
4	    // Convert data values to corresponding data types
5	    const productNameValue = productName;
6	    const productQuantityValue = Number(productQuantity);
7	    const productPriceValue = Number(productPrice);
8	    const productAvailableValue = productAvailable;
9	    const productExpirationDateValue = new Date(productExpirationDate);
10	    const productCategoriesValue = productCategories.split(',');
11	  } catch (error) {
12	    // Error can be caused by wrong type of values in fields
13	    Alert.alert('Error!', error.message);
14	    return false;
15	  }
16	};
```

ProductCreation.tsx

```typescript
1	const createProduct = async function (): Promise<[boolean]> {
2	  try {
3	    // These values come from state variables
4	    // Convert data values to corresponding data types
5	    const productNameValue: string = productName;
6	    const productQuantityValue: number = Number(productQuantity);
7	    const productPriceValue: number = Number(productPrice);
8	    const productAvailableValue: boolean = productAvailable;
9	    const productExpirationDateValue: Date = new Date(productExpirationDate);
10	    const productCategoriesValue: string[] = productCategories.split(',');
11	  } catch (error) {
12	    // Error can be caused by wrong type of values in fields
13	    Alert.alert('Error!', error.message);
14	    return false;
15	  }
16	};
```
:::

The number data conversion is done casting the value as a Number JavaScript object. DateTime is converted using the Date JavaScript object constructor; the array one is created by using the String.split method in JavaScript, creating an array containing each entry of the categories field separated by commas.

Note that your data is now contained inside a single object, which can be set in a new Parse.object instance to be saved to the server using the Parse.Object.set() method, which takes two arguments: the field name and the value to be set. Let’s also set a new field called completeData, which will be your object type field, assigning the same data object to it.

Go ahead and complete the createProduct function with the following:

:::CodeblockTabs
ProductCreation.js

```javascript
1	const createProduct = async function () {
2	  try {
3	    // These values come from state variables
4	    // Convert data values to corresponding data types
5	    const productNameValue = productName;
6	    const productQuantityValue = Number(productQuantity);
7	    const productPriceValue = Number(productPrice);
8	    const productAvailableValue = productAvailable;
9	    const productExpirationDateValue = new Date(productExpirationDate);
10	    const productCategoriesValue = productCategories.split(',');
11	  } catch (error) {
12	    // Error can be caused by wrong type of values in fields
13	    Alert.alert('Error!', error.message);
14	    return false;
15	  }
16	
17	  // Creates a new Product parse object instance
18	  let Product = new Parse.Object('Product');
19	  
20	  // Set data to parse object
21	  Product.set('name', productNameValue);
22	  Product.set('quantity', productQuantityValue);
23	  Product.set('price', productPriceValue);
24	  Product.set('available', productAvailableValue);
25	  Product.set('expirationDate', productExpirationDateValue);
26	  Product.set('categories', productCategoriesValue);
27	  Product.set('completeData', {
28	    name: productNameValue,
29	    quantity: productQuantityValue,
30	    price: productPriceValue,
31	    available: productAvailableValue,
32	    expirationDate: productExpirationDateValue,
33	    categories: productCategoriesValue,
34	  });
35	
36	  // After setting the values, save it on the server
37	  try {
38	    let savedProduct = await Product.save();
39	    // Success
40	    Alert.alert('Success!', JSON.stringify(savedProduct));
41	    return true;
42	  } catch (error) {
43	    // Error can be caused by lack of Internet connection
44	    Alert.alert('Error!', error.message);
45	    return false;
46	  };
47	};
```

ProductCreation.tsx

```typescript
1	const createProduct = async function (): Promise<[boolean]> {
2	  try {
3	    // These values come from state variables
4	    // Convert data values to corresponding data types
5	    const productNameValue: string = productName;
6	    const productQuantityValue: number = Number(productQuantity);
7	    const productPriceValue: number = Number(productPrice);
8	    const productAvailableValue: boolean = productAvailable;
9	    const productExpirationDateValue: Date = new Date(productExpirationDate);
10	    const productCategoriesValue: string[] = productCategories.split(',');
11	  } catch (error) {
12	    // Error can be caused by wrong type of values in fields
13	    Alert.alert('Error!', error.message);
14	    return false;
15	  }
16	
17	  // Creates a new Product parse object instance
18	  let Product: Parse.Object = new Parse.Object('Product');
19	  
20	  // Set data to parse object
21	  Product.set('name', productNameValue);
22	  Product.set('quantity', productQuantityValue);
23	  Product.set('price', productPriceValue);
24	  Product.set('available', productAvailableValue);
25	  Product.set('expirationDate', productExpirationDateValue);
26	  Product.set('categories', productCategoriesValue);
27	  Product.set('completeData', {
28	    name: productNameValue,
29	    quantity: productQuantityValue,
30	    price: productPriceValue,
31	    available: productAvailableValue,
32	    expirationDate: productExpirationDateValue,
33	    categories: productCategoriesValue,
34	  });
35	
36	  // After setting the values, save it on the server
37	  try {
38	    let savedProduct: Parse.Object = await Product.save();
39	    // Success
40	    Alert.alert('Success!', JSON.stringify(savedProduct));
41	    return true;
42	  } catch (error) {
43	    // Error can be caused by lack of Internet connection
44	    Alert.alert('Error!', error.message);
45	    return false;
46	  };
47	};
```
:::

You can now test the component, insert the createProduct function in it, and call it inside your form submit button onPress property. After creating a product, you should see an alert containing its data like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/v4m5GMpsyodUcAeq2MHf0_image.png" signedSrc size="50" width="344" height="731" position="center" caption}

To certify that your data was saved on the server using the correct data types, you can look at your Parse dashboard. Click on the Product data table and note that every column has its data type written at the header. Your class should look like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/BkePakZS4Q8hO3cOjaWqp_image.png)

## Conclusion

At the end of this guide, you learned how to save each of the basic data types available on Parse using a React Native component. In the next guide, you will learn about the relational data on Parse.
