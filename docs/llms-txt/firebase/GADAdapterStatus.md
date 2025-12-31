# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADAdapterStatus.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdapterStatus.md.txt

# GoogleMobileAds Framework Reference

# GADAdapterStatus

    class GADAdapterStatus : NSObject, NSCopying

An immutable snapshot of a mediation adapter's initialization status.
- `
  ``
  ``
  `

  ### [state](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdapterStatus#/c:objc(cs)GADAdapterStatus(py)state)

  `
  `  
  Initialization state of the adapter.  

  #### Declaration

  Swift  

      var state: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADAdapterInitializationState.html { get }

- `
  ``
  ``
  `

  ### [description](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdapterStatus#/c:objc(cs)GADAdapterStatus(py)description)

  `
  `  
  Detailed description of the status.  

  #### Declaration

  Swift  

      var description: String { get }

- `
  ``
  ``
  `

  ### [latency](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADAdapterStatus#/c:objc(cs)GADAdapterStatus(py)latency)

  `
  `  
  The adapter's initialization latency in seconds. 0 if initialization has not yet ended.  

  #### Declaration

  Swift  

      var latency: TimeInterval { get }