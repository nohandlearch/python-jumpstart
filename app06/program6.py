import os
import platform
import subprocess
import cat_service

def main():
    print_header()

    folder = get_or_create_output_folder()

    download_cats(folder)

    display_cats(folder)


def print_header():
    print('--------------------------')
    print('       CAT FACTORY')
    print('--------------------------')


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    cat_folder = 'cat_pictures'
    full_path = os.path.join(base_folder, cat_folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)
    
    return full_path


def download_cats(folder):
    print('Contacting server to download cats...')
    cat_count = 8
    for i in range(1, cat_count+1):
        cat_name = 'lolcat_{}'.format(i)
        print('Downloading cat ' + cat_name)
        cat_service.get_cat(folder, cat_name)
    print('Finished downloading {} cats'.format(cat_count))


def display_cats(folder):
    system_type = platform.system()
    if system_type == 'Linux':
        subprocess.call(['xdg-open', folder])
    elif system_type == 'Darwin':
        subprocess.call(['open', folder])
    elif system_type == 'Windows':
        subprocess.call(['explorer', folder])
    else:
        print('Unsupported OS {}'.format(system_type))


if __name__ == '__main__':
    main()