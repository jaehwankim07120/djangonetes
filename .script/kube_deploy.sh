#!/bin/bash
kubectl apply -f ./kuber/deployment/ingress.yml
kubectl apply -f ./kuber/deployment/dashboard.yml

kubectl apply -f ./kuber/deployment/django.yml
kubectl apply -f ./kuber/deployment/django.test.yml

kubectl apply -f ./kuber/secret/dashboard-adminuser.yml