FROM pndf/my-py:latest
LABEL author='I'
COPY . /server/

WORKDIR /server

RUN pip install -r requirements.txt --break-system-packages

EXPOSE 8080
ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=8080"]