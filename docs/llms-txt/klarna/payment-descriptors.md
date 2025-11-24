# Source: https://docs.klarna.com/payments/web-payments/additional-resources/ux-guidelines/payment-descriptors.md

# Localized Messaging for Checkout

## Find the latest Klarna payment descriptors per region and translations.

**Payment category** column in the tables below is what will be returned in the response to the `create_session` request as `payment_method_categories.identifier`.

The copies provided in the column for respective locale **(`en-US`, `es_ES`, `en-BE`, etc.)** is what will be returned in the response to the create_session request as `payment_method_categories.name`.

The **payment button copy** in the tables below must be used when creating the Klarna Payment button in the checkout.

## **Europe**

### **Austria**

| **Payment Category** | **EN-AT**         | **DE-AT**            |
|----------------------|-------------------|----------------------|
| `pay_now`            | Pay in full today | Sofort bezahlen      |
| `pay_later`          | Pay later         | Später bezahlen      |
| `pay_over_time`      | Spread the cost   | Teile die Kosten auf |
| `klarna`             | Pay flexibly      | Flexibel bezahlen    |

#### Payment Descriptors Approaches

- **English**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Pay flexibly** Pay now, in 30 days, in 3 interest-free installments of xx.xx €, or as low as xx.xx €/month. Interest may apply. |
| **Pay later** Pay in 30 days. |  |
| **Spread the cost** Pay in 3 interest-free installments of xx.xx €, or as low as xx.xx €/month. Interest may apply. |  |

- **German**

| **Three options approach** | **Single option approach** |
|----|----|
| **Sofort bezahlen** Bezahle sicher per Sofortüberweisung, Lastschrift oder mit Karte. | **Flexibel bezahlen** Bezahle sicher per Sofortüberweisung, Lastschrift oder mit Karte, in bis zu 30 Tagen, in 3 zinsfreien Teilzahlungen zu je xx,xx € oder ab xx,xx € pro Monat. Zinsen können anfallen. |
| **Später bezahlen** Bezahle in bis zu 30 Tagen. |  |
| **Teile die Kosten auf** Bezahle in 3 zinsfreien Teilzahlungen zu je xx,xx € oder ab xx,xx € pro Monat. Zinsen können anfallen. |  |

#### Payment Button approaches

| **Copy**      | **AT-AT**         |
|---------------|-------------------|
| Without badge | Weiter mit Klarna |
| With badge    | Weiter mit        |

### **Belgium**

| **Payment Category** | **EN-BE**         | **NL-BE**         | **FR-BE**          |
|----------------------|-------------------|-------------------|--------------------|
| `pay_now`            | Pay in full today | Betaal nu         | Payez maintenant   |
| `pay_later`          | Pay later         | Betaal later      | Payez plus tard    |
| pay_over_time        | Pay in 3          | Betaal in 3 delen | Paiement en 3 fois |
| `klarna`             | Pay with Klarna   | Betaal met Klarna | Payez avec Klarna  |

#### Payment Descriptors Approaches

- **English**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Pay with Klarna** Pay now, in 30 days, or in 3 installments. |
| **Pay later** Pay in 30 days. |  |
| **Pay in 3** Pay in 3 installments. |  |

- **Dutch**

| **Three options approach** | **Single option approach** |
|----|----|
| **Betaal nu** Betaal het hele bedrag vandaag. | **Betaal met Klarna** Betaal het hele bedrag vandaag, binnen 30 dagen, of in 3 delen. |
| **Betaal later** Betaal binnen 30 dagen. |  |
| **Betaal in 3 delen** Betaal in 3 delen. |  |

- **French**

| **Three options approach** | **Single option approach** |
|----|----|
| **Payez maintenant** Payez la totalité aujourd'hui. | **Payez avec Klarna** Payez maintenant, dans 30 jours ou en 3 versements. |
| **Payez plus tard** Payez dans 30 jours. |  |
| **Paiement en 3 fois** Payez en 3 versements. |  |

#### Payment Button approaches

| **Copy**      | **NL-BE**             | **FR-BE**             |
|---------------|-----------------------|-----------------------|
| Without badge | Verdergaan met Klarna | Continuer avec Klarna |
| With badge    | Verdergaan met        | Continuer avec        |

### **Czech Republic**

| **Payment Category** | **EN-CZ** | **CS-CZ** |
|----|----|----|
| `pay_now` | Pay in full today | Zaplať teď |
| `pay_later` | Pay later | Zaplať později |
| `pay_over_time` | Pay in 3 | Zaplať ve 3 platbách |
| `klarna` | Flexible payments with Klarna | Flexibilní platby s Klarna |

