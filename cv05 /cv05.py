import datetime
from init import collection

print(collection.find_one())

'''
DPB - 5. Cvičení

Implementujte jednotlivé body pomocí PyMongo knihovny - rozhraní je téměř stejné jako v Mongo shellu.
Před testováním Vašich řešení si nezapomeňte zapnout Mongo v Dockeru.

Pro pomoc je možné např. použít https://www.w3schools.com/python/python_mongodb_getstarted.asp

Funkce find vrací kurzor - pro vypsání výsledku je potřeba pomocí foru iterovat nad kurzorem:

cursor = collection.find(...)
for restaurant in cursor:
    print(restaurant) # případně print(restaurant['name'])

Všechny výsledky limitujte na 10 záznamů. Nepoužívejte české názvy proměnných!
'''


def print_delimiter(n):
    print('\n', '#' * 10, 'Úloha', n, '#' * 10, '\n')

# 1. Vypsání všech restaurací 
print_delimiter(1)
# for x in collection.find():
#     print(x)
# 2. Vypsání všech restaurací - pouze názvů, abecedně seřazených
print_delimiter(2)
# x = collection.find().sort("name",1)
# for i in x:
#     print(i)
# 3. Vypsání pouze 10 záznamů z předchozího dotazu
print_delimiter(3)
# x.limit(10)
# for i in x:
#     print(i)
# 4. Zobrazte dalších 10 záznamů
print_delimiter(4)
# x.skip(10).limit(10)
# for i in x:
#     print(i)

# 5. #Vypsání restaurací ve čtvrti Bronx (čtvrť = borough)
print_delimiter(5)
# x = collection.find({"borough":"Bronx"})
# for i in x:
#     print(i)

# 6. Vypsání restaurací, jejichž název začíná na písmeno M
print_delimiter(6)
# x = collection.find({"name": {"$regex": "^M"}}).limit(10)
# for i in x:
#     print(i)


# 7. Vypsání restaurací, které mají skóre větší než 80
print_delimiter(7)
# x = collection.find({"grades.score": {"$gt": 80}})
# for i in x:
#     print(i)

# 8. Vypsání restaurací, které mají skóre mezi 80 a 90
print_delimiter(8)

# x = collection.find({"grades" : { "$elemMatch":{"score":{"$gt" : 80 , "$lt" :90}}}})
# for i in x:
#     print(i)

'''
Bonusové úlohy:
'''

# 9. Vypsání všech restaurací, které mají skóre mezi 80 a 90 a zároveň nevaří americkou (American) kuchyni
print_delimiter(9)
# x = collection.find({"grades" : { "$elemMatch":{"score":{"$gt" : 80 , "$lt" :90}}, {"cuisine": {"$ne":"American"}}}})
# x = collection.find({
#     "$and": [
#         {
#             "grades" : { "$elemMatch":{"score":{"$gt": 80, "$lt": 90}}}
#         },
#         {
#             "cuisine": {"$ne": 'American '}
#         }
#     ]
# })
# for i in x:
#     print(i)


# 10. Vypsání všech restaurací, které mají alespoň osm hodnocení
print_delimiter(10)
# x = collection.aggregate([
#     {
#         "$match": {
#             "grades": {
#                 "$gte": {
#                     "$size":8
#                 }
#             }
#
#         }
#     }
# ])
# x = collection.find({'grades.7': {'$exists': 'true'}})
# for i in x:
#     print(i)



# 11. Vypsání všech restaurací, které mají alespoň jedno hodnocení z roku 2014 
print_delimiter(11)
# x = collection.find({
#     "grades":
#         {
#             "$elemMatch":
#                 {
#                     "date":
#                         {
#                             "$gte": datetime.datetime(2014,1,1)
#                         }
#                 }
#         }
# })
# for i in x:
#     print(i)

'''
V této části budete opět vytvářet vlastní restauraci.

Řešení:
Vytvořte si vaši restauraci pomocí slovníku a poté ji vložte do DB.
restaurant = {
    ...
}
'''

# 12. Uložte novou restauraci (stačí vyplnit název a adresu)
print_delimiter(12)
# collection.insert_one( { "name": "My First try", "restaurant_id": "1"})



# 13. Vypište svoji restauraci
print_delimiter(13)
# x = collection.find_one({"restaurant_id":"1"})
# print(x)

# 14. Aktualizujte svoji restauraci - změňte libovolně název
print_delimiter(14)
# collection.update_one(
#     {
#         "name": "My First try"
#     },
#     {
#         "$set":
#             {
#                 "name": "Changed"
#             }
#     }
# )


print_delimiter(15)
# 15. Smažte svoji restauraci
# 15.1 pomocí id (delete_one)
# collection.delete_one({
#     "restaurant_id": 1
# })
# # 15.2 pomocí prvního nebo druhého názvu (delete_many, využití or)
# x = collection.delete_many({
#     "name": {"$regex": "ˆMy"}
# })





'''
Poslední částí tohoto cvičení je vytvoření jednoduchého indexu.

Použijte např. 3. úlohu s vyhledáváním čtvrtě Bronx. První použijte Váš již vytvořený dotaz a na výsledek použijte:

cursor.explain()['executionStats'] - výsledek si vypište na výstup a všimněte si položky 'totalDocsExamined'

Poté vytvořte index na 'borough', zopakujte dotaz a porovnejte hodnoty 'totalDocsExamined'.

S řešením pomůže https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.create_index
'''
print_delimiter(16)
# x = collection.find({"borough":"Bronx"}).explain()['executionStats']
# collection.create_index("borough")
# x1 = collection.find({"borough":"Bronx"}).explain()['executionStats']
#
# print(x)
# print(x1)