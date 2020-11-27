class Track:
    def __init__(self, name, duration):
        self.name = name
        self.duration = int(duration)

    def __str__(self):
        print(f'<{self.name} - {self.duration} минуты>')

    def __gt__(self, other):
        if not isinstance(other, Track):
            print('False')
        return self.duration > other.duration


class Album:
    def __init__(self, name_album, group):
        self.name_album = name_album
        self.group = group
        self.list_track = []

    def __str__(self):
        print(f'Name group: {self.group} \nName album: {self.name_album} \nTracks: \n {self.list_track}')

    def add_track(self, track):
        self.list_track.append(track)

    def get_duration(self):
        sum_track = sum(el.duration for el in self.list_track)
        print(f'Duration album {self.name_album}: {sum_track} minutes')


track_1 = Track('moon', 4)
track_2 = Track('sun', 2)
track_3 = Track('sky', 3)

tracks = [track_1, track_2, track_3]

album_1 = Album('Ups', 'Dollar')
album_2 = Album('Bobik', 'Evro')

all_albums = [album_1, album_2]

album_1.add_track(track_1)
album_1.add_track(track_2)
album_2.add_track(track_3)

album_1.__str__()
album_2.__str__()

album_1.get_duration()
album_2.get_duration()

print(track_1 > track_2)
print(track_1 > track_3)
print(track_2 > track_3)

