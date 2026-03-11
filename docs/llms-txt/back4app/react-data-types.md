# Source: https://docs-containers.back4app.com/docs/react/data-objects/react-data-types.md

---
title: Data types
slug: docs/react/data-objects/react-data-types
description: In this guide you will learn which data types are supported in Parse on React
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-18T18:22:04.354Z
updatedAt: 2025-01-16T20:18:10.526Z
---

# &#x20;Parse Data Types in a React component

## Introduction

In the heart of Parse Core feature is the data objects management. Parse allows you to store and query its data straightforwardly using its SDKs or APIs (REST or GraphQL). All the data object features are built using the Parse.Object class, which fields may contain key-value pairs of several JSON-compatible data types. The primary data types that can be assigned to the object fields are the following:

- Number: integer (42) or floating-point (42.5) numbers, as long as ‘.’ is the decimal separator;
- boolean: true or false values;
- string: a string that can be as long as 2147483647 characters. Be aware that values this huge will slow down data operations;
- DateTime: DateTimeobjects stored in UTC format as default. If you need to use another timezone, conversion should be done manually;
- array: an array containing data in any Parse compatible data.
- object: a JSON object also containing any Parse data. When available in SDK, an include() call will bring details from the Object property.

:::hint{type="success"}
When you choose to use the Array type, we recommend keeping array objects small as this can affect your data operations’ overall performance. Our recommendation is to use the Array type if it does not exceed 20 elements and does not grow over time. Instead of the Array type, you can use the Pointer and Relations types as an alternative.
:::

In this guide, you will learn how to store data in each of the basic data types listed above. You will build a product registration component on React, which will show you how to format, convert and save data to your Parse Server in React.

Parse also offers the datatypes GeoPoint to use the power of geolocation resources, and the Parse-specific relational data using the types Pointer or Relation. You will see both covered in the next following guides.

## Prerequisites

:::hint{type="info"}
To complete this tutorial, you will need:

