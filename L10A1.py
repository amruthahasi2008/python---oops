class playlist :
    def __init__(self, name , genre):
        self.name = name
        self.genre = genre
        self.songs = []

    def add(self , song) :
        self.songs.append(song)
        print(f"{song} is added to {self.name}")
    
    def remove(self,song) :
        if song in self.songs :
            self.songs.remove(song)
            print(f"{song}is removed")
        else :
            print(f"{song} is not in {self.songs}")
    def display(self) :
        if self.songs :
            for i,song in enumerate(self.songs,1):
                print(f"{i}{song}")
        else :
            print("no songs yet")
    def __del__(self) :
        print("{self.name} has been deleted")
    
my_playlist = playlist("road mix","pop")
while True :
    print("\n1.add song  2. delete song  3. display songs 4. delete and quit")
    choice = int(input("enter your choice"))
    if choice == 1 :
        song = input("enter song name")
        my_playlist.add(song)
    elif choice == 2 :
        song = input("enter song name")
        my_playlist.remove(song)
    elif choice == 3 :
        my_playlist.display()
    elif choice == 4 :
        del my_playlist
        break
    else :
        print("invalid choice choose 1,2 ,3 or 4")
    
