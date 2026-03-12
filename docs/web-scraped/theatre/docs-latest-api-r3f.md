# Source: https://www.theatrejs.com/docs/latest/api/r3f

Title: @theatre/r3f – Theatre.js

URL Source: https://www.theatrejs.com/docs/latest/api/r3f

Markdown Content:
This is a documentation page for the r3f extension that makes it easier to use Theatre.js with [React Three Fiber](https://www.npmjs.com/package/@react-three/fiber). Want to learn how to set up Theater.js with React Three Fiber? Head over to the [Getting Started with React Three Fiber](https://www.theatrejs.com/docs/latest/getting-started/with-react-three-fiber) page

#editable
---------

The `editable` object can be used either as [a React component](https://www.theatrejs.com/docs/latest/api/r3f#editable-react-component) to create editable versions of r3f elements, or as [a function](https://www.theatrejs.com/docs/latest/api/r3f#editable-fn) to create editable versions of React components that have an API that matches that of a supported React Three Fiber element.

### #editable – as a React component

You can create editable versions of React Three Fiber elements using properties on the `editable` object.

`<editable.pointLight theatreKey="Key light" />`

These elements behave the same as the originals, but also show up in the Studio.

While they take the same props as their r3f counterparts, there are a couple of Theatre.js-specific props.

#### #props.theatreKey

The element's [object's](https://www.theatrejs.com/docs/latest/api/core#object) name in Theatre.js. All editable elements **need** to have a `theatreKey` prop so that they can be connected to a backing-object.

`<editable.group theatreKey="My group" />`

#### #props.visible

The `visible` prop is the same as for all r3f elements, however, while regular r3f elements can only take `true` or `false`, `editable` elements can take a third, `'editor'` option that signals to Theatre.js that we only want the object to be visible in the snapshot editor. This is helpful for helper objects that we don't want to be part of the final scene.

`<editable.mesh theatreKey="Marker" visible="editor">  <boxBufferGeometry />  <meshBasicMaterial color="yellow" /></editable.mesh>`

#### #props.additionalProps

Allows you to specify additional Theatre.js props under the backing-object of the element. These props won't have an immediate effect on the element, but you can observe them by subscribing to the element's backing-object directly through `objRef`.

`<editable.group  theatreKey="My group"  additionalProps={{    myCustomProp: types.number(0, {      nudgeMultiplier: 0.1,    }),  }}/>`

`props.additionalProps` can be used in combination with [`props.objRef`](https://www.theatrejs.com/docs/latest/api/r3f#props.objref)` to observe the additional props.

`const MyComponent = () => {  // A reference to the THREE.js object  const threeRef = useRef()  const [    // The Theatre.js object that represents our THREE.js object. It'll be initially `null`.    theatreObject,    setTheatreObject,  ] =    // Let's use `useState()` so our `useEffect()` will re-run when `theatreObject` changes    useState(null)  // This `useEffect()` will run when `theatreObject` changes  useEffect(    () => {      // if `theatreObject` is `null`, we don't need to do anything      if (!theatreObject) return      const unsubscribe = theatreObject.onValuesChange((newValues) => {        // Apply the new offset to our THREE.js object        threeRef.current.offset = newValues.offset      })      // unsubscribe from the listener when the component unmounts      return unsubscribe    },    // We only want to run this `useEffect()` when `theatreObject` changes    [theatreObject],  )  return (    <e.group      theatreKey="My group"      // We're defining one additional property, `offset`, which is not part of THREE.js      additionalProps={{        offset: 0,      }}      // a reference to the THREE.js object      ref={threeRef}      // a reference to the Theatre.js object      objRef={setTheatreObject}    />  )}`

#### #props.objRef

Exposes the element's backing-object directly.

`const MyComponent: React.FC = () => {  const objRef = useRef<ISheetObject>()  return <editable.group theatreKey="My group" objRef={objRef} />}`

See [`props.additionalProps`](https://www.theatrejs.com/docs/latest/api/r3f#props.additionalprops) for an example of how to use this.

#### #props.editableType

This prop is only used when using `editable.primitive`, since primitive elements can represent any THREE.js object. The `editableType` prop tells Theatre.js what THREE.js object type to assume in this case.

`<editable.primitive object={myMesh} theatreKey="My Mesh" editableType="mesh" />`

### #editable – as a function

You can also use `editable` as a function to create editable versions of react components that have an API that matches that of a supported React Three Fiber element.

`import { editable } from '@theatre/r3f'import { PerspectiveCamera } from '@react-three/drei'const EditableCamera = editable(PerspectiveCamera, 'perspectiveCamera')`

#SheetProvider
--------------

All editable elements are backed by a Theatre.js [sheet object](https://www.theatrejs.com/docs/latest/api/core#object). The r3f extension needs to know what [sheet](https://www.theatrejs.com/docs/latest/api/core#sheet) to attach these objects to. The way it does this is through the `SheetProvider` React component. `SheetPovider`s can be arbitrarily placed and nested, there are only two rules:

1.   All editable elements need to be a descendant of a `SheetProvider`.
2.   All editable elements need to have a unique `theatreKey` prop under their `SheetProvider`. `theatreKey`s across sheets don't need to be unique.

`<Canvas>  <SheetProvider sheet={getProject('Playground - R3F').sheet('R3F-Canvas')}>    <ambientLight intensity={0.5} />    <editable.spotLight position={[10, 10, 10]} angle={0.15} penumbra={1} theatreKey="Spotlight" />    <editable.pointLight theatreKey="PointLight" />    <editable.mesh theatreKey="Box">      <boxBufferGeometry />      <meshStandardMaterial color="orange" />    </editable.mesh>  </SheetProvider></Canvas>`

#useCurrentSheet()
------------------

Hook to access the sheet of the nearest `SheetProvider`.

`import { useCurrentSheet } from '@theatre/r3f'export default function Scene() {  const currentSheet = useCurrentSheet()  console.log(currentSheet)  return (    <editable.mesh theatreKey="Box">      <boxBufferGeometry />      <meshStandardMaterial color="orange" />    </editable.mesh>  )}`

#refreshSnapshot()
------------------

Utility to refresh the snapshot in the snapshot editor from code. Useful for example to refresh the snapshot editor when some assets have loaded that otherwise would not be visible.

`import { refreshSnapshot } from '@theatre/r3f'refreshSnapshot()`

#RefreshSnapshot
----------------

React component that refreshes the snapshot editor on mount. Useful when you use `Suspense` to wait for assets to load, and you want to refresh when the suspended components render.

`<Suspense fallback={Fallback}>  <RefreshSnapshot />  <MyModel /></Suspense>`

#Cameras Since 0.5.1
--------------------

The r3f extension comes with counterparts to the regular Three.js `perspectiveCamera` and `orthographicCamera` objects, which expose the `makeDefault` prop for making them the default for rendering, and are editable in the snapshot editor.

`import { PerspectiveCamera } from '@theatre/r3f'const MyComponent = () => (  // ...  <PerspectiveCamera theatreKey="Camera" makeDefault position={[0, 0, 16]} fov={75} />)`

These cameras also expose a `lookAt` prop, which can be passed any Three.js object, or object ref, and it'll automatically update the camera to track that object, both live, and in the snapshot editor.

`const MyComponent = () => {  const ref = useRef<THREE.Object3D>()  return (    // ...    <>      <PerspectiveCamera theatreKey="Camera" makeDefault position={[0, 0, 16]} fov={75} lookAt={ref} />      <editable.mesh theatreKey="Target" ref={ref}>        <boxBufferGeometry />        <meshStandardMaterial color="orange" />      </editable.mesh>    </>  )}`

#extension
----------

JS object used to register the extension with the Studio.

Note, `extension` is not exported from `@theatre/r3f`! It is instead exported from `@theatre/r3f/dist/extension` in order to aid in excluding it and Studio from production code.

`import { extension } from '@theatre/r3f/dist/extension'import studio from '@theatre/studio'studio.extend(extension)studio.initialize()`

* * *

Was this article helpful to you?

Last edited on February 01, 2024.

[Edit this page](https://github.com/theatre-js/website/blob/main/content/docs/0.5/500-api/300-r3f.mdx)
