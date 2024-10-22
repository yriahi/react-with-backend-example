

## Conver docker compose files to k8s manifests

```shell
kompose convert -f docker-compose.yml -o k8s

INFO Kubernetes file "k8s/backend-service.yaml" created
INFO Kubernetes file "k8s/frontend-service.yaml" created
INFO Kubernetes file "k8s/backend-deployment.yaml" created
INFO Kubernetes file "k8s/frontend-deployment.yaml" created
```
