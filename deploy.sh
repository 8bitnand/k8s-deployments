docker build  -t helloworld:latest -f Dockerfile .
docker run -d  -p 80:80 helloworld:latest 