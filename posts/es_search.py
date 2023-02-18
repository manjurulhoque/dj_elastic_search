from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Text, Date

connections.create_connection(hosts=["localhost"], timeout=20)


class PostDocument(Document):
    posted_date = Date()
    title = Text()
    body = Text()

    class Index:
        name = 'post_index'
