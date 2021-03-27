import os


def sort_files(paths):
    for values in os.listdir(paths):
        if os.path.isdir(paths + '/' + values):
            sort_files(paths + '/' + values)
        else:
            if values.endswith(base_photo[0]):
                base_photo.append(values)
            elif values.endswith(base_video[0]):
                base_video.append(values)
            elif values.endswith(base_documents[0]):
                base_documents.append(values)
            elif values.endswith(base_music[0]):
                base_music.append(values)
            elif values.endswith(base_archives[0]):
                base_archives.append(values)
            else:
                base_unknoun.append(values)


def main():
    path = r'C:/Users/Владыка/Desktop/Разобрать'
    return sort_files(path)


if __name__ == '__main__':
    base_photo = [('jpg', 'jpeg', 'png', 'svg')]
    base_video = [('avi', 'mp4', 'mov', 'mkv')]
    base_documents = [('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx')]
    base_music = [('mp3', 'ogg', 'wav', 'amr')]
    base_archives = [('zip', 'gz', 'tar')]
    base_unknoun = []
    main()
    print(f'Photos:\n {base_photo[1:-1]}\nVideos:\n {base_video[1:-1]}\nDocuments:\n {base_documents[1:-1]}\n'
          f'Music:\n {base_music[1:-1]}\nArchives:\n {base_archives[1:-1]}\nUnknoun:\n {base_unknoun}')
