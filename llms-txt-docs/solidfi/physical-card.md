# Source: https://docs.solidfi.com/card-issuance/physical-card.md

# Physical Card

> A guide to Physical Cards

Solid offers its clients a fully managed card-art program. That means Solid manages the physical card approval with the issuing bank, network, and card printer.

### 1. Card Art

Solid has put together simple templates & guidelines for the card program to follow for the Front of Card (FOC) design to simplify the process and get the required approval.

When customizing a card for your card program, you have the option to choose between a horizontal or a vertical card. All our cards are Dual Interface (DI), which means they have a single embedded chip. This unique feature allows the card to be used in both contact and contactless transactions, providing flexibility and convenience to your users.

The instructions below explain the Front of Card (FOC) and Back of Card (BOC) template and the customization available to meet your brand guidelines.

<AccordionGroup>
  <Accordion title="Horizontal Front of Card (HFOC)">
    1. Start with a blank Horizontal Card

    <Frame caption="Blank Horizontal Card">
      <img src="https://cdn.prod.website-files.com/66633a8deaa98cd86b9f0eb3/66d10207e2295ef6ada9cf42_Horizontal-Card-Front-Blank.png" />
    </Frame>

    <Note>On a Consumer Debit Card, Visa product identifier will display Debit under the Visa logo.
    On a Business Debit Card, Business Debit will display on the top left.</Note>
    2\. Apply your brand's visual design and logo

    <Frame caption="Branded Horizontal Card">
      <img src="https://cdn.prod.website-files.com/66633a8deaa98cd86b9f0eb3/66d10207c68888336325778f_Horizontal-Card-Front-Branded.png" />
    </Frame>

    <Note>Depending on the card's visual design (dark or light), Solid will setup the correct Visa logo (Blue, White or Black). Logo needs to contrast the card design (background).</Note>
  </Accordion>

  <Accordion title="Vertical Front of Card (HFOC)">
    1. Start with a blank Vertical Card

    <Frame caption="Blank Vertical Card">
      <img src="https://cdn.prod.website-files.com/66633a8deaa98cd86b9f0eb3/66d10207c688883363257768_Vertical-Card-Front-Blank.png" />
    </Frame>

    <Note>On a Consumer Debit Card, Visa product identifier will display Debit under the Visa logo.
    On a Business Debit Card, Business Debit will display on the top left.</Note>
    2\. Apply your brand's visual design and logo

    <Frame caption="Branded Horizontal Card">
      <img src="https://cdn.prod.website-files.com/66633a8deaa98cd86b9f0eb3/66d10207e55e970307649439_Vertical-Card-Front-Branded.png" />
    </Frame>

    <Note>Depending on the card's visual design (dark or light), Solid will setup the correct Visa logo (Blue, White or Black). Logo needs to contrast the card design (background).</Note>
  </Accordion>

  <Accordion title="Back of Card (BOC)">
    Back of the card displays your card's visual design with the card information.

    <Frame caption="Back of Card">
      <img src="https://cdn.prod.website-files.com/66633a8deaa98cd86b9f0eb3/66d1020728ba5335e1db8d31_Card-Back.png" />
    </Frame>

    * Name of the business (for example: SNACKCO DELIVERY LLC) is displayed only if the card is a Business Debit or Business Credit card.
    * BOC remains the same in case of horizontal or vertical card.
    * BOC follows the Visa Quick Read (QR) Design to display the card information (16 digit cad number, expiry and CVV)
    * If the card's visual design (background) is dark, text is in displayed in white. If the card's visual design (background) is light, text is in displayed in black.
    * Name of the person and business to be embossed on the card, max limit is 23 characters.
  </Accordion>
</AccordionGroup>

You can download the cart art template's Figma file [here](https://www.figma.com/file/cwxnEXJtFIalnq96UCefSj/Card-Art-Template?node-id=0%3A1). Then, you can customize your card art using the Figma app or your web browser, export it to an SVG file, and send it back to Solid. Alternatively, you can send back your .fig file.

