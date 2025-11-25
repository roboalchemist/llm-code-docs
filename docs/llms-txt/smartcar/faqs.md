# Source: https://smartcar.com/docs/help/oem-integrations/tesla/faqs.md

# Source: https://smartcar.com/docs/help/faqs.md

# Frequently Asked Questions (FAQs)

Below you'll find answers to some of the most frequently asked questions about Smartcar.

<AccordionGroup>
  <Accordion title="Does Smartcar make apps?">
    Smartcar does not build applications ourselves. Rather, we provide the building blocks that our customers need in order to build applications for a variety of use cases.
  </Accordion>

  <Accordion title="Do I need a connected services account?">
    Yes. For instance, if you own a VW, you will need to have Car-Net activated in the US or WeConnect in Europe. You can read more about connected service subscriptions [here](/help/brand-subscriptions).
  </Accordion>

  <Accordion title="What countries does Smartcar work in?">
    Take a look at our [Global Compatibility page](https://smartcar.com/global/) for the latest information on where Smartcar works.

    Smartcar is always expanding and working hard to ensure supported countries are stable and reliable. If your country is not currently supported, but you think we'll be a good fit for your use case, [schedule a demo](https://smartcar.com/demo/) and let's see how we can help you!
  </Accordion>

  <Accordion title="Which languages does Smartcar support?">
    [Smartcar Connect](/connect/what-is-connect) is available in English, Danish, German, Spanish (Spain), Spanish (Latin America), French, Italian, Dutch, Norwegian, and Swedish providing vehicle owners a native experience as they onboard vehicles to your platform.
  </Accordion>

  <Accordion title="How fresh is my data?">
    Smartcar will always try to pull the latest data point from any given vehicle. Each API response includes an [sc-data-age header](https://smartcar.com/docs/api#response-headers) that will contain the timestamp of when that data was last saved.

    Although each OEM saves data at different times, the data age header should not be older than the last time the vehicle was used.
  </Accordion>

  <Accordion title="How many cars is Smartcar compatible with?">
    <Tip>
      For a list of compatible vehicles, visit [our website](https://smartcar.com/product/compatible-vehicles/).
    </Tip>

    Smartcar is compatible with **161 million vehicles** across the US, Canada and Europe.

    **United States** <br />
    Smartcar is compatible with **29 car brands** in the United States.

    **Europe** <br />
    Smartcar is compatible with **19 car brands** in Europe.

    **Canada** <br />
    Smartcar is compatible with **21 car brands** in Canada.
  </Accordion>

  <Accordion title="Why isn't my car supported?">
    **If your make isn't supported...**

    We work hard to ensure that supported brands are stable and reliable, which takes time. If you don't see your make on our [compatibility page](https://smartcar.com/product/compatible-vehicles/) but you would like it to be, reach out to [support@smartcar.com](mailto:support@smartcar.com) to see how you can help speed up the process!

    **If we support your make, but not your model...**

    We might just need to do some additional testing. Sign up to our [research fleet](https://smartcar.com/research-fleet) and we'll reach out to see what we can do for you!

    **If we support your make, model, but not your year...**

    The majority of automakers only started adding internet connectivity to their cars around 2014. If you're able to access your car through a smartphone application and believe it should be supported, reach out to us and we'll be happy to take a look.
  </Accordion>

  <Accordion title="Smartcar versus Aftermarket Hardware">
    While on-board diagnostics dongles are versatile and useful for tracking and diagnostics of many kinds, they are far from ideal when it comes to mileage verification.
    They can be inaccurate, inconvenient, expensive and unreliable.Smartcar is only one example of a pure software alternative that uses API technology to offer the perfect
    mileage verification solution to auto insurance companies. Compared with traditional OBD-II devices, our API is accurate, cost efficient and tamper-resistant.

    You can read more about why using our API is a great choice on our [blog](https://smartcar.com/blog/obd-mileage-verification/).
  </Accordion>

  <Accordion title="Why do I see requests that resulted in a 460 status code with different error codes and error types on the Smartcar Dashboard?">
    In the event that we recieve a response from the OEM after the connection is closed, we will show the error code and error type we would have responded with on the Dashboard if the connection had been kept open.
  </Accordion>
</AccordionGroup>
