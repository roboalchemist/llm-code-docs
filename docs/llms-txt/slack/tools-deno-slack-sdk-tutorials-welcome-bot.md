Source: https://docs.slack.dev/tools/deno-slack-sdk/tutorials/welcome-bot

# Welcome bot

Workflow apps require a paid plan

Join the [Developer Program](https://api.slack.com/developer-program) and provision a sandbox with access to all Slack features for free.

![Bot avatar](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAWAAAAFgCAMAAACyv1N+AAAAb1BMVEUAAAAqERA8Ghl6imcEAgINBwcWDg37iYk2xfB7jGhSJCN/OjloLy4dHhyoT06URUQtMCs9QTlMUEdbYFW9W1nmd3ZnbWDab26ampdxgGLOZmXwf36qqqd/f332hIR0dHJSx+pxxt2NjYugub2NwM2ZSazLAAAACXBIWXMAAAsTAAALEwEAmpwYAAAdA0lEQVR42u2daXejurKGSyAmTyHtjN39/3/Zvrs7+yRpx5hZw/3QGSgBNrYROLG01l7rpE9i8EPxqqpUKhEfzNA5LIPAADaAzTCADWAD2AwD2AA2gM0wgA1gMwxgA9gANsMANoANYDMMYAPYADbDADaAzTCADWAD2AwD2AA2gM0wgA1gMwxgA9gANsMANoANYDMMYAPYADbDADaAzTCADWAD2AwD2AA2gM0wgA1gMwxgA9gANsMANoANYDMMYAPYADbDADaAzTCADWAD2AwD2AA2gM3oddCRr39fsglPOUgASQCIHQin8PjvLwOYjNbD/YfkkeCQA0gA+XY7f//zbGLN8tk/BvCBZpt6a5aDlMAaXyEGQAkQmJBFHvwygPcbV0XJcikZUAC2VboYUEI827X83wZwt3FnrcpcSraVLcbMKAGfLuj/GcA7x/dVmUlGu7FVIJOJ6z4awNuUIS0yCbAn3YpgEDK5+IR2PAzgOx7FB9Ot+JPW9FL8NoBrTkOcZvIoum+QGSW+GzwawMjfXUUC+sD7rhWzy38N4He8fzaiL7ofjGdz+7cBDAA//0Q94/2LmNEgmP46e8D38aozXvoew3X97SBY/HPegG+fU0bZLlIECEAJ5O/PEpy/qQnWgfGnsGJtgMNssx0vJQTKwJJUzsrg4d1dZrwgjCTSASnZTsTfyO/zBPzzeb0tZKOEMJ/Ywar9E5YxkxndDpkymIf/O0fA1w9FO16HlAEJoi6fMy/LrZApMAi//XtugK/iqFUdHMImVviwx6d5XKa0lTEFBt8u/++sAN/+ajNfapVTKz9AzzdbGFNg8+t/zwfwj+eoxdtyWODMDg1zw41MadkaQV8sfp0J4OuHgrbgPch4q1ohEipYixGHsxPNUNi9rnrei6eyka8D/mXCj/twLm4lIUTU/x8haJLdJF/fgq82q0b1dXgQ9mRgHmtWCsrot8nvL27B1//FlIkm673e9GVeXIZQOvWLCLBSebf+yoDv5WMJ9W9OZbBI+3x7C3HDGxFbiQiTrwv4Klo34p0s0rzne07FUjQgFjSRdxF8UQ0O46hhdnMcmuu57+U6tlldiJ3vD1/Tgq8f07r9Uulzrum+UxFCSYUqxCIJ868IePHYMLO7zkWm8c4LMSH1hyryefnlAN+LlxKazLfQe+9cOnVVEuVpEe6hfPXnai3r6usumf67Z3OrbiAv069lwVerTT24INrN99WIL0GqQnxaNnw04DBZCVHLDQz2FXNRlwnBTojwsYC/r+rRk+MvBnT4xbSUJ0z4SMDf/xc1uNZsUFeJhXWZYCfjrR0H+Pq5ztca3HqKuagRLm6TLwD4+iFVfX3qX8aDf4lcejXCpxI1HwO4Ibnu+MunMb6GcJSYg2bsW/LJATfwdV0Wj/M9hEO4EjWT682nBtzAl8yK0b6ICCTOewguy88MuIGvNR9z6mY1wuw+/ryAr1dpje/IolcnLBbZZwX8/TlSM1mTy7EXbJg60wl7fBk+DHC4qvlAk+nL6NYiHOytCQ7lpwR8lajGSv3LPz3d0RWdUc/z5s58f8URHs6LCDq6N3zIktGPp1WN77celmqWMSMie9u3TAB8S26twGwyGPxU6Dz89eks+O4lEr3zDYHkkeAsl2+ZGymlZIJHwndn3eeqeSaxSNj5pwMsI6byLY/zhxZEvoiSA1cSn0IIDlLwyPUmHTnlE+xKiLF9m/0B3z6VNb5H3cJcrgUTXLQKKwfJY9/ptn7K1YnOKj8X4HCd1vQhPgrvi+TtdN+jMpG5Lu820RX4T39Enwnwj2iNE2jUXR6hv1flixCiEzeQmd8pcJhhC+BwtflEgHmk8PAvj9gk4T8JLrr+sgAZTTuspOZTfIt8mnyeVeVbdYKbXB5RNums9xPIUqbO1e5fyzz8V5v7TwM4/KUAsaaH872yc7nv0n6R/1nu/q2AoB837LNIxM91jAWYLA+fQBbr4oAvLmQUFrtFAgnPqCmJvQDzyEJM3CPUbREXBxmWsJObdHfaB9WtiUnyKQB//x8ur3bcw13M25c2vtR6H6KZcHS5M+pw0WYOTpebTwD4x7MS5/tHaFvRxJeKv+Hb23j7J5Uw7PQ8OEUmzJ3sE3T++7PBKXb3omGCmxfgdtBlPy0b9sUyoJZnEyB/m9XxXDAGUKs7Zvkkq5V/A6C00IQVqCIQTj+bdv0b32XDBOeJ2JEE2MTfwTj8X4MN0sC2qP0fuG9GfgOFFDxtMHXrGuXY/DJ1JClJdauNg0RhvF1enSXixxOeWpxZUovK8lJwwbnNCnf7S1yPjSmdB8EfWWS2/X5rWVYyvnA8Udu6ZVdDiXnMueCCgy1ePgIRByV92EV86oDFBs051FedpeVvXorXJBjhbNtE5G1UYu5suhIZ53Y9aij5BRUET3iCLd9Fwl/Zr9WdQlD+/mSxCgtrrHi5K2DVg4CFAnD5qzL3CIskWwhbSrhNF9Ok4DbYduN8yNkFLZW/eP8EP60kOQX5IIwdCcfKThrw/R8sCERdz7n9164+AWERIds+bPkHp8WcxZpD4bbeIhScTdFuD8qc10/3IiX9y9+2H3FWvQHh5ycN2HrBAhGUtR0TTMmVgyNaUwrYnZ6ndtFsvG83WdhsRotq3oe9RhuZreboif+KvFqvRpk7UjRndaxiZ9hDUxMCXlFzhMpk3vJpuOKGztOi3Xxfr1dA4qDfsf9OWrS+l0u8gZzxasPcOIXTBXwXF8jQCVVTwA07aMHO2rr5IL6zFwB3Z2RWKFsvGAcAWCQNDq796nmupvgVO2HAPEK7MJzaApnHGpxVFjcnvlL0sCzX3c0XwC1cC/1acgsASYPAMfnmhNtONaAq708W8P0K43OW9RxXY5T40rL7qvq9p53LXd1JNe6kCQCkTddl1GvSCFaeLOA42iEQkDTevGyWPSKrMCy3663+R6rvkSgBPNqYDXmb3B4n6MUhpwr4aoUEgk5rDo/X7IowGTb/e/X6dlf7BZc4igjzZk9QJg0aASw5VcAJnuFEsPWlR1qSNa+tVRTCszvn35S8iQCQsuXBvq4ruax6Kf7zNAF/f0Ym587rRZRtL1/jitBthqMI6Fy0jcUkvYK24Mx5nebWQfW1STYnCfjuGaU0qZs1reO05eqanAhFWbvf63/I2h151dr7jrxPF9VXwDlJwBwrMN+nWFCKxv5IXYy/0YIRL7HJ257r+7/b6Oslpwj4LkIG7EyaMr175VEKufXN3yYQllULNWDrNDpHIizuTxCwXCFXiE+OvmKBQBB3nz9EBQ9kt3hjR20UT3gH4PtnbEXzxm0C/j6fTg6XQrfNG1Ev8f7SSVp5mBk7PcC4Ew+l2V4fQrYrJADQ/bx/GwtT6x9/iHD1V0rv5AD/VOroWnKbkuz6oi1hBuzH9z+CP9xvy7XO3v5HgK62OTnAf7ABT/O2fsstFmzvok7s/SQCTbhgtVyXvec3VgGa5e5ODPAPnEXjbb/cVoFdhn3eqgtACNJguxkw9Vu+n6QnBniFguRWA4ZV0HjnNHjYJczefv4HAgyk5cFWp1E5dixn7WHAi/Zpu9GULGdnrgfsw2+dsZYHyyreBq3eQ+GdFmBswM6WzG3IGhui7sr1AIU9UhEAYGNHGGjT7dPputq2uHq16O6UAP/EzRL5dJtD32CsJNhthPZxd5/TBhNGb5pHRq4U3gJ4jWzL2bojcFn34Chv/Da3x9wtXnsWALQeL+M3rRrLMSiKEwJ8j9fOtgfJD3OrxnfWnDzqtQAknzq1635rrUugkP44HcACTXFOsH0vfeYo39Rq2TqIbYj8d8S9ZwBQOsqrw5VNp1O0MBexkwF8h7MQO7M8zHNxZ1CmoZfjf3W5uXTxguFcSfc9TdGk+vzjVABz1HBjlwEDQOl85FioFQxhKhwAHq98t1KBVm+6Ul2YYxBFpwIYv0wtgqp06nxdlnSIf6ep1A4nIwoAgIcymLgUAKhrufd1XZpxdaUJTqHCPXxECux1aSqQw5x7Aix5EbW7zLY8rL5+S24+A5+7AJbtrxrKrB+DvGorkXMaFpyjL88WHSd1VnJesqhjvv2AsxJp483njHNeZs1WMMOJ4+j7KQD+ESMDnurqNkc6rxgdPnBATcth57kWwCv01Jml7fruAN8RmTCD1Wp8wHdFtZqPBifWeH5vE3bGEwmrzUfbnRWDo9c8hxoT5EjQYkiRaJ7How5ZsXHGQe71ep4WSCSskS34Ck1xHbJiI4lu55rqTLGj6HpcwAlarOS9LvyM0z5UWTUsV1djAr4vkY82eTwZC1YyRd0/K1cS1lF8NyJghhbrma/3DvYyaQkHrjeFGDCNkhEBb/DKZXQyeNWxRzemRywSjK3C0QDjKc5ydEYWcr8/voFOFVtdRELEP8cCjDc8sQudCbEBhyISLHoeDTCgetWH/nO4Pf31ft6sIhJAo9txAIdIIXRPcQM+HUUkWPkrHAUwOrim/ymuxw2Xcu8O2TjeKLL7MQCjPA8hetNn8mY/Cz4u6xQqPRFW6xEAhyisZLO+L/jYm+bQvUv5nuYuzmusr4cHXGCFWJ2QqLp4YxyRe18uc52hQ2YV8B0Kk4mj/4quTtlVx4Ua0MVDA84ylKicgd4Mac73CvrQzkZywM2pAR2NpgMDxpusphqaYR1hhPjmSnKQr6bIcBQOC7is+hCWDZprGyQ/PFImBz19hiuBWBHfDwk4zKu1cuWF7jWU/cwZN0Y60B0JFF8tfRkSMD4ec6rjHHO0JYnJg32OQ5e61zOiiMT1gIB5dRohWhQCn34ji30ylnkfYl4LmR9+DAb4B0pDa/EhoGpA9Ag3mNLDD5WiuMnd82CAGY4yHrUb8B6xcqH0AyOHuyMh1hrY3A4FOJKgN8oAgLWvyGrnSCOU+Pi4g2/haeEqebUfwwC+Q06arkylVd2gnR+cgSRHRPFKyKxTJBDgDDlpRFMeAtnhPo4w8tLgqMf/DW3aYbC5HgRwtTUM7bfepK1GQcoDk5X0qOqcB1yWzcrVzyEAlxUnjWly0mqOcNHdiRA97RGt+2o0fR4A8D1qkFjqKqmclVU/TXZ2Igqc6pHHHgBKB8lJVAGnSIIDbW3jUSTFO/tpN9iJOHbfsbKHUWb6AaPuXETb8np1TWMfNwLPccGxyz1YJBjEt9oBl1JbTWWbnwZQ8MMW5KweTglGIlE+/9QM+A5LsL6KKdzNTBSHzHFUHn8fWCRo+kczYDaMBOOIt+ssV5vj7L43OjMWXekFbCMvWGOFU7XFAKPJzUFzXB8GgMMNKhK9gKNBvGA1G8E6SoQ6x/URZuIeAQw2oVbA6ByBUudSFW4ELLtJMN4p0s8uiwznPEWuE/A9r+ZayQMMU9BPO81yBRQoV0l7esFQ4pKxONQIOEWPb6KRL1TPSWPQTYSxBPdVtfyEnGGqwYStSoctOowEA6z8/f20qgRTYH0ZQMioXhP+ALyRTHuyvVmEOxDGEsygt6rlxwk5wCk/CDAKlMuJ3gN+kAizmy41J2XPYcZ7G2IUz21+6AKM4ji9cxyAh0Q427myXKgS3GMYNCfoya10AbZRbYheA4Y16ptail3rci4USa+ptKqrVjVhVhb3mgDH1UAZJGg+6RJrRLhnO/he90ZiE86ZJsBo2tHrRCh9fRlkOxUixKfv9Xp72ITFRhNgtD9ZY67yNSxHFyjFfnEy69fHQSe1M3alB7Csemml9qYg2A/coRFqnNzzzpwJOkkoK/QAFuzgzurHagRAWuzlpPV8e+spPWQVdj/Ad9BbzcH+GkEZL7Y7aQxAY1Gij8/nuNIBmKJIdICOIAQ15EuW2500pBC87z7LUTVe7lkjrMbDXKR+wBfIKItyW6xR4KPTJ71vb6tOc0yWOgBX14sYGaCZ/BNuD85Ct2sY59haS2qBsZ8aADtDWzA4SIfSvNWEXSjQZivW/8agVTXxTnOhAbA1qBsMADBDzhEr24/+VRQieNLddPRFA+AUHys5AGDU951BFraYsOpDaPEhL6qr66UOC0anRpaPAwBG6xpAS95iwjUfQsfr9cRQ0vJn/4Dl8E1Jouo0x2jcbMJFTSG0VMSgI4X7PPTIajh+c6gDafA0V7YFGwMoBIBNWMUT9jQ3phuoy0nGFBN2iyaFyPUrBMAUecIbrRIx3IlKAQpRW1R4EIWAp1JTW5YB22TCjhN6WlR4iTKVjq7VWDQhSM2Ah6L+iBr7NplwUetDONVW6l8h3OMZ11ZTMg1GauwbX9RNGK9lgLZm5xIFAtnXkAhYKyZcqvOcGiY79jCNlNkXAYwXEwDSbIcTzLX1fEd7n/LJVwG8Vna+x3Nkwi4s8Tw40daIa7ZlQ/UnBqzsy6aiqJZI1KY4S9/tcqJnxWFswIojweIJmueUKY7qOw5BaErXvgL+PRphXBsGZVGZ52pTnM4kCVKFVK8FiyEJK0f9Vea5Agpe7ntk1eGZERR26AQ88Jl2Shk/iydvJuzCMsFT3Ao+3bBGbptc3zcv3kSigKJEXjG3Bmr9wnR8LtUSx3QZudJQ8q35oOqjgdYTf9CKAxFaLZjJYU0YV/mw8q9I1Hw01xmuW7+jWSJuBwW8XuDvUxShW4ALYYkXcrSe3IXaI3hJ74Dtai2Ekw5rwpnSZyvNwAWAHK3E0mCt95AkqmXV12o6QVvKoVMSFj7kIg5qNcG6ljI+1iGZVolwNIXi3UbkYBsuyrkLBT4wZar3PFkkCvav3gEXXnUnCBs+nsM/p0VRcKTAXG9Qfys1le9a7+ucbNTDRGZKC8J4EW7QLWk+lTGpPkxiaSj+s6t6LwYHnCuLbXKDD3Z2NZ/Wm8oKYTLpH/Bv0noc1yhJH4aDOKCagx/0znqlhkgOlaw6i+EJf9v2Xuo2YEiwHmkAPK8SliMcQ6t6EqC/0+7HCCkqlPulY6dnNaMvOYwgEu1W6gSayxGzauFNr7UXHxJR2T/MQI4AGKa8zYS55q29wGW1wH+mA/D/2Xoy+nudzmu1GfB6SAn2LC1p0KoGM2c+BuG8RYa1G/AChVb2P1oAOxXCVKbjLNA54xgw2ghPLT2JfGvUdM+7DI9hwEiCqTXVAzioznIsvYVxZNgdwYBxYZrXq3HZ749u47FKhOxwPgph7oClBuoX2r3yvHJN0W/1kAUtIixgpDoJT8l2u/oNeOkwXRJcBVwVYQbxSIChFHhtgS21XzJGXTupLsA+alVEvbEIX/Oqz2TNH2DIOa7XXCUG/Nuhp6ARsKpOdJQOUEMgKnMc82ba6i1CC62LLcYinFcKAi1ngAuiZ9hrmIEBSw+llJKxAFcOahnEgFEc1/MchwD/QoHqSMEcbq/O6SARur45Dhf/hahAi4546vqVeK2FGCIxjWpOyEwj4H+R5yDK8QA/3JHBDFipMyl0HnfmOqjZ64gm/DR3Aeh0kJUVhuIcXyfgADf2jcYDDHngAB/mCZPDDyvfF/AjXtm16YiEM8+dDvSE5XCHpl6in2USjki4HGptWxKNLc0UI42CakpNjBjPAYAYyFG0+EeljcWnsdaTwdHqPbBixHlusGFXI2X5fKXTgiFBWWEguf31AYdpZWITgt9FGgHDLLOQSDjiywNOmV39ysVmfpHo28blYqelTOZf34SVNb/y6WVxpc2Ck6BAazZUyC8PWF0fo1ksg2mmoU3CXxPGx14Rl311wDnFuxUY0AjcWWj9o8GCIUhxebBgYfHVCbtc2RkngJbphi2DpH/AV2slyXMGIsFdJur7tUX2Iv3ri+PWXEnd0XVUL8X5+iJx+0+Ts0QZgDN1Lf93nxYMLlMqEwSb8C8OOL6JZdNaHRUiiwkLL6MeATuFukeDki8vEmkj4b8gijTh3jTc9GbBuQpYgPvlw410KdsTLyJLC7EMo54suAYYhLJh+yuO7KYgW5SQZ/FBZtwNMJB8mX11wrHw7W0b2ESWkvJyXzVuAEyL+mWEzb9+QAf8RpT2NjEsspR5+4V4HQGDgDPI+kDMLiXfilhkpfTDi80xgEnWdIUz8NUAAHJxaZd0K+IizfhknhwM+K7lYCF6BjIMAJCzW2lvn9J5VkBXpagDvnhu7lhzHjIMAJAwGRJOdymFd9lFKeqA7aRlKj0Hb/ij7falZW/z2kAUWcYnV9H+gOebNl/lHLzhilLIxQ4z5lnBvF2LH3XAJGt1BnlxFhPdhxnfSmfrjCeykvvX0X6AG72094nuJj0jwpAwccM4FQBtmEVRFt7lYrNHuhJlK6nSBY+6l49wbsMTsc2AtsujO7mwfnW14J9VJ8Jx7VItthdnB5iLpeBb+ALPEj65XncDbFWdCJtexhK9HUK650cYMmH7zraGiyIr8qBxvqsBvogqgKm3nhRK9l06Z0gYgIsrxqnYIsaM+w2Ia4BlNZdmhymfCoUwOSNnrTpS8V3YpNziGZfcr8V3NcB21YkQBQBzFcK8mJ4nYYiZXFhb/DYhcunNsq2A7+JKqof6EgCEoz6183KH1RBPtiuFEKLIJgixWjpl5/VNj9PaL0UenO1YMyeYuKylfyhjInoOwnbAuFHE3x/W35ROgOysCQPkfDFrbY74F/H3NomYICfC/SsFxVRpQyVo/vXLfXYpBWtTCmHJInoTChUwciJEmL23elFcCTs5Xx1+zcx/FyWFFim25JsWq4CrmQj60eZWOMqatkWyMycMMbN9ApZosmIhBPmLuA74wwWzKs1VhIedNSHo2RMG4NK3QYpWocgmoQL4Lq64GJZdmfGuc8WGDeHXAI+XlmWJFqFILDUfCS2tKR4uXcXYmYx8MOOpvPJ4m0MBQrFgN65kNGy0gJ1cxLb6oM40L1Gf7wrmWKJ5utt2zA6Gv7oTqnddFNTwBYAH5rqiuWuhtWU7iFpT+XRXe0hl7hi8r57spBGxtc+23advQv0IltkLQxcAALJGxNaWQ9Wg1oUvqhOG4skzcNsR77n1OfomqHp+qzDOxBbE++4tj76pOsyoTIwQtyK2up9Q1aYSDMrMXhq0zYgt2PeYr+i6rsOQ/DIy0YzY2tpepXGslrVDFxiViXNlyDYgViI5O5XVRfvmEDC/adgmI0RkUhNoUeJv1dVBDVQeuOc01QbQWwO2gvinSxzVgn1kwU7r6rFwiFqGIWgpX4wRQ3VXzaUsrS2b77dFdSyoNY1jwETqmLiuMtblzcE9lrJ5gzMB5ebRuBPII1AAe92PsM6vG09wkrFtQuf2hhz7nNS3Ao8UTVlmx/MjQ7Y50OB7nYpdBo3NYMvN2jGRXTNg6e1lz9m8+aC3YvPLIG4sPNnYlZfeomL35tOypZtmsfGnheFbW7Z3q6vKluzg6wVt23uL1HeMW1yri6hsEUDL9u0e8U3ZtqGskNSb5AYwoHYnH6ujVml3O9DVadtAzUsRe+dtxtuyaUx2zC2wO9dtPdclzmw6B+MHvwFGS8ldX+8nCJjV5uAVBU0CEkRGIgAAvlXLV93u/bbZUm7ZvQCljF3bmebGgu1DA7sVzBkrtjSiT6i1mUjbW5834KIqEXKvzS45BMwutzb731Br41u2DFZnC9hHsTLZ78OyZcIttuNEhQQctvEtSeVZCEZtr3J1q/LbFoI9RrhJ7E52TwkLaH5+kxxU22R2dITxptMbxmiHmkshoDyHDXdW/R8qZ2TLA9Ynnti9Z3UrupTr+flZcFDtx+ESftCe06XgtFPlsCXOzoLRYVTywCh3xe4nE7e5wzYacQhn5kVgP21fN+JjPAL4bmKXO0SWpmdnwbR6LOJRB8Hk5fVksuP8O0ng3DR4U+3PLNjtMU3MMyZD6WxzKtqKh76wBeN/cY5N0USML712O2bzs7NgCOOKG2H10L69EPIGHNaUFqbBBs7OgqWG4+uesvLen04sdaudG56fHwwXxZ7Lct1GwoW8Fa5DmftW1Ub9+fP55SIA/E0l4UOu+k4vLnLCSCIBAufi4cvzhf8H4wFZuBJAi84AAAAASUVORK5CYII=)

Welcome Bot

Welcome to the Welcome Bot tutorial! We hope you enjoy your stay here!

What a nice message to read! It sure would be nice if everyone joining a Slack channel received such a message!

In this tutorial you'll learn how to create a Slack app that sends a friendly welcome message, similar to the one at the top of this page, to a user when they join a channel. A user in the channel will be able to create the custom message from a form.

Before we begin, ensure you have the following prerequisites completed:

* Install the [Slack CLI](/tools/deno-slack-sdk/guides/getting-started).
* Run `slack auth list` and ensure your workspace is listed.
* If your workspace is not listed, address any issues by following along with the [Getting started](/tools/deno-slack-sdk/guides/getting-started), then come on back.

## Create a blank project {#create-a-blank-project}

Create a blank app with the Slack CLI using the following command:

```text
slack create welcome-bot-app --template https://github.com/slack-samples/deno-blank-template
```

A new app folder will be created. Once you have your new project ready to go, change into your project directory. You'll be bouncing between a few folders, so we recommend using an editor that streamlines switching between files.

Welcome to your Slack app! There may not be a welcoming message, but do not fret, you can make yourself at home here. Slack apps are built around their flexibility; don't be afraid to run wild!

For now though, just make three folders within your app folder. Each folder will contain a fundamental building block of a Slack app:

* `functions`
* `workflows`
* `triggers`

With the setup complete, you can get building!

## Alternatively, create an app from the template {#alternatively-create-an-app-from-the-template}

If you want to follow along without placing the code yourself, use the pre-built [Welcome Bot app](https://github.com/slack-samples/deno-welcome-bot):

```text
slack create welcome-bot-app --template https://github.com/slack-samples/deno-welcome-bot
```

Once you have your new project ready to go, change into your project directory.

## Create the app manifest {#create-the-app-manifest}

The app manifest provides a sneak peak at what you'll be building throughout the rest of this tutorial. The recipe for the Welcome Bot app calls for:

* two workflows, imported from their files:
  * `MessageSetupWorkflow`
  * `SendWelcomeMessageWorkflow`
* one datastore imported from its file:
  * `WelcomeMessageDatastore`
* and six scopes:
  * [`chat:write`](https://docs.slack.dev/reference/scopes/chat.write)
  * [`chat:write.public`](https://docs.slack.dev/reference/scopes/chat.write.public)
  * [`datastore:read`](https://docs.slack.dev/reference/scopes/datastore.read)
  * [`datastore:write`](https://docs.slack.dev/reference/scopes/datastore.write)
  * [`channels:read`](https://docs.slack.dev/reference/scopes/channels.read)
  * [`triggers:write`](https://docs.slack.dev/reference/scopes/triggers.write)
  * [`triggers:read`](https://docs.slack.dev/reference/scopes/triggers.read)

Put that all together and your `manifest.ts` file will look like:

```python
// /manifest.tsimport { Manifest } from "deno-slack-sdk/mod.ts";import { WelcomeMessageDatastore } from "./datastores/messages.ts";import { MessageSetupWorkflow } from "./workflows/create_welcome_message.ts";import { SendWelcomeMessageWorkflow } from "./workflows/send_welcome_message.ts";export default Manifest({  name: "Welcome Message Bot",  description:    "Quick way to setup automated welcome messages for channels in your workspace.",  icon: "assets/default_new_app_icon.png",  workflows: [MessageSetupWorkflow, SendWelcomeMessageWorkflow],  outgoingDomains: [],  datastores: [WelcomeMessageDatastore],  botScopes: [    "chat:write",    "chat:write.public",    "datastore:read",    "datastore:write",    "channels:read",    "triggers:write",    "triggers:read",  ],});
```

We've provided you all this upfront to streamline the tutorial, but you would likely build up your manifest as you add workflows and datastores to your app.

## Define a workflow for setting up the welcome message {#define-a-workflow-for-setting-up-the-welcome-message}

In this step we'll be creating a [workflow](/tools/deno-slack-sdk/guides/creating-workflows) named `MessageSetupWorkflow`. This workflow will contain the functions needed for someone in the channel to create a welcome message with a form.

Create a file named `create_welcome_message.ts` within the `workflows` folder. There you'll add the following workflow definition:

```python
// /workflows/create_welcome_message.tsimport { DefineWorkflow, Schema } from "deno-slack-sdk/mod.ts";import { WelcomeMessageSetupFunction } from "../functions/create_welcome_message.ts";/** * The MessageSetupWorkflow opens a form where the user creates a * welcome message. The trigger for this workflow is found in * `/triggers/welcome_message_trigger.ts` */export const MessageSetupWorkflow = DefineWorkflow({  callback_id: "message_setup_workflow",  title: "Create Welcome Message",  description: " Creates a message to welcome new users into the channel.",  input_parameters: {    properties: {      interactivity: {        type: Schema.slack.types.interactivity,      },      channel: {        type: Schema.slack.types.channel_id,      },    },    required: ["interactivity"],  },});
```

The `input_parameters` you need are `interactivity` and `channel`. The `interactivity` parameter enables interactive elements, like the form you'll set up next.

## Add a form for the user to specify the welcome message {#add-a-form-for-the-user-to-specify-the-welcome-message}

You add functions to workflows by using the `addStep` method. In this case, you'll be adding the form the user will interact with.

This is done using a [Slack function](/tools/deno-slack-sdk/guides/creating-slack-functions). Slack functions give you the ability to add common Slack functionality without the need to do so from scratch.

The Slack function to use here is the [`OpenForm`](/tools/deno-slack-sdk/reference/slack-functions/open_form) function. Add it to your `create_welcome_message.ts` workflow like so:

```text
// /workflows/create_welcome_message.ts/** * This step uses the OpenForm Slack function. The form has two * inputs -- a welcome message and a channel id for that message to * be posted in. */const SetupWorkflowForm = MessageSetupWorkflow.addStep(  Schema.slack.functions.OpenForm,  {    title: "Welcome Message Form",    submit_label: "Submit",    description: ":wave: Create a welcome message for a channel!",    interactivity: MessageSetupWorkflow.inputs.interactivity,    fields: {      required: ["channel", "messageInput"],      elements: [        {          name: "messageInput",          title: "Your welcome message",          type: Schema.types.string,          long: true,        },        {          name: "channel",          title: "Select a channel to post this message in",          type: Schema.slack.types.channel_id,          default: MessageSetupWorkflow.inputs.channel,        },      ],    },  },);
```

This creates a form that will show the following fields:

* "Your welcome message", where the user provides the message as a string of text
* "Select a channel to post this message in", where the user provides the channel for the desired channel.

The user can then submit the form.

## Add a confirmation ephemeral message when submitting the form {#add-a-confirmation-ephemeral-message-when-submitting-the-form}

When the user submits the form, they'll want confirmation that it is submitted.

You can do this by using the Slack [`SendEphemeralMessage`](/tools/deno-slack-sdk/reference/slack-functions/send_ephemeral_message) function. Add the following step to your `create_welcome_message.ts` workflow:

```text
// /workflows/create_welcome_message.ts/** * This step takes the form output and passes it along to a custom * function which sets the welcome message up. * See `/functions/setup_function.ts` for more information. */MessageSetupWorkflow.addStep(WelcomeMessageSetupFunction, {  message: SetupWorkflowForm.outputs.fields.messageInput,  channel: SetupWorkflowForm.outputs.fields.channel,  author: MessageSetupWorkflow.inputs.interactivity.interactor.id,});/** * This step uses the SendEphemeralMessage Slack function. * An ephemeral confirmation message will be sent to the user * creating the welcome message, after the user submits the above * form. */MessageSetupWorkflow.addStep(Schema.slack.functions.SendEphemeralMessage, {  channel_id: SetupWorkflowForm.outputs.fields.channel,  user_id: MessageSetupWorkflow.inputs.interactivity.interactor.id,  message:    `Your welcome message for this channel was successfully created! :white_check_mark:`,});export default MessageSetupWorkflow;
```

This function takes the provided `message` text and sends it to the specified user and channel, both pulled from the `OpenForm` function step above.

Wonderful! Now let's build functionality to handle that welcome message once its submitted by a user.

## Create a datastore to store the welcome message {#create-a-datastore-to-store-the-welcome-message}

The message data needs to be accessible at a later time (when a user joins the channel), so it needs to be stored somewhere, like a [datastore](/tools/deno-slack-sdk/guides/using-datastores).

Within your `datastores` folder, create a file named `messages.ts`. Within it, define the datastore:

```python
// /datastores/messages.tsimport { DefineDatastore, Schema } from "deno-slack-sdk/mod.ts";export const WelcomeMessageDatastore = DefineDatastore({  name: "messages",  primary_key: "id",  attributes: {    id: {      type: Schema.types.string,    },    channel: {      type: Schema.slack.types.channel_id,    },    message: {      type: Schema.types.string,    },    author: {      type: Schema.slack.types.user_id,    },  },});
```

Each `attribute` is a type of information you want to store. In this case, it's the information from the form submission. Next, you'll fill the datastore with that information.

## Create a custom function to send the message to the datastore {#create-a-custom-function-to-send-the-message-to-the-datastore}

Within your `functions` folder, create a file named `create_welcome_message.ts`. This is where you'll define this [custom function](/tools/deno-slack-sdk/guides/creating-custom-functions).

The custom function you'll add here will take the form input the user provided and store that information in the created datastore.

Add the function definition to the `create_welcome_message.ts` file:

```python
// /functions/create_welcome_message.tsimport { DefineFunction, Schema, SlackFunction } from "deno-slack-sdk/mod.ts";import { SlackAPIClient } from "deno-slack-sdk/types.ts";import { SendWelcomeMessageWorkflow } from "../workflows/send_welcome_message.ts";import { WelcomeMessageDatastore } from "../datastores/messages.ts";/** * This custom function will take the initial form input, store it * in the datastore and create an event trigger to listen for * user_joined_channel events in the specified channel. */export const WelcomeMessageSetupFunction = DefineFunction({  callback_id: "welcome_message_setup_function",  title: "Welcome Message Setup",  description: "Takes a welcome message and stores it in the datastore",  source_file: "functions/create_welcome_message.ts",  input_parameters: {    properties: {      message: {        type: Schema.types.string,        description: "The welcome message",      },      channel: {        type: Schema.slack.types.channel_id,        description: "Channel to post in",      },      author: {        type: Schema.slack.types.user_id,        description:          "The user ID of the person who created the welcome message",      },    },    required: ["message", "channel"],  },});
```

This function provides three `properties` as `input_parameters`. These are the three pieces of information you want to pass to the datastore: the welcome message, the channel to post in, and the user ID of the person who created the message.

## Add the custom function's functionality {#add-the-custom-functions-functionality}

The actual functionality involves taking those input parameters and putting them into a datastore. Put this right below your function definition within `create_welcome_message.ts`:

```javascript
// /functions/create_welcome_message.tsexport default SlackFunction(  WelcomeMessageSetupFunction,  async ({ inputs, client }) => {    const { channel, message, author } = inputs;    const uuid = crypto.randomUUID();    // Save information about the welcome message to the datastore    const putResponse = await client.apps.datastore.put<      typeof WelcomeMessageDatastore.definition    >({      datastore: WelcomeMessageDatastore.name,      item: { id: uuid, channel, message, author },    });    if (!putResponse.ok) {      return { error: `Failed to save welcome message: ${putResponse.error}` };    }    // Search for any existing triggers for the welcome workflow    const triggers = await findUserJoinedChannelTrigger(client, channel);    if (triggers.error) {      return { error: `Failed to lookup existing triggers: ${triggers.error}` };    }    // Create a new user_joined_channel trigger if none exist    if (!triggers.exists) {      const newTrigger = await saveUserJoinedChannelTrigger(client, channel);      if (!newTrigger.ok) {        return {          error: `Failed to create welcome trigger: ${newTrigger.error}`,        };      }    }    return { outputs: {} };  },);
```

## Add the custom function to the workflow {#add-the-custom-function-to-the-workflow}

Add the custom function you created as a step in the workflow. This connection allows you to use inputs and outputs from previous steps, which is how you'll get the specific pieces of information.

Pivot back to your `create_welcome_message.ts` workflow file. Add the following step:

```text
// /workflows/create_welcome_message.ts/** * This step takes the form output and passes it along to a custom * function which sets the welcome message up. * See `/functions/setup_function.ts` for more information. */MessageSetupWorkflow.addStep(WelcomeMessageSetupFunction, {  message: SetupWorkflowForm.outputs.fields.messageInput,  channel: SetupWorkflowForm.outputs.fields.channel,  author: MessageSetupWorkflow.inputs.interactivity.interactor.id,});export default MessageSetupWorkflow;
```

Now you've created a workflow that will:

* let a user fill out a form with information for a welcome message
* store the welcome message information in a datastore

## Create the link trigger {#create-the-link-trigger}

You need to create a [trigger](/tools/deno-slack-sdk/guides/using-triggers) that will start the workflow, which provides a user the form to fill out.

This app will use a specific type of trigger called a [link trigger](/tools/deno-slack-sdk/guides/creating-link-triggers). Link triggers kick off workflows when a user clicks on their link.

Within your triggers folder, create a file named `create_welcome_message_shortcut.ts`. Place this trigger definition within that file:

```python
// triggers/create_welcome_message_shortcut.tsimport { Trigger } from "deno-slack-api/types.ts";import MessageSetupWorkflow from "../workflows/create_welcome_message.ts";import { TriggerContextData, TriggerTypes } from "deno-slack-api/mod.ts";/** * This link trigger prompts the MessageSetupWorkflow workflow. */const welcomeMessageTrigger: Trigger<typeof MessageSetupWorkflow.definition> = {  type: TriggerTypes.Shortcut,  name: "Setup a Welcome Message",  description: "Creates an automated welcome message for a given channel.",  workflow: `#/workflows/${MessageSetupWorkflow.definition.callback_id}`,  inputs: {    interactivity: {      value: TriggerContextData.Shortcut.interactivity,    },    channel: {      value: TriggerContextData.Shortcut.channel_id,    },  },};export default welcomeMessageTrigger;
```

This defines a trigger that will kick off the provided workflow, `message_setup_workflow`, along with an added bonus: it'll pass along the channel ID of the channel it was started in.

## Create the event trigger to start a second workflow {#create-the-event-trigger-to-start-a-second-workflow}

The workflow to send a message to a user needs to be invoked _after_ the message is created in the workflow. It also needs to be invoked whenever a new user joins the channel.

This calls for using a different type of trigger: an [event trigger](/tools/deno-slack-sdk/guides/creating-event-triggers). Event triggers are only invoked when a certain event happens. In this case, our event is `user_joined_channel`.

Think of your `setup` function as priming everything needed for that message to send. The final piece to set up is this trigger.

Since it runs at a certain point in a workflow, you'll actually place it within a function file. Place it within the `/functions/create_welcome_message.ts` file:

```text
// /functions/create_welcome_message.ts/** * findUserJoinedChannelTrigger returns if the user_joined_channel trigger * exists for the "Send Welcome Message" workflow in a channel. */export async function findUserJoinedChannelTrigger(  client: SlackAPIClient,  channel: string,): Promise<{ error?: string; exists?: boolean }> {  // Collect all existing triggers created by the app  const allTriggers = await client.workflows.triggers.list({ is_owner: true });  if (!allTriggers.ok) {    return { error: allTriggers.error };  }  // Find user_joined_channel triggers for the "Send Welcome Message"  // workflow in the specified channel  const joinedTriggers = allTriggers.triggers.filter((trigger) => (    trigger.workflow.callback_id ===      SendWelcomeMessageWorkflow.definition.callback_id &&    trigger.event_type === "slack#/events/user_joined_channel" &&    trigger.channel_ids.includes(channel)  ));  // Return if any matching triggers were found  const exists = joinedTriggers.length > 0;  return { exists };}/** * saveUserJoinedChannelTrigger creates a new user_joined_channel trigger * for the "Send Welcome Message" workflow in a channel. */export async function saveUserJoinedChannelTrigger(  client: SlackAPIClient,  channel: string,): Promise<{ ok: boolean; error?: string }> {  const triggerResponse = await client.workflows.triggers.create<    typeof SendWelcomeMessageWorkflow.definition  >({    type: "event",    name: "User joined channel",    description: "Send a message when a user joins the channel",    workflow:      `#/workflows/${SendWelcomeMessageWorkflow.definition.callback_id}`,    event: {      event_type: "slack#/events/user_joined_channel",      channel_ids: [channel],    },    inputs: {      channel: { value: channel },      triggered_user: { value: "{{data.user_id}}" },    },  });  if (!triggerResponse.ok) {    return { ok: false, error: triggerResponse.error };  }  return { ok: true };}
```

This trigger passes the event-related `channel` and `triggered_user` values on to your soon-to-be workflow. With those accessible, you can now build out your next workflow.

## Create a workflow for sending the welcome message {#create-a-workflow-for-sending-the-welcome-message}

This second workflow will retrieve the message from the datastore and send it to the channel when a new user joins that channel.

Navigate back to your `workflows` folder, and create a new file `send_welcome_message.ts`.

Within that file place the workflow definition:

```python
// /workflows/send_welcome_message.tsimport { DefineWorkflow, Schema } from "deno-slack-sdk/mod.ts";import { SendWelcomeMessageFunction } from "../functions/send_welcome_message.ts";/** * The SendWelcomeMessageWorkFlow will retrieve the welcome message * from the datastore and send it to the specified channel, when * a new user joins the channel. */export const SendWelcomeMessageWorkflow = DefineWorkflow({  callback_id: "send_welcome_message",  title: "Send Welcome Message",  description:    "Posts an ephemeral welcome message when a new user joins a channel.",  input_parameters: {    properties: {      channel: {        type: Schema.slack.types.channel_id,      },      triggered_user: {        type: Schema.slack.types.user_id,      },    },    required: ["channel", "triggered_user"],  },});
```

This workflow will have two inputs: `channel` and `triggered_user`, both acquired from the trigger invocation.

## Create a custom function that sends the welcome message {#create-a-custom-function-that-sends-the-welcome-message}

Navigate to the `functions` folder, and create a new file called `send_welcome_message.ts`.

Within that file add the definition for a function that uses the inputs `channel` and `triggered_user`:

```python
// /functions/send_welcome_message.tsimport { DefineFunction, Schema, SlackFunction } from "deno-slack-sdk/mod.ts";import { WelcomeMessageDatastore } from "../datastores/messages.ts";/** * This custom function will pull the stored message from the datastore * and send it to the joining user as an ephemeral message in the * specified channel. */export const SendWelcomeMessageFunction = DefineFunction({  callback_id: "send_welcome_message_function",  title: "Sending the Welcome Message",  description: "Pull the welcome messages and sends it to the new user",  source_file: "functions/send_welcome_message.ts",  input_parameters: {    properties: {      channel: {        type: Schema.slack.types.channel_id,        description: "Channel where the event was triggered",      },      triggered_user: {        type: Schema.slack.types.user_id,        description: "User that triggered the event",      },    },    required: ["channel", "triggered_user"],  },});
```

## Add the custom function's functionality {#add-the-custom-functions-functionality-1}

With the function defined, add the actual functionality right after:

```javascript
// /functions/send_welcome_message.tsexport default SlackFunction(SendWelcomeMessageFunction, async (  { inputs, client },) => {  // Querying datastore for stored messages  const messages = await client.apps.datastore.query<    typeof WelcomeMessageDatastore.definition  >({    datastore: WelcomeMessageDatastore.name,    expression: "#channel = :mychannel",    expression_attributes: { "#channel": "channel" },    expression_values: { ":mychannel": inputs.channel },  });  if (!messages.ok) {    return { error: `Failed to gather welcome messages: ${messages.error}` };  }  // Send the stored messages ephemerally  for (const item of messages["items"]) {    const message = await client.chat.postEphemeral({      channel: item["channel"],      text: item["message"],      user: inputs.triggered_user,    });    if (!message.ok) {      return { error: `Failed to send welcome message: ${message.error}` };    }  }  return {    outputs: {},  };});
```

This creates a function that:

* queries the datastore for stored messages
* posts an ephemeral message using the `message` item from the datastore with a matching `channel` channel ID value to the user with the `triggered_user` user ID.

## Add the custom function to the workflow {#add-the-custom-function-to-the-workflow-1}

With the custom function built, add it to your `send_welcome_message.ts` workflow as a step:

```text
// /workflows/send_welcome_message.tsSendWelcomeMessageWorkflow.addStep(SendWelcomeMessageFunction, {  channel: SendWelcomeMessageWorkflow.inputs.channel,  triggered_user: SendWelcomeMessageWorkflow.inputs.triggered_user,});
```

And with that, you have created the two workflows that contain all the functionality you need to send a custom ephemeral message to a user joining a new channel.

## Run your Slack app {#run-your-slack-app}

For now, you'll want to [locally install the app](/tools/deno-slack-sdk/guides/developing-locally) to the workspace. From the command line, within your app's root folder, run the following command:

```text
slack run
```

Proceed through the prompts until you have a local server running in that terminal instance.

It's installed! You can't use it quite yet though.

## Invoke the link trigger {#invoke-the-link-trigger}

Within a terminal located within that folder, you'll need to create that initial link trigger. You can open a new terminal tab or cancel your running server and restart later if you'd like.

You can do that with the `slack trigger create` command. Make it so.

```python
slack trigger create --trigger-def triggers/create_welcome_message_shortcut.ts
```

Since you haven't installed this trigger to a workspace yet, you'll be prompted to install the trigger to a new workspace. Then select an authorized workspace in which to install the app.

When you select your workspace, you will be prompted to choose an app environment for the trigger. Choose the _Local_ option so you can interact with your app while developing locally. The CLI will then finish installing your trigger.

Once your app's trigger is finished being installed, you will see the following output:

```text
📚 App Manifest   Created app manifest for "welcomebot (local)" in "myworkspace" workspace⚠️  Outgoing domains   No allowed outgoing domains are configured   If your function makes network requests, you will need to allow the outgoing domains   Learn more about upcoming changes to outgoing domains: https://docs.slack.dev/changelog🏠 Workspace Install   Installed "welcomebot (local)" app to "myworkspace" workspace   Finished in 1.5s⚡ Trigger created   Trigger ID:   Ft0123ABC456   Trigger Type: shortcut   Trigger Name: Setup a Welcome Message   Shortcut URL: https://slack.com/shortcuts/Ft0123ABC456/XYZ123...
```

Copy the URL, paste, and post it in a channel to kick off the first workflow and create a message.

## Deploy your Slack app {#deploy-your-slack-app}

When you're ready to make the app accessible to others, you'll want to [deploy it](/tools/deno-slack-sdk/guides/deploying-to-slack) instead of running it:

```text
slack deploy
```

And then create the trigger again, but choosing the _Deployed_ option this time:

```python
slack trigger create --trigger-def triggers/create_welcome_message_shortcut.ts
```

Other than that, the steps are the same.

## Pause and reflect {#pause-and-reflect}

Congratulations! You've successfully built your friendly neighborhood welcome bot, providing a cozy presence to all who enter your desired channel.

### Next steps {#next-steps}

For your next challenge, perhaps consider creating [an app that creates an issue in GitHub](/tools/deno-slack-sdk/tutorials/github-issues-app)!
