# Source: https://docs-containers.back4app.com/docs/react-native/graphql/users/working-with-users.md

---
title: Working with Users
slug: docs/react-native/graphql/users/working-with-users
description: In this guide you will get a brief intro about core functions for users on Back4App
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-20T13:11:54.004Z
updatedAt: 2025-01-17T14:13:22.299Z
---

# Working with Users

## Introduction

At the core of many apps, user accounts have a notion that lets users securely access their information. At Back4App/Parse provides a specialized user class called Parse.User that automatically handles much of the functionality required for user account management.

We will better explain how this class works by giving you a practical guide on making a user sign up, a user log-in, and a user logout. In the next tutorials, let’s understand how to implement each one in a React Native application using GraphQL and Relay.

## Goal

Explain the Parse.User class and how Relay will handle with this class.

## Parse User Class

Parse.User is a subclass of Parse.Object, and has all the same features, such as flexible schema, automatic persistence, and a key-value interface. All the methods on Parse.Object also exist in Parse.User. The difference is that Parse.User has some special additions specific to user accounts.

## Parse.User Properties

Parse.User has several values that set it apart from Parse.Object:

- username: The username for the user (required).
- password: The password for the user (required on signup).
- email: The email address for the user (optional).

We’ll go through each of these in detail as we run through the various use cases for users.

## Relay Mutation

A way to handle the User class on a front end with Relay in React Native is using Mutations. Mutations are responsible for creating functions, executing them, sending the data to the backend, and expecting a return. Any Mutation function will prepare the data to send it. When returned from the backend, handle the success or error scenario. In both cases, the application can control the next state and decide what will happen after.

This guide is using Relay Modern on the frontend to consume GraphQL. The flow to create a mutation is similar to create a query or fragment.

The Relay Mutation needs to be equal to the backend specification. When creating a new Mutation, the Relay Compiler will check if the backend structure is identical to the application/frontend source of truth, the schema.graphql.

Every Relay Mutation will have a principal function called commitMutation. This function handles the GraphQL fragment, the input variables, the completed, and the error callback. The Relay Mutation can have other arguments, but in the next tutorials won’t be used.

## commitMutation

commitMutation is the default function to create and execute mutations in your GraphQL on the client-side. Similar to QueryRenderer, the commitMutation will receive props. These props, combine in themselves, will prepare the fetch, call the server, and handle the return.

There so many props to handle your application on each case that it needs. But, in the next tutorials, it will use only the next one:

- environment: The environment is responsible for the store and network of applications.
- input is an object that contains the variables necessary to resolve the mutation.
- onCompleted and onError: are functions, as the name says, called when the mutation is complete. The onCompleted is for success and onError for error.

Example of commitMutation:

```javascript
1	function commit({environment, input, onCompleted, onError}) {
2	  const variables = {input};
3	
4	  commitMutation(environment, {
5	    mutation,
6	    variables,
7	    onCompleted,
8	    onError,
9	  });
10	}
11	
12	export default {
13	  commit,
```

:::hint{type="info"}
For more info about Relay Mutation go to the [**official docs**](https://relay.dev/docs/en/mutations).
:::

## Conclusion

Now, the mutation concept is clear and explained. In the next tutorial, it will handle the Sign Up flow on Back4App. There it will be specified how to implement a simple mutation to register a new user and return a session token.
