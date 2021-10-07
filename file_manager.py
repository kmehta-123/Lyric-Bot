import os

def write_to_file(lyrics):
    lyric_body = lyrics[1]
    file_path = '{}.txt'.format(lyrics[0].replace('\"', '').replace('\"', ''))
    if os.path.exists(file_path):
        os.remove(file_path)
    file = open(file_path, 'w+')
    for line in lyric_body:
        file.write(line + '\n')
    file.close()
    return file





