# PlayOnLinux

Site de ajuda à instalação de pacotes via PlayOnLinux

1. Abrir um terminal no mesmo diretório onde está o arquivo `requirements.txt`.

1. Se ainda não existir, criar o ambiente virtual: `python3 -m venv venv`.

1. Ativar o ambiente virtual: `source venv/bin/activate`.

1. Se ainda não tiver sido instalado, instalar os requisitos: `pip install -r requirements.txt`.

1. Se ainda não tiver feito a migração do banco de dados, implementar a migração: `python3 manage.py migrate`.

1. Colocar o site no ar: `python3 manage.py runserver`.

1. Visitar o site.

> Para mais detalhes de uso, consultar o arquivo `src/PlayOnLinux/templates/index.html`.