#### Payment Descriptors Approaches

- **English**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Flexible payments with Klarna** Pay now, in 30 days, or in 3 installments of x.xx kč. |
| **Pay later** Pay in 30 days. |  |
| **Pay in 3** Pay in 3 installments of x.xx kč. |  |

- **Czech**

| **Three options approach** | **Single option approach** |
|----|----|
| **Zaplať teď** Zaplať celou část dnes. | **Flexibilní platby s Klarnou.** Zaplať celou část dnes, za 30 dní, nebo ve 3 platbách ve výši x.xx kč. |
| **Zaplať později** Zaplať za 30 dní. |  |
| **Zaplať ve 3 platbách** Zaplať ve 3 platbách ve výši x.xx kč. |  |

#### Payment Button approaches

| **Copy**      | **CS-CH**          |
|---------------|--------------------|
| Without badge | Pokračuj s Klarnou |
| With badge    | Pokračuj s         |

### **Denmark**

| **Payment Category** | **EN-DK**         | **DK-DK**        |
|----------------------|-------------------|------------------|
| `pay_now`            | Pay in full today | Betal nu         |
| `pay_later`          | Pay later         | Betal senere     |
| `pay_over_time`      | Pay in 3          | Betal i 3 dele   |
| `klarna`             | Pay with Klarna   | Betal med Klarna |

#### Payment Descriptors Approaches

- **English**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Pay with Klarna** Pay now, in 30 days, or in 3 installments of x,xx kr. |
| **Pay later** Pay in 30 days. |  |
| **Pay in 3** Pay in 3 installments of x,xx kr. |  |

- **Danish**

| **Three options approach** | **Single option approach** |
|----|----|
| **Betal nu** Betal hele beløbet i dag. | **Betal med Klarna** Betal hele beløbet nu, i 3 dele af x,xx kr., eller om 30 dage. Rentefrit. |
| **Betal senere** Betal om 30 dage. |  |
| **Betal i 3 dele** Betal i 3 dele af x,xx kr. |  |

#### Payment Button approaches

| **Copy**      | **DA-DK**          |
|---------------|--------------------|
| Without badge | Fortsæt med Klarna |
| With badge    | Fortsæt med        |

### **Finland**

| **Payment Category** | **EN-FI** | **FI-FI** | **SV-FI** |
|----|----|----|----|
| `pay_now` | Online banking and card-payment | Verkkopankki- ja korttimaksu | Bank- och kortbetalning |
| `pay_later` | Pay later | Maksa myöhemmin | Betala senare |
| `pay_over_time` | Financing | Erämaksu | Delbetalning |
| `klarna` | Pay with Klarna | Maksa Klarnalla | Betala med Klarna |

#### Payment Descriptors Approaches

- **English**

| **Three options approach** | **Single option approach** |
|----|----|
| **Online banking and card payment** Pay in full today. | **Pay with Klarna** Pay in full today, in 30 days, or as low as x.xx €/month. |
| **Pay later** Pay in 30 days. |  |
| **Financing** Pay as low as x.xx €/month. |  |

- **Finnish**

| **Three options approach** | **Single option approach** |
|----|----|
| **Verkkopankki- ja korttimaksu** Maksa heti. | **Maksa Klarnalla** Maksa heti, 30 päivässä tai erissä alkaen x.xx €/kuukausi. |
| **Maksa myöhemmin** Maksa 30 päivässä. |  |
| **Erämaksu** Maksa erissä alkaen x.xx €/kuukausi. |  |

- **Swedish**

| **Three options approach** | **Single option approach** |
|----|----|
| **Bank- och kortbetalning** Betala hela beloppet idag. | **Betala med Klarna** Betala hela beloppet idag, om 30 dagar, eller så lite som x.xx €/månad. |
| **Betala senare** Betala om 30 dagar. |  |
| **Delbetalning** Betala så lite som x.xx €/månad. |  |

#### Payment Button approaches

| **Copy**      | **FI-FI**       | **SV-FI**           |
|---------------|-----------------|---------------------|
| Without badge | Jatka Klarnalla | Fortsätt med Klarna |
| With badge    | Jatka Klarnalla | Fortsätt med        |

### **France**

| **Payment Category** | **EN-FR** | **FR-FR** |
|----|----|----|
| `pay_now` | Pay in full today | Payez maintenant |
| `pay_later` | Pay later | Payez plus tard |
| `pay_over_time` | Pay in 3 | Payez en 3 fois |
| `klarna` | Flexible payments with Klarna | Paiements flexibles avec Klarna |

