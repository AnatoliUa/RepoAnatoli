import requests

class GitHub:
    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()
        return body
    
    def search_repo(self, name):
        r = requests.get('https://api.github.com/search/repositories', params={"q": name})
        body = r.json()
        return body
    
    def people_user_follows(self):
        token = 'Bearer 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'
        hdr = {'Accept': 'application/vnd.github+json', 'Authorization': token}
        #r = requests.get(f'https://api.github.com/user/following/{username}', {'Authorization': token})
        r = requests.get(f'https://api.github.com/user/following', headers=hdr)
        return r
    
    def emojis(self):
        r = requests.get('https://api.github.com/emojis')
        body = r.json()
        return body
    
    def root(self):
        r = requests.get('https://api.github.com/')
        body = r.json()
        return body
    
    def gitignore(self):
        r = requests.get('https://api.github.com/gitignore/templates')
        body = r.json()
        return body
    