import json


class ConfigManager:
    path_to_app_json = "config/app.json"

    @staticmethod
    def get_secret_key_from_app(key_string: str = "SECRET_KEY") -> str:
        path_to_file = ConfigManager.path_to_app_json
        with open(path_to_file) as file:
            try:
                templates = dict(json.load(file))
                return templates.get(key_string)
            except:
                raise Exception(f"Не удалось прочитать содержимое файла находящимся по пути {path_to_file}")
