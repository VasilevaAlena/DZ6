class Track():

    def __init__(self, name, duration):
        self.name = name
        self.duration = int(duration)

    def show(self):
        print(f'<{self.name} - {self.duration} минуты>')

track_1 = Track('moon', 3)
track_1.show()

track_2 = Track('sun', 4)
track_2.show()

track_3 = Track('sky', 2)
track_3.show()


class Album():

    def __init__(self, name_album, group):
        self.name_album = name_album
        self.group = group
        self.list_track = []

    # def get_tracks(self, name, duration):
    #     return track_1.show()

    # def add_track(self):
    #     name = input('Введите название трека ')
    #     time = input('Введите продолжительность трека ')
    #     self.list_track.append(Track(name, time))
#
#     def get_duration(self):

album_1 = Album('Ups', 'Dollar')
album_1.list_track = track_1, track_2

album_2 = Album('Bobik', 'Evro')
album_2.list_track = track_3
print(album_1.__dict__ )
print(album_2.__dict__ )

