from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.tag_creator_view import TagCreatorView
from src.errors.error_handler import handler_errors

tag_routes_bp = Blueprint('tags_routes', __name__)

@tag_routes_bp.route('/create_tag', methods=["POST"])

def create_tag():
    response = None
    try:
        tag_creator_view = TagCreatorView()
        http_request = HttpRequest(body=request.json)
        response = tag_creator_view.authenticate_and_create(http_request=http_request)
    except Exception as exception:
        response = handler_errors(exception)
    return jsonify(response.body), response.status_code
