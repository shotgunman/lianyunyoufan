# lianyouyunfan联云游帆
后端说明：  
使用框架django完成后端  
python使用  
3.10  
第三方库版本使用  
Package           Version  
----------------- -------
asgiref           3.7.2  
Django            5.0.1  
mysql-client      0.0.1  
mysqlclient       2.2.1  
pip               23.2.1  
setuptools        68.2.0  
sqlparse          0.4.4  
typing_extensions 4.9.0  
tzdata            2023.4  
wheel             0.41.2  
**没有上传虚拟环境，同时由于django框架的局限性，你还需要单独建立数据库，这个在setting.py中有对数据库的描述**
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lyyf', # my database name
        'USER': 'root',
        'PASSWORD':'123456',
        'HOST':'localhost',
        'POST':3306,
    }
}
```
在你的mysql数据库中执行以下指令(前提是你已经登录本地数据库)  
在打开项目文件后的使用  
在本地数据库已经登录情况下,数据库创建  
```
 CREATE DATABASE lyyf CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```  
在项目根目录之下执行，建立数据库的表  
```
python manage.py migrate 
```
```
python manage.py makemigrations 
```
运行  
```
python manage.py runserver 
```


