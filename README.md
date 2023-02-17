<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/jumble-word-api">
  </a>

<h3 align="center">Jumble-Word-API</h3>

  <p align="center">
    An API based on FastAPI that is used to scramble words
    <br />
  </p>
</div>


<!-- GETTING STARTED -->
## Getting Started

This project can be deployed locally or in a containerized workflow depending on the user's preference. Instructions for both deployments are located in the installation section.

### Assumptions
- Users will be familiar with the process to deploy a local kubernetes cluster and how to deploy resources on cluster

- All requests to api will be recorded in audit log (including request to get audit log)

### Prerequisites

This project requires the software below as a prerequisite. It has been split into two sections depending on the type of deployment

Containerized deployment
* docker desktop (required only if deploying k8s cluster using kind)
  ```sh
  choco install docker-desktop (windows through chocolatey)
  brew install docker (mac os through homebrew)
  ```
* kubernetes cli (kubectl)
  ```sh
  choco install kubernetes-cli (windows through chocolatey)
  brew install kubernetes-cli (mac os thorugh homebrew)
  ```

* helm (optional)
  ```sh
  choco install kubernetes-helm (windows through chocolatey)
  brew install helm (mac os through homebrew)
  ```

* kubernetes cluster (local)
* kind (requires docker desktop)
  ```sh
  choco install kind (windows through chocolatey)
  brew install kind (mac os though chocolatey)
  ```
or

* minikube
  ```sh
  choco install minikube (windows through chocolatey)
  brew install minikube (mac os through homebrew)
  ```

Local Deployment
* Python3
  ```sh
  choco install python (windows through chocolatey)
  brew install python@3.9 (macos through homebrew)
  ```

* FastAPI (requires python)
  ```sh
  pip install fastapi
  ```
* Uvicorn (requires python)
  ```sh
  pip install "uvicorn[standard]"
  ```

### Building/Updating Docker Image
1. Clone or Download the code from the repository
  ```sh
  git clone https://github.com/khan-belal/jumble-word-api.git
  ```
    or 
  
  Pull image from docker hub
  ```sh
  docker pull belalkhan/jumble-word-api:latest
  ```

2. Make required changes to Docker file/application file

3. Build docker image
  ```sh
  docker build -t khan-belal/jumble-word-api .
  ```

4. Run new built image
  ```sh
  docker run -p 80:80 khan-belal/jumble-word-api
  ```

### Installation

Containerized deployment
1. Clone or Download the code from the repository
  ```sh
  git clone https://github.com/khan-belal/jumble-word-api.git
  ```

2. Deploy a local kubernetes cluster.

    If using kind use the included config file to ensure networking ports are exposed for connectivity

  ```sh
  kind create cluster --name my-cluster --config=kind-config.yaml
  ```
    If using minikube, start the kubernetes cluster.
  ```sh
  minkube start
  ```

3. Check status of cluster and confirm kubectl has been setup correctly
   ```sh
   kubectl get nodes
   ```

4. Create namespace for application
  ```sh
  kubectl create namespace jumble-word
  ```

5. Deploy the application

    If using helm

   ```sh
   helm install --namespace jumble-word jumble-word-api --values ./jumble-word-api/values.yaml
   ```

    Otherwise, kubectl can be used to deploy the app directly
   ```sh
   kubectl apply -f -namespace jumble-word api-deployment.yaml
   ```

Local Deployment
1. Ensure python is installed

    ```sh
    python3 --version
    ```

2. Install required packages for FastAPI/Uvicorn

  ```sh
  pip install fastapi
  pip install "uvicorn[standard]"
  ```

3. Start the uvicorn server

  ```sh
  uvicorn main:app
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The api enables 2 functionalities with usage examples for each function below:

jumble-word
The main function of the api is to jumble words that are supplied to the api. 

To request a jumbled word from the api, first locate the ip address of the pod/instance running the api.

If running on the local machine, the address for the api will be 

http://localhost:8000

If running on a local kubernetes cluster, obtain the ip address of the running node. This is especially important if running the cluster in WSL2 on Windows.

```sh
minikube ip
```

If using kind obtain the ip address of the linux instance running in WSL2 (windows only)
 
```sh
ifconfig eth0
```

Once the ip address of the api is located, the api can be queried using the examples below:

Jumble-word
  To scramble the word happy, send the request to the api using:
  ```sh
  localhost:8000/jumble-word?word=happy
  ```
  Output:
  ```sh
  ppayh
  ```

Audit api
  To get an audit log of the last 10 calls made to the api, run:
  ```sh
  localhost:8000/audit
  ```
  Output:
  ```sh
  "{\"api_call\": \"Get audit-log\", \"query\": \"N/A\", \"payload\": \"N/A\"}\n"
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
