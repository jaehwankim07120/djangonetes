#!/bin/bash
kubectl apply -f ./kuber/ingress/dashboard.yml
kubectl apply -f ./kuber/ingress/django.live.yml
kubectl apply -f ./kuber/ingress/django.dev.yml

kubectl describe ingress --all-namespaces
kubectl get services -n ingress-nginx