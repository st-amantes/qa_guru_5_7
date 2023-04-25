import os.path
import requests

def test_download_file():
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'

    Project_root_path = os.path.dirname(os.path.abspath(__file__))
    tmp_folder = os.path.join(Project_root_path, 'tmp', 'selenium_logo.png' )
    if not os.path.exists(tmp_folder):
        os.mkdir('tmp')

    r = requests.get(url)
    with open(tmp_folder, 'wb') as file:
        file.write(r.content)

    size_file = os.path.getsize(tmp_folder)
    assert size_file == 30803

