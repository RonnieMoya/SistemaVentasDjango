import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MYSQL={
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sisventas',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',  # O la dirección IP del servidor de MySQL
        'PORT': '3306',       # El puerto por defecto de MySQL

    }
} 