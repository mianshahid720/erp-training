from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erp_training/__init__.py
from erp_training import __version__ as version

setup(
	name="erp_training",
	version=version,
	description="training of erpnext",
	author="shahid",
	author_email="shahid@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
