PKG_NAME := mvn-mesos
URL = https://github.com/apache/mesos/archive/1.4.0.tar.gz
ARCHIVES = https://repo1.maven.org/maven2/org/apache/mesos/mesos/1.4.0/mesos-1.4.0.jar : https://repo1.maven.org/maven2/org/apache/mesos/mesos/1.4.0/mesos-1.4.0.pom : https://repo.maven.apache.org/maven2/org/apache/mesos/mesos/1.4.0/mesos-1.4.0-shaded-protobuf.jar : https://repo1.maven.org/maven2/org/apache/mesos/mesos/1.0.1/mesos-1.0.1.jar : https://repo1.maven.org/maven2/org/apache/mesos/mesos/1.0.1/mesos-1.0.1.pom :

include ../common/Makefile.common
