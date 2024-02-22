import os
import time

path = rf"{input('Укажите путь к .mp3 файлам, которым нужно поправить вид: ')}"
data = sorted([song for song in os.listdir(path) if song.endswith('.mp3') and '_' in song])

song_name = list()
song_name_list = list()

for song in data:
    song_name = list()
    if '_' in song:
        for song_part in song.split('_'):
            if '.mp3' in song_part:
                song_part = song_part.strip('.mp3')
            if song_part.isalpha() or song_part == '-':
                song_name.append(song_part.capitalize())
        else:
            song_name = ' '.join(song_name)
            song_name += '.mp3'
            song_name_list.append(song_name)
else:
    del song_name, song, song_part
    song_name_list = sorted(tuple(song_name_list))


for index in range(len(data)):    
    old_name = data[index]
    new_name = song_name_list[index]
    os.rename(f'{path}\\{old_name}', f'{path}\\{new_name}')
else:
    input('Программа закончила переименование.\nНажмите Enter для закрытия окна...')



