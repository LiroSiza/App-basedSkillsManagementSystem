from flask import jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId # Import ObjectId for MongoDB document IDs
import Backend.globalInfo.Keys as Keys
import Backend.globalInfo.ResponseMessages as ResponseMessages

# Initialize MongoDB connection if not already done - No Auth
if Keys.dbconn == None:
    mongoConnection = MongoClient(Keys.strConnection)   # Client
    Keys.dbconn = mongoConnection[Keys.strDBConnection] # Database
    dbConnSMS = Keys.dbconn['collaborators']            # Collection
else:
    dbConnSMS = Keys.dbconn['collaborators']            # Collection


def getAllCollaborators():
    try:
        response = dbConnSMS.find()  # Fetch all collaborators documents
        print("Response from DB (GET ALL COLLABORATORS):", response)
        if response is None:
            return ResponseMessages.err472
        return list(response)  # Convert cursor to list
    except Exception as e:
        print(f"Error fetching colaborators: {e}")
        return jsonify(ResponseMessages.err500)
    
def getCollaboratorById(colaboratorId):
    try:
        response = dbConnSMS.find_one({ "_id" : ObjectId(colaboratorId) })
        print("Response from DB (GET COLLABORATOR):", response)
        if response is None:
            return ResponseMessages.err472
        return response
    except Exception as e:
        print(f"Error fetching collaborator: {e}")
        return jsonify(ResponseMessages.err500)
    
def postCollaborator(strName, strLastnames, strRol):
    try:
        newCollaborator = {
            "strName": strName,
            "strLastnames": strLastnames,
            "strRol": strRol,
            "skills": [],
        }
        result = dbConnSMS.insert_one(newCollaborator)
        return jsonify({
            "status": ResponseMessages.succ200,
            "data": {"_id": str(result.inserted_id)}
        }), 201
    except Exception as e:
        print(f"Error inserting collaborator: {e}")
        return jsonify(ResponseMessages.err500)

def putCollaborator(collaboratorId, strName, strLastnames, strRol):
    try:
        updateData = {
            "strName": strName,
            "strLastnames": strLastnames,
            "strRol": strRol
        }
        result = dbConnSMS.update_one(
            {"_id": ObjectId(collaboratorId)},
            {"$set": updateData}
        )
        if result.modified_count > 0:
            return jsonify({
                "status": ResponseMessages.succ200,
                "data": {"modified_count": result.modified_count}
            }), 200
        else:
            return jsonify(ResponseMessages.err472)
    except Exception as e:
        print(f"Error updating collaborator: {e}")
        return jsonify(ResponseMessages.err500)
    
def deleteCollaboratorById(collaboratorId):
    try:
        result = dbConnSMS.delete_one({ "_id": ObjectId(collaboratorId) })
        print("Delete Result function:", result)
        return result
    except Exception as e:
        print(f"Error deleting collaborator: {e}")
        return jsonify(ResponseMessages.err500)