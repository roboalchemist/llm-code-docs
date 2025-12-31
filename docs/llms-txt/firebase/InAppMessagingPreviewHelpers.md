# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingswift/api/reference/Enums/InAppMessagingPreviewHelpers.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Enums/InAppMessagingPreviewHelpers.md.txt

# FirebaseInAppMessaging Framework Reference

# InAppMessagingPreviewHelpers

    public enum InAppMessagingPreviewHelpers

Undocumented
- `
  ``
  ``
  `

  ### [cardMessage(campaignName:title:body:textColor:backgroundColor:portraitImage:landscapeImage:primaryButtonText:primaryButtonTextColor:primaryButtonBackgroundColor:primaryActionURL:secondaryButtonText:secondaryButtonTextColor:secondaryButtonBackgroundColor:secondaryActionURL:appData:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Enums/InAppMessagingPreviewHelpers#/s:22FirebaseInAppMessaging0bcD14PreviewHelpersO11cardMessage12campaignName5title4body9textColor010backgroundN013portraitImage09landscapeQ017primaryButtonText0stuN00st10BackgroundN00S9ActionURL09secondarytU00ytuN00ytvN00ywX07appDataSo05FIRIncD11CardDisplayCSS_S2SSgSo7UIColorCAYSo7UIImageCA_SgSSA2Y10Foundation0X0VSgAwYSgA5_A4_SDyS2SGSgtFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func cardMessage(campaignName: String = "Card message campaign",
                                     title: String = "Title for modal message",
                                     body: String? = "Body for modal message",
                                     textColor: UIColor = UIColor.label,
                                     backgroundColor: UIColor = UIColor.black,
                                     portraitImage: UIImage = UIImage(systemName: "rectangle")!,
                                     landscapeImage: UIImage? = UIImage(systemName: "square"),
                                     primaryButtonText: String = "Click me!",
                                     primaryButtonTextColor: UIColor = UIColor.systemBlue,
                                     primaryButtonBackgroundColor: UIColor = UIColor.systemGray,
                                     primaryActionURL: URL? = nil,
                                     secondaryButtonText: String? = "Dismiss",
                                     secondaryButtonTextColor: UIColor? = UIColor.secondaryLabel,
                                     secondaryButtonBackgroundColor: UIColor? = UIColor.systemYellow,
                                     secondaryActionURL: URL? = nil,
                                     appData: [String: String]? = nil) -> https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCardDisplay.html

- `
  ``
  ``
  `

  ### [modalMessage(campaignName:title:body:textColor:backgroundColor:image:buttonText:buttonTextColor:buttonBackgroundColor:actionURL:appData:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Enums/InAppMessagingPreviewHelpers#/s:22FirebaseInAppMessaging0bcD14PreviewHelpersO12modalMessage12campaignName5title4body9textColor010backgroundN05image10buttonText0qrN00q10BackgroundN09actionURL7appDataSo05FIRIncD12ModalDisplayCSS_S2SSgSo7UIColorCATSo7UIImageCSgArTSgAX10Foundation0U0VSgSDyS2SGSgtFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func modalMessage(campaignName: String = "Modal message campaign",
                                      title: String = "Title for modal message",
                                      body: String? = "Body for modal message",
                                      textColor: UIColor = UIColor.black,
                                      backgroundColor: UIColor = UIColor.white,
                                      image: UIImage? = UIImage(systemName: "rectangle"),
                                      buttonText: String? = "Click me!",
                                      buttonTextColor: UIColor? = UIColor.systemBlue,
                                      buttonBackgroundColor: UIColor? = UIColor
                                        .white,
                                      actionURL: URL? = nil,
                                      appData: [String: String]? = nil) -> https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingModalDisplay.html

- `
  ``
  ``
  `

  ### [bannerMessage(campaignName:title:body:textColor:backgroundColor:image:actionURL:appData:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Enums/InAppMessagingPreviewHelpers#/s:22FirebaseInAppMessaging0bcD14PreviewHelpersO13bannerMessage12campaignName5title4body9textColor010backgroundN05image9actionURL7appDataSo05FIRIncD13BannerDisplayCSS_S2SSgSo7UIColorCAQSo7UIImageCSg10Foundation0R0VSgSDyS2SGSgtFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func bannerMessage(campaignName: String = "Banner message campaign",
                                       title: String = "Title for banner message",
                                       body: String? = "Body for banner message",
                                       textColor: UIColor = UIColor.black,
                                       backgroundColor: UIColor = UIColor.white,
                                       image: UIImage? = UIImage(systemName: "square"),
                                       actionURL: URL? = nil,
                                       appData: [String: String]? = nil)
        -> https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingBannerDisplay.html

- `
  ``
  ``
  `

  ### [imageOnlyMessage(campaignName:image:actionURL:appData:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Enums/InAppMessagingPreviewHelpers#/s:22FirebaseInAppMessaging0bcD14PreviewHelpersO16imageOnlyMessage12campaignName0G09actionURL7appDataSo05FIRIncd5ImageH7DisplayCSS_So7UIImageC10Foundation0M0VSgSDyS2SGSgtFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func imageOnlyMessage(campaignName: String = "Image-only message campaign",
                                          image: UIImage,
                                          actionURL: URL? = nil,
                                          appData: [String: String]? = nil)
        -> https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageOnlyDisplay.html

- `
  ``
  ``
  `

  ### [Delegate](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Enums/InAppMessagingPreviewHelpers#/s:22FirebaseInAppMessaging0bcD14PreviewHelpersO8DelegateC)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public class Delegate : NSObject, https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Protocols/InAppMessagingDisplayDelegate.html