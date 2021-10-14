import app


class TestApp:
    def test_get_pokemon(self):
        assert "pikachu" == app.get_pokemon(25)
