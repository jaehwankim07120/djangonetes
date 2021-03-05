#!/bin/bash
kubectl get endpoints -o wide

kubectl describe ingress --all-namespaces
kubectl get services -n ingress-nginx