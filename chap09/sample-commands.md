
# create project "docker-book"

 1. open the GCP console.
 2. create the project "docker-book".
 3. "API and Service" -> "Library".
 4. search the "Google Compute Engine API" and enable it.

# create Service Account key

 https://cloud.google.com/docs/authentication/production

# create JSON file

```shell
 ~/.zshrc
 export GOOGLE_APPLICATION_CREDENTIALS="~/.gcp/docker-book-6fbc6b66425c.json"
```

# set/get Project ID

```shell
gcloud config set project docker-book-xxxx # use your PORJECT ID
PROJECT_ID=$(gcloud config list project --format "value(core.project)")
echo $PROJECT_ID
```

# list 9.3 create repository

```shell
gcloud alpha source repos create dockertext2
```

# list 9.4 set remote repository

```shell
git remote add google https://source.developers.google.com/p/$PROJECT_ID/r/dockertext2
```

# list 9.5

```shell
git push google master
```

# enable the APIs

- search these APIs and enabele them.
- "Google Kubenetes Engine API"
- "Google Container Registry API"
- "Google Cloud Container Builder API" <- I couldn't find it. is there on the GCP API?

# list 9.9

text book said `gcloud container builds submit --config config/cloudbuild.yaml .` but error occurred.
Then I execute below.

```shell
gcloud builds submit --config config/cloudbuild.yaml .
```

# list 9.11

```shell
gcloud container clusters get-credentials imageview --zone=asia-northeast1-a
```

# list 9.12

```shell
kubectl get nodes
```

# list 9.14

```shell
kubectl create -f config/configmap.yaml
```

# list 9.16

```shell
kubectl create -f config/secrets.yaml
```

# list 9.21

```shell
kubectl create -f config/deployment-blue.yaml
kubectl create -f config/deployment-green.yaml
```

# list 9.22

```shell
kubectl get pods
```


# list 9.27

```shell
kubectl create -f config/service.yaml
```

# list 9.28

```shell
kubectl get services
```

# list 9.33

```shell
kubectl create -f config/cronjob.yaml
```

# list 9.34

```shell
kubectl get cronjob
```

# list 9.35

```shell
kubectl get jobs --watch
```

# list 9.36

```shell
kubectl delete -f config/cronjob.yaml
```

# list 9.29

```shell
kubectl delete -f config/service.yaml
```

# list 9.25

```shell
kubectl delete -f config/deployment-blue.yaml
kubectl delete -f config/deployment-green.yaml
```
