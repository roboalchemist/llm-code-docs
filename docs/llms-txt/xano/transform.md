# Source: https://docs.xano.com/xanoscript/filter-reference/transform.md

# Source: https://docs.xano.com/the-function-stack/filters/transform.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Transform

### Lambda Filters

Higher Order Filters operate on a list of items and process a Lambda individually for each item. The Lambda has access to several context variables that represent various states of the iteration process. Details of each of these context variables are mentioned below.

## map

* **\$this** - the context variable that represents the element of the array being processed.

* **\$index** - the context variable that represents the numerical index of the element of the array being processed

* **\$parent** - the context variable that represents the entire array with all of its elements.

The map filter is extremely powerful because it allows you to easily transform the elements of one array into another. Here is an example of using using a map on a variable that contains a list of user objects. We will convert that into a list of user usernames.

<Frame caption="List of user objects.">
  <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/57b489b1-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=7933a45d820d63c8fd57bc6abf1aa22b" width="590" height="769" data-path="images/57b489b1-image.jpeg" />
</Frame>

<Frame caption="Map filter used to transform the list of user objects">
  <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f59444d5-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=e74f5d9279cd316cd7f118f8c24a4647" width="1529" height="610" data-path="images/f59444d5-image.jpeg" />
</Frame>

<Frame caption="The result is the list of usernames.">
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/38e408b7-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=65eaf4924f9d0ace71e6532eb473745c" width="590" height="340" data-path="images/38e408b7-image.jpeg" />
</Frame>

```java  theme={null}
return $this.username;
```

The above example changes the type of the array. Previously it was an array of user objects, but now it is an array of text. You can also use the map filter to return a subject each object while still maintaining the object type.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/3a95f9f1-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=37a9f55c4705d9dc47c5359842a47e74" width="597" height="505" data-path="images/3a95f9f1-image.jpeg" />
</Frame>

```java  theme={null}
return {id: $this.id, username: $this.username};
```

## some

* **\$this** - the context variable that represents the element of the array being processed.
* **\$index** - the context variable that represents the numerical index of the element of the array being processed.
* **\$parent** - the context variable that represents the entire array with all of its elements.

The some filter (also called \*\*has \*\*or **has any element**) allows you to easily determine if there is at least one element of an array that matches your condition. A common use case would be having an array of role objects and you wanted to see if a certain role was present.

<Frame caption="List of user objects.">
  <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/509289b2-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=7fcaf53d0dde849465cb2f760437639e" width="594" height="823" data-path="images/509289b2-image.jpeg" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/3c3de7eb-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=061beb914b0b8eccf0b517843465a699" width="594" height="479" data-path="images/3c3de7eb-image.jpeg" />
</Frame>

This will generate a true value if a role of admin is found in the array and a false value if it is not.

```java  theme={null}
return $this.role == "admin";
```

## every

* **\$this** - the context variable that represents the element of the array being processed.
* **\$index** - the context variable that represents the numerical index of the element of the array being processed.
* **\$parent** - the context variable that represents the entire array with all of its elements.

This filter (also called **find every element**) is identical to the **some** filter except that it requires that all elements of the array match the condition. A common use case would be a list of products and determining if they all have a price greater than 10.

<Frame caption="In this example, Every filter will determine if every price in the products array is greater than 10.">
  <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/eff78060-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=9902af296a3ab9490d98e209f10748ec" width="592" height="520" data-path="images/eff78060-image.jpeg" />
</Frame>

```java  theme={null}
return $this.price > 10;
```

## find

* **\$this** - the context variable that represents the element of the array being processed.
* **\$index** - the context variable that represents the numerical index of the element of the array being processed.
* **\$parent** - the context variable that represents the entire array with all of its elements.

This filter (also called **find first element**) is identical to the **some** filter except that it returns the actual element that matches the condition instead of returning whether or not it was found. A common use case would be finding the first product that has a price greater than 10.

