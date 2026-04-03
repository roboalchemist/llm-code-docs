# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/DFPCustomRenderedAd.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPCustomRenderedAd.md.txt

# GoogleMobileAds Framework Reference

# DFPCustomRenderedAd

    class DFPCustomRenderedAd : NSObject

Custom rendered ad. Your application renders the ad.
- `
  ``
  ``
  `

  ### [adHTML](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPCustomRenderedAd#/c:objc(cs)DFPCustomRenderedAd(py)adHTML)

  `
  `  
  The ad's HTML.  

  #### Declaration

  Swift  

      var adHTML: String { get }

- `
  ``
  ``
  `

  ### [adBaseURL](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPCustomRenderedAd#/c:objc(cs)DFPCustomRenderedAd(py)adBaseURL)

  `
  `  
  The base URL of the ad's HTML.  

  #### Declaration

  Swift  

      var adBaseURL: URL { get }

- `
  ``
  ``
  `

  ### [recordClick()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPCustomRenderedAd#/c:objc(cs)DFPCustomRenderedAd(im)recordClick)

  `
  `  
  Call this method when the user clicks the ad.  

  #### Declaration

  Swift  

      func recordClick()

- `
  ``
  ``
  `

  ### [recordImpression()](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPCustomRenderedAd#/c:objc(cs)DFPCustomRenderedAd(im)recordImpression)

  `
  `  
  Call this method when the ad is visible to the user.  

  #### Declaration

  Swift  

      func recordImpression()

- `
  ``
  ``
  `

  ### [finishedRenderingAdView(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/DFPCustomRenderedAd#/c:objc(cs)DFPCustomRenderedAd(im)finishedRenderingAdView:)

  `
  `  
  Call this method after the ad has been rendered in a UIView object.  

  #### Declaration

  Swift  

      func finishedRenderingAdView(_ view: UIView)