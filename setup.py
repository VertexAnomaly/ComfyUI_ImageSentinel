# ComfyUI_ImageSentinel/setup.py

from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ComfyUI_ImageSentinel",
    version="1.0.0",
    packages=find_packages(),
    install_requires=requirements,
)