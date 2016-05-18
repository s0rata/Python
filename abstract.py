class Document:
	def __init__(self,type):
		self.type=type

	def show(self):
		raise NotImplementedError("Subclass must implement abstract class")

class Pdf(Document):
	def show(self):
		return "PDF document"

class Word(Document):
	def show(self):
		return "Word document"

pdf = Pdf("doc1")
word = Word("doc2")


print pdf.show()
print word.show()
