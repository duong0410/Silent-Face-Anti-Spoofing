from setuptools import find_packages, setup

setup(
    name="silent-face-anti-spoofing",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.24",
        "torch>=2.1",
        "opencv-python>=4.8",
    ],
)
