# Source: https://docs.bugbug.io/editing-tests/components.md

# Components

## What are components?

Components are groups of steps that are shared across multiple tests. So basically, if you don't want to repeat the most often-used steps, such as visiting the main page and logging in using valid credentials, you create a new component that will contain all those steps and use it easily, and fast across all your tests that will require this action.

## Why use components?

Once you create a new component, remember that **when you change something inside that group it will be changed in all tests where you used that group.**

**To save time!** This can save you time when you want to work with test automation for complex products. With components, you can change your test only once, instead of [re-recording the steps](https://docs.bugbug.io/recording-tests-steps/re-recording-steps) hundreds of times or manually copy-pasting them between tests.

**How many components do you need?** It's better to have more than less. It's not a problem if all your groups are components.

{% hint style="info" %}
**Example:** make a component from `click` action on your "Sign up" button. All your tests that [test user registration](https://docs.bugbug.io/variables#test-user-registration-and-login-using-variables) can now use such a component and if you change the "Sign up" button [selector](https://docs.bugbug.io/preventing-failed-tests/selectors) in the future you can do it only once.
{% endhint %}

## Where are the components?

The "Components" module can be found under the same name in the main navigation. For starters, the list is empty, but this will change as soon as new components are added.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FBV1qnkgpnr2959zTbr0z%2F1emptyScreen.png?alt=media&#x26;token=0d51c2f4-7034-4ae9-aa6c-120eb16a34fd" alt=""><figcaption><p>Components page</p></figcaption></figure>

### Components list

When new components are added, they will be displayed on the list, where those that are used in the most tests are displayed at the top.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FQWUlTh6thQVuGq3g4fub%2F3listOfComponents.png?alt=media&#x26;token=79690ecb-c519-41c9-97bf-d45c86a499c0" alt=""><figcaption><p>Components list</p></figcaption></figure>

## How to make a reusable component?

Firstly you need to have a group of steps that are repeatable and useful in many tests.

1. [Group test steps](https://docs.bugbug.io/editing-tests/grouping-steps)
2. Make a component from this group

To create a component go to test view and choose the group of steps that will become your one component. Then click on the `MAKE COMPONENT` button on their group name.&#x20;

**From now on, every change you make in this component will also apply to other tests that have this component.**&#x20;

{% hint style="info" %}
**Tip:** Use "[new test from here](https://docs.bugbug.io/creating-tests/new-test-from-here)" to quickly work with tests that use components.
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fglpy1G5YbYf42aVqp6dp%2F11makeComponent.png?alt=media&#x26;token=f816b890-0e6c-4b92-9230-c42d5a929b4a" alt=""><figcaption></figcaption></figure>

## Insert an existing component

You can also add an existing component to an existing test:&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FkNBE3lt21AOBZ2UCD3ZS%2F11insertComponent.png?alt=media&#x26;token=1019f450-c561-4d48-ada0-72b28c5392b0" alt=""><figcaption></figcaption></figure>

This can be also done when creating a completely new test:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FG0CdalUKB3JQifHSzDJS%2F2addToNewTest.png?alt=media&#x26;token=506ee579-5e59-408c-9c3d-1e56e3811086" alt=""><figcaption><p>Insert a component to a new test</p></figcaption></figure>

You can browse all your components here and search for a specific one that you want to add:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F78jqh3Z4VCJQ9VTPeNqn%2F2addToNewTest2.png?alt=media&#x26;token=4c17f555-5abe-4765-8f5b-6c343837db48" alt=""><figcaption><p>List of existing components when adding to a new test</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FqQBdMTWbgR22PkFwCR0C%2Fimage.png?alt=media&#x26;token=745a2ffe-1036-4192-9842-0bdf46bb1b26" alt=""><figcaption><p>Inserting component</p></figcaption></figure>

## Inserting the same component multiple times

You can add the same component multiple times in a single test.&#x20;

As with components in general, a change to one instance will be reflected in the others.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FdyjW418yNpuKJ3DKmQc5%2Fimage.png?alt=media&#x26;token=6e869946-e035-4c66-b1c7-0cbf4f37cd0b" alt=""><figcaption><p>Inserting component multiple times in a single test</p></figcaption></figure>

### Parametrizing components

If you want to reuse the same component in a test multiple times but with different parameters, you can achieve that using variables and the ability to override them. A typical scenario involves reusing the login component for various roles within the same application. To do that, you have to:

1. Create a `{{login}}` [variable](https://docs.bugbug.io/editing-tests/variables) (could be empty by default).
2. Create a `{{password}}` [variable](https://docs.bugbug.io/editing-tests/variables) (could be empty by default).
3. Create a component that uses those variables to log in to the application.
4. Create a group **before** the instance of the component that you want to parametrize.
5. Override login and password variables using the `Set variable` step.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FsYo836ymmZ920Mms9xyR%2Fimage.png?alt=media&#x26;token=4328cdb8-04e8-40a7-8444-784d2772ed7d" alt=""><figcaption><p>Parametrizing components with overrided variables</p></figcaption></figure>

## Unlinking components

When you unlink a component, it will convert it to a regular group and append a "duplicate" to the group name. **This will only unlink it in this specific test!** Use it for making a small modification that is not required in any other test.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FewUsvXbKuGxdxqBSTBgu%2F4unlinkComponent.png?alt=media&#x26;token=298aa3a2-2034-4916-b0e9-dbc107884a7e" alt=""><figcaption><p>Unlink a component from a test</p></figcaption></figure>

## Splitting components

This works exactly the same as splitting a group. You will get two new components after splitting a component and you can immediately rename them. **All instances of this component in all tests will also be split.**&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FyJPEurnghYTZLs2ra4Mu%2F11splitComponent.png?alt=media&#x26;token=7961e4ee-1ed2-46a6-b6ff-c3c84ab18b5a" alt=""><figcaption></figcaption></figure>

## Removing components from a test

You can remove the component from a specific test.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FncllwjDyqgyHlW2jrIDs%2F5removeComponent.png?alt=media&#x26;token=e676760e-efe1-485c-bec5-544741f85825" alt=""><figcaption><p>Removing a component from a test</p></figcaption></figure>

* "Remove from this test" - This will only remove it from this test, but not from other tests.

{% hint style="info" %}
**Important!** When you remove the last instance of a component, it is **not** removed from your project and will still appear in the "Components" and be available through "Insert an existing component".
{% endhint %}

### Changing back the component to a regular group

You can always change your group back to being a regular one and not a component anymore, simply by clicking on the yellow label with "Component" text:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F2JLl9HCs7xkfXOqN7EjN%2F5removeComponent2.png?alt=media&#x26;token=d8216659-e06e-4a23-ac45-0e86521ca096" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important!** This won't delete the created component, so you can still preview it on the "Components" page, and use it in your tests.
{% endhint %}

## Edit components

{% hint style="warning" %}
You can edit a component in the context of a specific test. However, remember that this will affect other tests that use it.
{% endhint %}

Edit is located within the test, and there are two ways to get there - by navigating to the test via the "Tests" page, or by searching for the component in the "Components" page, and then through the list of tests that use it.

&#x20;Here on its details page click on the "**Edit component**" button:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FeiKzxeQTO6K3XC3r4b3D%2F6editComponent.png?alt=media&#x26;token=e57bb341-5bf9-4178-a2c0-f1dc65bc9ab5" alt=""><figcaption><p>Component's details page</p></figcaption></figure>

Next, click on the linked test from the list to enter the edit mode. \
\
On this screen, you will see a list of all the tests in which this component has been used, and you can choose one that best suits you when editing the component.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F2dZgvE6qs205jVKl5xSX%2F6editComponent2.png?alt=media&#x26;token=0617234e-23b5-42af-99d6-7622126b8a68" alt=""><figcaption><p>List of connected tests</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F5QTdqoRnIM6vYBFmbQRm%2F6editComponent3.png?alt=media&#x26;token=a8827803-c74c-4f94-80c7-105bdaf10259" alt=""><figcaption><p>Edit mode of a component used in a test</p></figcaption></figure>

{% hint style="info" %}
Editing a component won't be possible if it's not linked with any test. To enable editing link it first to any of your tests.
{% endhint %}

#### Preview steps that are within a component

When you are in the details of the component, you can see a preview of each step by clicking on it. This is done in the read-only view.

## Additional actions on single component

Being on the list of all components or on a view of a single component you can perform additional actions by clicking on the more menu, such as:

* **Duplicate** - This will duplicate the selected component by adding `- duplicate` prefix in its name. \
  Also, please remember that by default the duplicated item **won't** be connected to any test.<br>
* **Rename** - This will let you change the name of the selected component, which will apply to all tests that use it. Furthermore, the name must be unique.<br>
* **Show related tests** - This will show you a preview of all related tests with that component. They can be previewed by clicking on any of them in the list (which will open in a new tab). If there are a lot of them, you may also find the search box useful.<br>

  \
  This is accessible in the details of the component:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FxkjPBK1X7A5XMRkeD33c%2F33showRelatedTests3.png?alt=media&#x26;token=7ea83da5-0742-4c02-8b6c-f2a357fc445c" alt=""><figcaption><p>Show related tests</p></figcaption></figure>

Also from the "Actions" menu:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FVOgUVGzB8lxeJKpeeblQ%2F7editShowRelatedTests2.png?alt=media&#x26;token=3564890e-62d4-4001-96ef-e8cc8ec02f9f" alt=""><figcaption><p>Show related tests</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fn7jhnlIGxDI8SiD8J2nF%2F7editShowRelatedTests3.png?alt=media&#x26;token=36a91c07-78c1-4ba8-bcec-d1ef1356a628" alt=""><figcaption><p>List of related tests with a component</p></figcaption></figure>

If a component isn't linked to any test, this field will be disabled:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FrEBzGhBuiPKH4HEj5rL1%2F7editShowRelatedTests.png?alt=media&#x26;token=e895caa2-d2da-4803-b8d7-0dfbdb03bd8e" alt=""><figcaption><p>No related tests with a component</p></figcaption></figure>

* **Delete** - This allows you to delete components you no longer need, to keep the list tidy. Please note that deleting a component will permanently delete all instances of that component and cannot be undone.

Yet to not do it accidentally we distinguish two scenarios.&#x20;

1. Deleting a component when **it's not** linked to any test. A confirmation modal will show up:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FjJRo2o0MKLLeN88fkOO4%2F8deleteSingleComponent.png?alt=media&#x26;token=440eb9ea-d535-41e9-b228-fcf7a6730494" alt=""><figcaption><p>Deleting a component without any connected test</p></figcaption></figure>

2. Deleting a component when **it's** linked to a test you need to additionally confirm this action by typing the safe word on the confirmation modal:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FwfM5frFPNflcO8Hey5sI%2F8deleteMultiComponent.png?alt=media&#x26;token=74f416b6-89b6-433c-9a80-c57a1af4df68" alt=""><figcaption><p>Deleting a component with multiple connected tests</p></figcaption></figure>

## Additional bulk actions on components

For now, you can select multiple components from the list on the Components page and perform bulk actions such as:

* Delete - This will delete all selected components from the list

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FpHvffbHDEhX9riqy5FNq%2F22bulkActions.png?alt=media&#x26;token=f2868a58-383a-493e-a4f1-e50f158a5d5c" alt=""><figcaption><p>Delete in bulk</p></figcaption></figure>

* Deselect all - This will remove the selection&#x20;
