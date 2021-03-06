from trakt.interfaces.base import Interface


class AuthInterface(Interface):
    path = 'auth'

    def login(self, login, password):
        response = self.http.post('login', data={
            'login': login,
            'password': password
        })

        data = self.get_data(response)

        if not data:
            return None

        return data.get('token')

    def logout(self):
        pass
