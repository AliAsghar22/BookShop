# BookShop

بسم الله الرحمن الرحیم

پروژه پایانی مهندسی نرم  2

اینجا میتونید پروژه فروشگاه آنلاین کتاب رو که برای درس مهندسی نرم 2 نوشتیم ببینید.

 این پروژه بر اساس جنگو هست. برای اینکه پروژه رو شروع کنید از یک محیط مجازی برای پایتون استفاده کنید و مواردی که توی نیازمندی ها هست رو اضافه کنید.
 
 دستورات لازم:
 
 
 installing virtual environment:
 
 ```bash
 pip install virtualenv
 
 ```
 
 
 creating virtual environment:
 
 ```bash
 virtualenv venv
 ```
 
 
 using virtual environment:
 
 on linux:
 ```bash
 source venv/bin/activate
 ```
 on windows:
 
 ```bash
 .\venv\Scripts\activate
 ``` 
 installing requirements:
 
 ```bash
 pip install -r requirements.txt
 ```
 
 starting new app:
 
 ```bash
 python startapp newapp
 ```
 
 making migrations:
 
 ```bash
 python manage.py makemigrations
 
 python manage.py migrate
 ```
