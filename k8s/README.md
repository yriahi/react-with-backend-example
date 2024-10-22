# K8S & Helm

## 1- Convert docker-compose.yml to k8s manifests

```shell
kompose convert -f docker-compose.yml -o k8s

INFO Kubernetes file "k8s/backend-service.yaml" created
INFO Kubernetes file "k8s/frontend-service.yaml" created
INFO Kubernetes file "k8s/backend-deployment.yaml" created
INFO Kubernetes file "k8s/frontend-deployment.yaml" created
```

## 2- Cleanup kompose annotations

- This aims are removing annotations that are added by `kompose`
- Run `kompose-cleaner.py <target-dir>`


## 3- Helmify

Create a Helm Chart from your K8S manifests.

```shell
helmify  -f ./ my-app-chart 
```

## 4- helm chart helpers

- Add a template variable to your helm chart files to take a namespace.
- Run `chart-namespace-helper.py <target-dir>` to add `namespace: {{ .Values.namespace }}` to your 
- Ensure to add `namespace: yriahi` to your helm chart's `values.yaml`
