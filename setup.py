from setuptools import setup

setup(
		name='gutils',
		version='0.1.0',
		packages=['gutils'], # commented out gutils.gcp
		url='',
		license='',
		author='michaelwomack',
		author_email='mwomack93@gmail.com',
		description='Utilities for google apis',
		install_requires = [
			'google-cloud-storage==1.7.0'
		]
)