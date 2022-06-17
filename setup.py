from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in modon_statistics/__init__.py
from modon_statistics import __version__ as version

setup(
	name="modon_statistics",
	version=version,
	description="stattistics for modon servers",
	author="baha",
	author_email="baha@slnee.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
