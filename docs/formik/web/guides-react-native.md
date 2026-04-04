# Formik Documentation
# Source: https://formik.org/docs/guides/react-native
# Path: /docs/guides/react-native

#### Documentation

#### API Reference

#### Documentation

#### API Reference

# React Native

Formik is 100% compatible with React Native and React Native Web.However,
because of differences between ReactDOM's and React Native's handling of forms
and text input, there are some differences to be aware of. This section will walk
you through them and what we consider to be best practices.

### The gist

Before going any further, here's a super minimal gist of how to use Formik with
React Native that demonstrates the key differences:

```
1// Formik x React Native example2importReactfrom'react';3import{Button,TextInput,View}from'react-native';4import{Formik}from'formik';56exportconstMyReactNativeForm=props=>(7<Formik8initialValues={{email:''}}9onSubmit={values=>console.log(values)}10>11{({handleChange,handleBlur,handleSubmit,values})=>(12<View>13<TextInput14onChangeText={handleChange('email')}15onBlur={handleBlur('email')}16value={values.email}17/>18<ButtononPress={handleSubmit}title="Submit"/>19</View>20)}21</Formik>22);
```

As you can see above, the notable differences between using Formik with React
DOM and React Native are:

- Formik'shandleSubmitis passed to a<Button onPress={...} />instead of HTML<form onSubmit={...} />component (since there is no<form />element in React Native).
`handleSubmit`
`<Button onPress={...} />`
`<form onSubmit={...} />`
`<form />`
- <TextInput />uses Formik'shandleChange(fieldName)andhandleBlur(fieldName)instead of directly assigning the callbacks to props, because we have to get thefieldNamefrom somewhere and with React Native we can't get it automatically like in web (using input name attribute). You can also usesetFieldValue(fieldName, value)andsetFieldTouched(fieldName, bool)as an alternative.
`<TextInput />`
`handleChange(fieldName)`
`handleBlur(fieldName)`
`fieldName`
`setFieldValue(fieldName, value)`
`setFieldTouched(fieldName, bool)`

#### On this page

#### Resources

- Docs
- Learn
- Guides
- API Reference
- Blog

#### Community

- User Showcase
- Funding
- Community Chat
- Project Forum
- Releases
- Star

#### About Formium

- Home
- GitHub
- Twitter
- Contact Sales

#### Subscribe to our newsletter

The latest Formik news, articles, and resources, sent to your inbox.