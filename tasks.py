# tasks.py contains (or refers to) all tasks that the developer could want to
# run on a regular basis for this project.  As a rule everything that is in
# this tasks.py should be unique to this project, such as the url that the
# docker image of this repo will produce is placed or the protobuf complation
# process from commlib (at least until we have multiple projects that have
# protobufs that we need to compile), though even in that case, those tasks
# should be in a separate .py file in this repo to keep this file short and
# to the point
from cleargrid.build.invoke_tasks.sample.python_app import ns

ns = ns
