import pytest

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_non_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 42

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

@pytest.mark.myapi
def test_emojis(github_api):
    """Emoji 'ukraine' is available to use on GitHub."""
    r = github_api.emojis()
    assert 'ukraine' in r.keys()

@pytest.mark.myapi
def test_root(github_api):
    """Links to resource 'current_user_url' in GitHub"""
    r = github_api.root()
    assert r["current_user_url"] == "https://api.github.com/user"

@pytest.mark.myapi
def test_root(github_api):
    """Template for Gitignore for Android is in list of ignore-templates"""
    r = github_api.gitignore()
    assert "Android" in r

@pytest.mark.myapi
def test_get_a_code_of_conduct(github_api):
    """Return information about the specified GitHub code of conduct."""
    r = github_api.get_a_code_of_conduct("contributor_covenant")
    assert r["url"] == "https://api.github.com/codes_of_conduct/contributor_covenant"
  