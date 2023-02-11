from eat_it.app import ping, users, user, create_user, delete_user, update_user


def test_get_users(self):
    response = self.app.get('/users')
    self.assertEqual(response.status_code, 501)
    self.assertEqual(response.data, b'501 Not Implemented')

def test_create_user(self):
    response = self.app.post('/users', json={'username': 'john'})
    self.assertEqual(response.status_code, 201)
    self.assertEqual(response.get_json(), {'username': 'john'})

def test_update_user(self):
    response = self.app.put('/users/1', json={'username': 'john'})
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.get_json(), {'username': 'john'})
    with self.assertRaises(NotImplementedError):
        self.app.put('/users/1', json={'username': 'john'})

def test_partially_update_user(self):
    response = self.app.patch('/users/1', json={'username': 'john'})
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.get_json(), {'username': 'john'})
    with self.assertRaises(NotImplementedError):
        self.app.patch('/users/1', json={'username': 'john'})

def test_delete_user(self):
    response = self.app.delete('/users/1')
    self.assertEqual(response.status_code, 204)
    self.assertEqual(response.data, b'')
    with self.assertRaises(NotImplementedError):
        self.app.delete('/users/1')