#### Payment Descriptors Approaches

- **English**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Flexible payments with Klarna** Pay now, in 30 days, or in 3 installments of x.xx€. |
| **Pay later** Pay in 30 days. |  |
| **Pay in 3** Pay in 3 installments of x.xx€.   |  |

- **French**

| **Three options approach** | **Single option approach** |
|----|----|
| **Payez maintenant** Payez la totalité aujourd'hui. | **Paiements flexibles avec Klarna** Payez la totalité aujourd'hui, dans 30 jours ou en 3 versements de x.xx€. |
| **Payez plus tard** Payez dans 30 jours. |  |
| **Payez en 3 fois** Payez en 3 versements de x.xx€. |  |

#### Payment Button approaches

| **Copy**      | **FR-FR**             |
|---------------|-----------------------|
| Without badge | Continuer avec Klarna |
| With badge    | Continuer avec        |

### **Germany**

| **Payment Category** | **EN-DE**         | **DE-DE**            |
|----------------------|-------------------|----------------------|
| `pay_now`            | Pay in full today | Sofort bezahlen      |
| `pay_later`          | Pay later         | Später bezahlen      |
| `pay_over_time`      | Spread the cost   | Teile die Kosten auf |
| `klarna`             | Pay flexibly      | Flexibel bezahlen    |

#### Payment Descriptors Approaches

- **English**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Pay flexibly** Pay now, in 30 days, in 3 interest-free installments of xx.xx €, or as low as xx.xx €/month. Interest may apply. |
| **Pay later** Pay in 30 days. |  |
| **Spread the cost** Pay in 3 interest-free installments of xx.xx €, or as low as xx.xx €/month. Interest may apply. |  |

- **German**

| **Three options approach** | **Single option approach** |
|----|----|
| **Sofort bezahlen** Bezahle sicher per Sofortüberweisung, Lastschrift oder mit Karte. | **Flexibel bezahlen** Bezahle sicher per Sofortüberweisung, Lastschrift oder mit Karte, in bis zu 30 Tagen, in 3 zinsfreien Teilzahlungen zu je xx,xx € oder ab xx,xx € pro Monat. Zinsen können anfallen. |
| **Später bezahlen** Bezahle in bis zu 30 Tagen. |  |
| **Teile die Kosten auf** Bezahle in 3 zinsfreien Teilzahlungen zu je xx,xx € oder ab xx,xx € pro Monat. Zinsen können anfallen. |  |

#### Payment Button approaches

| **Copy**      | **DE-DE**         |
|---------------|-------------------|
| Without badge | Weiter mit Klarna |
| With badge    | Weiter mit        |

### **Greece**

| **Payment Category** | **EN-GR** | **EL-GR** |
|----|----|----|
| `pay_now` | Pay in full today | Πληρωμή τώρα |
| `pay_later` | Pay later | Πληρωμή αργότερα |
| `pay_over_time` | Pay in 3 | Πληρωμή σε 3 άτοκες δόσεις |
| `klarna` | Flexible payments with Klarna | Ευέλικτες πληρωμές με Klarna |

#### Payment Descriptors Approaches

- **English**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Flexible payments with Klarna** Pay now, in 30 days, or in 3 installments of x.xx€. |
| **Pay later** Pay in 30 days. |  |
| **Pay in 3** Pay in 3 installments of x.xx€. |  |

- **Greek**

| **Three options approach** | **Single option approach** |
|----|----|
| **Πληρωμή τώρα** Πληρώστε τώρα όλο το ποσό. | **Ευέλικτες πληρωμές με Klarna** Πληρώστε τώρα όλο το ποσό ή σε 30 ημέρες ή σε 3 άτοκες δόσεις των x.xx€. |
| **Πληρωμή αργότερα** Πληρώστε σε 30 ημέρες. |  |
| **Πληρωμή σε 3 άτοκες δόσεις** Πληρώστε σε 3 άτοκες δόσεις των x.xx€. |  |

#### Payment Button approaches

| **Copy**      | **EL-GR**              |
|---------------|------------------------|
| Without badge | Συνέχεια με την Klarna |
| With badge    | Συνέχεια με Klarna     |

### **Hungary**

| **Payment Category** | **EN-HU** | **HU-HU** |
|----|----|----|
| `pay_now` | Pay in full today | Fizess most\< |
| `pay_later` | Pay later | Fizess később |
| `pay_over_time` | Pay in 3 | Fizess 3 részletben |
| `klarna` | Flexible payments with Klarna | Rugalmas fizetési lehetőségek a Klarnával |

#### Payment Descriptors Approaches

