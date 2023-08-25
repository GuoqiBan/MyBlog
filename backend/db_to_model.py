import os
os.system(f'sqlacodegen mysql+pymysql://{"root"}:{"123456"}@{"localhost"}:{"3306"}/{"online_blog"}?charset=utf8mb4 > app/common/models.py')