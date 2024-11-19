import json

# Load JSON file
with open("saved_tracks.json", "r") as file:
    data = json.load(file)

# Start building the HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Spotify Tracks</title>
</head>
<body>
    <h1>My Saved Spotify Tracks</h1>
    <ul>
"""

# Loop through the JSON data to extract and display relevant details
for idx, item in enumerate(data['items']):
    track = item['track']
    artist = track['artists'][0]['name']
    song = track['name']
    url = track['external_urls']['spotify']
    html_content += f'<li>{idx + 1}: <a href="{url}" target="_blank">{artist} - {song}</a></li>'

html_content += """
    </ul>
</body>
</html>
"""

# Save the HTML content to a file
with open("saved_tracks.html", "w") as html_file:
    html_file.write(html_content)

print("HTML file 'saved_tracks.html' created!")
