# 文件解读说明

*语言解释*

*带文件后缀名是文件本身说明*

*带./前缀是对文件夹的说明*



main.py

```python
主启动文件
```

db.py

```
用于数据库CURD操作
将数据库交互和业务逻辑分离
```

pretreatment.py

```python
# 预操作
操作社团信息，录入社团信息excel -》数据库
```

loading.py

```python
# 预操作
操作学院专业信息excel -》数据库
```



./static

```python
该文件夹下面是存在该项目所使用资源的excel文件
```

./router

```python
主要业务代码
apply 申请相关
club  社团信息相关
stu   学生信息相关
```

./model

```
fastapi老生常谈的model
```

