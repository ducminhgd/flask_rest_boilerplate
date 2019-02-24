import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'), override=True)

DEBUG = os.environ.get('DEBUG') == 'True'

SECRET_KEY = 'r9PF/D1xlZR0L`o7q*p0xF1is7BCjt}y{Zs:+hC}S4rfD9++6sd{%%Bq|!Kq'

SQLALCHEMY_BINDS = {
    'default': 'mysql+mysqldb://root:mysql@127.0.0.1:3306/flask_rest_boilerplate',
}

if __name__ == '__main__':
    print(SECRET_KEY)
