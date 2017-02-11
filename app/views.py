from app import app, db, models
from api import Api
from flask import jsonify, abort, request, make_response

@app.route('/api/v1/pydeas', methods=['GET'])
def index():
    all_ideas = Api.get_all_ideas(models)
    if len(all_ideas) == 0:
        return abort(404)
    else:
        return jsonify({'ideas': all_ideas}), 200

@app.route('/api/v1/pydeas/create', methods=['POST'])
def create():
    new_idea = Api.create_idea(request.args)
    if new_idea == False:
        return abort(400)
    else:
        Api.save_idea(new_idea, models, db)
        return jsonify(new_idea), 201

@app.route('/api/v1/pydeas/<int:idea_id>', methods=['PUT'])
def update(idea_id):
    updated_idea = Api.update_idea(request.args, idea_id, models, db)
    if updated_idea == False:
        return abort(400)
    else:
        return jsonify(updated_idea), 201

@app.route('/api/v1/pydeas/<int:idea_id>', methods=['GET'])
def show(idea_id):
    idea = Api.get_idea(idea_id, models)
    if idea == False:
        return abort(404)
    else:
        return jsonify(idea), 200

@app.route('/api/v1/pydeas/<int:idea_id>', methods=['DELETE'])
def destroy(idea_id):
    if Api.delete_idea(idea_id, models, db) == False:
        return abort(404)
    else:
        return jsonify({'success': 'Idea id %s successfully deleted' % idea_id}), 200

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

@app.errorhandler(400)
def not_saved(error):
    return make_response(jsonify({'error': 'Missing parameter, record not saved'}), 400)
