from src.routes import *

def test_all_colors():
    response = app.test_client().get('/colors/all')
    
    assert response.status_code == 200
    assert response.json == {'cmyk': ['cyan', 'magenta', 'yellow', 'black'], 'rgb': ['red', 'green', 'blue']}
    
def test_cmyk_colors():
    response = app.test_client().get('/colors/cmyk')
    
    assert response.status_code == 200
    assert response.json == {'cmyk': ['cyan', 'magenta', 'yellow', 'black']}
    
def test_rgb_colors():
    response = app.test_client().get('/colors/rgb')
    
    assert response.status_code == 200
    assert response.json == {'rgb': ['red', 'green', 'blue']}
    
def test_wrong_colors():
    response = app.test_client().get('/colors/xyz')
    
    assert response.status_code == 200
    assert response.json == {'xyz': None}
    
def test_none_colors():
    response = app.test_client().get('/colors/')
    
    assert response.status_code == 404