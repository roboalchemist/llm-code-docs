# Source: https://www.theatrejs.com/docs/latest/manual/objects

Title: Sheet Objects – Theatre.js

URL Source: https://www.theatrejs.com/docs/latest/manual/objects

Markdown Content:
#What is an Object in Theatre.js?
---------------------------------

Everything on the page or in the scene is represented by a Theatre.js Sheet Object. These Sheet Objects have a matching [prop](https://www.theatrejs.com/docs/latest/manual/prop-types) for all the properties we want to animate for an object in our scene.

Sheet Object props in all cases have a type (`number`, `string`, etc.), and an initial value.

Objects can represent THREE.js objects, `<div>`s, or virtual objects that don't exist on the screen.

#Creating Sheet Objects
-----------------------

You can create a Sheet Object with the [Sheet.object](https://www.theatrejs.com/docs/latest/api/core#sheet.object) function in `@theatre/core`. If a Sheet Object with the given name already exists, it will return the existing Sheet Object instead of creating a new one. We create a Sheet Object by specifying its name and its props. In many cases, you can use a regular JavaScript object to specify the props, however if you need more control, you can specify the types [explicitly](https://www.theatrejs.com/docs/latest/manual/prop-types).

`// sheet is a Sheet created earlier through Poject.sheetconst myObject = sheet.object('My Object', { position: { x: 0, y: 0 } })`

#Reconfiguring existing objects Since 0.5.1
-------------------------------------------

Objects can be reconfigured on the fly. For example, you can add a `rotation` prop to a live object without having to refresh the page. Simply call `sheet.object()` with `{reconfigure: true}` and the existing object will be reconfigured.

`const obj = sheet.object('obj', { foo: 0 })console.log(obj.value.foo) // prints 0const obj2 = sheet.object('obj', { bar: 0 }, { reconfigure: true })console.log(obj.value.foo) // prints undefined, since we've removed this prop via reconfiguring the objectconsole.log(obj.value.bar) // prints 0, since we've introduced this prop by reconfiguring the objectassert(obj === obj2) // passes, because reconfiguring the object returns the same object`

#Detaching objects Since 0.5.1
------------------------------

Objects can be detached from their sheet. This is _almost_ like deleting an object, except that Theatre will still _remember_ the prop values of this object, so if you re-create an object with the same `key`, it'll retain the old object's props values.

`const obj = sheet.object('obj', { foo: 0 })const unsubscribe = obj.onValuesChange((values) => {  div.style.left = values.x + 'px'})// let's clean up our subscriptions before detaching the objectunsubscribe()sheet.detachObject('obj')`

#Namespacing objects
--------------------

The key of the sheet object can be used to namespace objects. Namespaces are separated by "/" characters in the object's key (e.g. "Namespace-1 / Namespace-2 / Object-name") and displayed in indented groups in the [Outline Panel](https://www.theatrejs.com/docs/latest/manual/Studio#outline-panel) as seen in the screenshot below.

`// `obj1` and `obj2` belong to the `Boxes` namepace,// which is under the `Basics` namespaceconst obj1 = sheet.object('Basics / Boxes / box-0', { x: 0 })const obj2 = sheet.object('Basics / Boxes / box-1', { x: 0 })`

![Image 1: Namespacing](https://www.theatrejs.com/images/docs/0.5/manual/objects/namespacing.png)

#API
----

Learn more about related API at [Sheet Object API docs](https://www.theatrejs.com/docs/latest/api/core#object).

#Learn more
-----------

Want to learn more? Take a look at some more in-depth topics from [our manual](https://www.theatrejs.com/docs/latest/manual):

* * *

Was this article helpful to you?

Last edited on February 01, 2024.

[Edit this page](https://github.com/theatre-js/website/blob/main/content/docs/0.5/300-manual/120-objects.mdx)
