import Backend.globalInfo.Keys as Keys
from bson import ObjectId

def load_initial_data():
    db = Keys.dbconn
    collaborators = db['collaborators']

    # If the collection already has data, skip seeding
    if collaborators.count_documents({}) > 0:
        return

    collaborators.insert_many([
        {
            "_id": ObjectId("684e2ccde93928fc8d6c4bd0"),
            "strName": "Daniel",
            "strLastnames": "De la Cruz",
            "strRol": "Desarrollador Backend",
            "skills": [
                { "strSName": "Python", "strSLevel": "Avanzado", "numSYOE": 4 },
                { "strSName": ".Net", "strSLevel": "Básico", "numSYOE": 1 },
                { "strSName": "SQL", "strSLevel": "Intermedio", "numSYOE": 3 }
            ]
        },
        {
            "_id": ObjectId("684e2ccde93928fc8d6c4bd1"),
            "strName": "Patricia",
            "strLastnames": "Loera",
            "strRol": "Desarrolladora Mobile",
            "skills": [
                { "strSName": "Flutter", "strSLevel": "Intermedio", "numSYOE": 2 },
                { "strSName": "React Native", "strSLevel": "Intermedio", "numSYOE": 3 },
                { "strSName": "Swift", "strSLevel": "Básico", "numSYOE": 1 }
            ]
        },
        {
            "_id": ObjectId("684e2ccde93928fc8d6c4bd2"),
            "strName": "Abraham",
            "strLastnames": "Ramírez Basurto",
            "strRol": "Desarrollador Frontend",
            "skills": [
                { "strSName": "Angular", "strSLevel": "Avanzado", "numSYOE": 5 },
                { "strSName": "Ionic", "strSLevel": "Básico", "numSYOE": 1 },
                { "strSName": "React Native", "strSLevel": "Intermedio", "numSYOE": 2 }
            ]
        },
        {
            "_id": ObjectId("684e2ccde93928fc8d6c4bd3"),
            "strName": "Ana",
            "strLastnames": "Martínez",
            "strRol": "Ingeniera de Datos",
            "skills": [
                { "strSName": "SQL", "strSLevel": "Avanzado", "numSYOE": 6 },
                { "strSName": "MongoDB", "strSLevel": "Intermedio", "numSYOE": 3 },
                { "strSName": "Python", "strSLevel": "Intermedio", "numSYOE": 2 }
            ]
        },
        {
            "_id": ObjectId("684e2ccde93928fc8d6c4bd4"),
            "strName": "Salvador",
            "strLastnames": "Agredano Herrera",
            "strRol": "Desarrollador Fullstack",
            "skills": [
                { "strSName": "PHP", "strSLevel": "Intermedio", "numSYOE": 4 },
                { "strSName": "Swift", "strSLevel": "Básico", "numSYOE": 1 },
                { "strSName": "MongoDB", "strSLevel": "Básico", "numSYOE": 1 },
                { "strSName": "Angular", "strSLevel": "Avanzado", "numSYOE": 3 }
            ]
        },
        {
            "_id": ObjectId("684e2ccde93928fc8d6c4bd5"),
            "strName": "César",
            "strLastnames": "Reyes Torres",
            "strRol": "Project Manager",
            "skills": [
                { "strSName": "Otro", "strSLevel": "Avanzado", "numSYOE": 7 },
                { "strSName": "SQL", "strSLevel": "Intermedio", "numSYOE": 2 },
                { "strSName": "MongoDB", "strSLevel": "Básico", "numSYOE": 1 }
            ]
        }
    ])
    print("Initial data loaded successfully.")
