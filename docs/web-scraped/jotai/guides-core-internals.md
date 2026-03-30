# Source: https://jotai.org/docs/guides/core-internals

<div>

# [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyODkuMTkgOTkuNzciIGNsYXNzPSJ0ZXh0LWJsYWNrIGRhcms6dGV4dC13aGl0ZSB3LVs0cmVtXSI+PHRpdGxlPkpvdGFpPC90aXRsZT48cGF0aCBkPSJNNDIuMzYsNS4zMkg2MS44MlY3MC4yM2EyOS40NiwyOS40NiwwLDAsMS00LDE1LjYxQTI3LjE5LDI3LjE5LDAsMCwxLDQ2LjY0LDk2LjA3YTM2LjI2LDM2LjI2LDAsMCwxLTE2LjU5LDMuNjEsMzcuNTYsMzcuNTYsMCwwLDEtMTUuMjUtM0EyNC4zLDI0LjMsMCwwLDEsNCw4Ny41OVEwLDgxLjUsMCw3Mi4yM0gxOS41OWMuMDYsMy42OSwxLjEzLDYuNTcsMy4yMSw4LjYxYTExLjIxLDExLjIxLDAsMCwwLDguMjUsMy4wN3ExMS4yMiwwLDExLjMxLTEzLjY4WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTEwNSw5OS43N3EtMTAuNTksMC0xOC4yOS00LjUyQTMwLjU0LDMwLjU0LDAsMCwxLDc0LjgyLDgyLjYxYTQwLjUyLDQwLjUyLDAsMCwxLTQuMTgtMTguODQsNDAuNzUsNDAuNzUsMCwwLDEsNC4xOC0xOC45M0EzMC42LDMwLjYsMCwwLDEsODYuNzEsMzIuMiwzNS41MiwzNS41MiwwLDAsMSwxMDUsMjcuNjhhMzUuNTgsMzUuNTgsMCwwLDEsMTguMyw0LjUyLDMwLjU3LDMwLjU3LDAsMCwxLDExLjg4LDEyLjY0LDQwLjc2LDQwLjc2LDAsMCwxLDQuMTksMTguOTMsNDAuNTIsNDAuNTIsMCwwLDEtNC4xOSwxOC44NEEzMC41MSwzMC41MSwwLDAsMSwxMjMuMyw5NS4yNVExMTUuNTksOTkuNzgsMTA1LDk5Ljc3Wk0xMjcuMTQsNS4zMnYxMC41SDgyLjg3VjUuMzJabS0yMiw3OS40NWExMiwxMiwwLDAsMCwxMC44OS02cTMuNy02LDMuNy0xNS4xM1QxMTYsNDguNDhhMTIsMTIsMCwwLDAtMTAuODktNiwxMi4xNSwxMi4xNSwwLDAsMC0xMSw2cS0zLjczLDYtMy43MywxNS4xNnQzLjczLDE1LjEzQTEyLjE2LDEyLjE2LDAsMCwwLDEwNS4wOSw4NC43N1oiIGZpbGw9ImN1cnJlbnRDb2xvciI+PC9wYXRoPjxwYXRoIGQ9Ik0xODYuMywyOC41OVY0My4xNEgxNzMuMTZWNzdxMCw0LDEuODIsNS40YTcuNSw3LjUsMCwwLDAsNC43MywxLjQxLDE0LjcyLDE0LjcyLDAsMCwwLDIuNzItLjI1bDIuMDktLjM4LDMsMTQuNDFjLTEsLjMtMi4zMy42Ni00LjA5LDEuMDZhMzQuMTMsMzQuMTMsMCwwLDEtNi40MS43NXEtMTAuNTUuNDctMTYuOTMtNC41NlQxNTMuOCw3OS41VjQzLjE0aC05LjU1VjI4LjU5aDkuNTVWMTEuODZoMTkuMzZWMjguNTlaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48cGF0aCBkPSJNMjE2LDk5LjczcS0xMCwwLTE2LjU5LTUuMjN0LTYuNTktMTUuNTlxMC03LjgxLDMuNjgtMTIuMjdhMjEuMTksMjEuMTksMCwwLDEsOS42Ni02LjUzQTU0Ljc4LDU0Ljc4LDAsMCwxLDIxOSw1Ny40MWE5OC41Nyw5OC41NywwLDAsMCwxMy0xLjkxcTMuOTItMSwzLjkxLTQuMzZ2LS4yOGE4LjQyLDguNDIsMCwwLDAtMi43LTYuNjhxLTIuNzItMi4zNS03LjY2LTIuMzZhMTMuNzcsMTMuNzcsMCwwLDAtOC4zMiwyLjI3LDEwLjcsMTAuNywwLDAsMC00LjA5LDUuNzdsLTE3LjkxLTEuNDVhMjMuODgsMjMuODgsMCwwLDEsOS45My0xNS4xNHE3Ljk0LTUuNTgsMjAuNDgtNS41OWE0Mi4yNCw0Mi4yNCwwLDAsMSwxNC41NCwyLjQ2LDI0LjE5LDI0LjE5LDAsMCwxLDEwLjk0LDcuNjZxNC4xNiw1LjIxLDQuMTYsMTMuNTJWOTguNDFIMjM2LjkyVjg4LjczaC0uNTRhMjAuMTgsMjAuMTgsMCwwLDEtNy42Miw3LjkzUTIyMy42OSw5OS43MywyMTYsOTkuNzNabTUuNTQtMTMuMzdBMTUsMTUsMCwwLDAsMjMyLDgyLjY2YTExLjk0LDExLjk0LDAsMCwwLDQuMDktOS4yVjY2LjA1YTExLjM4LDExLjM4LDAsMCwxLTMuNTIsMS4zNmMtMS42LjM5LTMuMjkuNzMtNS4xLDFzLTMuNDEuNTQtNC44NC43NWExOS4xOSwxOS4xOSwwLDAsMC04LjIsMi44Nyw3LjA2LDcuMDYsMCwwLDAtMy4xMSw2LjIyLDYuOTQsNi45NCwwLDAsMCwyLjg4LDZBMTIuNDMsMTIuNDMsMCwwLDAsMjIxLjUxLDg2LjM2WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTI3OC42OSwxOS41OWExMC40MSwxMC40MSwwLDAsMS03LjM3LTIuODksOS4xNCw5LjE0LDAsMCwxLTMuMDktNi45Myw5LjEsOS4xLDAsMCwxLDMuMDktNi45MSwxMSwxMSwwLDAsMSwxNC43OCwwLDkuMSw5LjEsMCwwLDEsMy4wOSw2LjkxLDkuMTQsOS4xNCwwLDAsMS0zLjA5LDYuOTNBMTAuNDUsMTAuNDUsMCwwLDEsMjc4LjY5LDE5LjU5Wk0yNjksOTguNDFWMjguNTloMTkuMzZWOTguNDFaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)[Jotai]

