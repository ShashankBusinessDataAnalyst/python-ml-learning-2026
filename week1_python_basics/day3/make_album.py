def make_album(artist_name, album_title, tracks=None):
    album = {
        "artist": artist_name.title(),
        "title": album_title.title()
    }
    if tracks:
        album["tracks"] = tracks
    return album

# Creating 3 album dictionaries
album1 = make_album("taylor swift", "1989")
album2 = make_album("adele", "25")
album3 = make_album("drake", "scorpion", tracks=18)

print(album1)
print(album2)
print(album3)
