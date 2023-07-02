from setuptools import setup, find_packages
import json
# import shutil 
# import pathlib, os

with open("libraryData.json", "r") as f:
    jsonTxt = f.read()
    libData = json.loads(jsonTxt)

    setup(name="typesetLib",
        version=libData["typesetLibVersion"],
        description="This tool allows typeset simple layouts using really simple object system.",
        author="Rafał Buchner",
        author_email="rafal.buchner@gmail.com",
        url="https://github.com/RafalBuchner/quickProof/",
        packages=find_packages(),    
        install_requires=libData["requirements"],
        dependency_links=libData["dependency_links"]
        # entry_points = {
        #     'console_scripts': ['typeset=typeset:main']
        # }
    )
