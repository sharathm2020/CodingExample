from media import Media, Movie, Song, Picture

#function to output the menu after each time a choice is entered
def repeatMenu():
    print('*** Media Library ***')
    print('a. Display all Media\n'
          'b. Display only Songs\n'
          'c. Display only Movies\n'
          'd. Display only Pictures\n'
          'e. Play a Song\n'
          'f. Play a Movie\n'
          'g. Show a Picture\n'
          'h. Add a Song\n'
          'i. Add a Movie\n'
          'j. Add a Picture\n'
          'k. Exit the program\n')


#main
if __name__ == '__main__':
    #initialize a list with all media added
    media = []
    #menu printed out
    repeatMenu()
    choice = input("Enter your choice: ")
    #while True loop that allows the user to continously enter a choice until k is entered, and the menu is repeatedly printed out as wel
    while True:
        
        #if and elif statements for each choice, using ifInstance to return either print out the media if found in the one of the medias
        if choice.lower() == 'a':
            for x in media:
                print(x)
            repeatMenu()
            choice = input("Enter your choice: ")
        elif choice.lower() == 'b':
            for x in media:
                if isinstance(x, Song):
                    print(x)
            repeatMenu()
            choice = input("Enter your choice: ")
        elif choice.lower() == 'c':
            for x in media:
                if isinstance(x, Movie):
                    print(x)
            repeatMenu()
            choice = input()
        elif choice.lower() == 'd':
            for x in media:
                if isinstance(x, Picture):
                    print(x)
            repeatMenu()
            choice = input("Enter your choice: ")
        elif choice.lower() == 'e':
            print("Enter name of the song to play: ")
            songName = input()
            if len(media) == 0:
                print("No such song in the media library")
            for x in media:
                if isinstance(x, Song) and x.getName() == songName:
                    songName.play()
                else:
                    print("No such song in the media library")
            repeatMenu()
            choice = input("Enter your choice: ")
        elif choice.lower() == 'f':
            print("Enter name of the Movie to play: ")
            movieName = input()
            if len(media) == 0:
                print("No such movie in the media library")
            for x in media:
                if isinstance(x, Movie) and x.getName() == movieName:
                    movieName.play()
                else:
                    print("No such movie in the media library")
            repeatMenu()
            choice = input("Enter your choice: ")
        elif choice.lower() == 'g':
            print("Enter name of the Picture to play: ")
            picName = input()
            if len(media) == 0:
                print("No such picture in the media library")
            for x in media:
                if isinstance(x, Picture) and x.getName() == picName:
                    picName.play()
                else:
                    print("No such picture in the media library")
            repeatMenu()
            choice = input("Enter your choice: ")
        elif choice.lower() == 'h':
            song = Song.add()
            media.append(song)
            repeatMenu()
            choice = input("Enter your choice: ")
        elif choice.lower() == 'i':
            movie = Movie.add()
            media.append(movie)
            repeatMenu()
            choice = input("Enter your choice: ")
        elif choice.lower() == 'j':
            picture = Picture.add()
            media.append(picture)
            repeatMenu()
            choice = input("Enter your choice: ")
        elif choice.lower() == 'k':
            print("Good-Bye!")
            break




