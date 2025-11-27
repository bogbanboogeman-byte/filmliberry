from flask import Flask
app = Flask(__name__)

@app.route('/register', methods=['GET'])
def user_register():
    return 'Register'

@app.post('/login')
def user_login():
    return 'Login'

@app.route('/logout', methods=['GET'])
def user_logout():
    return 'Logout'

@app.route('/user/<user_id>', methods=['GET'])
def user_profile(user_id):
    return f'User {user_id}'

@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    return f'User {user_id} deleted'

@app.route('/films', methods=['GET'])
def films():
    return 'Films'

@app.route('/films', methods=['POST'])
def add_film():
    return 'Film added'

@app.route('/films/<film_id>', methods=['GET'])
def film_info(film_id):
    return f'Film {film_id}'

@app.route('/films/<film_id>', methods=['PUT'])
def update_film(film_id):
    return f'Film {film_id} updated'

@app.route('/films/<film_id>', methods=['DELETE'])
def delete_film(film_id):
    return f'Film {film_id} deleted'

@app.route('/films/<film_id>/reting', methods=['POST'])
def film_rating(film_id):
    return f'Film {film_id} rated'

@app.route('/films/<film_id>/reting', methods=['GET'])
def film_rating_info(film_id):
    return f'Film {film_id} rating'

@app.route('/films/<film_id>/reting<feedback_id>', methods=['DELETE'])
def film_rating_delete(film_id, feedback_id):
    return f'Film {film_id} rating {feedback_id} deleted'

@app.route('/films/<film_id>/reting/<feedback_id>', methods=['PUT'])
def film_rating_update(film_id, feedback_id):
    return f'Film {film_id} rating {feedback_id} updated'


@app.route('/films/<film_id>/reting/<feedback_id>/feedback', methods=['GET'])
def film_rating_feedback(film_id, feedback_id):
    return f'Film {film_id} rating {feedback_id} feedback'


@app.route('/users/<user_id>/list', methods=["GET", 'POST'])
def user_list(user_id):
    return f'User {user_id} list'


@app.route('/users/<user_id>/list' , methods=["DELETE"])
def user_list_delete(user_id):
    return f'User {user_id} list deleted'

@app.route('/users/<user_id>/list/<list_id>', methods=["GET", "POST"])
def user_list_item(user_id, list_id):
    return f'User {user_id} list item {list_id}'

@app.route('/users/<user_id>/list/<list_id>/<film_id>', methods=["DELETE"])
def user_list_item_delete(user_id, list_id, film_id):
    return f'User {user_id} list item {list_id} film {film_id} deleted'

if __name__ == '__main__':
    app.run()

