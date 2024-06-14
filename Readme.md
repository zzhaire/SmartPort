## 预览图

![image-20240614102029617](https://zzhaire-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20240614102029617.png)

![image-20240614103437643](https://zzhaire-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20240614103437643.png)

## 项目依赖

### mysql 环境

>mysql 环境，配置本机的mysql 数据库，版本不限制， utf8编码即可
>
>创建SmartPort数据库即可， 在对应的setting.py 修改对应的数据库配置即可
>
>![image-20240614102343697](https://zzhaire-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20240614102343697.png)

### python 环境

推荐使用`conda`创建环境， 创建环境

```
conda create -n DjangoEnv python=3.8
```

激活环境 如果是配置了`Script`在环境变量， 直接`activate` `环境名` 即可

```
conda activate DjangoEnv
```

需要的依赖包

![image-20240614102716453](https://zzhaire-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20240614102716453.png)

使用pip 下载即可， 好像只需要`mysqlclient`, `Django` 这两个，具体的我忘了，缺少什么根据提示下载就好。

## 项目启动

### 数据库生成

使用django数据库工具产生sql语句生成数据库

```
python manage.py makemigrations
python manage.py migrate
```

创建超级管理员（可选）， 在/admin 下进入后台管理

```
python manage.py createsuperuser
```

### 项目启动

```
python manage.py runserver
```

## 测试数据生成

初试数据库里是空的，可通过/admin 后台自行添加，也可在dataGenerate 文件夹下执行单个文件（功能包括数据生成/数据库清空）生成数据

## 注意

外部库并没有全部下载， 需要科学上网环境正确打开项目， 如果需要本地无网络运行， 请自行下载相关包

位置：templates下的link 和 script 例如：base.html 中的vue element-ui axios 依赖包：

![image-20240614104539106](https://zzhaire-markdown.oss-cn-shanghai.aliyuncs.com/img/image-20240614104539106.png)