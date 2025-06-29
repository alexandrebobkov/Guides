SETING UP FRONT END
====================

Domain Name
-------------------

.. image:: graphics/switch.jpg

Configuring DNS entries for your registered domain name is essential for directing internet traffic to your website and associated services. Proper DNS setup ensures that users can access your site using your chosen domain, and that email and other services function reliably.

You can typically find your domain name details in your domain registrar's account dashboard or in the confirmation email you received when you registered the domain. This information is necessary for managing DNS records and verifying domain ownership.

DNS Configuration
^^^^^^^^^^^^^^^^^^

+------+------------------+---------------------+
| Type | Name             | Content             |
+======+==================+=====================+
| A    | domain-name.ca   | Public IP Address   |
+------+------------------+---------------------+
| MX   | domain-name.ca   | mail.domain-name.ca |
+------+------------------+---------------------+

E-Mail Delivery Services
-------------------------

Marketing E-Mail Campaigns (MAILGUN)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. important::
    To enable Ghost CMS to send authentication emails, newsletters, and marketing messages, you need to configure an email delivery service. Mailgun is natively supported by Ghost CMS, making integration simple and reliable. Just sign up for a Mailgun account, add your domain, and update your Ghost configuration to start sending emails with minimal hassle.

Business E-Mail (Google Workspace)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^