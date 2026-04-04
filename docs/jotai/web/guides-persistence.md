# Source: https://jotai.org/docs/guides/persistence

<div>

# [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyODkuMTkgOTkuNzciIGNsYXNzPSJ0ZXh0LWJsYWNrIGRhcms6dGV4dC13aGl0ZSB3LVs0cmVtXSI+PHRpdGxlPkpvdGFpPC90aXRsZT48cGF0aCBkPSJNNDIuMzYsNS4zMkg2MS44MlY3MC4yM2EyOS40NiwyOS40NiwwLDAsMS00LDE1LjYxQTI3LjE5LDI3LjE5LDAsMCwxLDQ2LjY0LDk2LjA3YTM2LjI2LDM2LjI2LDAsMCwxLTE2LjU5LDMuNjEsMzcuNTYsMzcuNTYsMCwwLDEtMTUuMjUtM0EyNC4zLDI0LjMsMCwwLDEsNCw4Ny41OVEwLDgxLjUsMCw3Mi4yM0gxOS41OWMuMDYsMy42OSwxLjEzLDYuNTcsMy4yMSw4LjYxYTExLjIxLDExLjIxLDAsMCwwLDguMjUsMy4wN3ExMS4yMiwwLDExLjMxLTEzLjY4WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTEwNSw5OS43N3EtMTAuNTksMC0xOC4yOS00LjUyQTMwLjU0LDMwLjU0LDAsMCwxLDc0LjgyLDgyLjYxYTQwLjUyLDQwLjUyLDAsMCwxLTQuMTgtMTguODQsNDAuNzUsNDAuNzUsMCwwLDEsNC4xOC0xOC45M0EzMC42LDMwLjYsMCwwLDEsODYuNzEsMzIuMiwzNS41MiwzNS41MiwwLDAsMSwxMDUsMjcuNjhhMzUuNTgsMzUuNTgsMCwwLDEsMTguMyw0LjUyLDMwLjU3LDMwLjU3LDAsMCwxLDExLjg4LDEyLjY0LDQwLjc2LDQwLjc2LDAsMCwxLDQuMTksMTguOTMsNDAuNTIsNDAuNTIsMCwwLDEtNC4xOSwxOC44NEEzMC41MSwzMC41MSwwLDAsMSwxMjMuMyw5NS4yNVExMTUuNTksOTkuNzgsMTA1LDk5Ljc3Wk0xMjcuMTQsNS4zMnYxMC41SDgyLjg3VjUuMzJabS0yMiw3OS40NWExMiwxMiwwLDAsMCwxMC44OS02cTMuNy02LDMuNy0xNS4xM1QxMTYsNDguNDhhMTIsMTIsMCwwLDAtMTAuODktNiwxMi4xNSwxMi4xNSwwLDAsMC0xMSw2cS0zLjczLDYtMy43MywxNS4xNnQzLjczLDE1LjEzQTEyLjE2LDEyLjE2LDAsMCwwLDEwNS4wOSw4NC43N1oiIGZpbGw9ImN1cnJlbnRDb2xvciI+PC9wYXRoPjxwYXRoIGQ9Ik0xODYuMywyOC41OVY0My4xNEgxNzMuMTZWNzdxMCw0LDEuODIsNS40YTcuNSw3LjUsMCwwLDAsNC43MywxLjQxLDE0LjcyLDE0LjcyLDAsMCwwLDIuNzItLjI1bDIuMDktLjM4LDMsMTQuNDFjLTEsLjMtMi4zMy42Ni00LjA5LDEuMDZhMzQuMTMsMzQuMTMsMCwwLDEtNi40MS43NXEtMTAuNTUuNDctMTYuOTMtNC41NlQxNTMuOCw3OS41VjQzLjE0aC05LjU1VjI4LjU5aDkuNTVWMTEuODZoMTkuMzZWMjguNTlaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48cGF0aCBkPSJNMjE2LDk5LjczcS0xMCwwLTE2LjU5LTUuMjN0LTYuNTktMTUuNTlxMC03LjgxLDMuNjgtMTIuMjdhMjEuMTksMjEuMTksMCwwLDEsOS42Ni02LjUzQTU0Ljc4LDU0Ljc4LDAsMCwxLDIxOSw1Ny40MWE5OC41Nyw5OC41NywwLDAsMCwxMy0xLjkxcTMuOTItMSwzLjkxLTQuMzZ2LS4yOGE4LjQyLDguNDIsMCwwLDAtMi43LTYuNjhxLTIuNzItMi4zNS03LjY2LTIuMzZhMTMuNzcsMTMuNzcsMCwwLDAtOC4zMiwyLjI3LDEwLjcsMTAuNywwLDAsMC00LjA5LDUuNzdsLTE3LjkxLTEuNDVhMjMuODgsMjMuODgsMCwwLDEsOS45My0xNS4xNHE3Ljk0LTUuNTgsMjAuNDgtNS41OWE0Mi4yNCw0Mi4yNCwwLDAsMSwxNC41NCwyLjQ2LDI0LjE5LDI0LjE5LDAsMCwxLDEwLjk0LDcuNjZxNC4xNiw1LjIxLDQuMTYsMTMuNTJWOTguNDFIMjM2LjkyVjg4LjczaC0uNTRhMjAuMTgsMjAuMTgsMCwwLDEtNy42Miw3LjkzUTIyMy42OSw5OS43MywyMTYsOTkuNzNabTUuNTQtMTMuMzdBMTUsMTUsMCwwLDAsMjMyLDgyLjY2YTExLjk0LDExLjk0LDAsMCwwLDQuMDktOS4yVjY2LjA1YTExLjM4LDExLjM4LDAsMCwxLTMuNTIsMS4zNmMtMS42LjM5LTMuMjkuNzMtNS4xLDFzLTMuNDEuNTQtNC44NC43NWExOS4xOSwxOS4xOSwwLDAsMC04LjIsMi44Nyw3LjA2LDcuMDYsMCwwLDAtMy4xMSw2LjIyLDYuOTQsNi45NCwwLDAsMCwyLjg4LDZBMTIuNDMsMTIuNDMsMCwwLDAsMjIxLjUxLDg2LjM2WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTI3OC42OSwxOS41OWExMC40MSwxMC40MSwwLDAsMS03LjM3LTIuODksOS4xNCw5LjE0LDAsMCwxLTMuMDktNi45Myw5LjEsOS4xLDAsMCwxLDMuMDktNi45MSwxMSwxMSwwLDAsMSwxNC43OCwwLDkuMSw5LjEsMCwwLDEsMy4wOSw2LjkxLDkuMTQsOS4xNCwwLDAsMS0zLjA5LDYuOTNBMTAuNDUsMTAuNDUsMCwwLDEsMjc4LjY5LDE5LjU5Wk0yNjksOTguNDFWMjguNTloMTkuMzZWOTguNDFaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)[Jotai]

