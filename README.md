
# **Djangonetes** - [![build](https://circleci.com/gh/jaehwankim07120/djangonetes.svg?style=shield&circle-token=6d6e029ba8299eb7f5c8bee2ee7484f60daf5a18)](https://app.circleci.com/pipelines/github/jaehwankim07120/djangonetes) [![Docker](https://img.shields.io/badge/Docker-20.1.2-brightgreen.svg)]() [![Kubernetes](https://img.shields.io/badge/Kubernetes-1.19.3-brightgreen.svg)]() [![Python](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://www.python.org/downloads/release/python-367/) [![Django](https://img.shields.io/badge/Django-3.1.7-brightgreen.svg)](https://docs.djangoproject.com/en/3.1/intro/install/) [![gunicorn](https://img.shields.io/badge/gunicorn-20.0.4-brightgreen.svg)]()

## **Getting Started**
---
### 따로 설정이 없을 경우 기본 어드민(superuser) 계정
```
ID: admin
PW: adminadmin
```

## **Run: django**
---
### Install 
```
python manage.py collectstatic

# when you add your database you have to change below part
python manage.py migrate
python manage.py create_admin
```

### Acces
```
python manage.py runserver 8000
```

![image](https://user-images.githubusercontent.com/36470472/110161602-f17d9000-7e30-11eb-96ee-71e77b7755c9.png)

Now access django at:

[`http://localhost:8000`](http://localhost:8000)

## **Run: docker-compose(docker desktop)**
---
### Install 
```
sh .script/compose_build.sh
sh .script/compose_deploy.sh
```
### Acces
Now access service at:

[`http://localhost:80`](http://localhost:80)

하단 이미지와 같이 서비스가 실행되면 성공
![image](https://user-images.githubusercontent.com/36470472/110159422-073d8600-7e2e-11eb-9796-866605281333.png)

## **Run: kubernetes(docker desktop)**
---
### Setup
hostname 을 등록해야만 작동함. 하지만 각 OS 별로 127.0.0.1 에 대한 hosts 변경 방법이 달라 변경하면 될 듯
일단 기본적으로 설정해야 하는 것은 아래와 같음
```
127.0.0.1 kuber.djangonetes.io
```
### Install 
```
sh .script/kube_build.sh
sh .script/kube_deploy.sh

... few_second..? for boot nginx-ingress

sh .script/kube_ingress.sh
```
### Acces
Now access kubernetes at:

[`http://kuber.djangonetes.io:node-port/`](http://kuber.djangonetes.io:node-port/)

![image](https://user-images.githubusercontent.com/36470472/110166475-c34f7e80-7e37-11eb-8706-cbacae3cd7eb.png)

[`http://kuber.djangonetes.io:node-port/live`](http://kuber.djangonetes.io:node-port/live)

![image](https://user-images.githubusercontent.com/36470472/110166537-de21f300-7e37-11eb-8751-8c226dd99126.png)

[`http://kuber.djangonetes.io:node-port/test`](http://kuber.djangonetes.io:node-port/test)

![image](https://user-images.githubusercontent.com/36470472/110166592-f134c300-7e37-11eb-9853-0a6b488eec59.png)

![image](https://user-images.githubusercontent.com/36470472/110166646-00b40c00-7e38-11eb-97b6-45d0189e02f7.png)

### NodePort?
```
sh .script/kube_status_ingress.sh
```

![image](https://user-images.githubusercontent.com/36470472/110166720-1cb7ad80-7e38-11eb-9984-b9d0403bd3c0.png)

## **Next step**
---
1. Kubernetes 같은 경우 dashboard(alternative먼저) 기본적인 nginx-ingress 를 기점으로 작업 예정. 기존에 사내 프로젝트에서 작업한 내역이 있어서 바로 적용이 가능할 것으로 생각됨
2. KGE 와 같이 연동하여 외부 서버에 노출 시키는 것을 적용
3. Circle CI를 통해 자동 배포를 적용
4. 위를 기점으로 Tutorial 이 가능한 선에서 Test Code 및 주석 보정
5. 이 기점으로 Database 또한 하나의 서비스로 분리 및 API Gateway 설계
