from setuptools import setup

setup(
    name="WetterKassel",
    version="0.0.1",
    url="https://github.com/jakobbbb/wetterkassel",
    author="jakobbb",
    author_email="jakobbbb@users.noreply.github.com",
    packages = ["WetterKassel"],
    description = "A twitter bot that tweets out forecasts",
    license = "MIT",
    install_requires = [
        "python-twitter>=3.2.1",
      ],
    )
