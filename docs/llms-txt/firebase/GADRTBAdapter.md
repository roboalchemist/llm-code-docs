# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Protocols/GADRTBAdapter.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRTBAdapter.md.txt

# GoogleMobileAds Framework Reference

# GADRTBAdapter

    protocol GADRTBAdapter : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADMediationAdapter.html

Adapter that provides signals to the Google Mobile Ads SDK to be included in an OpenRTB auction.
- `
  ``
  ``
  `

  ### [collectSignals(for:completionHandler:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Protocols/GADRTBAdapter#/c:objc(pl)GADRTBAdapter(im)collectSignalsForRequestParameters:completionHandler:)

  `
  `  
  Asks the receiver for encrypted signals. Signals are provided to the 3PAS at request time. The
  receiver must call completionHandler with signals or an error.

  This method is called on a non-main thread. The receiver should avoid using the main thread to
  prevent signal collection timeouts.  

  #### Declaration

  Swift  

      func collectSignals(for params: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRTBRequestParameters.html, completionHandler: @escaping https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Type-Definitions.html#/c:GADRTBAdapter.h@T@GADRTBSignalCompletionHandler)