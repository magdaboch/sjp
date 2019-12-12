import zipfile

if __name__ == '__main__':

    with zipfile.ZipFile('sjp-odm-20191209.zip') as zipped_file:
        for file_in_zip in zipped_file.namelist():
            bajts = len(zipped_file.read(file_in_zip))
            print(f'Plik: {file_in_zip} {bajts}b')


