Command line usages
===================

`Random Profile Generator` can be used as a command line tool. 
It can be used to generate a random profile and save it to a file. 
It can also be used to generate a random profile and print it to the console.

Usages:

.. code-block:: bash

    rp --help or random_profile -h
    Usage: rp [OPTIONS]

    rp -n 10 -p

    optional arguments:
        -h, --help      show this help message and exit
        -n N            Number of random profiles
    
        -f, --fullname  Get full name instead of first name
        -p, --profile   Get full profile instead of first name
        -l, --lastname  Get last name instead of first name
        -ip, --ipv4     Get an ipv4 IP address
        -j, --jobtitle  Get job title
    
Get Random Profile:
-------------------

.. code-block:: bash

    # n = number of random profiles, p = profile
    rp -n 10 -p

Get First Name:
---------------

.. code-block:: bash

    # n = number of random profiles, f = first name
    rp -n 10 -f 

Get Last Name:
--------------

.. code-block:: bash

    # n = number of random profiles, l = last name
    rp -n 10 -l

Get Job Title:
--------------

.. code-block:: bash

    # n = number of random profiles, j = job title
    rp -n 10 -j

Get IPv4 Address:
-----------------

.. code-block:: bash

    # n = number of random profiles, ip = ipv4
    rp -n 10 -ip

Get Random Profile and Save to File:
------------------------------------

.. code-block:: bash

    # n = number of random profiles, p = profile
    rp -n 10 -p > rps.txt

.. code-block:: bash

    # save to a file
    # n = number of random profiles, p = profile
    rp -n 10 -p >> rps.txt


Get Random Profile version:
---------------------------

.. code-block:: bash

    rp --version

    rp 0.2.3
