Tests in pytest for GRAPHQL free public API

1. https://gorest.co.in/  and read the api docs
2. Add user then get the user to see of all the details are correct.
3. Update your user and change the name, then get and see if all the details are correct.
4. Select 10 random distinct users and print their names.
5. Iterate the users and print how many unique names there are, and how many users have
the same name, sorted from the biggest to smallest.
a. For example:
i. Total unique names: 89
    Dima_XYZ : 1
    Dima_XYZ_1234: 1

6. Post 3 Posts in the following order
a. Post 1
b. Post 2
i. Comment 1
ii. Comment 2
c. Post 3
i. Comment 3

7. Get all users post and comment and print them in the same format as in section 6
Note: Use the get command to find out the right body for the Post/Patch commands

Token:
e2684965e4b313ee7b8e465d36c0bd4815561c6a16840d99eb9f83714077e365

How to run?

`pytest {test_files.py}`
i.e : `pytest tests_posts.py tests_users.py`
