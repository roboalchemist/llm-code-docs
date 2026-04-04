# Source: https://reactcommunity.org/react-transition-group/transition

Title: React Transition Group

URL Source: https://reactcommunity.org/react-transition-group/transition

Markdown Content:
The Transition component lets you describe a transition from one component state to another _over time_ with a simple declarative API. Most commonly it's used to animate the mounting and unmounting of a component, but can also be used to describe in-place transition states as well.

* * *

**Note**: `Transition` is a platform-agnostic base component. If you're using transitions in CSS, you'll probably want to use [`CSSTransition`](https://reactcommunity.org/react-transition-group/css-transition) instead. It inherits all the features of `Transition`, but contains additional features necessary to play nice with CSS transitions (hence the name of the component).

* * *

By default the `Transition` component does not alter the behavior of the component it renders, it only tracks "enter" and "exit" states for the components. It's up to you to give meaning and effect to those states. For example we can add styles to a component when it enters or exits:

```
import { Transition } from 'react-transition-group';
import { useRef } from 'react';

const duration = 300;

const defaultStyle = {
  transition: `opacity ${duration}ms ease-in-out`,
  opacity: 0,
}

const transitionStyles = {
  entering: { opacity: 1 },
  entered:  { opacity: 1 },
  exiting:  { opacity: 0 },
  exited:  { opacity: 0 },
};

function Fade({ in: inProp }) {
  const nodeRef = useRef(null);
  return (
    <Transition nodeRef={nodeRef} in={inProp} timeout={duration}>
      {state => (
        <div ref={nodeRef} style={{
          ...defaultStyle,
          ...transitionStyles[state]
        }}>
          I'm a fade Transition!
        </div>
      )}
    </Transition>
  );
}
```

There are 4 main states a Transition can be in:

*   `'entering'`
*   `'entered'`
*   `'exiting'`
*   `'exited'`

Transition state is toggled via the `in` prop. When `true` the component begins the "Enter" stage. During this stage, the component will shift from its current transition state, to `'entering'` for the duration of the transition and then to the `'entered'` stage once it's complete. Let's take the following example (we'll use the [useState](https://reactjs.org/docs/hooks-reference.html#usestate) hook):

```
import { Transition } from 'react-transition-group';
import { useState, useRef } from 'react';

function App() {
  const [inProp, setInProp] = useState(false);
  const nodeRef = useRef(null);
  return (
    <div>
      <Transition nodeRef={nodeRef} in={inProp} timeout={500}>
        {state => (
          // ...
        )}
      </Transition>
      <button onClick={() => setInProp(true)}>
        Click to Enter
      </button>
    </div>
  );
}
```

When the button is clicked the component will shift to the `'entering'` state and stay there for 500ms (the value of `timeout`) before it finally switches to `'entered'`.

When `in` is `false` the same thing happens except the state moves from `'exiting'` to `'exited'`.

[Props](https://reactcommunity.org/react-transition-group/transition#Transition-props)
--------------------------------------------------------------------------------------

### [`nodeRef`](https://reactcommunity.org/react-transition-group/transition#Transition-prop-nodeRef)

A React reference to the DOM element that needs to transition: [https://stackoverflow.com/a/51127130/4671932](https://stackoverflow.com/a/51127130/4671932)

*   This prop is optional, but recommended in order to avoid defaulting to [`ReactDOM.findDOMNode`](https://reactjs.org/docs/react-dom.html#finddomnode), which is deprecated in `StrictMode`
*   When `nodeRef` prop is used, `node` is not passed to callback functions (e.g. `onEnter`) because user already has direct access to the node.
*   When changing `key` prop of `Transition` in a `TransitionGroup` a new `nodeRef` need to be provided to `Transition` with changed `key` prop (see [test/CSSTransition-test.js](https://github.com/reactjs/react-transition-group/blob/13435f897b3ab71f6e19d724f145596f5910581c/test/CSSTransition-test.js#L362-L437)).

type: `shape`

### [`children`](https://reactcommunity.org/react-transition-group/transition#Transition-prop-children)

A `function` child can be used instead of a React element. This function is called with the current transition status (`'entering'`, `'entered'`, `'exiting'`, `'exited'`), which can be used to apply context specific props to a component.

```
<Transition nodeRef={nodeRef} in={this.state.in} timeout={150}>
  {state => (
    <MyComponent ref={nodeRef} className={`fade fade-${state}`} />
  )}
</Transition>
```

type: `Function | element`

required

### [`in`](https://reactcommunity.org/react-transition-group/transition#Transition-prop-in)

Show the component; triggers the enter or exit states

type: `boolean`

default: `false`

### [`mountOnEnter`](https://reactcommunity.org/react-transition-group/transition#Transition-prop-mountOnEnter)

By default the child component is mounted immediately along with the parent `Transition` component. If you want to "lazy mount" the component on the first `in={true}` you can set `mountOnEnter`. After the first enter transition the component will stay mounted, even on "exited", unless you also specify `unmountOnExit`.

type: `boolean`

default: `false`

### [`unmountOnExit`](https://reactcommunity.org/react-transition-group/transition#Transition-prop-unmountOnExit)

By default the child component stays mounted after it reaches the `'exited'` state. Set `unmountOnExit` if you'd prefer to unmount the component after it finishes exiting.

type: `boolean`

default: `false`

### [`appear`](https://reactcommunity.org/react-transition-group/transition#Transition-prop-appear)

By default the child component does not perform the enter transition when it first mounts, regardless of the value of `in`. If you want this behavior, set both `appear` and `in` to `true`.

> **Note**: there are no special appear states like `appearing`/`appeared`, this prop only adds an additional enter transition. However, in the `<CSSTransition>` component that first enter transition does result in additional `.appear-*` classes, that way you can choose to style it differently.

type: `boolean`

default: `false`

### [`enter`](https://reactcommunity.org/react-transition-group/transition#Transition-prop-enter)

Enable or disable enter transitions.

type: `boolean`

default: `true`

### [`exit`](https://reactcommunity.org/react-transition-group/transition#Transition-prop-exit)

Enable or disable exit transitions.

type: `boolean`

default: `true`

### [`timeout`](https://reactcommunity.org/react-transition-group/transition#Transition-prop-timeout)

The duration of the transition, in milliseconds. Required unless `addEndListener` is provided.

You may specify a single timeout for all transitions:

`timeout={500}`

or individually:

```
timeout={{
 appear: 500,
 enter: 300,
 exit: 500,
}}
```

*   `appear` defaults to the value of `enter`
*   `enter` defaults to `0`
*   `exit` defaults to `0`

type: `number | { enter?: number, exit?: number, appear?: number }`

### [`addEndListener`](https://reactcommunity.org/react-transition-group/transition#Transition-prop-addEndListener)

Add a custom transition end trigger. Called with the transitioning DOM node and a `done` callback. Allows for more fine grained transition end logic. Timeouts are still used as a fallback if provided.

**Note**: when `nodeRef` prop is passed, `node` is not passed, so `done` is being passed as the first argument.

```
addEndListener={(node, done) => {
  // use the css transitionend event to mark the finish of a transition
  node.addEventListener('transitionend', done, false);
}}
```

type: `Function`

### [`onEnter`](https://reactcommunity.org/react-transition-group/transition#Transition-prop-onEnter)

Callback fired before the "entering" status is applied. An extra parameter `isAppearing` is supplied to indicate if the enter stage is occurring on the initial mount

**Note**: when `nodeRef` prop is passed, `node` is not passed, so `isAppearing` is being passed as the first argument.

type: `Function(node: HtmlElement, isAppearing: bool) -> void`

default: `function noop() {}`

### [`onEntering`](https://reactcommunity.org/react-transition-group/transition#Transition-prop-onEntering)

Callback fired after the "entering" status is applied. An extra parameter `isAppearing` is supplied to indicate if the enter stage is occurring on the initial mount

**Note**: when `nodeRef` prop is passed, `node` is not passed, so `isAppearing` is being passed as the first argument.

type: `Function(node: HtmlElement, isAppearing: bool)`

default: `function noop() {}`

### [`onEntered`](https://reactcommunity.org/react-transition-group/transition#Transition-prop-onEntered)

Callback fired after the "entered" status is applied. An extra parameter `isAppearing` is supplied to indicate if the enter stage is occurring on the initial mount

**Note**: when `nodeRef` prop is passed, `node` is not passed, so `isAppearing` is being passed as the first argument.

type: `Function(node: HtmlElement, isAppearing: bool) -> void`

default: `function noop() {}`

### [`onExit`](https://reactcommunity.org/react-transition-group/transition#Transition-prop-onExit)

Callback fired before the "exiting" status is applied.

**Note**: when `nodeRef` prop is passed, `node` is not passed.

type: `Function(node: HtmlElement) -> void`

default: `function noop() {}`

### [`onExiting`](https://reactcommunity.org/react-transition-group/transition#Transition-prop-onExiting)

Callback fired after the "exiting" status is applied.

**Note**: when `nodeRef` prop is passed, `node` is not passed.

type: `Function(node: HtmlElement) -> void`

default: `function noop() {}`

### [`onExited`](https://reactcommunity.org/react-transition-group/transition#Transition-prop-onExited)

Callback fired after the "exited" status is applied.

**Note**: when `nodeRef` prop is passed, `node` is not passed

type: `Function(node: HtmlElement) -> void`

default: `function noop() {}`
