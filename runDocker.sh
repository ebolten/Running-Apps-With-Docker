#!/bin/sh

# building the docker files
echo 'building python application. . .'
echo ''
docker build --tag=me/python-img -f Dockerfile_python .
echo 'building fortran application. . .'
echo ''
docker build --tag=me/fortran-img -f Dockerfile_fortran .
echo ''
echo 'building node application. . .'
docker build --tag=me/node-img -f Dockerfile_node .
echo ''
echo 'building ruby application. . .'
docker build --tag=me/ruby-img -f Dockerfile_ruby .
echo ''
# running the docker files
docker run me/ruby-img
docker run me/python-img
docker run me/node-img
docker run me/fortran-img
echo ''