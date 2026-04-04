# Source: https://docs.xano.com/xanoscript/filter-reference/comparison.md

# Source: https://docs.xano.com/the-function-stack/filters/comparison.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Comparison

Comparison filters are useful for comparisons and checking data types, especially for conditional logic. They will result in a true or false boolean value.

* [**bitwise\_not**](/the-function-stack/filters/comparison#bitwise_not) - Returns the existing value with its bits flipped.
* [**equals**](/the-function-stack/filters/comparison#equals) - Returns a boolean if both values are equal.
* [**even**](/the-function-stack/filters/comparison#even) - Returns whether or not the value is even.
* [**greater\_than**](/the-function-stack/filters/comparison#greater_than) - Returns a boolean if the left value is greater than the right value.
* [**greater\_than\_or\_equal**](/the-function-stack/filters/comparison#greater_than_or_equal) - Returns a boolean if the left value is greater than or equal to the right value.
* [**in**](/the-function-stack/filters/comparison#in) - Returns whether or not the value is in the array.
* [**is\_array**](/the-function-stack/filters/comparison#is_array) - Returns whether or not the value is a numerical indexed array.
* [**is\_bool**](/the-function-stack/filters/comparison#is_bool) - Returns whether or not the value is a boolean.
* [**is\_decimal**](/the-function-stack/filters/comparison#is_decimal) - Returns whether or not the value is a decimal value.
* [**is\_empty**](/the-function-stack/filters/comparison#is_empty) - Returns whether or not the value is empty ("", null, 0, \[], \{}).
* [**is\_int**](/the-function-stack/filters/comparison#is_int) - Returns whether or not the value is an integer.
* [**is\_null**](/the-function-stack/filters/comparison#is_null) - Returns whether or not the value is null
* [**is\_object**](/the-function-stack/filters/comparison#is_object) - Returns whether or not the value is an object.
* [**is\_text**](/the-function-stack/filters/comparison#is_text) - Returns whether or not the value is text.
* [**less\_than**](/the-function-stack/filters/comparison#less_than) - Returns a boolean if the left value is less than the right value
* [**less\_than\_or\_equal**](/the-function-stack/filters/comparison#less_than_or_equal) - Returns a boolean if the left value is less than or equal to the right value
* [**not**](/the-function-stack/filters/comparison#not) - Returns the opposite of the existing value evaluated as a boolean
* [**not\_equals**](/the-function-stack/filters/comparison#not_equals) - Returns a boolean if both values are not equal
* [**odd**](/the-function-stack/filters/comparison#odd) - Returns whether or not the value is odd

#### **bitwise\_not**

Returns the existing value with its bits flipped.

#### **equals**

Returns a boolean if both values are equal\*\*.\*\*

<Frame caption="var_2 is also 7, so in this example, the result will be true.">
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/236f8009-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=eefbd77cf889da98989e42d3ceff9295" width="596" height="474" data-path="images/236f8009-image.jpeg" />
</Frame>

#### even

Returns whether or not the value is even, this returns a response of true or false.

<Frame caption="In this example, we have a variable with the int 23 after applying the even filter the variable becomes false.">
  <img src="https://mintcdn.com/xano-997cb9ee/-vy8_DWVOwkWo8Bt/images/81c51e2a-image.jpeg?fit=max&auto=format&n=-vy8_DWVOwkWo8Bt&q=85&s=1cf23bf6422f3227b87e7ec4db2bd090" width="595" height="427" data-path="images/81c51e2a-image.jpeg" />
</Frame>

#### greater\_than

Returns a boolean if the left value is greater than the right value.

<Frame caption="The result will be true because 23 is greater than 5.">
  <img src="https://mintcdn.com/xano-997cb9ee/NAqNmVIgcJlXegps/images/03803791-image.jpeg?fit=max&auto=format&n=NAqNmVIgcJlXegps&q=85&s=149bfa87cc7ee071375609e64e5e8f37" width="594" height="474" data-path="images/03803791-image.jpeg" />
</Frame>

#### greater\_than\_or\_equal

Returns a boolean if the left value is greater than or equal to the right value.

<Frame caption="The result will be true because 23 is equal to 23.">
  <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/a6b1a6fb-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=0fac2e5af24fdeeb7246f68561eacf0f" width="593" height="464" data-path="images/a6b1a6fb-image.jpeg" />
</Frame>

#### in

Returns whether or not the value is in the Array, this returns a response of true or false.

<Frame caption="var_2 is the array [1,2,7,23]. The result will be true because 23 is IN the array.">
  <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/42403def-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=e44998eecfd99346a9ee6160f49e8a24" width="599" height="473" data-path="images/42403def-image.jpeg" />
</Frame>

#### is\_array

Returns whether or not the value is a numerical indexed array.

<Frame caption="var2 is the array [1,2,7,23]. The result will be true because var_2 is an array.">
  <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/5f2f3cef-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=bba3c5b0aba24cb0750bd66a2badb765" width="592" height="429" data-path="images/5f2f3cef-image.jpeg" />
</Frame>

#### is\_bool

Returns whether or not the value is a boolean.

<Frame caption="False is a boolean so the result will be true.">
  <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/5800b5b0-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=5fbe6ca8651c470656fc7f862704284d" width="593" height="411" data-path="images/5800b5b0-image.jpeg" />
</Frame>

#### is\_decimal

Returns whether or not the value is a decimal value.

<Frame caption="9.86 is a decimal so the result will be true.">
  <img src="https://mintcdn.com/xano-997cb9ee/NAqNmVIgcJlXegps/images/05f9b671-image.jpeg?fit=max&auto=format&n=NAqNmVIgcJlXegps&q=85&s=c01adddd822ef6ca51cbb9eafccd52c2" width="593" height="444" data-path="images/05f9b671-image.jpeg" />
</Frame>

#### is\_empty

Returns whether or not the value is empty ("", null, 0, \[], \{}).

<Frame caption="The result will be true because the value is an empty object {}.">
  <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/a93522e0-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=bfc484ed3545714118942c57bf1cb1a7" width="589" height="423" data-path="images/a93522e0-image.jpeg" />
</Frame>

#### is\_int

Returns whether or not the value is an integer.

<Frame caption="-9 is an integer so the result will be true.">
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/293563e6-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=0236fbdbfff9aeb7befca65e6a0db8a9" width="590" height="426" data-path="images/293563e6-image.jpeg" />
</Frame>

#### is\_null

Returns whether or not the value is null, this returns a response of true or false.

<Frame caption="In this example, we have a variable with the int 23 after applying the is_null filter the variable becomes false.">
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/235cda04-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=a875eb2e3bc2d6fbe1f023899804ab84" width="591" height="418" data-path="images/235cda04-image.jpeg" />
</Frame>

#### is\_object

Returns whether or not the value is an object.

<Frame caption="The result is true because the value is an object {}.">
  <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/74c29006-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=e109158f31b2feb56486a04eefa1537b" width="590" height="425" data-path="images/74c29006-image.jpeg" />
</Frame>

#### is\_text

Returns whether or not the value is text.

<Frame caption="Hello there is a text string so the result will be true.">
  <img src="https://mintcdn.com/xano-997cb9ee/dyVYERTquSXdpw_-/images/9fdbc7e8-image.jpeg?fit=max&auto=format&n=dyVYERTquSXdpw_-&q=85&s=29e3747bec3fc70874cbf913882314e5" width="590" height="435" data-path="images/9fdbc7e8-image.jpeg" />
</Frame>

#### less\_than

Returns a boolean if the left value is less than the right value

<Frame caption="The result will be true because 5 is less than 12.">
  <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/91a4f60f-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=bcadae25f90bfd9cc908e53d13aed1af" width="595" height="445" data-path="images/91a4f60f-image.jpeg" />
</Frame>

#### less\_than\_or\_equal

Returns a boolean if the left value is less than or equal to the right value.

<Frame caption="5 is not less than or equal to 1 so the result will be false.">
  <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/eaffb5e2-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=e9f4d99c1d85b1047f2fe708952f1a16" width="591" height="451" data-path="images/eaffb5e2-image.jpeg" />
</Frame>

#### not

Returns the opposite of the existing value evaluated as a boolean.

<Frame caption="In this example, we first have the odd filter applied to 5 which results in a true boolean. Then, the not filter is applied resulting in the opposite existing value - making the result false.">
  <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/d9f41519-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=e34843293ebd15f7dd2d9c1ed968fb70" width="592" height="451" data-path="images/d9f41519-image.jpeg" />
</Frame>

#### not\_equals

Returns a boolean if both values are not equal.

<Frame caption="The result will be true because 5 is not equal to 6.">
  <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/43c335f6-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=0a91f4fb04b8002b85bcff25a73c4d4f" width="591" height="474" data-path="images/43c335f6-image.jpeg" />
</Frame>

#### odd

Returns whether or not the value is odd, this returns a response of true or false.

<Frame caption="5 is an odd number so the result will be true.">
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/294158b1-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=a2fddbe078940334a4a970a3a2c9819d" width="594" height="401" data-path="images/294158b1-image.jpeg" />
</Frame>


Built with [Mintlify](https://mintlify.com).