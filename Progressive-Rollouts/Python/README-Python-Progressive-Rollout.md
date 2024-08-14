# DJ Toggle's Top Tracks - Progressive Rollout Demo

This project demonstrates the use of LaunchDarkly's progressive rollout feature to manage the release of a new database-driven playlist system for DJ Toggle's Top Tracks.

## Overview

The application showcases two versions of a playlist:
1. A JSON-based version with the top 10 tracks
2. A database-driven version with the full playlist

LaunchDarkly's feature flag "progressive-rollout" is used to control which version users see.

## Why Use Progressive Rollout?

Progressive rollout is beneficial for several reasons:

1. **Risk Mitigation**: Gradually expose new features to users, allowing you to catch and address issues before they affect your entire user base.

2. **Performance Monitoring**: Assess the impact of the new database-driven system on application performance with a subset of users.

3. **User Feedback**: Gather feedback from a select group of users (e.g., beta testers) before full deployment.

4. **Rollback Capability**: Easily revert to the previous version if unexpected issues arise.

5. **A/B Testing**: Compare user engagement between the limited and full playlist versions.

## Setup and Usage

1. Install required dependencies:

```pip install ldclient-py```


2. Set up your LaunchDarkly SDK key as an environment variable:

```export LD_SDK_KEY=your_sdk_key_here```


3. Run the application:

```python main.py```


4. Use LaunchDarkly's dashboard to control the "progressive-rollout" feature flag:
- Set to `false` for the JSON-based top 10 tracks
- Set to `true` for the full database-driven playlist

5. Target specific users or groups (e.g., 'beta_testers') for early access to the new feature.

## How It Works

The application uses LaunchDarkly's SDK to check the state of the "progressive-rollout" feature flag for each user. Based on the flag's value, it either displays the top 10 tracks from a JSON file or the full playlist from a SQLite database.

This setup allows for a controlled, gradual rollout of the new database-driven system, ensuring a smooth transition and minimizing potential disruptions to the user experience.

## Questions? Comments? Quandaries? 
I'd love to chat with you!  Email me at [emikail@launchdarkly.com](mailto:emikail@launchdarkly.com) find me on [LinkedIn](https://www.linkedin.com/in/emikail/), or join the [LaunchDarkly Discord](https://discord.gg/CXSbsZZ6)

Happy Togglin'! 