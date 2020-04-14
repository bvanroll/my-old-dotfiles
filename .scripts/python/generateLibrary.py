import os


destFolder = "~/lib"
destDb = "~/lib/db.json"

if !os.path.exists(destFolder):
	os.mkdir(destFolder)
else:
	if !os.path.exists(destDb):
		destDb = {}
	else:
		destDb = loadDb(destDb)




categories = {
	"0 uncategorized": {
		"00 images": [],
		"01 movies": [],
		"02 songs": [],
		"03 documents": [],
		"04 scripts and code": [],
		"05 archives": [],
		"06 executables": [],
		"07 project files": [],
		"09 other": []
	},
	"1 code": {
		"10 uncategorized git repos": [],
		"11 java": [],
		"12 csharp": [],
		"13 python": [],
		"14 c": [],
		"15 lua": [],
		"19 other": []
	},
	"2 media": {
		"20 pictures": [],
		"21 music": [],
		"22 video": []
		"29 other": []
	},
	"3 documents": { #if i get this to be content aware, that would be dope,
					 #but i dont think i can. for now i'm writing it as content aware though
		"30 school documents": [],
		"31 work documents": [],
		"32 personal research/general documents": [],
		"39 other": []
	}
}










# classes

class file:
	name = ""
	ext = ""
	url = ""

	def __init__(self, url):
		self.url = url
		self.name = getFileNameFromUrl(url)
		None, self.ext = getFileExtensionFromUrl(url)




# functions


def loadDb(url):
	with open(url) as json_file:
		return json.load(json_file)

def getFileNameFromUrl(url):
	return os.path.basename(url)

def getFileExtensionFromUrl(url)
	return os.path.splitext(url)









