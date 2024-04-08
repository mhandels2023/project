from flask import Blueprint, jsonify, request

bp = Blueprint('api', __name__, url_prefix='/api')

posts = [
    {"id": 1, "title": "First post", "content": "Content of the first post"},
    {"id": 2, "title": "Second post", "content": "Content of the second post"}
]
next_id = 3

@bp.route('/dummy', methods=['GET'])
def dummy_endpoint():
    return jsonify({"message": "This is a dummy endpoint"}), 200

@bp.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts), 200

@bp.route('/posts', methods=['POST'])
def create_post():
    global next_id
    data = request.json
    data['id'] = next_id
    next_id += 1
    posts.append(data)
    return jsonify(data), 201

@bp.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.json
    for post in posts:
        if post['id'] == post_id:
            post.update(data)
            return jsonify(post), 200
    return jsonify({"error": "Post not found"}), 404

@bp.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    posts = [post for post in posts if post['id'] != post_id]
    return jsonify({"message": "Post deleted"}), 200

def configure_routes(app):
    app.register_blueprint(bp)
