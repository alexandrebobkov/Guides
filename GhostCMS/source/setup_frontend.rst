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
    For Ghost CMS to function properly, you need to set up e-mail services for sending notification and authentication e-mails. While there are many providers, Mailgun is recommended. Create a Mailgun account and configure it to handle your domain's email delivery. This is essential for sending newsletters and other marketing emails.

Business E-Mail (Google Workspace)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^