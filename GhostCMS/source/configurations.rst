CONFIGURATIONS
==================

Nginx
------------------

Reverse Proxy Configuration (non-SSL)

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

.. important::
    This configuration is for a reverse proxy setup with Nginx, which forwards requests to the Ghost CMS instance running on port 2368. Ensure that the server name matches your domain and that the root directory and port number are set correctly.

.. tip::
    You may run the command ``ghost ls`` to display the port number of the Ghost CMS instance.

Reverse Proxy Configuration (SSL)

.. code-block:: bash

    map $status $header_content_type_options {
    204 "";
    default "nosniff";
    }

    server {
        listen 443 ssl http2;
        listen [::]:443 ssl http2;

        server_name activcount.ca;
        root /var/www/activcount/system/nginx-root; # Used for acme.sh SSL verification (https://acme.sh)

        ssl_certificate /etc/letsencrypt/activcount.ca/fullchain.cer;
        ssl_certificate_key /etc/letsencrypt/activcount.ca/activcount.ca.key;
        include /etc/nginx/snippets/ssl-params.conf;

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

	    client_max_body_size 1g;
    }

Ghost CMS
------------------

configuration.json

.. code-block:: json

    {
        "url": "https://domain-name.ca",
        "server": {
            "port": 2370,
            "host": "127.0.0.1"
        },
        "database": {
            "client": "mysql",
            "connection": {
                "host": "127.0.0.1",
                "user": "ghost-66",
                "password": "generated_password",
                "database": "ghost_db"
            }
        },
        "mail": {
            "transport": "SMTP",
            "options": {
                "host": "smtp.mailgun.org",
                "port": 587,
                "secure": false,
                "service": "Mailgun",
                "auth": {
                    "user": "postmaster@domain-name.ca",
                    "pass": "password"
                }
            }
        },
        "logging": {
            "transports": [
                "file",
                "stdout"
            ]
        },
        "process": "systemd",
        "paths": {
            "contentPath": "/var/www/ghost-cms-website/content"
        }
    }