状態

Primitive and flexible state management for React

</div>

# Core internals 

This guide is beneficial for those who want to understand the core implementation of Jotai. It\'s not meant to be a complete example of the core implementation but rather a simplified version. It\'s inspired by the collection of tweets by Daishi Kato([\@dai_shi](https://twitter.com/dai_shi)).

### [First Version](#first-version)

Let\'s start with an easy example. An atom is just a function that will return a configuration object. We are using WeakMap to map atom with their state. WeakMap doesn\'t keep its keys in memory, so if an atom is garbage collected, its state will be garbage collected too. This helps avoid memory leaks.

    import  from 'react'
    // atom function returns a config object which contains initial valueexport const atom = (initialValue) => ()
    // we need to keep track of the state of the atom.// we are using weakmap to avoid memory leaksconst atomStateMap = new WeakMap()const getAtomState = (atom) =>     atomStateMap.set(atom, atomState)  }  return atomState}
    // useAtom hook returns a tuple of the current value// and a function to update the atom's valueexport const useAtom = (atom) => , [atomState])
      const setAtom = (nextValue) => 
      return [value, setAtom]}

Here\'s an example using our simplified atom implementation. [Counter example](https://codesandbox.io/s/zealous-field-z2xk6?file=/src/App.js)

Ref tweet: [Demystifying the internal of jotai](https://twitter.com/dai_shi/status/1484835169475653634)

### [Second Version](#second-version)

Hang on! We can do better. In Jotai, we can create derived atom. A derived atom is an atom that depends on other atoms.

    const priceAtom = atom(10)const readOnlyAtom = atom((get) => get(priceAtom) * 2)const writeOnlyAtom = atom(  null, // it's a convention to pass `null` for the first argument  (get, set, args) => ,)const readWriteAtom = atom(  (get) => get(priceAtom) * 2,  (get, set, newPrice) => ,)

To keep track of all the dependents, we need to add one more property to the atom\'s state. Let\'s say atom X depends on atom Y, so when we update atom Y, we also update atom X. This is called dependency tracking.

    const atomState = 

We now need to create functions for reading and writing an atom that can handle updating dependent atoms\' state.

    import  from 'react'
    export const atom = (read, write) =>   }  const config =  else       }),  }  return config}
    // same as above but the state has one extra property: dependentsconst atomStateMap = new WeakMap()const getAtomState = (atom) =>     atomStateMap.set(atom, atomState)  }  return atomState}
    // If atom is primitive, we return it's value.// If atom is derived, we read the parent atom's value// and add current atom to parent's the dependent set (recursively).const readAtom = (atom) =>     const aState = getAtomState(a)    aState.dependents.add(atom) // XXX add only    return readAtom(a) // XXX no caching  }  const value = atom.read(get)  atomState.value = value  return value}
    // if atomState is modified, we need to notify all the dependent atoms (recursively)// now run callbacks for all the components that are dependent on this atomconst notify = (atom) => )  atomState.listeners.forEach((l) => l())}
    // writeAtom calls atom.write with the necessary params and triggers notify functionconst writeAtom = (atom, value) => 
      // if 'a' is the same as atom, update the value, notify that atom and return  // else calls writeAtom for 'a' (recursively)  const set = (a, v) =>     writeAtom(a, v)  }
      atom.write(get, set, value)}
    export const useAtom = (atom) => , [atom])  const setAtom = (nextValue) =>   return [value, setAtom]}

Here is an example using our derived atom implementation. [Derived counter example](https://codesandbox.io/s/affectionate-chandrasekhar-nuxms?file=/src/App.js)

Ref tweet: [Supporting derived atoms](https://twitter.com/dai_shi/status/1485434083778117632)

[library by [Daishi Kato]](https://twitter.com/dai_shi "Daishi Kato")[art by [Jessie Waters]](https://jessiewaters.com "Jessie Waters")[](https://candycode.com/ "candycode, an alternative graphic design and web development agency based in San Diego")

[site by]![candycode alternative graphic design web development agency San Diego](https://storage.googleapis.com/candycode/candycode.svg)