状態

Primitive and flexible state management for React

</div>

# Persistence 

Jotai has an [atomWithStorage function in the utils bundle](../utilities/storage) for persistence that supports persisting state in `sessionStorage`, `localStorage`, `AsyncStorage`, or the URL hash.

(Note: This guide is a bit outdated and requires some rewrites.)

There are also several alternate implementations here:

### [A simple pattern with localStorage](#a-simple-pattern-with-localstorage)

    const strAtom = atom(localStorage.getItem('myKey') ?? 'foo')
    const strAtomWithPersistence = atom(  (get) => get(strAtom),  (get, set, newStr) => ,)

### [A helper function with localStorage and JSON parse](#a-helper-function-with-localstorage-and-json-parse)

    const atomWithLocalStorage = (key, initialValue) =>     return initialValue  }  const baseAtom = atom(getInitialValue())  const derivedAtom = atom(    (get) => get(baseAtom),    (get, set, update) => ,  )  return derivedAtom}

(Error handling should be added.)

### [A helper function with AsyncStorage and JSON parse](#a-helper-function-with-asyncstorage-and-json-parse)

This requires [onMount](../core/atom#onmount-property).

    const atomWithAsyncStorage = (key, initialValue) => )()  }  const derivedAtom = atom(    (get) => get(baseAtom),    (get, set, update) => ,  )  return derivedAtom}

Don\'t forget to check out the [Async documentation](../guides/async) for more details on how to use async atoms.

### [Example with sessionStorage](#example-with-sessionstorage)

Same as AsyncStorage, just use `atomWithStorage` util and override the default storage with the `sessionStorage`

    import  from 'jotai/utils'
    const storage = createJSONStorage(() => sessionStorage)const someAtom = atomWithStorage('some-key', someInitialValue, storage)

### [A serialize atom pattern](#a-serialize-atom-pattern)

    type Actions =  |   | 
    const serializeAtom = atom(null, (get, set, action: Actions) =>     action.callback(JSON.stringify(obj))  } else if (action.type === 'deserialize') })
    const Persist = () => ,    })  }  const load = () => )    }  }  return (    <div>      <button onClick=>Save to localStorage</button>      <button onClick=>Load from localStorage</button>    </div>  )}

#### [Examples](#examples)

### [A pattern with atomFamily](#a-pattern-with-atomfamily)

    type Actions =  |   | 
    const serializeAtom = atom(null, (get, set, action: Actions) => > =     todos.forEach((id) => ))    })    const obj =     action.callback(JSON.stringify(obj))  } else if (action.type === 'deserialize') ), todo)    })    set(todosAtom, obj.todos)  }})
    const Persist = () => ,    })  }  const load = () => )    }  }  return (    <div>      <button onClick=>Save to localStorage</button>      <button onClick=>Load from localStorage</button>    </div>  )}

#### [Examples](#examples) 

[library by [Daishi Kato]](https://twitter.com/dai_shi "Daishi Kato")[art by [Jessie Waters]](https://jessiewaters.com "Jessie Waters")[](https://candycode.com/ "candycode, an alternative graphic design and web development agency based in San Diego")

[site by]![candycode alternative graphic design web development agency San Diego](https://storage.googleapis.com/candycode/candycode.svg)