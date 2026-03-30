# Source: https://docs.aws.amazon.com/contact-lens/latest/APIReference/llms.txt

# Amazon Connect Contact Lens API Reference

> Amazon Connect Contact Lens enables you to analyze conversations between customer and agents, by using speech transcription, natural language processing, and intelligent search capabilities. It performs sentiment analysis, detects issues, and enables you to automatically categorize contacts.

- [Welcome](https://docs.aws.amazon.com/contact-lens/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/contact-lens/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/contact-lens/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/contact-lens/latest/APIReference/API_Operations.html)

- [ListRealtimeContactAnalysisSegments](https://docs.aws.amazon.com/contact-lens/latest/APIReference/API_ListRealtimeContactAnalysisSegments.html): Provides a list of analysis segments for a real-time analysis session for voice.


## [Data Types](https://docs.aws.amazon.com/contact-lens/latest/APIReference/API_Types.html)

- [Categories](https://docs.aws.amazon.com/contact-lens/latest/APIReference/API_Categories.html): Provides the category rules that are used to automatically categorize contacts based on uttered keywords and phrases.
- [CategoryDetails](https://docs.aws.amazon.com/contact-lens/latest/APIReference/API_CategoryDetails.html): Provides information about the category rule that was matched.
- [CharacterOffsets](https://docs.aws.amazon.com/contact-lens/latest/APIReference/API_CharacterOffsets.html): For characters that were detected as issues, where they occur in the transcript.
- [IssueDetected](https://docs.aws.amazon.com/contact-lens/latest/APIReference/API_IssueDetected.html): Potential issues that are detected based on an artificial intelligence analysis of each turn in the conversation.
- [PointOfInterest](https://docs.aws.amazon.com/contact-lens/latest/APIReference/API_PointOfInterest.html): The section of the contact audio where that category rule was detected.
- [PostContactSummary](https://docs.aws.amazon.com/contact-lens/latest/APIReference/API_PostContactSummary.html): Information about the post-contact summary.
- [RealtimeContactAnalysisSegment](https://docs.aws.amazon.com/contact-lens/latest/APIReference/API_RealtimeContactAnalysisSegment.html): An analyzed segment for a real-time analysis session.
- [Transcript](https://docs.aws.amazon.com/contact-lens/latest/APIReference/API_Transcript.html): A list of messages in the session.
