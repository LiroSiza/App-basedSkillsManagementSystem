from flask import Blueprint, request, jsonify
import Backend.globalInfo.ResponseMessages as ResponseMessages
import Backend.functions.collaboratorsFunctions as collaboratorsFunctions

colaboratorBP = Blueprint('collabBP', __name__, url_prefix='/api/collaborator')

@colaboratorBP.get('/')
def getCollaborators():
    """
    Obtener todos los colaboradores
    ---
    tags:
      - Collaborators
    responses:
      200:
        description: Lista de colaboradores obtenida correctamente
        schema:
          type: object
          properties:
            status:
              type: object
            data:
              type: array
              items:
                type: object
      404:
        description: No se encontraron colaboradores
      500:
        description: Error interno del servidor
    """
    try:
        collaboratorsInfo = collaboratorsFunctions.getAllCollaborators()

        if not collaboratorsInfo:
            return jsonify(ResponseMessages.err472)

        for collaborator in collaboratorsInfo:
            if '_id' in collaborator:
                collaborator['_id'] = str(collaborator['_id'])

        return jsonify({
            "status": ResponseMessages.succ200,
            "data": collaboratorsInfo
        }), 200

    except Exception as e:
        print(f"Error fetching collaborators: {e}")
        return jsonify(ResponseMessages.err500)


@colaboratorBP.get('/<collaboratorId>')
def getCollaboratorsById(collaboratorId):
    """
    Obtener un colaborador por ID
    ---
    tags:
      - Collaborators
    parameters:
      - name: collaboratorId
        in: path
        type: string
        required: true
        description: ID del colaborador
    responses:
      200:
        description: Colaborador encontrado
        schema:
          type: object
          properties:
            status:
              type: object
            data:
              type: object
      404:
        description: Colaborador no encontrado
      500:
        description: Error interno del servidor
    """
    try:
        if not collaboratorId:
            return jsonify(ResponseMessages.err203)

        collaboratorInfo = collaboratorsFunctions.getCollaboratorById(collaboratorId)

        if not collaboratorInfo:
            return jsonify(ResponseMessages.err472)

        if '_id' in collaboratorInfo:
            collaboratorInfo['_id'] = str(collaboratorInfo['_id'])

        return jsonify({
            "status": ResponseMessages.succ200,
            "data": collaboratorInfo
        }), 200

    except Exception as e:
        print(f"Error fetching collaborator: {e}")
        return jsonify(ResponseMessages.err500)


@colaboratorBP.post('/')
def postCollaborator():
    """
    Crear un nuevo colaborador
    ---
    tags:
      - Collaborators
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - strName
            - strLastnames
            - strRol
          properties:
            strName:
              type: string
            strLastnames:
              type: string
            strRol:
              type: string
    responses:
      201:
        description: Colaborador creado exitosamente
        schema:
          type: object
          properties:
            status:
              type: object
            data:
              type: object
      400:
        description: Datos de entrada incompletos
      500:
        description: Error interno del servidor
    """
    try:
        requestData = request.get_json()
        if not requestData:
            return jsonify(ResponseMessages.err472)

        if 'strName' not in requestData or 'strLastnames' not in requestData or 'strRol' not in requestData:
            return jsonify(ResponseMessages.err203)

        print("Request Data for POST Collaborator:", requestData)
        result = collaboratorsFunctions.postCollaborator(
            requestData['strName'],
            requestData['strLastnames'],
            requestData['strRol']
        )

        return result

    except Exception as e:
        print(f"Error processing POST collaborator request: {e}")
        return jsonify(ResponseMessages.err500)


@colaboratorBP.put('/')
def putCollaborator():
    """
    Actualizar un colaborador
    ---
    tags:
      - Collaborators
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - _id
            - strName
            - strLastnames
            - strRol
          properties:
            _id:
              type: string
            strName:
              type: string
            strLastnames:
              type: string
            strRol:
              type: string
    responses:
      200:
        description: Colaborador actualizado exitosamente
        schema:
          type: object
          properties:
            status:
              type: object
            data:
              type: object
      400:
        description: Datos de entrada incompletos
      404:
        description: Colaborador no encontrado
      500:
        description: Error interno del servidor
    """
    try:
        requestData = request.get_json()
        if not requestData:
            return jsonify(ResponseMessages.err472)

        if '_id' not in requestData or 'strName' not in requestData or 'strLastnames' not in requestData or 'strRol' not in requestData:
            return jsonify(ResponseMessages.err203)

        print("Request Data for PUT Collaborator:", requestData)
        result = collaboratorsFunctions.putCollaborator(
            requestData['_id'],
            requestData['strName'],
            requestData['strLastnames'],
            requestData['strRol']
        )

        return result

    except Exception as e:
        print(f"Error processing PUT collaborator request: {e}")
        return jsonify(ResponseMessages.err500)


@colaboratorBP.delete('/<collaboratorId>')
def deleteCollaboratorById(collaboratorId):
    """
    Eliminar un colaborador por ID
    ---
    tags:
      - Collaborators
    parameters:
      - name: collaboratorId
        in: path
        type: string
        required: true
        description: ID del colaborador a eliminar
    responses:
      200:
        description: Colaborador eliminado exitosamente
        schema:
          type: object
          properties:
            status:
              type: object
            data:
              type: object
      404:
        description: Colaborador no encontrado
      500:
        description: Error interno del servidor
    """
    try:
        if not collaboratorId:
            return jsonify(ResponseMessages.err203)

        deleteResult = collaboratorsFunctions.deleteCollaboratorById(collaboratorId)
        print("Delete Result direction:", deleteResult)

        if deleteResult is None or deleteResult.deleted_count == 0:
            return jsonify(ResponseMessages.err472)

        result_data = {"deleted_count": deleteResult.deleted_count}
        return jsonify({
            "status": ResponseMessages.succ200,
            "data": result_data
        }), 200

    except Exception as e:
        print(f"Error processing DELETE collaborator request for {collaboratorId}: {e}")
        return jsonify(ResponseMessages.err500), 500
