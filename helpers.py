import uuid


def generate_user_data():
    unique_name = f"DimaGurevich_{uuid.uuid4()}"
    unique_email = f"gurevich@{uuid.uuid4()}"
    return '{"name":"%s", "gender":"male", "email":"%s", ' \
           '"status":"active"} ' % (unique_name, unique_email)


def generate_post_data(user_id, title, body):
    return '{"user_id": "%s", "title": "%s", "body": "%s"}' \
           % (user_id, title, body)


def generate_comment_data(user_id, name, email, title, body):
    return '{"user_id": "%s","name": "%s","email":"%s", "title": "%s", "body": "%s"}' \
           % (user_id, name, email, title, body)
