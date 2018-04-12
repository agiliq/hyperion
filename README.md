Hyperion - Watch your sites, get notified whene there is a problem
-------------------------------------------------------------------------

![Hyperion image](hyperion.jpg)

Sometimes your site will go down. Be the first to know when that happens.

Hyperion is a open source, self hosted alternatives to pingdom, pageduty, gtmetrix or uptime robot.

#### Architecture

Hyperion consists of two parts,

- A UI to setup the watces. You can setup the URL, the check frequency and the expected http status code.
This can be run locally. The created watches are stored in Google cloud datastore
- A scheduled google cloud function runs the watches at regular frequency, and if the statsu code doesn't match the expected status code an email is sent to the registered email.


#### Built with

- Python 3
- Flask
- GCP Data store
- GCP Cloud functions
