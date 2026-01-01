# Formik Documentation
# Source: https://formik.org/docs/guides/arrays
# Path: /docs/guides/arrays

#### Documentation

#### API Reference

#### Documentation

#### API Reference

# Arrays and Nested Objects

Formik has support for nested objects and arrays out of the box. These subjects are somewhat related because they both leverage the same syntax.

## Nested Objects

Thenameprops in Formik can use lodash-like dot paths to reference nested Formik values. This means that you do not need to flatten out your form's values anymore.

`name`

```
1importReactfrom'react';2import{Formik,Form,Field}from'formik';34exportconstNestedExample=()=>(5<div>6<h1>Social Profiles</h1>7<Formik8initialValues={{9social:{10facebook:'',11twitter:'',12},13}}14onSubmit={values=>{15// same shape as initial values16console.log(values);17}}18>19<Form>20<Fieldname="social.facebook"/>21<Fieldname="social.twitter"/>22<buttontype="submit">Submit</button>23</Form>24</Formik>25</div>26);
```

## Arrays

Formik also has support for arrays and arrays of objects out of the box. Using lodash-like bracket syntax fornamestring you can quickly build fields for items in a list.

`name`

```
1importReactfrom'react';2import{Formik,Form,Field}from'formik';34exportconstBasicArrayExample=()=>(5<div>6<h1>Friends</h1>7<Formik8initialValues={{9friends:['jared','ian'],10}}11onSubmit={values=>{12// same shape as initial values13console.log(values);14}}15>16<Form>17<Fieldname="friends[0]"/>18<Fieldname="friends[1]"/>19<buttontype="submit">Submit</button>20</Form>21</Formik>22</div>23);
```

For more information around manipulating (add/remove/etc) items in lists, see the API reference section on the<FieldArray>component.

`<FieldArray>`

## Avoid nesting

If you want to avoid this default behavior Formik also has support for it to have fields with dots.

```
1importReactfrom'react';2import{Formik,Form,Field}from'formik';34exportconstNestedExample=()=>(5<div>6<h1>Social Profiles</h1>7<Formik8initialValues={{9'owner.fullname':'',10}}11onSubmit={values=>{12// same shape as initial values13console.log(values);14}}15>16<Form>17<Fieldname="['owner.fullname']"/>18<buttontype="submit">Submit</button>19</Form>20</Formik>21</div>22);
```

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