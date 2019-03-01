# Docker file for the freesurfer_pp plugin app

FROM fnndsc/ubuntu-python3:latest
MAINTAINER fnndsc "dev@babymri.org"

ENV APPROOT="/usr/src/freesurfer_pp"  VERSION="0.1"
COPY ["freesurfer_pp", "${APPROOT}"]
COPY ["requirements.txt", "${APPROOT}"]

WORKDIR $APPROOT

RUN pip install -r requirements.txt

CMD ["freesurfer_pp.py", "--help"]