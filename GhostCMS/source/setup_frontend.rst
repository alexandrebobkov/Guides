SETING UP FRONT END
====================

Domain Name
-------------------

.. image:: graphics/switch.jpg

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