FROM ubuntu:latest
LABEL authors="eugenkonyshev"

ENTRYPOINT ["top", "-b"]