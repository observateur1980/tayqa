
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEBUG = False
ALLOWED_HOSTS = ['www.tayqa.com', 'tayqa.com', '173.255.210.251']
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
