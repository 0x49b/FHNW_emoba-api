FROM python:3.9

LABEL Maintainer="Florian Thiévent"
LABEL traefik.enable="true"
LABEL traefik.http.middlewares.emoba-https-redirect.redirectscheme.scheme="https"
LABEL traefik.http.routers.emoba-secure.entrypoints="https"
LABEL traefik.http.routers.emoba-secure.rule="Host(`emoba.thievent.org`)"
LABEL traefik.http.routers.emoba-secure.service="emoba"
LABEL traefik.http.routers.emoba-secure.tls="true"
LABEL traefik.http.routers.emoba-secure.tls.certresolver="http"
LABEL traefik.http.routers.emoba.entrypoints="http"
LABEL traefik.http.routers.emoba.middlewares="emoba-https-redirect"
LABEL traefik.http.routers.emoba.rule="Host(`emoba.thievent.org`)"
LABEL traefik.http.routers.emoba.service="emoba"
LABEL traefik.http.routers.emoba.tls.certresolver="leresolver"
LABEL traefik.http.services.emoba.loadbalancer.server.port="8000"

# Set variables for project name, and where to place files in container.
ENV PROJECT=emoba
ENV CONTAINER_HOME=/opt
ENV CONTAINER_PROJECT=$CONTAINER_HOME/$PROJECT

# Create application subdirectories
RUN mkdir $CONTAINER_PROJECT
WORKDIR $CONTAINER_PROJECT
RUN mkdir $CONTAINER_PROJECT/logs
RUN echo "" > $CONTAINER_PROJECT/logs/gunicorn.log
# Copy application source code to $CONTAINER_PROJECT
COPY . $CONTAINER_PROJECT

# Install Python dependencies
#RUN python -m pip install --upgrade pip
RUN pip install -r $CONTAINER_PROJECT/requirements.txt
RUN python manage.py collectstatic --noinput
RUN ["chmod", "+x", "/opt/emoba/staticfiles"]

RUN python manage.py collectstatic --noinput

# Copy and set entrypoint
WORKDIR $CONTAINER_PROJECT
#COPY ./start.sh /
#RUN ["chmod", "+x", "/opt/emoba/start.sh"]

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]