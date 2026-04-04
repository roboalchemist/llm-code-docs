# Greenify | Localized community-driven greenification/plantation solution with AI

Source: https://docs.perplexity.ai/docs/cookbook/showcase/greenify

A mobile application that analyzes photos and location data to suggest suitable plants and build sustainable communities using Perplexity Sonar API

**Greenify** is a mobile application designed to encourage sustainable practices by analyzing live images and building communities. Users capture photos of their space (balcony, roadside, basement, etc.) and Greenify automatically analyzes the image using Perplexity's Sonar API to suggest suitable plants for that location. The app also connects like-minded people in the locality to create communities for sustainable, economic, and social growth.

<iframe title="YouTube video player" />

## Features

* **AI-Powered Plant Analysis** using image recognition and location data to suggest suitable plants
* **Location-Based Recommendations** considering weather, sunlight, and environmental conditions
* **Community Building** connecting users with similar plant interests and sustainable goals
* **Cross-Platform Mobile App** built with Expo for iOS, Android, and web
* **Real-time Weather Integration** for accurate plant suitability assessment
* **Structured JSON Output** using Pydantic models for consistent data handling
* **AR Model Support** for enhanced plant visualization

## Abstract Data Flow Diagram

![Abstract Data Flow Diagram](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/003/418/290/datas/gallery.jpg)

## Prerequisites

* Node.js 20.19.4+ and npm
* Python 3.10.0+ and pip
* Expo CLI and SDK 51+
* Perplexity API key (Sonar Pro and Sonar Deep Research)
* Android SDK/Studio or Xcode (for local builds)
* Mobile device with camera for image capture

## Installation

```bash theme={null}
