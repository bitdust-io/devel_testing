FROM python:2.7.15

RUN apt-get install -y git

#ADD https://api.github.com/repos/StasEvseev/devel/git/refs/heads/master version.json
RUN git clone https://github.com/StasEvseev/devel.git bitdust

WORKDIR bitdust
RUN python bitdust.py install

ENV PATH="/root/.bitdust:${PATH}"

RUN bitdust set services/identity-server/host is
CMD ["bitdust", "identity", "server", "start"]
#rm -rf /root/.bitdust/id