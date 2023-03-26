# Muzik API

Personal Music API to download and search music from several platforms such as JioSaavn.


## Documentation

| Endpoint | GET query params | Example |
|:--------:|:----------------:|:-------:|
|/api/jiosaavn/search/|type={all,song,album}&query={query:str}&page_no={page_no:int}| /api/jiosaavn/search/?type=all&query=arijit+singh&page_no=1 |
|/api/jiosaavn/details/|type={playlist,song,album}&query={link_or_id:str/int} | /api/jiosaavn/details/?type=playlist&query=802336660, /api/jiosaavn/details/?type=playlist&query=https://www.jiosaavn.com/s/playlist/a60306bf0bd5cacc95a888a361163e07/Ppll/Iz0pi7nkjUHfemJ68FuXsA__, /api/jiosaavn/details/?type=song&query=https://www.jiosaavn.com/song/phir-bhi-tumko-chaahunga/OQQJQBJ4fGc, /api/jiosaavn/details/?type=album&query=https://www.jiosaavn.com/album/kisi-ka-bhai-kisi-ki-jaan/MBf5fKyNXlY_|
