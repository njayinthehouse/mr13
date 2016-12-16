# imports

def search(name = None, status = None, author = None, genres = []):
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

def find(name, display_chapter_list = False, chapters = []):
	'''
	Searches for a manga online by exact name. 
	If the ~chapterlist (or ~c) flag is on, it displays the chapters.
	It can also accept chapters to be downloaded if the ~stash (or ~s) flag is on.
	'''
	pass

def destroy(name, chapters = []):
	'''
	Searches for a manga in the database by exact name and deletes it.
	If the ~chapters (or ~c) flag is on, it just deletes the specified chapters.
	'''
	pass

def scout(status = None, genres = [], start = 0):
	'''
	Searches for manga online which match the given criteria.
	The ~limit (or ~l) flag allows you to specify the maximum number of results desired, which is by default 30.
	'''
	pass

def fetch(name, chapters = []):
	'''
	Fetches manga data from the database by exact name.
	If the ~chapters (or ~c) flag is set, you can also open chapters of that manga.
	'''
	pass

def track(name):
	'''
	Tracks a manga in the database, watching for updates online and storing such notifications in a log file. 
	If the ~active (or ~a) flag is set, it automatically downloads chapters of that manga on release.
	If the ~passive (or ~p) flag is set, it changes tracking status from active to inactive
	'''
	pass

def abort(name):
	'''
	Stops tracking a manga.
	'''
	pass

def report():
	'''
	Displays the log file.
	'''
	pass
