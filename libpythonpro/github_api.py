import requests


def buscar_avatar(usuario):
    """
    Busca o avatar de um usuário no Github

    :param usuario: str com o nome de usuário no github
    :return: str com o link do avatar
    """
    # no exercício, o Renzo copia a url direto da api e muda esta url pelo atributo da função.
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']

if __name__ == '__main__':
    print(buscar_avatar('GetulioCastro'))
