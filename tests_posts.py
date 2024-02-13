from Utils.api import api
from Utils.Consts import POSTS_ENDPOINT, USERS_ENDPOINT
from Utils.helpers import generate_post_data, generate_comment_data

posts_api = api(endpoint=POSTS_ENDPOINT)
users_api = api(endpoint=USERS_ENDPOINT)

# Post 3 Posts in the following order
''' a. Post 1
        Comment 1
    b. Post 2
        Comment 2
    c. Post 3
         Comment 3'''


def test_post_diff_three_posts(req):
    user = req.get(url=users_api.api_endpoint).json()[0]
    for i in range(1, 4):
        create_post = req.post(
            url=f'{users_api.api_endpoint}/{user["id"]}/posts',
            data=generate_post_data(
                user_id=user['id'],
                title=f'Post{i}', body=f'body{i}'))
        assert create_post.status_code == 201
        create_comment = req.post(
            url=f'{posts_api.api_endpoint}/{create_post.json()["id"]}/comments',
            data=generate_comment_data(
                user_id=user['id'],
                name=user['name'],
                email=user['email'],
                title=f'Comment{i}', body=f'Comment{i}'))
        assert create_comment.status_code == 201


# Get all users posts and comment and print them in the following order:
#   Post 1
# ... (comments)
# Post2
# ... (comments)
# etc...
def test_user_posts(req):
    user = req.get(url=users_api.api_endpoint).json()[0]
    user_posts = req.get(url=f'{users_api.api_endpoint}/{user["id"]}/posts')
    posts_to_check = ['Post1', 'Post2', 'Post3']
    comments_to_check = ['Comment1', 'Comment2', 'Comment3']
    for post in user_posts.json():
        if 'Post' not in post["title"]:
            continue
        print(f'\n{post["title"]}')
        assert post["title"] in posts_to_check
        post_comments = req.get(
            url=f'{posts_api.api_endpoint}/{post["id"]}/comments')
        assert post_comments.status_code == 200
        assert post_comments.json()[0]['body'] in comments_to_check
        print('  ' + post_comments.json()[0]['body'])
