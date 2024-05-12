FROM python:3.11-slim-bullseye

ENV DEBIAN_FRONTEND=noninteractive
ENV HF_HUB_DISABLE_PROGRESS_BARS=1

RUN rm -rf /etc/apt/sources.list.d/*.list && \
    apt-get update && apt-get install -y git gcc build-essential python3-dev libgeos-dev

RUN python3 -m pip install --upgrade pip setuptools wheel

COPY requirements.txt .
RUN python3 -m pip install --upgrade --no-cache-dir pip setuptools wheel cython numpy pyshp six pyproj streamlit-folium leafmap psutil geopandas rioxarray localtileserver huggingface_hub

#RUN python3 -m pip install --upgrade --no-cache-dir --no-binary :all: shapely
#RUN python3 -m pip install --no-cache-dir git+https://github.com/SciTools/cartopy.git --upgrade cartopy

#RUN python3 -m pip install --no-cache-dir --compile -r requirements.txt
RUN python3 -m pip install --no-cache-dir -r requirements.txt

RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME

RUN mkdir ./pages
COPY --chown=user /pages ./pages
COPY --chown=user /Home.py ./Home.py

RUN pip install jupyter-server-proxy

ENV JUPYTER_ENABLE_LAB=yes

ARG LOCALTILESERVER_CLIENT_PREFIX='proxy/{port}'
ENV LOCALTILESERVER_CLIENT_PREFIX=$LOCALTILESERVER_CLIENT_PREFIX

EXPOSE 7860

CMD ["streamlit", "run", "./Home.py", "--server.port=7860"]
