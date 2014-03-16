Jeff's bike and build site

To deploy to dreamhost:
 * login
 * go to bikeandbuild dir
 * git pull
 * source the ve
 * ./manage.py syncdb --migrate
 * ./manage.py collectstatic
 * cd ..
 * touch tmp/restart.txt

DO NOT FORGET THE RESTART!!
