from pathlib import Path
from setuptools import setup

setup(install_requires=Path("requirements.txt").read_text(), use_scm_version=True)
