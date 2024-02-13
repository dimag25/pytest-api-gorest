## Project for tests in pytest for free public API endpoints.

## Check api https://gorest.co.in/  and read the api docs

`tests_users.py` related to `https://gorest.co.in/public/v2/users`
- Add user then get the user to see of all the details are correct.
- Update your user and change the name, then get and see if all the details are correct.
- Select 10 random distinct users and print their names.
- Iterate the users and print how many unique names there are, and how many users have
the same name, sorted from the biggest to smallest.
    For example:
    Total unique names: 89
    Dima_XYZ : 1
    Dima_XYZ_1234: 1

`tests_posts.py` related to `https://gorest.co.in/public/v2/posts`
- Post 3 Posts in the following order
    a. Post 1
    b. Post 2
    i. Comment 1
    ii. Comment 2
    c. Post 3
    i. Comment 3
- Get all users post and comment and print them in the same format as previous section.



## Project Setup

### Step 1: Clone the project

```bash
git clone https://github.com/dimag25/pytest-api-gorest.git
cd pytest-api-gorest
```


### Step 2: `Local Run prerequisites`
`Run via docker from any OS ( Win/Mac/Linux )`

- Build : 
`docker build -t pytest-api-gorest .`

- Run : 
`docker run -v ./:/pytest-api-gorest  pytest-api-gorest`


### View Results Locally:
- See tests result report inside `/result.xml`

Enjoy! :)
