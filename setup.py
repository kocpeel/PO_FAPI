from setuptools import setup, find_packages

setup(
    name="orator",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi",
        "pyttsx3",
        "pydantic",
    ],
)