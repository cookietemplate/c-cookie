import os
import shutil
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

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


def format_license(license_content):
    """Format the license file"""
    license_content = license_content.replace("[year]", "{% now 'local', '%Y' %}")
    license_content = license_content.replace("[fullname]", "{{ cookiecutter.full_name }}")
    license_content = license_content.replace("[email]", "{{ cookiecutter.email }}")
    license_content = license_content.replace("[project]", "{{ cookiecutter.project_name }}")

    # GPL 3-Clause License
    license_content = license_content.replace("<year>", "{% now 'local', '%Y' %}")
    license_content = license_content.replace("<name of author>", "{{ cookiecutter.full_name }}")
    license_content = license_content.replace(
        "<one line to give the program's name and a brief idea of what it does.>",
        "{{ cookiecutter.project_short_description }}"
    )

    return license_content


def write_license_file(license_name):
    """Write the license file to the project directory"""
    license_content = download_license_from_github(license_name)
    if license_content:
        with open(os.path.join(PROJECT_DIRECTORY, 'LICENSE'), 'w') as f:
            f.write(license_content)


def init_git_repo():
    """Initialize the git repository"""
    os.system("git init")
    os.system("git add .")
    os.system("git commit -m 'Initial commit'")

def init_poetry():
    """Initialize the poetry"""
    os.system("poetry install")

if __name__ == '__main__':
    if "{{ cookiecutter.open_source_license }}" != "Proprietary":
        write_license_file("{{ cookiecutter.open_source_license }}")

    init_git_repo()
    init_poetry()
