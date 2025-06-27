docker build  -t helloworld:latest -f Dockerfile .
docker run -p 80:80 helloworld:latest 