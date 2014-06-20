from setuptools import setup

setup(name="dodsbirscrape",
	version='1.0',
	description='Scraping library for DODSBIR.net',
	url='http://github.com/jroo/dodsbir-scrape',
	author='Joshua Ruihley/18F',
	author_email='josh.ruihley@gsa.gov',
	packages = ['dodsbirscrape'],
	license='LICENSE.md',
	zip_safe=False,
	install_requires = [
		'beautifulsoup4>=4.3.2',
		'requests==2.3.0'
	]
)
