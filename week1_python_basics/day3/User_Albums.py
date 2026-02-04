def make_album(artist_name, album_title, tracks=None):
    album = {
        "artist": artist_name.title(),
        "title": album_title.title()
    }
    if tracks:
        album["tracks"] = tracks
    return album

while True:
    print("\nEnter 'q' at any time to quit.")
    
    artist = input("Enter artist name: ")
    if artist.lower() == 'q':
        break

    title = input("Enter album title: ")
    if title.lower() == 'q':
        break

    tracks = input("Enter number of tracks (press Enter to skip): ")
    if tracks.lower() == 'q':
        break

    if tracks:
        album = make_album(artist, title, tracks=int(tracks))
    else:
        album = make_album(artist, title)

    print(album)
