from init import collection

print(collection.find_one())


def print_delimiter(n):
    print('\n', '#' * 10, 'Úloha', n, '#' * 10, '\n')


print_delimiter(1)

# x = collection.aggregate([
#     {
#         "$group":
#             {
#                 "_id": "$address.zipcode",
#                 "counter": {"$sum": 1}
#             }
#     },
#     {
#         "$match":
#             {
#                 "counter": {"$gt": 1},
#             }
#     },
#     {
#         # "$sort": {"counter": -1}
#         "$sort": {"_id": 1}
#     },
#     {
#         "$limit": 10
#     }
# ])
#
# for i in x:
#     print(i)

print_delimiter(2)

# x = collection.aggregate([
#     {
#         "$project":
#             {
#                 "avg": {"$avg":"$grades.score"}
#             }
#     },
#     {
#         "$limit":10
#     }
#
# ])
x = collection.aggregate([
    {
        "$unwind": "$grades"
    },
    {
        "$group":
            {
                "_id":"$grades.grade",
                "avg": {"$avg":"$grades.score"}
            }
    },
    {
        "$match":
            {
                "_id": {"$ne": "Not Yet Graded"}
            }
    }
])
for i in x:
    print(i)

print_delimiter(3)
# var map = function(){emit(this.address.zipcode,1)}
# var reduce = function(key,values){return Array.sum(values)}
# db.restaurants.mapReduce(map,reduce,{out:"first"})
# db.first.find().sort({_id:1})

print_delimiter(4)

# x = collection.aggregate([
#     {
#         "$project":
#             {
#                 # "grades.score": "A",
#                 "count_of_grades": { "$cond": { "if": { "$isArray": "$grades" }, "then": { "$size": "$grades" }, "else": "NA"} },
#                 "avg": {"$avg":"$grades.score"}
#
#
#             }
#     },
#     {
#         "$match":
#             {
#                 "count_of_grades": {"$gte":3}
#             }
#     },
#     {
#         "$sort": {"avg":-1}
#
#     },
#     {
#         "$limit":5
#     }
# ])
#
# for i in x:
#     print(i)


print_delimiter(5)
# x = collection.aggregate([
#     {
#         "$unwind": "$grades"
#     },
#     {
#         "$group":
#             {
#                 "_id":"$cuisine",
#                 "avg": {"$avg":"$grades.score"},
#             }
#     },
# ])
#
# for i in x:
#     print(i)


