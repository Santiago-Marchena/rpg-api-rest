from flask import Blueprint,request,jsonify
import services
from utils import validate_character

bp = Blueprint("routes",__name__)

@bp.route("/characters",methods=["POST"])
def create():
    data=request.json
    err=validate_character(data)
    if err:
        return jsonify({"error":err}),400
    c=services.create_character(data)
    return jsonify(c.to_dict()),201

@bp.route("/characters",methods=["GET"])
def get_all():
    return jsonify([c.to_dict() for c in services.get_all()])

@bp.route("/characters/<int:id>",methods=["GET"])
def get_one(id):
    c=services.get_by_id(id)
    if not c:
        return jsonify({"error":"Not found"}),404
    return jsonify(c.to_dict())

@bp.route("/characters/<int:id>",methods=["PUT"])
def update(id):
    c=services.update_character(id,request.json)
    if not c:
        return jsonify({"error":"Not found"}),404
    return jsonify(c.to_dict())

@bp.route("/characters/<int:id>",methods=["DELETE"])
def delete(id):
    services.delete_character(id)
    return jsonify({"msg":"deleted"})

@bp.route("/battle",methods=["POST"])
def battle():
    data=request.json
    res=services.battle(data.get("id1"),data.get("id2"))
    if not res:
        return jsonify({"error":"Invalid"}),404
    return jsonify(res)
