FROM alpine:latest AS buildbase

#Объявление переменных LEGACY?
#ENV NGINX_VERSION 

RUN set -e && \
    apk add --no-cache build-base pcre pcre-dev zlib-dev perl linux-headers && \
    mkdir /src && \
    cd /src && \
    wget https://nginx.org/download/nginx-1.29.6.tar.gz && \
    wget https://github.com/openssl/openssl/releases/download/openssl-3.3.5/openssl-3.3.5.tar.gz && \
    tar xvf nginx-1.29.6.tar.gz && \
    tar xvf openssl-3.3.5.tar.gz && \ 
    cd nginx-1.29.6 && \ 
    ./configure \
        --prefix=/var/www --error-log-path=/var/log/nginx/error.log \ 
        --http-log-path=/var/log/nginx/access.log \
        --conf-path=/etc/nginx/nginx.conf \
        --pid-path=/run/nginx/nginx.pid \ 
        --lock-path=/run/nginx/nginx.lock \
        --sbin-path=/usr/bin/nginx \ 
        --builddir=/src/nginx-1.29.6/build \ 
        --with-http_v2_module \ 
        --with-http_realip_module \
        --with-http_auth_request_module \
        --with-http_ssl_module \
        --with-openssl=/src/openssl-3.3.5 \
        --with-openssl-opt=enable-tls1_3 && \
    make -j $(nproc) && \
    make install


FROM alpine:latest

COPY --from=buildbase /usr/bin/nginx /usr/bin/nginx
COPY --from=buildbase /var/www /var/www
COPY --from=buildbase /etc/nginx /etc/nginx

RUN set -e && \
    apk add --no-cache pcre pcre-dev zlib-dev && \
    addgroup -g 101 -S nginx && \
    adduser -S -D -H -u 101 -h /var/cache/nginx -s /sbin/nologin -g nginx nginx && \
    #mkdir /var/www && \ 
    #mkdir -p /etc/nginx/conf.d && \
    #cp -r /src/html /var/www && \
    #cp -r /src/build /usr/bin/nginx && \
    #cp -r /src/conf/* /etc/nginx/conf.d && \
   #mkdir /run/nginx && \
    mkdir -p /run/nginx && \ 
    mkdir /var/log/nginx && \  
    chown -R nginx:nginx /var/www/html && \
    #rm -rf /src/* && \
    touch /var/log/nginx/error.log && \
    touch /var/log/nginx/access.log && \  
    touch /run/nginx/nginx.pid && \
    ln -sf /dev/stderr /var/log/nginx/error.log  && \
    ln -sf /dev/stdout /var/log/nginx/access.log

COPY nginx.conf /etc/nginx/nginx.conf
COPY def.conf /etc/nginx/conf.d/def.conf

EXPOSE 80

STOPSIGNAL SIGQUIT

CMD ["nginx", "-g", "daemon off;"]