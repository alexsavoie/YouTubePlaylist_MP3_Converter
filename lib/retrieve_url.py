import requests
import json
import config

def search_video(title):
  # Set the API key for your project
  api_key = config.api_key

  # Set the parameters for the search request
  params = {
      "key": api_key,
      "q": title,
      "part": "snippet",
      "type": "video",
      "maxResults": 1
  }

  # Make the request to the YouTube API
  r = requests.get("https://www.googleapis.com/youtube/v3/search", params=params)
  
  # Extract the search results
  results = r.json()["items"]

  # Get the first result
  if len(results) > 0:
    video = results[0]
    # Return the URL of the video
    return f"https://www.youtube.com/watch?v={video['id']['videoId']}"
  else:
    print("No videos found with that title.")
    
