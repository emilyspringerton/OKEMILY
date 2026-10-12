# okemily.com on GKE (K8S-MV-02): static site baked from git; generated content comes from IDUNA's PVC (see okemily-web.conf).
FROM nginx:1.27-alpine
RUN rm -rf /usr/share/nginx/html/* /etc/nginx/conf.d/default.conf
COPY site/ /usr/share/nginx/html/
COPY okemily-web.conf /etc/nginx/conf.d/default.conf
RUN printf '#!/bin/sh\nexec nginx -g "daemon off;"\n' > /run-nginx.sh && chmod +x /run-nginx.sh
RUN chmod -R a+rX /usr/share/nginx/html
