import urllib.request
import zipfile
import glob
import os
import sys



def download_file(filename, url, target_file=None, target_path=''):
    target_file = filename if not target_file else target_file
    response = urllib.request.urlopen(f'{url}{filename}')
    result = response.read()

    os.makedirs(target_path, exist_ok=True)
    with open(f'{target_path}{target_file}', 'wb') as file:
        file.write(result)

def zipped_one_file(url, file_in_zip, target_path):
    with zipfile.ZipFile(url, 'r') as zipped_file:
        zipped_file.extract(file_in_zip, path=target_path)

def add_palindrom_to_file(poli_list: list, target_path=''):
    if not poli_list:
        return
    with open(f'{target_path}palindroms.txt', 'w') as file:
        file.write('\n'.join(poli_list))



if __name__ == '__main__':
    download_file('sjp-odm-20191209.zip', 'https://sjp.pl/slownik/odmiany/', 'sjp-odm-20191209.zip', 'torbabobra/')
    zipped_one_file('./torbabobra/sjp-odm-20191209.zip', 'odm.txt', 'torbabobra/')
    poli_list = []
    with open('torbabobra/odm.txt') as file:
        for linia in file.readlines():
            for char in linia.strip().split(', '):
                char = char.lower()
                rev_char = char[::-1]
                if len(char) > 3 and char == rev_char:
                    poli_list.append(char)
    poli_list = sorted(list(set(poli_list)))
    print(len(poli_list))
    add_palindrom_to_file(poli_list, 'torbabobra/')