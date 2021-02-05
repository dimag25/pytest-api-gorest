import base64


class api:
    def __init__(self, userName, password):
        # for docker need to use : host.docker.internal , for your local machine : localhost.
        self.apiUrl = 'http://host.docker.internal:8000/players?page={0}'
        self.setAuthorization(userName, password)

    '''
    should work only admin:admin pair.
    '''
    def setAuthorization(self, userName, password):
        self.userName = userName
        self.password = password
        authPair = ('{0}:{1}'.format(userName, password))
        message_bytes = authPair.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        self.authorization = "Basic {0}".format(str(base64_bytes.decode('ascii')))
