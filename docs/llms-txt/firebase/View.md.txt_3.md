# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingswift/api/reference/Extensions/View.md.txt

# FirebaseInAppMessagingSwift Framework Reference

# View

    public extension View

- `


  ### [imageOnlyInAppMessage(closure:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingswift/api/reference/Extensions/View#/s:7SwiftUI4ViewP022FirebaseInAppMessagingA0E09imageOnlyeF7Message7closureQrqd__So05FIRInfg5ImageI7DisplayC_So0lfgN8Delegate_ptc_tAaBRd__lF)


  ` Overrides the default display of an image only in-app message as defined on the Firebase console.

  #### Declaration

  Swift

      func imageOnlyInAppMessage<Content: View>(closure: @escaping (InAppMessagingImageOnlyDisplay,
                                                                    InAppMessagingDisplayDelegate)
          -> Content)
        -> some View

[## Banner messages.](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingswift/api/reference/Extensions/View#/Banner-messages.)

- `


  ### [bannerInAppMessage(closure:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingswift/api/reference/Extensions/View#/s:7SwiftUI4ViewP022FirebaseInAppMessagingA0E06bannereF7Message7closureQrqd__So05FIRInfG13BannerDisplayC_So0kfgM8Delegate_ptc_tAaBRd__lF)


  ` Overrides the default display of a banner in-app message as defined on the Firebase console.

  #### Declaration

  Swift

      func bannerInAppMessage<Content: View>(closure: @escaping (InAppMessagingBannerDisplay,
                                                                 InAppMessagingDisplayDelegate)
          -> Content)
        -> some View

[## Modal messages.](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingswift/api/reference/Extensions/View#/Modal-messages.)

- `


  ### [modalInAppMessage(closure:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingswift/api/reference/Extensions/View#/s:7SwiftUI4ViewP022FirebaseInAppMessagingA0E05modaleF7Message7closureQrqd__So05FIRInfG12ModalDisplayC_So0kfgM8Delegate_ptc_tAaBRd__lF)


  ` Overrides the default display of a modal in-app message as defined on the Firebase console.

  #### Declaration

  Swift

      func modalInAppMessage<Content: View>(closure: @escaping (InAppMessagingModalDisplay,
                                                                InAppMessagingDisplayDelegate)
          -> Content)
        -> some View

[## Card messages.](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingswift/api/reference/Extensions/View#/Card-messages.)

- `


  ### [cardInAppMessage(closure:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingswift/api/reference/Extensions/View#/s:7SwiftUI4ViewP022FirebaseInAppMessagingA0E04cardeF7Message7closureQrqd__So05FIRInfG11CardDisplayC_So0kfgM8Delegate_ptc_tAaBRd__lF)


  ` Overrides the default display of a card in-app message as defined on the Firebase console.

  #### Declaration

  Swift

      func cardInAppMessage<Content: View>(closure: @escaping (InAppMessagingCardDisplay,
                                                               InAppMessagingDisplayDelegate)
          -> Content)
        -> some View