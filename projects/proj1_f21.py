#########################################
##### Name:  Xiangyun Deng          #####
##### Uniqname:  dengxy             #####
#########################################

import json
import requests
import webbrowser

class Media:

    def __init__(self, title="No Title", author="No Author", release_year = "No Release Year", url = "No URL", json = None):
        if json == None:
            self.title = title
            self.author = author
            self.release_year = release_year
            self.url = url
        else:
            try:
                self.title = json['trackName']
            except:
                self.title = json['collectionName']
            self.author = json['artistName']
            self.release_year = json['releaseDate'][:4]
            if 'trackViewUrl' in json:
                self.url = json['trackViewUrl']
            else:
                self.url = json['collectionViewUrl']


    def info(self):
        return f"{self.title} by {self.author} ({self.release_year})"
    
    def length(self):
        return 0

class Song(Media):
    def __init__(self, title="No Title", author="No Author", release_year = "No Release Year", url = "No URL", album = "No Album", genre = "No Genre", track_length = 0, json = None):
        super().__init__(title, author, release_year, url, json)
        if json == None: 
            self.album = album
            self.genre = genre
            self.track_length = track_length
        else:
            self.album = json["collectionName"]
            self.genre = json["primaryGenreName"]
            self.track_length = json["trackTimeMillis"]
    
    def info(self):
        return super().info() + f" [{self.genre}]"

    def length(self):
        return round(self.track_length/1000)

class Movie(Media):
    def __init__(self, title="No Title", author="No Author", release_year = "No Release Year", url = "No URL", rating = "No Rating", movie_length = 0, json = None): 
        super().__init__(title, author, release_year, url, json)
        if json == None: 
            self.rating = rating
            self.movie_length = movie_length
        else:
            self.rating = json["contentAdvisoryRating"]
            self.movie_length = json["trackTimeMillis"]

    
    def info(self):
        return super().info() + f" [{self.rating}]"
    
    def length(self):
        return round(self.movie_length/60000)   

def get_data(artist, limit):
    params = {
        'term': artist,
        'limit': limit
    }
    response = requests.get("https://itunes.apple.com/search?", params=params)
    artist_info = json.loads(response.text)
    return artist_info

# Test 
# My_Favorite = get_data('Travis Scott', 10)
# print(type(My_Favorite))
# print(My_Favorite['results'])

def get_results(name):
    num_media = 0
    while True:
        num_results_str = input("How many results do you want to preview? ")
        try:
            num_results = int(num_results_str)
        except:
            print("Please enter an integer number.")
            continue
        if num_results < 1 or num_results > 100:
            print("Please enter a valid number between 1 and 100.")
            continue
        break
    results = get_data(name, num_results)

    print(f"\nSONGS")
    num_song = 0
    for result in results['results']:
        if result['wrapperType'] == 'track':
            if 'song' == result['kind']:
                num_media += 1
                num_song += 1
                print(f"{str(num_media)} {Song(json=result).info()}")
                media_list.append(result)
    if num_song == 0:
        print('There are no songs that match your search.')

    print(f"\nMOVIES")
    num_movie = 0
    for result in results['results']:
        if result['wrapperType'] == 'track':
            if 'feature-movie' == result['kind']:
                num_media += 1
                num_movie += 1
                print(f"{str(num_media)} {Movie(json=result).info()}")
                media_list.append(result)
    if num_movie == 0:
        print('There are no movies that match your search.')

    print(f"\nOTHER MEDIA")
    num_othermedia = 0
    for result in results['results']:
        if result['wrapperType'] == 'track':
            if result['kind'] not in ["feature-movie", "song"]:
                num_media += 1
                num_othermedia += 1
                print(f"{str(num_media)} {Media(json=result).info()}")
                media_list.append(result)
        else:
            num_media += 1
            num_othermedia += 1
            print(f"{str(num_media)} {Media(json=result).info()}")
            media_list.append(result)

    if num_othermedia == 0:
        print(f"There is no other media that matches your search.\n")

    if num_media == 0:
        print(f"There are no results for your search.")



if __name__ == "__main__":
    # your control code for Part 4 (interactive search) should go here
    media_list = []
    info = ''
    while True:
        if len(media_list) == 0:
            term = input('Enter a search term, or "exit" to quit: ')
            if term == 'exit':
                print('Bye!')
                break
            else:
                get_results(term)
        else:
            info = input('Enter a number for more info, or another search term, or "exit": ')
            if info == 'exit':
                print('Bye!')
                break
            try:
                num = int(info)
                print("Launching")
                if 'trackViewUrl' in media_list[num-1]:
                    print(media_list[num-1]['trackViewUrl'])
                    print(f"in web browser...")
                    webbrowser.open(media_list[num-1]['trackViewUrl'])
                else:
                    print(media_list[num-1]['collectionViewUrl'])
                    print(f"in web browser...")
                    webbrowser.open(media_list[num-1]['collectionViewUrl'])
            except:
                media_list = []
                get_results(info)
