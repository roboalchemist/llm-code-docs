# References

References, or refs for short, are stable, local values that persist across component renders but don't trigger rerenders like state or props would when they change.

Most often you'll see refs used to facilitate imperative manipulation of the DOM but they can be used to store any arbitrary local value that you need to be kept stable. You may use them to track a previous state value, keep a reference to an interval or timeout ID, or simply a counter value. Importantly, refs should not be used for rendering logic, instead, consumed in lifecycle methods and event handlers only.

---

*   [Creating a Ref](#creating-a-ref)
*   [Using Refs to Access DOM Nodes](#using-refs-to-access-dom-nodes)
    *   [Callback Refs](#callback-refs)
*   [Using Refs to Store Local Values](#using-refs-to-store-local-values)

---

## Creating a Ref

There are two ways to create refs in Preact, depending on your preferred component style: `createRef` (class components) and `useRef` (function components/hooks). Both APIs fundamentally work the same way: they create a stable, plain object with a `current` property, optionally initialized to a value.

### Classes

```jsx
import { createRef } from 'preact';

class MyComponent extends Component {
  countRef = createRef();
  inputRef = createRef(null);

  // ...
}
```

### Hooks

```jsx
import { useRef } from 'preact/hooks';

function MyComponent() {
  const countRef = useRef();
  const inputRef = useRef(null);

  // ...
}
```

## Using Refs to Access DOM Nodes

The most common use case for refs is to access the underlying DOM node of a component. This is useful for imperative DOM manipulation, such as measuring elements, calling native methods on various elements (such as `.focus()` or `.play()`), and integrating with third-party libraries written in vanilla JS. In the following examples, upon rendering, Preact will assign the DOM node to the `current` property of the ref object, making it available for use after the component has mounted.

### Classes

```jsx
class MyInput extends Component {
  ref = createRef(null);

  componentDidMount() {
    console.log(this.ref.current);
    // Logs: [HTMLInputElement]
  }

  render() {
    return <input ref={this.ref} />;
  }
}

[Run in REPL](/repl?code=aW1wb3J0IHsgcmVuZGVyLCBDb21wb25lbnQsIGNyZWF0ZVJlZiB9IGZyb20gJ3ByZWFjdCc7CgpjbGFzcyBTaUlucHV0IGV4dGVuZHMgQ29tcG9uZW50IHsKCXJlZiA9IGNyZWF0ZVJlZihudWxsKTsKCgljb21wb25lbnREaWRNb3VudCgpIHsKCQljb25zb2xlLmxvZyh0aGlzLnJlZi5jdXJyZW50KTsKCQkvLyBMb2dzOiBbSFRNTElucHV0RWxlbWVudF0KCX0KCglyZW5kZXIoKSB7CgkJcmV0dXJuIDxpbnB1dCByZWY9e3RoaXMucmVmfSAvPjsKCX0KfQoKcmVuZGVyKDxNeUlucHV0IC8%2BLCBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnYXBwJykpOwo%3D)
```

### Hooks

```jsx
function MyInput() {
  const ref = useRef(null);

  useEffect(() => {
    console.log(ref.current);
    // Logs: [HTMLInputElement]
  }, []);

  return <input ref={ref} />;
}
```

[Run in REPL](/repl?code=aW1wb3J0IHsgcmVuZGVyIH0gZnJvbSAncHJlYWN0JzsKaW1wb3J0IHsgdXNlUmVmLCB1c2VFZmZlY3QgfSBmcm9tICdwcmVhY3QvaG9va3MnOwoKZnVuY3Rpb24gTXlJbnB1dCgpIHsKCWNvbnN0IHJlZiA9IHVzZVJlZihudWxsKTsKCgl1c2VFZmZlY3QoKCkgPT4gewoJCWNvbnNvbGUubG9nKHJlZi5jdXJyZW50KTsKCQkvLyBMb2dzOiBbSFRNTElucHV0RWxlbWVudF0KCX0sIFtdKTsKCglyZXR1cm4gPGlucHV0IHJlZj17cmVmfSAvPjsKfQoKcmVuZGVyKDxNeUlucHV0IC8%2BLCBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnYXBwJykpOwo%3D)

### Callback Refs

Another way to use references is by passing a function to the `ref` prop, where the DOM node will be passed as an argument.

#### Classes

```jsx
class MyInput extends Component {
  render() {
    return (
      <input
        ref={dom => {
          console.log('Mounted:', dom);

          // As of Preact 10.23.0, you can optionally return a cleanup function
          return () => {
            console.log('Unmounted:', dom);
          };
        }}
      />
    );
  }
}

[Run in REPL](/repl?code=aW1wb3J0IHsgcmVuZGVyLCBDb21wb25lbnQgfSBmcm9tICdwcmVhY3QnOwoKY2xhc3MgTXlJbnB1dCBleHRlbmRzIENvbXBvbmVudCB7CglyZW5kZXIoKSB7CgkJcmV0dXJuICgKCQkJPGlucHV0CgkJCQlyZWY9e2RvbSA9PiB7CgkJCQkJY29uc29sZS5sb2coJ01vdW50ZWQ6JywgZG9tKTsKCgkJCQkJLy8gQXMgb2YgUHJlYWN0IDEwLjIzLjAsIHlvdSBjYW4gb3B0aW9uYWxseSByZXR1cm4gYSBjbGVhbnVwIGZ1bmN0aW9uCgkJCQkJcmV0dXJuICgpID0%2BIHsKCQkJCQkJY29uc29sZS5sb2coJ1VubW91bnRlZDonLCBkb20pOwoJCQkJCX07CgkJCQl9fQoJCQkvPgoJCSk7Cgl9Cn0KCnJlbmRlcig8TXlJbnB1dCAvPiwgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2FwcCcpKTsK)
```

#### Hooks

```jsx
function MyInput() {
  return (
    <input
      ref={dom => {
        console.log('Mounted:', dom);

        // As of Preact 10.23.0, you can optionally return a cleanup function
        return () => {
          console.log('Unmounted:', dom);
        };
      }}
    />
  );
}
```

[Run in REPL](/repl?code=aW1wb3J0IHsgcmVuZGVyIH0gZnJvbSAncHJlYWN0JzsKCmZ1bmN0aW9uIE15SW5wdXQoKSB7CglyZXR1cm4gKAoJCTxpbnB1dAoJCQlyZWY9e2RvbSA9PiB7CgkJCQljb25zb2xlLmxvZygnTW91bnRlZDonLCBkb20pOwoKCQkJCS8vIEFzIG9mIFByZWFjdCAxMC4yMy4wLCB5b3UgY2FuIG9wdGlvbmFsbHkgcmV0dXJuIGEgY2xlYW51cCBmdW5jdGlvbgoJCQkJcmV0dXJuICgpID0%2BIHsKCQkJCQljb25zb2xlLmxvZygnVW5tb3VudGVkOicsIGRvbSk7CgkJCQl9OwoJCQl9fQoJCS8%2BCgkpOwp9CgpyZW5kZXIoPE15SW5wdXQgLz4sIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdhcHAnKSk7Cg%3D%3D)

> If the provided ref callback is unstable (such as one that's defined inline, as shown above), and _does not_ return a cleanup function, **it will be called twice** upon all rerenders: once with `null` and then once with the actual reference. This is a common issue and the `createRef`/`useRef` APIs make this a little easier by forcing the user to check if `ref.current` is defined.
>
> A stable function, for comparison, could be a method on the class component instance, a function defined outside of the component, or a function created with `useCallback`, for example.

## Using Refs to Store Local Values

Refs aren't limited to storing DOM nodes, however; they can be used to store any type of value that you may need.

In the following example, we store the ID of an interval in a ref to be able to start & stop it independently.

### Classes

```jsx
class SimpleClock extends Component {
  state = {
    time: Date.now()
  };
  intervalId = createRef(null);

  startClock = () => {
    this.setState({ time: Date.now() });
    this.intervalId.current = setInterval(() => {
      this.setState({ time: Date.now() });
    }, 1000);
  };

  stopClock = () => {
    clearInterval(this.intervalId.current);
  };

  render(_,
    { time }) {
    const formattedTime = new Date(time).toLocaleTimeString();

    return (
      <div>
        <button onClick={this.startClock}>Start Clock</button>
        <time dateTime={formattedTime}>{formattedTime}</time>
        <button onClick={this.stopClock}>Stop Clock</button>
      </div>
    );
  }
}
```

[Run in REPL](/repl?code=aW1wb3J0IHsgcmVuZGVyLCBDb21wb25lbnQsIGNyZWF0ZVJlZiB9IGZyb20gJ3ByZWFjdCc7CgpjbGFzcyBTaW1wbGVDbG9jayBleHRlbmRzIENvbXBvbmVudCB7CglzdGF0ZSA9IHsKCQl0aW1lOiBEYXRlLm5vdygpCgl9OwoJaW50ZXJ2YWxJZCA9IGNyZWF0ZVJlZihudWxsKTsKCglzdGFydENsb2NrID0gKCkgPT4gewoJCXRoaXMuc2V0U3RhdGUoeyB0aW1lOiBEYXRlLm5vdygpIH0pOwoJCXRoaXMuaW50ZXJ2YWxJZC5jdXJyZW50ID0gc2V0SW50ZXJ2YWwoKCkgPT4gewoJCQl0aGlzLnNldFN0YXRlKHsgdGltZTogRGF0ZS5ub3coKSB9KTsKCQl9LCAxMDAwKTsKCX07CgoJc3RvcENsb2NrID0gKCkgPT4gewoJCWNsZWFySW50ZXJ2YWwodGhpcy5pbnRlcnZhbElkLmN1cnJlbnQpOwoJfTsKCglyZW5kZXIoXywgeyB0aW1lIH0pIHsKCQljb25zdCBmb3JtYXR0ZWRUaW1lID0gbmV3IERhdGUodGltZSkudG9Mb2NhbGVUaW1lU3RyaW5nKCk7CgoJCXJldHVybiAoCgkJCTxkaXY%2BCgkJCQk8YnV0dG9uIG9uQ2xpY2s9e3RoaXMuc3RhcnRDbG9ja30%2BU3RhcnQgQ2xvY2s8L2J1dHRvbj4KCQkJCTx0aW1lIGRhdGVUaW1lPXtmb3JtYXR0ZWRUaW1lfT57Zm9ybWF0dGVkVGltZX08L3RpbWU%2BCgkJCQk8YnV0dG9uIG9uQ2xpY2s9e3RoaXMuc3RvcENsb2NrfT5TdG9wIENsb2NrPC9idXR0b24%2BCgkJCTwvZGl2PgoJCSk7Cgl9Cn0KCnJlbmRlcig8U2ltcGxlQ2xvY2sgLz4sIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdhcHAnKSk7Cg%3D%3D)

### Hooks

```jsx
function SimpleClock() {
  const [time, setTime] = useState(Date.now());
  const intervalId = useRef(null);

  const startClock = () => {
    setTime(Date.now());
    intervalId.current = setInterval(() => {
      setTime(Date.now());
    }, 1000);
  };

  const stopClock = () => {
    clearInterval(intervalId.current);
  };

  const formattedTime = new Date(time).toLocaleTimeString();

  return (
    <div>
      <button onClick={startClock}>Start Clock</button>
      <time dateTime={formattedTime}>{formattedTime}</time>
      <button onClick={stopClock}>Stop Clock</button>
    </div>
  );
}
```

[Run in REPL](/repl?code=aW1wb3J0IHsgcmVuZGVyIH0gZnJvbSAncHJlYWN0JzsKaW1wb3J0IHsgdXNlU3RhdGUsIHVzZVJlZiB9IGZyb20gJ3ByZWFjdC9ob29rcyc7CgpmdW5jdGlvbiBTaW1wbGVDbG9jaygpIHsKCWNvbnN0IFt0aW1lLCBzZXRUaW1lXSA9IHVzZVN0YXRlKERhdGUubm93KCkpOwoJY29uc3QgaW50ZXJ2YWxJZCA9IHVzZVJlZihudWxsKTsKCgljb25zdCBzdGFydENsb2NrID0gKCkgPT4gewoJCXNldFRpbWUoRGF0ZS5ub3coKSk7CgkJaW50ZXJ2YWxJZC5jdXJyZW50ID0gc2V0SW50ZXJ2YWwoKCkgPT4gewoJCQlzZXRUaW1lKERhdGUubm93KCkpOwoJCX0sIDEwMDApOwoJfTsKCgljb25zdCBzdG9wQ2xvY2sgPSAoKSA9PiB7CgkJY2xlYXJJbnRlcnZhbChpbnRlcnZhbElkLmN1cnJlbnQpOwoJfTsKCgljb25zdCBmb3JtYXR0ZWRUaW1lID0gbmV3IERhdGUodGltZSkudG9Mb2NhbGVUaW1lU3RyaW5nKCk7CgoJcmV0dXJuICgKCQk8ZGl2PgoJCQk8YnV0dG9uIG9uQ2xpY2s9e3N0YXJ0Q2xvY2t9PlN0YXJ0IENsb2NrPC9idXR0b24%2BCgkJCTx0aW1lIGRhdGVUaW1lPXtmb3JtYXR0ZWRUaW1lfT57Zm9ybWF0dGVkVGltZX08L3RpbWU%2BCgkJCTxidXR0b24gb25DbGljaz17c3RvcENsb2NrfT5TdG9wIENsb2NrPC9idXR0b24%2BCgkJPC9kaXY%2BCgkpOwp9CgpyZW5kZXIoPFNpbXBsZUNsb2NrIC8%2BLCBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnYXBwJykpOwo%3D)