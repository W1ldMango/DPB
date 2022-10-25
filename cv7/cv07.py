from elasticsearch import Elasticsearch

INDEX_NAME = 'person'


def print_delimiter(n):
    print('\n', '#' * 10, 'Úloha', n, '#' * 10, '\n')


# Připojení k YES
# es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
# es = Elasticsearch("http://localhost:9200",verify_certs=False,basic_auth=("elastic","keks123"))
#
es = Elasticsearch(
    "https://localhost:9200",
    verify_certs=False,
    basic_auth=("elastic", "keks123")
)

# es = Elasticsearch(hosts="http://elastic:keks123@localhost:9200/")
# Kontrola zda existuje index 'person'
# if not es.indices.exists(index=INDEX_NAME):
#     # Vytvoření indexu
#     es.indices.create(index=INDEX_NAME)

# es.indices.create(index=INDEX_NAME)
# es.info()

# Index není potřeba vytvářet - pokud neexistuje, tak se automaticky vytvoří při vložení prvního dokumentu

# 1. Vložte osobu se jménem Artem
print_delimiter(1)
doc = {"name": "Artem"}
resp = es.index(index=INDEX_NAME, id=1, document=doc)

# 2. Vypište vytvořenou osobu (pomocí get a parametru id)
print_delimiter(2)
resp = es.get(index=INDEX_NAME, id=1)
print(resp['_source'])

# 3. Vypište všechny osoby (pomocí search)
print_delimiter(3)
resp = es.search(index=INDEX_NAME, query={"match_all": {}})
print(resp)


# 4. Přejmenujte vytvořenou osobu na 'Jane'
print_delimiter(4)
es.update(index=INDEX_NAME, id=1, doc={"name": "Jane"})

# 5. Smažte vytvořenou osobu
print_delimiter(5)
es.delete(index=INDEX_NAME, id=1)

# 6. Smažte vytvořený index
print_delimiter(6)
es.indices.delete(index=INDEX_NAME)


