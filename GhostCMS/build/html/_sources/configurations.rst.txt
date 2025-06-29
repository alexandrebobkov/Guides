CONFIGURATIONS
==================

Nginx
------------------

Reverse Proxy Configuration

.. code-block:: bash
 
    map $status $header_content_type_options {
        204 "";
        default "nosniff";
    }

    server {
        listen 80;
        listen [::]:80;

        server_name activcount.ca www.activcount.ca;
        root /var/www/activcount/system/nginx-root; # Used for acme.sh SSL verification (https://acme.sh)

        location / {
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header Host $http_host;
            proxy_pass http://127.0.0.1:2368;

            add_header X-Content-Type-Options $header_content_type_options;
        }

        location ~ /.well-known {
            allow all;
        }

        client_max_body_size 50m;
    }

.. note::

    This configuration is for a reverse proxy setup with Nginx, which forwards requests to the Ghost CMS instance running on port 2368. The `X-Content-Type-Options` header is set to `nosniff` to prevent MIME type sniffing, enhancing security.

    Ensure that the server name matches your domain and that the root directory is set correctly.

Ghost CMS
------------------


.. code-block:: json

    