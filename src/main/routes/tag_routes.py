from flask import Blueprint, request, jsonify

tag_routes_bp = Blueprint('tags_routes', __name__)

@tag_routes_bp.route('/create_tag', methods=["POST"])

def create_tag():
    print(request.json)
    return jsonify({"response": "ok"}), 200
