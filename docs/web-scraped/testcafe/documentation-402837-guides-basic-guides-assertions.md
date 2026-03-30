# Source: https://testcafe.io/documentation/402837/guides/basic-guides/assertions

Title: Assertions | Basic Guides | Guides

URL Source: https://testcafe.io/documentation/402837/guides/basic-guides/assertions

Markdown Content:
[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#article-summary)Article Summary[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#article-summary)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Assertions allow you to compare the **actual** state of your application to your **expectations**. Assertions are necessary to **conclusively** determine [test success](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#why-use-assertions).

Assertions begin with the invocation of the [t.expect](https://testcafe.io/documentation/402702/reference/test-api/testcontroller/expect) method. The following simple assertion compares variable _x_ to variable _y_ and succeeds if the two are equal:

```
await t.expect(x).eql(y);
```

The [left side of the assertion](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#the-first-operand) can contain asynchronous functions that extract information from the page. TestCafe offers [a set of assertion methods](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#assertion-methods) that compare and evaluate assertion operands. TestCafe employs the [Smart Assertion Query Mechanism](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#smart-assertion-query-mechanism) to eliminate false negatives.

[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#table-of-contents)Table of Contents[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#table-of-contents)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Why use assertions](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#why-use-assertions)
    *   [Examples](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#examples)

*   [Assertion structure](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#assertion-structure)
    *   [The assertion declaration](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#the-assertion-declaration)
    *   [The first operand](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#the-first-operand)
    *   [The assertion method](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#the-assertion-method)
    *   [The second operand](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#the-second-operand)
    *   [How to chain assertions](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#how-to-chain-assertions)

*   [Use assertions to extract page information](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#use-assertions-to-extract-page-information)
    *   [Common Errors and Best Practices](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#common-errors-and-best-practices)

*   [Assertion methods](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#assertion-methods)
    *   [Strict equality](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#strict-equality)
    *   [Value comparison](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#value-comparison)
    *   [Superset](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#superset)
    *   [Numeric range check](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#numeric-range-check)
    *   [Truthiness check](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#truthiness-check)
    *   [Type check](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#type-check)
    *   [Regular expression check](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#regular-expression-check)

*   [Assertion options](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#assertion-options)
    *   [Custom error message](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#custom-error-message)
    *   [Assertion timeout](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#assertion-timeout)
    *   [Allow Unawaited Promise](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#allow-unawaited-promise)

*   [How Assertions Work](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#how-assertions-work)
    *   [Smart Assertion Query Mechanism](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#smart-assertion-query-mechanism)

*   [Debug Assertions](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#debug-assertions)

[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#why-use-assertions)Why use assertions[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#why-use-assertions)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tests without an explicit **success condition** are inconclusive.

If one of the following errors occurs, the test automatically fails:

1.   TestCafe **cannot reach** the test page URL.
2.   TestCafe **cannot perform a test action** — for example, if the target element does not exist.
3.   Your website **throws a [JavaScript error](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors)**.

But you still don’t know if test actions have had the desired effect. That’s why you should add **assertions** (custom success conditions) to your test.

### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#examples)Examples[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#examples)

If your test includes a log-in routine, you may use assertions to perform the following checks:

1.   Log-in status check

Confirm that the log-in routine has been successful. Check the page for items that are invisible to unauthenticated users:

```
await t.expect(Selector('#account-preferences').filterVisible().exists).ok();
```
2.   User check

Check that the page displays the correct username.

```
await t.expect(Selector('#user-name').innerText).contains('Jane Doe');
```
3.   Cookies check

Confirm that the user [received the cookies](https://testcafe.io/documentation/403873/reference/test-api/testcontroller/getcookies) necessary to continue the session:

```
let cookies = await t.getCookies({ domain: 'yourwebsite.com' });
await t.expect(cookies.length).eql(2);
```

[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#assertion-structure)Assertion structure[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#assertion-structure)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following simple assertion compares variable _x_ to variable _y_ and succeeds if the two are equal:

![Image 1: await t.expect(x).eql(y);](https://testcafe.io/images/assertions/assertion-structure.svg)

This assertion consists of the following parts:

### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#the-assertion-declaration)The assertion declaration[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#the-assertion-declaration)

Assertions start with the invocation of the `t.expect` method. Assertions are [asynchronous](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#how-assertions-work) methods, and require the use of the `await` keyword.

You can declare an assertion in any function that has access to the [Test Controller](https://testcafe.io/documentation/402665/reference/test-api/testcontroller), such as the [test body](https://testcafe.io/documentation/403366/reference/test-api/test), [test hooks](https://testcafe.io/documentation/403435/guides/intermediate-guides/hooks), and [Role definitions](https://testcafe.io/documentation/402845/guides/intermediate-guides/authentication). Manually import the TestController object to declare assertions elsewhere.

### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#the-first-operand)The first operand[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#the-first-operand)

The first operand indicates the **actual** state of the application. It can contain an asynchronous function that [extracts page information](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#use-assertions-to-extract-page-information):

```
await t.expect(Selector('#article-header').innerText).contains('10 Best Vacation Spots');
```

When you pass [a compatible function](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#use-assertions-to-extract-page-information) to the assertion, TestCafe engages the [Smart Assertion Query Mechanism](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#smart-assertion-query-mechanism). If the function fails the first time, TestCafe executes it again to account for possible client-side changes.

### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#the-assertion-method)The assertion method[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#the-assertion-method)

The assertion method determines the nature of the comparison. For example. the `eql` assertion method succeeds when the two operands are equal. See the [assertion methods](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#assertion-methods) section for an overview of available assertion methods.

### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#the-second-operand)The second operand[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#the-second-operand)

The second operand indicates the **expected value** of the assertion’s first operand. The second operand of the assertion **cannot** contain a function.

### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#how-to-chain-assertions)How to chain assertions[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#how-to-chain-assertions)

You can [chain](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#action-chaining) assertions with other TestController methods:

```
// TestCafe executes the 'click' action after the assertion:
t.expect(x).eql(y).click('#button');
```

You can only chain **complete** assertions:

```
// The test fails to start because the assertion is incomplete:
t.expect(x).click('#button');
```

To extract information from the page, pass an asynchronous function to [the first operand](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#the-first-operand).

If the function fails, TestCafe retries it multiple times within [the assertion timeout](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#assertion-timeout). See [Smart Assertion Query Mechanism](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#smart-assertion-query-mechanism) for more information.

TestCafe automatically awaits the following functions:

*   [Client functions](https://testcafe.io/documentation/402671/reference/test-api/clientfunction)

```
const getLocationPart = ClientFunction(locationPart => {
    return window.location[locationPart];
});

await t.expect(getLocationPart('host')).eql('devexpress.github.io');
```
*   [Selector](https://testcafe.io/documentation/402666/reference/test-api/selector) property invocations

```
await t.expect(Selector('#article-header').innerText).contains('10 Best Vacation Spots');
```
*   Two [RequestLogger](https://testcafe.io/documentation/402668/reference/test-api/requestlogger) methods — [count](https://testcafe.io/documentation/402767/reference/test-api/requestlogger/count) and [contains](https://testcafe.io/documentation/402768/reference/test-api/requestlogger/contains)

```
import { RequestLogger } from 'testcafe';

const logger = RequestLogger();

fixture('RequestLogger')
    .page('https://devexpress.github.io/testcafe/example/')
    .requestHooks(logger);

test('Check request', async t => {
    await t.expect(logger.count()).ok();
    await t.expect(logger.contains(record => record.response.statusCode === 200)).ok();
});
```
*   [HTTP requests and responses](https://testcafe.io/documentation/403981/reference/test-api/testcontroller/request)

```
const responseBody = t.request('http://localhost:3000/helloworld').body;
await t.expect(responseBody).contains('Hello World');
```

### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#common-errors-and-best-practices)Common Errors and Best Practices[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#common-errors-and-best-practices)

*   Do not place Selector queries **without properties** into the left-hand side of the assertion:

```
test('test', async t => {
    await t
    .typeText('input', '123')
    .expect(Selector('input')).contains('123'); // fails
});
```
*   If you place the`await` keyword into the left-hand side of the assertion, TestCafe **does not enage** the Smart Assertion Query Mechanism.

```
test('test', async t => {
    await t
    .typeText('input', '123')
    .expect(await Selector('input').value).eql('123');
});
```
*   If you pass the result of Selector evaluation to the assertion, TestCafe **does not enage** the Smart Assertion Query Mechanism.

```
test('test', async t => {

const buttonValue = await Selector('#btn').textContent; // The constant stores the return value of the Selector query. 

await t.expect(buttonValue).contains('Loading...'); // This assertion compares two static values. if the assertion fails, TestCafe does not retry it, because the result would not change.

await t.expect(Selector('#btn').textContent).contains('Loading...'); // This assertion contians a proper Selector query. TestCafe retries the assertion in case of failure.
});
```
*   Do not place a function that returns a promise in the left hand-side of the assertion.

[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#assertion-methods)Assertion methods[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#assertion-methods)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TestCafe offers a comprehensive set of assertion methods.

Different assertion methods require different arguments. For example, the `within` method requires **two** numeric arguments. The `ok` and `notOk` methods are Boolean, and do not require an argument. Refer to the documentation of a specific assertion method for more information.

We can divide assertion methods into groups based on their mathematical function:

*   [Strict equality](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#strict-equality)
    *   [eql (X = Y)](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#eql-x--y)
    *   [notEql (X ≠ Y)](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#noteql-x--y)

*   [Value comparison](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#value-comparison)
    *   [gt (X > Y)](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#gt-x--y)
    *   [gte (X ≥ Y)](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#gte-x--y)
    *   [lte (X ≤ Y)](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#lte-x--y)
    *   [lt (X < Y)](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#lt-x--y)

*   [Superset](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#superset)
    *   [contains (Y ∈ X)](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#contains-y--x)
    *   [notContains (Y ∉ X)](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#notcontains-y--x)

*   [Numeric range check](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#numeric-range-check)
    *   [within (X ∈ [Yᵃ, Yᵇ])](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#numeric-range-check)
    *   [notWithin (X ∉ [Yᵃ, Yᵇ])](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#numeric-range-check)

*   [Truthiness check](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#truthiness-check)
    *   [ok (⊤X)](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#ok-x)
    *   [notOK (⊥X)](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#notok-x)

*   [Type check](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#type-check)
    *   [typeOf (X ∈ type Y)](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#typeof-x--type-y)
    *   [notTypeOf (X ∉ type Y)](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#nottypeof-x--type-y)

*   [Regular expression check](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#regular-expression-check)
    *   [match](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#match)
    *   [notMatch](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#notmatch)

### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#strict-equality)Strict equality[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#strict-equality)

The following assertion methods perform a strict equality check:

#### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#eql-x--y)eql (X = Y)[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#eql-x--y)

**Method reference**: [eql](https://testcafe.io/documentation/402728/reference/test-api/testcontroller/expect/eql)

**Examples**:

```
// successful assertions:
await t.expect(20).eql(20);
await t.expect('20').eql('20');
await t.expect({ username: 'steve@example.com' }).eq({ username: 'steve@example.com' });

// failed assertions:
await t.expect(15).eql(20);
await t.expect('20').eql('15');
await t.expect({ username: 'steve@example.com' }).eq({ username: 'dave@example.com' });
// invalid assertions:
await t.expect('20').eql(20); // operand data types don't match
```

#### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#noteql-x--y)notEql (X ≠ Y)[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#noteql-x--y)

**Method reference**: [notEql](https://testcafe.io/documentation/402721/reference/test-api/testcontroller/expect/noteql)

**Examples**:

```
// successful assertions:
await t.expect(15).notEql(20);
await t.expect('20').notEql('15');
await t.expect({ username: 'steve@example.com' })notEql({ username: 'dave@example.com' });

// failed assertions:
await t.expect(20).notEql(20);
await t.expect('20').notEql('20');
await t.expect({ username: 'steve@example.com' })notEql({ username: 'steve@example.com' });

// invalid assertions:
await t.expect('20').notEql(20);  // operand data types don't match
```

### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#value-comparison)Value comparison[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#value-comparison)

The following assertion methods compare two numeric values:

#### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#gt-x--y)gt (X > Y)[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#gt-x--y)

**Method reference**: [gt](https://testcafe.io/documentation/402727/reference/test-api/testcontroller/expect/gt)

**Examples**:

```
const today = new Date(); // current date
const lovelessReleaseDate = new Date(1991, 10, 4); // November 4th, 1991

// successful assertions:
await t.expect(20).gt(15)
await t.expect(today).gt(lovelessReleaseDate);

// failed assertions:
await t.expect(15).gt(15)
await t.expect(lovelessReleaseDate).gt(today);

// invalid assertions:
await t.expect('16').gt(15); // invalid data type (string)
await t.expect(today).gt(15); // operand data types don't match
```

#### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#gte-x--y)gte (X ≥ Y)[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#gte-x--y)

**Method reference**: [gte](https://testcafe.io/documentation/402726/reference/test-api/testcontroller/expect/gte)

**Examples**:

```
const today = new Date(); // current date
const lovelessReleaseDate = new Date(1991, 10, 4); // November 4th, 1991

// successful assertions:
await t.expect(20).gte(15);
await t.expect(15).gte(15);
await t.expect(today).gte(lovelessReleaseDate);
await t.expect(today).gte(today);

// failed assertions:
await t.expect(14).gte(15);
await t.expect(lovelessReleaseDate).gte(today);

// invalid assertions:
await t.expect('16').gte(15); // invalid data type (string)
await t.expect(today).gte(15); // operand data types don't match
```

#### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#lte-x--y)lte (X ≤ Y)[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#lte-x--y)

**Method reference**: [lte](https://testcafe.io/documentation/402724/reference/test-api/testcontroller/expect/lte)

**Examples**:

```
const today = new Date(); // current date
const lovelessReleaseDate = new Date(1991, 10, 4); // November 4th, 1991

// successful assertions:
await t.expect(14).lte(15);
await t.expect(15).lte(15);
await t.expect(lovelessReleaseDate).lte(today);
await t.expect(today).lte(today);

// failed assertions:
await t.expect(20).lte(15);
await t.expect(today).lte(lovelessReleaseDate);

// invalid assertions:
await t.expect('14').lte(15) // invalid data type (string)
await t.expect(today).lte(15) // operand data types don't match
```

#### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#lt-x--y)lt (X < Y)[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#lt-x--y)

**Method reference**: [lt](https://testcafe.io/documentation/402725/reference/test-api/testcontroller/expect/lt)

```
const today = new Date(); // current date
const lovelessReleaseDate = new Date(1991, 10, 4); // November 4th, 1991

// successful assertions:
await t.expect(14).lt(15)
await t.expect(lovelessReleaseDate).lt(today);

// failed assertions:
await t.expect(15).lt(15)
await t.expect(today).lt(lovelessReleaseDate);

// invalid assertions:
await t.expect('14').lt(15); // invalid data type (string)
await t.expect(today).lt(15); // operand data types don't match
```

### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#superset)Superset[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#superset)

The following assertion methods check whether X includes Y:

#### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#contains-y--x)contains (Y ∈ X)[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#contains-y--x)

**Method reference**: [contains](https://testcafe.io/documentation/402729/reference/test-api/testcontroller/expect/contains)

**Examples**:

```
// successful assertions:
await t.expect(['x','y']).contains('y');
await t.expect('Username: steve@example.com').contains('Username');
await t.expect({ username: 'steve@example.com', subscriptionPlan: 'basic' }).contains({ username: 'steve@example.com' });

// failed assertions:
await t.expect(['x','y']).contains('z');
await t.expect('Username: steve@example.com').contains('Password');
await t.expect({ username: 'steve@example.com', subscriptionPlan: 'basic' }).contains({ username: 'dave@example.com' });

// invalid assertions:
await t.expect({ username: 'steve@example.com', subscriptionPlan: 'basic' }).contains('steve@example.com'); // operand data types don't match
```

#### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#notcontains-y--x)notContains (Y ∉ X)[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#notcontains-y--x)

**Method reference**: [notContains](https://testcafe.io/documentation/402722/reference/test-api/testcontroller/expect/notcontains)

**Examples**:

```
// successful assertions:
await t.expect(['x','y']).notContains('z');
await t.expect('Username: steve@example.com').notContains('Password');
await t.expect({ username: 'steve@example.com', subscriptionPlan: 'basic' }).notContains({ username: 'dave@example.com' });

// failed assertions:
await t.expect(['x','y']).notContains('y');
await t.expect('Username: steve@example.com').notContains('Username');
await t.expect({ username: 'steve@example.com', subscriptionPlan: 'basic' }).notContains({ username: 'steve@example.com' });

// invalid assertions:
await t.expect({ username: 'steve@example.com', subscriptionPlan: 'basic' }).notContains('dave@example.com'); // operand data types don't match
```

### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#numeric-range-check)Numeric range check[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#numeric-range-check)

The following assertion methods check whether the Y range of numbers includes X.

#### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#within-x--y%E1%B5%83-y%E1%B5%87)within (X ∈ [Yᵃ, Yᵇ])[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#within-x--y%E1%B5%83-y%E1%B5%87)

**Method reference**: [within](https://testcafe.io/documentation/402714/reference/test-api/testcontroller/expect/within)

**Examples**:

```
await t.expect(10).within(1, 20); // success
await t.expect(22).within(1, 20); // failure

// invalid assertions:
await t.expect(22).within([20, 100]); // the second operand is an array
await t.expect(22).within(1); // insufficient number of range definition arguments
await t.expect(10).within(20, 1); // invalid range definition: 20 is greater than 1
```

#### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#notwithin-x--y%E1%B5%83-y%E1%B5%87)notWithin (X ∉ [Yᵃ, Yᵇ])[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#notwithin-x--y%E1%B5%83-y%E1%B5%87)

**Method reference**:[notWithin](https://testcafe.io/documentation/402717/reference/test-api/testcontroller/expect/notwithin)

**Examples**:

```
await t.expect(22).notWithin(1, 20); // success
await t.expect(10).notWithin(1, 20); // failure

// invalid assertions:
await t.expect(12).notWithin([20, 100]); // the second operand is an array    
await t.expect(22).notWithin(1); // insufficient number of range definition arguments
await t.expect(22).notWithin(20, 1); // invalid range definition: 20 is greater than 1
```

### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#truthiness-check)Truthiness check[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#truthiness-check)

The following assertion methods check the Boolean value of X.

#### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#ok-x)ok (⊤(X))[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#ok-x)

**Method reference**: [ok](https://testcafe.io/documentation/402716/reference/test-api/testcontroller/expect/ok)

```
const inputField = Selector('#developer-name');
const fakeElement = Selector('#this-element-does-not-exist');

// successful assertions:
await t.expect(inputField.exists).ok();
await t.expect('Hello!').ok();

// failed assertions:
await t.expect(fakeElement.exists).ok(); // the element doesn't exist  
await t.expect('').ok(); // the string is empty
await t.expect(null).ok(); // null isn't truthy
await t.expect(undefined).ok(); // undefined isn't truthy
```

#### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#notok-x)notOK (⊥(X))[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#notok-x)

**Method reference**: [notOk](https://testcafe.io/documentation/402719/reference/test-api/testcontroller/expect/notok)

**Examples**:

```
const inputField = Selector('#developer-name');
const fakeElement = Selector('#this-element-does-not-exist');

// successful assertions:
await t.expect(fakeElement.exists).notOk(); // the element doesn't exist  
await t.expect('').notOk(); // the string is empty
await t.expect(null).notOk(); // null is falsy
await t.expect(undefined).notOk(); // undefined is falsy

// failed assertions:
await t.expect(inputField.exists).notOk();
await t.expect('Hello!').notOk();
```

### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#type-check)Type check[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#type-check)

The following assertion methods check whether X belongs to data type Y.

#### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#typeof-x--type-y)typeOf (X ∈ type Y)[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#typeof-x--type-y)

**Method reference**: [typeOf](https://testcafe.io/documentation/402715/reference/test-api/testcontroller/expect/typeof)

**Examples**:

```
await t.expect(12).typeOf('Number'); // success
await t.expect(12).typeOf('Object'); // failure
```

#### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#nottypeof-x--type-y)notTypeOf (X ∉ type Y)[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#nottypeof-x--type-y)

**Method reference**: [notTypeOf](https://testcafe.io/documentation/402718/reference/test-api/testcontroller/expect/nottypeof)

**Examples**:

```
await t.expect(12).notTypeOf('Object'); // success
await t.expect(12).notTypeOf('Number'); // failure
```

### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#regular-expression-check)Regular expression check[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#regular-expression-check)

The following assertion methods check whether X matches the regular expression Y:

#### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#match)match[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#match)

**Method reference**: [match](https://testcafe.io/documentation/402723/reference/test-api/testcontroller/expect/match)

X matches the regular expression Y.

**Examples**:

```
const emailRegex = new RegExp(/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/);

await t.expect('email@email.com').match(emailRegex); // success
await t.expect('email@email.com').match(/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/); // success
await t.expect('email.com').match(emailRegex); // failure
```

#### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#notmatch)notMatch[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#notmatch)

**Method reference**: [notMatch](https://testcafe.io/documentation/402720/reference/test-api/testcontroller/expect/notmatch)

X does not match the regular expression Y.

**Examples**:

```
const emailRegex = new RegExp(/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/);

await t.expect('email.com').notMatch(emailRegex); // success
await t.expect('email.com').notMatch(/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/); // success
await t.expect('email@email.com').notMatch(emailRegex); // failure
```

[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#assertion-options)Assertion options[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#assertion-options)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#custom-error-message)Custom error message[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#custom-error-message)

**Type**: String

You can define a custom error message for the assertion. Pass the string with the message to the assertion method:

```
await t.expect({ a: 'bar' }).eql({ a: 'foo' }, 'this assertion will fail');
```

![Image 2: Assertion Failure Custom Message](https://testcafe.io/images/assertions/assertion-failure-custom-message.png)

### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#assertion-timeout)Assertion timeout[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#assertion-timeout)

**Type**: Number

If an assertion’s first operand contains a **compatible function**, the assertion is subject to the **Smart Assertion Query Mechanism**.

If such an assertion fails, TestCafe executes it again until it meets either of the following criteria:

*   The assertion succeeds.
*   The **assertion timeout** elapses.

```
await t.expect(Selector('h1').innerText).eql('text', 'check element text', { timeout: 20000 });
```

To set the timeout for the entire test run, define the assertion timeout in one of the following ways:

*   Set the [assertionTimeout](https://testcafe.io/documentation/402638/reference/configuration-file#assertiontimeout) configuration file option.
*   Set the [assertion-timeout](https://testcafe.io/documentation/402639/reference/command-line-interface#--assertion-timeout-ms) CLI option.
*   Set the [assertionTimeout](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run#assertiontimeout) Runner API option.

Note

The `timeout` option applies to built-in TestCafe assertion methods. Use the [t.wait()](https://testcafe.io/documentation/402672/reference/test-api/testcontroller/wait) method to specify timeouts for third-party assertion methods ([assert](https://nodejs.org/api/assert.html) or [chai](https://www.chaijs.com/)).

### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#allow-unawaited-promise)Allow Unawaited Promise[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#allow-unawaited-promise)

TestCafe awaits **Promises** from **compatible asynchronous functions**. If your assertion includes a custom function that returns a Promise, the assertion fails.

When you create assertions, avoid the use of custom functions that return a Promise. If you can’t work around this limitation, use the `allowUnawaitedPromise` option:

```
await t
        .expect(new Promise(resolve => setTimeout(resolve, 100)))
        .ok('received a promise', { allowUnawaitedPromise: true });
```

[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#how-assertions-work)How Assertions Work[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#how-assertions-work)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Functional web tests are fundamentally asynchronous. It takes time for the application to respond to user actions.

The application’s reponse speed depends on factors such as the speed of the network, the speed of the database, and front-end animations. Since the response is not immediate, it is often impossible to execute assertions right after the action ends.

Traditional end-to-end frameworks solve this issue with an extra timeout:

![Image 3: Asynchronous Functional Testing with Extra Waiting](https://testcafe.io/images/assertions/extra-waiting.png)

TestCafe improves on this approach with its Smart Assertion Query Mechanism.

### [](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#smart-assertion-query-mechanism)Smart Assertion Query Mechanism[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#smart-assertion-query-mechanism)

If the first operand of an assertion is a [compatible asynchronous function](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#use-assertions-to-extract-page-information) — for example, a Selector property — TestCafe retries the assertion multiple times within [the assertion timeout](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#assertion-timeout).

The [timeout](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#assertion-options) option sets the timeout value on a per-assertion basis. To set the timeout for the entire test run, pass the timeout value to the [assertion-timeout](https://testcafe.io/documentation/402639/reference/command-line-interface#--assertion-timeout-ms) CLI option or the [runner.run](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run) option (Test Runner API).

The test fails if the assertion doesn’t succeed by the end of the timeout period.

![Image 4: TestCafe Smart Assertion Query Mechanism](https://testcafe.io/images/assertions/query-mechanism.png)

**Example:**

Consider the following HTML page:

```
<html>
<body>
    <div id="btn" onclick="window.setTimeout(() => this.textContent = 'Loading...', 100)">Click me!</div>
</body>
</html>
```

When the user clicks the `#btn` element, the browser initiates a 100ms wait period. When the wait period elapses, the browser changes the button’s content.

A regular assertion would fail because the application does not respond instantly. TestCafe accounts for the possibility of a slow reponse, and the following assertion succeeds:

```
test('Button click', async t => {
    const btn = Selector('#btn');

    await t
        .click(btn)
        .expect(btn.textContent).contains('Loading...');
});
```

[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#debug-assertions)Debug Assertions[](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#debug-assertions)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Assertions may fail thanks to a badly written [Element Selector query](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors) or a short [assertion timeout](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#assertion-timeout). Read the [Debug Tests guide](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests) for more information.
