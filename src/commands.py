import requests
from bs4 import BeautifulSoup
import os

import htmlparsers.mangareader as mrparser


# String * IntOption * IntOption -> BeautifulSoup
def get_soup(name, chapter_number = None, page_number = None):
	def formatted_name():
		def aux(str, acc=''):
			if str == '':
				return acc
			if str[0].isalnum():
				return aux(str[1:], acc + str[0].lower())
			elif str[0] == ' ' and acc[-1] != '-':
				return aux(str[1:], acc + '-')
			else:
				return aux(str[1:], acc)
		url = os.path.join(mrparser.BASE_URL, aux(name))

		if chapter_number is not None:
			url = os.path.join(url, str(chapter_number))
			if page_number is not None:
				url = os.path.join(url, str(page_number))

		return url
	url = formatted_name()
	r = requests.get(url)

	if r.status_code == 404:
		raise Exception('Manga ' + name + ' does not exist at ' + url)
	else:
		return BeautifulSoup(r.content, 'html.parser')

def search (name = None, status = None, author = None, genres = []):
	'''
	Searches for a manga in the database based on given flags :
	1. ~name or ~n
	2. ~status or ~s
	3. ~author or ~s
	4. ~genres or ~g
	and returns the manga name and information.
	Also returns the chapterlist if the ~chapterlist (or ~c) flag is on.
	'''
	pass

# String * Boolean * Boolean * ChapterList -> O/P
def find(name, should_get_chapter_list = False, stash=False, chapters = []):
	'''
	Searches for a manga online by exact name.
	If the ~chapterlist (or ~c) flag is on, it displays the chapters.
	It can also accept chapters to be downloaded if the ~stash (or ~s) flag is on.
	'''
	soup = get_soup(name)
	def display_info():
		manga_data = mrparser.get_info(soup)
		print 'Name:\t' + manga_data['name']
		print 'Author:\t' + manga_data['author']
		print 'Artist:\t' + manga_data['artist']
		print 'Genres:\t' + ', '.join(manga_data['genres'])
		print 'Year:\t' + manga_data['year']
		print 'Status:\t' +	manga_data['status']
		print 'Summary:\n' + manga_data['summary']
	def display_chapter_list():
		for i, chapter in enumerate(mrparser.get_chapter_list(soup)):
			print 'Chapter ' + str(i) + ':\t' + chapter[0] + '\t\t\t\t' + chapter[1]

	display_info()
	if should_get_chapter_list:
		display_chapter_list()

	if stash:
		pass

def destroy (name, chapters = []):
	'''
	Searches for a manga in the database by exact name and deletes it.
	If the ~chapters (or ~c) flag is on, it just deletes the specified chapters.
	'''
	pass

def scout (status = None, genres = [], start = 0):
	'''
	Searches for manga online which match the given criteria.
	The ~limit (or ~l) flag allows you to specify the maximum number of results desired, which is by default 30.
	'''
	pass

def fetch (name, chapters = []):
	'''
	Fetches manga data from the database by exact name.
	If the ~chapters (or ~c) flag is set, you can also open chapters of that manga.
	'''
	pass

def track (name):
	'''
	Tracks a manga in the database, watching for updates online and storing such notifications in a log file. 
	If the ~active (or ~a) flag is set, it automatically downloads chapters of that manga on release.
	If the ~passive (or ~p) flag is set, it changes tracking status from active to inactive
	'''
	pass

def abort (name):
	'''
	Stops tracking a manga.
	'''
	pass

def report ():
	'''
	Displays the log file.
	'''
	pass
