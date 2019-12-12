import zipfile
import glob
import os

if __name__ == '__main__':
    # with zipped_file = zipfile.ZipFile('sjp-odm-20191209.zip') as zipped_file:
    #     for file_in_zip in zipped_file.namelist():
    #         bajts = len(zipped_file.read(file_in_zip))
    #         print(f'Plik: {file_in_zip} {bajts}b')
    with zipfile.ZipFile('/tmp/pytgup6_day_2.zip', 'w') as zip_handler:
        for file in glob.glob('*.py'):
            #file_resource = open(file, 'rb').read() # czytamy pliki binarnie
            zip_handler.write(file, arcname=f'cmp_{file}')
        #zip_handler.close() - niepotrzebne, bo kontekst zamknął
    print('Huraaa!'
        if os.path.exists('/tmp/pytgup6_day_2.zip')
        else 'No i dupa'
    )