For physical cards, the printer will ultimately use EPS format with CMYK colors (Solid handles the formatting), so ideally, you would proof your colors in a design program such as Adobe Illustrator and export an EPS file from there.

### 2. Mailer Art

Solid manages the production of the physical card mailer with the card printer. The mailer is a 5x7 inch bi-fold greeting card style. See mock-ups below.

<Frame caption="Mailer Front">
  <img src="https://cdn.prod.website-files.com/66633a8deaa98cd86b9f0eb3/66d0e56bdcc4a998c2b11485_Mailer-Front.png" />
</Frame>

<Frame caption="Mailer Inside">
  <img src="https://cdn.prod.website-files.com/66633a8deaa98cd86b9f0eb3/66d0e56b503bad98e24619db_Mailer-Inside.png" />
</Frame>

<Frame caption="Mailer Outside">
  <img src="https://cdn.prod.website-files.com/66633a8deaa98cd86b9f0eb3/66d0e56b8cd2257453b1bb64_Mailer-Outside.png" />
</Frame>

<Frame caption="Mailer Open">
  <img src="https://cdn.prod.website-files.com/66633a8deaa98cd86b9f0eb3/66d0e56b95fdea503e95c6fb_Mailer-Open.png" />
</Frame>

Note:

* Both inside and outside pages can display your visual design.
* Card location cannot be changed.
* You can provide your copy for all the pages including card activation.
* The mailer cannot be customized for each cardholder.

You can download the mailer art template's Figma file [here](https://www.figma.com/file/cwxnEXJtFIalnq96UCefSj/Card-Art-Template?node-id=2%3A436). Then, you can customize your mailer art using the Figma app or your web browser, export it to an SVG file, and send it back to Solid. Alternatively, you can send back your .fig file.

### 3. Timelines

When issuing physical cards, timing is essential, but quality is even more so. Here are the key details you need to know:

* We will collaborate closely with you during the approximately two weeks it takes to configure your artwork. It ensures that all the necessary details are in place and your design looks exactly how you want it to.
* Once the artwork has been finalized, we will begin the printing process. Depending on the size of your order and our current workload, this typically takes around two days to complete.
* Finally, shipping times will vary based on the method you have selected. We offer a range of shipping options to meet your needs, from standard delivery to expedited shipping for those needing cards as quickly as possible.

By carefully managing each step of the process, we can ensure that your cards are delivered on time and with the highest quality.

### 4. Support

To comply with the issuing bank's requirements, you must provide support information to your cardholders, which needs to be included on the back of physical cards.

### 5. Reissuing Cards

You can [Reissue a Card](/v2/api-reference/cards/reissue-a-card) if your end user informs you that it is misplaced, lost, or stolen. Solid does not cover the cost of reissued cards for such scenarios.

If the card arrives damaged, you must request that your end user send photo evidence of the damage. Solid will contact its fulfillment partners for an explanation. In some cases, they may grant a credit. This credit is likely to cover shipping issues (resulting in a shipping credit), but it's possible that it could also cover printing issues (printing credit).
Please note that damaged cards are reviewed case by case and are not guaranteed. If a credit is received, it can be deducted from the program's next invoice. As usual, the program should submit a ticket for any such cases.

### 6. Multiple Card Designs (Themes)

Solid offers a feature called Solid Card Themes, which enables you to manage multiple card types and artwork within a single program.

For example, you could offer a single product that allows end users to choose a white or black card. Alternatively, you could use this feature to offer multiple financial products within a single program, such as Brand X Card and Brand Y Card.

Solid implementation team sets up themes in conjunction with your card program needs. Every card in the program will be assigned a unique theme, and each theme requires the artwork to be set up.

Once the Solid Solutions team has set up all card themes, they will provide you with the necessary information about the possible theme values, ensuring your confidence in the process.

You pass the theme in the [Create a Card](/v2/api-reference/cards/create-a-card) API.
