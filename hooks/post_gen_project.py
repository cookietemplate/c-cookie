import json
import os
import pathlib
import requests
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
PROJECT_ROOT = pathlib.Path(PROJECT_DIRECTORY)

LICENSES_DICT = {
    "Proprietary": None,
    "Apache-2.0": "Apache-2.0",
    "MIT": "MIT",
    "BSD-4-Clause": "BSD-4-Clause",
    "BSD-3-Clause": "BSD-3-Clause",
    "BSD-2-Clause": "BSD-2-Clause",
    "GPL-2.0-only": "GPL-2.0",
    "GPL-2.0-or-later": "GPL-2.0",
    "GPL-3.0-only": "GPL-3.0",
    "GPL-3.0-or-later": "GPL-3.0",
    "LGPL-2.1-only": "LGPL-2.1",
    "LGPL-2.1-or-later": "LGPL-2.1",
    "LGPL-3.0-only": "LGPL-3.0",
    "LGPL-3.0-or-later": "LGPL-3.0",
    "ISC": "ISC",
}


def download_license_from_github(license_name):
    """Download the license file from GitHub"""
    license_name = LICENSES_DICT[license_name]
    if license_name:
        url = 'https://api.github.com/licenses/{}'.format(license_name)
        response = requests.get(url)
        if response.status_code == 200:
            license_content = json.loads(response.content.decode('utf-8'))['body']
            return license_content
    return None


def write_license_file(license_name):
    """Write the license file to the project directory"""
    license_content = download_license_from_github(license_name)
    if license_content:
        with open(os.path.join(PROJECT_DIRECTORY, 'LICENSE'), 'w') as f:
            f.write(license_content)


def remove_file(file_path, missing_ok=False):
    (PROJECT_ROOT / file_path).unlink(missing_ok=missing_ok)

def remove_folder(dir_path:str):
    shutil.rmtree((PROJECT_ROOT / dir_path))

if __name__ == '__main__':
    if "{{ cookiecutter.open_source_license }}" != "Proprietary":
        write_license_file("{{ cookiecutter.open_source_license }}")

    if {{ cookiecutter.has_include_folder }}:
        remove_file("src/library.h")
    else:
        remove_folder("include")

    if not {{ cookiecutter.has_include_folder }}:
        remove_folder("app")

    if not {{ cookiecutter.has_test }}:
        remove_folder("test")

    if not {{ cookiecutter.has_example }}:
        remove_folder("example")
