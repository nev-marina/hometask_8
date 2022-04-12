import requests


class YaUploader:
    def __init__(self, _token: str):
        self.token = _token

    def upload(self, file_path):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        filename = file_path.split('/', )[-1]
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": f"Загрузки/{filename}", "overwrite": "true"}
        responсe = requests.get(url, headers=headers, params=params).json()
        href = responсe.get("href", "")
        responce_ = requests.put(href, data=open(file_path, 'rb'))
        if responce_.status_code == 201:
            return 'Успешно'
        else:
            return f"Ошибка загрузки! Код ошибки: {responce_.status_code}"


if __name__ == '__main__':
    path_to_file = '/Users/marinanevskaya/Desktop/Дз 9/Test2.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)