-
  A React App created and [**connected to Back4App**](https://www.back4app.com/docs/react/quickstart).
- If you want to test/use the screen layout provided by this guide, you should set up the [**&#x20;library**](https://ant.design/docs/react/introduce).
:::

## Goal

To understand the Parse-compatible basic data types, and to store each data type on Parse from a React component.

## 1 - The Product Creation Component

Let’s first create the component structure. Let’s make it simple and create a form screen with one text input to each data type, one checkbox, and a submit button to save the object. These inputs will collect your Product field values: name (string), quantity (number), price (number), available (boolean), expiration date (DateTime), and categories(array). Also, you will save an additional object type field in your saving method as well, but this one won’t need an input field.

Create a separate component in a file called ProductCreation.js/ProductCreation.tsx including the following code, or add it to your main application file (App.js/App.tsx). You can use this layout with complete stylings using Ant Design and adding the CSS code to your App.css file or set up your own custom form.

:::CodeblockTabs
ProductCreation.js

```javascript
1   import React, { useState } from 'react';
2   import Parse from 'parse/dist/parse.min.js';
3   import './App.css';
4   import { Button, Checkbox, Input } from 'antd';
5   import { PlusOutlined } from '@ant-design/icons';
6
7   export const ProductCreation = () => {
8     // State variables
9     const [productName, setProductName] = useState('');
10    const [productQuantity, setProductQuantity] = useState('');
11    const [productPrice, setProductPrice] = useState('');
12    const [productAvailable, setProductAvailable] = useState(false);
13    const [productExpirationDate, setProductExpirationDate] = useState('');
14    const [productCategories, setProductCategories] = useState('');
15
16    return (
17      <div>
18        <div className="header">
19          <img
20            className="header_logo"
21            alt="Back4App Logo"
22            src={
23              'https://blog.back4app.com/wp-content/uploads/2019/05/back4app-white-logo-500px.png'
24            }
25          />
26          <p className="header_text_bold">{'React on Back4App'}</p>
27          <p className="header_text">{'Product Creation'}</p>
28        </div>
29        <div className="container">
30          {/* Product field inputs */}
31          <div className="flex_between">
32            <h2 className="list_heading">Available?</h2>
33            <Checkbox
34              onChange={(e) => setProductAvailable(e.target.checked)}
35            ></Checkbox>
36          </div>
37          <div className="form_wrapper">
38            <Input
39              className="form_input"
40              value={productName}
41              onChange={(event) => setProductName(event.target.value)}
42              placeholder="Name"
43              size="large"
44            />
45            <Input
46              className="form_input"
47              value={productQuantity}
48              onChange={(event) => setProductQuantity(event.target.value)}
49              placeholder="Quantity"
50              size="large"
51            />
52            <Input
53              className="form_input"
54              value={productPrice}
55              onChange={(event) => setProductPrice(event.target.value)}
56              placeholder="Price"
57              size="large"
58            />
59            <Input
60              className="form_input"
61              value={productExpirationDate}
62              onChange={(event) => setProductExpirationDate(event.target.value)}
63              placeholder="Expiration Date (mm/dd/yyyy)"
64              size="large"
65            />
66            <Input
67              className="form_input"
68              value={productCategories}
69              onChange={(event) => setProductCategories(event.target.value)}
70              placeholder="Categories (separated by comma)"
71              size="large"
72            />
73            {/* Add product button */}
74            <Button
75              type="primary"
76              className="form_button"
77              color={'#208AEC'}
78              size={'large'}
79              onClick={createProduct}
80              icon={<PlusOutlined />}
81            >
82              CREATE PRODUCT
83            </Button>
84          </div>
85        </div>
86      </div>
87    );
88 };
```

ProductCreation.tsx

```typescript
1   import React, { useState, FC, ReactElement } from 'react';
2   import './App.css';
3   import { Button, Checkbox, Input } from 'antd';
4   import { PlusOutlined } from '@ant-design/icons';
5   const Parse = require('parse/dist/parse.min.js');
6
7   export const ProductCreation: FC<{}> = (): ReactElement => {
8     // State variables
9     const [productName, setProductName] = useState('');
10    const [productQuantity, setProductQuantity] = useState('');
11    const [productPrice, setProductPrice] = useState('');
12    const [productAvailable, setProductAvailable] = useState(false);
13    const [productExpirationDate, setProductExpirationDate] = useState('');
14    const [productCategories, setProductCategories] = useState('');
15
16    const createProduct = async function (): Promise<boolean> {
17      try {
18        // These values come from state variables
19        // Convert data values to corresponding data types
20        const productNameValue: string = productName;
21        const productQuantityValue: number = Number(productQuantity);
22        const productPriceValue: number = Number(productPrice);
23        const productAvailableValue: boolean = productAvailable;
24        const productExpirationDateValue: Date = new Date(productExpirationDate);
25        const productCategoriesValue: string[] = productCategories.split(',');
26
27        // Creates a new Product parse object instance
28        let Product: Parse.Object = new Parse.Object('Product');
29
30        // Set data to parse object
31        Product.set('name', productNameValue);
32        Product.set('quantity', productQuantityValue);
33        Product.set('price', productPriceValue);
34        Product.set('available', productAvailableValue);
35        Product.set('expirationDate', productExpirationDateValue);
36        Product.set('categories', productCategoriesValue);
37        Product.set('completeData', {
38          name: productNameValue,
39          quantity: productQuantityValue,
40          price: productPriceValue,
41          available: productAvailableValue,
42          expirationDate: productExpirationDateValue,
43          categories: productCategoriesValue,
44        });
45
46        // After setting the values, save it on the server
47        try {
48          let savedProduct: Parse.Object = await Product.save();
49          // Success
50          alert(`Success! ${JSON.stringify(savedProduct)}`);
51          return true;
52        } catch (error) {
53          // Error can be caused by lack of Internet connection
54          alert(`Error! ${error.message}`);
55          return false;
56        }
57      } catch (error: any) {
58        // Error can be caused by wrong type of values in fields
59        alert(`Error! ${error.message}`);
60        return false;
61      }
62    };
63
64    return (
65      <div>
66        <div className="header">
67          <img
68            className="header_logo"
69            alt="Back4App Logo"
70            src={
71              'https://blog.back4app.com/wp-content/uploads/2019/05/back4app-white-logo-500px.png'
72            }
73          />
74          <p className="header_text_bold">{'React on Back4App'}</p>
75          <p className="header_text">{'Product Creation'}</p>
76        </div>
77        <div className="container">
78          {/* Product field inputs */}
79          <div className="flex_between">
80            <h2 className="list_heading">Available?</h2>
81            <Checkbox
82              onChange={(e) => setProductAvailable(e.target.checked)}
83            ></Checkbox>
84          </div>
85          <div className="form_wrapper">
86            <Input
87              className="form_input"
88              value={productName}
89              onChange={(event) => setProductName(event.target.value)}
90              placeholder="Name"
91              size="large"
92            />
93            <Input
94              className="form_input"
95              value={productQuantity}
96              onChange={(event) => setProductQuantity(event.target.value)}
97              placeholder="Quantity"
98              size="large"
99            />
100           <Input
101             className="form_input"
102             value={productPrice}
103             onChange={(event) => setProductPrice(event.target.value)}
104             placeholder="Price"
105             size="large"
106           />
107           <Input
108             className="form_input"
109             value={productExpirationDate}
110             onChange={(event) => setProductExpirationDate(event.target.value)}
111             placeholder="Expiration Date (mm/dd/yyyy)"
112             size="large"
113           />
114           <Input
115             className="form_input"
116             value={productCategories}
117             onChange={(event) => setProductCategories(event.target.value)}
118             placeholder="Categories (separated by comma)"
119             size="large"
120           />
121           {/* Add product button */}
122           <Button
123             type="primary"
124             className="form_button"
125             color={'#208AEC'}
126             size={'large'}
127             onClick={createProduct}
128             icon={<PlusOutlined />}
129           >
130             CREATE PRODUCT
131           </Button>
132         </div>
133       </div>
134     </div>
135   );
136 };
```
:::

```css
1   html {
2     box-sizing: border-box;
3     outline: none;
4     overflow: auto;
5   }
6
7   *,
8   *:before,
9   *:after {
10    margin: 0;
11    padding: 0;
12    box-sizing: inherit;
13  }
14
15  h1,
16  h2,
17  h3,
18  h4,
19  h5,
20  h6 {
21    margin: 0;
22  }
23
24  p {
25    margin: 0;
26  }
27
28  body {
29    margin: 0;
30    background-color: #fff;
31  }
32
33  .container {
34    width: 100%;
35    max-width: 600px;
36    margin: auto;
37    padding: 20px 0;
38  }
39
40  .header {
41    align-items: center;
42    padding: 25px 0;
43    background-color: #208AEC;
44  }
45
46  .header_logo {
47    height: 55px;
48    margin-bottom: 20px;
49    object-fit: contain;
50  }
51
52  .header_text_bold {
53    margin-bottom: 3px;
54    color: rgba(255, 255, 255, 0.9);
55    font-size: 16px;
56    font-weight: bold;
57  }
58
59  .header_text {
60    color: rgba(255, 255, 255, 0.9);
61    font-size: 15px;
62  }
63
64  .flex_between {
65    display: flex;
66    align-items: center;
67    justify-content: space-between;
68  }
69
70  .list_heading {
71    font-weight: bold;
72  }
73
74  .form_wrapper {
75    margin-top: 20px;
76    margin-bottom: 10px;
77  }
78
79  .form_input {
80    margin-bottom: 20px;
81  }
82
83  .form_button {
84    width: 100%;
85  }
```

After setting up this screen, your application should look like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/k_tQsJUhWUD_0s458TFty_image.png)

Note that each Product attribute has its text input field, except for the boolean checkbox input, meaning that the data in them needs conversion to the corresponding data type before saving.

## 2 - Converting Input Data

Before saving your data to the Parse.object, you need to correctly format the number, DateTime, and array inputs. Let’s now create a saving function, which will retrieve data from your state variables and apply the suitable data conversion:

:::CodeblockTabs
ProductCreation.js

```javascript
1   const createProduct = async function () {
2     try {
3       // These values come from state variables
4       // Convert data values to corresponding data types
5       const productNameValue = productName;
6       const productQuantityValue = Number(productQuantity);
7       const productPriceValue = Number(productPrice);
8       const productAvailableValue = productAvailable;
9       const productExpirationDateValue = new Date(productExpirationDate);
10      const productCategoriesValue = productCategories.split(',');
11    } catch (error) {
12      // Error can be caused by wrong type of values in fields
13      alert(`Error! ${error.message}`);
14      return false;
15    }
16  };
```

ProductCreation.tsx

```typescript
1   const createProduct = async function (): Promise<boolean> {
2     try {
3       // These values come from state variables
4       // Convert data values to corresponding data types
5       const productNameValue: string = productName;
6       const productQuantityValue: number = Number(productQuantity);
7       const productPriceValue: number = Number(productPrice);
8       const productAvailableValue: boolean = productAvailable;
9       const productExpirationDateValue: Date = new Date(productExpirationDate);
10      const productCategoriesValue: string[] = productCategories.split(',');
11    } catch (error: any) {
12      // Error can be caused by wrong type of values in fields
13      alert(`Error! ${error.message}`);
14      return false;
15    }
16  };
```
:::

The number data conversion is done casting the value as a Number JavaScript object. DateTime is converted using the Date JavaScript object constructor; the array one is created by using the String.split method in JavaScript, creating an array containing each entry of the categories field separated by commas.

Note that your data is now contained inside a single object, which can be set in a new Parse.object instance to be saved to the server using the Parse.Object.set() method, which takes two arguments: the field name and the value to be set. Let’s also set a new field called completeData, which will be your object type field, assigning the same data object to it.

Go ahead and complete the createProduct function with the following:

:::CodeblockTabs
ProductCreation.js

```javascript
1   const createProduct = async function () {
2     try {
3       // These values come from state variables
4       // Convert data values to corresponding data types
5       const productNameValue = productName;
6       const productQuantityValue = Number(productQuantity);
7       const productPriceValue = Number(productPrice);
8       const productAvailableValue = productAvailable;
9       const productExpirationDateValue = new Date(productExpirationDate);
10      const productCategoriesValue = productCategories.split(',');
11
12      // Creates a new Product parse object instance
13      let Product = new Parse.Object('Product');
14
15      // Set data to parse object
16      Product.set('name', productNameValue);
17      Product.set('quantity', productQuantityValue);
18      Product.set('price', productPriceValue);
19      Product.set('available', productAvailableValue);
20      Product.set('expirationDate', productExpirationDateValue);
21      Product.set('categories', productCategoriesValue);
22      Product.set('completeData', {
23        name: productNameValue,
24        quantity: productQuantityValue,
25        price: productPriceValue,
26        available: productAvailableValue,
27        expirationDate: productExpirationDateValue,
28        categories: productCategoriesValue,
29      });
30
31      // After setting the values, save it on the server
32      try {
33        let savedProduct = await Product.save();
34        // Success
35        alert(`Success! ${JSON.stringify(savedProduct)}`);
36        return true;
37      } catch (error) {
38        // Error can be caused by lack of Internet connection
39        alert(`Error! ${error.message}`);
40        return false;
41      }
42    } catch (error) {
43      // Error can be caused by wrong type of values in fields
44      alert(`Error! ${error.message}`);
45      return false;
46    }
47  };
```

ProductCreation.tsx

```typescript
1   const createProduct = async function (): Promise<boolean> {
2     try {
3       // These values come from state variables
4       // Convert data values to corresponding data types
5       const productNameValue: string = productName;
6       const productQuantityValue: number = Number(productQuantity);
7       const productPriceValue: number = Number(productPrice);
8       const productAvailableValue: boolean = productAvailable;
9       const productExpirationDateValue: Date = new Date(productExpirationDate);
10      const productCategoriesValue: string[] = productCategories.split(',');
11
12      // Creates a new Product parse object instance
13      let Product: Parse.Object = new Parse.Object('Product');
14    
15      // Set data to parse object
16      Product.set('name', productNameValue);
17      Product.set('quantity', productQuantityValue);
18      Product.set('price', productPriceValue);
19      Product.set('available', productAvailableValue);
20      Product.set('expirationDate', productExpirationDateValue);
21      Product.set('categories', productCategoriesValue);
22      Product.set('completeData', {
23        name: productNameValue,
24        quantity: productQuantityValue,
25        price: productPriceValue,
26        available: productAvailableValue,
27        expirationDate: productExpirationDateValue,
28        categories: productCategoriesValue,
29      });
30
31      // After setting the values, save it on the server
32      try {
33        let savedProduct: Parse.Object = await Product.save();
34        // Success
35        alert(`Success! ${JSON.stringify(savedProduct)}`);
36        return true;
37      } catch (error: any) {
38        // Error can be caused by lack of Internet connection
39        alert(`Error! ${error.message}`);
40        return false;
41      };
42    } catch (error: any) {
43      // Error can be caused by wrong type of values in fields
44      alert(`Error! ${error.message}`);
45      return false;
46    }
47  };
```
:::

You can now test the component, inserting the createProduct function in it, and calling it inside your form submit button onClick property. After creating a product, you should see an alert containing its data like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/j2KECnAWhxB-N37QGU9Tv_image.png)

To certify that your data was saved on the server using the correct data types, you can look at your Parse dashboard. Click on the Product data table and note that every column has its data type written at the header. Your class should look like this:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Mf_H4HBZ1ANY7LKMT0hsT_image.png)

## Conclusion

At the end of this guide, you learned how to save each of the basic data types available on Parse using a React component. In the next guide, you will learn about the relational data on Parse.
