#!/bin/bash
kubectl apply -f ./kuber/deployment/ingress.yml
kubectl apply -f ./kuber/deployment/dashboard.yml

kubectl apply -f ./kuber/deployment/django.live.yml
kubectl apply -f ./kuber/deployment/django.dev.yml

kubectl apply -f ./kuber/secret/dashboard-adminuser.yml