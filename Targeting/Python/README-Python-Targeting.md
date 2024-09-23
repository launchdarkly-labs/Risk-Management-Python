# DJ Toggle's Top Tracks - Targeting Tutorial

## Overview
This project demonstrates how to use LaunchDarkly's targeting and segmentation features to serve different content to different user groups in a Python application.

## Why create segments? Why use Targeting?
Segments and targeting allow you to:
- Serve different content to specific user groups (e.g., DJ Toggle's team vs. general audience)
- Gradually roll out features to different user segments
- Personalize user experiences based on user attributes or group membership

## Setup and Usage
1. Install dependencies:
```pip install -r requirements.txt```
2. Set up your LaunchDarkly SDK key in a .env file:
```LD_SDK_KEY=your_sdk_key_here```

3. Create two segments in your LaunchDarkly dashboard:
- "DJ Toggle Team"
- "General Audience"
4. Set up two feature flags in LaunchDarkly:
- "use-database": Target "DJ Toggle Team" to serve 'true', default 'false'
- "show-release-dates": Target "General Audience" to serve 'true', default 'false'
5. Run the application:
```python main.py```

## How It Works
- The application uses LaunchDarkly contexts to represent different user segments.
- Feature flags determine which content to serve based on the user's segment.
- DJ Toggle's team sees the full playlist from the database.
- The general audience sees the top 10 tracks from a JSON file, including release dates.


## Questions? Comments? Quandries?
I'd love to chat with you!  Email me at [emikail@launchdarkly.com](mailto:emikail@launchdarkly.com) find me on [LinkedIn](https://www.linkedin.com/in/emikail/),[Twitter](https://twitter.com/erinmikail) or join the [LaunchDarkly Discord](https://discord.gg/CXSbsZZ6)

Happy Togglin'!