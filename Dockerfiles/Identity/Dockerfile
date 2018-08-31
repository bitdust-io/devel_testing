FROM python:2.7.15

#RUN apt-get install -y git

#ADD https://api.github.com/repos/StasEvseev/devel/git/refs/heads/master version.json
#RUN echo $RANDOM
#RUN git clone https://github.com/bitdust-io/devel.git bitdust --progress
COPY src/bitdust bitdust

WORKDIR bitdust
RUN python bitdust.py install

ENV PATH="/root/.bitdust:${PATH}"

RUN bitdust set services/identity-server/host is
ENTRYPOINT ["bitdust", "identity", "server", "start"]
#rm -rf /root/.bitdust/id