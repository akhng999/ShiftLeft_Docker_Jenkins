#Dockerfile
FROM python:3.7-buster

#Install NGINX
RUN apt-get update && apt-get install nginx -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default

RUN mkdir /VulnerableWebApp
COPY . /VulnerableWebApp
 
WORKDIR /VulnerableWebApp/VulnerableWebApp

RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["./startup.sh"]
