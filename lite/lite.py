import requests


class Setup:
    def __init__(self, name, author, description, version, filename):
        self.name = name
        self.author = author
        self.description = description
        self.version = version
        self.filename = filename

    def register(self):
        files = {'file': open(self.filename, 'r')}
        info = {
            "name": self.name,
            "author": self.author,
            "description": self.description,
            "version": self.version
        }
        requests.post(f"https://rcyclegar.pythonanywhere.com/register/{self.name}", files=files)
        requests.post(f"https://rcyclegar.pythonanywhere.com/register-info/{self.name}", data=info)
        print(f"Module {self.name} successfully registered!")
