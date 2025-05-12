FROM ubuntu:22.04
RUN apt update && \
apt install -y python3 python3-pip python3-requests && \
rm -rf /var/lib/apt/lists
WORKDIR /tmp
COPY script.py /tmp/script.py
ENTRYPOINT ["python3", "script.py"]
