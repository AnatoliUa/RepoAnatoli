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
    
    def emojis(self):
        """List all the emojis available to use on GitHub."""
        r = requests.get('https://api.github.com/emojis')
        body = r.json()
        return body
    
    def root(self):
        """Get links to resources accessible in GitHub's REST API."""
        r = requests.get('https://api.github.com/')
        body = r.json()
        return body
    
    def gitignore(self):
        """List all templates available to pass as an option when creating a repository."""
        r = requests.get('https://api.github.com/gitignore/templates')
        body = r.json()
        return body
    
    def get_a_code_of_conduct(self, key):
        """Return information about the specified GitHub code of conduct."""
        r = requests.get(f'https://api.github.com/codes_of_conduct/{key}')
        body = r.json()
        return body
    