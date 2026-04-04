# Source: https://firebase.google.com/docs/reference/ios/googlemobileads/api/reference/Classes/GADSearchRequest.md.txt

# Source: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADSearchRequest.md.txt

# GoogleMobileAds Framework Reference

# GADSearchRequest

    class GADSearchRequest : https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADRequest.html

Specifies parameters for search ads.
- `
  ``
  ``
  `

  ### [query](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)query)

  `
  `  
  The search ad query.  

  #### Declaration

  Swift  

      var query: String? { get set }

- `
  ``
  ``
  `

  ### [backgroundColor](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)backgroundColor)

  `
  `  
  The search ad background color.  

  #### Declaration

  Swift  

      @NSCopying var backgroundColor: UIColor? { get }

- `
  ``
  ``
  `

  ### [gradientFrom](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)gradientFrom)

  `
  `  
  The search ad gradient from color.  

  #### Declaration

  Swift  

      @NSCopying var gradientFrom: UIColor? { get }

- `
  ``
  ``
  `

  ### [gradientTo](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)gradientTo)

  `
  `  
  The search ad gradient to color.  

  #### Declaration

  Swift  

      @NSCopying var gradientTo: UIColor? { get }

- `
  ``
  ``
  `

  ### [headerColor](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)headerColor)

  `
  `  
  The search ad header color.  

  #### Declaration

  Swift  

      @NSCopying var headerColor: UIColor? { get set }

- `
  ``
  ``
  `

  ### [descriptionTextColor](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)descriptionTextColor)

  `
  `  
  The search ad description text color.  

  #### Declaration

  Swift  

      @NSCopying var descriptionTextColor: UIColor? { get set }

- `
  ``
  ``
  `

  ### [anchorTextColor](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)anchorTextColor)

  `
  `  
  The search ad anchor text color.  

  #### Declaration

  Swift  

      @NSCopying var anchorTextColor: UIColor? { get set }

- `
  ``
  ``
  `

  ### [fontFamily](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)fontFamily)

  `
  `  
  The search ad text font family.  

  #### Declaration

  Swift  

      var fontFamily: String? { get set }

- `
  ``
  ``
  `

  ### [headerTextSize](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)headerTextSize)

  `
  `  
  The search ad header text size.  

  #### Declaration

  Swift  

      var headerTextSize: UInt { get set }

- `
  ``
  ``
  `

  ### [borderColor](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)borderColor)

  `
  `  
  The search ad border color.  

  #### Declaration

  Swift  

      @NSCopying var borderColor: UIColor? { get set }

- `
  ``
  ``
  `

  ### [borderType](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)borderType)

  `
  `  
  The search ad border type.  

  #### Declaration

  Swift  

      var borderType: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADSearchBorderType.html { get set }

- `
  ``
  ``
  `

  ### [borderThickness](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)borderThickness)

  `
  `  
  The search ad border thickness.  

  #### Declaration

  Swift  

      var borderThickness: UInt { get set }

- `
  ``
  ``
  `

  ### [customChannels](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)customChannels)

  `
  `  
  The search ad custom channels.  

  #### Declaration

  Swift  

      var customChannels: String? { get set }

- `
  ``
  ``
  `

  ### [callButtonColor](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(py)callButtonColor)

  `
  `  
  The search ad call button color.  

  #### Declaration

  Swift  

      var callButtonColor: https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Enums/GADSearchCallButtonColor.html { get set }

- `
  ``
  ``
  `

  ### [setBackgroundSolid(_:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(im)setBackgroundSolid:)

  `
  `  
  A solid background color for rendering the ad. The background of the ad
  can either be a solid color, or a gradient, which can be specified through
  setBackgroundGradientFrom:toColor: method. If both solid and gradient
  background is requested, only the latter is considered.  

  #### Declaration

  Swift  

      func setBackgroundSolid(_ color: UIColor)

- `
  ``
  ``
  `

  ### [setBackgroundGradientFrom(_:to:)](https://firebase.google.com/docs/reference/swift/googlemobileads/api/reference/Classes/GADSearchRequest#/c:objc(cs)GADSearchRequest(im)setBackgroundGradientFrom:toColor:)

  `
  `  
  A linear gradient background color for rendering the ad. The background of
  the ad can either be a linear gradient, or a solid color, which can be
  specified through setBackgroundSolid method. If both solid and gradient
  background is requested, only the latter is considered.  

  #### Declaration

  Swift  

      func setBackgroundGradientFrom(_ from: UIColor, to toColor: UIColor)