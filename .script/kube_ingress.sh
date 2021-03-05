#!/bin/bash
kubectl apply -f ./kuber/ingress/dashboard.yml
kubectl apply -f ./kuber/ingress/django.yml
kubectl apply -f ./kuber/ingress/django.test.yml

kubectl describe ingress --all-namespaces
kubectl get services -n ingress-nginx