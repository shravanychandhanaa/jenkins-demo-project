# Flask App with Jenkins CI/CD on Ubuntu EC2

This project demonstrates deploying a Flask web application using
Jenkins on an Ubuntu EC2 instance with Docker.

## Prerequisites

-   **Ubuntu EC2 instance**
-   **Jenkins** installed and running on EC2
-   **Docker** installed
-   GitHub repository with application source code (configured in
    Jenkins via "Git from SCM")

## Installation Steps

### 1. Install Docker on Ubuntu EC2

``` bash
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu
```

### 2. Install Jenkins on Ubuntu EC2

``` bash
sudo apt update
sudo apt install -y openjdk-17-jdk
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt install -y jenkins
sudo systemctl start jenkins
sudo systemctl enable jenkins
```

Access Jenkins in browser:

    http://<EC2_PUBLIC_IP>:8080

### 3. Configure Jenkins

-   Install **Docker Pipeline** plugin in Jenkins.
-   Create a **Pipeline** job.
-   In **Pipeline Definition**, choose **Pipeline script from SCM**.
-   Select **Git** and provide repository URL and branch.
-   Add Jenkinsfile to repo.

### 4. Flask App Files

**app.py**
**requirements.txt**
**Dockerfile**
**Jenkinsfile**

### 7. Test Application

Access in browser:

    http://<EC2_PUBLIC_IP>:5000 (screenshot included)


