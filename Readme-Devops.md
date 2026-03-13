# 🚀 End-to-End DevOps Project: Local -> Kubernetes(EKS)

This project demonstrates a complete **DevOps workflow for deploying a containerized application to Kubernetes using CI/CD and GitOps principles**.

The pipeline takes an application from **local development to automated deployment on AWS EKS using Docker, Helm, GitHub Actions, and ArgoCD.**

---

# 📌 Project Overview

In real-world production environments, multiple DevOps tools work together to automate application delivery.

This project connects the following components into a single workflow:

Local Development
⬇
Docker Containerization
⬇
Kubernetes Deployment
⬇
AWS EKS Cluster
⬇
NGINX Ingress Controller
⬇
Helm Packaging
⬇
GitHub Actions CI Pipeline
⬇
ArgoCD Continuous Delivery (GitOps)

The result is a **fully automated CI/CD pipeline for Kubernetes deployments.**

---

# 🛠 Tech Stack

* Docker
* Kubernetes
* AWS EKS
* Helm
* GitHub Actions
* ArgoCD
* NGINX Ingress
* AWS CLI
* kubectl

---

# 🏗 Architecture Workflow

The project follows this DevOps lifecycle:

1️⃣ Develop and test the application locally
2️⃣ Build a production-ready Docker image
3️⃣ Deploy the container to Kubernetes
4️⃣ Run the cluster on AWS EKS
5️⃣ Expose services using NGINX Ingress
6️⃣ Package Kubernetes manifests with Helm
7️⃣ Automate builds with GitHub Actions
8️⃣ Deploy automatically using ArgoCD (GitOps)

---

# ⚙️ Step-by-Step Implementation

## 1️⃣ Run Application Locally

The first step is validating the application locally to ensure it works before containerizing it.

This helps catch issues early before deploying to cloud infrastructure.

---

## 2️⃣ Build Multi-Stage Docker Image

The application is containerized using a **multi-stage Docker build**.

Benefits of multi-stage builds:

* Smaller image size
* Improved security
* Separate build and runtime environments

Build the Docker image:

```
docker build -t app-image .
```

---

## 3️⃣ Create Kubernetes Manifests

To deploy the application to Kubernetes, the following YAML files are created.

### Deployment

Defines the application container and manages pods.

### Service

Exposes the application internally within the cluster.

### Ingress

Routes external traffic to the Kubernetes service.

These files allow Kubernetes to manage the application lifecycle.

---

## 4️⃣ Setup AWS Environment

To interact with AWS resources securely, an IAM user is created.

Steps include:

* Create IAM user
* Assign required permissions
* Generate Access Key and Secret Key

---

## 5️⃣ Install and Configure AWS CLI

Install AWS CLI and configure it with IAM credentials.

```
aws configure
```

Provide:

* Access Key
* Secret Key
* Default Region

This allows the local system to interact with AWS services.

---

## 6️⃣ Setup Kubernetes Cluster with AWS EKS

Install the required tools:

* kubectl
* eksctl

Create the Kubernetes cluster on AWS using EKS and connect kubectl to it.

This enables management of the Kubernetes cluster from the local machine.

---

## 7️⃣ Install NGINX Ingress Controller

The **NGINX Ingress Controller** manages external access to services in the Kubernetes cluster.

It acts as a:

* Reverse proxy
* Load balancer
* Traffic router

This allows users to access applications via HTTP/HTTPS.

---

## 8️⃣ Deploy Application to Kubernetes

Apply Kubernetes manifests:

```
kubectl apply -f k8s/
```

This creates:

* Deployment
* Service
* Ingress

The application is now running inside the Kubernetes cluster.

---

## 9️⃣ Map DNS to Load Balancer

Once the ingress controller is installed, Kubernetes provisions a cloud load balancer.

The load balancer exposes the application externally.

A domain name can be mapped to this endpoint for public access.

---

## 🔟 Package Application with Helm

Helm is used to package Kubernetes manifests into reusable charts.

Create a Helm chart:

```
helm create app-chart
```

Move Kubernetes YAML files into the **templates/** directory.

Helm allows configuration through **values.yaml**, making deployments reusable and configurable.

---

## 1️⃣1️⃣ Test Helm Deployment

Before automation, the Helm chart is tested manually.

First delete previously deployed resources, then install using Helm.

```
helm install my-app ./chart
```

This verifies that the Helm chart deploys the application correctly.

---

# 🔁 Continuous Integration with GitHub Actions

A GitHub Actions workflow automates the CI pipeline.

Typical pipeline steps include:

* Checkout repository
* Build Docker image
* Run tests
* Push image to container registry

The pipeline runs automatically whenever new code is pushed.

---

# 🚀 Continuous Delivery using ArgoCD

ArgoCD enables **GitOps-based deployment** for Kubernetes.

Instead of manually applying Kubernetes manifests, ArgoCD continuously syncs the cluster with the Git repository.

Steps include:

1. Install ArgoCD in Kubernetes
2. Retrieve the admin password from Kubernetes secret
3. Access the ArgoCD UI
4. Connect the GitHub repository
5. Create a new ArgoCD application

Now every change pushed to GitHub automatically updates the Kubernetes cluster.

---

# 🎯 Key Benefits of This Architecture

✔ Fully automated CI/CD pipeline
✔ GitOps-based Kubernetes deployments
✔ Reproducible infrastructure
✔ Scalable container deployments
✔ Reduced manual operations

---

# 📚 What This Project Demonstrates

This project showcases practical DevOps concepts including:

* Docker containerization
* Kubernetes workload management
* Helm package management
* CI pipelines using GitHub Actions
* GitOps deployment with ArgoCD
* Kubernetes ingress configuration

---

# 🔮 Future Improvements

Potential enhancements include:

* Monitoring using Prometheus and Grafana
* Centralized logging with EFK stack
* Security scanning for Docker images
* Infrastructure provisioning using Terraform

---

# 👩‍💻 Author

**Sravya Pothuraju**

Cloud & DevOps Engineer focused on building scalable infrastructure and automated deployment pipelines.


