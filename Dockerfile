FROM python:3-onbuild
MAINTAINER Jaosn Mills <jmmills@cpan.org>
USER daemon
RUN nosetests tests/
HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1
EXPOSE 8000
CMD ["uwsgi", "--ini", "demo.ini"]
