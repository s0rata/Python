class  DocType(object):
	def factory(type):
		if type=='.doc':
			return Doc()
		if type=='.pdf':
			return Pdf()
	factory = staticmethod(factory) ##what is this?

class Doc(DocType):
	def createDoc(self, name):
		print name + ".doc"
class Pdf(DocType):
	def createDoc(self, name):
		print name + ".pdf"

doc = DocType.factory('.doc')
doc.createDoc("assignment")

pdf = DocType.factory('.pdf')
pdf.createDoc("homework")