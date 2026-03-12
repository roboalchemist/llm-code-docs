# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/calculator/troubleshooting-the-calculator-step/length-and-precision-calculator-pdi-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/calculator/troubleshooting-the-calculator-step/length-and-precision-calculator-pdi-step.md

# Length and precision

* **Question**

  I made a transformation using the A/B function and it rounded incorrectly. I entered integers in **Field A** and **Field B**, but my result type was a number, so I would expect the integers to be converted to numbers before executing the division.

  For example, when I execute `28/222`, the result is `0.0` instead of 0.1261 which is expected behavior. It seems the result type is ignored. If I change the values in **Field A** and **Field B** to numbers (`6, 4`) my result is `0.12612612612612611` which still ignores the result type (4 places after the comma).

  * **Suggested Solution**

    Length and Precision are metadata pieces. We convert to the required metadata type when we result the data to a location, not during the transformation.

    If you want to round to the specified precision, you should do this rounding in another step. However, rounding double point precision values is futile anyway. A floating point number is stored as an approximation, so 0.1261, your desired output, would probably be stored as `0.126099999999` or `0.1261000000001`.

    **Note:** This behavior is not true for the data type BigNumbers.

    So the calculation is rounded using BigDecimals once the numbers are stored in the output table, but not during the transformation.

    **Note:** This behavior is also true for the Text File Output step. If you would have specified Integer as the result type, the internal number format would have been retained. When you press **Get Fields**, the required Integer type would be filled in. Then the required conversion would occur at this point. See [Text File Output](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/text-file-output-cp) for details.
