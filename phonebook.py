#phonebook using python and mongodb crud operations
import pymongo
import time as tm

#mongodb connection details
pbclient=pymongo.MongoClient("mongodb://localhost:27017/")

pbdb=pbclient["mydatabase"]

#check if collection exists , if exists then drop
collist = pbdb.list_collection_names()

if("phonebook" in collist):
  pbdb.collection.drop()

#create collection
pbcol=pbdb["phonebook"]


#empty dictionary to store name and number
pbdict={}

print("...Phonebook Mongo...")

#select the operation
def choice():
  print("\n 1 : Add \n 2 : Search \n 3 : Delete \n 4 : Delete all \n 5 : View all \n 6 : Quit")
  ch=int(input("Enter your choice: "))
  return ch

#insert new record
def pbadd():
  nm = input("Enter name: ")
  for i in nm:
    if(i.isdigit()=='True'):
      print("Please Enter a valid name")
      nm = input("Enter name: ")
  no = int(input("Enter number: "))
  if(len(str(no))!=10):
    print("Please Enter a valid 10 digit number")
    no=int(input("Enter number: "))
  pbdict["name"] = nm
  pbdict["phone"] = no
  pbaddc = pbcol.insert_one(pbdict)
  print("Successfully added", nm)
  addy = input("Add more? y/n: ")
  if (addy == 'y'):
    pbadd()
  #else:
    #return

#find record
def pbsearch():
  nmf = input("Enter name to search: ")
  fin = pbcol.find({"name": nmf}, {"_id": 0, "name": 1, "phone": 1})
  for i in fin:
    print(i)

#delete record
def pbdelete():
  nmd = input("Enter name to delete: ")
  pbd = pbcol.delete_one({"name": nmd})
  print(pbd.deleted_count, "record deleted")

#delete all records
def pbdeleteall():
  pbda=pbcol.delete_many({})
  print(pbda.deleted_count,"records deleted")

#main function
while True:
  ch=choice()
  if(ch==1):
    pbadd()

  if(ch==2):
    pbsearch()

  if(ch==3):
    pbdelete()

  if(ch==4):
    pbdeleteall()

#view all records
  if(ch==5):
    pbv=pbcol.find({},{"_id":0,"name":1,"phone":1})
    res=list(pbv)
    if len(res)==0:
      print("No records found")
      flag_in=input("Would you like to add records? y/n ")
      if flag_in=='y':
        pbadd()
    for i in res:
      print(i)

#sleep 5sec so that it looks likr we are exiting
  if(ch==6):
    print("Exiting...")
    tm.sleep(5)
    break
