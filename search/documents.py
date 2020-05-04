from django_elasticsearch_dsl import Document, Index#, DocType
from products.models import Product

_index = Index('prods')


@_index.doc_type
class ProdDocument(Document):
	class Django:
		model = Product

		fields = [
			'name',
			'description'
		]