- **English**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Flexible payments with Klarna** Pay now, in 30 days, or in 3 installments of x.xx Ft. |
| **Pay later** Pay in 30 days. |  |
| **Pay in 3** Pay in 3 installments of x.xx Ft. |  |

- **Hungarian**

| **Three options approach** | **Single option approach** |
|----|----|
| **Fizess most** Fizesd ki a teljes összeget most. | **Rugalmas fizetési lehetőségek a Klarnával** Fizess ki a teljes összeget most, 30 napon belül, vagy 3 x.xx Ft-os részletben. |
| **Fizess később** Fizess 30 napon belül. |  |
| **Fizess 3 részletben** Fizess 3 x.xx Ft-os részletben. |  |

#### Payment Button approaches

| **Copy**      | **HU-HU**        |
|---------------|------------------|
| Without badge | Tovább Klarnával |
| With badge    | Tovább           |

### **Ireland**

| **Payment Category** | **EN-IE**                     |
|----------------------|-------------------------------|
| `pay_now`            | Pay in full today             |
| `pay_later`          | Pay later                     |
| `pay_over_time`      | Pay in 3                      |
| `klarna`             | Flexible payments with Klarna |

#### Payment Descriptors Approaches

- **English**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Flexible payments with Klarna** Pay now or in 3 installments of €x.xx. |
| **Pay in 3** Pay in 3 installments of €x.xx. |  |
| **Pay later** Pay in 30 days. |  |

#### Payment Button approaches

| **Copy**      | **EN-IE**            |
|---------------|----------------------|
| Without badge | Continue with Klarna |
| With badge    | Continue with        |

### **Italy**

