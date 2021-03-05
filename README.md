
# **Djangonetes** - [![build](https://circleci.com/gh/jaehwankim07120/djangonetes.svg?style=shield&circle-token=4d691bd2b328bdb794976d6897bc04be89cb7536)](https://app.circleci.com/gh/jaehwankim07120/djangonetes) [![Docker](https://img.shields.io/badge/Docker-20.1.2-brightgreen.svg)]() [![Kubernetes](https://img.shields.io/badge/Kubernetes-1.19.3-brightgreen.svg)]() [![Python](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://www.python.org/downloads/release/python-367/) [![Django](https://img.shields.io/badge/Django-3.1.7-brightgreen.svg)](https://docs.djangoproject.com/en/3.1/intro/install/) [![gunicorn](https://img.shields.io/badge/gunicorn-20.0.4-brightgreen.svg)]()

## **Reference**
---

## **Install**
---

## **Tutorial**
---
1. Docker Desktop 을 위 서술한 같은 버전으로 셋업해둔 상태를 기점으로 시작한다.
  - <내용추가>
2. <Docker-Compose 설치 내용 추가>
3. `> .script/compose-build` 를 통해서 docker image 설치 및 실행
4. <내용추가>
5. 하단 이미지와 같이 서비스가 실행되면 성공
 - ![image](https://user-images.githubusercontent.com/36470472/110159422-073d8600-7e2e-11eb-9796-866605281333.png)

## **Run**
---
  http://localhost:80
  - docker-compose 를 통해서 port는 변경 가능
    - 만약 변경한다면 `docker-compose.yml` 과 `docker/nginx/nginx.conf` 를 수정하여 변경
  - `django-compose` 가 아닌 `> python manage.py runserver 8000` 를 입력했을 경우 http://localhost:8000 으로 접속
  - ![image](https://user-images.githubusercontent.com/36470472/110161602-f17d9000-7e30-11eb-96ee-71e77b7755c9.png)

## **Next step**
---
1. Kubernetes 같은 경우 dashboard(alternative먼저) 기본적인 nginx-ingress 를 기점으로 작업 예정. 기존에 사내 프로젝트에서 작업한 내역이 있어서 바로 적용이 가능할 것으로 생각됨
2. KGE 와 같이 연동하여 외부 서버에 노출 시키는 것을 적용
3. Circle CI를 통해 자동 배포를 적용
4. 위를 기점으로 Tutorial 이 가능한 선에서 Test Code 및 주석 보정
5. 이 기점으로 Database 또한 하나의 서비스로 분리 및 API Gateway 설계
