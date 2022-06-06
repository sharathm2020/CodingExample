#importing abstract
from abc import abstractmethod

class Media:
    #constructor for Media
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
    
    #getters and setters
    def getName(self):
        return self.__name
    
    def getRating(self):
        return self.__rating
    
    def setRating(self, rating):
        self.__rating = rating
    
    
    #str output function
    def __str__(self):
        return "Media: " +str(self.__name)+", "+str(self.__rating)+" stars."
    
    
    @abstractmethod
    #abstract method for add
    def add():
        pass
    

class Movie(Media):
    #constructor for Movie
    def __init__(self, name, rating, director, running_time):
        super().__init__(name, rating)
        self.__director = director
        self.__running_time = running_time
    
    #getters and setters
    def setDirector(self, director):
        self.__director = director
    
    def getDirector(self):
        return self.__director
        
    def setRunningTime(self, time):
        self.__running_time = time
        
    def getRunningTime(self):
        return self.__running_time
    
    #play function that prints the current movie playing
    def play(self):
        print("Movie: "+str(self.getName())+" playing now.")
    
    #str output function for movie
    def __str__(self):
        return "Movie: "+str(self.getName())+", "+str(self.getRating())+" stars, Directed by: "+str(self.__director)+", Running time: "+str(self.__running_time)+" minutes."
    

    #static add function override for Movie
    def add():
        name = input("Enter movie name: ")
        director = input("Enter director: ")
        running_time = input("Enter movie duration: ")
        rating = input("Enter rating: ")
        print("Movie added!")
        movie1 = Movie(name, rating, director, running_time)
        return movie1
    
    
    
class Song(Media):
    #constructor for Song
    def __init__(self, name, rating, artist, album):
        super().__init__(name, rating)
        self.__artist = artist
        self.__album = album
    
    #getters and setters
    def getArtist(self):
        return self.__artist
    
    def getAlbum(self):
        return self.__album
    
    def setArtist(self, artist):
        self.__artist = artist
    
    def setAlbum(self, album):
        self.__album = album
    
    #play function that prints the current song and artist playing now
    def play(self):
        print(str(self.getName()),"by "+self.__artist+" playing now.")
    
    #str output function for Song
    def __str__(self):
        return "Song: "+str(self.getName())+", "+str(self.getRating())+" stars, Artist: "+self.getArtist()+", Album: "+self.getAlbum()+"."
    
    #static add function override for Song
    def add():
        name = input("Enter song name: ")
        artist = input("Enter artist: ")
        album = input("Enter album: ")
        rating = input("Enter rating: ")
        print("Song added!")
        song1 = Song(name, rating, artist, album)
        return song1
    

class Picture(Media):
    #constructor for Picture
    def __init__(self, name, rating, dpi):
        super().__init__(name, rating)
        self.__dpi = dpi
    
    #getter and setter for Resolution
    def getResolution(self):
        return self.__dpi
    
    def setResolution(self, dpi):
        self.__dpi = dpi
    
    #show function that prints the current picture being shown
    def show(self):
        print("Showing "+str(self.getName())+".")
    
    #str output function for Picture
    def __str__(self):
        return "Picture: "+str(self.getName())+", "+str(self.getRating())+" stars, Resolution: "+self.getResolution()+" dpi."
    
    #static add function override for Picture
    def add():
        name = input("Enter picture name: ")
        dpi = input("Enter dpi: ")
        rating = input("Enter rating: ")
        print("Picture added!")
        pic1 = Picture(name, rating, dpi)
        return pic1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        