| Payment Category | EN-IT | IT-IT |
|----------------|-----|-----|
| `pay_now` | Pay in full today | Paga ora |
| `pay_later` | Pay later | Paga dopo |
| `pay_over_time` | <ul><li>Pay in 3 (without financing</li><li>Pay over time (with financing)</li></ul> | <ul><li>Paga in 3 rate (without financing)</li><li>Paga a rate (with financing)</li></ul> |
| `klarna` | Flexible payments with Klarna | Pagamenti flessibili con Klarna |

#### Payment Descriptors Approaches

- **English - without financing**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Flexible payments with Klarna** Pay now, in 30 days, or in 3 installments of x.xx€. |
| **Pay later** Pay in 30 days. |  |
| **Pay in 3** Pay in 3 installments of x.xx€. |  |

- **English - with financing**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Flexible payments with Klarna** Pay now, in 30 days, in 3 installments of x.xx€, or as low as x.xx€/month. |
| **Pay later** Pay in 30 days. |  |
| **Pay over time** Pay in 3 installments of x.xx€ or as low as x.xx€/month. |  |

- **Italian - without financing**

| **Three options approach** | **Single option approach** |
|----|----|
| **Paga ora** Paga tutto oggi. | **Pagamenti flessibili con Klarna** Paga tutto oggi, dopo 30 giorni o in 3 rate da x.xx€. |
| **Paga dopo** Paga dopo 30 giorni. |  |
| **Paga in 3 rate** Paga in 3 rate da x.xx€. |  |

- **Italian - with financing**

| **Three options approach** | **Single option approach** |
|----|----|
| **Paga ora** Paga tutto oggi. | **Pagamenti flessibili con Klarna** Paga tutto oggi, dopo 30 giorni, in 3 rate da x.xx€ o a partire da x.xx€/mese. |
| **Paga dopo** Paga dopo 30 giorni. |  |
| **Paga a rate** Paga in 3 rate da x.xx€ o a partire da x.xx€/mese. |  |

#### Payment Button approaches

| **Copy**      | **IT-IT**           |
|---------------|---------------------|
| Without badge | Continua con Klarna |
| With badge    | Continua con        |

### **Netherlands**

| **Payment Category** | **EN-NL**         | **NL-NL**         |
|----------------------|-------------------|-------------------|
| `pay_now`            | Pay in full today | Betaal nu         |
| `pay_later`          | Pay later         | Betaal later      |
| `pay_over_time`      | Pay in 3          | Betaal in 3 delen |
| `klarna`             | Pay with Klarna   | Betaal met Klarna |

#### Payment Descriptors Approaches

- **English**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Pay with Klarna** Pay now, in 30 days, or in 3 installments of € X,XX. |
| **Pay later** Pay in 30 days. |  |
| **Pay in 3** Pay in 3 installments of € X,XX. |  |

- **Dutch**

| **Three options approach** | **Single option approach** |
|----|----|
| **Betaal nu** Betaal het hele bedrag vandaag. | **Betaal met Klarna** Betaal het hele bedrag vandaag, binnen 30 dagen, of in 3 delen van € X,XX. |
| **Betaal later** Betaal binnen 30 dagen. |  |
| **Betaal in 3 delen** Betaal in 3 delen van € X,XX. |  |

#### Payment Button approaches

| **Copy**      | **NL-NL**             |
|---------------|-----------------------|
| Without badge | Verdergaan met Klarna |
| With badge    | Verdergaan met        |

### **Norway**

| **Payment Category** | **EN-NO**         | **NO-NO**        |
|----------------------|-------------------|------------------|
| `pay_now`            | Pay in full today | Betal nå         |
| `pay_later`          | Pay later         | Betal senere     |
| `pay_over_time`      | Financing         | Delbetaling      |
| `klarna`             | Pay with Klarna   | Betal med Klarna |

#### Payment Descriptors Approaches

- **English**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Pay with Klarna** Pay now, in 30 days, in 3 installments of x,xx kr or as low as x,xx kr/month. |
| **Pay later** Pay in 30 days. |  |
| **Financing** Pay in 3 installments of x,xx kr or as low as x,xx kr/month. |  |

- **Norwegian**

| **Three options approach** | **Single option approach** |
|----|----|
| **Betal nå** Betal hele beløpet idag. | **Betal med Klarna** Betal nå, om 30 dager, i 3 deler à x,xx kr eller fra x,xx kr per måned. |
| **Betal senere** Betal om 30 dager. |  |
| **Delbetaling** Betal i 3 deler à x,xx kr eller fra x,xx kr per måned. |  |

#### Payment Button approaches

| **Copy**      | **NB-NO**           |
|---------------|---------------------|
| Without badge | Fortsett med Klarna |
| With badge    | Fortsett med        |

### **Poland**

| **Payment Category** | **EN-PL** | **PL-PL** |
|----|----|----|
| `pay_now` | Pay in full today | Zapłać teraz |
| `pay_later` | Pay later | Zapłać później |
| `pay_over_time` | Pay in 3 | Zapłać w 3 ratach |
| `klarna` | Flexible payments with Klarna | Elastyczne płatności z Klarną |

#### Payment Descriptors Approaches

- **English**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Flexible payments with Klarna** Pay now, in 30 days, or in 3 installments of x,xx zl. |
| **Pay later** Pay in 30 days. |  |
| **Pay in 3** Pay in 3 interest-free installments of x,xx zl. |  |

- **Polish**

| **Three options approach** | **Single option approach** |
|----|----|
| **Zapłać teraz** Zapłać całość dzisiaj. | **Elastyczne płatności z Klarną** Zapłać całość dzisiaj, za 30 dni lub w 3 ratach po x,xx zl. |
| **Zapłać później** Zapłać za 30 dni. |  |
| **Zapłać w 3 ratach** Płatność w 3 ratach po x,xx zl. |  |

#### Payment Button approaches

| **Copy**      | **PL-PL**          |
|---------------|--------------------|
| Without badge | Kontynuuj z Klarna |
| With badge    | Kontynuuj z        |

### **Portugal**

| **Payment Category** | **EN-PT** | **PT-PT** |
|----|----|----|
| `pay_now` | Pay in full today | Paga agora |
| `pay_later` | Pay later | Paga mais tarde |
| `pay_over_time` | Pay in 3 | Paga em 3 prestações |
| `klarna` | Flexible payments with Klarna | Pagamentos flexíveis com Klarna |

#### Payment Descriptors Approaches

- **English**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Flexible payments with Klarna** Pay now, in 30 days, or in 3 installments of x,xx €. |
| **Pay later** Pay in 30 days. |  |
| **Pay in 3** Pay in 3 installments of x,xx €. |  |

- **Portuguese**

| **Three options approach** | **Single option approach** |
|----|----|
| **Paga agora** Paga hoje na totalidade. | **Pagamentos flexíveis com Klarna** Paga agora, a 30 dias ou em 3 prestações de x,xx €. |
| **Paga mais tarde** Paga a 30 dias. |  |
| **Paga em 3 prestações** Paga em 3 prestações de x,xx €. |  |

#### Payment Button approaches

| **Copy**      | **PT-PT**            |
|---------------|----------------------|
| Without badge | Continuar com Klarna |
| With badge    | Continuar com        |

### **Romania**

| **Payment Category** | **EN-RO** | **RO-RO** |
|----|----|----|
| `pay_now` | Pay in full today | Plătește acum |
| `pay_later` | Pay later | Plătește mai târziu |
| `pay_over_time` | Pay in 3 | Plătește în 3 |
| `klarna` | Flexible payments with Klarna | Plăți flexibile cu Klarna |

#### Payment Descriptors Approaches

- **English**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Flexible payments with Klarna** Pay now, in 30 days, or in 3 installments of x,xx lei. |
| **Pay later** Pay in 30 days. |  |
| **Pay in 3** Pay in 3 installments of x,xx lei. |  |

- **Romanian**

| **Three options approach** | **Single option approach** |
|----|----|
| **Plătește acum** Plătește integral astǎzi. | **Plăți flexibile cu Klarna** Plătește acum, în 30 de zile sau în 3 rate în valoare de x,xx lei. |
| **Plătește mai târziu** Plătește în 30 de zile. |  |
| **Plătește în 3** Plătește în 3 rate în valoare de x,xx lei. |  |

#### Payment Button approaches

| **Copy**      | **RO-RO**          |
|---------------|--------------------|
| Without badge | Continuă cu Klarna |
| With badge    | Continuă cu        |

### **Slovakia**

| **Payment Category** | **EN-SK** | **SK-SK** |
|----|----|----|
| `pay_now` | Pay in full today | Zaplať teraz |
| `pay_later` | Pay later | Zaplaťneskôr |
| `pay_over_time` | Pay in 3 | Zaplať v 3 platbách |
| `klarna` | Flexible payments with Klarna | Flexibilné platby s Klarnou |

#### Payment Descriptors Approaches

- **English**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Flexible payments with Klarna** Pay now, in 30 days, or in 3 installments of x,xx €. |
| **Pay later** Pay in 30 days. |  |
| **Pay in 3** Pay in 3 installments of x,xx €. |  |

- **Slovak**

| Three options approach | Single option approach |
|----------------------|----------------------|
| Zaplať teraz Zaplať celú čiastku dnes. | Flexibilné platby s Klarnou Zaplať celú čiastku dnes, za 30 dní, alebo v 3 bezúročných platbách po x,xx €. |
| Zaplaťneskôr Zaplať za 30 dní. |  |
| Zaplať v 3 platbách Zaplať v 3 bezúročných platbách po x,xx €. |  |

#### Payment Button approaches

| **Copy**      | **SK-SK** |
|---------------|-----------|
| Without badge |           |
| With badge    |           |

### **Spain**

| Payment Category | EN-ES (without financing) | ES-ES (without financing) |
|----------------|-------------------------|-------------------------|
| `pay_now` | Pay in full today | Paga el total hoy |
| `pay_later` | Pay later | Paga más tarde |
| `pay_over_time` | <ul><li>Pay in 3 (without financing)</li></ul> | <ul><li>Divide el coste (without financing)</li></ul> |
| `klarna` | Flexible payments with Klarna | Pagos flexibles con Klarna |

#### Payment Descriptors Approaches

- **English without financing**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Flexible payments with Klarna** Pay now, in 30 days, or in 3 installments of x.xx €. |
| **Pay later** Pay in 30 days. |  |
| **Pay in 3** Pay in 3 installments of x.xx €. |  |

- **Spanish without financing**

| **Three options approach** | **Single option approach** |
|----|----|
| **Paga el total hoy** Sin comisiones ni intereses. | **Pagos flexibles con Klarna** Paga el total hoy, paga en 30 días o en 3 plazos de X.XX €. |
| **Paga más tarde** Paga en 30 días. |  |
| **Divide el coste** Paga en 3 plazos de X.XX €. |  |

- **English with financing**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Flexible payments with Klarna** Pay now, in 30 days, in 3 installments of x.xx€ or as low as x.xx€/month. |
| **Pay later** Pay in 30 days. |  |
| **Financing** Pay in 3 installments of x.xx€ or as low as x.xx€/month. |  |

- **Spanish with financing**

| **Three options approach** | **Single option approach** |
|----|----|
| **Paga el total hoy** Sin comisiones ni intereses. | **Pagos flexibles con Klarna** Paga ahora, en 30 días, en 3 plazos de x,xx €, o desde x,xx € /mes. |
| **Paga más tarde** Paga en 30 días.   |  |
| **Divide el coste** Paga en 3 plazos de X.XX € o desde x,xx € /mes. |  |

#### Payment Button approaches

| **Copy**      | **ES-ES**            |
|---------------|----------------------|
| Without badge | Continuar con Klarna |
| With badge    | Continuar con        |

### Sweden

| **Payment Category** | **EN-SE**         | **SV-SE**         |
|----------------------|-------------------|-------------------|
| `pay_now`            | Pay in full today | Betala direkt     |
| `pay_later`          | Pay later         | Betala senare     |
| `pay_over_time`      | Financing         | Dela upp          |
| `klarna`             | Pay with Klarna   | Betala med Klarna |

#### Payment Descriptors Approaches

- **English**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Pay with Klarna** Pay now,  in 3 installments of x.xx kr or as low as x.xx kr/month, in 30 days or with monthly invoice. |
| **Pay later** Pay in 30 days or with monthly invoice. |  |
| **Financing** Pay in 3 installments of x.xx kr or as low as x.xx kr/month. |  |

- **Swedish**

| **Three options approach** | **Single option approach** |
|----|----|
| **Betala direkt** Betala hela beloppet idag. | **Betala med Klarna** Betala hela beloppet idag, i 3 delar om x.xx kr eller från x.xx kr/månad, inom 30 dagar eller med månadsfaktura. |
| **Betala senare** Betala om 30 dagar eller med månadsfaktura. |  |
| **Dela upp** Betala i 3 delar om x.xx kr eller från x.xx kr/månad. |  |

#### Payment Button approaches

| **Copy**      | **SV-SE**           |
|---------------|---------------------|
| Without badge | Fortsätt med Klarna |
| With badge    | Fortsätt med        |

### **Switzerland**

| **Payment Category** | **EN-CH** | **DE-CH** | **FR-CH** | **IT-CH** |
|----|----|----|----|----|
| `pay_now` | Pay in full today | Sofort bezahlen | Payer maintenant | Paga ora |
| `pay_later` | Pay later | Später bezahlen | Payer dans 30 jours | Paga dopo |
| `pay_over_time` | 3 interest-free installments | 3 zinsfreie Teilzahlungen | Payer en 3 fois sans frais | Dividi il costo |
| `klarna` | Pay with Klarna | Flexibel bezahlen | Paiements flexibles avec Klarna | Paga con Klarna |

#### Payment Descriptors Approaches

- **English**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Pay with Klarna** Pay now, in 30 days or over two months. |
| **Pay later** Pay in 30 days. |  |
| **3 interest-free installments** Pay over two months. |  |

- **German**

| **Three options approach** | **Single option approach** |
|----|----|
| **Sofort bezahlen** Bezahle sicher und schnell per Sofortüberweisung. | **Flexibel bezahlen** Bezahle sicher und schnell per Sofortüberweisung, in bis zu 30 Tagen oder über zwei Monate. |
| **Später bezahlen** Bezahle in bis zu 30 Tagen. |  |
| **3 zinsfreie Teilzahlungen** Bezahle über zwei Monate. |  |

- **French**

| **Three options approach** | **Single option approach** |
|----|----|
| **Payer maintenant** Payer la totalité aujourd’hui. | **Paiements flexibles avec Klarna** Payer la totalité aujourd’hui, plus tard ou en 3 versements. |
| **Payer dans 30 jours** Payer plus tard. |  |
| **Payer en 3 fois sans frais** Payer en 3 versements. |  |

- **Italian**

| **Three options approach** | **Single option approach** |
|----|----|
| **Paga ora** Paga tutto oggi. | **Paga con Klarna** Paga tutto oggi, dopo 30 giorni o in 3 rate senza interessi. |
| **Paga dopo** Paga dopo 30 giorni. |  |
| **Dividi il costo** Paga in 3 rate senza interessi. |  |

#### Payment Button approaches

| **DE-CH**     | **FR-CH**         | **IT-CH**             |
|---------------|-------------------|-----------------------|
| Without badge | Weiter mit Klarna | Continuer avec Klarna |
| With badge    | Weiter mit        | Continuer avec        |

### United Kingdom

| **Payment Category** | **EN-GB**         |
|----------------------|-------------------|
| `pay_now`            | Pay in full today |
| `pay_later`          | Pay later         |
| `pay_over_time`      | Pay over time     |
| `klarna`             | Pay with Klarna   |

#### Payment Descriptors Approaches

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Pay with Klarna** Pay now, in 30 days, in 3 instalments of £x.xx, or as low as £x.xx/month. |
| **Pay later** Pay in 30 days. |  |
| **Pay over time** Pay in 3 instalments of £x.xx or pay as low as £x.xx/month. |  |

#### Payment Button approaches

| **EN-GB**     |
|---------------|
| Without badge |
| With badge    |

## Americas

### **Canada**

| **Payment Category** | **EN-CA** | **FR-CA** |
|----|----|----|
| `pay_now` | Pay in full today | Payez maintenant |
| `pay_later` | Pay later | Payez plus tard |
| `pay_over_time` | Pay over time | Payez dans le temps |
| `klarna` | Flexible payments with Klarna | Paiements flexibles avec Klarna |

#### Payment Descriptors Approaches

- **English**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Flexible payments with Klarna** Pay now, in 4 payments of \$x.xx, or as low as \$x.xx/month. |
| **Pay over time** Pay in 4 payments of \$x.xx or as low as \$x.xx/month. |  |
| ***Pay later*** *Pay in 30 days.* |  |

- **French**

| **Three options approach** | **Single option approach** |
|----|----|
| **Payez maintenant** Payez la totalité aujourd'hui. | **Paiements flexibles avec Klarna** Payez la totalité aujourd'hui, ou en 4 versements de x,xx \$, ou à x,xx \$/mois. |
| **Payez dans le temps** Payez en 4 versements de x,xx \$ ou aussi peu que x,xx \$/mois. |  |
| ***Payez plus tard*** *Payez en 30 jours.* |  |

#### Payment Button approaches

| **EN-CA**     | **FR-CA**            |
|---------------|----------------------|
| Without badge | Continue with Klarna |
| With badge    | Continue with        |

### **Mexico**

| **Payment Category** | **EN-MX**       | **ES-MX**       |
|----------------------|-----------------|-----------------|
| `pay_over_time`      | Pay with Klarna | Paga con Klarna |
| `pay_later`          | Pay later       | Paga después    |
| `klarna`             | Pay with Klarna | Paga con Klarna |

#### Payment Descriptors Approaches

| **Two options approach** | **Single option approach** |
|----|----|
| **Paga con Klarna** Paga en 4 cuotas de \$x.xx. | NA |
| **Paga después** Paga en 30 días. | NA |

#### Payment Button approaches

| **ES-MX**     |
|---------------|
| Without badge |
| With badge    |

### **United States**

| **Payment Category** | **EN-US**         | **ES-US**       |
|----------------------|-------------------|-----------------|
| `pay_now`            | Pay in full today | Paga ahora      |
| `pay_later`          | Pay later         | Paga después    |
| `pay_over_time`      | Pay over time     | Paga a plazos   |
| `klarna`             | Pay with Klarna   | Paga con Klarna |

#### Payment Descriptors Approaches

- **English**

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Pay with Klarna** Pay now, in 30 days, in 4 payments of \$x.xx, or as low as \$x.xx/month. |
| **Pay later** Pay in 30 days. |  |
| **Pay over time** Pay in 4 payments of \$x.xx, or pay as low as \$x.xx/month. |  |

- **Spanish**

| **Three options approach** | **Single option approach** |
|----|----|
| **Paga ahora** Paga el total hoy. | **Paga con Klarna** Paga el total hoy, en 30 días, en 4 pagos de \$x.xx, o desde \$x.xx al mes. |
| **Paga después** Paga en 30 días. |  |
| **Paga a plazos** Paga en 4 pagos de \$x.xx, o desde \$x.xx al mes. |  |

#### Payment Button approaches

| **EN-US**     | **ES-US**            |
|---------------|----------------------|
| Without badge | Continue with Klarna |
| With badge    | Continue with        |

## Asia and Oceania

### **Australia**

| **Payment Category** | **EN-AU**                     |
|----------------------|-------------------------------|
| `pay_now`            | Pay in full today             |
| `pay_later`          | Pay later                     |
| `pay_over_time`      | Pay in 4                      |
| `klarna`             | Flexible payments with Klarna |

#### Payment Descriptors Approaches

| **Three options approach** | **Single option approach** |
|----|----|
| **Pay in full today** No fees, no interest. | **Flexible payments with Klarna** Pay now, in 4 payments of \$x.xx or in 30 days. |
| **Pay later** Pay in 30 days. |  |
| **Pay in 4** Pay in 4 payments of \$x.xx. |  |

#### Payment Button approaches

| **EN-AU**     |
|---------------|
| Without badge |
| With badge    |

### **New Zealand**

| **Payment Category** | **EN-NZ**       |
|----------------------|-----------------|
| `pay_over_time`      | Pay with Klarna |
| `pay_later`          | Pay later       |
| `klarna`             | Pay with Klarna |

#### Payment Descriptors Approaches

| **Two options approach** | **Single option approach** |
|----|----|
| **Pay with Klarna** Pay in 4 payments of \$x.xx. | NA |
| **Pay later** Pay in 30 days. | NA |

#### Payment Button approaches

| **EN-NZ**     |
|---------------|
| Without badge |
| With badge    |