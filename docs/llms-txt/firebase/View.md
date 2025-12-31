# Source: https://firebase.google.com/docs/reference/swift/firebaseanalyticsswift/api/reference/Extensions/View.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingswift/api/reference/Extensions/View.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Extensions/View.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingswift/api/reference/Extensions/View.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Extensions/View.md.txt

# FirebaseInAppMessaging Framework Reference

# View

    public extension View

- `
  ``
  ``
  `

  ### [imageOnlyInAppMessage(closure:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Extensions/View#/s:7SwiftUI4ViewP22FirebaseInAppMessagingE09imageOnlyeF7Message7closureQrqd__So05FIRInfg5ImageI7DisplayC_So0lfgN8Delegate_ptc_tAaBRd__lF)

  `
  `  
  Overrides the default display of an image only in-app message as defined on the Firebase
  console.  

  #### Declaration

  Swift  

      @MainActor
      func imageOnlyInAppMessage<Content: View>(closure: @escaping (https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingImageOnlyDisplay.html,
                                                                    https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Protocols/InAppMessagingDisplayDelegate.html)
          -> Content)
        -> some View

[## Banner messages.](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Extensions/View#/Banner-messages.)

- `
  ``
  ``
  `

  ### [bannerInAppMessage(closure:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Extensions/View#/s:7SwiftUI4ViewP22FirebaseInAppMessagingE06bannereF7Message7closureQrqd__So05FIRInfG13BannerDisplayC_So0kfgM8Delegate_ptc_tAaBRd__lF)

  `
  `  
  Overrides the default display of a banner in-app message as defined on the Firebase console.  

  #### Declaration

  Swift  

      @MainActor
      func bannerInAppMessage<Content: View>(closure: @escaping (https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingBannerDisplay.html,
                                                                 https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Protocols/InAppMessagingDisplayDelegate.html)
          -> Content)
        -> some View

[## Modal messages.](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Extensions/View#/Modal-messages.)

- `
  ``
  ``
  `

  ### [modalInAppMessage(closure:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Extensions/View#/s:7SwiftUI4ViewP22FirebaseInAppMessagingE05modaleF7Message7closureQrqd__So05FIRInfG12ModalDisplayC_So0kfgM8Delegate_ptc_tAaBRd__lF)

  `
  `  
  Overrides the default display of a modal in-app message as defined on the Firebase console.  

  #### Declaration

  Swift  

      @MainActor
      func modalInAppMessage<Content: View>(closure: @escaping (https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingModalDisplay.html,
                                                                https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Protocols/InAppMessagingDisplayDelegate.html)
          -> Content)
        -> some View

[## Card messages.](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Extensions/View#/Card-messages.)

- `
  ``
  ``
  `

  ### [cardInAppMessage(closure:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Extensions/View#/s:7SwiftUI4ViewP22FirebaseInAppMessagingE04cardeF7Message7closureQrqd__So05FIRInfG11CardDisplayC_So0kfgM8Delegate_ptc_tAaBRd__lF)

  `
  `  
  Overrides the default display of a card in-app message as defined on the Firebase console.  

  #### Declaration

  Swift  

      @MainActor
      func cardInAppMessage<Content: View>(closure: @escaping (https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Classes/InAppMessagingCardDisplay.html,
                                                               https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Protocols/InAppMessagingDisplayDelegate.html)
          -> Content)
        -> some View