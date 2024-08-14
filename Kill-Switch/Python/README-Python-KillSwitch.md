# DJ Toggle's Top Tracks - Kill Switch Demo

This project demonstrates the use of LaunchDarkly's kill switch feature to manage the availability of a new database-driven playlist system for DJ Toggle's Top Tracks.

## Overview

The application showcases two versions of a playlist:
1. A JSON-based version with the top 10 tracks
2. A database-driven version with the full playlist

LaunchDarkly's feature flag "use-database" is used as a kill switch to control which version users see.

## Why Use a Kill Switch?

A kill switch is beneficial for several reasons:

1. **Immediate Issue Resolution**: Quickly disable problematic features without deploying new code.

2. **Emergency Control**: Instantly revert to a stable version if critical issues arise in production.

3. **Maintenance Mode**: Easily switch off features during scheduled maintenance or updates.

4. **Gradual Feature Deprecation**: Control the sunset of old features while introducing new ones.

5. **Compliance and Regulation**: Quickly adapt to changing regulatory requirements by toggling features on/off.

1. Install required dependencies:

```pip install launchdarkly-server-sdk python-dotenv```


2. Create a `.env` file in the project root and add your LaunchDarkly SDK key:


```LD_SDK_KEY=your_sdk_key_here```


1. Run the application:

```python main.py```



4. Use LaunchDarkly's dashboard to control the "use-database" feature flag:
- Set to `false` for the JSON-based top 10 tracks
- Set to `true` for the full database-driven playlist

5. The application uses a Context with a 'beta_testers' group, allowing for targeted feature releases.

## How It Works

1. The application initializes the LaunchDarkly client using the SDK key from the `.env` file.
2. It loads the tracklist from a JSON file and sets up a SQLite database with the full playlist.
3. The `run_app()` function creates a user context and checks the "use-database" feature flag.
4. Based on the flag's value, it either displays the top 10 tracks from the JSON file or the full playlist from the database.
5. The chosen playlist is then printed to the console.

This setup allows for flexible control over which version of the playlist is served, enabling easy switching between the limited JSON version and the full database version based on the feature flag setting.

## Questions? Comments? Quandaries? 
I'd love to chat with you!  Email me at [emikail@launchdarkly.com](mailto:emikail@launchdarkly.com) find me on [LinkedIn](https://www.linkedin.com/in/emikail/), or join the [LaunchDarkly Discord](https://discord.gg/CXSbsZZ6)

Happy Togglin'! 