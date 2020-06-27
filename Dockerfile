FROM alpine
RUN  apk update && \
 apk upgrade &&  \
 apk add python3 && \
 apk add py3-pip
COPY ./app.py /opt/app.py
RUN chmod u+x /opt/app.py
WORKDIR /opt/
CMD ["python3"]
ENTRYPOINT [ "/opt/app.py" ] 