<Frame caption="In this example, the first product object with a price greater than 10 will be returned.">
  <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e9462114-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=294f0392d20a328c3a577db537bf9322" width="585" height="519" data-path="images/e9462114-image.jpeg" />
</Frame>

```java  theme={null}
return $this.price > 10;
```

## findIndex

* **\$this** - the context variable that represents the element of the array being processed.
* **\$index** - the context variable that represents the numerical index of the element of the array being processed.
* **\$parent** - the context variable that represents the entire array with all of its elements.

This filter (also called **find first element index**) is identical to the **some** filter except that it returns the index of the element that matches the condition instead of returning whether or not it was found. A common use case would be finding the index of the first product that has a price greater than 10.

<Frame caption="In this example, findIndex will return the first element index where the price is greater than 10.">
  <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/8fbd16e6-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=3854dbe8fa3db5987132e865acf86c72" width="593" height="511" data-path="images/8fbd16e6-image.jpeg" />
</Frame>

```java  theme={null}
return $this.price > 10;
```

## filter

* **\$this** - the context variable that represents the element of the array being processed.
* **\$index** - the context variable that represents the numerical index of the element of the array being processed.
* **\$parent** - the context variable that represents the entire array with all of its elements.

This filter (also called **find all elements**) is identical to the **find** filter except that it returns it returns all elements that match the condition. Even if there is only one match, it would return an array of one. A common use case would be finding all products that have a price greater than 10.

<Frame caption="In this example, filter will return all elements where the price is greater than 10.">
  <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/8f564686-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=76fcc7bb7340abe9c52e80523eb1ec3f" width="592" height="482" data-path="images/8f564686-image.jpeg" />
</Frame>

```java  theme={null}
return $this.price > 10;
```

## reduce

* **\$this** - the context variable that represents the element of the array being processed.
* **\$index** - the context variable that represents the numerical index of the element of the array being processed.
* **\$parent** - the context variable that represents the entire array with all of its elements.
* **\$result** - the context variable that is used to represent the result of the previous iteration or the initial value on the first iteration.

This reduce filter is a bit more complicated than the higher order examples because its environment changes each time the Lambda is processed. The reduce filter starts out with an initial value (normally 0) and then is responsible for turning the array into a single result. Because of this, there is a new context variable named `$result` which can be referenced. The `$result` variable is the state of the reduction process. The first time the Lambda runs, the `$result` variable is the same as the initial variable. The return statement of the Lambda will be the `$result` variable for the 2nd iteration and so forth until there are no iterations left. The final value of the `$result` variable will be assigned to whatever is referencing the reduce filter.

The details above may feel like a mouthful, but things should start to click when seeing a few examples.

The most basic example would be sum a list of values.

<Frame caption="Here's an example array of [1, 10, 100].">
  <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f390c272-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=fac0c769377b4ba5b54f7b54ad2102ed" width="586" height="710" data-path="images/f390c272-image.jpeg" />
</Frame>

<Frame caption="In this example, the reduce filter will result in a sum of the array or 111.">
  <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/57608a8c-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=dfaae77a2d93fa3cbe6230d85cc3deb1" width="590" height="417" data-path="images/57608a8c-image.jpeg" />
</Frame>

Using an initial value of 0 we would get the sum of numbers with the following Lambda.

```php  theme={null}
return $this + $result;
```

If the above example was a list of objects instead of a list of scalar values, then the Lambda would change slightly.

<Frame caption="In this example, we have an array of objects.">
  <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/96f7fe0e-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=ead1a7dd5f5718d3bc88fd4be306b8b3" width="573" height="277" data-path="images/96f7fe0e-image.jpeg" />
</Frame>

<Frame caption="Using the reduce filter in this example, we sum the values of num for each object resulting in 111.">
  <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/cccbc720-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=1778417611c18737a08aa920709fc96e" width="592" height="295" data-path="images/cccbc720-image.jpeg" />
</Frame>

```php  theme={null}
return $this.num + $result;
```


Built with [Mintlify](https://mintlify.com).