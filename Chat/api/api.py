from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://hkey:c452254k@cluster0.q5ds9.mongodb.net/users?retryWrites=true&w=majority")
db = cluster['chat']
cl = db['users']

def addUser():
    new = {
        "username":"cemal",
        "password":"123",
        "messages":[]
    }

    cl.insert_one(new)

def getAll():
    f = cl.find({})

    return f


def addMessage():
    message = {
        "from":"mehmeh ali erbil",
        "to":"abc",
        "message":"valla bak"
        }
    
    to = message["to"]

    all = getAll()

    for _ in all:
        if _["username"] == to:
            user = _
        
    userMessages = user["messages"]
    userMessages.append(message)

    cl.update_one({"username":"abc"}, {"$set":{"messages":userMessages}})

def isIn(all, fromA):
    for _ in all:
        if fromA in _:
            return True
    
    return False

def getMessages1():
    all = getAll()

    for _ in all:
        if _["username"] == "abc":
            user = _

    userMessages = user["messages"]
    allM = []

    for _ in userMessages:
        if _["from"] != "abc":
            if not isIn(allM, _["from"]):
                allM.append((_["from"], _["message"]))

    return allM

def getMsgU(u1, u2):
    all = getAll()

    for _ in all:
        if _["username"] == u1:
            user = _
    msgs = {"messages":[]}
    for _ in user["messages"]:
        if _["from"] == u2:
            msgs["messages"].append(("other", _["message"]))
        if _["to"] == u2:
            msgs["messages"].append(("you", _["message"]))
    
    return msgs

def postMessage(fromu, to, message):
    all = getAll()

    for _ in all:
        if _["username"] == fromu:
            user1 = _
        if _["username"] == to:
            user2 = _
    
    message = {
        "from":fromu,
        "to":to,
        "message":message}
    
    # İki kullanıcının mesajlar kısmına eklenecek

    messages1 = user1["messages"]
    messages2 = user2["messages"]

    messages1.append(message)
    messages2.append(message)

    cl.update_one({"username":fromu}, {"$set":{"messages":messages1}})
    cl.update_one({"username":to}, {"$set":{"messages":messages2}})
    

