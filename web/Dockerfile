FROM docker.io/library/nginx:1.23-alpine3.17

# Static Files
RUN mkdir /usr/local/www
COPY ./dist/ /usr/local/www/
RUN rm /etc/nginx/conf.d/default.conf

# Get nginx configs
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./nginx/proxy.conf /etc/nginx/proxy.conf
COPY ./nginx/conf.d/ /etc/nginx/conf.d/

# Adjust Permissions
RUN chown -R nginx:nginx /usr/local/www