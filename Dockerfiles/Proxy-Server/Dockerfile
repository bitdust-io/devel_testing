FROM python:2.7.15

RUN apt-get install -y git

#ADD https://api.github.com/repos/StasEvseev/devel/git/refs/heads/master version.json
RUN git clone https://github.com/StasEvseev/devel.git bitdust

WORKDIR bitdust
RUN python bitdust.py install

ENV PATH="/root/.bitdust:${PATH}"

ENV BITDUST_API_PASS_EXTERNAL_CONNECTIONS=1

RUN bitdust set services/identity-propagate/known-servers is:8084:6661
RUN bitdust set services/entangled-dht/known-nodes "dht_seed_1:14441, dht_seed_2:14441"
RUN bitdust set services/proxy-server/enabled true

RUN bitdust set services/proxy-transport/enabled false
#RUN bitdust set services/p2p-notifications/enabled false

ENTRYPOINT ["bitdust"]