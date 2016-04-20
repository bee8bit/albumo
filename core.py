class Image:
	"""Describes an image of any kind. Does not necessarily contain the image pixels themselves."""
	
	def __init__(self):
		self.id = None
		self.name = None
		self.metadata = {
			'creator': None,
			'summary': None,
			'resolution': {},
			'created': None,
			'modified': None
		}

	
	def __repr__(self):
		return 'Image "%s" (%s)' % (self.name, self.id)
		



class Catalog:
	"""Any list of images. May be a file system directory, a search result, ...
	May reference to Image objects in other catalogs(?)"""
	
	def __init__(self):
		self.id = '2'
		self.images = []
		self.parentCatalog = None
	
	
	def getImage(self, id):
		raise NotImplementedError


